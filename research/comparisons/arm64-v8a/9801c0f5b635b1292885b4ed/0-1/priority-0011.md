# v15.7.4 → v16.0.0 · 最優先の変更候補 (11)

[一覧の目次](README.md)

<a id="compare-4ec51e4973504e71d343b98a46a933f6"></a>

### [`004dbf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbf98.md) → [`004fee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fee30.md) _ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdccc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccc0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdcb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb00.md)
- 新版 呼出元 1件 [`00c59710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59710.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59550.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fee7c",
      "incomplete_value": true,
      "site": "004feea4",
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
      "definition_site": "004dbfe4",
      "incomplete_value": true,
      "site": "004dc00c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004fee60",
      "READ",
      [
        "storage",
        "00c1b2d8",
        null,
        "pointer"
      ]
    ],
    [
      "004feea4",
      "DATA",
      [
        "storage",
        "00bea7a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004fee60",
      "READ",
      [
        "storage",
        "00c9acc8",
        null,
        "pointer"
      ]
    ],
    [
      "004feea4",
      "DATA",
      [
        "storage",
        "00c67368",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dbfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbf98.md#insn-004dbfbc) · [`004dbfc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbf98.md#insn-004dbfc8) · [`004dc034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbf98.md#insn-004dc034)
- 新版 [`004fee54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fee30.md#insn-004fee54) · [`004fee60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fee30.md#insn-004fee60) · [`004feecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fee30.md#insn-004feecc)

~~~diff
- 004dbfbc ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004fee54 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004dbfbc bytes 093a0090
+ 004fee54 bytes e93c0090
- 004dbfc8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2d8:8"]]
- 004dbfc8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fee60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc8:8"]]
+ 004fee60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004dbfc8 bytes 296d41f9
+ 004fee60 bytes 296546f9
- 004dc034 ["INT_ADD", "register:40f0:8", ["const:4dc034:8", "const:4:8"]]
- 004dc034 ["CALL", null, ["callee:00c59550:8"]]
+ 004feecc ["INT_ADD", "register:40f0:8", ["const:4feecc:8", "const:4:8"]]
+ 004feecc ["CALL", null, ["callee:00c59550:8"]]
- 004dc034 bytes b3021c94
+ 004feecc bytes a1691d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3716391efc68eeeb64867797aafb0ca6"></a>

### [`004dc3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc3d8.md) → [`004ff270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff270.md) _ZN5Botan15AlternativeName13add_othernameERKNS_3OIDERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`004dc4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc4a4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdcb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb10.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59560.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.62% / 新版 97.62%

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
      "site": "004ff2bc",
      "value": [
        "leaf",
        "ram:c59560:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004dc424",
      "value": [
        "leaf",
        "ram:bdcb10:8"
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
      "004ff2bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcb10"
      ]
    ]
  ],
  "added": [
    [
      "004ff2bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59560"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dc424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc3d8.md#insn-004dc424) · [`004dc434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc3d8.md#insn-004dc434) · [`004dc444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc3d8.md#insn-004dc444)
- 新版 [`004ff2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff270.md#insn-004ff2bc) · [`004ff2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff270.md#insn-004ff2cc) · [`004ff2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff270.md#insn-004ff2dc)

~~~diff
- 004dc424 ["INT_ADD", "register:40f0:8", ["const:4dc424:8", "const:4:8"]]
- 004dc424 ["CALL", null, ["ram:bdcb10:8"]]
+ 004ff2bc ["INT_ADD", "register:40f0:8", ["const:4ff2bc:8", "const:4:8"]]
+ 004ff2bc ["CALL", null, ["ram:c59560:8"]]
- 004dc424 bytes bb011c94
+ 004ff2bc bytes a9681d94
- 004dc434 ["INT_ADD", "register:40f0:8", ["const:4dc434:8", "const:4:8"]]
- 004dc434 ["CALL", null, ["callee:004ff33c:8"]]
+ 004ff2cc ["INT_ADD", "register:40f0:8", ["const:4ff2cc:8", "const:4:8"]]
+ 004ff2cc ["CALL", null, ["callee:004ff33c:8"]]
- 004dc434 bytes 1c000094
+ 004ff2cc bytes 1c000094
- 004dc444 ["INT_ADD", "register:40f0:8", ["const:4dc444:8", "const:4:8"]]
- 004dc444 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004ff2dc ["INT_ADD", "register:40f0:8", ["const:4ff2dc:8", "const:4:8"]]
+ 004ff2dc ["CALL", null, ["callee:00c57ab0:8"]]
- 004dc444 bytes 07fb1b94
+ 004ff2dc bytes f5611d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64de9e7a8ec2baef3ff9390cfaeaeef2"></a>

### [`004dcbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcbd4.md) → [`004ffa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md) FUN_004ffa6c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004dc960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc960.md) · 呼出先 13件 [`004e56e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e56e4.md) [`004f1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1ecc.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`005251c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005251c0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004ff7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff7f8.md) · 呼出先 13件 [`0050857c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md) [`00514d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.66% / 新版 93.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffaf0",
      "incomplete_value": true,
      "site": "004ffaf0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004dcc58",
      "incomplete_value": true,
      "site": "004dcc58",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffaf0",
      "incomplete_value": true,
      "site": "004ffaf0",
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
      "definition_site": "004dcc58",
      "incomplete_value": true,
      "site": "004dcc58",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffae4",
      "incomplete_value": true,
      "site": "004ffaf8",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dcc4c",
      "incomplete_value": true,
      "site": "004dcc60",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
      "004ffac8",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "004ffae0",
      "READ",
      [
        "storage",
        "00c13340",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffae4",
      "READ",
      [
        "storage",
        "00c13380",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "004ffac8",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "004ffae0",
      "READ",
      [
        "storage",
        "00c92ce8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffae4",
      "READ",
      [
        "storage",
        "00c92d28",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dcd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcbd4.md#insn-004dcd38) · [`004dce60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcbd4.md#insn-004dce60) · [`004dcc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcbd4.md#insn-004dcc18)
- 新版 [`004ffbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md#insn-004ffbd0) · [`004ffcf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md#insn-004ffcf8) · [`004ffab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md#insn-004ffab0)

~~~diff
- 004dcd38 ["INT_ADD", "register:40f0:8", ["const:4dcd38:8", "const:4:8"]]
- 004dcd38 ["CALL", null, ["ram:bdcb10:8"]]
+ 004ffbd0 ["INT_ADD", "register:40f0:8", ["const:4ffbd0:8", "const:4:8"]]
+ 004ffbd0 ["CALL", null, ["ram:c59560:8"]]
- 004dcd38 bytes 76ff1b94
+ 004ffbd0 bytes 64661d94
- 004dce60 ["INT_ADD", "register:40f0:8", ["const:4dce60:8", "const:4:8"]]
- 004dce60 ["CALL", null, ["callee:00c57dc0:8"]]
+ 004ffcf8 ["INT_ADD", "register:40f0:8", ["const:4ffcf8:8", "const:4:8"]]
+ 004ffcf8 ["CALL", null, ["callee:00c57dc0:8"]]
- 004dce60 bytes 44f91b94
+ 004ffcf8 bytes 32601d94
- 004dcc18 ["INT_ADD", "register:40f0:8", ["const:4dcc18:8", "const:4:8"]]
- 004dcc18 ["CALL", null, ["callee:00548058:8"]]
+ 004ffab0 ["INT_ADD", "register:40f0:8", ["const:4ffab0:8", "const:4:8"]]
+ 004ffab0 ["CALL", null, ["callee:00548058:8"]]
- 004dcc18 bytes 6a210194
+ 004ffab0 bytes 6a210194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bf7c0992fc4e6a78c35f533324e0c0b"></a>

### [`004dcf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcf48.md) → [`004ffde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md) _ZN5Botan15AlternativeName11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`004dc4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dc4a4.md) [`004e40b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e40b8.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`004ff33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) [`00506f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.72% / 新版 95.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 11件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffe50",
      "incomplete_value": true,
      "site": "004ffe54",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004dcfb8",
      "incomplete_value": true,
      "site": "004dcfbc",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
      "definition_site": "004ffe60",
      "incomplete_value": true,
      "site": "004ffe60",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004dcfc8",
      "incomplete_value": true,
      "site": "004dcfc8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffe60",
      "incomplete_value": true,
      "site": "004ffe60",
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
      "definition_site": "004dcfc8",
      "incomplete_value": true,
      "site": "004dcfc8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ffe34",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "004ffe4c",
      "READ",
      [
        "storage",
        "00c13340",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffe50",
      "READ",
      [
        "storage",
        "00c13380",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "004ffe34",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "004ffe4c",
      "READ",
      [
        "storage",
        "00c92ce8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffe50",
      "READ",
      [
        "storage",
        "00c92d28",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dd0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcf48.md#insn-004dd0b8) · [`004dd148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcf48.md#insn-004dd148) · [`004dd2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcf48.md#insn-004dd2c0)
- 新版 [`004fff50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md#insn-004fff50) · [`004fffe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md#insn-004fffe0) · [`00500158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md#insn-00500158)

~~~diff
- 004dd0b8 ["INT_ADD", "register:40f0:8", ["const:4dd0b8:8", "const:4:8"]]
- 004dd0b8 ["CALL", null, ["ram:bdba40:8"]]
+ 004fff50 ["INT_ADD", "register:40f0:8", ["const:4fff50:8", "const:4:8"]]
+ 004fff50 ["CALL", null, ["ram:c58490:8"]]
- 004dd0b8 bytes 62fa1b94
+ 004fff50 bytes 50611d94
- 004dd148 ["INT_ADD", "register:40f0:8", ["const:4dd148:8", "const:4:8"]]
- 004dd148 ["CALL", null, ["ram:bdba40:8"]]
+ 004fffe0 ["INT_ADD", "register:40f0:8", ["const:4fffe0:8", "const:4:8"]]
+ 004fffe0 ["CALL", null, ["ram:c58490:8"]]
- 004dd148 bytes 3efa1b94
+ 004fffe0 bytes 2c611d94
- 004dd2c0 ["INT_ADD", "register:40f0:8", ["const:4dd2c0:8", "const:4:8"]]
- 004dd2c0 ["CALL", null, ["ram:bdba40:8"]]
+ 00500158 ["INT_ADD", "register:40f0:8", ["const:500158:8", "const:4:8"]]
+ 00500158 ["CALL", null, ["ram:c58490:8"]]
- 004dd2c0 bytes e0f91b94
+ 00500158 bytes ce601d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27fcd32156c198d0e7111286badd2fb3"></a>

### [`004ddc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dd/004ddc24.md) → [`00500abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500abc.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERKNS_7X509_DNE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb50.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c595a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595a0.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.51% / 新版 97.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00500dfc",
      "incomplete_value": false,
      "site": "00500e04",
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
    "old": {
      "definition_site": "004ddf64",
      "incomplete_value": false,
      "site": "004ddf6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:ab6:8"
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
      "00500d28",
      "PARAM",
      [
        "storage",
        "002a8302",
        null,
        null
      ]
    ],
    [
      "00500d7c",
      "PARAM",
      [
        "storage",
        "00296b41",
        null,
        null
      ]
    ],
    [
      "00500dac",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00500d28",
      "PARAM",
      [
        "storage",
        "002b8fa4",
        null,
        null
      ]
    ],
    [
      "00500d7c",
      "PARAM",
      [
        "storage",
        "002a6676",
        null,
        null
      ]
    ],
    [
      "00500dac",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ddf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dd/004ddc24.md#insn-004ddf6c) · [`004ddc64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dd/004ddc24.md#insn-004ddc64) · [`004ddc7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dd/004ddc24.md#insn-004ddc7c)
- 新版 [`00500e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500abc.md#insn-00500e04) · [`00500afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500abc.md#insn-00500afc) · [`00500b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500abc.md#insn-00500b14)

~~~diff
- 004ddf6c ["INT_ADD", "register:40f0:8", ["const:4ddf6c:8", "const:4:8"]]
- 004ddf6c ["CALL", null, ["callee:00459490:8"]]
+ 00500e04 ["INT_ADD", "register:40f0:8", ["const:500e04:8", "const:4:8"]]
+ 00500e04 ["CALL", null, ["callee:00459490:8"]]
- 004ddf6c bytes a361fd97
+ 00500e04 bytes a361fd97
- 004ddc64 ["INT_ADD", "register:40f0:8", ["const:4ddc64:8", "const:4:8"]]
- 004ddc64 ["CALL", null, ["callee:00c595b0:8"]]
+ 00500afc ["INT_ADD", "register:40f0:8", ["const:500afc:8", "const:4:8"]]
+ 00500afc ["CALL", null, ["callee:00c595b0:8"]]
- 004ddc64 bytes bffb1b94
+ 00500afc bytes ad621d94
- 004ddc7c ["COPY", "register:40a0:8", ["const:2a8000:8"]]
+ 00500b14 ["COPY", "register:40a0:8", ["const:2b8000:8"]]
- 004ddc7c bytes 54eefff0
+ 00500b14 bytes d4edff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97bd8617d34c50e0771a2cd05ef0fb64"></a>

### [`004de068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de068.md) → [`00500f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500f00.md) _ZN5Botan9to_stringENS_23Certificate_Status_CodeE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb70.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c595c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595c0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate, unresolved_return_alignment

命令の説明率　旧版 83.09% / 新版 83.09%

CFGの説明率　旧版 98.33% / 新版 98.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 43件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00500f54",
      "incomplete_value": false,
      "site": "00500f58",
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
            "const:9ed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004de0bc",
      "incomplete_value": false,
      "site": "004de0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:5da:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00500f90",
      "incomplete_value": false,
      "site": "00500f94",
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
            "const:d9d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004de0f8",
      "incomplete_value": false,
      "site": "004de0fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:a77:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00500fc4",
      "incomplete_value": false,
      "site": "00500fc8",
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
            "const:626:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004de12c",
      "incomplete_value": false,
      "site": "004de130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:af1:8"
          ]
        ]
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
      "00500f54",
      "DATA",
      [
        "storage",
        "0029f5da",
        null,
        "string"
      ]
    ],
    [
      "00500f90",
      "DATA",
      [
        "storage",
        "002ada77",
        null,
        "string"
      ]
    ],
    [
      "00500fc4",
      "DATA",
      [
        "storage",
        "00296af1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00500f54",
      "DATA",
      [
        "storage",
        "002af9ed",
        null,
        "string"
      ]
    ],
    [
      "00500f90",
      "DATA",
      [
        "storage",
        "002bed9d",
        null,
        "string"
      ]
    ],
    [
      "00500fc4",
      "DATA",
      [
        "storage",
        "002a6626",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004de0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de068.md#insn-004de0b8) · [`004de0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de068.md#insn-004de0bc) · [`004de0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de068.md#insn-004de0f4)
- 新版 [`00500f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500f00.md#insn-00500f50) · [`00500f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500f00.md#insn-00500f54) · [`00500f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500f00.md#insn-00500f8c)

~~~diff
- 004de0b8 ["COPY", "register:4000:8", ["const:29f000:8"]]
+ 00500f50 ["COPY", "register:4000:8", ["const:2af000:8"]]
- 004de0b8 bytes 00eeffb0
+ 00500f50 bytes 60edfff0
- 004de0bc ["COPY", "tmp:0:8", ["const:5da:8"]]
- 004de0bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004de0bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004de0bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00500f54 ["COPY", "tmp:0:8", ["const:9ed:8"]]
+ 00500f54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00500f54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00500f54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004de0bc bytes 00681791
+ 00500f54 bytes 00b42791
- 004de0f4 ["COPY", "register:4000:8", ["const:2ad000:8"]]
+ 00500f8c ["COPY", "register:4000:8", ["const:2be000:8"]]
- 004de0f4 bytes 60eefff0
+ 00500f8c bytes e0edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5193fc51c853df96e771785d89bc6fe7"></a>

### [`004de4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de4b0.md) → [`00501348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501348.md) _ZN5Botan27Certificate_Store_In_Memory15add_certificateERKNS_16X509_CertificateE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb80.md) · 呼出先 10件 [`00518128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518128.md) [`005254d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005254d0.md) [`005254e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005254e0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c595d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595d0.md) · 呼出先 10件 [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md) [`00548368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548368.md) [`00548378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

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
      "definition_site": "00501424",
      "incomplete_value": true,
      "site": "00501428",
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
      "definition_site": "004de58c",
      "incomplete_value": true,
      "site": "004de590",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00501440",
      "incomplete_value": true,
      "site": "00501448",
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
      "definition_site": "004de5a8",
      "incomplete_value": true,
      "site": "004de5b0",
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
      "0050141c",
      "READ",
      [
        "storage",
        "00c1b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "00501428",
      "DATA",
      [
        "storage",
        "00bed780",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "0050143c",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050141c",
      "READ",
      [
        "storage",
        "00c9acd8",
        null,
        "pointer"
      ]
    ],
    [
      "00501428",
      "DATA",
      [
        "storage",
        "00c6a340",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "0050143c",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004de534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de4b0.md#insn-004de534) · [`004de544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de4b0.md#insn-004de544) · [`004de564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de4b0.md#insn-004de564)
- 新版 [`005013cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501348.md#insn-005013cc) · [`005013dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501348.md#insn-005013dc) · [`005013fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501348.md#insn-005013fc)

~~~diff
- 004de534 ["INT_ADD", "register:40f0:8", ["const:4de534:8", "const:4:8"]]
- 004de534 ["CALL", null, ["callee:00c57c50:8"]]
+ 005013cc ["INT_ADD", "register:40f0:8", ["const:5013cc:8", "const:4:8"]]
+ 005013cc ["CALL", null, ["callee:00c57c50:8"]]
- 004de534 bytes 33f31b94
+ 005013cc bytes 215a1d94
- 004de544 ["INT_ADD", "register:40f0:8", ["const:4de544:8", "const:4:8"]]
- 004de544 ["CALL", null, ["callee:00c582a0:8"]]
+ 005013dc ["INT_ADD", "register:40f0:8", ["const:5013dc:8", "const:4:8"]]
+ 005013dc ["CALL", null, ["callee:00c582a0:8"]]
- 004de544 bytes c3f41b94
+ 005013dc bytes b15b1d94
- 004de564 ["INT_ADD", "register:40f0:8", ["const:4de564:8", "const:4:8"]]
- 004de564 ["CALL", null, ["callee:00c57c50:8"]]
+ 005013fc ["INT_ADD", "register:40f0:8", ["const:5013fc:8", "const:4:8"]]
+ 005013fc ["CALL", null, ["callee:00c57c50:8"]]
- 004de564 bytes 27f31b94
+ 005013fc bytes 155a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6d2240c42bc02fc66af2f86ee2c4dbb"></a>

### [`004def78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004def78.md) → [`00501e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501e10.md) _ZNK5Botan27Certificate_Store_In_Memory24find_cert_by_pubkey_sha1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

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
      "definition_site": "00502028",
      "incomplete_value": false,
      "site": "00502030",
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
            "const:ae9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004df190",
      "incomplete_value": false,
      "site": "004df198",
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
            "const:428:8"
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
      "definition_site": "00502060",
      "incomplete_value": true,
      "site": "0050206c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004df1c8",
      "incomplete_value": true,
      "site": "004df1d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050205c",
      "incomplete_value": false,
      "site": "0050206c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004df1c4",
      "incomplete_value": false,
      "site": "004df1d4",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00502028",
      "PARAM",
      [
        "storage",
        "002a2428",
        null,
        "string"
      ]
    ],
    [
      "0050205c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "00502060",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502028",
      "PARAM",
      [
        "storage",
        "002b2ae9",
        null,
        "string"
      ]
    ],
    [
      "0050205c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00502060",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004df198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004def78.md#insn-004df198) · [`004df1d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004def78.md#insn-004df1d4) · [`004defec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004def78.md#insn-004defec)
- 新版 [`00502030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501e10.md#insn-00502030) · [`0050206c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501e10.md#insn-0050206c) · [`00501e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501e10.md#insn-00501e84)

~~~diff
- 004df198 ["INT_ADD", "register:40f0:8", ["const:4df198:8", "const:4:8"]]
- 004df198 ["CALL", null, ["callee:0043dd98:8"]]
+ 00502030 ["INT_ADD", "register:40f0:8", ["const:502030:8", "const:4:8"]]
+ 00502030 ["CALL", null, ["callee:0043dd98:8"]]
- 004df198 bytes 40f0fc97
+ 00502030 bytes 5aeffc97
- 004df1d4 ["INT_ADD", "register:40f0:8", ["const:4df1d4:8", "const:4:8"]]
- 004df1d4 ["CALL", null, ["callee:00c57b10:8"]]
+ 0050206c ["INT_ADD", "register:40f0:8", ["const:50206c:8", "const:4:8"]]
+ 0050206c ["CALL", null, ["callee:00c57b10:8"]]
- 004df1d4 bytes bbef1b94
+ 0050206c bytes a9561d94
- 004defec ["INT_ADD", "register:40f0:8", ["const:4defec:8", "const:4:8"]]
- 004defec ["CALL", null, ["callee:00c589f0:8"]]
+ 00501e84 ["INT_ADD", "register:40f0:8", ["const:501e84:8", "const:4:8"]]
+ 00501e84 ["CALL", null, ["callee:00c589f0:8"]]
- 004defec bytes edf31b94
+ 00501e84 bytes db5a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df055aeb72439526f22529ce65ea70c4"></a>

### [`004df290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df290.md) → [`00502128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502128.md) _ZNK5Botan27Certificate_Store_In_Memory34find_cert_by_raw_subject_dn_sha256ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.71% / 新版 98.71%

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
      "definition_site": "00502348",
      "incomplete_value": false,
      "site": "00502350",
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
            "const:505:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004df4b0",
      "incomplete_value": false,
      "site": "004df4b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:acc:8"
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
      "definition_site": "00502380",
      "incomplete_value": true,
      "site": "0050238c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004df4e8",
      "incomplete_value": true,
      "site": "004df4f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050237c",
      "incomplete_value": false,
      "site": "0050238c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004df4e4",
      "incomplete_value": false,
      "site": "004df4f4",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00502348",
      "PARAM",
      [
        "storage",
        "00295acc",
        null,
        "string"
      ]
    ],
    [
      "0050237c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "00502380",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502348",
      "PARAM",
      [
        "storage",
        "002a5505",
        null,
        "string"
      ]
    ],
    [
      "0050237c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00502380",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004df4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df290.md#insn-004df4b8) · [`004df4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df290.md#insn-004df4f4) · [`004df30c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df290.md#insn-004df30c)
- 新版 [`00502350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502128.md#insn-00502350) · [`0050238c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502128.md#insn-0050238c) · [`005021a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502128.md#insn-005021a4)

~~~diff
- 004df4b8 ["INT_ADD", "register:40f0:8", ["const:4df4b8:8", "const:4:8"]]
- 004df4b8 ["CALL", null, ["callee:0043dd98:8"]]
+ 00502350 ["INT_ADD", "register:40f0:8", ["const:502350:8", "const:4:8"]]
+ 00502350 ["CALL", null, ["callee:0043dd98:8"]]
- 004df4b8 bytes 78effc97
+ 00502350 bytes 92eefc97
- 004df4f4 ["INT_ADD", "register:40f0:8", ["const:4df4f4:8", "const:4:8"]]
- 004df4f4 ["CALL", null, ["callee:00c57b10:8"]]
+ 0050238c ["INT_ADD", "register:40f0:8", ["const:50238c:8", "const:4:8"]]
+ 0050238c ["CALL", null, ["callee:00c57b10:8"]]
- 004df4f4 bytes f3ee1b94
+ 0050238c bytes e1551d94
- 004df30c ["INT_ADD", "register:40f0:8", ["const:4df30c:8", "const:4:8"]]
- 004df30c ["CALL", null, ["callee:00c589f0:8"]]
+ 005021a4 ["INT_ADD", "register:40f0:8", ["const:5021a4:8", "const:4:8"]]
+ 005021a4 ["CALL", null, ["callee:00c589f0:8"]]
- 004df30c bytes 25f31b94
+ 005021a4 bytes 135a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf59140de74bb3a1ff1b5d2e07eada0a"></a>

### [`004df5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df5b0.md) → [`00502448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502448.md) _ZN5Botan27Certificate_Store_In_Memory7add_crlERKNS_8X509_CRLE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00518128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518128.md) [`00525bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525bf0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md) [`00548a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a88.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

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
      "definition_site": "00502490",
      "incomplete_value": true,
      "site": "00502494",
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
      "definition_site": "004df5f8",
      "incomplete_value": true,
      "site": "004df5fc",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005024ac",
      "incomplete_value": true,
      "site": "005024b4",
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
      "definition_site": "004df614",
      "incomplete_value": true,
      "site": "004df61c",
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
      "00502488",
      "READ",
      [
        "storage",
        "00c1b2f8",
        null,
        "pointer"
      ]
    ],
    [
      "00502494",
      "DATA",
      [
        "storage",
        "00bed7d0",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005024a8",
      "READ",
      [
        "storage",
        "00c1b300",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502488",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00502494",
      "DATA",
      [
        "storage",
        "00c6a390",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005024a8",
      "READ",
      [
        "storage",
        "00c9acf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004df5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df5b0.md#insn-004df5e0) · [`004df5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df5b0.md#insn-004df5e4) · [`004df5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df5b0.md#insn-004df5f0)
- 新版 [`00502478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502448.md#insn-00502478) · [`0050247c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502448.md#insn-0050247c) · [`00502488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502448.md#insn-00502488)

~~~diff
- 004df5e0 ["INT_ADD", "register:40f0:8", ["const:4df5e0:8", "const:4:8"]]
- 004df5e0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00502478 ["INT_ADD", "register:40f0:8", ["const:502478:8", "const:4:8"]]
+ 00502478 ["CALL", null, ["callee:00c57a90:8"]]
- 004df5e0 bytes 98ee1b94
+ 00502478 bytes 86551d94
- 004df5e4 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 0050247c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004df5e4 bytes e8390090
+ 0050247c bytes c83c0090
- 004df5f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f8:8"]]
- 004df5f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502488 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce8:8"]]
+ 00502488 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004df5f0 bytes 087d41f9
+ 00502488 bytes 087546f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6d235e74379432a46eececf4432116c"></a>

### [`004df920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df920.md) → [`005027b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md) FUN_005027b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`004de868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de868.md) [`004df724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df724.md) [`0050645c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/0050645c.md) [`00506ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) [`0052581c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/0052581c.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00517bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517bcc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 5件 [`00501700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501700.md) [`005025bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005025bc.md) [`005292f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md) [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) [`005486b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0053aa64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053aa64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005027f8",
      "incomplete_value": true,
      "site": "00502800",
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
      "definition_site": "004df960",
      "incomplete_value": true,
      "site": "004df968",
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
      "005027e8",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "00502800",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005027e8",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "00502800",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004df944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df920.md#insn-004df944) · [`004df950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df920.md#insn-004df950) · [`004df990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004df920.md#insn-004df990)
- 新版 [`005027dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md#insn-005027dc) · [`005027e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md#insn-005027e8) · [`00502828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md#insn-00502828)

~~~diff
- 004df944 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005027dc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004df944 bytes e8390090
+ 005027dc bytes c83c0090
- 004df950 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 004df950 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005027e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
+ 005027e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004df950 bytes 087141f9
+ 005027e8 bytes 086946f9
- 004df990 ["INT_ADD", "register:40f0:8", ["const:4df990:8", "const:4:8"]]
- 004df990 ["CALL", null, ["callee:00c57a90:8"]]
+ 00502828 ["INT_ADD", "register:40f0:8", ["const:502828:8", "const:4:8"]]
+ 00502828 ["CALL", null, ["callee:00c57a90:8"]]
- 004df990 bytes aced1b94
+ 00502828 bytes 9a541d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-619ea026911cef0ce4875d27354daa6d"></a>

### [`004dfc64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfc64.md) → [`00502afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502afc.md) _ZN5Botan27Certificate_Store_In_MemoryC1ERKNS_16X509_CertificateE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdcb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c595d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502b20",
      "incomplete_value": true,
      "site": "00502b24",
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
      "definition_site": "004dfc88",
      "incomplete_value": true,
      "site": "004dfc8c",
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
      "00502b18",
      "READ",
      [
        "storage",
        "00c1b308",
        null,
        "pointer"
      ]
    ],
    [
      "00502b24",
      "DATA",
      [
        "storage",
        "00bea7d8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00502b18",
      "READ",
      [
        "storage",
        "00c9acf8",
        null,
        "pointer"
      ]
    ],
    [
      "00502b24",
      "DATA",
      [
        "storage",
        "00c67398",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dfc78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfc64.md#insn-004dfc78) · [`004dfc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfc64.md#insn-004dfc80) · [`004dfc84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfc64.md#insn-004dfc84)
- 新版 [`00502b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502afc.md#insn-00502b10) · [`00502b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502afc.md#insn-00502b18)

~~~diff
- 004dfc78 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00502b10 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004dfc78 bytes e8390090
+ 00502b10 bytes c83c0090
- 004dfc80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:308:8"]]
- 004dfc80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502b18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf8:8"]]
+ 00502b18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004dfc80 bytes 088541f9
+ 00502b18 bytes 087d46f9
- 004dfc84 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 004dfc84 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-137812bc1d79497d68713aea34b0d1dd"></a>

### [`004dfd64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfd64.md) → [`00502bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md) _ZN5Botan27Certificate_Store_In_MemoryC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`005254e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005254e0.md) [`00525ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525ea0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00548378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md) [`00548d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d38.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502c34",
      "incomplete_value": true,
      "site": "00502c3c",
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
      "definition_site": "004dfd9c",
      "incomplete_value": true,
      "site": "004dfda4",
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
      "00502c28",
      "READ",
      [
        "storage",
        "00c1b308",
        null,
        "pointer"
      ]
    ],
    [
      "00502c3c",
      "DATA",
      [
        "storage",
        "00bea7d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00502c84",
      "READ",
      [
        "storage",
        "00c1b310",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502c28",
      "READ",
      [
        "storage",
        "00c9acf8",
        null,
        "pointer"
      ]
    ],
    [
      "00502c3c",
      "DATA",
      [
        "storage",
        "00c67398",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00502c84",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dfd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfd64.md#insn-004dfd84) · [`004dfd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfd64.md#insn-004dfd90) · [`004dfdd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfd64.md#insn-004dfdd8)
- 新版 [`00502c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md#insn-00502c1c) · [`00502c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md#insn-00502c28) · [`00502c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md#insn-00502c70)

~~~diff
- 004dfd84 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00502c1c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004dfd84 bytes e8390090
+ 00502c1c bytes c83c0090
- 004dfd90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:308:8"]]
- 004dfd90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502c28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf8:8"]]
+ 00502c28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004dfd90 bytes 088541f9
+ 00502c28 bytes 087d46f9
- 004dfdd8 ["INT_ADD", "register:40f0:8", ["const:4dfdd8:8", "const:4:8"]]
- 004dfdd8 ["CALL", null, ["callee:00c59430:8"]]
+ 00502c70 ["INT_ADD", "register:40f0:8", ["const:502c70:8", "const:4:8"]]
+ 00502c70 ["CALL", null, ["callee:00c59430:8"]]
- 004dfdd8 bytes 02f31b94
+ 00502c70 bytes f0591d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-088dc52d8192488d34cbe8e2778a02be"></a>

### [`004e0038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0038.md) → [`00502ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ed0.md) _ZN5Botan9CRL_EntryC2ERKNS_16X509_CertificateENS_8CRL_CodeE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00525f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb730.md) [`00bdcba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcba0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502f08",
      "incomplete_value": true,
      "site": "00502f10",
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
      "definition_site": "004e0070",
      "incomplete_value": true,
      "site": "004e0078",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502f3c",
      "incomplete_value": true,
      "site": "00502f3c",
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
      "definition_site": "004e00a4",
      "incomplete_value": true,
      "site": "004e00a4",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502f60",
      "incomplete_value": true,
      "site": "00502f60",
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
      "definition_site": "004e00c8",
      "incomplete_value": true,
      "site": "004e00c8",
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
      "00502ef8",
      "READ",
      [
        "storage",
        "00c1b318",
        null,
        "pointer"
      ]
    ],
    [
      "00502f10",
      "DATA",
      [
        "storage",
        "00bea828",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00502f2c",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502ef8",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "00502f10",
      "DATA",
      [
        "storage",
        "00c673e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00502f2c",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e0054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0038.md#insn-004e0054) · [`004e0060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0038.md#insn-004e0060) · [`004e0088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0038.md#insn-004e0088)
- 新版 [`00502eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ed0.md#insn-00502eec) · [`00502ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ed0.md#insn-00502ef8) · [`00502f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ed0.md#insn-00502f20)

~~~diff
- 004e0054 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 00502eec ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004e0054 bytes c93900f0
+ 00502eec bytes c93c0090
- 004e0060 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:318:8"]]
- 004e0060 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502ef8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d08:8"]]
+ 00502ef8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e0060 bytes 298d41f9
+ 00502ef8 bytes 298546f9
- 004e0088 ["INT_ADD", "register:40f0:8", ["const:4e0088:8", "const:4:8"]]
- 004e0088 ["CALL", null, ["callee:00c57a90:8"]]
+ 00502f20 ["INT_ADD", "register:40f0:8", ["const:502f20:8", "const:4:8"]]
+ 00502f20 ["CALL", null, ["callee:00c57a90:8"]]
- 004e0088 bytes eeeb1b94
+ 00502f20 bytes dc521d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fed417110f23bd9034cec7df468ed0b8"></a>

### [`004e01ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e01ec.md) → [`00503084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md) _ZN5Botan10Extensions3addEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc30.md) · 呼出先 17件 [`004f3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3cec.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`0051a850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a850.md) [`00528a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a6c.md)
- 新版 呼出元 1件 [`00c59680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59680.md) · 呼出先 17件 [`00516b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516b84.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0053d6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d6e8.md) [`0054b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503258",
      "incomplete_value": true,
      "site": "00503258",
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
      "definition_site": "004e03c0",
      "incomplete_value": true,
      "site": "004e03c0",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050329c",
      "incomplete_value": true,
      "site": "005032a0",
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
      "definition_site": "004e0404",
      "incomplete_value": true,
      "site": "004e0408",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005031ac",
      "incomplete_value": false,
      "site": "005031b4",
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
            "const:c5c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e0314",
      "incomplete_value": false,
      "site": "004e031c",
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
            "const:6a2:8"
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
      "005031ac",
      "PARAM",
      [
        "storage",
        "002a06a2",
        null,
        "string"
      ]
    ],
    [
      "005031f8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "005031fc",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005031ac",
      "PARAM",
      [
        "storage",
        "002b0c5c",
        null,
        "string"
      ]
    ],
    [
      "005031f8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005031fc",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e031c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e01ec.md#insn-004e031c) · [`004e0370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e01ec.md#insn-004e0370) · [`004e022c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e01ec.md#insn-004e022c)
- 新版 [`005031b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md#insn-005031b4) · [`00503208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md#insn-00503208) · [`005030c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md#insn-005030c4)

~~~diff
- 004e031c ["INT_ADD", "register:40f0:8", ["const:4e031c:8", "const:4:8"]]
- 004e031c ["CALL", null, ["callee:00c57b70:8"]]
+ 005031b4 ["INT_ADD", "register:40f0:8", ["const:5031b4:8", "const:4:8"]]
+ 005031b4 ["CALL", null, ["callee:00c57b70:8"]]
- 004e031c bytes 81eb1b94
+ 005031b4 bytes 6f521d94
- 004e0370 ["INT_ADD", "register:40f0:8", ["const:4e0370:8", "const:4:8"]]
- 004e0370 ["CALL", null, ["callee:00c57b10:8"]]
+ 00503208 ["INT_ADD", "register:40f0:8", ["const:503208:8", "const:4:8"]]
+ 00503208 ["CALL", null, ["callee:00c57b10:8"]]
- 004e0370 bytes 54eb1b94
+ 00503208 bytes 42521d94
- 004e022c ["COPY", "register:0:8", ["register:4048:8"]]
- 004e022c ["INT_ADD", "register:40f0:8", ["const:4e022c:8", "const:4:8"]]
- 004e022c ["CALLIND", null, ["register:0:8"]]
+ 005030c4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005030c4 ["INT_ADD", "register:40f0:8", ["const:5030c4:8", "const:4:8"]]
+ 005030c4 ["CALLIND", null, ["register:0:8"]]
- 004e022c bytes 20013fd6
+ 005030c4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb35688d8e8982c6ba8d20d8250354fd"></a>

### [`004e0894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0894.md) → [`0050372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md) _ZN5Botan9CRL_Entry11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc60.md) · 呼出先 16件 [`0048bb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bb9c.md) [`004e0c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0c08.md) [`004f4778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4778.md) [`00525efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525efc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c596b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596b0.md) · 呼出先 16件 [`004aea34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aea34.md) [`00503aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503aa0.md) [`00517610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517610.md) [`00548d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d94.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.94% / 新版 94.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503780",
      "incomplete_value": true,
      "site": "00503780",
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
      "definition_site": "004e08e8",
      "incomplete_value": true,
      "site": "004e08e8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005037a4",
      "incomplete_value": true,
      "site": "005037a4",
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
      "definition_site": "004e090c",
      "incomplete_value": true,
      "site": "004e090c",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050388c",
      "incomplete_value": true,
      "site": "0050388c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:498:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e09f4",
      "incomplete_value": true,
      "site": "004e09f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:963:8"
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
      "00503770",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "00503780",
      "DATA",
      [
        "storage",
        "00be93b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00503790",
      "READ",
      [
        "storage",
        "00c1b320",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00503770",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ],
    [
      "00503780",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00503790",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e0ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0894.md#insn-004e0ae8) · [`004e0b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0894.md#insn-004e0b28) · [`004e08d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0894.md#insn-004e08d0)
- 新版 [`00503980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md#insn-00503980) · [`005039c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md#insn-005039c0) · [`00503768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md#insn-00503768)

~~~diff
- 004e0ae8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e0ae8 ["INT_ADD", "register:40f0:8", ["const:4e0ae8:8", "const:4:8"]]
- 004e0ae8 ["CALLIND", null, ["register:0:8"]]
+ 00503980 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00503980 ["INT_ADD", "register:40f0:8", ["const:503980:8", "const:4:8"]]
+ 00503980 ["CALLIND", null, ["register:0:8"]]
- 004e0ae8 bytes 20013fd6
+ 00503980 bytes 20013fd6
- 004e0b28 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e0b28 ["INT_ADD", "register:40f0:8", ["const:4e0b28:8", "const:4:8"]]
- 004e0b28 ["CALLIND", null, ["register:0:8"]]
+ 005039c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005039c0 ["INT_ADD", "register:40f0:8", ["const:5039c0:8", "const:4:8"]]
+ 005039c0 ["CALLIND", null, ["register:0:8"]]
- 004e0b28 bytes 20013fd6
+ 005039c0 bytes 20013fd6
- 004e08d0 ["INT_ADD", "register:40f0:8", ["const:4e08d0:8", "const:4:8"]]
- 004e08d0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00503768 ["INT_ADD", "register:40f0:8", ["const:503768:8", "const:4:8"]]
+ 00503768 ["CALL", null, ["callee:00c57a90:8"]]
- 004e08d0 bytes dce91b94
+ 00503768 bytes ca501d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85a668cb70eb3ed969c7d9dd16bbacfd"></a>

### [`004e0c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0c08.md) → [`00503aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503aa0.md) FUN_00503aa0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e0894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0894.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`0050372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00503adc",
      "incomplete_value": true,
      "site": "00503adc",
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
      "definition_site": "004e0c44",
      "incomplete_value": true,
      "site": "004e0c44",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00503b18",
      "incomplete_value": false,
      "site": "00503b20",
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
            "const:243:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e0c80",
      "incomplete_value": false,
      "site": "004e0c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:92d:8"
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
      "definition_site": "00503b54",
      "incomplete_value": true,
      "site": "00503b60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e0cbc",
      "incomplete_value": true,
      "site": "004e0cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f98:8"
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
      "00503acc",
      "READ",
      [
        "storage",
        "00c1b328",
        null,
        "pointer"
      ]
    ],
    [
      "00503b18",
      "PARAM",
      [
        "storage",
        "0029492d",
        null,
        "string"
      ]
    ],
    [
      "00503b50",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00503acc",
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      "00503b18",
      "PARAM",
      [
        "storage",
        "002a4243",
        null,
        "string"
      ]
    ],
    [
      "00503b50",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e0c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0c08.md#insn-004e0c88) · [`004e0cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0c08.md#insn-004e0cc8) · [`004e0c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0c08.md#insn-004e0c28)
- 新版 [`00503b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503aa0.md#insn-00503b20) · [`00503b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503aa0.md#insn-00503b60) · [`00503ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503aa0.md#insn-00503ac0)

~~~diff
- 004e0c88 ["INT_ADD", "register:40f0:8", ["const:4e0c88:8", "const:4:8"]]
- 004e0c88 ["CALL", null, ["callee:0043dd98:8"]]
+ 00503b20 ["INT_ADD", "register:40f0:8", ["const:503b20:8", "const:4:8"]]
+ 00503b20 ["CALL", null, ["callee:0043dd98:8"]]
- 004e0c88 bytes 84e9fc97
+ 00503b20 bytes 9ee8fc97
- 004e0cc8 ["INT_ADD", "register:40f0:8", ["const:4e0cc8:8", "const:4:8"]]
- 004e0cc8 ["CALL", null, ["callee:00c57b10:8"]]
+ 00503b60 ["INT_ADD", "register:40f0:8", ["const:503b60:8", "const:4:8"]]
+ 00503b60 ["CALL", null, ["callee:00c57b10:8"]]
- 004e0cc8 bytes fee81b94
+ 00503b60 bytes ec4f1d94
- 004e0c28 ["INT_ADD", "register:40f0:8", ["const:4e0c28:8", "const:4:8"]]
- 004e0c28 ["CALL", null, ["callee:00c596c0:8"]]
+ 00503ac0 ["INT_ADD", "register:40f0:8", ["const:503ac0:8", "const:4:8"]]
+ 00503ac0 ["CALL", null, ["callee:00c596c0:8"]]
- 004e0c28 bytes 12f01b94
+ 00503ac0 bytes 00571d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f79709596add4ab881e02836563d051f"></a>

### [`004e0d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0d1c.md) → [`00503bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503bb4.md) FUN_00503bb4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "00503bec",
      "incomplete_value": true,
      "site": "00503bec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:498:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e0d54",
      "incomplete_value": true,
      "site": "004e0d54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:963:8"
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
      "00503bdc",
      "READ",
      [
        "storage",
        "00296963",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00503bdc",
      "READ",
      [
        "storage",
        "002a6498",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e0d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0d1c.md#insn-004e0d34) · [`004e0d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0d1c.md#insn-004e0d38) · [`004e0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0d1c.md#insn-004e0d60)
- 新版 [`00503bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503bb4.md#insn-00503bcc) · [`00503bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503bb4.md#insn-00503bd0) · [`00503bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503bb4.md#insn-00503bf8)

~~~diff
- 004e0d34 ["COPY", "register:4048:8", ["const:296000:8"]]
+ 00503bcc ["COPY", "register:4048:8", ["const:2a6000:8"]]
- 004e0d34 bytes a9edffd0
+ 00503bcc bytes 09edfff0
- 004e0d38 ["COPY", "tmp:0:8", ["const:963:8"]]
- 004e0d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e0d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e0d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00503bd0 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 00503bd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00503bd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00503bd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e0d38 bytes 298d2591
+ 00503bd0 bytes 29611291
- 004e0d60 ["INT_ADD", "register:40f0:8", ["const:4e0d60:8", "const:4:8"]]
- 004e0d60 ["CALL", null, ["callee:00c58290:8"]]
+ 00503bf8 ["INT_ADD", "register:40f0:8", ["const:503bf8:8", "const:4:8"]]
+ 00503bf8 ["CALL", null, ["callee:00c58290:8"]]
- 004e0d60 bytes b8ea1b94
+ 00503bf8 bytes a6511d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68ba98a1a41aa3a16f44305952362340"></a>

### [`004e0dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0dc4.md) → [`00503c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503c5c.md) _ZNK5Botan9CRL_Entry4dataEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc50.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c596a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596a0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "definition_site": "00503cbc",
      "incomplete_value": false,
      "site": "00503cc4",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e0e24",
      "incomplete_value": false,
      "site": "004e0e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:ae7:8"
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
      "definition_site": "00503cf8",
      "incomplete_value": true,
      "site": "00503d04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e0e60",
      "incomplete_value": true,
      "site": "004e0e6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f58:8"
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
      "definition_site": "00503cf4",
      "incomplete_value": false,
      "site": "00503d04",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004e0e5c",
      "incomplete_value": false,
      "site": "004e0e6c",
      "value": [
        "leaf",
        "const:512990:8"
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
      "00503cbc",
      "PARAM",
      [
        "storage",
        "00291ae7",
        null,
        "string"
      ]
    ],
    [
      "00503cf4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "00503cf8",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00503cbc",
      "PARAM",
      [
        "storage",
        "002a1100",
        null,
        "string"
      ]
    ],
    [
      "00503cf4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00503cf8",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e0e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0dc4.md#insn-004e0e2c) · [`004e0e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0dc4.md#insn-004e0e6c) · [`004e0e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0dc4.md#insn-004e0e18)
- 新版 [`00503cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503c5c.md#insn-00503cc4) · [`00503d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503c5c.md#insn-00503d04) · [`00503cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503c5c.md#insn-00503cb0)

~~~diff
- 004e0e2c ["INT_ADD", "register:40f0:8", ["const:4e0e2c:8", "const:4:8"]]
- 004e0e2c ["CALL", null, ["callee:0043dd98:8"]]
+ 00503cc4 ["INT_ADD", "register:40f0:8", ["const:503cc4:8", "const:4:8"]]
+ 00503cc4 ["CALL", null, ["callee:0043dd98:8"]]
- 004e0e2c bytes 1be9fc97
+ 00503cc4 bytes 35e8fc97
- 004e0e6c ["INT_ADD", "register:40f0:8", ["const:4e0e6c:8", "const:4:8"]]
- 004e0e6c ["CALL", null, ["callee:00c57b10:8"]]
+ 00503d04 ["INT_ADD", "register:40f0:8", ["const:503d04:8", "const:4:8"]]
+ 00503d04 ["CALL", null, ["callee:00c57b10:8"]]
- 004e0e6c bytes 95e81b94
+ 00503d04 bytes 834f1d94
- 004e0e18 ["INT_ADD", "register:40f0:8", ["const:4e0e18:8", "const:4:8"]]
- 004e0e18 ["CALL", null, ["callee:00c57af0:8"]]
+ 00503cb0 ["INT_ADD", "register:40f0:8", ["const:503cb0:8", "const:4:8"]]
+ 00503cb0 ["CALL", null, ["callee:00c57af0:8"]]
- 004e0e18 bytes a2e81b94
+ 00503cb0 bytes 904f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39fa06813d0de252e9e38fe5cb0cfa00"></a>

### [`004e13e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e13e0.md) → [`00504278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504278.md) _ZNK5Botan10Data_Store4get1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
      "definition_site": "00504378",
      "incomplete_value": false,
      "site": "00504384",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e14e0",
      "incomplete_value": false,
      "site": "004e14ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:85a:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005043b4",
      "incomplete_value": true,
      "site": "005043c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e151c",
      "incomplete_value": true,
      "site": "004e1528",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f58:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005043b0",
      "incomplete_value": false,
      "site": "005043c0",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004e1518",
      "incomplete_value": false,
      "site": "004e1528",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00504378",
      "PARAM",
      [
        "storage",
        "0029485a",
        null,
        "string"
      ]
    ],
    [
      "005043b0",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "005043b4",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00504378",
      "PARAM",
      [
        "storage",
        "002a4170",
        null,
        "string"
      ]
    ],
    [
      "005043b0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005043b4",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e14ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e13e0.md#insn-004e14ec) · [`004e1528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e13e0.md#insn-004e1528) · [`004e154c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e13e0.md#insn-004e154c)
- 新版 [`00504384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504278.md#insn-00504384) · [`005043c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504278.md#insn-005043c0) · [`005043e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504278.md#insn-005043e4)

~~~diff
- 004e14ec ["INT_ADD", "register:40f0:8", ["const:4e14ec:8", "const:4:8"]]
- 004e14ec ["CALL", null, ["callee:00c57cb0:8"]]
+ 00504384 ["INT_ADD", "register:40f0:8", ["const:504384:8", "const:4:8"]]
+ 00504384 ["CALL", null, ["callee:00c57cb0:8"]]
- 004e14ec bytes 5de71b94
+ 00504384 bytes 4b4e1d94
- 004e1528 ["INT_ADD", "register:40f0:8", ["const:4e1528:8", "const:4:8"]]
- 004e1528 ["CALL", null, ["callee:00c57b10:8"]]
+ 005043c0 ["INT_ADD", "register:40f0:8", ["const:5043c0:8", "const:4:8"]]
+ 005043c0 ["CALL", null, ["callee:00c57b10:8"]]
- 004e1528 bytes e6e61b94
+ 005043c0 bytes d44d1d94
- 004e154c ["INT_ADD", "register:40f0:8", ["const:4e154c:8", "const:4:8"]]
- 004e154c ["CALL", null, ["callee:00c57cb0:8"]]
+ 005043e4 ["INT_ADD", "register:40f0:8", ["const:5043e4:8", "const:4:8"]]
+ 005043e4 ["CALL", null, ["callee:00c57cb0:8"]]
- 004e154c bytes 45e71b94
+ 005043e4 bytes 334e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b29d229670bcdf7743d3d19367d8b599"></a>

### [`004e15f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e15f0.md) → [`00504488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504488.md) _ZNK5Botan10Data_Store4get1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

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
      "definition_site": "00504598",
      "incomplete_value": false,
      "site": "005045a4",
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
            "const:7d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1700",
      "incomplete_value": false,
      "site": "004e170c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:b7a:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005045d4",
      "incomplete_value": true,
      "site": "005045e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e173c",
      "incomplete_value": true,
      "site": "004e1748",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f58:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005045d0",
      "incomplete_value": false,
      "site": "005045e0",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004e1738",
      "incomplete_value": false,
      "site": "004e1748",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00504598",
      "PARAM",
      [
        "storage",
        "00297b7a",
        null,
        "string"
      ]
    ],
    [
      "005045d0",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "005045d4",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00504598",
      "PARAM",
      [
        "storage",
        "002a77d3",
        null,
        "string"
      ]
    ],
    [
      "005045d0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005045d4",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e170c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e15f0.md#insn-004e170c) · [`004e1748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e15f0.md#insn-004e1748) · [`004e1620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e15f0.md#insn-004e1620)
- 新版 [`005045a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504488.md#insn-005045a4) · [`005045e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504488.md#insn-005045e0) · [`005044b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504488.md#insn-005044b8)

~~~diff
- 004e170c ["INT_ADD", "register:40f0:8", ["const:4e170c:8", "const:4:8"]]
- 004e170c ["CALL", null, ["callee:00c57cb0:8"]]
+ 005045a4 ["INT_ADD", "register:40f0:8", ["const:5045a4:8", "const:4:8"]]
+ 005045a4 ["CALL", null, ["callee:00c57cb0:8"]]
- 004e170c bytes d5e61b94
+ 005045a4 bytes c34d1d94
- 004e1748 ["INT_ADD", "register:40f0:8", ["const:4e1748:8", "const:4:8"]]
- 004e1748 ["CALL", null, ["callee:00c57b10:8"]]
+ 005045e0 ["INT_ADD", "register:40f0:8", ["const:5045e0:8", "const:4:8"]]
+ 005045e0 ["CALL", null, ["callee:00c57b10:8"]]
- 004e1748 bytes 5ee61b94
+ 005045e0 bytes 4c4d1d94
- 004e1620 ["INT_ADD", "register:40f0:8", ["const:4e1620:8", "const:4:8"]]
- 004e1620 ["CALL", null, ["callee:00c596e0:8"]]
+ 005044b8 ["INT_ADD", "register:40f0:8", ["const:5044b8:8", "const:4:8"]]
+ 005044b8 ["CALL", null, ["callee:00c596e0:8"]]
- 004e1620 bytes 9ced1b94
+ 005044b8 bytes 8a541d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09938052350fff076904107f8bf9885b"></a>

### [`004e17a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e17a8.md) → [`00504640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504640.md) _ZNK5Botan10Data_Store11get1_memvecERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

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
      "definition_site": "0050474c",
      "incomplete_value": false,
      "site": "00504758",
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
            "const:df5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e18b4",
      "incomplete_value": false,
      "site": "004e18c0",
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
            "const:911:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504788",
      "incomplete_value": true,
      "site": "00504794",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e18f0",
      "incomplete_value": true,
      "site": "004e18fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f58:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504784",
      "incomplete_value": false,
      "site": "00504794",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004e18ec",
      "incomplete_value": false,
      "site": "004e18fc",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050474c",
      "PARAM",
      [
        "storage",
        "002ae911",
        null,
        "string"
      ]
    ],
    [
      "00504784",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "00504788",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050474c",
      "PARAM",
      [
        "storage",
        "002bfdf5",
        null,
        "string"
      ]
    ],
    [
      "00504784",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00504788",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e18c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e17a8.md#insn-004e18c0) · [`004e18fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e17a8.md#insn-004e18fc) · [`004e17d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e17a8.md#insn-004e17d4)
- 新版 [`00504758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504640.md#insn-00504758) · [`00504794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504640.md#insn-00504794) · [`0050466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504640.md#insn-0050466c)

~~~diff
- 004e18c0 ["INT_ADD", "register:40f0:8", ["const:4e18c0:8", "const:4:8"]]
- 004e18c0 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00504758 ["INT_ADD", "register:40f0:8", ["const:504758:8", "const:4:8"]]
+ 00504758 ["CALL", null, ["callee:00c57cb0:8"]]
- 004e18c0 bytes 68e61b94
+ 00504758 bytes 564d1d94
- 004e18fc ["INT_ADD", "register:40f0:8", ["const:4e18fc:8", "const:4:8"]]
- 004e18fc ["CALL", null, ["callee:00c57b10:8"]]
+ 00504794 ["INT_ADD", "register:40f0:8", ["const:504794:8", "const:4:8"]]
+ 00504794 ["CALL", null, ["callee:00c57b10:8"]]
- 004e18fc bytes f1e51b94
+ 00504794 bytes df4c1d94
- 004e17d4 ["INT_ADD", "register:40f0:8", ["const:4e17d4:8", "const:4:8"]]
- 004e17d4 ["CALL", null, ["callee:00c596e0:8"]]
+ 0050466c ["INT_ADD", "register:40f0:8", ["const:50466c:8", "const:4:8"]]
+ 0050466c ["CALL", null, ["callee:00c596e0:8"]]
- 004e17d4 bytes 2fed1b94
+ 0050466c bytes 1d541d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11620250330828c1e59fcdaec16b0bd8"></a>

### [`004e195c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e195c.md) → [`005047f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/005047f4.md) _ZNK5Botan10Data_Store11get1_uint32ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

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
      "definition_site": "005048dc",
      "incomplete_value": false,
      "site": "005048e8",
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
            "const:552:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1a44",
      "incomplete_value": false,
      "site": "004e1a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:b19:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504918",
      "incomplete_value": true,
      "site": "00504924",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e1a80",
      "incomplete_value": true,
      "site": "004e1a8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f58:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504914",
      "incomplete_value": false,
      "site": "00504924",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004e1a7c",
      "incomplete_value": false,
      "site": "004e1a8c",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005048dc",
      "PARAM",
      [
        "storage",
        "00295b19",
        null,
        "string"
      ]
    ],
    [
      "00504914",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "00504918",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005048dc",
      "PARAM",
      [
        "storage",
        "002a5552",
        null,
        "string"
      ]
    ],
    [
      "00504914",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00504918",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e1a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e195c.md#insn-004e1a50) · [`004e1a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e195c.md#insn-004e1a8c) · [`004e1988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e195c.md#insn-004e1988)
- 新版 [`005048e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/005047f4.md#insn-005048e8) · [`00504924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/005047f4.md#insn-00504924) · [`00504820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/005047f4.md#insn-00504820)

~~~diff
- 004e1a50 ["INT_ADD", "register:40f0:8", ["const:4e1a50:8", "const:4:8"]]
- 004e1a50 ["CALL", null, ["callee:00c57cb0:8"]]
+ 005048e8 ["INT_ADD", "register:40f0:8", ["const:5048e8:8", "const:4:8"]]
+ 005048e8 ["CALL", null, ["callee:00c57cb0:8"]]
- 004e1a50 bytes 04e61b94
+ 005048e8 bytes f24c1d94
- 004e1a8c ["INT_ADD", "register:40f0:8", ["const:4e1a8c:8", "const:4:8"]]
- 004e1a8c ["CALL", null, ["callee:00c57b10:8"]]
+ 00504924 ["INT_ADD", "register:40f0:8", ["const:504924:8", "const:4:8"]]
+ 00504924 ["CALL", null, ["callee:00c57b10:8"]]
- 004e1a8c bytes 8de51b94
+ 00504924 bytes 7b4c1d94
- 004e1988 ["INT_ADD", "register:40f0:8", ["const:4e1988:8", "const:4:8"]]
- 004e1988 ["CALL", null, ["callee:00c596e0:8"]]
+ 00504820 ["INT_ADD", "register:40f0:8", ["const:504820:8", "const:4:8"]]
+ 00504820 ["CALL", null, ["callee:00c596e0:8"]]
- 004e1988 bytes c2ec1b94
+ 00504820 bytes b0531d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63fdf1dfa89c14b4131576511398ca0d"></a>

### [`004e1f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1f38.md) → [`00504dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504dd0.md) _ZN5Botan9create_dnERKNS_10Data_StoreE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00526374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526374.md) [`00526378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526378.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0054920c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/0054920c.md) [`00549210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549210.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00504df0",
      "incomplete_value": false,
      "site": "00504e00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e1f58",
      "incomplete_value": false,
      "site": "004e1f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "definition_site": "00504e6c",
      "incomplete_value": true,
      "site": "00504e6c",
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
      "definition_site": "004e1fd4",
      "incomplete_value": true,
      "site": "004e1fd4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00504e00",
      "DATA",
      [
        "storage",
        "00bed8c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00504e38",
      "READ",
      [
        "storage",
        "00bed8e0",
        null,
        "pointer"
      ]
    ],
    [
      "00504e38",
      "READ",
      [
        "storage",
        "00bed8e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00504e00",
      "DATA",
      [
        "storage",
        "00c6a480",
        null,
        "undefined *"
      ]
    ],
    [
      "00504e38",
      "READ",
      [
        "storage",
        "00c6a4a0",
        null,
        "pointer"
      ]
    ],
    [
      "00504e38",
      "READ",
      [
        "storage",
        "00c6a4a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e1f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1f38.md#insn-004e1f54) · [`004e1f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1f38.md#insn-004e1f58) · [`004e1f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1f38.md#insn-004e1f78)
- 新版 [`00504dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504dd0.md#insn-00504dec) · [`00504df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504dd0.md#insn-00504df0) · [`00504e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504dd0.md#insn-00504e10)

~~~diff
- 004e1f54 ["COPY", "register:4048:8", ["const:bed000:8"]]
+ 00504dec ["COPY", "register:4048:8", ["const:c6a000:8"]]
- 004e1f54 bytes 69380090
+ 00504dec bytes 293b00d0
- 004e1f58 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 004e1f58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e1f58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e1f58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00504df0 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00504df0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00504df0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00504df0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e1f58 bytes 29012391
+ 00504df0 bytes 29011291
- 004e1f78 ["INT_ADD", "register:40f0:8", ["const:4e1f78:8", "const:4:8"]]
- 004e1f78 ["CALL", null, ["callee:00c596d0:8"]]
+ 00504e10 ["INT_ADD", "register:40f0:8", ["const:504e10:8", "const:4:8"]]
+ 00504e10 ["CALL", null, ["callee:00c596d0:8"]]
- 004e1f78 bytes 42eb1b94
+ 00504e10 bytes 30521d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5bee24f23cc314c20e096d3589c585a"></a>

### [`004e21a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e21a8.md) → [`00505040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505040.md) _ZN5Botan15create_alt_nameERKNS_10Data_StoreE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0052647c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/0052647c.md) [`00526480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526480.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00549314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549314.md) [`00549318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549318.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00505070",
      "incomplete_value": false,
      "site": "00505070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e21d8",
      "incomplete_value": false,
      "site": "004e21d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "00505070",
      "DATA",
      [
        "storage",
        "00bed950",
        null,
        "undefined *"
      ]
    ],
    [
      "005050a8",
      "READ",
      [
        "storage",
        "00bed970",
        null,
        "pointer"
      ]
    ],
    [
      "005050a8",
      "READ",
      [
        "storage",
        "00bed978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00505070",
      "DATA",
      [
        "storage",
        "00c6a510",
        null,
        "undefined *"
      ]
    ],
    [
      "005050a8",
      "READ",
      [
        "storage",
        "00c6a530",
        null,
        "pointer"
      ]
    ],
    [
      "005050a8",
      "READ",
      [
        "storage",
        "00c6a538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e21c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e21a8.md#insn-004e21c4) · [`004e21c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e21a8.md#insn-004e21c8) · [`004e21e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e21a8.md#insn-004e21e8)
- 新版 [`0050505c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505040.md#insn-0050505c) · [`00505060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505040.md#insn-00505060) · [`00505080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505040.md#insn-00505080)

~~~diff
- 004e21c4 ["COPY", "register:4048:8", ["const:bed000:8"]]
+ 0050505c ["COPY", "register:4048:8", ["const:c6a000:8"]]
- 004e21c4 bytes 493800f0
+ 0050505c bytes 293b00b0
- 004e21c8 ["COPY", "tmp:0:8", ["const:950:8"]]
- 004e21c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e21c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e21c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00505060 ["COPY", "tmp:0:8", ["const:510:8"]]
+ 00505060 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00505060 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00505060 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e21c8 bytes 29412591
+ 00505060 bytes 29411491
- 004e21e8 ["INT_ADD", "register:40f0:8", ["const:4e21e8:8", "const:4:8"]]
- 004e21e8 ["CALL", null, ["callee:00c596d0:8"]]
+ 00505080 ["INT_ADD", "register:40f0:8", ["const:505080:8", "const:4:8"]]
+ 00505080 ["CALL", null, ["callee:00c596d0:8"]]
- 004e21e8 bytes a6ea1b94
+ 00505080 bytes 94511d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b47de796b0b4e424d7a40e256c691ec2"></a>

### [`004e242c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e242c.md) → [`005052c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/005052c4.md) _ZN5Botan25key_constraints_to_stringENS_15Key_ConstraintsE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdccd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccd0.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c59720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59720.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.80% / 新版 88.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 33件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00505330",
      "incomplete_value": true,
      "site": "00505330",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e2498",
      "incomplete_value": true,
      "site": "004e2498",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:ba5:8"
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
      "definition_site": "00505334",
      "incomplete_value": true,
      "site": "00505334",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004e249c",
      "incomplete_value": true,
      "site": "004e249c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00505368",
      "incomplete_value": true,
      "site": "00505368",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e24d0",
      "incomplete_value": true,
      "site": "004e24d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:46b:8"
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
      "00505320",
      "READ",
      [
        "storage",
        "00297ba5",
        null,
        "string"
      ]
    ],
    [
      "00505324",
      "READ",
      [
        "storage",
        "00297bab",
        null,
        "string"
      ]
    ],
    [
      "00505350",
      "READ",
      [
        "storage",
        "002a246b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00505320",
      "READ",
      [
        "storage",
        "002a77fe",
        null,
        "string"
      ]
    ],
    [
      "00505324",
      "READ",
      [
        "storage",
        "002a7804",
        null,
        "string"
      ]
    ],
    [
      "00505350",
      "READ",
      [
        "storage",
        "002b2b2c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e247c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e242c.md#insn-004e247c) · [`004e2480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e242c.md#insn-004e2480) · [`004e24a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e2/004e242c.md#insn-004e24a8)
- 新版 [`00505314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/005052c4.md#insn-00505314) · [`00505318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/005052c4.md#insn-00505318) · [`00505340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/005052c4.md#insn-00505340)

~~~diff
- 004e247c ["COPY", "register:4048:8", ["const:297000:8"]]
+ 00505314 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 004e247c bytes a9edffb0
+ 00505314 bytes 09edffd0
- 004e2480 ["COPY", "tmp:0:8", ["const:ba5:8"]]
- 004e2480 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004e2480 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004e2480 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00505318 ["COPY", "tmp:0:8", ["const:7fe:8"]]
+ 00505318 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00505318 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00505318 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004e2480 bytes 29952e91
+ 00505318 bytes 29f91f91
- 004e24a8 ["INT_ADD", "register:40f0:8", ["const:4e24a8:8", "const:4:8"]]
- 004e24a8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00505340 ["INT_ADD", "register:40f0:8", ["const:505340:8", "const:4:8"]]
+ 00505340 ["CALL", null, ["callee:00c57a90:8"]]
- 004e24a8 bytes e6e21b94
+ 00505340 bytes d4491d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90e3f657acf92f15014b66dee3dd7ffd"></a>

### [`004e3024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3024.md) → [`00505ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505ebc.md) _ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcce0.md) · 呼出先 10件 [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c59730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59730.md) · 呼出先 10件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.58% / 新版 98.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00506174",
      "incomplete_value": false,
      "site": "00506180",
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
            "const:89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e32dc",
      "incomplete_value": false,
      "site": "004e32e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:b47:8"
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
      "definition_site": "00506188",
      "incomplete_value": false,
      "site": "00506190",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e32f0",
      "incomplete_value": false,
      "site": "004e32f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:b33:8"
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
      "definition_site": "005061f8",
      "incomplete_value": true,
      "site": "00506204",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e3360",
      "incomplete_value": true,
      "site": "004e336c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f98:8"
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
      "00506174",
      "PARAM",
      [
        "storage",
        "00290b47",
        null,
        "string"
      ]
    ],
    [
      "00506188",
      "PARAM",
      [
        "storage",
        "00296b33",
        null,
        "string"
      ]
    ],
    [
      "005061f4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00506174",
      "PARAM",
      [
        "storage",
        "002a0089",
        null,
        "string"
      ]
    ],
    [
      "00506188",
      "PARAM",
      [
        "storage",
        "002a6668",
        null,
        "string"
      ]
    ],
    [
      "005061f4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e32e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3024.md#insn-004e32e8) · [`004e32f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3024.md#insn-004e32f8) · [`004e336c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3024.md#insn-004e336c)
- 新版 [`00506180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505ebc.md#insn-00506180) · [`00506190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505ebc.md#insn-00506190) · [`00506204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505ebc.md#insn-00506204)

~~~diff
- 004e32e8 ["INT_ADD", "register:40f0:8", ["const:4e32e8:8", "const:4:8"]]
- 004e32e8 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00506180 ["INT_ADD", "register:40f0:8", ["const:506180:8", "const:4:8"]]
+ 00506180 ["CALL", null, ["callee:00c57cb0:8"]]
- 004e32e8 bytes dedf1b94
+ 00506180 bytes cc461d94
- 004e32f8 ["INT_ADD", "register:40f0:8", ["const:4e32f8:8", "const:4:8"]]
- 004e32f8 ["CALL", null, ["callee:00c57b70:8"]]
+ 00506190 ["INT_ADD", "register:40f0:8", ["const:506190:8", "const:4:8"]]
+ 00506190 ["CALL", null, ["callee:00c57b70:8"]]
- 004e32f8 bytes 8adf1b94
+ 00506190 bytes 78461d94
- 004e336c ["INT_ADD", "register:40f0:8", ["const:4e336c:8", "const:4:8"]]
- 004e336c ["CALL", null, ["callee:00c57b10:8"]]
+ 00506204 ["INT_ADD", "register:40f0:8", ["const:506204:8", "const:4:8"]]
+ 00506204 ["CALL", null, ["callee:00c57b10:8"]]
- 004e336c bytes 55df1b94
+ 00506204 bytes 43461d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5fa05b28d06f3df6a675c9e98f61a54"></a>

### [`004e3458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3458.md) → [`005062f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005062f0.md) _ZN5Botan11GeneralNameC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd30.md) · 呼出先 12件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c59780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59780.md) · 呼出先 12件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00506334",
      "incomplete_value": true,
      "site": "0050633c",
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
      "definition_site": "004e349c",
      "incomplete_value": true,
      "site": "004e34a4",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00506518",
      "incomplete_value": false,
      "site": "00506520",
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
            "const:cfb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e3680",
      "incomplete_value": false,
      "site": "004e3688",
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
            "const:6af:8"
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
      "definition_site": "00506550",
      "incomplete_value": true,
      "site": "0050655c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e36b8",
      "incomplete_value": true,
      "site": "004e36c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
      "0050631c",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ],
    [
      "0050633c",
      "DATA",
      [
        "storage",
        "00beb110",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506518",
      "PARAM",
      [
        "storage",
        "002a16af",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050631c",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      "0050633c",
      "DATA",
      [
        "storage",
        "00c67cd0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506518",
      "PARAM",
      [
        "storage",
        "002b1cfb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e3688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3458.md#insn-004e3688) · [`004e36c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3458.md#insn-004e36c4) · [`004e3478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3458.md#insn-004e3478)
- 新版 [`00506520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005062f0.md#insn-00506520) · [`0050655c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005062f0.md#insn-0050655c) · [`00506310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005062f0.md#insn-00506310)

~~~diff
- 004e3688 ["INT_ADD", "register:40f0:8", ["const:4e3688:8", "const:4:8"]]
- 004e3688 ["CALL", null, ["callee:0043dd98:8"]]
+ 00506520 ["INT_ADD", "register:40f0:8", ["const:506520:8", "const:4:8"]]
+ 00506520 ["CALL", null, ["callee:0043dd98:8"]]
- 004e3688 bytes 04dffc97
+ 00506520 bytes 1edefc97
- 004e36c4 ["INT_ADD", "register:40f0:8", ["const:4e36c4:8", "const:4:8"]]
- 004e36c4 ["CALL", null, ["callee:00c57b10:8"]]
+ 0050655c ["INT_ADD", "register:40f0:8", ["const:50655c:8", "const:4:8"]]
+ 0050655c ["CALL", null, ["callee:00c57b10:8"]]
- 004e36c4 bytes 7fde1b94
+ 0050655c bytes 6d451d94
- 004e3478 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00506310 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004e3478 bytes c8390090
+ 00506310 bytes a83c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cf1b913e7cc66a508d7b17f11a2eabb"></a>

### [`004e3770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3770.md) → [`00506608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506608.md) _ZNK5Botan11GeneralName11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc690.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c590e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590e0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.11% / 新版 86.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050663c",
      "incomplete_value": true,
      "site": "00506658",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:db7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e37a4",
      "incomplete_value": true,
      "site": "004e37c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a91:8"
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
      "site": "00506664",
      "value": [
        "leaf",
        "ram:c590e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e37cc",
      "value": [
        "leaf",
        "ram:bdc690:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00506684",
      "incomplete_value": true,
      "site": "00506690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e37ec",
      "incomplete_value": true,
      "site": "004e37f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:1e0:8"
              ]
            ]
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
      "0050663c",
      "READ",
      [
        "storage",
        "002ada91",
        null,
        "string"
      ]
    ],
    [
      "00506664",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc690"
      ]
    ],
    [
      "00506680",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050663c",
      "READ",
      [
        "storage",
        "002bedb7",
        null,
        "string"
      ]
    ],
    [
      "00506664",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c590e0"
      ]
    ],
    [
      "00506680",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e37cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3770.md#insn-004e37cc) · [`004e37f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3770.md#insn-004e37f8) · [`004e3794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3770.md#insn-004e3794)
- 新版 [`00506664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506608.md#insn-00506664) · [`00506690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506608.md#insn-00506690) · [`0050662c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506608.md#insn-0050662c)

~~~diff
- 004e37cc ["INT_ADD", "register:40f0:8", ["const:4e37cc:8", "const:4:8"]]
- 004e37cc ["CALL", null, ["ram:bdc690:8"]]
+ 00506664 ["INT_ADD", "register:40f0:8", ["const:506664:8", "const:4:8"]]
+ 00506664 ["CALL", null, ["ram:c590e0:8"]]
- 004e37cc bytes b1e31b94
+ 00506664 bytes 9f4a1d94
- 004e37f8 ["INT_ADD", "register:40f0:8", ["const:4e37f8:8", "const:4:8"]]
- 004e37f8 ["CALL", null, ["callee:00c57b10:8"]]
+ 00506690 ["INT_ADD", "register:40f0:8", ["const:506690:8", "const:4:8"]]
+ 00506690 ["CALL", null, ["callee:00c57b10:8"]]
- 004e37f8 bytes 32de1b94
+ 00506690 bytes 20451d94
- 004e3794 ["INT_ADD", "register:40f0:8", ["const:4e3794:8", "const:4:8"]]
- 004e3794 ["CALL", null, ["callee:00c57af0:8"]]
+ 0050662c ["INT_ADD", "register:40f0:8", ["const:50662c:8", "const:4:8"]]
+ 0050662c ["CALL", null, ["callee:00c57af0:8"]]
- 004e3794 bytes 43de1b94
+ 0050662c bytes 31451d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ba72ed76e8ee267334cb5b834d59269"></a>

### [`004e3840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3840.md) → [`005066d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005066d8.md) _ZN5Botan11GeneralName11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 29件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)
- 新版 呼出元 0件  · 呼出先 29件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.27% / 新版 94.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00506764",
      "incomplete_value": true,
      "site": "00506764",
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
      "definition_site": "004e38cc",
      "incomplete_value": true,
      "site": "004e38cc",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005067e8",
      "incomplete_value": true,
      "site": "005067f0",
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
      "definition_site": "004e3950",
      "incomplete_value": true,
      "site": "004e3958",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "005067f8",
      "incomplete_value": true,
      "site": "005067f8",
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
      "definition_site": "004e3960",
      "incomplete_value": true,
      "site": "004e3960",
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
      "0050674c",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "00506764",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506774",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba40"
      ]
    ]
  ],
  "added": [
    [
      "0050674c",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "00506764",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506774",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58490"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e38dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3840.md#insn-004e38dc) · [`004e3940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3840.md#insn-004e3940) · [`004e39dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e3/004e3840.md#insn-004e39dc)
- 新版 [`00506774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005066d8.md#insn-00506774) · [`005067d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005066d8.md#insn-005067d8) · [`00506874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005066d8.md#insn-00506874)

~~~diff
- 004e38dc ["INT_ADD", "register:40f0:8", ["const:4e38dc:8", "const:4:8"]]
- 004e38dc ["CALL", null, ["ram:bdba40:8"]]
+ 00506774 ["INT_ADD", "register:40f0:8", ["const:506774:8", "const:4:8"]]
+ 00506774 ["CALL", null, ["ram:c58490:8"]]
- 004e38dc bytes 59e01b94
+ 00506774 bytes 47471d94
- 004e3940 ["INT_ADD", "register:40f0:8", ["const:4e3940:8", "const:4:8"]]
- 004e3940 ["CALL", null, ["callee:00c57d90:8"]]
+ 005067d8 ["INT_ADD", "register:40f0:8", ["const:5067d8:8", "const:4:8"]]
+ 005067d8 ["CALL", null, ["callee:00c57d90:8"]]
- 004e3940 bytes 80de1b94
+ 005067d8 bytes 6e451d94
- 004e39dc ["COPY", "register:0:8", ["register:4048:8"]]
- 004e39dc ["INT_ADD", "register:40f0:8", ["const:4e39dc:8", "const:4:8"]]
- 004e39dc ["CALLIND", null, ["register:0:8"]]
+ 00506874 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00506874 ["INT_ADD", "register:40f0:8", ["const:506874:8", "const:4:8"]]
+ 00506874 ["CALLIND", null, ["register:0:8"]]
- 004e39dc bytes 20013fd6
+ 00506874 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4dcf98e4e35f81ad3ee87a9c3e23055"></a>

### [`004e40b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e40b8.md) → [`00506f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md) _ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004dcf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcf48.md) [`004f03d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f03d8.md) [`00bdccf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccf0.md) · 呼出先 12件 [`00482aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482aa8.md) [`00525f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 3件 [`004ffde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md) [`00513270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md) [`00c59740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59740.md) · 呼出先 12件 [`004a5940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md) [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.34% / 新版 95.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00506fe4",
      "incomplete_value": true,
      "site": "00506fe4",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004e414c",
      "incomplete_value": true,
      "site": "004e414c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00506ff8",
      "value": [
        "leaf",
        "ram:c58480:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e4160",
      "value": [
        "leaf",
        "ram:bdba30:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050711c",
      "incomplete_value": true,
      "site": "0050711c",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004e4284",
      "incomplete_value": true,
      "site": "004e4284",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00506fd4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00506ff8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba30"
      ]
    ],
    [
      "0050710c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00506fd4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00506ff8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58480"
      ]
    ],
    [
      "0050710c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e414c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e40b8.md#insn-004e414c) · [`004e4160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e40b8.md#insn-004e4160) · [`004e4284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e40b8.md#insn-004e4284)
- 新版 [`00506fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md#insn-00506fe4) · [`00506ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md#insn-00506ff8) · [`0050711c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md#insn-0050711c)

~~~diff
- 004e414c ["COPY", "register:0:8", ["register:4048:8"]]
- 004e414c ["INT_ADD", "register:40f0:8", ["const:4e414c:8", "const:4:8"]]
- 004e414c ["CALLIND", null, ["register:0:8"]]
+ 00506fe4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00506fe4 ["INT_ADD", "register:40f0:8", ["const:506fe4:8", "const:4:8"]]
+ 00506fe4 ["CALLIND", null, ["register:0:8"]]
- 004e414c bytes 20013fd6
+ 00506fe4 bytes 20013fd6
- 004e4160 ["INT_ADD", "register:40f0:8", ["const:4e4160:8", "const:4:8"]]
- 004e4160 ["CALL", null, ["ram:bdba30:8"]]
+ 00506ff8 ["INT_ADD", "register:40f0:8", ["const:506ff8:8", "const:4:8"]]
+ 00506ff8 ["CALL", null, ["ram:c58480:8"]]
- 004e4160 bytes 34de1b94
+ 00506ff8 bytes 22451d94
- 004e4284 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e4284 ["INT_ADD", "register:40f0:8", ["const:4e4284:8", "const:4:8"]]
- 004e4284 ["CALLIND", null, ["register:0:8"]]
+ 0050711c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050711c ["INT_ADD", "register:40f0:8", ["const:50711c:8", "const:4:8"]]
+ 0050711c ["CALLIND", null, ["register:0:8"]]
- 004e4284 bytes 20013fd6
+ 0050711c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2a19b4440a4745de3a0f2b5c2be0bbf"></a>

### [`004e4494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md) → [`0050732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) _ZNK5Botan11GeneralName7matchesERKNS_16X509_CertificateE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd00.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`004e4bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4bdc.md)
- 新版 呼出元 1件 [`00c59750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59750.md) · 呼出先 23件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00507a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a74.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.49% / 新版 95.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005073fc",
      "incomplete_value": true,
      "site": "005073fc",
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
      "definition_site": "004e4564",
      "incomplete_value": true,
      "site": "004e4564",
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
    "kind": "store_value",
    "new": {
      "definition_site": "005073fc",
      "incomplete_value": true,
      "site": "005073fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e4564",
      "incomplete_value": true,
      "site": "004e4564",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:348:8"
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
      "definition_site": "0050747c",
      "incomplete_value": true,
      "site": "0050747c",
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
      "definition_site": "004e45e4",
      "incomplete_value": true,
      "site": "004e45e4",
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
      "005073dc",
      "READ",
      [
        "storage",
        "00c1b340",
        null,
        "pointer"
      ]
    ],
    [
      "005073e0",
      "READ",
      [
        "storage",
        "00c1b348",
        null,
        "pointer"
      ]
    ],
    [
      "005073fc",
      "DATA",
      [
        "storage",
        "00bed9d0",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "005073dc",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ],
    [
      "005073e0",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "005073fc",
      "DATA",
      [
        "storage",
        "00c6a590",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e44d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md#insn-004e44d8) · [`004e44e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md#insn-004e44e4) · [`004e4538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md#insn-004e4538)
- 新版 [`00507370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md#insn-00507370) · [`0050737c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md#insn-0050737c) · [`005073d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md#insn-005073d0)

~~~diff
- 004e44d8 ["INT_ADD", "register:40f0:8", ["const:4e44d8:8", "const:4:8"]]
- 004e44d8 ["CALL", null, ["callee:00c595f0:8"]]
+ 00507370 ["INT_ADD", "register:40f0:8", ["const:507370:8", "const:4:8"]]
+ 00507370 ["CALL", null, ["callee:00c595f0:8"]]
- 004e44d8 bytes b2e11b94
+ 00507370 bytes a0481d94
- 004e44e4 ["INT_ADD", "register:40f0:8", ["const:4e44e4:8", "const:4:8"]]
- 004e44e4 ["CALL", null, ["callee:00c595f0:8"]]
+ 0050737c ["INT_ADD", "register:40f0:8", ["const:50737c:8", "const:4:8"]]
+ 0050737c ["CALL", null, ["callee:00c595f0:8"]]
- 004e44e4 bytes afe11b94
+ 0050737c bytes 9d481d94
- 004e4538 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005073d0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004e4538 bytes a83900f0
+ 005073d0 bytes 883c00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45cf6786d0923e27eb87c82abd2e7ec5"></a>

### [`004e4bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4bf4.md) → [`00507a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a8c.md) _ZNK5Botan11GeneralName11matches_dnsERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e4494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0050732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.49% / 新版 99.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00507b98",
      "incomplete_value": false,
      "site": "00507ba8",
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
    "old": {
      "definition_site": "004e4d00",
      "incomplete_value": false,
      "site": "004e4d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7da:8"
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
      "00507b98",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00507b98",
      "PARAM",
      [
        "storage",
        "002a630f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e4d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4bf4.md#insn-004e4d10) · [`004e4c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4bf4.md#insn-004e4c8c) · [`004e4cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4bf4.md#insn-004e4cfc)
- 新版 [`00507ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a8c.md#insn-00507ba8) · [`00507b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a8c.md#insn-00507b24) · [`00507b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a8c.md#insn-00507b94)

~~~diff
- 004e4d10 ["INT_ADD", "register:40f0:8", ["const:4e4d10:8", "const:4:8"]]
- 004e4d10 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00507ba8 ["INT_ADD", "register:40f0:8", ["const:507ba8:8", "const:4:8"]]
+ 00507ba8 ["CALL", null, ["callee:00c57cb0:8"]]
- 004e4d10 bytes 54d91b94
+ 00507ba8 bytes 42401d94
- 004e4c8c ["INT_ADD", "register:40f0:8", ["const:4e4c8c:8", "const:4:8"]]
- 004e4c8c ["CALL", null, ["callee:00c57c50:8"]]
+ 00507b24 ["INT_ADD", "register:40f0:8", ["const:507b24:8", "const:4:8"]]
+ 00507b24 ["CALL", null, ["callee:00c57c50:8"]]
- 004e4c8c bytes 5dd91b94
+ 00507b24 bytes 4b401d94
- 004e4cfc ["COPY", "register:4000:8", ["const:296000:8"]]
+ 00507b94 ["COPY", "register:4000:8", ["const:2a6000:8"]]
- 004e4cfc bytes 80edffd0
+ 00507b94 bytes e0ecfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ee029d0a5cd669b4eddfc6b88019a5a"></a>

### [`004e50d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md) → [`00507f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md) _ZNK5Botan11GeneralName10matches_dnERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e4494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md) · 呼出先 13件 [`004e56e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e56e4.md) [`004e5d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5d50.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00526790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526790.md) [`005267f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005267f0.md)
- 新版 呼出元 1件 [`0050732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) · 呼出先 13件 [`0050857c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md) [`00508be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508be8.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00549628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) [`00549688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549688.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.66% / 新版 94.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00507fd8",
      "incomplete_value": true,
      "site": "00507fd8",
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
      "definition_site": "004e5140",
      "incomplete_value": true,
      "site": "004e5140",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00507fe4",
      "incomplete_value": true,
      "site": "00507fe4",
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
      "definition_site": "004e514c",
      "incomplete_value": true,
      "site": "004e514c",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005081d4",
      "incomplete_value": true,
      "site": "005081dc",
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
      "definition_site": "004e533c",
      "incomplete_value": true,
      "site": "004e5344",
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
      "00507fc0",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "00507fd8",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00507fe4",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00507fc0",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "00507fd8",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00507fe4",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md#insn-004e5108) · [`004e5118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md#insn-004e5118) · [`004e511c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md#insn-004e511c)
- 新版 [`00507fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md#insn-00507fa0) · [`00507fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md#insn-00507fb0) · [`00507fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md#insn-00507fb4)

~~~diff
- 004e5108 ["INT_ADD", "register:40f0:8", ["const:4e5108:8", "const:4:8"]]
- 004e5108 ["CALL", null, ["callee:0050857c:8"]]
+ 00507fa0 ["INT_ADD", "register:40f0:8", ["const:507fa0:8", "const:4:8"]]
+ 00507fa0 ["CALL", null, ["callee:0050857c:8"]]
- 004e5108 bytes 77010094
+ 00507fa0 bytes 77010094
- 004e5118 ["INT_ADD", "register:40f0:8", ["const:4e5118:8", "const:4:8"]]
- 004e5118 ["CALL", null, ["callee:0050857c:8"]]
+ 00507fb0 ["INT_ADD", "register:40f0:8", ["const:507fb0:8", "const:4:8"]]
+ 00507fb0 ["CALL", null, ["callee:0050857c:8"]]
- 004e5118 bytes 73010094
+ 00507fb0 bytes 73010094
- 004e511c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00507fb4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004e511c bytes a83900d0
+ 00507fb4 bytes 883c00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd89ce49d64d009686bc4e58cdf2dd95"></a>

### [`004e548c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e548c.md) → [`00508324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508324.md) _ZNK5Botan11GeneralName10matches_ipERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `boundary_candidate`

- 旧版 呼出元 1件 [`004e4494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4494.md) · 呼出先 15件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`00463ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ea0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md)
- 新版 呼出元 1件 [`0050732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) · 呼出先 12件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00486d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d38.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.95% / 新版 96.46%

CFGの説明率　旧版 70.00% / 新版 96.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 4件, `call_argument_candidate` 2件, `call_count` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00508358",
      "incomplete_value": false,
      "site": "00508360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e54c0",
      "incomplete_value": false,
      "site": "004e54c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "site": "004e5654"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "004e5658"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00508360",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "005083a8",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      "005083a8",
      "READ",
      [
        "storage",
        "00bed718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00508360",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005083a8",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "005083a8",
      "READ",
      [
        "storage",
        "00c6a2d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e55f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e548c.md#insn-004e55f4) · [`004e5630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e548c.md#insn-004e5630) · [`004e5654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e548c.md#insn-004e5654)
- 新版 [`0050848c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508324.md#insn-0050848c) · [`005084c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508324.md#insn-005084c8)

~~~diff
- 004e55f4 ["INT_ADD", "register:40f0:8", ["const:4e55f4:8", "const:4:8"]]
- 004e55f4 ["CALL", null, ["callee:0043dd98:8"]]
+ 0050848c ["INT_ADD", "register:40f0:8", ["const:50848c:8", "const:4:8"]]
+ 0050848c ["CALL", null, ["callee:0043dd98:8"]]
- 004e55f4 bytes 29d7fc97
+ 0050848c bytes 43d6fc97
- 004e5630 ["INT_ADD", "register:40f0:8", ["const:4e5630:8", "const:4:8"]]
- 004e5630 ["CALL", null, ["callee:00c57b10:8"]]
+ 005084c8 ["INT_ADD", "register:40f0:8", ["const:5084c8:8", "const:4:8"]]
+ 005084c8 ["CALL", null, ["callee:00c57b10:8"]]
- 004e5630 bytes a4d61b94
+ 005084c8 bytes 923d1d94
- 004e5654 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 004e5654 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 004e5654 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 004e5654 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 004e5654 bytes 68000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9cdc91ae5eef64a3a00877d3ca52b6a"></a>

### [`004e56e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e56e4.md) → [`0050857c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md) FUN_0050857c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004dcbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcbd4.md) [`004e50d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md) · 呼出先 4件 [`00525380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525380.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3a0.md) [`00bdb5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5e0.md)
- 新版 呼出元 2件 [`004ffa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md) [`00507f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md) · 呼出先 4件 [`00548218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548218.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md) [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 78.08% / 新版 78.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005085cc",
      "incomplete_value": true,
      "site": "005085cc",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e5734",
      "incomplete_value": true,
      "site": "004e5734",
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
            "const:68:8"
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
      "definition_site": "005085d0",
      "incomplete_value": true,
      "site": "005085d0",
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
      "definition_site": "004e5738",
      "incomplete_value": true,
      "site": "004e5738",
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
      "definition_site": "005085c8",
      "incomplete_value": true,
      "site": "005085d8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004e5730",
      "incomplete_value": true,
      "site": "004e5740",
      "value": [
        "LOAD",
        "8",
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
      "005085a4",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "005085b0",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "005085c8",
      "READ",
      [
        "storage",
        "00c13350",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "005085a4",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "005085b0",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "005085c8",
      "READ",
      [
        "storage",
        "00c92cf8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e56e4.md#insn-004e5700) · [`004e5704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e56e4.md#insn-004e5704) · [`004e570c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e56e4.md#insn-004e570c)
- 新版 [`00508598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md#insn-00508598) · [`0050859c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md#insn-0050859c) · [`005085a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md#insn-005085a4)

~~~diff
- 004e5700 ["COPY", "register:40c8:8", ["const:c1a000:8"]]
+ 00508598 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
- 004e5700 bytes b93900b0
+ 00508598 bytes 993c00d0
- 004e5704 ["COPY", "register:40c0:8", ["const:c1a000:8"]]
+ 0050859c ["COPY", "register:40c0:8", ["const:c9a000:8"]]
- 004e5704 bytes b83900b0
+ 0050859c bytes 983c00d0
- 004e570c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e28:8"]]
- 004e570c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005085a4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:818:8"]]
+ 005085a4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004e570c bytes 391747f9
+ 005085a4 bytes 390f44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f30898a4d4e28ecbd8fcc3d9cfd41672"></a>

### [`004e5850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5850.md) → [`005086e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/005086e8.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_7X509_DNE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb40.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004f2498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2498.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c59590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59590.md) · 呼出先 12件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00515330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515330.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.02% / 新版 99.02%

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
      "definition_site": "005089cc",
      "incomplete_value": false,
      "site": "005089d4",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e5b34",
      "incomplete_value": false,
      "site": "004e5b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:b43:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00508a04",
      "incomplete_value": true,
      "site": "00508a10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e5b6c",
      "incomplete_value": true,
      "site": "004e5b78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00508a00",
      "incomplete_value": false,
      "site": "00508a10",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004e5b68",
      "incomplete_value": false,
      "site": "004e5b78",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 18,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005089cc",
      "PARAM",
      [
        "storage",
        "00296b43",
        null,
        "string"
      ]
    ],
    [
      "00508a00",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "00508a04",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005089cc",
      "PARAM",
      [
        "storage",
        "002a6678",
        null,
        "string"
      ]
    ],
    [
      "00508a00",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00508a04",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5850.md#insn-004e5b3c) · [`004e5b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5850.md#insn-004e5b78) · [`004e58dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5850.md#insn-004e58dc)
- 新版 [`005089d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/005086e8.md#insn-005089d4) · [`00508a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/005086e8.md#insn-00508a10) · [`00508774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/005086e8.md#insn-00508774)

~~~diff
- 004e5b3c ["INT_ADD", "register:40f0:8", ["const:4e5b3c:8", "const:4:8"]]
- 004e5b3c ["CALL", null, ["callee:0043dd98:8"]]
+ 005089d4 ["INT_ADD", "register:40f0:8", ["const:5089d4:8", "const:4:8"]]
+ 005089d4 ["CALL", null, ["callee:0043dd98:8"]]
- 004e5b3c bytes d7d5fc97
+ 005089d4 bytes f1d4fc97
- 004e5b78 ["INT_ADD", "register:40f0:8", ["const:4e5b78:8", "const:4:8"]]
- 004e5b78 ["CALL", null, ["callee:00c57b10:8"]]
+ 00508a10 ["INT_ADD", "register:40f0:8", ["const:508a10:8", "const:4:8"]]
+ 00508a10 ["CALL", null, ["callee:00c57b10:8"]]
- 004e5b78 bytes 52d51b94
+ 00508a10 bytes 403c1d94
- 004e58dc ["INT_ADD", "register:40f0:8", ["const:4e58dc:8", "const:4:8"]]
- 004e58dc ["CALL", null, ["callee:00515330:8"]]
+ 00508774 ["INT_ADD", "register:40f0:8", ["const:508774:8", "const:4:8"]]
+ 00508774 ["CALL", null, ["callee:00515330:8"]]
- 004e58dc bytes ef320094
+ 00508774 bytes ef320094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1387d6e836381ff04ec943893213ea1a"></a>

### [`004e5d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5d50.md) → [`00508be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508be8.md) FUN_00508be8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004e50d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00507f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00508c20",
      "incomplete_value": true,
      "site": "00508c24",
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
      "definition_site": "004e5d88",
      "incomplete_value": true,
      "site": "004e5d8c",
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
      "00508c10",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "00508c24",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00508c10",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "00508c24",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5d50.md#insn-004e5d6c) · [`004e5d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5d50.md#insn-004e5d78) · [`004e5da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5d50.md#insn-004e5da0)
- 新版 [`00508c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508be8.md#insn-00508c04) · [`00508c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508be8.md#insn-00508c10) · [`00508c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508be8.md#insn-00508c38)

~~~diff
- 004e5d6c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00508c04 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004e5d6c bytes a83900b0
+ 00508c04 bytes 883c00d0
- 004e5d78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
- 004e5d78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00508c10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
+ 00508c10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e5d78 bytes 08a947f9
+ 00508c10 bytes 08a144f9
- 004e5da0 ["INT_ADD", "register:40f0:8", ["const:4e5da0:8", "const:4:8"]]
- 004e5da0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00508c38 ["INT_ADD", "register:40f0:8", ["const:508c38:8", "const:4:8"]]
+ 00508c38 ["CALL", null, ["callee:00c57a90:8"]]
- 004e5da0 bytes a8d41b94
+ 00508c38 bytes 963b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f432d071a6c336076fb6a85899afeaa"></a>

### [`004e5e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5e70.md) → [`00508d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508d08.md) _ZN5Botan14GeneralSubtreeC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00508d58",
      "incomplete_value": true,
      "site": "00508d58",
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
      "definition_site": "004e5ec0",
      "incomplete_value": true,
      "site": "004e5ec0",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00508d58",
      "incomplete_value": true,
      "site": "00508d58",
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
      "definition_site": "004e5ec0",
      "incomplete_value": true,
      "site": "004e5ec0",
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
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00508ef8",
      "value": [
        "leaf",
        "ram:c59780:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e6060",
      "value": [
        "leaf",
        "ram:bdcd30:8"
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
      "00508d34",
      "READ",
      [
        "storage",
        "00c1b360",
        null,
        "pointer"
      ]
    ],
    [
      "00508d3c",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ],
    [
      "00508d58",
      "DATA",
      [
        "storage",
        "00beb158",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00508d34",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ],
    [
      "00508d3c",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00508d58",
      "DATA",
      [
        "storage",
        "00c67d18",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5e70.md#insn-004e6060) · [`004e616c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5e70.md#insn-004e616c) · [`004e61a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5e70.md#insn-004e61a8)
- 新版 [`00508ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508d08.md#insn-00508ef8) · [`00509004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508d08.md#insn-00509004) · [`00509040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508d08.md#insn-00509040)

~~~diff
- 004e6060 ["INT_ADD", "register:40f0:8", ["const:4e6060:8", "const:4:8"]]
- 004e6060 ["CALL", null, ["ram:bdcd30:8"]]
+ 00508ef8 ["INT_ADD", "register:40f0:8", ["const:508ef8:8", "const:4:8"]]
+ 00508ef8 ["CALL", null, ["ram:c59780:8"]]
- 004e6060 bytes 34db1b94
+ 00508ef8 bytes 22421d94
- 004e616c ["INT_ADD", "register:40f0:8", ["const:4e616c:8", "const:4:8"]]
- 004e616c ["CALL", null, ["callee:0043dd98:8"]]
+ 00509004 ["INT_ADD", "register:40f0:8", ["const:509004:8", "const:4:8"]]
+ 00509004 ["CALL", null, ["callee:0043dd98:8"]]
- 004e616c bytes 4bd4fc97
+ 00509004 bytes 65d3fc97
- 004e61a8 ["INT_ADD", "register:40f0:8", ["const:4e61a8:8", "const:4:8"]]
- 004e61a8 ["CALL", null, ["callee:00c57b10:8"]]
+ 00509040 ["INT_ADD", "register:40f0:8", ["const:509040:8", "const:4:8"]]
+ 00509040 ["CALL", null, ["callee:00c57b10:8"]]
- 004e61a8 bytes c6d31b94
+ 00509040 bytes b43a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-008a25860d7c8bee0a5e3bfaaba804b3"></a>

### [`004e6294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6294.md) → [`0050912c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/0050912c.md) _ZNK5Botan14GeneralSubtree11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050916c",
      "incomplete_value": true,
      "site": "00509180",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fa0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e62d4",
      "incomplete_value": true,
      "site": "004e62e8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:292000:8"
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509170",
      "incomplete_value": true,
      "site": "00509184",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004e62d8",
      "incomplete_value": true,
      "site": "004e62ec",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509174",
      "incomplete_value": true,
      "site": "00509188",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "004e62dc",
      "incomplete_value": true,
      "site": "004e62f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c60:8"
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
      "0050916c",
      "READ",
      [
        "storage",
        "00292890",
        null,
        "string"
      ]
    ],
    [
      "00509170",
      "READ",
      [
        "storage",
        "002928a0",
        null,
        "string"
      ]
    ],
    [
      "00509174",
      "READ",
      [
        "storage",
        "002b0c60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050916c",
      "READ",
      [
        "storage",
        "002a1fa0",
        null,
        "string"
      ]
    ],
    [
      "00509170",
      "READ",
      [
        "storage",
        "002a1fb0",
        null,
        "string"
      ]
    ],
    [
      "00509174",
      "READ",
      [
        "storage",
        "002c2260",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6294.md#insn-004e6300) · [`004e632c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6294.md#insn-004e632c) · [`004e62b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6294.md#insn-004e62b8)
- 新版 [`00509198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/0050912c.md#insn-00509198) · [`005091c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/0050912c.md#insn-005091c4) · [`00509150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/0050912c.md#insn-00509150)

~~~diff
- 004e6300 ["INT_ADD", "register:40f0:8", ["const:4e6300:8", "const:4:8"]]
- 004e6300 ["CALL", null, ["ram:bdc690:8"]]
+ 00509198 ["INT_ADD", "register:40f0:8", ["const:509198:8", "const:4:8"]]
+ 00509198 ["CALL", null, ["ram:c590e0:8"]]
- 004e6300 bytes e4d81b94
+ 00509198 bytes d23f1d94
- 004e632c ["INT_ADD", "register:40f0:8", ["const:4e632c:8", "const:4:8"]]
- 004e632c ["CALL", null, ["callee:00c57b10:8"]]
+ 005091c4 ["INT_ADD", "register:40f0:8", ["const:5091c4:8", "const:4:8"]]
+ 005091c4 ["CALL", null, ["callee:00c57b10:8"]]
- 004e632c bytes 65d31b94
+ 005091c4 bytes 533a1d94
- 004e62b8 ["INT_ADD", "register:40f0:8", ["const:4e62b8:8", "const:4:8"]]
- 004e62b8 ["CALL", null, ["callee:00c57af0:8"]]
+ 00509150 ["INT_ADD", "register:40f0:8", ["const:509150:8", "const:4:8"]]
+ 00509150 ["CALL", null, ["callee:00c57af0:8"]]
- 004e62b8 bytes 7ad31b94
+ 00509150 bytes 683a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6faec461d6f9bab4b54c4ff99f6914e"></a>

### [`004e637c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e637c.md) → [`00509214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509214.md) _ZN5Botan14GeneralSubtree11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd40.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c59790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59790.md) · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.53% / 新版 97.53%

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
      "definition_site": "005092bc",
      "incomplete_value": true,
      "site": "005092bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e6424",
      "incomplete_value": true,
      "site": "004e6424",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
      "definition_site": "0050930c",
      "incomplete_value": false,
      "site": "00509314",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6474",
      "incomplete_value": false,
      "site": "004e647c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:e22:8"
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
      "definition_site": "00509344",
      "incomplete_value": true,
      "site": "00509350",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e64ac",
      "incomplete_value": true,
      "site": "004e64b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
      "005092ac",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050930c",
      "PARAM",
      [
        "storage",
        "00298e22",
        null,
        "string"
      ]
    ],
    [
      "00509340",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005092ac",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0050930c",
      "PARAM",
      [
        "storage",
        "002a8be0",
        null,
        "string"
      ]
    ],
    [
      "00509340",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e637c.md#insn-004e6424) · [`004e647c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e637c.md#insn-004e647c) · [`004e64b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e637c.md#insn-004e64b8)
- 新版 [`005092bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509214.md#insn-005092bc) · [`00509314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509214.md#insn-00509314) · [`00509350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509214.md#insn-00509350)

~~~diff
- 004e6424 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e6424 ["INT_ADD", "register:40f0:8", ["const:4e6424:8", "const:4:8"]]
- 004e6424 ["CALLIND", null, ["register:0:8"]]
+ 005092bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005092bc ["INT_ADD", "register:40f0:8", ["const:5092bc:8", "const:4:8"]]
+ 005092bc ["CALLIND", null, ["register:0:8"]]
- 004e6424 bytes 20013fd6
+ 005092bc bytes 20013fd6
- 004e647c ["INT_ADD", "register:40f0:8", ["const:4e647c:8", "const:4:8"]]
- 004e647c ["CALL", null, ["callee:0043dd98:8"]]
+ 00509314 ["INT_ADD", "register:40f0:8", ["const:509314:8", "const:4:8"]]
+ 00509314 ["CALL", null, ["callee:0043dd98:8"]]
- 004e647c bytes 87d3fc97
+ 00509314 bytes a1d2fc97
- 004e64b8 ["INT_ADD", "register:40f0:8", ["const:4e64b8:8", "const:4:8"]]
- 004e64b8 ["CALL", null, ["callee:00c57b10:8"]]
+ 00509350 ["INT_ADD", "register:40f0:8", ["const:509350:8", "const:4:8"]]
+ 00509350 ["CALL", null, ["callee:00c57b10:8"]]
- 004e64b8 bytes 02d31b94
+ 00509350 bytes f0391d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1b19ceea7cada7ea0a6e8ca89c5b61e"></a>

### [`004e6520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6520.md) → [`005093b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005093b8.md) FUN_005093b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004f7f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7f54.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 1件 [`0051adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051adec.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509424",
      "incomplete_value": true,
      "site": "00509428",
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
      "definition_site": "004e658c",
      "incomplete_value": true,
      "site": "004e6590",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005093f4",
      "incomplete_value": false,
      "site": "005093f8",
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
    "old": {
      "definition_site": "004e655c",
      "incomplete_value": false,
      "site": "004e6560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:ab6:8"
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
      "definition_site": "005094b0",
      "incomplete_value": false,
      "site": "005094b8",
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
            "const:987:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e6618",
      "incomplete_value": false,
      "site": "004e6620",
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
            "const:3cd:8"
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
      "005093f4",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ],
    [
      "00509404",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ],
    [
      "0050941c",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005093f4",
      "PARAM",
      [
        "storage",
        "002a998f",
        null,
        null
      ]
    ],
    [
      "00509404",
      "PARAM",
      [
        "storage",
        "002a998f",
        null,
        null
      ]
    ],
    [
      "0050941c",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6520.md#insn-004e6560) · [`004e6620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6520.md#insn-004e6620) · [`004e654c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6520.md#insn-004e654c)
- 新版 [`005093f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005093b8.md#insn-005093f8) · [`005094b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005093b8.md#insn-005094b8) · [`005093e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005093b8.md#insn-005093e4)

~~~diff
- 004e6560 ["INT_ADD", "register:40f0:8", ["const:4e6560:8", "const:4:8"]]
- 004e6560 ["CALL", null, ["callee:00459490:8"]]
+ 005093f8 ["INT_ADD", "register:40f0:8", ["const:5093f8:8", "const:4:8"]]
+ 005093f8 ["CALL", null, ["callee:00459490:8"]]
- 004e6560 bytes 2640fd97
+ 005093f8 bytes 2640fd97
- 004e6620 ["INT_ADD", "register:40f0:8", ["const:4e6620:8", "const:4:8"]]
- 004e6620 ["CALL", null, ["callee:00459490:8"]]
+ 005094b8 ["INT_ADD", "register:40f0:8", ["const:5094b8:8", "const:4:8"]]
+ 005094b8 ["CALL", null, ["callee:00459490:8"]]
- 004e6620 bytes f63ffd97
+ 005094b8 bytes f63ffd97
- 004e654c ["INT_ADD", "register:40f0:8", ["const:4e654c:8", "const:4:8"]]
- 004e654c ["CALL", null, ["callee:00c57e00:8"]]
+ 005093e4 ["INT_ADD", "register:40f0:8", ["const:5093e4:8", "const:4:8"]]
+ 005093e4 ["CALL", null, ["callee:00c57e00:8"]]
- 004e654c bytes 99d31b94
+ 005093e4 bytes 873a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-730cffddcdc11eef2c3ca2e06bf1b1b0"></a>

### [`004e66d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e66d0.md) → [`00509568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509568.md) _ZN5Botan4OCSP7RequestC2ERKNS_16X509_CertificateES4_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00518128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518128.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.81% / 新版 96.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005095a4",
      "incomplete_value": true,
      "site": "005095a8",
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
      "definition_site": "004e670c",
      "incomplete_value": true,
      "site": "004e6710",
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00509600",
      "value": [
        "leaf",
        "ram:c597a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e6768",
      "value": [
        "leaf",
        "ram:bdcd50:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00509628",
      "incomplete_value": true,
      "site": "00509628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e6790",
      "incomplete_value": true,
      "site": "004e6790",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
      "005095a0",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "005095a8",
      "DATA",
      [
        "storage",
        "00beaac8",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00509600",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcd50"
      ]
    ]
  ],
  "added": [
    [
      "005095a0",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "005095a8",
      "DATA",
      [
        "storage",
        "00c67688",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00509600",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c597a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e66d0.md#insn-004e6768) · [`004e6790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e66d0.md#insn-004e6790) · [`004e6804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e66d0.md#insn-004e6804)
- 新版 [`00509600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509568.md#insn-00509600) · [`00509628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509568.md#insn-00509628) · [`0050969c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509568.md#insn-0050969c)

~~~diff
- 004e6768 ["INT_ADD", "register:40f0:8", ["const:4e6768:8", "const:4:8"]]
- 004e6768 ["CALL", null, ["ram:bdcd50:8"]]
+ 00509600 ["INT_ADD", "register:40f0:8", ["const:509600:8", "const:4:8"]]
+ 00509600 ["CALL", null, ["ram:c597a0:8"]]
- 004e6768 bytes 7ad91b94
+ 00509600 bytes 68401d94
- 004e6790 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e6790 ["INT_ADD", "register:40f0:8", ["const:4e6790:8", "const:4:8"]]
- 004e6790 ["CALLIND", null, ["register:0:8"]]
+ 00509628 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509628 ["INT_ADD", "register:40f0:8", ["const:509628:8", "const:4:8"]]
+ 00509628 ["CALLIND", null, ["register:0:8"]]
- 004e6790 bytes 20013fd6
+ 00509628 bytes 20013fd6
- 004e6804 ["INT_ADD", "register:40f0:8", ["const:4e6804:8", "const:4:8"]]
- 004e6804 ["CALL", null, ["callee:0043dd98:8"]]
+ 0050969c ["INT_ADD", "register:40f0:8", ["const:50969c:8", "const:4:8"]]
+ 0050969c ["CALL", null, ["callee:0043dd98:8"]]
- 004e6804 bytes a5d2fc97
+ 0050969c bytes bfd1fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4976e74e6119593e0580a012cd38ac6c"></a>

### [`004e697c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e697c.md) → [`00509814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509814.md) FUN_00509814

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

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
      "definition_site": "00509830",
      "incomplete_value": true,
      "site": "00509834",
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
      "definition_site": "004e6998",
      "incomplete_value": true,
      "site": "004e699c",
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
      "definition_site": "00509870",
      "incomplete_value": true,
      "site": "00509874",
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
      "definition_site": "004e69d8",
      "incomplete_value": true,
      "site": "004e69dc",
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
      "00509828",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "00509834",
      "DATA",
      [
        "storage",
        "00beaac8",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00509868",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509828",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "00509834",
      "DATA",
      [
        "storage",
        "00c67688",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00509868",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e697c.md#insn-004e6988) · [`004e6990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e697c.md#insn-004e6990) · [`004e69ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e697c.md#insn-004e69ac)
- 新版 [`00509820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509814.md#insn-00509820) · [`00509828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509814.md#insn-00509828) · [`00509844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509814.md#insn-00509844)

~~~diff
- 004e6988 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00509820 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004e6988 bytes a83900b0
+ 00509820 bytes 883c00b0
- 004e6990 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f0:8"]]
- 004e6990 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00509828 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce0:8"]]
+ 00509828 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004e6990 bytes 087941f9
+ 00509828 bytes 087146f9
- 004e69ac ["INT_ADD", "register:40f0:8", ["const:4e69ac:8", "const:4:8"]]
- 004e69ac ["CALL", null, ["callee:00c538e0:8"]]
+ 00509844 ["INT_ADD", "register:40f0:8", ["const:509844:8", "const:4:8"]]
+ 00509844 ["CALL", null, ["callee:00c538e0:8"]]
- 004e69ac bytes 39c11b94
+ 00509844 bytes 27281d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d4ca625d9e25ed1d6c0f6c8b6fb3a71"></a>

### [`004e6a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6a30.md) → [`005098c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005098c8.md) _ZN5Botan4OCSP7RequestC1ERKNS_16X509_CertificateERKNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00518128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518128.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdcd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c597a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597a0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005098f0",
      "incomplete_value": true,
      "site": "005098f8",
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
      "definition_site": "004e6a58",
      "incomplete_value": true,
      "site": "004e6a60",
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0050991c",
      "value": [
        "leaf",
        "ram:c597a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e6a84",
      "value": [
        "leaf",
        "ram:bdcd50:8"
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
      "005098ec",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "005098f8",
      "DATA",
      [
        "storage",
        "00beaac8",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "0050991c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcd50"
      ]
    ]
  ],
  "added": [
    [
      "005098ec",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "005098f8",
      "DATA",
      [
        "storage",
        "00c67688",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "0050991c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c597a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6a30.md#insn-004e6a84) · [`004e6a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6a30.md#insn-004e6a4c) · [`004e6a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6a30.md#insn-004e6a50)
- 新版 [`0050991c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005098c8.md#insn-0050991c) · [`005098e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005098c8.md#insn-005098e4) · [`005098e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005098c8.md#insn-005098e8)

~~~diff
- 004e6a84 ["INT_ADD", "register:40f0:8", ["const:4e6a84:8", "const:4:8"]]
- 004e6a84 ["CALL", null, ["ram:bdcd50:8"]]
+ 0050991c ["INT_ADD", "register:40f0:8", ["const:50991c:8", "const:4:8"]]
+ 0050991c ["CALL", null, ["ram:c597a0:8"]]
- 004e6a84 bytes b3d81b94
+ 0050991c bytes a13f1d94
- 004e6a4c ["INT_ADD", "register:40f0:8", ["const:4e6a4c:8", "const:4:8"]]
- 004e6a4c ["CALL", null, ["callee:0053afc0:8"]]
+ 005098e4 ["INT_ADD", "register:40f0:8", ["const:5098e4:8", "const:4:8"]]
+ 005098e4 ["CALL", null, ["callee:0053afc0:8"]]
- 004e6a4c bytes b7c50094
+ 005098e4 bytes b7c50094
- 004e6a50 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005098e8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004e6a50 bytes a83900b0
+ 005098e8 bytes 883c00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cedd9d30e38160f9d2b3ebecb82e6fdd"></a>

### [`004e6aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6aac.md) → [`00509944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509944.md) _ZNK5Botan4OCSP7Request10BER_encodeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd60.md) · 呼出先 10件 [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 1件 [`00c597b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597b0.md) · 呼出先 10件 [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005099f0",
      "incomplete_value": true,
      "site": "005099f0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004e6b58",
      "incomplete_value": true,
      "site": "004e6b58",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00509ac4",
      "incomplete_value": true,
      "site": "00509ac4",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004e6c2c",
      "incomplete_value": true,
      "site": "004e6c2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005099e0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00509ab4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005099e0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00509ab4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6aac.md#insn-004e6b58) · [`004e6c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6aac.md#insn-004e6c2c) · [`004e6af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6aac.md#insn-004e6af0)
- 新版 [`005099f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509944.md#insn-005099f0) · [`00509ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509944.md#insn-00509ac4) · [`00509988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509944.md#insn-00509988)

~~~diff
- 004e6b58 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e6b58 ["INT_ADD", "register:40f0:8", ["const:4e6b58:8", "const:4:8"]]
- 004e6b58 ["CALLIND", null, ["register:0:8"]]
+ 005099f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005099f0 ["INT_ADD", "register:40f0:8", ["const:5099f0:8", "const:4:8"]]
+ 005099f0 ["CALLIND", null, ["register:0:8"]]
- 004e6b58 bytes 20013fd6
+ 005099f0 bytes 20013fd6
- 004e6c2c ["COPY", "register:0:8", ["register:4048:8"]]
- 004e6c2c ["INT_ADD", "register:40f0:8", ["const:4e6c2c:8", "const:4:8"]]
- 004e6c2c ["CALLIND", null, ["register:0:8"]]
+ 00509ac4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509ac4 ["INT_ADD", "register:40f0:8", ["const:509ac4:8", "const:4:8"]]
+ 00509ac4 ["CALLIND", null, ["register:0:8"]]
- 004e6c2c bytes 20013fd6
+ 00509ac4 bytes 20013fd6
- 004e6af0 ["INT_ADD", "register:40f0:8", ["const:4e6af0:8", "const:4:8"]]
- 004e6af0 ["CALL", null, ["callee:00c582b0:8"]]
+ 00509988 ["INT_ADD", "register:40f0:8", ["const:509988:8", "const:4:8"]]
+ 00509988 ["CALL", null, ["callee:00c582b0:8"]]
- 004e6af0 bytes 5cd31b94
+ 00509988 bytes 4a3a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db4cb44db3206599a60ce40fbc925595"></a>

### [`004e6d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md) → [`00509bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md) _ZN5Botan4OCSP8ResponseC2EPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 41件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md) [`00482aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482aa8.md) [`0048bb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bb9c.md) [`004e7aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7aa4.md)
- 新版 呼出元 0件  · 呼出先 41件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004a5940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md) [`004aea34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aea34.md) [`0050a93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050a93c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.01% / 新版 94.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 5件, `store_value` 10件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509c5c",
      "incomplete_value": true,
      "site": "00509c5c",
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
      "definition_site": "004e6dc4",
      "incomplete_value": true,
      "site": "004e6dc4",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509c84",
      "incomplete_value": true,
      "site": "00509c84",
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
      "definition_site": "004e6dec",
      "incomplete_value": true,
      "site": "004e6dec",
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509cb0",
      "incomplete_value": true,
      "site": "00509cb0",
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
      "definition_site": "004e6e18",
      "incomplete_value": true,
      "site": "004e6e18",
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
    "ordinal": 33,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00509c50",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "00509c5c",
      "DATA",
      [
        "storage",
        "00be93b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00509c6c",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509c50",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ],
    [
      "00509c5c",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00509c6c",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e6e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md#insn-004e6e64) · [`004e6eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md#insn-004e6eb8) · [`004e6f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md#insn-004e6f74)
- 新版 [`00509cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md#insn-00509cfc) · [`00509d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md#insn-00509d50) · [`00509e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md#insn-00509e0c)

~~~diff
- 004e6e64 ["INT_ADD", "register:40f0:8", ["const:4e6e64:8", "const:4:8"]]
- 004e6e64 ["CALL", null, ["ram:bdba30:8"]]
+ 00509cfc ["INT_ADD", "register:40f0:8", ["const:509cfc:8", "const:4:8"]]
+ 00509cfc ["CALL", null, ["ram:c58480:8"]]
- 004e6e64 bytes f3d21b94
+ 00509cfc bytes e1391d94
- 004e6eb8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e6eb8 ["INT_ADD", "register:40f0:8", ["const:4e6eb8:8", "const:4:8"]]
- 004e6eb8 ["CALLIND", null, ["register:0:8"]]
+ 00509d50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509d50 ["INT_ADD", "register:40f0:8", ["const:509d50:8", "const:4:8"]]
+ 00509d50 ["CALLIND", null, ["register:0:8"]]
- 004e6eb8 bytes 20013fd6
+ 00509d50 bytes 20013fd6
- 004e6f74 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e6f74 ["INT_ADD", "register:40f0:8", ["const:4e6f74:8", "const:4:8"]]
- 004e6f74 ["CALLIND", null, ["register:0:8"]]
+ 00509e0c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509e0c ["INT_ADD", "register:40f0:8", ["const:509e0c:8", "const:4:8"]]
+ 00509e0c ["CALLIND", null, ["register:0:8"]]
- 004e6f74 bytes 20013fd6
+ 00509e0c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6d07f758d8a3fad5bf1f2f878a83874"></a>

### [`004e7aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7aa4.md) → [`0050a93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050a93c.md) FUN_0050a93c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004e6d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00509bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.57% / 新版 98.57%

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
      "definition_site": "0050aa44",
      "incomplete_value": true,
      "site": "0050aa4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e7bac",
      "incomplete_value": true,
      "site": "004e7bb4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050aa40",
      "incomplete_value": false,
      "site": "0050aa4c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004e7ba8",
      "incomplete_value": false,
      "site": "004e7bb4",
      "value": [
        "leaf",
        "const:512990:8"
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
      "0050aa40",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "0050aa44",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ],
    [
      "0050aa44",
      "PARAM",
      [
        "storage",
        "00be9300",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0050aa40",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0050aa44",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ],
    [
      "0050aa44",
      "PARAM",
      [
        "storage",
        "00c65ec0",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e7bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7aa4.md#insn-004e7bb4) · [`004e7adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7aa4.md#insn-004e7adc) · [`004e7aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7aa4.md#insn-004e7aec)
- 新版 [`0050aa4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050a93c.md#insn-0050aa4c) · [`0050a974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050a93c.md#insn-0050a974) · [`0050a984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050a93c.md#insn-0050a984)

~~~diff
- 004e7bb4 ["INT_ADD", "register:40f0:8", ["const:4e7bb4:8", "const:4:8"]]
- 004e7bb4 ["CALL", null, ["callee:00c57b10:8"]]
+ 0050aa4c ["INT_ADD", "register:40f0:8", ["const:50aa4c:8", "const:4:8"]]
+ 0050aa4c ["CALL", null, ["callee:00c57b10:8"]]
- 004e7bb4 bytes 43cd1b94
+ 0050aa4c bytes 31341d94
- 004e7adc ["INT_ADD", "register:40f0:8", ["const:4e7adc:8", "const:4:8"]]
- 004e7adc ["CALL", null, ["callee:00c58290:8"]]
+ 0050a974 ["INT_ADD", "register:40f0:8", ["const:50a974:8", "const:4:8"]]
+ 0050a974 ["CALL", null, ["callee:00c58290:8"]]
- 004e7adc bytes 59cf1b94
+ 0050a974 bytes 47361d94
- 004e7aec ["INT_ADD", "register:40f0:8", ["const:4e7aec:8", "const:4:8"]]
- 004e7aec ["CALL", null, ["callee:00c57ab0:8"]]
+ 0050a984 ["INT_ADD", "register:40f0:8", ["const:50a984:8", "const:4:8"]]
+ 0050a984 ["CALL", null, ["callee:00c57ab0:8"]]
- 004e7aec bytes 5dcd1b94
+ 0050a984 bytes 4b341d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85136d6d62a352bc31b9e5d4f9cc9a7e"></a>

### [`004e7c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7c0c.md) → [`0050aaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050aaa4.md) _ZN5Botan11BER_Decoder15decode_optionalINS_7X509_DNEEERS0_RT_NS_8ASN1_TagES6_RKS4_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd80.md) · 呼出先 9件 [`00518ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518ea0.md) [`00525f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8d0.md)
- 新版 呼出元 1件 [`00c597d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597d0.md) · 呼出先 9件 [`0053bd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md) [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58320.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.01% / 新版 99.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0050ab14",
      "value": [
        "leaf",
        "ram:c58490:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e7c7c",
      "value": [
        "leaf",
        "ram:bdba40:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050ab70",
      "incomplete_value": true,
      "site": "0050ab70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e7cd8",
      "incomplete_value": true,
      "site": "004e7cd8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050abfc",
      "incomplete_value": true,
      "site": "0050abfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e7d64",
      "incomplete_value": true,
      "site": "004e7d64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
      "0050ab14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba40"
      ]
    ],
    [
      "0050ab60",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050abec",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050ab14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58490"
      ]
    ],
    [
      "0050ab60",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0050abec",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e7c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7c0c.md#insn-004e7c7c) · [`004e7cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7c0c.md#insn-004e7cd8) · [`004e7d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7c0c.md#insn-004e7d64)
- 新版 [`0050ab14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050aaa4.md#insn-0050ab14) · [`0050ab70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050aaa4.md#insn-0050ab70) · [`0050abfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050aaa4.md#insn-0050abfc)

~~~diff
- 004e7c7c ["INT_ADD", "register:40f0:8", ["const:4e7c7c:8", "const:4:8"]]
- 004e7c7c ["CALL", null, ["ram:bdba40:8"]]
+ 0050ab14 ["INT_ADD", "register:40f0:8", ["const:50ab14:8", "const:4:8"]]
+ 0050ab14 ["CALL", null, ["ram:c58490:8"]]
- 004e7c7c bytes 71cf1b94
+ 0050ab14 bytes 5f361d94
- 004e7cd8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e7cd8 ["INT_ADD", "register:40f0:8", ["const:4e7cd8:8", "const:4:8"]]
- 004e7cd8 ["CALLIND", null, ["register:0:8"]]
+ 0050ab70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050ab70 ["INT_ADD", "register:40f0:8", ["const:50ab70:8", "const:4:8"]]
+ 0050ab70 ["CALLIND", null, ["register:0:8"]]
- 004e7cd8 bytes 20013fd6
+ 0050ab70 bytes 20013fd6
- 004e7d64 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e7d64 ["INT_ADD", "register:40f0:8", ["const:4e7d64:8", "const:4:8"]]
- 004e7d64 ["CALLIND", null, ["register:0:8"]]
+ 0050abfc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050abfc ["INT_ADD", "register:40f0:8", ["const:50abfc:8", "const:4:8"]]
+ 0050abfc ["CALLIND", null, ["register:0:8"]]
- 004e7d64 bytes 20013fd6
+ 0050abfc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2350918359677bfb9750e13f12710835"></a>

### [`004e7de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7de0.md) → [`0050ac78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ac78.md) FUN_0050ac78

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004e6d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e6/004e6d3c.md) [`004f6548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6548.md) [`004fdfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdfd8.md) · 呼出先 8件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8d0.md) [`00bdba40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba40.md) [`00bdba50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba50.md)
- 新版 呼出元 3件 [`00509bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md) [`005193e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005193e0.md) [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) · 呼出先 8件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58320.md) [`00c58490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58490.md) [`00c584a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584a0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.96% / 新版 98.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0050acec",
      "value": [
        "leaf",
        "ram:c58490:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e7e54",
      "value": [
        "leaf",
        "ram:bdba40:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050ad4c",
      "incomplete_value": true,
      "site": "0050ad4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e7eb4",
      "incomplete_value": true,
      "site": "004e7eb4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050adbc",
      "incomplete_value": true,
      "site": "0050adbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e7f24",
      "incomplete_value": true,
      "site": "004e7f24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
      "0050acec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba40"
      ]
    ],
    [
      "0050ad3c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050adac",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050acec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58490"
      ]
    ],
    [
      "0050ad3c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0050adac",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e7e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7de0.md#insn-004e7e54) · [`004e7eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7de0.md#insn-004e7eb4) · [`004e7f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7de0.md#insn-004e7f24)
- 新版 [`0050acec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ac78.md#insn-0050acec) · [`0050ad4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ac78.md#insn-0050ad4c) · [`0050adbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ac78.md#insn-0050adbc)

~~~diff
- 004e7e54 ["INT_ADD", "register:40f0:8", ["const:4e7e54:8", "const:4:8"]]
- 004e7e54 ["CALL", null, ["ram:bdba40:8"]]
+ 0050acec ["INT_ADD", "register:40f0:8", ["const:50acec:8", "const:4:8"]]
+ 0050acec ["CALL", null, ["ram:c58490:8"]]
- 004e7e54 bytes fbce1b94
+ 0050acec bytes e9351d94
- 004e7eb4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e7eb4 ["INT_ADD", "register:40f0:8", ["const:4e7eb4:8", "const:4:8"]]
- 004e7eb4 ["CALLIND", null, ["register:0:8"]]
+ 0050ad4c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050ad4c ["INT_ADD", "register:40f0:8", ["const:50ad4c:8", "const:4:8"]]
+ 0050ad4c ["CALLIND", null, ["register:0:8"]]
- 004e7eb4 bytes 20013fd6
+ 0050ad4c bytes 20013fd6
- 004e7f24 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e7f24 ["INT_ADD", "register:40f0:8", ["const:4e7f24:8", "const:4:8"]]
- 004e7f24 ["CALLIND", null, ["register:0:8"]]
+ 0050adbc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050adbc ["INT_ADD", "register:40f0:8", ["const:50adbc:8", "const:4:8"]]
+ 0050adbc ["CALLIND", null, ["register:0:8"]]
- 004e7f24 bytes 20013fd6
+ 0050adbc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-121a33cc31d5969aa6187215a67b1f70"></a>

### [`004e7fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7fa0.md) → [`0050ae38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md) _ZN5Botan11BER_Decoder11decode_listINS_4OCSP14SingleResponseEEERS0_RNSt6__ndk16vectorIT_NS5_9allocatorIS7_EEEENS_8ASN1_TagESC_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd90.md) · 呼出先 10件 [`004e9fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9fdc.md) [`005269b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005269b0.md) [`00526bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526bb4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c597e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597e0.md) · 呼出先 10件 [`0050ce74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md) [`00549848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md) [`00549a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549a4c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.53% / 新版 90.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050af7c",
      "incomplete_value": true,
      "site": "0050af7c",
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
      "definition_site": "004e80e4",
      "incomplete_value": true,
      "site": "004e80e4",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050af9c",
      "incomplete_value": true,
      "site": "0050af9c",
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
      "definition_site": "004e8104",
      "incomplete_value": true,
      "site": "004e8104",
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
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050af98",
      "incomplete_value": true,
      "site": "0050afa8",
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
      "definition_site": "004e8100",
      "incomplete_value": true,
      "site": "004e8110",
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
      "0050ae8c",
      "READ",
      [
        "storage",
        "00c1b370",
        null,
        "pointer"
      ]
    ],
    [
      "0050ae90",
      "READ",
      [
        "storage",
        "00c1b378",
        null,
        "pointer"
      ]
    ],
    [
      "0050ae94",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050ae8c",
      "READ",
      [
        "storage",
        "00c9ad60",
        null,
        "pointer"
      ]
    ],
    [
      "0050ae90",
      "READ",
      [
        "storage",
        "00c9ad68",
        null,
        "pointer"
      ]
    ],
    [
      "0050ae94",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e8168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7fa0.md#insn-004e8168) · [`004e81fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7fa0.md#insn-004e81fc) · [`004e7fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7fa0.md#insn-004e7fe4)
- 新版 [`0050b000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md#insn-0050b000) · [`0050b094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md#insn-0050b094) · [`0050ae7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md#insn-0050ae7c)

~~~diff
- 004e8168 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e8168 ["INT_ADD", "register:40f0:8", ["const:4e8168:8", "const:4:8"]]
- 004e8168 ["CALLIND", null, ["register:0:8"]]
+ 0050b000 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050b000 ["INT_ADD", "register:40f0:8", ["const:50b000:8", "const:4:8"]]
+ 0050b000 ["CALLIND", null, ["register:0:8"]]
- 004e8168 bytes 20013fd6
+ 0050b000 bytes 20013fd6
- 004e81fc ["COPY", "register:0:8", ["register:4048:8"]]
- 004e81fc ["INT_ADD", "register:40f0:8", ["const:4e81fc:8", "const:4:8"]]
- 004e81fc ["CALLIND", null, ["register:0:8"]]
+ 0050b094 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050b094 ["INT_ADD", "register:40f0:8", ["const:50b094:8", "const:4:8"]]
+ 0050b094 ["CALLIND", null, ["register:0:8"]]
- 004e81fc bytes 20013fd6
+ 0050b094 bytes 20013fd6
- 004e7fe4 ["INT_ADD", "register:40f0:8", ["const:4e7fe4:8", "const:4:8"]]
- 004e7fe4 ["CALL", null, ["callee:00c58300:8"]]
+ 0050ae7c ["INT_ADD", "register:40f0:8", ["const:50ae7c:8", "const:4:8"]]
+ 0050ae7c ["CALL", null, ["callee:00c58300:8"]]
- 004e7fe4 bytes 33ce1b94
+ 0050ae7c bytes 21351d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f92778b964ee25ab412f9eed8ead51b6"></a>

### [`004e82ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e82ac.md) → [`0050b144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b144.md) _ZN5Botan11BER_Decoder15decode_optionalINS_10ExtensionsEEERS0_RT_NS_8ASN1_TagES6_RKS4_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcda0.md) · 呼出先 9件 [`0051bd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bd98.md) [`00526f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526f54.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8d0.md)
- 新版 呼出元 1件 [`00c597f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597f0.md) · 呼出先 9件 [`0053ec30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ec30.md) [`00549dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58320.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0050b1b4",
      "value": [
        "leaf",
        "ram:c58490:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e831c",
      "value": [
        "leaf",
        "ram:bdba40:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050b210",
      "incomplete_value": true,
      "site": "0050b210",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e8378",
      "incomplete_value": true,
      "site": "004e8378",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050b2a0",
      "incomplete_value": true,
      "site": "0050b2a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e8408",
      "incomplete_value": true,
      "site": "004e8408",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
      "0050b1b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba40"
      ]
    ],
    [
      "0050b200",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050b290",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050b1b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58490"
      ]
    ],
    [
      "0050b200",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0050b290",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e831c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e82ac.md#insn-004e831c) · [`004e8378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e82ac.md#insn-004e8378) · [`004e8408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e82ac.md#insn-004e8408)
- 新版 [`0050b1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b144.md#insn-0050b1b4) · [`0050b210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b144.md#insn-0050b210) · [`0050b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b144.md#insn-0050b2a0)

~~~diff
- 004e831c ["INT_ADD", "register:40f0:8", ["const:4e831c:8", "const:4:8"]]
- 004e831c ["CALL", null, ["ram:bdba40:8"]]
+ 0050b1b4 ["INT_ADD", "register:40f0:8", ["const:50b1b4:8", "const:4:8"]]
+ 0050b1b4 ["CALL", null, ["ram:c58490:8"]]
- 004e831c bytes c9cd1b94
+ 0050b1b4 bytes b7341d94
- 004e8378 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e8378 ["INT_ADD", "register:40f0:8", ["const:4e8378:8", "const:4:8"]]
- 004e8378 ["CALLIND", null, ["register:0:8"]]
+ 0050b210 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050b210 ["INT_ADD", "register:40f0:8", ["const:50b210:8", "const:4:8"]]
+ 0050b210 ["CALLIND", null, ["register:0:8"]]
- 004e8378 bytes 20013fd6
+ 0050b210 bytes 20013fd6
- 004e8408 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e8408 ["INT_ADD", "register:40f0:8", ["const:4e8408:8", "const:4:8"]]
- 004e8408 ["CALLIND", null, ["register:0:8"]]
+ 0050b2a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050b2a0 ["INT_ADD", "register:40f0:8", ["const:50b2a0:8", "const:4:8"]]
+ 0050b2a0 ["CALLIND", null, ["register:0:8"]]
- 004e8408 bytes 20013fd6
+ 0050b2a0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc17d1e71d30d0853cf019cb774a26c4"></a>

### [`004e85ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e85ec.md) → [`0050b484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b484.md) _ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdb0.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00483d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483d44.md) [`00524c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c3c.md) [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c98.md)
- 新版 呼出元 1件 [`00c59800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59800.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004a6bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6bdc.md) [`00547ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547ad4.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.43% / 新版 98.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0050b4d4",
      "incomplete_value": false,
      "site": "0050b4d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e863c",
      "incomplete_value": false,
      "site": "004e863c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "site": "0050b6b0",
      "value": [
        "leaf",
        "ram:c58e70:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e8818",
      "value": [
        "leaf",
        "ram:bdc420:8"
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
      "0050b4d4",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0050b518",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      "0050b518",
      "READ",
      [
        "storage",
        "00bed718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0050b4d4",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0050b518",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "0050b518",
      "READ",
      [
        "storage",
        "00c6a2d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e8818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e85ec.md#insn-004e8818) · [`004e861c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e85ec.md#insn-004e861c) · [`004e862c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e85ec.md#insn-004e862c)
- 新版 [`0050b6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b484.md#insn-0050b6b0) · [`0050b4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b484.md#insn-0050b4b4) · [`0050b4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b484.md#insn-0050b4c4)

~~~diff
- 004e8818 ["INT_ADD", "register:40f0:8", ["const:4e8818:8", "const:4:8"]]
- 004e8818 ["CALL", null, ["ram:bdc420:8"]]
+ 0050b6b0 ["INT_ADD", "register:40f0:8", ["const:50b6b0:8", "const:4:8"]]
+ 0050b6b0 ["CALL", null, ["ram:c58e70:8"]]
- 004e8818 bytes 02cf1b94
+ 0050b6b0 bytes f0351d94
- 004e861c ["INT_ADD", "register:40f0:8", ["const:4e861c:8", "const:4:8"]]
- 004e861c ["CALL", null, ["callee:00c59810:8"]]
+ 0050b4b4 ["INT_ADD", "register:40f0:8", ["const:50b4b4:8", "const:4:8"]]
+ 0050b4b4 ["CALL", null, ["callee:00c59810:8"]]
- 004e861c bytes e9d11b94
+ 0050b4b4 bytes d7381d94
- 004e862c ["INT_ADD", "register:40f0:8", ["const:4e862c:8", "const:4:8"]]
- 004e862c ["CALL", null, ["callee:00c584b0:8"]]
+ 0050b4c4 ["INT_ADD", "register:40f0:8", ["const:50b4c4:8", "const:4:8"]]
+ 0050b4c4 ["CALL", null, ["callee:00c584b0:8"]]
- 004e862c bytes 0dcd1b94
+ 0050b4c4 bytes fb331d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-211e09e4f3d831261e6f87c7f8c29f3b"></a>

### [`004e8a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8a14.md) → [`0050b8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b8ac.md) _ZNK5Botan4OCSP8Response15check_signatureERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS2_9allocatorIS5_EEEERKNS3_INS2_10shared_ptrIKNS_16X5

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcdd0.md) · 呼出先 13件 [`00518128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518128.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c59820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59820.md) · 呼出先 13件 [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.35% / 新版 97.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050bbb0",
      "incomplete_value": true,
      "site": "0050bbbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c7a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e8d18",
      "incomplete_value": true,
      "site": "004e8d24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:40d:8"
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
      "definition_site": "0050bd44",
      "incomplete_value": true,
      "site": "0050bd48",
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
      "definition_site": "004e8eac",
      "incomplete_value": true,
      "site": "004e8eb0",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050bd78",
      "incomplete_value": true,
      "site": "0050bd7c",
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
      "definition_site": "004e8ee0",
      "incomplete_value": true,
      "site": "004e8ee4",
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
      "0050bbb0",
      "READ",
      [
        "storage",
        "002a440d",
        null,
        "string"
      ]
    ],
    [
      "0050bd3c",
      "READ",
      [
        "storage",
        "00c1b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "0050bd48",
      "DATA",
      [
        "storage",
        "00bed780",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "0050bbb0",
      "READ",
      [
        "storage",
        "002b4c7a",
        null,
        "string"
      ]
    ],
    [
      "0050bd3c",
      "READ",
      [
        "storage",
        "00c9acd8",
        null,
        "pointer"
      ]
    ],
    [
      "0050bd48",
      "DATA",
      [
        "storage",
        "00c6a340",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e8a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8a14.md#insn-004e8a98) · [`004e8ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8a14.md#insn-004e8ab8) · [`004e8ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8a14.md#insn-004e8ad0)
- 新版 [`0050b930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b8ac.md#insn-0050b930) · [`0050b950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b8ac.md#insn-0050b950) · [`0050b968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b8ac.md#insn-0050b968)

~~~diff
- 004e8a98 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e8a98 ["INT_ADD", "register:40f0:8", ["const:4e8a98:8", "const:4:8"]]
- 004e8a98 ["CALLIND", null, ["register:0:8"]]
+ 0050b930 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050b930 ["INT_ADD", "register:40f0:8", ["const:50b930:8", "const:4:8"]]
+ 0050b930 ["CALLIND", null, ["register:0:8"]]
- 004e8a98 bytes 20013fd6
+ 0050b930 bytes 20013fd6
- 004e8ab8 ["INT_ADD", "register:40f0:8", ["const:4e8ab8:8", "const:4:8"]]
- 004e8ab8 ["CALL", null, ["callee:00c538e0:8"]]
+ 0050b950 ["INT_ADD", "register:40f0:8", ["const:50b950:8", "const:4:8"]]
+ 0050b950 ["CALL", null, ["callee:00c538e0:8"]]
- 004e8ab8 bytes f6b81b94
+ 0050b950 bytes e41f1d94
- 004e8ad0 ["INT_ADD", "register:40f0:8", ["const:4e8ad0:8", "const:4:8"]]
- 004e8ad0 ["CALL", null, ["callee:00c538e0:8"]]
+ 0050b968 ["INT_ADD", "register:40f0:8", ["const:50b968:8", "const:4:8"]]
+ 0050b968 ["CALL", null, ["callee:00c538e0:8"]]
- 004e8ad0 bytes f0b81b94
+ 0050b968 bytes de1f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1943281def01ae5af863fc2d294cafbb"></a>

### [`004e8fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8fec.md) → [`0050be84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050be84.md) _ZNK5Botan16X509_Certificate33subject_public_key_bitstring_sha1Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcde0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c59830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59830.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "definition_site": "0050befc",
      "incomplete_value": false,
      "site": "0050bf04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:16f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e9064",
      "incomplete_value": false,
      "site": "004e906c",
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
            "const:b4b:8"
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
      "definition_site": "0050bf38",
      "incomplete_value": true,
      "site": "0050bf44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e90a0",
      "incomplete_value": true,
      "site": "004e90ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:fa8:8"
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
      "definition_site": "0050bf34",
      "incomplete_value": false,
      "site": "0050bf44",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004e909c",
      "incomplete_value": false,
      "site": "004e90ac",
      "value": [
        "leaf",
        "const:512990:8"
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
      "0050befc",
      "PARAM",
      [
        "storage",
        "002afb4b",
        null,
        "string"
      ]
    ],
    [
      "0050bf34",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "0050bf38",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050befc",
      "PARAM",
      [
        "storage",
        "002c116f",
        null,
        "string"
      ]
    ],
    [
      "0050bf34",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0050bf38",
      "READ",
      [
        "storage",
        "00c9a998",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e906c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8fec.md#insn-004e906c) · [`004e90ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8fec.md#insn-004e90ac) · [`004e9010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8fec.md#insn-004e9010)
- 新版 [`0050bf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050be84.md#insn-0050bf04) · [`0050bf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050be84.md#insn-0050bf44) · [`0050bea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050be84.md#insn-0050bea8)

~~~diff
- 004e906c ["INT_ADD", "register:40f0:8", ["const:4e906c:8", "const:4:8"]]
- 004e906c ["CALL", null, ["callee:0043dd98:8"]]
+ 0050bf04 ["INT_ADD", "register:40f0:8", ["const:50bf04:8", "const:4:8"]]
+ 0050bf04 ["CALL", null, ["callee:0043dd98:8"]]
- 004e906c bytes 8bc8fc97
+ 0050bf04 bytes a5c7fc97
- 004e90ac ["INT_ADD", "register:40f0:8", ["const:4e90ac:8", "const:4:8"]]
- 004e90ac ["CALL", null, ["callee:00c57b10:8"]]
+ 0050bf44 ["INT_ADD", "register:40f0:8", ["const:50bf44:8", "const:4:8"]]
+ 0050bf44 ["CALL", null, ["callee:00c57b10:8"]]
- 004e90ac bytes 05c81b94
+ 0050bf44 bytes f32e1d94
- 004e9010 ["INT_ADD", "register:40f0:8", ["const:4e9010:8", "const:4:8"]]
- 004e9010 ["CALL", null, ["callee:00c595f0:8"]]
+ 0050bea8 ["INT_ADD", "register:40f0:8", ["const:50bea8:8", "const:4:8"]]
+ 0050bea8 ["CALL", null, ["callee:00c595f0:8"]]
- 004e9010 bytes e4ce1b94
+ 0050bea8 bytes d2351d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8d99eb26932d6225c9ad861932c48f8"></a>

### [`004e9260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9260.md) → [`0050c0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c0f8.md) _ZNK5Botan4OCSP8Response10status_forERKNS_16X509_CertificateES4_NSt6__ndk16chrono10time_pointINS6_12system_clockENS6_8durationIxNS5_5ratioIL

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdce00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce00.md) · 呼出先 4件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb90.md) [`00bdcc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc20.md) [`00bdce10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce10.md)
- 新版 呼出元 1件 [`00c59850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59850.md) · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md) [`00c59670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59670.md) [`00c59860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59860.md)

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
      "definition_site": "0050c1b8",
      "incomplete_value": true,
      "site": "0050c1c0",
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
      "definition_site": "004e9320",
      "incomplete_value": true,
      "site": "004e9328",
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
      "0050c1ac",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "0050c1c0",
      "DATA",
      [
        "storage",
        "00be93b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050c1fc",
      "DATA",
      [
        "storage",
        "00be93b8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050c1ac",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ],
    [
      "0050c1c0",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050c1fc",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e92a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9260.md#insn-004e92a8) · [`004e92f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9260.md#insn-004e92f0) · [`004e9308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9260.md#insn-004e9308)
- 新版 [`0050c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c0f8.md#insn-0050c140) · [`0050c188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c0f8.md#insn-0050c188) · [`0050c1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c0f8.md#insn-0050c1a0)

~~~diff
- 004e92a8 ["INT_ADD", "register:40f0:8", ["const:4e92a8:8", "const:4:8"]]
- 004e92a8 ["CALL", null, ["callee:00c59860:8"]]
+ 0050c140 ["INT_ADD", "register:40f0:8", ["const:50c140:8", "const:4:8"]]
+ 0050c140 ["CALL", null, ["callee:00c59860:8"]]
- 004e92a8 bytes dace1b94
+ 0050c140 bytes c8351d94
- 004e92f0 ["INT_ADD", "register:40f0:8", ["const:4e92f0:8", "const:4:8"]]
- 004e92f0 ["CALL", null, ["callee:00c59670:8"]]
+ 0050c188 ["INT_ADD", "register:40f0:8", ["const:50c188:8", "const:4:8"]]
+ 0050c188 ["CALL", null, ["callee:00c59670:8"]]
- 004e92f0 bytes 4cce1b94
+ 0050c188 bytes 3a351d94
- 004e9308 ["COPY", "register:4098:8", ["const:c1a000:8"]]
+ 0050c1a0 ["COPY", "register:4098:8", ["const:c9a000:8"]]
- 004e9308 bytes 933900b0
+ 0050c1a0 bytes 733c00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b1b6e43b6057fdaa24c732abce45644"></a>

### [`004e97e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e97e0.md) → [`0050c678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c678.md) _ZN5Botan4OCSP6CertIDC2ERKNS_16X509_CertificateERKNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd50.md) · 呼出先 14件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c597a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597a0.md) · 呼出先 14件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050c6c4",
      "incomplete_value": true,
      "site": "0050c6d0",
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
      "definition_site": "004e982c",
      "incomplete_value": true,
      "site": "004e9838",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050c6d4",
      "incomplete_value": true,
      "site": "0050c6d4",
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
      "definition_site": "004e983c",
      "incomplete_value": true,
      "site": "004e983c",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0050c7a0",
      "value": [
        "leaf",
        "ram:c58a10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e9908",
      "value": [
        "leaf",
        "ram:bdbfc0:8"
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
      "0050c6b4",
      "READ",
      [
        "storage",
        "00c1b378",
        null,
        "pointer"
      ]
    ],
    [
      "0050c6b8",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0050c6d0",
      "DATA",
      [
        "storage",
        "00bea858",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050c6b4",
      "READ",
      [
        "storage",
        "00c9ad68",
        null,
        "pointer"
      ]
    ],
    [
      "0050c6b8",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0050c6d0",
      "DATA",
      [
        "storage",
        "00c67418",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e9908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e97e0.md#insn-004e9908) · [`004e9a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e97e0.md#insn-004e9a70) · [`004e9b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e97e0.md#insn-004e9b58)
- 新版 [`0050c7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c678.md#insn-0050c7a0) · [`0050c908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c678.md#insn-0050c908) · [`0050c9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c678.md#insn-0050c9f0)

~~~diff
- 004e9908 ["INT_ADD", "register:40f0:8", ["const:4e9908:8", "const:4:8"]]
- 004e9908 ["CALL", null, ["ram:bdbfc0:8"]]
+ 0050c7a0 ["INT_ADD", "register:40f0:8", ["const:50c7a0:8", "const:4:8"]]
+ 0050c7a0 ["CALL", null, ["ram:c58a10:8"]]
- 004e9908 bytes aec91b94
+ 0050c7a0 bytes 9c301d94
- 004e9a70 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e9a70 ["INT_ADD", "register:40f0:8", ["const:4e9a70:8", "const:4:8"]]
- 004e9a70 ["CALLIND", null, ["register:0:8"]]
+ 0050c908 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050c908 ["INT_ADD", "register:40f0:8", ["const:50c908:8", "const:4:8"]]
+ 0050c908 ["CALLIND", null, ["register:0:8"]]
- 004e9a70 bytes 20013fd6
+ 0050c908 bytes 20013fd6
- 004e9b58 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e9b58 ["INT_ADD", "register:40f0:8", ["const:4e9b58:8", "const:4:8"]]
- 004e9b58 ["CALLIND", null, ["register:0:8"]]
+ 0050c9f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050c9f0 ["INT_ADD", "register:40f0:8", ["const:50c9f0:8", "const:4:8"]]
+ 0050c9f0 ["CALLIND", null, ["register:0:8"]]
- 004e9b58 bytes 20013fd6
+ 0050c9f0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8c6da3e45169ae7fd09c010e656f5a3"></a>

### [`004e9ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9ef4.md) → [`0050cd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cd8c.md) _ZNK5Botan4OCSP14SingleResponse11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050cdcc",
      "incomplete_value": true,
      "site": "0050cde0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:137:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e9f34",
      "incomplete_value": true,
      "site": "004e9f48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b13:8"
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
      "definition_site": "0050cdd0",
      "incomplete_value": true,
      "site": "0050cde4",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e9f38",
      "incomplete_value": true,
      "site": "004e9f4c",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
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
      "definition_site": "0050cdd4",
      "incomplete_value": true,
      "site": "0050cde8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:640:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e9f3c",
      "incomplete_value": true,
      "site": "004e9f50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:30:8"
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
      "0050cdcc",
      "READ",
      [
        "storage",
        "002afb13",
        null,
        "string"
      ]
    ],
    [
      "0050cdd0",
      "READ",
      [
        "storage",
        "002afb1e",
        null,
        "string"
      ]
    ],
    [
      "0050cdd4",
      "READ",
      [
        "storage",
        "002b1030",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050cdcc",
      "READ",
      [
        "storage",
        "002c1137",
        null,
        "string"
      ]
    ],
    [
      "0050cdd0",
      "READ",
      [
        "storage",
        "002c1142",
        null,
        "string"
      ]
    ],
    [
      "0050cdd4",
      "READ",
      [
        "storage",
        "002c2640",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e9f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9ef4.md#insn-004e9f60) · [`004e9f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9ef4.md#insn-004e9f8c) · [`004e9f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9ef4.md#insn-004e9f18)
- 新版 [`0050cdf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cd8c.md#insn-0050cdf8) · [`0050ce24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cd8c.md#insn-0050ce24) · [`0050cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cd8c.md#insn-0050cdb0)

~~~diff
- 004e9f60 ["INT_ADD", "register:40f0:8", ["const:4e9f60:8", "const:4:8"]]
- 004e9f60 ["CALL", null, ["ram:bdc690:8"]]
+ 0050cdf8 ["INT_ADD", "register:40f0:8", ["const:50cdf8:8", "const:4:8"]]
+ 0050cdf8 ["CALL", null, ["ram:c590e0:8"]]
- 004e9f60 bytes ccc91b94
+ 0050cdf8 bytes ba301d94
- 004e9f8c ["INT_ADD", "register:40f0:8", ["const:4e9f8c:8", "const:4:8"]]
- 004e9f8c ["CALL", null, ["callee:00c57b10:8"]]
+ 0050ce24 ["INT_ADD", "register:40f0:8", ["const:50ce24:8", "const:4:8"]]
+ 0050ce24 ["CALL", null, ["callee:00c57b10:8"]]
- 004e9f8c bytes 4dc41b94
+ 0050ce24 bytes 3b2b1d94
- 004e9f18 ["INT_ADD", "register:40f0:8", ["const:4e9f18:8", "const:4:8"]]
- 004e9f18 ["CALL", null, ["callee:00c57af0:8"]]
+ 0050cdb0 ["INT_ADD", "register:40f0:8", ["const:50cdb0:8", "const:4:8"]]
+ 0050cdb0 ["CALL", null, ["callee:00c57af0:8"]]
- 004e9f18 bytes 62c41b94
+ 0050cdb0 bytes 502b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46a1d4a9de7cfec32879c4b9c7bbbc9b"></a>

### [`004e9fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9fdc.md) → [`0050ce74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md) _ZN5Botan4OCSP14SingleResponse11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004e7fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7fa0.md) · 呼出先 10件 [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md)
- 新版 呼出元 1件 [`0050ae38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md) · 呼出先 10件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.97% / 新版 94.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050cebc",
      "incomplete_value": true,
      "site": "0050cebc",
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
      "definition_site": "004ea024",
      "incomplete_value": true,
      "site": "004ea024",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050cf44",
      "incomplete_value": true,
      "site": "0050cf44",
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
      "definition_site": "004ea0ac",
      "incomplete_value": true,
      "site": "004ea0ac",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d02c",
      "incomplete_value": true,
      "site": "0050d02c",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004ea194",
      "incomplete_value": true,
      "site": "004ea194",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "0050cea8",
      "READ",
      [
        "storage",
        "00c1b320",
        null,
        "pointer"
      ]
    ],
    [
      "0050cebc",
      "DATA",
      [
        "storage",
        "00beb900",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050cf34",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050cea8",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "0050cebc",
      "DATA",
      [
        "storage",
        "00c684c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050cf34",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9fdc.md#insn-004ea194) · [`004ea21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9fdc.md#insn-004ea21c) · [`004e9ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e9/004e9fdc.md#insn-004e9ffc)
- 新版 [`0050d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md#insn-0050d02c) · [`0050d0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md#insn-0050d0b4) · [`0050ce94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md#insn-0050ce94)

~~~diff
- 004ea194 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ea194 ["INT_ADD", "register:40f0:8", ["const:4ea194:8", "const:4:8"]]
- 004ea194 ["CALLIND", null, ["register:0:8"]]
+ 0050d02c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d02c ["INT_ADD", "register:40f0:8", ["const:50d02c:8", "const:4:8"]]
+ 0050d02c ["CALLIND", null, ["register:0:8"]]
- 004ea194 bytes 20013fd6
+ 0050d02c bytes 20013fd6
- 004ea21c ["COPY", "register:0:8", ["register:4040:8"]]
- 004ea21c ["INT_ADD", "register:40f0:8", ["const:4ea21c:8", "const:4:8"]]
- 004ea21c ["CALLIND", null, ["register:0:8"]]
+ 0050d0b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050d0b4 ["INT_ADD", "register:40f0:8", ["const:50d0b4:8", "const:4:8"]]
+ 0050d0b4 ["CALLIND", null, ["register:0:8"]]
- 004ea21c bytes 00013fd6
+ 0050d0b4 bytes 00013fd6
- 004e9ffc ["COPY", "register:40a0:8", ["const:c1b000:8"]]
+ 0050ce94 ["COPY", "register:40a0:8", ["const:c9a000:8"]]
- 004e9ffc bytes 943900d0
+ 0050ce94 bytes 743c00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15703841ec527a5df44fee7f69d0d9fb"></a>

### [`004ea2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea2b0.md) → [`0050d148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d148.md) _ZN5Botan11BER_Decoder15decode_optionalINS_9X509_TimeEEERS0_RT_NS_8ASN1_TagES6_RKS4_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce20.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8d0.md) [`00bdba40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba40.md) [`00bdbbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbd0.md)
- 新版 呼出元 1件 [`00c59870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59870.md) · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58320.md) [`00c58490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58490.md) [`00c58620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58620.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.95% / 新版 98.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0050d1b8",
      "value": [
        "leaf",
        "ram:c58490:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ea320",
      "value": [
        "leaf",
        "ram:bdba40:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d214",
      "incomplete_value": true,
      "site": "0050d214",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ea37c",
      "incomplete_value": true,
      "site": "004ea37c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050d288",
      "incomplete_value": true,
      "site": "0050d288",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ea3f0",
      "incomplete_value": true,
      "site": "004ea3f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
      "0050d1b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba40"
      ]
    ],
    [
      "0050d204",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0050d278",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050d1b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58490"
      ]
    ],
    [
      "0050d204",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0050d278",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea2b0.md#insn-004ea320) · [`004ea37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea2b0.md#insn-004ea37c) · [`004ea3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea2b0.md#insn-004ea3f0)
- 新版 [`0050d1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d148.md#insn-0050d1b8) · [`0050d214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d148.md#insn-0050d214) · [`0050d288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d148.md#insn-0050d288)

~~~diff
- 004ea320 ["INT_ADD", "register:40f0:8", ["const:4ea320:8", "const:4:8"]]
- 004ea320 ["CALL", null, ["ram:bdba40:8"]]
+ 0050d1b8 ["INT_ADD", "register:40f0:8", ["const:50d1b8:8", "const:4:8"]]
+ 0050d1b8 ["CALL", null, ["ram:c58490:8"]]
- 004ea320 bytes c8c51b94
+ 0050d1b8 bytes b62c1d94
- 004ea37c ["COPY", "register:0:8", ["register:4048:8"]]
- 004ea37c ["INT_ADD", "register:40f0:8", ["const:4ea37c:8", "const:4:8"]]
- 004ea37c ["CALLIND", null, ["register:0:8"]]
+ 0050d214 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d214 ["INT_ADD", "register:40f0:8", ["const:50d214:8", "const:4:8"]]
+ 0050d214 ["CALLIND", null, ["register:0:8"]]
- 004ea37c bytes 20013fd6
+ 0050d214 bytes 20013fd6
- 004ea3f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ea3f0 ["INT_ADD", "register:40f0:8", ["const:4ea3f0:8", "const:4:8"]]
- 004ea3f0 ["CALLIND", null, ["register:0:8"]]
+ 0050d288 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d288 ["INT_ADD", "register:40f0:8", ["const:50d288:8", "const:4:8"]]
+ 0050d288 ["CALLIND", null, ["register:0:8"]]
- 004ea3f0 bytes 20013fd6
+ 0050d288 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4bac08983bf813f2fb12e191d7011d7"></a>

### [`004ea46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea46c.md) → [`0050d304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d304.md) _ZNK5Botan14PKCS10_Request9PEM_labelEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d310",
      "incomplete_value": true,
      "site": "0050d324",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:fa9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ea478",
      "incomplete_value": true,
      "site": "004ea48c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:28f000:8"
              ],
              [
                "leaf",
                "const:b69:8"
              ]
            ]
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
      "0050d310",
      "READ",
      [
        "storage",
        "0028fb69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050d310",
      "READ",
      [
        "storage",
        "0029efa9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea46c.md#insn-004ea46c) · [`004ea470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea46c.md#insn-004ea470)
- 新版 [`0050d304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d304.md#insn-0050d304) · [`0050d308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d304.md#insn-0050d308)

~~~diff
- 004ea46c ["COPY", "register:4050:8", ["const:28f000:8"]]
+ 0050d304 ["COPY", "register:4050:8", ["const:29e000:8"]]
- 004ea46c bytes 2aedffb0
+ 0050d304 bytes 8aecffb0
- 004ea470 ["COPY", "tmp:0:8", ["const:b69:8"]]
- 004ea470 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004ea470 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004ea470 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050d308 ["COPY", "tmp:0:8", ["const:fa9:8"]]
+ 0050d308 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050d308 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050d308 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004ea470 bytes 4aa52d91
+ 0050d308 bytes 4aa53e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e43a857ff88200184de7e9d06138e738"></a>

### [`004ea498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea498.md) → [`0050d330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d330.md) _ZNK5Botan14PKCS10_Request20alternate_PEM_labelsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d364",
      "incomplete_value": true,
      "site": "0050d374",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:994:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ea4cc",
      "incomplete_value": true,
      "site": "004ea4dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:91c:8"
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
      "definition_site": "0050d378",
      "incomplete_value": true,
      "site": "0050d378",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ea4e0",
      "incomplete_value": true,
      "site": "004ea4e0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d36c",
      "incomplete_value": true,
      "site": "0050d37c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "004ea4d4",
      "incomplete_value": true,
      "site": "004ea4e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e10:8"
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
      "0050d364",
      "READ",
      [
        "storage",
        "002ac91c",
        null,
        "string"
      ]
    ],
    [
      "0050d368",
      "READ",
      [
        "storage",
        "002ac92b",
        null,
        "string"
      ]
    ],
    [
      "0050d36c",
      "READ",
      [
        "storage",
        "002b0e10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050d364",
      "READ",
      [
        "storage",
        "002bd994",
        null,
        "string"
      ]
    ],
    [
      "0050d368",
      "READ",
      [
        "storage",
        "002bd9a3",
        null,
        "string"
      ]
    ],
    [
      "0050d36c",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea498.md#insn-004ea4bc) · [`004ea4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea498.md#insn-004ea4c0) · [`004ea4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea498.md#insn-004ea4c4)
- 新版 [`0050d354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d330.md#insn-0050d354) · [`0050d358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d330.md#insn-0050d358) · [`0050d35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d330.md#insn-0050d35c)

~~~diff
- 004ea4bc ["INT_ADD", "register:40f0:8", ["const:4ea4bc:8", "const:4:8"]]
- 004ea4bc ["CALL", null, ["callee:00c57a90:8"]]
+ 0050d354 ["INT_ADD", "register:40f0:8", ["const:50d354:8", "const:4:8"]]
+ 0050d354 ["CALL", null, ["callee:00c57a90:8"]]
- 004ea4bc bytes e1c21b94
+ 0050d354 bytes cf291d94
- 004ea4c0 ["COPY", "register:4040:8", ["const:2ac000:8"]]
+ 0050d358 ["COPY", "register:4040:8", ["const:2bd000:8"]]
- 004ea4c0 bytes 08eeffd0
+ 0050d358 bytes 88edff90
- 004ea4c4 ["COPY", "tmp:0:8", ["const:91c:8"]]
- 004ea4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004ea4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004ea4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050d35c ["COPY", "tmp:0:8", ["const:994:8"]]
+ 0050d35c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050d35c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050d35c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004ea4c4 bytes 08712491
+ 0050d35c bytes 08512691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdce22d9fb7787ef7f7d7869deeef48a"></a>

### [`004ea55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea55c.md) → [`0050d3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d3f4.md) _ZN5Botan14PKCS10_RequestC2ERNS_10DataSourceE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) [`00bdce30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) [`00c59880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59880.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d434",
      "incomplete_value": true,
      "site": "0050d434",
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
      "definition_site": "004ea59c",
      "incomplete_value": true,
      "site": "004ea59c",
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
      "definition_site": "0050d434",
      "incomplete_value": true,
      "site": "0050d434",
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
      "definition_site": "004ea59c",
      "incomplete_value": true,
      "site": "004ea59c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050d474",
      "incomplete_value": true,
      "site": "0050d47c",
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
      "definition_site": "004ea5dc",
      "incomplete_value": true,
      "site": "004ea5e4",
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
      "0050d414",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "0050d41c",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0050d434",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050d414",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "0050d41c",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0050d434",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea55c.md#insn-004ea574) · [`004ea578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea55c.md#insn-004ea578) · [`004ea57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea55c.md#insn-004ea57c)
- 新版 [`0050d40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d3f4.md#insn-0050d40c) · [`0050d410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d3f4.md#insn-0050d410) · [`0050d414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d3f4.md#insn-0050d414)

~~~diff
- 004ea574 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 0050d40c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004ea574 bytes 883900b0
+ 0050d40c bytes 683c00b0
- 004ea578 ["COPY", "register:4050:8", ["const:c1a000:8"]]
+ 0050d410 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 004ea578 bytes 8a390090
+ 0050d410 bytes 6a3c00b0
- 004ea57c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
- 004ea57c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d414 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 0050d414 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea57c bytes 08b541f9
+ 0050d414 bytes 08ad46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4f2218e7015a591e82706531610665f"></a>

### [`004ea660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea660.md) → [`0050d4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md) _ZN5Botan11X509_Object9load_dataERNS_10DataSourceE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdce30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce30.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`004840c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/004840c4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md)
- 新版 呼出元 1件 [`00c59880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59880.md) · 呼出先 18件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`004a6f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d590",
      "incomplete_value": true,
      "site": "0050d590",
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
      "definition_site": "004ea6f8",
      "incomplete_value": true,
      "site": "004ea6f8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d5cc",
      "incomplete_value": true,
      "site": "0050d5cc",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004ea734",
      "incomplete_value": true,
      "site": "004ea734",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050d6a4",
      "incomplete_value": true,
      "site": "0050d6a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ea80c",
      "incomplete_value": true,
      "site": "004ea80c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
      "0050d580",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "0050d590",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050d5bc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050d580",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "0050d590",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050d5bc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea660.md#insn-004ea734) · [`004ea80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea660.md#insn-004ea80c) · [`004eaa04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea660.md#insn-004eaa04)
- 新版 [`0050d5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md#insn-0050d5cc) · [`0050d6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md#insn-0050d6a4) · [`0050d89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md#insn-0050d89c)

~~~diff
- 004ea734 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ea734 ["INT_ADD", "register:40f0:8", ["const:4ea734:8", "const:4:8"]]
- 004ea734 ["CALLIND", null, ["register:0:8"]]
+ 0050d5cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d5cc ["INT_ADD", "register:40f0:8", ["const:50d5cc:8", "const:4:8"]]
+ 0050d5cc ["CALLIND", null, ["register:0:8"]]
- 004ea734 bytes 20013fd6
+ 0050d5cc bytes 20013fd6
- 004ea80c ["COPY", "register:0:8", ["register:4048:8"]]
- 004ea80c ["INT_ADD", "register:40f0:8", ["const:4ea80c:8", "const:4:8"]]
- 004ea80c ["CALLIND", null, ["register:0:8"]]
+ 0050d6a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d6a4 ["INT_ADD", "register:40f0:8", ["const:50d6a4:8", "const:4:8"]]
+ 0050d6a4 ["CALLIND", null, ["register:0:8"]]
- 004ea80c bytes 20013fd6
+ 0050d6a4 bytes 20013fd6
- 004eaa04 ["COPY", "register:0:8", ["register:4048:8"]]
- 004eaa04 ["INT_ADD", "register:40f0:8", ["const:4eaa04:8", "const:4:8"]]
- 004eaa04 ["CALLIND", null, ["register:0:8"]]
+ 0050d89c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d89c ["INT_ADD", "register:40f0:8", ["const:50d89c:8", "const:4:8"]]
+ 0050d89c ["CALLIND", null, ["register:0:8"]]
- 004eaa04 bytes 20013fd6
+ 0050d89c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a98abbb994e5e6e6b9fc9e7e493a8b4"></a>

### [`004eaec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004eaec8.md) → [`0050dd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd60.md) _ZN5Botan14PKCS10_RequestC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd120.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 1件 [`00c59b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b70.md) · 呼出先 7件 [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050dda0",
      "incomplete_value": true,
      "site": "0050dda0",
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
      "definition_site": "004eaf08",
      "incomplete_value": true,
      "site": "004eaf08",
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
      "definition_site": "0050dda0",
      "incomplete_value": true,
      "site": "0050dda0",
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
      "definition_site": "004eaf08",
      "incomplete_value": true,
      "site": "004eaf08",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050dde8",
      "incomplete_value": true,
      "site": "0050ddf4",
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
      "definition_site": "004eaf50",
      "incomplete_value": true,
      "site": "004eaf5c",
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
      "0050dd80",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "0050dd88",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0050dda0",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050dd80",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "0050dd88",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0050dda0",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eafb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004eaec8.md#insn-004eafb4) · [`004eaee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004eaec8.md#insn-004eaee0) · [`004eaee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004eaec8.md#insn-004eaee4)
- 新版 [`0050de4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd60.md#insn-0050de4c) · [`0050dd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd60.md#insn-0050dd78) · [`0050dd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd60.md#insn-0050dd7c)

~~~diff
- 004eafb4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004eafb4 ["INT_ADD", "register:40f0:8", ["const:4eafb4:8", "const:4:8"]]
- 004eafb4 ["CALLIND", null, ["register:0:8"]]
+ 0050de4c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050de4c ["INT_ADD", "register:40f0:8", ["const:50de4c:8", "const:4:8"]]
+ 0050de4c ["CALLIND", null, ["register:0:8"]]
- 004eafb4 bytes 20013fd6
+ 0050de4c bytes 20013fd6
- 004eaee0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 0050dd78 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004eaee0 bytes 883900b0
+ 0050dd78 bytes 683c00b0
- 004eaee4 ["COPY", "register:4050:8", ["const:c1a000:8"]]
+ 0050dd7c ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 004eaee4 bytes 8a390090
+ 0050dd7c bytes 6a3c00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4b7fc5537dca5378ae566d3cff04efb"></a>

### [`004eb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb040.md) → [`0050ded8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050ded8.md) _ZN5Botan14PKCS10_RequestC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) [`00bdc810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md) [`00bdc820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050df18",
      "incomplete_value": true,
      "site": "0050df18",
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
      "definition_site": "004eb080",
      "incomplete_value": true,
      "site": "004eb080",
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
      "definition_site": "0050df18",
      "incomplete_value": true,
      "site": "0050df18",
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
      "definition_site": "004eb080",
      "incomplete_value": true,
      "site": "004eb080",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050df58",
      "incomplete_value": true,
      "site": "0050df60",
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
      "definition_site": "004eb0c0",
      "incomplete_value": true,
      "site": "004eb0c8",
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
      "0050def8",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "0050df00",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0050df18",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050def8",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "0050df00",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0050df18",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eb0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb040.md#insn-004eb0ec) · [`004eb058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb040.md#insn-004eb058) · [`004eb05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb040.md#insn-004eb05c)
- 新版 [`0050df84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050ded8.md#insn-0050df84) · [`0050def0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050ded8.md#insn-0050def0) · [`0050def4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050ded8.md#insn-0050def4)

~~~diff
- 004eb0ec ["INT_ADD", "register:40f0:8", ["const:4eb0ec:8", "const:4:8"]]
- 004eb0ec ["CALL", null, ["ram:bdc820:8"]]
+ 0050df84 ["INT_ADD", "register:40f0:8", ["const:50df84:8", "const:4:8"]]
+ 0050df84 ["CALL", null, ["ram:c59270:8"]]
- 004eb0ec bytes cdc51b94
+ 0050df84 bytes bb2c1d94
- 004eb058 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 0050def0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004eb058 bytes 88390090
+ 0050def0 bytes 683c00b0
- 004eb05c ["COPY", "register:4050:8", ["const:c1a000:8"]]
+ 0050def4 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 004eb05c bytes 6a3900f0
+ 0050def4 bytes 6a3c00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-877f54dcc190ac168ee295e7568e3dd4"></a>

### [`004eb16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb16c.md) → [`0050e004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) _ZN5Botan14PKCS10_Request12force_decodeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 40件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`004830c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004830c8.md) [`00483d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483d44.md)
- 新版 呼出元 0件  · 呼出先 40件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a5f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md) [`004a6bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6bdc.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 5件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e1dc",
      "incomplete_value": true,
      "site": "0050e1fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "004eb344",
      "incomplete_value": true,
      "site": "004eb364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e474",
      "incomplete_value": true,
      "site": "0050e484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f7d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eb5dc",
      "incomplete_value": true,
      "site": "004eb5ec",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:293000:8"
              ],
              [
                "leaf",
                "const:784:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e488",
      "incomplete_value": true,
      "site": "0050e488",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004eb5f0",
      "incomplete_value": true,
      "site": "004eb5f0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 59,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050e084",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba30"
      ]
    ],
    [
      "0050e1c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba40"
      ]
    ],
    [
      "0050e1d0",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050e084",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58480"
      ]
    ],
    [
      "0050e1c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58490"
      ]
    ],
    [
      "0050e1d0",
      "READ",
      [
        "storage",
        "00c9a958",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eb1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb16c.md#insn-004eb1ec) · [`004eb328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb16c.md#insn-004eb328) · [`004eb3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb16c.md#insn-004eb3d4)
- 新版 [`0050e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md#insn-0050e084) · [`0050e1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md#insn-0050e1c0) · [`0050e26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md#insn-0050e26c)

~~~diff
- 004eb1ec ["INT_ADD", "register:40f0:8", ["const:4eb1ec:8", "const:4:8"]]
- 004eb1ec ["CALL", null, ["ram:bdba30:8"]]
+ 0050e084 ["INT_ADD", "register:40f0:8", ["const:50e084:8", "const:4:8"]]
+ 0050e084 ["CALL", null, ["ram:c58480:8"]]
- 004eb1ec bytes 11c21b94
+ 0050e084 bytes ff281d94
- 004eb328 ["INT_ADD", "register:40f0:8", ["const:4eb328:8", "const:4:8"]]
- 004eb328 ["CALL", null, ["ram:bdba40:8"]]
+ 0050e1c0 ["INT_ADD", "register:40f0:8", ["const:50e1c0:8", "const:4:8"]]
+ 0050e1c0 ["CALL", null, ["ram:c58490:8"]]
- 004eb328 bytes c6c11b94
+ 0050e1c0 bytes b4281d94
- 004eb3d4 ["INT_ADD", "register:40f0:8", ["const:4eb3d4:8", "const:4:8"]]
- 004eb3d4 ["CALL", null, ["ram:bdba30:8"]]
+ 0050e26c ["INT_ADD", "register:40f0:8", ["const:50e26c:8", "const:4:8"]]
+ 0050e26c ["CALL", null, ["ram:c58480:8"]]
- 004eb3d4 bytes 97c11b94
+ 0050e26c bytes 85281d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7c1cec94f8e732812894cd3f6e19a8b"></a>

### [`004ebed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004ebed4.md) → [`0050ed6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ed6c.md) _ZNK5Botan11X509_Object15check_signatureEPKNS_10Public_KeyE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdce50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce50.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`00c598a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598a0.md) · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050ee00",
      "incomplete_value": false,
      "site": "0050ee0c",
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
            "const:e39:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ebf68",
      "incomplete_value": false,
      "site": "004ebf74",
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
            "const:955:8"
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
      "definition_site": "0050ee2c",
      "incomplete_value": false,
      "site": "0050ee34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:25:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ebf94",
      "incomplete_value": false,
      "site": "004ebf9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:28f000:8"
          ],
          [
            "leaf",
            "const:be5:8"
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
      "definition_site": "0050ee7c",
      "incomplete_value": true,
      "site": "0050ee88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ebfe4",
      "incomplete_value": true,
      "site": "004ebff0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f98:8"
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
      "0050ee00",
      "PARAM",
      [
        "storage",
        "002ae955",
        null,
        "string"
      ]
    ],
    [
      "0050ee2c",
      "PARAM",
      [
        "storage",
        "0028fbe5",
        null,
        "string"
      ]
    ],
    [
      "0050ee78",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050ee00",
      "PARAM",
      [
        "storage",
        "002bfe39",
        null,
        "string"
      ]
    ],
    [
      "0050ee2c",
      "PARAM",
      [
        "storage",
        "0029f025",
        null,
        "string"
      ]
    ],
    [
      "0050ee78",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ebf74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004ebed4.md#insn-004ebf74) · [`004ebf9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004ebed4.md#insn-004ebf9c) · [`004ebff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004ebed4.md#insn-004ebff0)
- 新版 [`0050ee0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ed6c.md#insn-0050ee0c) · [`0050ee34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ed6c.md#insn-0050ee34) · [`0050ee88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ed6c.md#insn-0050ee88)

~~~diff
- 004ebf74 ["INT_ADD", "register:40f0:8", ["const:4ebf74:8", "const:4:8"]]
- 004ebf74 ["CALL", null, ["callee:00c57b60:8"]]
+ 0050ee0c ["INT_ADD", "register:40f0:8", ["const:50ee0c:8", "const:4:8"]]
+ 0050ee0c ["CALL", null, ["callee:00c57b60:8"]]
- 004ebf74 bytes 67bc1b94
+ 0050ee0c bytes 55231d94
- 004ebf9c ["INT_ADD", "register:40f0:8", ["const:4ebf9c:8", "const:4:8"]]
- 004ebf9c ["CALL", null, ["callee:00c57b70:8"]]
+ 0050ee34 ["INT_ADD", "register:40f0:8", ["const:50ee34:8", "const:4:8"]]
+ 0050ee34 ["CALL", null, ["callee:00c57b70:8"]]
- 004ebf9c bytes 61bc1b94
+ 0050ee34 bytes 4f231d94
- 004ebff0 ["INT_ADD", "register:40f0:8", ["const:4ebff0:8", "const:4:8"]]
- 004ebff0 ["CALL", null, ["callee:00c57b10:8"]]
+ 0050ee88 ["INT_ADD", "register:40f0:8", ["const:50ee88:8", "const:4:8"]]
+ 0050ee88 ["CALL", null, ["callee:00c57b10:8"]]
- 004ebff0 bytes 34bc1b94
+ 0050ee88 bytes 22231d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b86f53e7ad1a62d0b2609baa580f0990"></a>

### [`004ec0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec0b4.md) → [`0050ef4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ef4c.md) _ZNK5Botan14PKCS10_Request18subject_public_keyEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdce40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce40.md) · 呼出先 6件 [`00513e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513e2c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc880.md) [`00bdce70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce70.md)
- 新版 呼出元 1件 [`00c59890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59890.md) · 呼出先 6件 [`00536cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536cc4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c592d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md) [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050ef84",
      "incomplete_value": true,
      "site": "0050ef84",
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
      "definition_site": "004ec0ec",
      "incomplete_value": true,
      "site": "004ec0ec",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050efcc",
      "incomplete_value": true,
      "site": "0050efcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ec134",
      "incomplete_value": true,
      "site": "004ec134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:bea000:8"
              ],
              [
                "leaf",
                "const:778:8"
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
      "0050ef74",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "0050ef84",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050efbc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050ef74",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "0050ef84",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050efbc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec0b4.md#insn-004ec134) · [`004ec0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec0b4.md#insn-004ec0d4) · [`004ec0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec0b4.md#insn-004ec0d8)
- 新版 [`0050efcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ef4c.md#insn-0050efcc) · [`0050ef6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ef4c.md#insn-0050ef6c) · [`0050ef70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ef4c.md#insn-0050ef70)

~~~diff
- 004ec134 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ec134 ["INT_ADD", "register:40f0:8", ["const:4ec134:8", "const:4:8"]]
- 004ec134 ["CALLIND", null, ["register:0:8"]]
+ 0050efcc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050efcc ["INT_ADD", "register:40f0:8", ["const:50efcc:8", "const:4:8"]]
+ 0050efcc ["CALLIND", null, ["register:0:8"]]
- 004ec134 bytes 20013fd6
+ 0050efcc bytes 20013fd6
- 004ec0d4 ["INT_ADD", "register:40f0:8", ["const:4ec0d4:8", "const:4:8"]]
- 004ec0d4 ["CALL", null, ["callee:00c598c0:8"]]
+ 0050ef6c ["INT_ADD", "register:40f0:8", ["const:50ef6c:8", "const:4:8"]]
+ 0050ef6c ["CALL", null, ["callee:00c598c0:8"]]
- 004ec0d4 bytes 67c31b94
+ 0050ef6c bytes 552a1d94
- 004ec0d8 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0050ef70 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004ec0d8 bytes 683900d0
+ 0050ef70 bytes 683c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f5188435aca6e23840d407f9ff7063a"></a>

### [`004ec1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec1d0.md) → [`0050f068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f068.md) _ZNK5Botan14PKCS10_Request4dataEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdce70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce70.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "definition_site": "0050f0c8",
      "incomplete_value": false,
      "site": "0050f0d0",
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
            "const:11d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec230",
      "incomplete_value": false,
      "site": "004ec238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:b04:8"
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
      "definition_site": "0050f104",
      "incomplete_value": true,
      "site": "0050f110",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ec26c",
      "incomplete_value": true,
      "site": "004ec278",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050f100",
      "incomplete_value": false,
      "site": "0050f110",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004ec268",
      "incomplete_value": false,
      "site": "004ec278",
      "value": [
        "leaf",
        "const:512990:8"
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
      "0050f0c8",
      "PARAM",
      [
        "storage",
        "00291b04",
        null,
        "string"
      ]
    ],
    [
      "0050f100",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "0050f104",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050f0c8",
      "PARAM",
      [
        "storage",
        "002a111d",
        null,
        "string"
      ]
    ],
    [
      "0050f100",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0050f104",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec1d0.md#insn-004ec238) · [`004ec278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec1d0.md#insn-004ec278) · [`004ec224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec1d0.md#insn-004ec224)
- 新版 [`0050f0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f068.md#insn-0050f0d0) · [`0050f110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f068.md#insn-0050f110) · [`0050f0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f068.md#insn-0050f0bc)

~~~diff
- 004ec238 ["INT_ADD", "register:40f0:8", ["const:4ec238:8", "const:4:8"]]
- 004ec238 ["CALL", null, ["callee:0043dd98:8"]]
+ 0050f0d0 ["INT_ADD", "register:40f0:8", ["const:50f0d0:8", "const:4:8"]]
+ 0050f0d0 ["CALL", null, ["callee:0043dd98:8"]]
- 004ec238 bytes 18bcfc97
+ 0050f0d0 bytes 32bbfc97
- 004ec278 ["INT_ADD", "register:40f0:8", ["const:4ec278:8", "const:4:8"]]
- 004ec278 ["CALL", null, ["callee:00c57b10:8"]]
+ 0050f110 ["INT_ADD", "register:40f0:8", ["const:50f110:8", "const:4:8"]]
+ 0050f110 ["CALL", null, ["callee:00c57b10:8"]]
- 004ec278 bytes 92bb1b94
+ 0050f110 bytes 80221d94
- 004ec224 ["INT_ADD", "register:40f0:8", ["const:4ec224:8", "const:4:8"]]
- 004ec224 ["CALL", null, ["callee:00c57af0:8"]]
+ 0050f0bc ["INT_ADD", "register:40f0:8", ["const:50f0bc:8", "const:4:8"]]
+ 0050f0bc ["CALL", null, ["callee:00c57af0:8"]]
- 004ec224 bytes 9fbb1b94
+ 0050f0bc bytes 8d221d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6522f35a885b8c73ca482941c37ceaf"></a>

### [`004ec368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec368.md) → [`0050f200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f200.md) _ZNK5Botan14PKCS10_Request11constraintsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdce80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce80.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdcc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc70.md) [`00bdce70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce70.md)
- 新版 呼出元 1件 [`00c598d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598d0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c596c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596c0.md) [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f244",
      "incomplete_value": true,
      "site": "0050f244",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a8d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec3ac",
      "incomplete_value": true,
      "site": "004ec3ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:bb4:8"
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
      "definition_site": "0050f238",
      "incomplete_value": true,
      "site": "0050f248",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ec3a0",
      "incomplete_value": true,
      "site": "004ec3b0",
      "value": [
        "LOAD",
        "8",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0050f2b0",
      "incomplete_value": true,
      "site": "0050f2b0",
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
      "definition_site": "004ec418",
      "incomplete_value": true,
      "site": "004ec418",
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
      "0050f230",
      "READ",
      [
        "storage",
        "00299bb4",
        null,
        "string"
      ]
    ],
    [
      "0050f238",
      "READ",
      [
        "storage",
        "00299bbb",
        null,
        "string"
      ]
    ],
    [
      "0050f2a0",
      "READ",
      [
        "storage",
        "00c1b388",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050f230",
      "READ",
      [
        "storage",
        "002a9a8d",
        null,
        "string"
      ]
    ],
    [
      "0050f238",
      "READ",
      [
        "storage",
        "002a9a94",
        null,
        "string"
      ]
    ],
    [
      "0050f2a0",
      "READ",
      [
        "storage",
        "00c9ad78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec368.md#insn-004ec388) · [`004ec390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec368.md#insn-004ec390) · [`004ec394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec368.md#insn-004ec394)
- 新版 [`0050f220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f200.md#insn-0050f220) · [`0050f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f200.md#insn-0050f228) · [`0050f22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f200.md#insn-0050f22c)

~~~diff
- 004ec388 ["INT_ADD", "register:40f0:8", ["const:4ec388:8", "const:4:8"]]
- 004ec388 ["CALL", null, ["callee:00c598c0:8"]]
+ 0050f220 ["INT_ADD", "register:40f0:8", ["const:50f220:8", "const:4:8"]]
+ 0050f220 ["CALL", null, ["callee:00c598c0:8"]]
- 004ec388 bytes bac21b94
+ 0050f220 bytes a8291d94
- 004ec390 ["COPY", "register:4048:8", ["const:299000:8"]]
+ 0050f228 ["COPY", "register:4048:8", ["const:2a9000:8"]]
- 004ec390 bytes 69edffb0
+ 0050f228 bytes c9ecffd0
- 004ec394 ["COPY", "tmp:0:8", ["const:bb4:8"]]
- 004ec394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ec394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ec394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050f22c ["COPY", "tmp:0:8", ["const:a8d:8"]]
+ 0050f22c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050f22c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050f22c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ec394 bytes 29d12e91
+ 0050f22c bytes 29352a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb8450358ca70537bc13db9f2509820e"></a>

### [`004ec514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec514.md) → [`0050f3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md) _ZNK5Botan14PKCS10_Request14ex_constraintsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcea0.md) · 呼出先 12件 [`0050ecac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050ecac.md) [`0051bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 1件 [`00c598f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598f0.md) · 呼出先 12件 [`00531b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531b44.md) [`0053ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) [`0053efc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`00540694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_value

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f3f4",
      "incomplete_value": true,
      "site": "0050f404",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec55c",
      "incomplete_value": true,
      "site": "004ec56c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:516:8"
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
      "definition_site": "0050f408",
      "incomplete_value": true,
      "site": "0050f408",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ec570",
      "incomplete_value": true,
      "site": "004ec570",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f3fc",
      "incomplete_value": true,
      "site": "0050f40c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "004ec564",
      "incomplete_value": true,
      "site": "004ec574",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e10:8"
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
      "0050f3f4",
      "READ",
      [
        "storage",
        "002a9516",
        null,
        "string"
      ]
    ],
    [
      "0050f3f8",
      "READ",
      [
        "storage",
        "002a9525",
        null,
        "string"
      ]
    ],
    [
      "0050f3fc",
      "READ",
      [
        "storage",
        "002b0e10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f3f4",
      "READ",
      [
        "storage",
        "002ba1b9",
        null,
        "string"
      ]
    ],
    [
      "0050f3f8",
      "READ",
      [
        "storage",
        "002ba1c8",
        null,
        "string"
      ]
    ],
    [
      "0050f3fc",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec514.md#insn-004ec540) · [`004ec54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec514.md#insn-004ec54c) · [`004ec550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec514.md#insn-004ec550)
- 新版 [`0050f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md#insn-0050f3d8) · [`0050f3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md#insn-0050f3e4) · [`0050f3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md#insn-0050f3e8)

~~~diff
- 004ec540 ["INT_ADD", "register:40f0:8", ["const:4ec540:8", "const:4:8"]]
- 004ec540 ["CALL", null, ["callee:00c598c0:8"]]
+ 0050f3d8 ["INT_ADD", "register:40f0:8", ["const:50f3d8:8", "const:4:8"]]
+ 0050f3d8 ["CALL", null, ["callee:00c598c0:8"]]
- 004ec540 bytes 4cc21b94
+ 0050f3d8 bytes 3a291d94
- 004ec54c ["INT_ADD", "register:40f0:8", ["const:4ec54c:8", "const:4:8"]]
- 004ec54c ["CALL", null, ["callee:00c57a90:8"]]
+ 0050f3e4 ["INT_ADD", "register:40f0:8", ["const:50f3e4:8", "const:4:8"]]
+ 0050f3e4 ["CALL", null, ["callee:00c57a90:8"]]
- 004ec54c bytes bdba1b94
+ 0050f3e4 bytes ab211d94
- 004ec550 ["COPY", "register:4040:8", ["const:2a9000:8"]]
+ 0050f3e8 ["COPY", "register:4040:8", ["const:2ba000:8"]]
- 004ec550 bytes e8edffb0
+ 0050f3e8 bytes 48edfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba2cd1034956a6142dc5aed2354cead4"></a>

### [`004ec73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec73c.md) → [`0050f5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f5d4.md) _ZNK5Botan14PKCS10_Request5is_CAEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdceb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdceb0.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdcc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc70.md)
- 新版 呼出元 1件 [`00c59900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59900.md) · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c596c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596c0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f610",
      "incomplete_value": true,
      "site": "0050f620",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fe7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec778",
      "incomplete_value": true,
      "site": "004ec788",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9c3:8"
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
      "definition_site": "0050f624",
      "incomplete_value": true,
      "site": "0050f624",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ec78c",
      "incomplete_value": true,
      "site": "004ec78c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050f618",
      "incomplete_value": true,
      "site": "0050f628",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "004ec780",
      "incomplete_value": true,
      "site": "004ec790",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e10:8"
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
      "0050f610",
      "READ",
      [
        "storage",
        "002af9c3",
        null,
        "string"
      ]
    ],
    [
      "0050f614",
      "READ",
      [
        "storage",
        "002af9d2",
        null,
        "string"
      ]
    ],
    [
      "0050f618",
      "READ",
      [
        "storage",
        "002b0e10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f610",
      "READ",
      [
        "storage",
        "002c0fe7",
        null,
        "string"
      ]
    ],
    [
      "0050f614",
      "READ",
      [
        "storage",
        "002c0ff6",
        null,
        "string"
      ]
    ],
    [
      "0050f618",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec73c.md#insn-004ec75c) · [`004ec768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec73c.md#insn-004ec768) · [`004ec76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec73c.md#insn-004ec76c)
- 新版 [`0050f5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f5d4.md#insn-0050f5f4) · [`0050f600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f5d4.md#insn-0050f600) · [`0050f604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f5d4.md#insn-0050f604)

~~~diff
- 004ec75c ["INT_ADD", "register:40f0:8", ["const:4ec75c:8", "const:4:8"]]
- 004ec75c ["CALL", null, ["callee:00c598c0:8"]]
+ 0050f5f4 ["INT_ADD", "register:40f0:8", ["const:50f5f4:8", "const:4:8"]]
+ 0050f5f4 ["CALL", null, ["callee:00c598c0:8"]]
- 004ec75c bytes c5c11b94
+ 0050f5f4 bytes b3281d94
- 004ec768 ["INT_ADD", "register:40f0:8", ["const:4ec768:8", "const:4:8"]]
- 004ec768 ["CALL", null, ["callee:00c57a90:8"]]
+ 0050f600 ["INT_ADD", "register:40f0:8", ["const:50f600:8", "const:4:8"]]
+ 0050f600 ["CALL", null, ["callee:00c57a90:8"]]
- 004ec768 bytes 36ba1b94
+ 0050f600 bytes 24211d94
- 004ec76c ["COPY", "register:4040:8", ["const:2af000:8"]]
+ 0050f604 ["COPY", "register:4040:8", ["const:2c0000:8"]]
- 004ec76c bytes 08eefff0
+ 0050f604 bytes 88edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cefdc9d1a4d4006edb0b009d4c802ed9"></a>

### [`004ec8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec8c8.md) → [`0050f760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f760.md) _ZNK5Botan14PKCS10_Request10path_limitEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdcec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcec0.md) · 呼出先 9件 [`0050e110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e110.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md)
- 新版 呼出元 1件 [`00c59910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59910.md) · 呼出先 9件 [`00530fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530fa8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f79c",
      "incomplete_value": true,
      "site": "0050f7ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fe7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ec904",
      "incomplete_value": true,
      "site": "004ec914",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9c3:8"
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
      "definition_site": "0050f7b0",
      "incomplete_value": true,
      "site": "0050f7b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ec918",
      "incomplete_value": true,
      "site": "004ec918",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050f7a4",
      "incomplete_value": true,
      "site": "0050f7b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "004ec90c",
      "incomplete_value": true,
      "site": "004ec91c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e10:8"
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
      "0050f79c",
      "READ",
      [
        "storage",
        "002af9c3",
        null,
        "string"
      ]
    ],
    [
      "0050f7a0",
      "READ",
      [
        "storage",
        "002af9d2",
        null,
        "string"
      ]
    ],
    [
      "0050f7a4",
      "READ",
      [
        "storage",
        "002b0e10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f79c",
      "READ",
      [
        "storage",
        "002c0fe7",
        null,
        "string"
      ]
    ],
    [
      "0050f7a0",
      "READ",
      [
        "storage",
        "002c0ff6",
        null,
        "string"
      ]
    ],
    [
      "0050f7a4",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec8c8.md#insn-004ec8e8) · [`004ec8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec8c8.md#insn-004ec8f4) · [`004ec8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ec8c8.md#insn-004ec8f8)
- 新版 [`0050f780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f760.md#insn-0050f780) · [`0050f78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f760.md#insn-0050f78c) · [`0050f790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f760.md#insn-0050f790)

~~~diff
- 004ec8e8 ["INT_ADD", "register:40f0:8", ["const:4ec8e8:8", "const:4:8"]]
- 004ec8e8 ["CALL", null, ["callee:00c598c0:8"]]
+ 0050f780 ["INT_ADD", "register:40f0:8", ["const:50f780:8", "const:4:8"]]
+ 0050f780 ["CALL", null, ["callee:00c598c0:8"]]
- 004ec8e8 bytes 62c11b94
+ 0050f780 bytes 50281d94
- 004ec8f4 ["INT_ADD", "register:40f0:8", ["const:4ec8f4:8", "const:4:8"]]
- 004ec8f4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0050f78c ["INT_ADD", "register:40f0:8", ["const:50f78c:8", "const:4:8"]]
+ 0050f78c ["CALL", null, ["callee:00c57a90:8"]]
- 004ec8f4 bytes d3b91b94
+ 0050f78c bytes c1201d94
- 004ec8f8 ["COPY", "register:4040:8", ["const:2af000:8"]]
+ 0050f790 ["COPY", "register:4040:8", ["const:2c0000:8"]]
- 004ec8f8 bytes 08eefff0
+ 0050f790 bytes 88edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1707d32afce3e98928b0e22cb830ae6"></a>

### [`004eca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004eca70.md) → [`0050f908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f908.md) _ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdced0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdced0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c59920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59920.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

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
      "definition_site": "0050f96c",
      "incomplete_value": false,
      "site": "0050f974",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ecad4",
      "incomplete_value": false,
      "site": "004ecadc",
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
            "const:4df:8"
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
      "definition_site": "0050f9a8",
      "incomplete_value": true,
      "site": "0050f9b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ecb10",
      "incomplete_value": true,
      "site": "004ecb1c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f58:8"
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
      "definition_site": "0050f9a4",
      "incomplete_value": false,
      "site": "0050f9b4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004ecb0c",
      "incomplete_value": false,
      "site": "004ecb1c",
      "value": [
        "leaf",
        "const:512990:8"
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
      "0050f96c",
      "PARAM",
      [
        "storage",
        "002a24df",
        null,
        "string"
      ]
    ],
    [
      "0050f9a4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "0050f9a8",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050f96c",
      "PARAM",
      [
        "storage",
        "002b2ba0",
        null,
        "string"
      ]
    ],
    [
      "0050f9a4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0050f9a8",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ecadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004eca70.md#insn-004ecadc) · [`004ecb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004eca70.md#insn-004ecb1c) · [`004ecac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004eca70.md#insn-004ecac8)
- 新版 [`0050f974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f908.md#insn-0050f974) · [`0050f9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f908.md#insn-0050f9b4) · [`0050f960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f908.md#insn-0050f960)

~~~diff
- 004ecadc ["INT_ADD", "register:40f0:8", ["const:4ecadc:8", "const:4:8"]]
- 004ecadc ["CALL", null, ["callee:0043dd98:8"]]
+ 0050f974 ["INT_ADD", "register:40f0:8", ["const:50f974:8", "const:4:8"]]
+ 0050f974 ["CALL", null, ["callee:0043dd98:8"]]
- 004ecadc bytes efb9fc97
+ 0050f974 bytes 09b9fc97
- 004ecb1c ["INT_ADD", "register:40f0:8", ["const:4ecb1c:8", "const:4:8"]]
- 004ecb1c ["CALL", null, ["callee:00c57b10:8"]]
+ 0050f9b4 ["INT_ADD", "register:40f0:8", ["const:50f9b4:8", "const:4:8"]]
+ 0050f9b4 ["CALL", null, ["callee:00c57b10:8"]]
- 004ecb1c bytes 69b91b94
+ 0050f9b4 bytes 57201d94
- 004ecac8 ["INT_ADD", "register:40f0:8", ["const:4ecac8:8", "const:4:8"]]
- 004ecac8 ["CALL", null, ["callee:00c57af0:8"]]
+ 0050f960 ["INT_ADD", "register:40f0:8", ["const:50f960:8", "const:4:8"]]
+ 0050f960 ["CALL", null, ["callee:00c57af0:8"]]
- 004ecac8 bytes 76b91b94
+ 0050f960 bytes 64201d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71fa2a326d83a1e52099184ef3cca730"></a>

### [`004ecb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ecb70.md) → [`0050fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md) _ZN5Botan7X509_CAC2ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEEERNS_21Ra

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`004ed050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed050.md) [`004ed188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed188.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0050fee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fee8.md) [`00510020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.38% / 新版 97.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050fa50",
      "incomplete_value": true,
      "site": "0050fa50",
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
      "definition_site": "004ecbb8",
      "incomplete_value": true,
      "site": "004ecbb8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050fa8c",
      "incomplete_value": true,
      "site": "0050fa90",
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
      "definition_site": "004ecbf4",
      "incomplete_value": true,
      "site": "004ecbf8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050fba8",
      "incomplete_value": false,
      "site": "0050fbb4",
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
            "const:c4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ecd10",
      "incomplete_value": false,
      "site": "004ecd1c",
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
            "const:692:8"
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
      "0050fa34",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0050fa50",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050fa88",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050fa34",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0050fa50",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050fa88",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ecd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ecb70.md#insn-004ecd1c) · [`004ecec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ecb70.md#insn-004ecec0) · [`004ecefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ecb70.md#insn-004ecefc)
- 新版 [`0050fbb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md#insn-0050fbb4) · [`0050fd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md#insn-0050fd58) · [`0050fd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md#insn-0050fd94)

~~~diff
- 004ecd1c ["INT_ADD", "register:40f0:8", ["const:4ecd1c:8", "const:4:8"]]
- 004ecd1c ["CALL", null, ["callee:0050fee8:8"]]
+ 0050fbb4 ["INT_ADD", "register:40f0:8", ["const:50fbb4:8", "const:4:8"]]
+ 0050fbb4 ["CALL", null, ["callee:0050fee8:8"]]
- 004ecd1c bytes cd000094
+ 0050fbb4 bytes cd000094
- 004ecec0 ["INT_ADD", "register:40f0:8", ["const:4ecec0:8", "const:4:8"]]
- 004ecec0 ["CALL", null, ["callee:0043dd98:8"]]
+ 0050fd58 ["INT_ADD", "register:40f0:8", ["const:50fd58:8", "const:4:8"]]
+ 0050fd58 ["CALL", null, ["callee:0043dd98:8"]]
- 004ecec0 bytes f6b8fc97
+ 0050fd58 bytes 10b8fc97
- 004ecefc ["INT_ADD", "register:40f0:8", ["const:4ecefc:8", "const:4:8"]]
- 004ecefc ["CALL", null, ["callee:00c57b10:8"]]
+ 0050fd94 ["INT_ADD", "register:40f0:8", ["const:50fd94:8", "const:4:8"]]
+ 0050fd94 ["CALL", null, ["callee:00c57b10:8"]]
- 004ecefc bytes 71b81b94
+ 0050fd94 bytes 5f1f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d7e3b8c29effe298bc2cac367f00a42"></a>

### [`004ed188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed188.md) → [`00510020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md) FUN_00510020

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`004ecb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ec/004ecb70.md) [`004edb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004edb24.md) [`004ef8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef8d4.md) [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 16件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 5件 [`0050fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md) [`005109bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/005109bc.md) [`0051276c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051276c.md) [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 16件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.31% / 新版 97.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00510188",
      "incomplete_value": false,
      "site": "00510194",
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
            "const:389:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ed2f0",
      "incomplete_value": false,
      "site": "004ed2fc",
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
            "const:6e6:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005101c8",
      "incomplete_value": true,
      "site": "005101d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ed330",
      "incomplete_value": true,
      "site": "004ed33c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005101c4",
      "incomplete_value": false,
      "site": "005101d4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004ed32c",
      "incomplete_value": false,
      "site": "004ed33c",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00510188",
      "PARAM",
      [
        "storage",
        "002a96e6",
        null,
        "string"
      ]
    ],
    [
      "005101c4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "005101c8",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00510188",
      "PARAM",
      [
        "storage",
        "002ba389",
        null,
        "string"
      ]
    ],
    [
      "005101c4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005101c8",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ed2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed188.md#insn-004ed2fc) · [`004ed33c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed188.md#insn-004ed33c) · [`004ed388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed188.md#insn-004ed388)
- 新版 [`00510194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md#insn-00510194) · [`005101d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md#insn-005101d4) · [`00510220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md#insn-00510220)

~~~diff
- 004ed2fc ["INT_ADD", "register:40f0:8", ["const:4ed2fc:8", "const:4:8"]]
- 004ed2fc ["CALL", null, ["callee:00c57cb0:8"]]
+ 00510194 ["INT_ADD", "register:40f0:8", ["const:510194:8", "const:4:8"]]
+ 00510194 ["CALL", null, ["callee:00c57cb0:8"]]
- 004ed2fc bytes d9b71b94
+ 00510194 bytes c71e1d94
- 004ed33c ["INT_ADD", "register:40f0:8", ["const:4ed33c:8", "const:4:8"]]
- 004ed33c ["CALL", null, ["callee:00c57b10:8"]]
+ 005101d4 ["INT_ADD", "register:40f0:8", ["const:5101d4:8", "const:4:8"]]
+ 005101d4 ["CALL", null, ["callee:00c57b10:8"]]
- 004ed33c bytes 61b71b94
+ 005101d4 bytes 4f1e1d94
- 004ed388 ["INT_ADD", "register:40f0:8", ["const:4ed388:8", "const:4:8"]]
- 004ed388 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00510220 ["INT_ADD", "register:40f0:8", ["const:510220:8", "const:4:8"]]
+ 00510220 ["CALL", null, ["callee:00c57cb0:8"]]
- 004ed388 bytes b6b71b94
+ 00510220 bytes a41e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2227d8a1513942e55c990942735bede7"></a>

### [`004edb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004edb24.md) → [`005109bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/005109bc.md) _ZN5Botan7X509_CAC1ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk13mapINS7_12basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004ed188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ed188.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00518128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518128.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00510020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00510a08",
      "incomplete_value": true,
      "site": "00510a08",
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
      "definition_site": "004edb70",
      "incomplete_value": true,
      "site": "004edb70",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00510a44",
      "incomplete_value": true,
      "site": "00510a48",
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
      "definition_site": "004edbac",
      "incomplete_value": true,
      "site": "004edbb0",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00510b18",
      "incomplete_value": false,
      "site": "00510b20",
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
            "const:fbd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004edc80",
      "incomplete_value": false,
      "site": "004edc88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:28f000:8"
          ],
          [
            "leaf",
            "const:b7d:8"
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
      "005109e8",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "00510a08",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00510a40",
      "READ",
      [
        "storage",
        "00c1b2f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005109e8",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00510a08",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00510a40",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004edc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004edb24.md#insn-004edc88) · [`004edcc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004edb24.md#insn-004edcc4) · [`004edb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004edb24.md#insn-004edb44)
- 新版 [`00510b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/005109bc.md#insn-00510b20) · [`00510b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/005109bc.md#insn-00510b5c) · [`005109dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/005109bc.md#insn-005109dc)

~~~diff
- 004edc88 ["INT_ADD", "register:40f0:8", ["const:4edc88:8", "const:4:8"]]
- 004edc88 ["CALL", null, ["callee:0043dd98:8"]]
+ 00510b20 ["INT_ADD", "register:40f0:8", ["const:510b20:8", "const:4:8"]]
+ 00510b20 ["CALL", null, ["callee:0043dd98:8"]]
- 004edc88 bytes 84b5fc97
+ 00510b20 bytes 9eb4fc97
- 004edcc4 ["INT_ADD", "register:40f0:8", ["const:4edcc4:8", "const:4:8"]]
- 004edcc4 ["CALL", null, ["callee:00c57b10:8"]]
+ 00510b5c ["INT_ADD", "register:40f0:8", ["const:510b5c:8", "const:4:8"]]
+ 00510b5c ["CALL", null, ["callee:00c57b10:8"]]
- 004edcc4 bytes ffb41b94
+ 00510b5c bytes ed1b1d94
- 004edb44 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 005109dc ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004edb44 bytes 693900b0
+ 005109dc bytes 493c00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41f61c3e6703d028ec11a00ec3ee753c"></a>

### [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) → [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) _ZNK5Botan7X509_CA12sign_requestERKNS_14PKCS10_RequestERNS_21RandomNumberGeneratorERKNS_9X509_TimeES8_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`004e8484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e8/004e8484.md) [`004ee34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee34c.md) [`004ee760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee760.md) [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0050b31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b31c.md) [`005111e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md) [`005115f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005115f8.md) [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00510e04",
      "incomplete_value": true,
      "site": "00510e08",
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
      "definition_site": "004edf6c",
      "incomplete_value": true,
      "site": "004edf70",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00510e38",
      "incomplete_value": true,
      "site": "00510e3c",
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
      "definition_site": "004edfa0",
      "incomplete_value": true,
      "site": "004edfa4",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00510e78",
      "incomplete_value": true,
      "site": "00510e84",
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
      "definition_site": "004edfe0",
      "incomplete_value": true,
      "site": "004edfec",
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
      "00510df8",
      "READ",
      [
        "storage",
        "00c1b398",
        null,
        "pointer"
      ]
    ],
    [
      "00510e08",
      "DATA",
      [
        "storage",
        "00bea990",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00510e30",
      "READ",
      [
        "storage",
        "00c1b388",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00510df8",
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ],
    [
      "00510e08",
      "DATA",
      [
        "storage",
        "00c67550",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00510e30",
      "READ",
      [
        "storage",
        "00c9ad78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004edecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md#insn-004edecc) · [`004edee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md#insn-004edee4) · [`004edef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md#insn-004edef0)
- 新版 [`00510d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md#insn-00510d64) · [`00510d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md#insn-00510d7c) · [`00510d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md#insn-00510d88)

~~~diff
- 004edecc ["INT_ADD", "register:40f0:8", ["const:4edecc:8", "const:4:8"]]
- 004edecc ["CALL", null, ["callee:00c59900:8"]]
+ 00510d64 ["INT_ADD", "register:40f0:8", ["const:510d64:8", "const:4:8"]]
+ 00510d64 ["CALL", null, ["callee:00c59900:8"]]
- 004edecc bytes f9bb1b94
+ 00510d64 bytes e7221d94
- 004edee4 ["INT_ADD", "register:40f0:8", ["const:4edee4:8", "const:4:8"]]
- 004edee4 ["CALL", null, ["callee:00c59890:8"]]
+ 00510d7c ["INT_ADD", "register:40f0:8", ["const:510d7c:8", "const:4:8"]]
+ 00510d7c ["CALL", null, ["callee:00c59890:8"]]
- 004edee4 bytes d7bb1b94
+ 00510d7c bytes c5221d94
- 004edef0 ["INT_ADD", "register:40f0:8", ["const:4edef0:8", "const:4:8"]]
- 004edef0 ["CALL", null, ["callee:00c598d0:8"]]
+ 00510d88 ["INT_ADD", "register:40f0:8", ["const:510d88:8", "const:4:8"]]
+ 00510d88 ["CALL", null, ["callee:00c598d0:8"]]
- 004edef0 bytes e4bb1b94
+ 00510d88 bytes d2221d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f117a64856b8f57cd81fa0a057b889e8"></a>

### [`004ee34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee34c.md) → [`005111e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md) FUN_005111e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) [`00503af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503af8.md) [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 7件 [`00519534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519534.md) [`0051bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bf98.md) [`0051c12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c12c.md) [`0051d7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d7fc.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 4件 [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) [`00526990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md) [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 7件 [`0053c3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c3cc.md) [`0053ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) [`0053efc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`00540694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00511228",
      "incomplete_value": true,
      "site": "0051123c",
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
      "definition_site": "004ee390",
      "incomplete_value": true,
      "site": "004ee3a4",
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
      "00511218",
      "READ",
      [
        "storage",
        "00c1b320",
        null,
        "pointer"
      ]
    ],
    [
      "0051123c",
      "DATA",
      [
        "storage",
        "00beb900",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00511218",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "0051123c",
      "DATA",
      [
        "storage",
        "00c684c0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee34c.md#insn-004ee370) · [`004ee380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee34c.md#insn-004ee380) · [`004ee3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee34c.md#insn-004ee3c0)
- 新版 [`00511208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md#insn-00511208) · [`00511218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md#insn-00511218) · [`00511258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md#insn-00511258)

~~~diff
- 004ee370 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 00511208 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004ee370 bytes 693900b0
+ 00511208 bytes 493c00b0
- 004ee380 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:320:8"]]
- 004ee380 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511218 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d10:8"]]
+ 00511218 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ee380 bytes 299141f9
+ 00511218 bytes 298946f9
- 004ee3c0 ["INT_ADD", "register:40f0:8", ["const:4ee3c0:8", "const:4:8"]]
- 004ee3c0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00511258 ["INT_ADD", "register:40f0:8", ["const:511258:8", "const:4:8"]]
+ 00511258 ["CALL", null, ["callee:00c57a90:8"]]
- 004ee3c0 bytes 20b31b94
+ 00511258 bytes 0e1a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea3ba765cd15d226721807c4d5461f6d"></a>

### [`004ee4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md) → [`0051138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md) _ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcee0.md) · 呼出先 13件 [`004f3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3cec.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`0051a850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a850.md) [`00528a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a6c.md) [`00528d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528d24.md)
- 新版 呼出元 1件 [`00c59930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59930.md) · 呼出先 13件 [`00516b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516b84.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0053d6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d6e8.md) [`0054b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md) [`0054bbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bbbc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.83% / 新版 97.83%

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
      "definition_site": "00511420",
      "incomplete_value": true,
      "site": "00511420",
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
      "definition_site": "004ee588",
      "incomplete_value": true,
      "site": "004ee588",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00511464",
      "incomplete_value": true,
      "site": "00511468",
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
      "definition_site": "004ee5cc",
      "incomplete_value": true,
      "site": "004ee5d0",
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
      "00511410",
      "READ",
      [
        "storage",
        "00c1b330",
        null,
        "pointer"
      ]
    ],
    [
      "00511420",
      "DATA",
      [
        "storage",
        "00bed478",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00511458",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00511410",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "00511420",
      "DATA",
      [
        "storage",
        "00c6a038",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00511458",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md#insn-004ee534) · [`004ee540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md#insn-004ee540) · [`004ee550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md#insn-004ee550)
- 新版 [`005113cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md#insn-005113cc) · [`005113d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md#insn-005113d8) · [`005113e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md#insn-005113e8)

~~~diff
- 004ee534 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ee534 ["INT_ADD", "register:40f0:8", ["const:4ee534:8", "const:4:8"]]
- 004ee534 ["CALLIND", null, ["register:0:8"]]
+ 005113cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005113cc ["INT_ADD", "register:40f0:8", ["const:5113cc:8", "const:4:8"]]
+ 005113cc ["CALLIND", null, ["register:0:8"]]
- 004ee534 bytes 20013fd6
+ 005113cc bytes 20013fd6
- 004ee540 ["INT_ADD", "register:40f0:8", ["const:4ee540:8", "const:4:8"]]
- 004ee540 ["CALL", null, ["callee:0054bed4:8"]]
+ 005113d8 ["INT_ADD", "register:40f0:8", ["const:5113d8:8", "const:4:8"]]
+ 005113d8 ["CALL", null, ["callee:0054bed4:8"]]
- 004ee540 bytes bfea0094
+ 005113d8 bytes bfea0094
- 004ee550 ["INT_ADD", "register:40f0:8", ["const:4ee550:8", "const:4:8"]]
- 004ee550 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005113e8 ["INT_ADD", "register:40f0:8", ["const:5113e8:8", "const:4:8"]]
+ 005113e8 ["CALL", null, ["callee:00c57ab0:8"]]
- 004ee550 bytes c4b21b94
+ 005113e8 bytes b2191d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-489ea2a74b31225cefad05e8bb89709f"></a>

### [`004ee7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee7d8.md) → [`00511670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511670.md) _ZN5Botan7X509_CA9make_certEPNS_9PK_SignerERNS_21RandomNumberGeneratorERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS8_9allocatorIhEEEER

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf00.md) · 呼出先 16件 [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c59950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59950.md) · 呼出先 16件 [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.50% / 新版 95.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005116d0",
      "value": [
        "leaf",
        "ram:c58f50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ee838",
      "value": [
        "leaf",
        "ram:bdc500:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00511744",
      "incomplete_value": true,
      "site": "00511744",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:338:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ee8ac",
      "incomplete_value": true,
      "site": "004ee8ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005118d8",
      "value": [
        "leaf",
        "ram:c597c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004eea40",
      "value": [
        "leaf",
        "ram:bdcd70:8"
      ]
    },
    "ordinal": 27,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005116d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc500"
      ]
    ],
    [
      "00511734",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "005118d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcd70"
      ]
    ]
  ],
  "added": [
    [
      "005116d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58f50"
      ]
    ],
    [
      "00511734",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "005118d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c597c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee7d8.md#insn-004ee838) · [`004ee8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee7d8.md#insn-004ee8ac) · [`004eea40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee7d8.md#insn-004eea40)
- 新版 [`005116d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511670.md#insn-005116d0) · [`00511744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511670.md#insn-00511744) · [`005118d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511670.md#insn-005118d8)

~~~diff
- 004ee838 ["INT_ADD", "register:40f0:8", ["const:4ee838:8", "const:4:8"]]
- 004ee838 ["CALL", null, ["ram:bdc500:8"]]
+ 005116d0 ["INT_ADD", "register:40f0:8", ["const:5116d0:8", "const:4:8"]]
+ 005116d0 ["CALL", null, ["ram:c58f50:8"]]
- 004ee838 bytes 32b71b94
+ 005116d0 bytes 201e1d94
- 004ee8ac ["COPY", "register:0:8", ["register:4048:8"]]
- 004ee8ac ["INT_ADD", "register:40f0:8", ["const:4ee8ac:8", "const:4:8"]]
- 004ee8ac ["CALLIND", null, ["register:0:8"]]
+ 00511744 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00511744 ["INT_ADD", "register:40f0:8", ["const:511744:8", "const:4:8"]]
+ 00511744 ["CALLIND", null, ["register:0:8"]]
- 004ee8ac bytes 20013fd6
+ 00511744 bytes 20013fd6
- 004eea40 ["INT_ADD", "register:40f0:8", ["const:4eea40:8", "const:4:8"]]
- 004eea40 ["CALL", null, ["ram:bdcd70:8"]]
+ 005118d8 ["INT_ADD", "register:40f0:8", ["const:5118d8:8", "const:4:8"]]
+ 005118d8 ["CALL", null, ["ram:c597c0:8"]]
- 004eea40 bytes ccb81b94
+ 005118d8 bytes ba1f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9d7c10cdc5b2cf907d530737bd98d14"></a>

### [`004ef204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef204.md) → [`0051209c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051209c.md) _ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf20.md) · 呼出先 21件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`004f43b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f43b8.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c59970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59970.md) · 呼出先 21件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00517250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517250.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.17% / 新版 94.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005120f0",
      "incomplete_value": true,
      "site": "005120f0",
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
      "definition_site": "004ef258",
      "incomplete_value": true,
      "site": "004ef258",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512140",
      "incomplete_value": true,
      "site": "0051214c",
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
      "definition_site": "004ef2a8",
      "incomplete_value": true,
      "site": "004ef2b4",
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005121b0",
      "incomplete_value": true,
      "site": "005121b4",
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
      "definition_site": "004ef318",
      "incomplete_value": true,
      "site": "004ef31c",
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
      "005120d8",
      "READ",
      [
        "storage",
        "00c1b320",
        null,
        "pointer"
      ]
    ],
    [
      "005120f0",
      "DATA",
      [
        "storage",
        "00beb900",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00512130",
      "READ",
      [
        "storage",
        "00c1b3a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005120d8",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "005120f0",
      "DATA",
      [
        "storage",
        "00c684c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00512130",
      "READ",
      [
        "storage",
        "00c9ad90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ef390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef204.md#insn-004ef390) · [`004ef52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef204.md#insn-004ef52c) · [`004ef598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004ef204.md#insn-004ef598)
- 新版 [`00512228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051209c.md#insn-00512228) · [`005123c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051209c.md#insn-005123c4) · [`00512430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051209c.md#insn-00512430)

~~~diff
- 004ef390 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ef390 ["INT_ADD", "register:40f0:8", ["const:4ef390:8", "const:4:8"]]
- 004ef390 ["CALLIND", null, ["register:0:8"]]
+ 00512228 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00512228 ["INT_ADD", "register:40f0:8", ["const:512228:8", "const:4:8"]]
+ 00512228 ["CALLIND", null, ["register:0:8"]]
- 004ef390 bytes 20013fd6
+ 00512228 bytes 20013fd6
- 004ef52c ["COPY", "register:0:8", ["register:4048:8"]]
- 004ef52c ["INT_ADD", "register:40f0:8", ["const:4ef52c:8", "const:4:8"]]
- 004ef52c ["CALLIND", null, ["register:0:8"]]
+ 005123c4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005123c4 ["INT_ADD", "register:40f0:8", ["const:5123c4:8", "const:4:8"]]
+ 005123c4 ["CALLIND", null, ["register:0:8"]]
- 004ef52c bytes 20013fd6
+ 005123c4 bytes 20013fd6
- 004ef598 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ef598 ["INT_ADD", "register:40f0:8", ["const:4ef598:8", "const:4:8"]]
- 004ef598 ["CALLIND", null, ["register:0:8"]]
+ 00512430 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00512430 ["INT_ADD", "register:40f0:8", ["const:512430:8", "const:4:8"]]
+ 00512430 ["CALLIND", null, ["register:0:8"]]
- 004ef598 bytes 20013fd6
+ 00512430 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b343573e12a4637a354353a8a74a7bd"></a>

### [`004efa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efa38.md) → [`005128d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005128d0.md) _ZN5Botan8X509_CRLC1ERNS_10DataSourceE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) [`00bdce30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) [`00c59880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59880.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512910",
      "incomplete_value": true,
      "site": "00512910",
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
      "definition_site": "004efa78",
      "incomplete_value": true,
      "site": "004efa78",
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
      "definition_site": "00512910",
      "incomplete_value": true,
      "site": "00512910",
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
      "definition_site": "004efa78",
      "incomplete_value": true,
      "site": "004efa78",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00512950",
      "incomplete_value": true,
      "site": "00512958",
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
      "definition_site": "004efab8",
      "incomplete_value": true,
      "site": "004efac0",
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
      "005128f0",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "005128f8",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "00512910",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "005128f0",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "005128f8",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00512910",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efa50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efa38.md#insn-004efa50) · [`004efa54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efa38.md#insn-004efa54) · [`004efa58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efa38.md#insn-004efa58)
- 新版 [`005128e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005128d0.md#insn-005128e8) · [`005128ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005128d0.md#insn-005128ec) · [`005128f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005128d0.md#insn-005128f0)

~~~diff
- 004efa50 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 005128e8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004efa50 bytes 68390090
+ 005128e8 bytes 483c0090
- 004efa54 ["COPY", "register:4050:8", ["const:c1a000:8"]]
+ 005128ec ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 004efa54 bytes 4a3900f0
+ 005128ec bytes 4a3c0090
- 004efa58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
- 004efa58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005128f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 005128f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efa58 bytes 08b541f9
+ 005128f0 bytes 08ad46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86222cecbdc486844e3b285f8512c2f0"></a>

### [`004efb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efb8c.md) → [`00512a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512a24.md) _ZN5Botan8X509_CRLC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf40.md) · 呼出先 7件 [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 1件 [`00c59990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59990.md) · 呼出先 7件 [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512a64",
      "incomplete_value": true,
      "site": "00512a64",
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
      "definition_site": "004efbcc",
      "incomplete_value": true,
      "site": "004efbcc",
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
      "definition_site": "00512a64",
      "incomplete_value": true,
      "site": "00512a64",
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
      "definition_site": "004efbcc",
      "incomplete_value": true,
      "site": "004efbcc",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00512aac",
      "incomplete_value": true,
      "site": "00512ab8",
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
      "definition_site": "004efc14",
      "incomplete_value": true,
      "site": "004efc20",
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
      "00512a44",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "00512a4c",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "00512a64",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512a44",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00512a4c",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00512a64",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efc78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efb8c.md#insn-004efc78) · [`004efba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efb8c.md#insn-004efba4) · [`004efba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efb8c.md#insn-004efba8)
- 新版 [`00512b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512a24.md#insn-00512b10) · [`00512a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512a24.md#insn-00512a3c) · [`00512a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512a24.md#insn-00512a40)

~~~diff
- 004efc78 ["COPY", "register:0:8", ["register:4048:8"]]
- 004efc78 ["INT_ADD", "register:40f0:8", ["const:4efc78:8", "const:4:8"]]
- 004efc78 ["CALLIND", null, ["register:0:8"]]
+ 00512b10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00512b10 ["INT_ADD", "register:40f0:8", ["const:512b10:8", "const:4:8"]]
+ 00512b10 ["CALLIND", null, ["register:0:8"]]
- 004efc78 bytes 20013fd6
+ 00512b10 bytes 20013fd6
- 004efba4 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00512a3c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004efba4 bytes 68390090
+ 00512a3c bytes 483c0090
- 004efba8 ["COPY", "register:4050:8", ["const:c1a000:8"]]
+ 00512a40 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 004efba8 bytes 4a3900f0
+ 00512a40 bytes 4a3c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24bfb4623a4a855d50ad6c9ea6a86f99"></a>

### [`004efd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efd04.md) → [`00512b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512b9c.md) _ZN5Botan8X509_CRLC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) [`00bdc810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc810.md) [`00bdc820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc820.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512bdc",
      "incomplete_value": true,
      "site": "00512bdc",
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
      "definition_site": "004efd44",
      "incomplete_value": true,
      "site": "004efd44",
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
      "definition_site": "00512bdc",
      "incomplete_value": true,
      "site": "00512bdc",
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
      "definition_site": "004efd44",
      "incomplete_value": true,
      "site": "004efd44",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00512c1c",
      "incomplete_value": true,
      "site": "00512c24",
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
      "definition_site": "004efd84",
      "incomplete_value": true,
      "site": "004efd8c",
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
      "00512bbc",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "00512bc4",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "00512bdc",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512bbc",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00512bc4",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00512bdc",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efd04.md#insn-004efdb0) · [`004efd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efd04.md#insn-004efd1c) · [`004efd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efd04.md#insn-004efd20)
- 新版 [`00512c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512b9c.md#insn-00512c48) · [`00512bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512b9c.md#insn-00512bb4) · [`00512bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512b9c.md#insn-00512bb8)

~~~diff
- 004efdb0 ["INT_ADD", "register:40f0:8", ["const:4efdb0:8", "const:4:8"]]
- 004efdb0 ["CALL", null, ["ram:bdc820:8"]]
+ 00512c48 ["INT_ADD", "register:40f0:8", ["const:512c48:8", "const:4:8"]]
+ 00512c48 ["CALL", null, ["ram:c59270:8"]]
- 004efdb0 bytes 9cb21b94
+ 00512c48 bytes 8a191d94
- 004efd1c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00512bb4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004efd1c bytes 68390090
+ 00512bb4 bytes 483c0090
- 004efd20 ["COPY", "register:4050:8", ["const:c1a000:8"]]
+ 00512bb8 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 004efd20 bytes 4a3900f0
+ 00512bb8 bytes 4a3c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98c77f4b96e9c28288c0c6ab12b0f059"></a>

### [`004efe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efe30.md) → [`00512cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md) _ZN5Botan8X509_CRLC1ERKNS_7X509_DNERKNS_9X509_TimeES6_RKNSt6__ndk16vectorINS_9CRL_EntryENS7_9allocatorIS9_EEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00518ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518ea0.md) [`00525f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md) [`00527c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527c8c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053bd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md) [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) [`0054ab24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054ab24.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.61% / 新版 85.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512d3c",
      "incomplete_value": true,
      "site": "00512d3c",
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
      "definition_site": "004efea4",
      "incomplete_value": true,
      "site": "004efea4",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512d3c",
      "incomplete_value": true,
      "site": "00512d3c",
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
      "definition_site": "004efea4",
      "incomplete_value": true,
      "site": "004efea4",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512d78",
      "incomplete_value": true,
      "site": "00512d80",
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
      "definition_site": "004efee0",
      "incomplete_value": true,
      "site": "004efee8",
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
      "00512d24",
      "READ",
      [
        "storage",
        "00c1b368",
        null,
        "pointer"
      ]
    ],
    [
      "00512d28",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "00512d3c",
      "DATA",
      [
        "storage",
        "00beca60",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512d24",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00512d28",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00512d3c",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efe58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efe30.md#insn-004efe58) · [`004efe78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efe30.md#insn-004efe78) · [`004efe8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efe30.md#insn-004efe8c)
- 新版 [`00512cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md#insn-00512cf0) · [`00512d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md#insn-00512d10) · [`00512d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md#insn-00512d24)

~~~diff
- 004efe58 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 00512cf0 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004efe58 bytes 493900f0
+ 00512cf0 bytes 493c0090
- 004efe78 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00512d10 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004efe78 bytes 68390090
+ 00512d10 bytes 483c0090
- 004efe8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
- 004efe8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512d24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 00512d24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004efe8c bytes 08b541f9
+ 00512d24 bytes 08ad46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a2471165151ec81be26a7df86211db2"></a>

### [`004f03d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f03d8.md) → [`00513270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md) _ZN5Botan8X509_CRL12force_decodeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 42件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md)
- 新版 呼出元 0件  · 呼出先 42件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.27% / 新版 90.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 9件, `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005132d0",
      "incomplete_value": true,
      "site": "005132d0",
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
      "definition_site": "004f0438",
      "incomplete_value": true,
      "site": "004f0438",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005132f0",
      "incomplete_value": true,
      "site": "005132f0",
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
      "definition_site": "004f0458",
      "incomplete_value": true,
      "site": "004f0458",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005132f8",
      "incomplete_value": true,
      "site": "005132f8",
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
      "definition_site": "004f0460",
      "incomplete_value": true,
      "site": "004f0460",
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
      "005132b4",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "005132d0",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005132dc",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005132b4",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "005132d0",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005132dc",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f04b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f03d8.md#insn-004f04b4) · [`004f05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f03d8.md#insn-004f05ac) · [`004f06b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f03d8.md#insn-004f06b4)
- 新版 [`0051334c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md#insn-0051334c) · [`00513444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md#insn-00513444) · [`0051354c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md#insn-0051354c)

~~~diff
- 004f04b4 ["INT_ADD", "register:40f0:8", ["const:4f04b4:8", "const:4:8"]]
- 004f04b4 ["CALL", null, ["ram:bdba30:8"]]
+ 0051334c ["INT_ADD", "register:40f0:8", ["const:51334c:8", "const:4:8"]]
+ 0051334c ["CALL", null, ["ram:c58480:8"]]
- 004f04b4 bytes 5fad1b94
+ 0051334c bytes 4d141d94
- 004f05ac ["INT_ADD", "register:40f0:8", ["const:4f05ac:8", "const:4:8"]]
- 004f05ac ["CALL", null, ["ram:bdba40:8"]]
+ 00513444 ["INT_ADD", "register:40f0:8", ["const:513444:8", "const:4:8"]]
+ 00513444 ["CALL", null, ["ram:c58490:8"]]
- 004f05ac bytes 25ad1b94
+ 00513444 bytes 13141d94
- 004f06b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f06b4 ["INT_ADD", "register:40f0:8", ["const:4f06b4:8", "const:4:8"]]
- 004f06b4 ["CALLIND", null, ["register:0:8"]]
+ 0051354c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051354c ["INT_ADD", "register:40f0:8", ["const:51354c:8", "const:4:8"]]
+ 0051354c ["CALLIND", null, ["register:0:8"]]
- 004f06b4 bytes 20013fd6
+ 0051354c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-311513825b06e87a085e295a939e90e5"></a>

### [`004f0f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f0f78.md) → [`00513e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513e10.md) _ZNK5Botan8X509_CRL4dataEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc00.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "definition_site": "00513e70",
      "incomplete_value": false,
      "site": "00513e78",
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
            "const:dd3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f0fd8",
      "incomplete_value": false,
      "site": "004f0fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:aad:8"
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
      "definition_site": "00513eac",
      "incomplete_value": true,
      "site": "00513eb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004f1014",
      "incomplete_value": true,
      "site": "004f1020",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:f58:8"
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
      "definition_site": "00513ea8",
      "incomplete_value": false,
      "site": "00513eb8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004f1010",
      "incomplete_value": false,
      "site": "004f1020",
      "value": [
        "leaf",
        "const:512990:8"
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
      "00513e70",
      "PARAM",
      [
        "storage",
        "002adaad",
        null,
        "string"
      ]
    ],
    [
      "00513ea8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "00513eac",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00513e70",
      "PARAM",
      [
        "storage",
        "002bedd3",
        null,
        "string"
      ]
    ],
    [
      "00513ea8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00513eac",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f0fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f0f78.md#insn-004f0fe0) · [`004f1020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f0f78.md#insn-004f1020) · [`004f0fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f0/004f0f78.md#insn-004f0fcc)
- 新版 [`00513e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513e10.md#insn-00513e78) · [`00513eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513e10.md#insn-00513eb8) · [`00513e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513e10.md#insn-00513e64)

~~~diff
- 004f0fe0 ["INT_ADD", "register:40f0:8", ["const:4f0fe0:8", "const:4:8"]]
- 004f0fe0 ["CALL", null, ["callee:0043dd98:8"]]
+ 00513e78 ["INT_ADD", "register:40f0:8", ["const:513e78:8", "const:4:8"]]
+ 00513e78 ["CALL", null, ["callee:0043dd98:8"]]
- 004f0fe0 bytes aea8fc97
+ 00513e78 bytes c8a7fc97
- 004f1020 ["INT_ADD", "register:40f0:8", ["const:4f1020:8", "const:4:8"]]
- 004f1020 ["CALL", null, ["callee:00c57b10:8"]]
+ 00513eb8 ["INT_ADD", "register:40f0:8", ["const:513eb8:8", "const:4:8"]]
+ 00513eb8 ["CALL", null, ["callee:00c57b10:8"]]
- 004f1020 bytes 28a81b94
+ 00513eb8 bytes 160f1d94
- 004f0fcc ["INT_ADD", "register:40f0:8", ["const:4f0fcc:8", "const:4:8"]]
- 004f0fcc ["CALL", null, ["callee:00c57af0:8"]]
+ 00513e64 ["INT_ADD", "register:40f0:8", ["const:513e64:8", "const:4:8"]]
+ 00513e64 ["CALL", null, ["callee:00c57af0:8"]]
- 004f0fcc bytes 35a81b94
+ 00513e64 bytes 230f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b90527b8637d238651383038e278e0c"></a>

### [`004f10f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f10f4.md) → [`00513f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f8c.md) _ZN5Botan7X509_DNC2ERKNSt6__ndk18multimapINS_3OIDENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_4lessIS3_EENS7_INS1_4pair

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdccb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59700.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00513fd4",
      "incomplete_value": true,
      "site": "00513fdc",
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
      "definition_site": "004f113c",
      "incomplete_value": true,
      "site": "004f1144",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00513fc8",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "00513fdc",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00513fc8",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "00513fdc",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f10f4.md#insn-004f1118) · [`004f1130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f10f4.md#insn-004f1130) · [`004f116c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f10f4.md#insn-004f116c)
- 新版 [`00513fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f8c.md#insn-00513fb0) · [`00513fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f8c.md#insn-00513fc8) · [`00514004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f8c.md#insn-00514004)

~~~diff
- 004f1118 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00513fb0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004f1118 bytes 483900d0
+ 00513fb0 bytes 283c00f0
- 004f1130 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 004f1130 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00513fc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
+ 00513fc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f1130 bytes 087141f9
+ 00513fc8 bytes 086946f9
- 004f116c ["INT_ADD", "register:40f0:8", ["const:4f116c:8", "const:4:8"]]
- 004f116c ["CALL", null, ["callee:00c59700:8"]]
+ 00514004 ["INT_ADD", "register:40f0:8", ["const:514004:8", "const:4:8"]]
+ 00514004 ["CALL", null, ["callee:00c59700:8"]]
- 004f116c bytes d1ae1b94
+ 00514004 bytes bf151d94
~~~


<a id="compare-45ae42c2dd0d95b109dda4c0d665d3c1"></a>

### [`004f1394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1394.md) → [`0051422c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051422c.md) _ZN5Botan7X509_DNC1ERKNSt6__ndk18multimapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_NS1_4lessIS8_EENS6_INS1_4pairIKS8_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdccb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c59700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59700.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514288",
      "incomplete_value": true,
      "site": "00514290",
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
      "definition_site": "004f13f0",
      "incomplete_value": true,
      "site": "004f13f8",
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
      "0051427c",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "00514290",
      "DATA",
      [
        "storage",
        "00beaa38",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0051427c",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "00514290",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f13cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1394.md#insn-004f13cc) · [`004f13e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1394.md#insn-004f13e4) · [`004f141c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1394.md#insn-004f141c)
- 新版 [`00514264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051422c.md#insn-00514264) · [`0051427c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051422c.md#insn-0051427c) · [`005142b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051422c.md#insn-005142b4)

~~~diff
- 004f13cc ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00514264 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004f13cc bytes 483900d0
+ 00514264 bytes 283c00d0
- 004f13e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 004f13e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051427c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
+ 0051427c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f13e4 bytes 087141f9
+ 0051427c bytes 086946f9
- 004f141c ["INT_ADD", "register:40f0:8", ["const:4f141c:8", "const:4:8"]]
- 004f141c ["CALL", null, ["callee:00c58280:8"]]
+ 005142b4 ["INT_ADD", "register:40f0:8", ["const:5142b4:8", "const:4:8"]]
+ 005142b4 ["CALL", null, ["callee:00c58280:8"]]
- 004f141c bytes 05a91b94
+ 005142b4 bytes f30f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee1313090f1152ec9cdb4ca63152ef53"></a>

### [`004f1734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1734.md) → [`005145cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005145cc.md) _ZN5Botan7X509_DN16deref_info_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcd20.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md)
- 新版 呼出元 1件 [`00c59770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59770.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.41% / 新版 86.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514750",
      "incomplete_value": true,
      "site": "00514750",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f18b8",
      "incomplete_value": true,
      "site": "004f18b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:56e:8"
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
      "definition_site": "005147ac",
      "incomplete_value": true,
      "site": "005147ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1914",
      "incomplete_value": true,
      "site": "004f1914",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:96d:8"
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
      "definition_site": "005147a0",
      "incomplete_value": true,
      "site": "005147b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004f1908",
      "incomplete_value": true,
      "site": "004f1918",
      "value": [
        "LOAD",
        "8",
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
      "00514720",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ],
    [
      "0051473c",
      "READ",
      [
        "storage",
        "002aa56e",
        null,
        "string"
      ]
    ],
    [
      "00514760",
      "PARAM",
      [
        "storage",
        "002afb2f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00514720",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ],
    [
      "0051473c",
      "READ",
      [
        "storage",
        "002bb2ea",
        null,
        "string"
      ]
    ],
    [
      "00514760",
      "PARAM",
      [
        "storage",
        "002c1153",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1734.md#insn-004f1890) · [`004f18d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1734.md#insn-004f18d0) · [`004f18e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1734.md#insn-004f18e4)
- 新版 [`00514728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005145cc.md#insn-00514728) · [`00514768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005145cc.md#insn-00514768) · [`0051477c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005145cc.md#insn-0051477c)

~~~diff
- 004f1890 ["INT_ADD", "register:40f0:8", ["const:4f1890:8", "const:4:8"]]
- 004f1890 ["CALL", null, ["callee:00441e54:8"]]
+ 00514728 ["INT_ADD", "register:40f0:8", ["const:514728:8", "const:4:8"]]
+ 00514728 ["CALL", null, ["callee:00441e54:8"]]
- 004f1890 bytes b1b6fc97
+ 00514728 bytes cbb5fc97
- 004f18d0 ["INT_ADD", "register:40f0:8", ["const:4f18d0:8", "const:4:8"]]
- 004f18d0 ["CALL", null, ["callee:00441e54:8"]]
+ 00514768 ["INT_ADD", "register:40f0:8", ["const:514768:8", "const:4:8"]]
+ 00514768 ["CALL", null, ["callee:00441e54:8"]]
- 004f18d0 bytes a1b6fc97
+ 00514768 bytes bbb5fc97
- 004f18e4 ["INT_ADD", "register:40f0:8", ["const:4f18e4:8", "const:4:8"]]
- 004f18e4 ["CALL", null, ["callee:00441e54:8"]]
+ 0051477c ["INT_ADD", "register:40f0:8", ["const:51477c:8", "const:4:8"]]
+ 0051477c ["CALL", null, ["callee:00441e54:8"]]
- 004f18e4 bytes 9cb6fc97
+ 0051477c bytes b6b5fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbf24ce55e42a49b09e91b2bb17d11a0"></a>

### [`004f1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1ecc.md) → [`00514d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md) _ZNK5Botan7X509_DN11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004dcbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004dc/004dcbd4.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 11件 [`004f2228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2228.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00526790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526790.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`004ffa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 11件 [`005150c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/005150c0.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00549628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514df4",
      "incomplete_value": true,
      "site": "00514df4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1f5c",
      "incomplete_value": true,
      "site": "004f1f5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:56e:8"
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
      "definition_site": "00514e3c",
      "incomplete_value": true,
      "site": "00514e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1fa4",
      "incomplete_value": true,
      "site": "004f1fa4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:97d:8"
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
      "definition_site": "00514e84",
      "incomplete_value": true,
      "site": "00514e84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
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
      "definition_site": "004f1fec",
      "incomplete_value": true,
      "site": "004f1fec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4f8:8"
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
      "00514de0",
      "READ",
      [
        "storage",
        "002aa56e",
        null,
        "string"
      ]
    ],
    [
      "00514e2c",
      "READ",
      [
        "storage",
        "0029697d",
        null,
        "string"
      ]
    ],
    [
      "00514e74",
      "READ",
      [
        "storage",
        "002a54f8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00514de0",
      "READ",
      [
        "storage",
        "002bb2ea",
        null,
        "string"
      ]
    ],
    [
      "00514e2c",
      "READ",
      [
        "storage",
        "002a64b2",
        null,
        "string"
      ]
    ],
    [
      "00514e74",
      "READ",
      [
        "storage",
        "002b5f26",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1ecc.md#insn-004f1efc) · [`004f1f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1ecc.md#insn-004f1f0c) · [`004f1f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1ecc.md#insn-004f1f34)
- 新版 [`00514d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md#insn-00514d94) · [`00514da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md#insn-00514da4) · [`00514dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md#insn-00514dcc)

~~~diff
- 004f1efc ["INT_ADD", "register:40f0:8", ["const:4f1efc:8", "const:4:8"]]
- 004f1efc ["CALL", null, ["callee:00c59620:8"]]
+ 00514d94 ["INT_ADD", "register:40f0:8", ["const:514d94:8", "const:4:8"]]
+ 00514d94 ["CALL", null, ["callee:00c59620:8"]]
- 004f1efc bytes 35ab1b94
+ 00514d94 bytes 23121d94
- 004f1f0c ["INT_ADD", "register:40f0:8", ["const:4f1f0c:8", "const:4:8"]]
- 004f1f0c ["CALL", null, ["callee:00c582b0:8"]]
+ 00514da4 ["INT_ADD", "register:40f0:8", ["const:514da4:8", "const:4:8"]]
+ 00514da4 ["CALL", null, ["callee:00c582b0:8"]]
- 004f1f0c bytes 55a61b94
+ 00514da4 bytes 430d1d94
- 004f1f34 ["INT_ADD", "register:40f0:8", ["const:4f1f34:8", "const:4:8"]]
- 004f1f34 ["CALL", null, ["callee:00c582c0:8"]]
+ 00514dcc ["INT_ADD", "register:40f0:8", ["const:514dcc:8", "const:4:8"]]
+ 00514dcc ["CALL", null, ["callee:00c582c0:8"]]
- 004f1f34 bytes 4fa61b94
+ 00514dcc bytes 3d0d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36b53ee5127396a1a010631a9acc5142"></a>

### [`004f2228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2228.md) → [`005150c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/005150c0.md) FUN_005150c0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004f1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1ecc.md) · 呼出先 7件 [`0051a4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a4d4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) [`00bdb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md)
- 新版 呼出元 1件 [`00514d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md) · 呼出先 7件 [`0053d36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d36c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.28% / 新版 99.28%

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
      "site": "00515270",
      "value": [
        "leaf",
        "ram:c59560:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004f23d8",
      "value": [
        "leaf",
        "ram:bdcb10:8"
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
      "00515270",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcb10"
      ]
    ]
  ],
  "added": [
    [
      "00515270",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59560"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f23d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2228.md#insn-004f23d8) · [`004f2260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2228.md#insn-004f2260) · [`004f2340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2228.md#insn-004f2340)
- 新版 [`00515270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/005150c0.md#insn-00515270) · [`005150f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/005150c0.md#insn-005150f8) · [`005151d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/005150c0.md#insn-005151d8)

~~~diff
- 004f23d8 ["INT_ADD", "register:40f0:8", ["const:4f23d8:8", "const:4:8"]]
- 004f23d8 ["CALL", null, ["ram:bdcb10:8"]]
+ 00515270 ["INT_ADD", "register:40f0:8", ["const:515270:8", "const:4:8"]]
+ 00515270 ["CALL", null, ["ram:c59560:8"]]
- 004f23d8 bytes cea91b94
+ 00515270 bytes bc101d94
- 004f2260 ["INT_ADD", "register:40f0:8", ["const:4f2260:8", "const:4:8"]]
- 004f2260 ["CALL", null, ["callee:00c58280:8"]]
+ 005150f8 ["INT_ADD", "register:40f0:8", ["const:5150f8:8", "const:4:8"]]
+ 005150f8 ["CALL", null, ["callee:00c58280:8"]]
- 004f2260 bytes 74a51b94
+ 005150f8 bytes 620c1d94
- 004f2340 ["INT_ADD", "register:40f0:8", ["const:4f2340:8", "const:4:8"]]
- 004f2340 ["CALL", null, ["callee:0053d36c:8"]]
+ 005151d8 ["INT_ADD", "register:40f0:8", ["const:5151d8:8", "const:4:8"]]
+ 005151d8 ["CALL", null, ["callee:0053d36c:8"]]
- 004f2340 bytes 65a00094
+ 005151d8 bytes 65a00094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-322c2ce963182698b8a0563e3d48146b"></a>

### [`004f2498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2498.md) → [`00515330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515330.md) FUN_00515330

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004e5850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5850.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`005086e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/005086e8.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "site": "00515364",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004f24cc",
      "value": [
        "leaf",
        "ram:bdcf80:8"
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
      "00515364",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ]
  ],
  "added": [
    [
      "00515364",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f24cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2498.md#insn-004f24cc) · [`004f250c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2498.md#insn-004f250c) · [`004f2534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2498.md#insn-004f2534)
- 新版 [`00515364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515330.md#insn-00515364) · [`005153a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515330.md#insn-005153a4) · [`005153cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515330.md#insn-005153cc)

~~~diff
- 004f24cc ["INT_ADD", "register:40f0:8", ["const:4f24cc:8", "const:4:8"]]
- 004f24cc ["CALL", null, ["ram:bdcf80:8"]]
+ 00515364 ["INT_ADD", "register:40f0:8", ["const:515364:8", "const:4:8"]]
+ 00515364 ["CALL", null, ["ram:c599d0:8"]]
- 004f24cc bytes adaa1b94
+ 00515364 bytes 9b111d94
- 004f250c ["COPY", "register:0:8", ["register:4040:8"]]
- 004f250c ["INT_ADD", "register:40f0:8", ["const:4f250c:8", "const:4:8"]]
- 004f250c ["CALLIND", null, ["register:0:8"]]
+ 005153a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005153a4 ["INT_ADD", "register:40f0:8", ["const:5153a4:8", "const:4:8"]]
+ 005153a4 ["CALLIND", null, ["register:0:8"]]
- 004f250c bytes 00013fd6
+ 005153a4 bytes 00013fd6
- 004f2534 ["INT_ADD", "register:40f0:8", ["const:4f2534:8", "const:4:8"]]
- 004f2534 ["CALL", null, ["callee:00c57ea0:8"]]
+ 005153cc ["INT_ADD", "register:40f0:8", ["const:5153cc:8", "const:4:8"]]
+ 005153cc ["CALL", null, ["callee:00c57ea0:8"]]
- 004f2534 bytes c7a31b94
+ 005153cc bytes b50a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-403ac313664e8f1e722e2bc9d258e66c"></a>

### [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) → [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) _ZN5Botan10Extensions15create_extn_objERKNS_3OIDEbRKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdcf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf90.md) · 呼出先 27件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`004e0d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0d1c.md) [`004f3788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3788.md) [`004f3830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3830.md) [`004f38d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f38d8.md)
- 新版 呼出元 1件 [`00c599e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599e0.md) · 呼出先 27件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00503bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503bb4.md) [`00516620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516620.md) [`005166c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005166c8.md) [`00516770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516770.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005156e8",
      "incomplete_value": true,
      "site": "005156e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004f2850",
      "incomplete_value": true,
      "site": "004f2850",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:45e:8"
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
      "definition_site": "005157b8",
      "incomplete_value": true,
      "site": "005157b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:79d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2920",
      "incomplete_value": true,
      "site": "004f2920",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:418:8"
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
      "definition_site": "005158d8",
      "incomplete_value": true,
      "site": "005158d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2a40",
      "incomplete_value": true,
      "site": "004f2a40",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:564:8"
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
      "005156d8",
      "READ",
      [
        "storage",
        "002a445e",
        null,
        "string"
      ]
    ],
    [
      "00515780",
      "READ",
      [
        "storage",
        "00c1b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "0051578c",
      "DATA",
      [
        "storage",
        "00beaa68",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005156d8",
      "READ",
      [
        "storage",
        "002b4ccb",
        null,
        "string"
      ]
    ],
    [
      "00515780",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "0051578c",
      "DATA",
      [
        "storage",
        "00c67628",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f2830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md#insn-004f2830) · [`004f2834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md#insn-004f2834) · [`004f2838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md#insn-004f2838)
- 新版 [`005156c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md#insn-005156c8) · [`005156cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md#insn-005156cc) · [`005156d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md#insn-005156d0)

~~~diff
- 004f2830 ["INT_ADD", "register:40f0:8", ["const:4f2830:8", "const:4:8"]]
- 004f2830 ["CALL", null, ["callee:00c58400:8"]]
+ 005156c8 ["INT_ADD", "register:40f0:8", ["const:5156c8:8", "const:4:8"]]
+ 005156c8 ["CALL", null, ["callee:00c58400:8"]]
- 004f2830 bytes 60a41b94
+ 005156c8 bytes 4e0b1d94
- 004f2834 ["COPY", "register:4048:8", ["const:2a4000:8"]]
+ 005156cc ["COPY", "register:4048:8", ["const:2b4000:8"]]
- 004f2834 bytes 89edffd0
+ 005156cc bytes e9ecfff0
- 004f2838 ["COPY", "tmp:0:8", ["const:45e:8"]]
- 004f2838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f2838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f2838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005156d0 ["COPY", "tmp:0:8", ["const:ccb:8"]]
+ 005156d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005156d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005156d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f2838 bytes 29791191
+ 005156d0 bytes 292d3391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-851f6d00862a34c5fb6bee9d3d7709f4"></a>

### [`004f3788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3788.md) → [`00516620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516620.md) FUN_00516620

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "00516658",
      "incomplete_value": true,
      "site": "00516658",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:36:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f37c0",
      "incomplete_value": true,
      "site": "004f37c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:720:8"
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
      "00516648",
      "READ",
      [
        "storage",
        "00294720",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516648",
      "READ",
      [
        "storage",
        "002a4036",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f37a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3788.md#insn-004f37a0) · [`004f37a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3788.md#insn-004f37a4) · [`004f37cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3788.md#insn-004f37cc)
- 新版 [`00516638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516620.md#insn-00516638) · [`0051663c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516620.md#insn-0051663c) · [`00516664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516620.md#insn-00516664)

~~~diff
- 004f37a0 ["COPY", "register:4048:8", ["const:294000:8"]]
+ 00516638 ["COPY", "register:4048:8", ["const:2a4000:8"]]
- 004f37a0 bytes 09edffb0
+ 00516638 bytes 69ecffd0
- 004f37a4 ["COPY", "tmp:0:8", ["const:720:8"]]
- 004f37a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f37a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f37a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051663c ["COPY", "tmp:0:8", ["const:36:8"]]
+ 0051663c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051663c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051663c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f37a4 bytes 29811c91
+ 0051663c bytes 29d90091
- 004f37cc ["INT_ADD", "register:40f0:8", ["const:4f37cc:8", "const:4:8"]]
- 004f37cc ["CALL", null, ["callee:00c58290:8"]]
+ 00516664 ["INT_ADD", "register:40f0:8", ["const:516664:8", "const:4:8"]]
+ 00516664 ["CALL", null, ["callee:00c58290:8"]]
- 004f37cc bytes 1da01b94
+ 00516664 bytes 0b071d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab780ab46e51676e3e74b5090a7424cd"></a>

### [`004f3830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3830.md) → [`005166c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005166c8.md) FUN_005166c8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "00516700",
      "incomplete_value": true,
      "site": "00516700",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:ea0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3868",
      "incomplete_value": true,
      "site": "004f3868",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:28f000:8"
              ],
              [
                "leaf",
                "const:a60:8"
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
      "005166f0",
      "READ",
      [
        "storage",
        "0028fa60",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005166f0",
      "READ",
      [
        "storage",
        "0029eea0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f3848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3830.md#insn-004f3848) · [`004f384c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3830.md#insn-004f384c) · [`004f3874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3830.md#insn-004f3874)
- 新版 [`005166e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005166c8.md#insn-005166e0) · [`005166e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005166c8.md#insn-005166e4) · [`0051670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005166c8.md#insn-0051670c)

~~~diff
- 004f3848 ["COPY", "register:4048:8", ["const:28f000:8"]]
+ 005166e0 ["COPY", "register:4048:8", ["const:29e000:8"]]
- 004f3848 bytes e9ecff90
+ 005166e0 bytes 49ecff90
- 004f384c ["COPY", "tmp:0:8", ["const:a60:8"]]
- 004f384c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f384c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f384c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005166e4 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 005166e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005166e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005166e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f384c bytes 29812991
+ 005166e4 bytes 29813a91
- 004f3874 ["INT_ADD", "register:40f0:8", ["const:4f3874:8", "const:4:8"]]
- 004f3874 ["CALL", null, ["callee:00c58290:8"]]
+ 0051670c ["INT_ADD", "register:40f0:8", ["const:51670c:8", "const:4:8"]]
+ 0051670c ["CALL", null, ["callee:00c58290:8"]]
- 004f3874 bytes f39f1b94
+ 0051670c bytes e1061d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d8eab0d4d9a4ea810e1d89c81c0b20c"></a>

### [`004f38d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f38d8.md) → [`00516770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516770.md) FUN_00516770

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "005167a8",
      "incomplete_value": true,
      "site": "005167a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ad:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3910",
      "incomplete_value": true,
      "site": "004f3910",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:a54:8"
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
      "00516798",
      "READ",
      [
        "storage",
        "00297a54",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516798",
      "READ",
      [
        "storage",
        "002a76ad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f38f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f38d8.md#insn-004f38f0) · [`004f38f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f38d8.md#insn-004f38f4) · [`004f391c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f38d8.md#insn-004f391c)
- 新版 [`00516788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516770.md#insn-00516788) · [`0051678c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516770.md#insn-0051678c) · [`005167b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516770.md#insn-005167b4)

~~~diff
- 004f38f0 ["COPY", "register:4048:8", ["const:297000:8"]]
+ 00516788 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 004f38f0 bytes 29edff90
+ 00516788 bytes 89ecffb0
- 004f38f4 ["COPY", "tmp:0:8", ["const:a54:8"]]
- 004f38f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f38f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f38f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051678c ["COPY", "tmp:0:8", ["const:6ad:8"]]
+ 0051678c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051678c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051678c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f38f4 bytes 29512991
+ 0051678c bytes 29b51a91
- 004f391c ["INT_ADD", "register:40f0:8", ["const:4f391c:8", "const:4:8"]]
- 004f391c ["CALL", null, ["callee:00c58290:8"]]
+ 005167b4 ["INT_ADD", "register:40f0:8", ["const:5167b4:8", "const:4:8"]]
+ 005167b4 ["CALL", null, ["callee:00c58290:8"]]
- 004f391c bytes c99f1b94
+ 005167b4 bytes b7061d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa06c8a5754bff21250522d723b27bbe"></a>

### [`004f3980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3980.md) → [`00516818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516818.md) FUN_00516818

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f27ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f27ec.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md)
- 新版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)

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
      "definition_site": "00516850",
      "incomplete_value": true,
      "site": "00516850",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:49d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f39b8",
      "incomplete_value": true,
      "site": "004f39b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:57a:8"
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
      "00516840",
      "READ",
      [
        "storage",
        "002ab57a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516840",
      "READ",
      [
        "storage",
        "002bc49d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f3998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3980.md#insn-004f3998) · [`004f399c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3980.md#insn-004f399c) · [`004f39c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f3/004f3980.md#insn-004f39c4)
- 新版 [`00516830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516818.md#insn-00516830) · [`00516834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516818.md#insn-00516834) · [`0051685c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516818.md#insn-0051685c)

~~~diff
- 004f3998 ["COPY", "register:4048:8", ["const:2ab000:8"]]
+ 00516830 ["COPY", "register:4048:8", ["const:2bc000:8"]]
- 004f3998 bytes c9edff90
+ 00516830 bytes 29edffd0
- 004f399c ["COPY", "tmp:0:8", ["const:57a:8"]]
- 004f399c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f399c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f399c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516834 ["COPY", "tmp:0:8", ["const:49d:8"]]
+ 00516834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f399c bytes 29e91591
+ 00516834 bytes 29751291
- 004f39c4 ["INT_ADD", "register:40f0:8", ["const:4f39c4:8", "const:4:8"]]
- 004f39c4 ["CALL", null, ["callee:00c58290:8"]]
+ 0051685c ["INT_ADD", "register:40f0:8", ["const:51685c:8", "const:4:8"]]
+ 0051685c ["CALL", null, ["callee:00c58290:8"]]
- 004f39c4 bytes 9f9f1b94
+ 0051685c bytes 8d061d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

