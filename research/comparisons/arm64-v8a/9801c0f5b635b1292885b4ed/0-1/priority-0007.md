# v15.7.4 → v16.0.0 · 最優先の変更候補 (7)

[一覧の目次](README.md)

<a id="compare-0d3a9067db443932e0993403eba37819"></a>

### [`00484570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484570.md) → [`004a7408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7408.md) _ZN5Botan3OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "0048459c",
      "incomplete_value": true,
      "site": "004845a4",
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
      "site": "004a7504",
      "value": [
        "leaf",
        "ram:c583e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048466c",
      "value": [
        "leaf",
        "ram:bdb990:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "0048468c",
      "incomplete_value": true,
      "site": "00484694",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa0:8"
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
      "004a742c",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004a743c",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004a7504",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb990"
      ]
    ]
  ],
  "added": [
    [
      "004a742c",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "004a743c",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004a7504",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c583e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048466c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484570.md#insn-0048466c) · [`00484694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484570.md#insn-00484694) · [`004846a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484570.md#insn-004846a8)
- 新版 [`004a7504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7408.md#insn-004a7504) · [`004a752c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7408.md#insn-004a752c) · [`004a7540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7408.md#insn-004a7540)

~~~diff
- 0048466c ["INT_ADD", "register:40f0:8", ["const:48466c:8", "const:4:8"]]
- 0048466c ["CALL", null, ["ram:bdb990:8"]]
+ 004a7504 ["INT_ADD", "register:40f0:8", ["const:4a7504:8", "const:4:8"]]
+ 004a7504 ["CALL", null, ["ram:c583e0:8"]]
- 0048466c bytes c95c1d94
+ 004a7504 bytes b7c31e94
- 00484694 ["INT_ADD", "register:40f0:8", ["const:484694:8", "const:4:8"]]
- 00484694 ["CALL", null, ["callee:00c57b10:8"]]
+ 004a752c ["INT_ADD", "register:40f0:8", ["const:4a752c:8", "const:4:8"]]
+ 004a752c ["CALL", null, ["callee:00c57b10:8"]]
- 00484694 bytes 8b5a1d94
+ 004a752c bytes 79c11e94
- 004846a8 ["INT_ADD", "register:40f0:8", ["const:4846a8:8", "const:4:8"]]
- 004846a8 ["CALL", null, ["ram:bdb990:8"]]
+ 004a7540 ["INT_ADD", "register:40f0:8", ["const:4a7540:8", "const:4:8"]]
+ 004a7540 ["CALL", null, ["ram:c583e0:8"]]
- 004846a8 bytes ba5c1d94
+ 004a7540 bytes a8c31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e9f8bdcfd185e7f55228756ddfe9c00"></a>

### [`00484754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484754.md) → [`004a75ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md) _ZN5Botan14parse_asn1_oidERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb980.md) · 呼出先 12件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c583d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583d0.md) · 呼出先 12件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a78b8",
      "value": [
        "leaf",
        "ram:c583e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00484a20",
      "value": [
        "leaf",
        "ram:bdb990:8"
      ]
    },
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00484a44",
      "incomplete_value": true,
      "site": "00484a4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa0:8"
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
      "definition_site": "004a78d8",
      "incomplete_value": false,
      "site": "004a78e4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00484a40",
      "incomplete_value": false,
      "site": "00484a4c",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 12,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a78b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb990"
      ]
    ],
    [
      "004a78d8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004a78dc",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a78b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c583e0"
      ]
    ],
    [
      "004a78d8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004a78dc",
      "READ",
      [
        "storage",
        "00c9a990",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00484a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484754.md#insn-00484a20) · [`00484a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484754.md#insn-00484a4c) · [`00484a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484754.md#insn-00484a94)
- 新版 [`004a78b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md#insn-004a78b8) · [`004a78e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md#insn-004a78e4) · [`004a792c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a75ec.md#insn-004a792c)

~~~diff
- 00484a20 ["INT_ADD", "register:40f0:8", ["const:484a20:8", "const:4:8"]]
- 00484a20 ["CALL", null, ["ram:bdb990:8"]]
+ 004a78b8 ["INT_ADD", "register:40f0:8", ["const:4a78b8:8", "const:4:8"]]
+ 004a78b8 ["CALL", null, ["ram:c583e0:8"]]
- 00484a20 bytes dc5b1d94
+ 004a78b8 bytes cac21e94
- 00484a4c ["INT_ADD", "register:40f0:8", ["const:484a4c:8", "const:4:8"]]
- 00484a4c ["CALL", null, ["callee:00c57b10:8"]]
+ 004a78e4 ["INT_ADD", "register:40f0:8", ["const:4a78e4:8", "const:4:8"]]
+ 004a78e4 ["CALL", null, ["callee:00c57b10:8"]]
- 00484a4c bytes 9d591d94
+ 004a78e4 bytes 8bc01e94
- 00484a94 ["INT_ADD", "register:40f0:8", ["const:484a94:8", "const:4:8"]]
- 00484a94 ["CALL", null, ["ram:bdb990:8"]]
+ 004a792c ["INT_ADD", "register:40f0:8", ["const:4a792c:8", "const:4:8"]]
+ 004a792c ["CALL", null, ["ram:c583e0:8"]]
- 00484a94 bytes bf5b1d94
+ 004a792c bytes adc21e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be87a3475f29d1b5ad5d77b0d413810c"></a>

### [`00484e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484e1c.md) → [`004a7cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7cb4.md) _ZN5BotanplERKNS_3OIDEj

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

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
    "old": {
      "definition_site": "00484e4c",
      "incomplete_value": true,
      "site": "00484e58",
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
      "004a7cd4",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004a7cf0",
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
      "004a7cd4",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "004a7cf0",
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

- 旧版 [`00484e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484e1c.md#insn-00484e34) · [`00484e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484e1c.md#insn-00484e3c) · [`00484e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484e1c.md#insn-00484e68)
- 新版 [`004a7ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7cb4.md#insn-004a7ccc) · [`004a7cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7cb4.md#insn-004a7cd4) · [`004a7d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7cb4.md#insn-004a7d00)

~~~diff
- 00484e34 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004a7ccc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00484e34 bytes a83c00d0
+ 004a7ccc bytes 883f00f0
- 00484e3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
- 00484e3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a7cd4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
+ 004a7cd4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00484e3c bytes 08a947f9
+ 004a7cd4 bytes 08a144f9
- 00484e68 ["INT_ADD", "register:40f0:8", ["const:484e68:8", "const:4:8"]]
- 00484e68 ["CALL", null, ["callee:00c57a90:8"]]
+ 004a7d00 ["INT_ADD", "register:40f0:8", ["const:4a7d00:8", "const:4:8"]]
+ 004a7d00 ["CALL", null, ["callee:00c57a90:8"]]
- 00484e68 bytes 76581d94
+ 004a7d00 bytes 64bf1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-789735822c30e9e621a9fbf581cd8ca8"></a>

### [`00484f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484f50.md) → [`004a7de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7de8.md) _ZNK5Botan3OID11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
    "old": {
      "definition_site": "004852ac",
      "incomplete_value": false,
      "site": "004852cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:4b2:8"
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
    "old": {
      "definition_site": "004852b4",
      "incomplete_value": false,
      "site": "004852cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:6f3:8"
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
    "old": {
      "definition_site": "004852bc",
      "incomplete_value": false,
      "site": "004852cc",
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
            "const:3b0:8"
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
      "004a8144",
      "PARAM",
      [
        "storage",
        "002aa4b2",
        null,
        "string"
      ]
    ],
    [
      "004a814c",
      "PARAM",
      [
        "storage",
        "002926f3",
        null,
        "string"
      ]
    ],
    [
      "004a8154",
      "PARAM",
      [
        "storage",
        "002a93b0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a8144",
      "PARAM",
      [
        "storage",
        "002bb22e",
        null,
        "string"
      ]
    ],
    [
      "004a814c",
      "PARAM",
      [
        "storage",
        "002a1e03",
        null,
        "string"
      ]
    ],
    [
      "004a8154",
      "PARAM",
      [
        "storage",
        "002ba053",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004852cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484f50.md#insn-004852cc) · [`0048533c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484f50.md#insn-0048533c) · [`0048537c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484f50.md#insn-0048537c)
- 新版 [`004a8164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7de8.md#insn-004a8164) · [`004a81d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7de8.md#insn-004a81d4) · [`004a8214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a7/004a7de8.md#insn-004a8214)

~~~diff
- 004852cc ["INT_ADD", "register:40f0:8", ["const:4852cc:8", "const:4:8"]]
- 004852cc ["CALL", null, ["callee:00c58250:8"]]
+ 004a8164 ["INT_ADD", "register:40f0:8", ["const:4a8164:8", "const:4:8"]]
+ 004a8164 ["CALL", null, ["callee:00c58250:8"]]
- 004852cc bytes 4d591d94
+ 004a8164 bytes 3bc01e94
- 0048533c ["INT_ADD", "register:40f0:8", ["const:48533c:8", "const:4:8"]]
- 0048533c ["CALL", null, ["callee:0043dd98:8"]]
+ 004a81d4 ["INT_ADD", "register:40f0:8", ["const:4a81d4:8", "const:4:8"]]
+ 004a81d4 ["CALL", null, ["callee:0043dd98:8"]]
- 0048533c bytes d757fe97
+ 004a81d4 bytes f156fe97
- 0048537c ["INT_ADD", "register:40f0:8", ["const:48537c:8", "const:4:8"]]
- 0048537c ["CALL", null, ["callee:00c57b10:8"]]
+ 004a8214 ["INT_ADD", "register:40f0:8", ["const:4a8214:8", "const:4:8"]]
+ 004a8214 ["CALL", null, ["callee:00c57b10:8"]]
- 0048537c bytes 51571d94
+ 004a8214 bytes 3fbe1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1499d6809b868241ac022ba4592083cb"></a>

### [`004854c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/004854c8.md) → [`004a8360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8360.md) _ZN5Botan3OID11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.36% / 新版 97.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "004857b8",
      "incomplete_value": true,
      "site": "004857b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00485804",
      "incomplete_value": false,
      "site": "0048580c",
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
            "const:94b:8"
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
    "old": {
      "definition_site": "00485840",
      "incomplete_value": true,
      "site": "0048584c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a8640",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004a869c",
      "PARAM",
      [
        "storage",
        "0028f94b",
        null,
        "string"
      ]
    ],
    [
      "004a86d4",
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
      "004a8640",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004a869c",
      "PARAM",
      [
        "storage",
        "0029ed8b",
        null,
        "string"
      ]
    ],
    [
      "004a86d4",
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

- 旧版 [`004857b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/004854c8.md#insn-004857b8) · [`0048580c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/004854c8.md#insn-0048580c) · [`0048584c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/004854c8.md#insn-0048584c)
- 新版 [`004a8650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8360.md#insn-004a8650) · [`004a86a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8360.md#insn-004a86a4) · [`004a86e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8360.md#insn-004a86e4)

~~~diff
- 004857b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004857b8 ["INT_ADD", "register:40f0:8", ["const:4857b8:8", "const:4:8"]]
- 004857b8 ["CALLIND", null, ["register:0:8"]]
+ 004a8650 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a8650 ["INT_ADD", "register:40f0:8", ["const:4a8650:8", "const:4:8"]]
+ 004a8650 ["CALLIND", null, ["register:0:8"]]
- 004857b8 bytes 20013fd6
+ 004a8650 bytes 20013fd6
- 0048580c ["INT_ADD", "register:40f0:8", ["const:48580c:8", "const:4:8"]]
- 0048580c ["CALL", null, ["callee:0043dd98:8"]]
+ 004a86a4 ["INT_ADD", "register:40f0:8", ["const:4a86a4:8", "const:4:8"]]
+ 004a86a4 ["CALL", null, ["callee:0043dd98:8"]]
- 0048580c bytes a356fe97
+ 004a86a4 bytes bd55fe97
- 0048584c ["INT_ADD", "register:40f0:8", ["const:48584c:8", "const:4:8"]]
- 0048584c ["CALL", null, ["callee:00c57b10:8"]]
+ 004a86e4 ["INT_ADD", "register:40f0:8", ["const:4a86e4:8", "const:4:8"]]
+ 004a86e4 ["CALL", null, ["callee:00c57b10:8"]]
- 0048584c bytes 1d561d94
+ 004a86e4 bytes 0bbd1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cf316e1546b3d73380e122966179697"></a>

### [`00485a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485a10.md) → [`004a88a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md) _ZN5Botan11BER_Decoder15get_next_objectEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8d0.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048cb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cb40.md) [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md)
- 新版 呼出元 1件 [`00c58320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58320.md) · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004af9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md) [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00485b60",
      "incomplete_value": false,
      "site": "00485b68",
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
            "const:384:8"
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
      "site": "004a8a10",
      "value": [
        "leaf",
        "ram:c58450:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00485b78",
      "value": [
        "leaf",
        "ram:bdba00:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00485b98",
      "incomplete_value": true,
      "site": "00485ba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
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
      "004a89f8",
      "PARAM",
      [
        "storage",
        "002a1384",
        null,
        "string"
      ]
    ],
    [
      "004a8a10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba00"
      ]
    ],
    [
      "004a8a2c",
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
      "004a89f8",
      "PARAM",
      [
        "storage",
        "002b19d0",
        null,
        "string"
      ]
    ],
    [
      "004a8a10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58450"
      ]
    ],
    [
      "004a8a2c",
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

- 旧版 [`00485b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485a10.md#insn-00485b68) · [`00485b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485a10.md#insn-00485b78) · [`00485ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485a10.md#insn-00485ba4)
- 新版 [`004a8a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md#insn-004a8a00) · [`004a8a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md#insn-004a8a10) · [`004a8a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md#insn-004a8a3c)

~~~diff
- 00485b68 ["INT_ADD", "register:40f0:8", ["const:485b68:8", "const:4:8"]]
- 00485b68 ["CALL", null, ["callee:0043dd98:8"]]
+ 004a8a00 ["INT_ADD", "register:40f0:8", ["const:4a8a00:8", "const:4:8"]]
+ 004a8a00 ["CALL", null, ["callee:0043dd98:8"]]
- 00485b68 bytes cc55fe97
+ 004a8a00 bytes e654fe97
- 00485b78 ["INT_ADD", "register:40f0:8", ["const:485b78:8", "const:4:8"]]
- 00485b78 ["CALL", null, ["ram:bdba00:8"]]
+ 004a8a10 ["INT_ADD", "register:40f0:8", ["const:4a8a10:8", "const:4:8"]]
+ 004a8a10 ["CALL", null, ["ram:c58450:8"]]
- 00485b78 bytes a2571d94
+ 004a8a10 bytes 90be1e94
- 00485ba4 ["INT_ADD", "register:40f0:8", ["const:485ba4:8", "const:4:8"]]
- 00485ba4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004a8a3c ["INT_ADD", "register:40f0:8", ["const:4a8a3c:8", "const:4:8"]]
+ 004a8a3c ["CALL", null, ["callee:00c57b10:8"]]
- 00485ba4 bytes 47551d94
+ 004a8a3c bytes 35bc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d24acd168c0de6e2966990fc5589c430"></a>

### [`00485cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485cc4.md) → [`004a8b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8b5c.md) _ZNK5Botan14ASN1_Formatter5printEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)

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
    "old": {
      "definition_site": "00485d0c",
      "incomplete_value": true,
      "site": "00485d1c",
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
    "old": {
      "definition_site": "00485d14",
      "incomplete_value": true,
      "site": "00485d24",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "00485d2c",
      "incomplete_value": true,
      "site": "00485d2c",
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
      "004a8b90",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "004a8b94",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8bac",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004a8b90",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "004a8b94",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8bac",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00485ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485cc4.md#insn-00485ce8) · [`00485cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485cc4.md#insn-00485cec) · [`00485cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485cc4.md#insn-00485cf8)
- 新版 [`004a8b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8b5c.md#insn-004a8b80) · [`004a8b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8b5c.md#insn-004a8b84) · [`004a8b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8b5c.md#insn-004a8b90)

~~~diff
- 00485ce8 ["COPY", "register:40d8:8", ["const:c1a000:8"]]
+ 004a8b80 ["COPY", "register:40d8:8", ["const:c9a000:8"]]
- 00485ce8 bytes bb3c00b0
+ 004a8b80 bytes 9b3f00d0
- 00485cec ["COPY", "register:40d0:8", ["const:c1a000:8"]]
+ 004a8b84 ["COPY", "register:40d0:8", ["const:c9a000:8"]]
- 00485cec bytes ba3c00b0
+ 004a8b84 bytes 9a3f00d0
- 00485cf8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e98:8"]]
- 00485cf8 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a8b90 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:888:8"]]
+ 004a8b90 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00485cf8 bytes 7b4f47f9
+ 004a8b90 bytes 7b4744f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74e0dad293b1db0c65d952d8c6bc3745"></a>

### [`00485e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485e70.md) → [`004a8d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8d08.md) _ZNK5Botan14ASN1_Formatter15print_to_streamERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdba10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba10.md) · 呼出先 5件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8f0.md) [`00bdba20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba20.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00c58460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58460.md) · 呼出先 5件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58340.md) [`00c58470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58470.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a8d3c",
      "value": [
        "leaf",
        "ram:c58340:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00485ea4",
      "value": [
        "leaf",
        "ram:bdb8f0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a8d90",
      "incomplete_value": true,
      "site": "004a8d90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00485ef8",
      "incomplete_value": true,
      "site": "00485ef8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004a8d3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb8f0"
      ]
    ],
    [
      "004a8d80",
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
      "004a8d3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58340"
      ]
    ],
    [
      "004a8d80",
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

- 旧版 [`00485ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485e70.md#insn-00485ea4) · [`00485ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485e70.md#insn-00485ef8) · [`00485eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485e70.md#insn-00485eb8)
- 新版 [`004a8d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8d08.md#insn-004a8d3c) · [`004a8d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8d08.md#insn-004a8d90) · [`004a8d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8d08.md#insn-004a8d50)

~~~diff
- 00485ea4 ["INT_ADD", "register:40f0:8", ["const:485ea4:8", "const:4:8"]]
- 00485ea4 ["CALL", null, ["ram:bdb8f0:8"]]
+ 004a8d3c ["INT_ADD", "register:40f0:8", ["const:4a8d3c:8", "const:4:8"]]
+ 004a8d3c ["CALL", null, ["ram:c58340:8"]]
- 00485ea4 bytes 93561d94
+ 004a8d3c bytes 81bd1e94
- 00485ef8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00485ef8 ["INT_ADD", "register:40f0:8", ["const:485ef8:8", "const:4:8"]]
- 00485ef8 ["CALLIND", null, ["register:0:8"]]
+ 004a8d90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a8d90 ["INT_ADD", "register:40f0:8", ["const:4a8d90:8", "const:4:8"]]
+ 004a8d90 ["CALLIND", null, ["register:0:8"]]
- 00485ef8 bytes 20013fd6
+ 004a8d90 bytes 20013fd6
- 00485eb8 ["INT_ADD", "register:40f0:8", ["const:485eb8:8", "const:4:8"]]
- 00485eb8 ["CALL", null, ["callee:00c58470:8"]]
+ 004a8d50 ["INT_ADD", "register:40f0:8", ["const:4a8d50:8", "const:4:8"]]
+ 004a8d50 ["CALL", null, ["callee:00c58470:8"]]
- 00485eb8 bytes da561d94
+ 004a8d50 bytes c8bd1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-833128b24828388a07364f5e5c4d4871"></a>

### [`00485f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485f54.md) → [`004a8dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md) _ZNK5Botan14ASN1_Formatter6decodeERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEERNS_11BER_DecoderEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdba20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba20.md) · 呼出先 36件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c58470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58470.md) · 呼出先 36件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.41% / 新版 93.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 12件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00486034",
      "incomplete_value": true,
      "site": "00486048",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "00486058",
      "incomplete_value": true,
      "site": "00486058",
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
    "old": {
      "definition_site": "00486058",
      "incomplete_value": true,
      "site": "00486058",
      "value": [
        "LOAD",
        "8",
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
      "004a8e58",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004a8eb4",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8ecc",
      "READ",
      [
        "storage",
        "00c13458",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004a8e58",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004a8eb4",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8ecc",
      "READ",
      [
        "storage",
        "00c92e00",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00485fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485f54.md#insn-00485fd0) · [`004860f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485f54.md#insn-004860f0) · [`00486154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485f54.md#insn-00486154)
- 新版 [`004a8e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md#insn-004a8e68) · [`004a8f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md#insn-004a8f88) · [`004a8fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a8dec.md#insn-004a8fec)

~~~diff
- 00485fd0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00485fd0 ["INT_ADD", "register:40f0:8", ["const:485fd0:8", "const:4:8"]]
- 00485fd0 ["CALLIND", null, ["register:0:8"]]
+ 004a8e68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a8e68 ["INT_ADD", "register:40f0:8", ["const:4a8e68:8", "const:4:8"]]
+ 004a8e68 ["CALLIND", null, ["register:0:8"]]
- 00485fd0 bytes 20013fd6
+ 004a8e68 bytes 20013fd6
- 004860f0 ["INT_ADD", "register:40f0:8", ["const:4860f0:8", "const:4:8"]]
- 004860f0 ["CALL", null, ["ram:bdba30:8"]]
+ 004a8f88 ["INT_ADD", "register:40f0:8", ["const:4a8f88:8", "const:4:8"]]
+ 004a8f88 ["CALL", null, ["ram:c58480:8"]]
- 004860f0 bytes 50561d94
+ 004a8f88 bytes 3ebd1e94
- 00486154 ["INT_ADD", "register:40f0:8", ["const:486154:8", "const:4:8"]]
- 00486154 ["CALL", null, ["ram:bdba40:8"]]
+ 004a8fec ["INT_ADD", "register:40f0:8", ["const:4a8fec:8", "const:4:8"]]
+ 004a8fec ["CALL", null, ["ram:c58490:8"]]
- 00486154 bytes 3b561d94
+ 004a8fec bytes 29bd1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2628ebabf01ffb9a0805499b081145a"></a>

### [`004873a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00487/004873a4.md) → [`004aa23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004aa/004aa23c.md) _ZN5Botan4OIDS6lookupERKNS_3OIDE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdba60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba60.md) · 呼出先 5件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9b0.md)
- 新版 呼出元 1件 [`00c584b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584b0.md) · 呼出先 5件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58400.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 30.47% / 新版 30.47%

CFGの説明率　旧版 24.71% / 新版 24.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 49件, `store_value` 1件, `unresolved_branch_alignment` 131件, `unresolved_call_alignment` 131件

アドレスに依存する影響 `call_argument_candidate` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "0048760c",
      "incomplete_value": true,
      "site": "0048760c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8a8:8"
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
      "site": "004875a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "004875c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:004874e4",
      "PARAM",
      [
        "storage",
        "002968b2",
        null,
        null
      ]
    ],
    [
      "unmatched:00487594",
      "PARAM",
      [
        "storage",
        "0029c478",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0048759c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00441e54"
      ]
    ]
  ],
  "added": [
    [
      "004aa37c",
      "PARAM",
      [
        "storage",
        "002a63e7",
        null,
        null
      ]
    ],
    [
      "004aa42c",
      "PARAM",
      [
        "storage",
        "002ac611",
        null,
        "string"
      ]
    ],
    [
      "004aa438",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004aa448"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004875a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00487/004873a4.md#insn-004875a0) · [`004875c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00487/004873a4.md#insn-004875c0) · [`004875e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00487/004873a4.md#insn-004875e0)

~~~diff
- 004875a0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 004875a0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 004875a0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 004875a0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 004875a0 bytes 80000036
- 004875c0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 004875c0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 004875c0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 004875c0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 004875c0 bytes 80000036
- 004875e0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 004875e0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 004875e0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 004875e0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 004875e0 bytes c0020036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6ad13e3c55e692d5e084e4bfba2ce50"></a>

### [`00488e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00488/00488e94.md) → [`004abd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abd2c.md) _ZN5Botan11BER_Decoder6decodeERNS_6BigIntENS_8ASN1_TagES3_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdba70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba70.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8d0.md) [`00bdb8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8e0.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md)
- 新版 呼出元 1件 [`00c584c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584c0.md) · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58320.md) [`00c58330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58330.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "00488fc4",
      "incomplete_value": true,
      "site": "00488fc4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004abe88",
      "value": [
        "leaf",
        "ram:c58530:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00488ff0",
      "value": [
        "leaf",
        "ram:bdbae0:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048904c",
      "incomplete_value": true,
      "site": "0048904c",
      "value": [
        "LOAD",
        "8",
        [
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
      "004abe4c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004abe88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbae0"
      ]
    ],
    [
      "004abed4",
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
      "004abe4c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004abe88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58530"
      ]
    ],
    [
      "004abed4",
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

- 旧版 [`00488fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00488/00488e94.md#insn-00488fc4) · [`00488ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00488/00488e94.md#insn-00488ff0) · [`0048904c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00488/00488e94.md#insn-0048904c)
- 新版 [`004abe5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abd2c.md#insn-004abe5c) · [`004abe88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abd2c.md#insn-004abe88) · [`004abee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ab/004abd2c.md#insn-004abee4)

~~~diff
- 00488fc4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00488fc4 ["INT_ADD", "register:40f0:8", ["const:488fc4:8", "const:4:8"]]
- 00488fc4 ["CALLIND", null, ["register:0:8"]]
+ 004abe5c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004abe5c ["INT_ADD", "register:40f0:8", ["const:4abe5c:8", "const:4:8"]]
+ 004abe5c ["CALLIND", null, ["register:0:8"]]
- 00488fc4 bytes 20013fd6
+ 004abe5c bytes 20013fd6
- 00488ff0 ["INT_ADD", "register:40f0:8", ["const:488ff0:8", "const:4:8"]]
- 00488ff0 ["CALL", null, ["ram:bdbae0:8"]]
+ 004abe88 ["INT_ADD", "register:40f0:8", ["const:4abe88:8", "const:4:8"]]
+ 004abe88 ["CALL", null, ["ram:c58530:8"]]
- 00488ff0 bytes bc4a1d94
+ 004abe88 bytes aab11e94
- 0048904c ["COPY", "register:0:8", ["register:4048:8"]]
- 0048904c ["INT_ADD", "register:40f0:8", ["const:48904c:8", "const:4:8"]]
- 0048904c ["CALLIND", null, ["register:0:8"]]
+ 004abee4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004abee4 ["INT_ADD", "register:40f0:8", ["const:4abee4:8", "const:4:8"]]
+ 004abee4 ["CALLIND", null, ["register:0:8"]]
- 0048904c bytes 20013fd6
+ 004abee4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff1c8711c23e9fe8fc1e77a2168e10e1"></a>

### [`0048930c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/0048930c.md) → [`004ac1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac1a4.md) _ZNK5Botan9X509_Time15readable_stringEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbac0.md) · 呼出先 17件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)
- 新版 呼出元 1件 [`00c58510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58510.md) · 呼出先 17件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "004894c8",
      "incomplete_value": true,
      "site": "004894d0",
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
    "old": {
      "definition_site": "004894d8",
      "incomplete_value": true,
      "site": "004894d8",
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
    "old": {
      "definition_site": "004894d8",
      "incomplete_value": true,
      "site": "004894d8",
      "value": [
        "LOAD",
        "8",
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
      "004ac214",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004ac214",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004ac230",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "004ac214",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "004ac214",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004ac230",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00489380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/0048930c.md#insn-00489380) · [`00489398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/0048930c.md#insn-00489398) · [`004893d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/0048930c.md#insn-004893d0)
- 新版 [`004ac218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac1a4.md#insn-004ac218) · [`004ac230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac1a4.md#insn-004ac230) · [`004ac268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac1a4.md#insn-004ac268)

~~~diff
- 00489380 ["INT_ADD", "register:40f0:8", ["const:489380:8", "const:4:8"]]
- 00489380 ["CALL", null, ["callee:00c57e80:8"]]
+ 004ac218 ["INT_ADD", "register:40f0:8", ["const:4ac218:8", "const:4:8"]]
+ 004ac218 ["CALL", null, ["callee:00c57e80:8"]]
- 00489380 bytes 2c481d94
+ 004ac218 bytes 1aaf1e94
- 00489398 ["INT_ADD", "register:40f0:8", ["const:489398:8", "const:4:8"]]
- 00489398 ["CALL", null, ["ram:bdb440:8"]]
+ 004ac230 ["INT_ADD", "register:40f0:8", ["const:4ac230:8", "const:4:8"]]
+ 004ac230 ["CALL", null, ["ram:c57e90:8"]]
- 00489398 bytes 2a481d94
+ 004ac230 bytes 18af1e94
- 004893d0 ["INT_ADD", "register:40f0:8", ["const:4893d0:8", "const:4:8"]]
- 004893d0 ["CALL", null, ["callee:00459490:8"]]
+ 004ac268 ["INT_ADD", "register:40f0:8", ["const:4ac268:8", "const:4:8"]]
+ 004ac268 ["CALL", null, ["callee:00459490:8"]]
- 004893d0 bytes 8ab4fe97
+ 004ac268 bytes 8ab4fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12d878dde391175b4025a6a1d0ec2364"></a>

### [`00489628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489628.md) → [`004ac4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac4c0.md) _ZNK5Botan19ASN1_Pretty_Printer6formatENS_8ASN1_TagES1_mmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "004896dc",
      "incomplete_value": true,
      "site": "004896e0",
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
    "old": {
      "definition_site": "004896d8",
      "incomplete_value": true,
      "site": "004896e4",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "004896ec",
      "incomplete_value": true,
      "site": "004896ec",
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
      "004ac55c",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "004ac560",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "004ac570",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004ac55c",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "004ac560",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "004ac570",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00489760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489628.md#insn-00489760) · [`00489790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489628.md#insn-00489790) · [`004897bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489628.md#insn-004897bc)
- 新版 [`004ac5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac4c0.md#insn-004ac5f8) · [`004ac628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac4c0.md#insn-004ac628) · [`004ac654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac4c0.md#insn-004ac654)

~~~diff
- 00489760 ["INT_ADD", "register:40f0:8", ["const:489760:8", "const:4:8"]]
- 00489760 ["CALL", null, ["callee:00459490:8"]]
+ 004ac5f8 ["INT_ADD", "register:40f0:8", ["const:4ac5f8:8", "const:4:8"]]
+ 004ac5f8 ["CALL", null, ["callee:00459490:8"]]
- 00489760 bytes a6b3fe97
+ 004ac5f8 bytes a6b3fe97
- 00489790 ["INT_ADD", "register:40f0:8", ["const:489790:8", "const:4:8"]]
- 00489790 ["CALL", null, ["callee:00459490:8"]]
+ 004ac628 ["INT_ADD", "register:40f0:8", ["const:4ac628:8", "const:4:8"]]
+ 004ac628 ["CALL", null, ["callee:00459490:8"]]
- 00489790 bytes 9ab3fe97
+ 004ac628 bytes 9ab3fe97
- 004897bc ["INT_ADD", "register:40f0:8", ["const:4897bc:8", "const:4:8"]]
- 004897bc ["CALL", null, ["callee:00459490:8"]]
+ 004ac654 ["INT_ADD", "register:40f0:8", ["const:4ac654:8", "const:4:8"]]
+ 004ac654 ["CALL", null, ["callee:00459490:8"]]
- 004897bc bytes 8fb3fe97
+ 004ac654 bytes 8fb3fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1cc6b687f7b98de937b5126a4fc8a14"></a>

### [`00489f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489f78.md) → [`004ace10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ace10.md) _ZN5Botan11ASN1_StringC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb10.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0048a0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a0a0.md)
- 新版 呼出元 1件 [`00c59560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59560.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004acf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acf38.md)

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
    "old": {
      "definition_site": "00489fa4",
      "incomplete_value": true,
      "site": "00489fa8",
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
      "004ace2c",
      "READ",
      [
        "storage",
        "00c1afc8",
        null,
        "pointer"
      ]
    ],
    [
      "004ace40",
      "DATA",
      [
        "storage",
        "00be9388",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004aceb4",
      "DATA",
      [
        "storage",
        "002bdde8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ace2c",
      "READ",
      [
        "storage",
        "00c9a9b8",
        null,
        "pointer"
      ]
    ],
    [
      "004ace40",
      "DATA",
      [
        "storage",
        "00c65f48",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004aceb4",
      "DATA",
      [
        "storage",
        "002cf528",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00489f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489f78.md#insn-00489f88) · [`00489f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489f78.md#insn-00489f94) · [`00489fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489f78.md#insn-00489fd4)
- 新版 [`004ace20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ace10.md#insn-004ace20) · [`004ace2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ace10.md#insn-004ace2c) · [`004ace6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ace10.md#insn-004ace6c)

~~~diff
- 00489f88 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004ace20 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00489f88 bytes 883c00b0
+ 004ace20 bytes 683f00d0
- 00489f94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc8:8"]]
- 00489f94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ace2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
+ 004ace2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00489f94 bytes 08e547f9
+ 004ace2c bytes 08dd44f9
- 00489fd4 ["INT_ADD", "register:40f0:8", ["const:489fd4:8", "const:4:8"]]
- 00489fd4 ["CALL", null, ["callee:0043bae0:8"]]
+ 004ace6c ["INT_ADD", "register:40f0:8", ["const:4ace6c:8", "const:4:8"]]
+ 004ace6c ["CALL", null, ["callee:0043bae0:8"]]
- 00489fd4 bytes 033cfe97
+ 004ace6c bytes 1d3bfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c191b404e7504a3551c8bb629cd6056"></a>

### [`0048a0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a0a0.md) → [`004acf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acf38.md) FUN_004acf38

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00489f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489f78.md) [`0048a89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a89c.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 2件 [`004ace10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ace10.md) [`004ad734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad734.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

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
    "old": {
      "definition_site": "0048a128",
      "incomplete_value": false,
      "site": "0048a134",
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
            "const:60a:8"
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
    "old": {
      "definition_site": "0048a180",
      "incomplete_value": true,
      "site": "0048a18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ad014",
      "incomplete_value": false,
      "site": "004ad024",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048a17c",
      "incomplete_value": false,
      "site": "0048a18c",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004acfc0",
      "PARAM",
      [
        "storage",
        "0029e60a",
        null,
        "string"
      ]
    ],
    [
      "004ad014",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004ad018",
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
      "004acfc0",
      "PARAM",
      [
        "storage",
        "002ae98f",
        null,
        "string"
      ]
    ],
    [
      "004ad014",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ad018",
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

- 旧版 [`0048a134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a0a0.md#insn-0048a134) · [`0048a18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a0a0.md#insn-0048a18c) · [`0048a110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a0a0.md#insn-0048a110)
- 新版 [`004acfcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acf38.md#insn-004acfcc) · [`004ad024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acf38.md#insn-004ad024) · [`004acfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004acf38.md#insn-004acfa8)

~~~diff
- 0048a134 ["INT_ADD", "register:40f0:8", ["const:48a134:8", "const:4:8"]]
- 0048a134 ["CALL", null, ["callee:00c57b60:8"]]
+ 004acfcc ["INT_ADD", "register:40f0:8", ["const:4acfcc:8", "const:4:8"]]
+ 004acfcc ["CALL", null, ["callee:00c57b60:8"]]
- 0048a134 bytes f7431d94
+ 004acfcc bytes e5aa1e94
- 0048a18c ["INT_ADD", "register:40f0:8", ["const:48a18c:8", "const:4:8"]]
- 0048a18c ["CALL", null, ["callee:00c57b10:8"]]
+ 004ad024 ["INT_ADD", "register:40f0:8", ["const:4ad024:8", "const:4:8"]]
+ 004ad024 ["CALL", null, ["callee:00c57b10:8"]]
- 0048a18c bytes cd431d94
+ 004ad024 bytes bbaa1e94
- 0048a110 ["INT_ADD", "register:40f0:8", ["const:48a110:8", "const:4:8"]]
- 0048a110 ["CALL", null, ["callee:00c57af0:8"]]
+ 004acfa8 ["INT_ADD", "register:40f0:8", ["const:4acfa8:8", "const:4:8"]]
+ 004acfa8 ["CALL", null, ["callee:00c57af0:8"]]
- 0048a110 bytes e4431d94
+ 004acfa8 bytes d2aa1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9279cbbd2b756d11bc14a90cb10a4d00"></a>

### [`0048a208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a208.md) → [`004ad0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad0a0.md) _ZN5Botan11ASN1_StringC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbaa0.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00c584f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584f0.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

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
    "old": {
      "definition_site": "0048a22c",
      "incomplete_value": true,
      "site": "0048a230",
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
      "004ad0b8",
      "READ",
      [
        "storage",
        "00c1afc8",
        null,
        "pointer"
      ]
    ],
    [
      "004ad0c8",
      "DATA",
      [
        "storage",
        "00be9388",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ad12c",
      "DATA",
      [
        "storage",
        "002bdde8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ad0b8",
      "READ",
      [
        "storage",
        "00c9a9b8",
        null,
        "pointer"
      ]
    ],
    [
      "004ad0c8",
      "DATA",
      [
        "storage",
        "00c65f48",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ad12c",
      "DATA",
      [
        "storage",
        "002cf528",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048a214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a208.md#insn-0048a214) · [`0048a220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a208.md#insn-0048a220) · [`0048a25c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a208.md#insn-0048a25c)
- 新版 [`004ad0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad0a0.md#insn-004ad0ac) · [`004ad0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad0a0.md#insn-004ad0b8) · [`004ad0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad0a0.md#insn-004ad0f4)

~~~diff
- 0048a214 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004ad0ac ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0048a214 bytes 883c0090
+ 004ad0ac bytes 683f00b0
- 0048a220 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc8:8"]]
- 0048a220 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ad0b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
+ 004ad0b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048a220 bytes 08e547f9
+ 004ad0b8 bytes 08dd44f9
- 0048a25c ["INT_ADD", "register:40f0:8", ["const:48a25c:8", "const:4:8"]]
- 0048a25c ["CALL", null, ["callee:0043bae0:8"]]
+ 004ad0f4 ["INT_ADD", "register:40f0:8", ["const:4ad0f4:8", "const:4:8"]]
+ 004ad0f4 ["CALL", null, ["callee:0043bae0:8"]]
- 0048a25c bytes 613bfe97
+ 004ad0f4 bytes 7b3afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51fe1ce8eb6b84d91220b4cce63a528e"></a>

### [`0048a2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a2e8.md) → [`004ad180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad180.md) _ZN5Botan14utf8_to_latin1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb20.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58570.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
    "old": {
      "definition_site": "0048a3fc",
      "incomplete_value": false,
      "site": "0048a404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:82b:8"
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
    "old": {
      "definition_site": "0048a434",
      "incomplete_value": true,
      "site": "0048a440",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ad2c8",
      "incomplete_value": false,
      "site": "004ad2d8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048a430",
      "incomplete_value": false,
      "site": "0048a440",
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
      "004ad294",
      "PARAM",
      [
        "storage",
        "0029282b",
        null,
        "string"
      ]
    ],
    [
      "004ad2c8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004ad2cc",
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
      "004ad294",
      "PARAM",
      [
        "storage",
        "002a1f3b",
        null,
        "string"
      ]
    ],
    [
      "004ad2c8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ad2cc",
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

- 旧版 [`0048a404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a2e8.md#insn-0048a404) · [`0048a440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a2e8.md#insn-0048a440) · [`0048a460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a2e8.md#insn-0048a460)
- 新版 [`004ad29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad180.md#insn-004ad29c) · [`004ad2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad180.md#insn-004ad2d8) · [`004ad2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad180.md#insn-004ad2f8)

~~~diff
- 0048a404 ["INT_ADD", "register:40f0:8", ["const:48a404:8", "const:4:8"]]
- 0048a404 ["CALL", null, ["callee:0043dd98:8"]]
+ 004ad29c ["INT_ADD", "register:40f0:8", ["const:4ad29c:8", "const:4:8"]]
+ 004ad29c ["CALL", null, ["callee:0043dd98:8"]]
- 0048a404 bytes a543fe97
+ 004ad29c bytes bf42fe97
- 0048a440 ["INT_ADD", "register:40f0:8", ["const:48a440:8", "const:4:8"]]
- 0048a440 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ad2d8 ["INT_ADD", "register:40f0:8", ["const:4ad2d8:8", "const:4:8"]]
+ 004ad2d8 ["CALL", null, ["callee:00c57b10:8"]]
- 0048a440 bytes 20431d94
+ 004ad2d8 bytes 0eaa1e94
- 0048a460 ["INT_ADD", "register:40f0:8", ["const:48a460:8", "const:4:8"]]
- 0048a460 ["CALL", null, ["callee:0043dd98:8"]]
+ 004ad2f8 ["INT_ADD", "register:40f0:8", ["const:4ad2f8:8", "const:4:8"]]
+ 004ad2f8 ["CALL", null, ["callee:0043dd98:8"]]
- 0048a460 bytes 8e43fe97
+ 004ad2f8 bytes a842fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6af6100230ad4d2a93ced60cf6bc757"></a>

### [`0048a5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a5d8.md) → [`004ad470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md) _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md) · 呼出先 8件 [`0048f37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f37c.md) [`0048f6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f6e8.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c58420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58420.md) · 呼出先 8件 [`004b2214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md) [`004b2580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2580.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

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
    "old": {
      "definition_site": "0048a698",
      "incomplete_value": true,
      "site": "0048a698",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "old": {
      "definition_site": "0048a720",
      "incomplete_value": true,
      "site": "0048a720",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "old": {
      "definition_site": "0048a80c",
      "incomplete_value": true,
      "site": "0048a80c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "004ad520",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004ad5a8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004ad694",
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
      "004ad520",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ad5a8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ad694",
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

- 旧版 [`0048a698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a5d8.md#insn-0048a698) · [`0048a720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a5d8.md#insn-0048a720) · [`0048a80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a5d8.md#insn-0048a80c)
- 新版 [`004ad530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md#insn-004ad530) · [`004ad5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md#insn-004ad5b8) · [`004ad6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md#insn-004ad6a4)

~~~diff
- 0048a698 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048a698 ["INT_ADD", "register:40f0:8", ["const:48a698:8", "const:4:8"]]
- 0048a698 ["CALLIND", null, ["register:0:8"]]
+ 004ad530 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ad530 ["INT_ADD", "register:40f0:8", ["const:4ad530:8", "const:4:8"]]
+ 004ad530 ["CALLIND", null, ["register:0:8"]]
- 0048a698 bytes 20013fd6
+ 004ad530 bytes 20013fd6
- 0048a720 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048a720 ["INT_ADD", "register:40f0:8", ["const:48a720:8", "const:4:8"]]
- 0048a720 ["CALLIND", null, ["register:0:8"]]
+ 004ad5b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ad5b8 ["INT_ADD", "register:40f0:8", ["const:4ad5b8:8", "const:4:8"]]
+ 004ad5b8 ["CALLIND", null, ["register:0:8"]]
- 0048a720 bytes 20013fd6
+ 004ad5b8 bytes 20013fd6
- 0048a80c ["COPY", "register:0:8", ["register:4048:8"]]
- 0048a80c ["INT_ADD", "register:40f0:8", ["const:48a80c:8", "const:4:8"]]
- 0048a80c ["CALLIND", null, ["register:0:8"]]
+ 004ad6a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ad6a4 ["INT_ADD", "register:40f0:8", ["const:4ad6a4:8", "const:4:8"]]
+ 004ad6a4 ["CALLIND", null, ["register:0:8"]]
- 0048a80c bytes 20013fd6
+ 004ad6a4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-242885161b774f4516df8a839694c8c9"></a>

### [`0048aad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048aad4.md) → [`004ad96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad96c.md) _ZN5Botan12ucs2_to_utf8EPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb30.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004d6338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6338.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58580.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004f91d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f91d0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

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
    "old": {
      "definition_site": "0048ab60",
      "incomplete_value": false,
      "site": "0048ab68",
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
            "const:5df:8"
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
    "old": {
      "definition_site": "0048ab98",
      "incomplete_value": true,
      "site": "0048aba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ada2c",
      "incomplete_value": false,
      "site": "004ada3c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048ab94",
      "incomplete_value": false,
      "site": "0048aba4",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004ad9f8",
      "PARAM",
      [
        "storage",
        "002a95df",
        null,
        "string"
      ]
    ],
    [
      "004ada2c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004ada30",
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
      "004ad9f8",
      "PARAM",
      [
        "storage",
        "002ba282",
        null,
        "string"
      ]
    ],
    [
      "004ada2c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ada30",
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

- 旧版 [`0048ab68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048aad4.md#insn-0048ab68) · [`0048aba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048aad4.md#insn-0048aba4) · [`0048ab20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048aad4.md#insn-0048ab20)
- 新版 [`004ada00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad96c.md#insn-004ada00) · [`004ada3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad96c.md#insn-004ada3c) · [`004ad9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad96c.md#insn-004ad9b8)

~~~diff
- 0048ab68 ["INT_ADD", "register:40f0:8", ["const:48ab68:8", "const:4:8"]]
- 0048ab68 ["CALL", null, ["callee:0043dd98:8"]]
+ 004ada00 ["INT_ADD", "register:40f0:8", ["const:4ada00:8", "const:4:8"]]
+ 004ada00 ["CALL", null, ["callee:0043dd98:8"]]
- 0048ab68 bytes cc41fe97
+ 004ada00 bytes e640fe97
- 0048aba4 ["INT_ADD", "register:40f0:8", ["const:48aba4:8", "const:4:8"]]
- 0048aba4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ada3c ["INT_ADD", "register:40f0:8", ["const:4ada3c:8", "const:4:8"]]
+ 004ada3c ["CALL", null, ["callee:00c57b10:8"]]
- 0048aba4 bytes 47411d94
+ 004ada3c bytes 35a81e94
- 0048ab20 ["INT_ADD", "register:40f0:8", ["const:48ab20:8", "const:4:8"]]
- 0048ab20 ["CALL", null, ["callee:004f91d0:8"]]
+ 004ad9b8 ["INT_ADD", "register:40f0:8", ["const:4ad9b8:8", "const:4:8"]]
+ 004ad9b8 ["CALL", null, ["callee:004f91d0:8"]]
- 0048ab20 bytes 062e0194
+ 004ad9b8 bytes 062e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b9ab7734ee811912a0a140f2aa9d6c5"></a>

### [`0048ac0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ac0c.md) → [`004adaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adaa4.md) _ZN5Botan12ucs4_to_utf8EPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb40.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004d6338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6338.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58590.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004f91d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f91d0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

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
    "old": {
      "definition_site": "0048ac98",
      "incomplete_value": false,
      "site": "0048aca0",
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
            "const:7cf:8"
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
    "old": {
      "definition_site": "0048acd0",
      "incomplete_value": true,
      "site": "0048acdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004adb64",
      "incomplete_value": false,
      "site": "004adb74",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048accc",
      "incomplete_value": false,
      "site": "0048acdc",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004adb30",
      "PARAM",
      [
        "storage",
        "002947cf",
        null,
        "string"
      ]
    ],
    [
      "004adb64",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004adb68",
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
      "004adb30",
      "PARAM",
      [
        "storage",
        "002a40e5",
        null,
        "string"
      ]
    ],
    [
      "004adb64",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004adb68",
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

- 旧版 [`0048aca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ac0c.md#insn-0048aca0) · [`0048acdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ac0c.md#insn-0048acdc) · [`0048ac58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ac0c.md#insn-0048ac58)
- 新版 [`004adb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adaa4.md#insn-004adb38) · [`004adb74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adaa4.md#insn-004adb74) · [`004adaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adaa4.md#insn-004adaf0)

~~~diff
- 0048aca0 ["INT_ADD", "register:40f0:8", ["const:48aca0:8", "const:4:8"]]
- 0048aca0 ["CALL", null, ["callee:0043dd98:8"]]
+ 004adb38 ["INT_ADD", "register:40f0:8", ["const:4adb38:8", "const:4:8"]]
+ 004adb38 ["CALL", null, ["callee:0043dd98:8"]]
- 0048aca0 bytes 7e41fe97
+ 004adb38 bytes 9840fe97
- 0048acdc ["INT_ADD", "register:40f0:8", ["const:48acdc:8", "const:4:8"]]
- 0048acdc ["CALL", null, ["callee:00c57b10:8"]]
+ 004adb74 ["INT_ADD", "register:40f0:8", ["const:4adb74:8", "const:4:8"]]
+ 004adb74 ["CALL", null, ["callee:00c57b10:8"]]
- 0048acdc bytes f9401d94
+ 004adb74 bytes e7a71e94
- 0048ac58 ["INT_ADD", "register:40f0:8", ["const:48ac58:8", "const:4:8"]]
- 0048ac58 ["CALL", null, ["callee:004f91d0:8"]]
+ 004adaf0 ["INT_ADD", "register:40f0:8", ["const:4adaf0:8", "const:4:8"]]
+ 004adaf0 ["CALL", null, ["callee:004f91d0:8"]]
- 0048ac58 bytes b82d0194
+ 004adaf0 bytes b82d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b667c15da08afec3b9fc2f11a95a6ffe"></a>

### [`0048ad44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ad44.md) → [`004adbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adbdc.md) _ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc20.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb50.md) [`00bdbb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb60.md)
- 新版 呼出元 1件 [`00c59670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59670.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c585a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585a0.md) [`00c585b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585b0.md)

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
    "old": {
      "definition_site": "0048ad70",
      "incomplete_value": true,
      "site": "0048ad70",
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
      "004adbf8",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "004adc08",
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
      "004adbf8",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ],
    [
      "004adc08",
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

- 旧版 [`0048ad54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ad44.md#insn-0048ad54) · [`0048ad60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ad44.md#insn-0048ad60) · [`0048ad84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ad44.md#insn-0048ad84)
- 新版 [`004adbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adbdc.md#insn-004adbec) · [`004adbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adbdc.md#insn-004adbf8) · [`004adc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adbdc.md#insn-004adc1c)

~~~diff
- 0048ad54 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004adbec ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0048ad54 bytes 883c0090
+ 004adbec bytes 683f00b0
- 0048ad60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc0:8"]]
- 0048ad60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004adbf8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b0:8"]]
+ 004adbf8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048ad60 bytes 08e147f9
+ 004adbf8 bytes 08d944f9
- 0048ad84 ["INT_ADD", "register:40f0:8", ["const:48ad84:8", "const:4:8"]]
- 0048ad84 ["CALL", null, ["callee:00c585a0:8"]]
+ 004adc1c ["INT_ADD", "register:40f0:8", ["const:4adc1c:8", "const:4:8"]]
+ 004adc1c ["CALL", null, ["callee:00c585a0:8"]]
- 0048ad84 bytes 73431d94
+ 004adc1c bytes 61aa1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ba9bae07afffc5c36e9f322c98ec8c8"></a>

### [`0048ae8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ae8c.md) → [`004add24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004add24.md) _ZN5Botan9X509_Time6set_toERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb70.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c585c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585c0.md) · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "0048b40c",
      "incomplete_value": true,
      "site": "0048b410",
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
    "old": {
      "definition_site": "0048af3c",
      "incomplete_value": false,
      "site": "0048af48",
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
            "const:c8a:8"
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
    "old": {
      "definition_site": "0048af50",
      "incomplete_value": false,
      "site": "0048af58",
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
            "const:87b:8"
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
      "004addd4",
      "PARAM",
      [
        "storage",
        "00298c8a",
        null,
        "string"
      ]
    ],
    [
      "004adde8",
      "PARAM",
      [
        "storage",
        "0029687b",
        null,
        null
      ]
    ],
    [
      "004ade34",
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
      "004addd4",
      "PARAM",
      [
        "storage",
        "002a8a48",
        null,
        "string"
      ]
    ],
    [
      "004adde8",
      "PARAM",
      [
        "storage",
        "002a63b0",
        null,
        null
      ]
    ],
    [
      "004ade34",
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

- 旧版 [`0048af48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ae8c.md#insn-0048af48) · [`0048af58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ae8c.md#insn-0048af58) · [`0048afac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ae8c.md#insn-0048afac)
- 新版 [`004adde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004add24.md#insn-004adde0) · [`004addf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004add24.md#insn-004addf0) · [`004ade44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004add24.md#insn-004ade44)

~~~diff
- 0048af48 ["INT_ADD", "register:40f0:8", ["const:48af48:8", "const:4:8"]]
- 0048af48 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004adde0 ["INT_ADD", "register:40f0:8", ["const:4adde0:8", "const:4:8"]]
+ 004adde0 ["CALL", null, ["callee:00c57cb0:8"]]
- 0048af48 bytes c6401d94
+ 004adde0 bytes b4a71e94
- 0048af58 ["INT_ADD", "register:40f0:8", ["const:48af58:8", "const:4:8"]]
- 0048af58 ["CALL", null, ["callee:00c57b70:8"]]
+ 004addf0 ["INT_ADD", "register:40f0:8", ["const:4addf0:8", "const:4:8"]]
+ 004addf0 ["CALL", null, ["callee:00c57b70:8"]]
- 0048af58 bytes 72401d94
+ 004addf0 bytes 60a71e94
- 0048afac ["INT_ADD", "register:40f0:8", ["const:48afac:8", "const:4:8"]]
- 0048afac ["CALL", null, ["callee:00c57b10:8"]]
+ 004ade44 ["INT_ADD", "register:40f0:8", ["const:4ade44:8", "const:4:8"]]
+ 004ade44 ["CALL", null, ["callee:00c57b10:8"]]
- 0048afac bytes 45401d94
+ 004ade44 bytes 33a71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7841d2fe0200ae7d3b6af9386aa401b0"></a>

### [`0048b6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b6ac.md) → [`004ae544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae544.md) _ZNK5Botan9X509_Time11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

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
    "old": {
      "definition_site": "0048b758",
      "incomplete_value": false,
      "site": "0048b760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:768:8"
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
    "old": {
      "definition_site": "0048b790",
      "incomplete_value": true,
      "site": "0048b79c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ae624",
      "incomplete_value": false,
      "site": "004ae634",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048b78c",
      "incomplete_value": false,
      "site": "0048b79c",
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
      "004ae5f0",
      "PARAM",
      [
        "storage",
        "00293768",
        null,
        "string"
      ]
    ],
    [
      "004ae624",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004ae628",
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
      "004ae5f0",
      "PARAM",
      [
        "storage",
        "002a2f61",
        null,
        "string"
      ]
    ],
    [
      "004ae624",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ae628",
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

- 旧版 [`0048b760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b6ac.md#insn-0048b760) · [`0048b79c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b6ac.md#insn-0048b79c) · [`0048b6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b6ac.md#insn-0048b6e8)
- 新版 [`004ae5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae544.md#insn-004ae5f8) · [`004ae634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae544.md#insn-004ae634) · [`004ae580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae544.md#insn-004ae580)

~~~diff
- 0048b760 ["INT_ADD", "register:40f0:8", ["const:48b760:8", "const:4:8"]]
- 0048b760 ["CALL", null, ["callee:0043dd98:8"]]
+ 004ae5f8 ["INT_ADD", "register:40f0:8", ["const:4ae5f8:8", "const:4:8"]]
+ 004ae5f8 ["CALL", null, ["callee:0043dd98:8"]]
- 0048b760 bytes ce3efe97
+ 004ae5f8 bytes e83dfe97
- 0048b79c ["INT_ADD", "register:40f0:8", ["const:48b79c:8", "const:4:8"]]
- 0048b79c ["CALL", null, ["callee:00c57b10:8"]]
+ 004ae634 ["INT_ADD", "register:40f0:8", ["const:4ae634:8", "const:4:8"]]
+ 004ae634 ["CALL", null, ["callee:00c57b10:8"]]
- 0048b79c bytes 493e1d94
+ 004ae634 bytes 37a51e94
- 0048b6e8 ["INT_ADD", "register:40f0:8", ["const:48b6e8:8", "const:4:8"]]
- 0048b6e8 ["CALL", null, ["callee:00c585d0:8"]]
+ 004ae580 ["INT_ADD", "register:40f0:8", ["const:4ae580:8", "const:4:8"]]
+ 004ae580 ["CALL", null, ["callee:00c585d0:8"]]
- 0048b6e8 bytes 26411d94
+ 004ae580 bytes 14a81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dcf0741a077cc36d42320aa60959f51"></a>

### [`0048b804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b804.md) → [`004ae69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae69c.md) _ZNK5Botan9X509_Time9to_stringEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb80.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c585d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585d0.md) · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "0048b8c4",
      "incomplete_value": false,
      "site": "0048b8cc",
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
            "const:343:8"
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
    "old": {
      "definition_site": "0048b9b8",
      "incomplete_value": false,
      "site": "0048b9c0",
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
            "const:412:8"
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
    "old": {
      "definition_site": "0048b9f0",
      "incomplete_value": true,
      "site": "0048b9fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ae75c",
      "PARAM",
      [
        "storage",
        "002a1343",
        null,
        null
      ]
    ],
    [
      "004ae7fc",
      "PARAM",
      [
        "storage",
        "002a74cc",
        null,
        null
      ]
    ],
    [
      "004ae850",
      "PARAM",
      [
        "storage",
        "0029f412",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ae75c",
      "PARAM",
      [
        "storage",
        "002b198f",
        null,
        null
      ]
    ],
    [
      "004ae7fc",
      "PARAM",
      [
        "storage",
        "002b803b",
        null,
        null
      ]
    ],
    [
      "004ae850",
      "PARAM",
      [
        "storage",
        "002af825",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048b8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b804.md#insn-0048b8cc) · [`0048b9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b804.md#insn-0048b9c0) · [`0048b9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b804.md#insn-0048b9fc)
- 新版 [`004ae764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae69c.md#insn-004ae764) · [`004ae858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae69c.md#insn-004ae858) · [`004ae894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae69c.md#insn-004ae894)

~~~diff
- 0048b8cc ["INT_ADD", "register:40f0:8", ["const:48b8cc:8", "const:4:8"]]
- 0048b8cc ["CALL", null, ["callee:00c57b70:8"]]
+ 004ae764 ["INT_ADD", "register:40f0:8", ["const:4ae764:8", "const:4:8"]]
+ 004ae764 ["CALL", null, ["callee:00c57b70:8"]]
- 0048b8cc bytes 153e1d94
+ 004ae764 bytes 03a51e94
- 0048b9c0 ["INT_ADD", "register:40f0:8", ["const:48b9c0:8", "const:4:8"]]
- 0048b9c0 ["CALL", null, ["callee:0043dd98:8"]]
+ 004ae858 ["INT_ADD", "register:40f0:8", ["const:4ae858:8", "const:4:8"]]
+ 004ae858 ["CALL", null, ["callee:0043dd98:8"]]
- 0048b9c0 bytes 363efe97
+ 004ae858 bytes 503dfe97
- 0048b9fc ["INT_ADD", "register:40f0:8", ["const:48b9fc:8", "const:4:8"]]
- 0048b9fc ["CALL", null, ["callee:00c57b10:8"]]
+ 004ae894 ["INT_ADD", "register:40f0:8", ["const:4ae894:8", "const:4:8"]]
+ 004ae894 ["CALL", null, ["callee:00c57b10:8"]]
- 0048b9fc bytes b13d1d94
+ 004ae894 bytes 9fa41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b97594f07985ec08493195b3a30acb49"></a>

### [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) → [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) FUN_004aec24

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 29件 [`004826c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004826c4.md) [`00482c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482c08.md) [`0048930c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/0048930c.md) [`0048b804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b804.md) [`0048be04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048be04.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 29件 [`004a555c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a555c.md) [`004a5aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5aa0.md) [`004ac1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac1a4.md) [`004ae69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004ae69c.md) [`004aec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec9c.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

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
    "old": {
      "definition_site": "0048bda8",
      "incomplete_value": true,
      "site": "0048bda8",
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
    "old": {
      "definition_site": "0048bddc",
      "incomplete_value": true,
      "site": "0048bde0",
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
      "004aec38",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004aec40",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004aec70",
      "READ",
      [
        "storage",
        "00c1afe8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004aec38",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004aec40",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004aec70",
      "READ",
      [
        "storage",
        "00c9a9d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048bd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md#insn-0048bd98) · [`0048bda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md#insn-0048bda0) · [`0048bdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md#insn-0048bdd0)
- 新版 [`004aec30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md#insn-004aec30) · [`004aec38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md#insn-004aec38) · [`004aec68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md#insn-004aec68)

~~~diff
- 0048bd98 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004aec30 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0048bd98 bytes 683c00f0
+ 004aec30 bytes 683f0090
- 0048bda0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 0048bda0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aec38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 004aec38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048bda0 bytes 08f147f9
+ 004aec38 bytes 08e944f9
- 0048bdd0 ["INT_ADD", "register:40f0:8", ["const:48bdd0:8", "const:4:8"]]
- 0048bdd0 ["CALL", null, ["callee:0043bae0:8"]]
+ 004aec68 ["INT_ADD", "register:40f0:8", ["const:4aec68:8", "const:4:8"]]
+ 004aec68 ["CALL", null, ["callee:0043bae0:8"]]
- 0048bdd0 bytes 8434fe97
+ 004aec68 bytes 9e33fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61b3a4bfffa38b3baa34321772f65086"></a>

### [`0048be04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048be04.md) → [`004aec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec9c.md) _ZNK5Botan9X509_Time3cmpERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb90.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

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
    "old": {
      "definition_site": "0048bee8",
      "incomplete_value": false,
      "site": "0048bef0",
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
            "const:160:8"
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
    "old": {
      "definition_site": "0048bf24",
      "incomplete_value": true,
      "site": "0048bf30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004aedb8",
      "incomplete_value": false,
      "site": "004aedc8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048bf20",
      "incomplete_value": false,
      "site": "0048bf30",
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
      "004aed80",
      "PARAM",
      [
        "storage",
        "002a8160",
        null,
        "string"
      ]
    ],
    [
      "004aedb8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004aedbc",
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
      "004aed80",
      "PARAM",
      [
        "storage",
        "002b8e02",
        null,
        "string"
      ]
    ],
    [
      "004aedb8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004aedbc",
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

- 旧版 [`0048bef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048be04.md#insn-0048bef0) · [`0048bf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048be04.md#insn-0048bf30) · [`0048bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048be04.md#insn-0048bedc)
- 新版 [`004aed88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec9c.md#insn-004aed88) · [`004aedc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec9c.md#insn-004aedc8) · [`004aed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec9c.md#insn-004aed74)

~~~diff
- 0048bef0 ["INT_ADD", "register:40f0:8", ["const:48bef0:8", "const:4:8"]]
- 0048bef0 ["CALL", null, ["callee:0043dd98:8"]]
+ 004aed88 ["INT_ADD", "register:40f0:8", ["const:4aed88:8", "const:4:8"]]
+ 004aed88 ["CALL", null, ["callee:0043dd98:8"]]
- 0048bef0 bytes ea3cfe97
+ 004aed88 bytes 043cfe97
- 0048bf30 ["INT_ADD", "register:40f0:8", ["const:48bf30:8", "const:4:8"]]
- 0048bf30 ["CALL", null, ["callee:00c57b10:8"]]
+ 004aedc8 ["INT_ADD", "register:40f0:8", ["const:4aedc8:8", "const:4:8"]]
+ 004aedc8 ["CALL", null, ["callee:00c57b10:8"]]
- 0048bf30 bytes 643c1d94
+ 004aedc8 bytes 52a31e94
- 0048bedc ["INT_ADD", "register:40f0:8", ["const:48bedc:8", "const:4:8"]]
- 0048bedc ["CALL", null, ["callee:00c57af0:8"]]
+ 004aed74 ["INT_ADD", "register:40f0:8", ["const:4aed74:8", "const:4:8"]]
+ 004aed74 ["CALL", null, ["callee:00c57af0:8"]]
- 0048bedc bytes 713c1d94
+ 004aed74 bytes 5fa31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9019a5afa7843e2521d29649524bc10d"></a>

### [`0048bf84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bf84.md) → [`004aee1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aee1c.md) _ZN5Botan9to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9a0.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00c583f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583f0.md) · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

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
    "old": {
      "definition_site": "0048c044",
      "incomplete_value": false,
      "site": "0048c050",
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
            "const:626:8"
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
    "old": {
      "definition_site": "0048c084",
      "incomplete_value": true,
      "site": "0048c090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004aef18",
      "incomplete_value": false,
      "site": "004aef28",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048c080",
      "incomplete_value": false,
      "site": "0048c090",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004aeedc",
      "PARAM",
      [
        "storage",
        "002a9626",
        null,
        "string"
      ]
    ],
    [
      "004aef18",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004aef1c",
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
      "004aeedc",
      "PARAM",
      [
        "storage",
        "002ba2c9",
        null,
        "string"
      ]
    ],
    [
      "004aef18",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004aef1c",
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

- 旧版 [`0048c050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bf84.md#insn-0048c050) · [`0048c090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bf84.md#insn-0048c090) · [`0048c0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bf84.md#insn-0048c0b8)
- 新版 [`004aeee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aee1c.md#insn-004aeee8) · [`004aef28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aee1c.md#insn-004aef28) · [`004aef50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aee1c.md#insn-004aef50)

~~~diff
- 0048c050 ["INT_ADD", "register:40f0:8", ["const:48c050:8", "const:4:8"]]
- 0048c050 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004aeee8 ["INT_ADD", "register:40f0:8", ["const:4aeee8:8", "const:4:8"]]
+ 004aeee8 ["CALL", null, ["callee:00c57cb0:8"]]
- 0048c050 bytes 843c1d94
+ 004aeee8 bytes 72a31e94
- 0048c090 ["INT_ADD", "register:40f0:8", ["const:48c090:8", "const:4:8"]]
- 0048c090 ["CALL", null, ["callee:00c57b10:8"]]
+ 004aef28 ["INT_ADD", "register:40f0:8", ["const:4aef28:8", "const:4:8"]]
+ 004aef28 ["CALL", null, ["callee:00c57b10:8"]]
- 0048c090 bytes 0c3c1d94
+ 004aef28 bytes faa21e94
- 0048c0b8 ["INT_ADD", "register:40f0:8", ["const:48c0b8:8", "const:4:8"]]
- 0048c0b8 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004aef50 ["INT_ADD", "register:40f0:8", ["const:4aef50:8", "const:4:8"]]
+ 004aef50 ["CALL", null, ["callee:00c57cb0:8"]]
- 0048c0b8 bytes 6a3c1d94
+ 004aef50 bytes 58a31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fad13062e77fe86c03a47971f11a33be"></a>

### [`0048c2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c2e0.md) → [`004af178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af178.md) _ZNK5Botan14calendar_point16to_std_timepointEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbb0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58600.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
    "old": {
      "definition_site": "0048c408",
      "incomplete_value": false,
      "site": "0048c410",
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
            "const:5f2:8"
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
    "old": {
      "definition_site": "0048c444",
      "incomplete_value": true,
      "site": "0048c450",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004af2d8",
      "incomplete_value": false,
      "site": "004af2e8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048c440",
      "incomplete_value": false,
      "site": "0048c450",
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
      "004af2a0",
      "PARAM",
      [
        "storage",
        "002a05f2",
        null,
        "string"
      ]
    ],
    [
      "004af2d8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004af2dc",
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
      "004af2a0",
      "PARAM",
      [
        "storage",
        "002b0bac",
        null,
        "string"
      ]
    ],
    [
      "004af2d8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004af2dc",
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

- 旧版 [`0048c410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c2e0.md#insn-0048c410) · [`0048c450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c2e0.md#insn-0048c450) · [`0048c474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c2e0.md#insn-0048c474)
- 新版 [`004af2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af178.md#insn-004af2a8) · [`004af2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af178.md#insn-004af2e8) · [`004af30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af178.md#insn-004af30c)

~~~diff
- 0048c410 ["INT_ADD", "register:40f0:8", ["const:48c410:8", "const:4:8"]]
- 0048c410 ["CALL", null, ["callee:0043dd98:8"]]
+ 004af2a8 ["INT_ADD", "register:40f0:8", ["const:4af2a8:8", "const:4:8"]]
+ 004af2a8 ["CALL", null, ["callee:0043dd98:8"]]
- 0048c410 bytes a23bfe97
+ 004af2a8 bytes bc3afe97
- 0048c450 ["INT_ADD", "register:40f0:8", ["const:48c450:8", "const:4:8"]]
- 0048c450 ["CALL", null, ["callee:00c57b10:8"]]
+ 004af2e8 ["INT_ADD", "register:40f0:8", ["const:4af2e8:8", "const:4:8"]]
+ 004af2e8 ["CALL", null, ["callee:00c57b10:8"]]
- 0048c450 bytes 1c3b1d94
+ 004af2e8 bytes 0aa21e94
- 0048c474 ["INT_ADD", "register:40f0:8", ["const:48c474:8", "const:4:8"]]
- 0048c474 ["CALL", null, ["callee:0043dd98:8"]]
+ 004af30c ["INT_ADD", "register:40f0:8", ["const:4af30c:8", "const:4:8"]]
+ 004af30c ["CALL", null, ["callee:0043dd98:8"]]
- 0048c474 bytes 893bfe97
+ 004af30c bytes a33afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-126a6097fb0bb8de0c0e96cf160ea54d"></a>

### [`0048c5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c5ac.md) → [`004af444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af444.md) _ZNK5Botan10BER_Object11assert_is_aENS_8ASN1_TagES1_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8e0.md) · 呼出先 9件 [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58330.md) · 呼出先 9件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "0048c640",
      "incomplete_value": false,
      "site": "0048c64c",
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
            "const:364:8"
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
    "old": {
      "definition_site": "0048c66c",
      "incomplete_value": false,
      "site": "0048c674",
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
            "const:83d:8"
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
    "old": {
      "definition_site": "0048c6b0",
      "incomplete_value": false,
      "site": "0048c6b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:4bd:8"
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
      "004af4d8",
      "PARAM",
      [
        "storage",
        "002a1364",
        null,
        "string"
      ]
    ],
    [
      "004af504",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ],
    [
      "004af548",
      "PARAM",
      [
        "storage",
        "002aa4bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004af4d8",
      "PARAM",
      [
        "storage",
        "002b19b0",
        null,
        "string"
      ]
    ],
    [
      "004af504",
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ],
    [
      "004af548",
      "PARAM",
      [
        "storage",
        "002bb239",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048c64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c5ac.md#insn-0048c64c) · [`0048c674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c5ac.md#insn-0048c674) · [`0048c6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c5ac.md#insn-0048c6b8)
- 新版 [`004af4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af444.md#insn-004af4e4) · [`004af50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af444.md#insn-004af50c) · [`004af550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af444.md#insn-004af550)

~~~diff
- 0048c64c ["INT_ADD", "register:40f0:8", ["const:48c64c:8", "const:4:8"]]
- 0048c64c ["CALL", null, ["callee:00c57b60:8"]]
+ 004af4e4 ["INT_ADD", "register:40f0:8", ["const:4af4e4:8", "const:4:8"]]
+ 004af4e4 ["CALL", null, ["callee:00c57b60:8"]]
- 0048c64c bytes b13a1d94
+ 004af4e4 bytes 9fa11e94
- 0048c674 ["INT_ADD", "register:40f0:8", ["const:48c674:8", "const:4:8"]]
- 0048c674 ["CALL", null, ["callee:00c57b70:8"]]
+ 004af50c ["INT_ADD", "register:40f0:8", ["const:4af50c:8", "const:4:8"]]
+ 004af50c ["CALL", null, ["callee:00c57b70:8"]]
- 0048c674 bytes ab3a1d94
+ 004af50c bytes 99a11e94
- 0048c6b8 ["INT_ADD", "register:40f0:8", ["const:48c6b8:8", "const:4:8"]]
- 0048c6b8 ["CALL", null, ["callee:00c57b70:8"]]
+ 004af550 ["INT_ADD", "register:40f0:8", ["const:4af550:8", "const:4:8"]]
+ 004af550 ["CALL", null, ["callee:00c57b70:8"]]
- 0048c6b8 bytes 9a3a1d94
+ 004af550 bytes 88a11e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11bd24cc650b29466d9754a1987695ce"></a>

### [`0048c9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c9bc.md) → [`004af854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af854.md) _ZN5Botan11BER_Decoder10verify_endEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbd0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58620.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

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
    "old": {
      "definition_site": "0048ca40",
      "incomplete_value": false,
      "site": "0048ca48",
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
            "const:969:8"
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
    "old": {
      "definition_site": "0048ca7c",
      "incomplete_value": true,
      "site": "0048ca88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004af910",
      "incomplete_value": false,
      "site": "004af920",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048ca78",
      "incomplete_value": false,
      "site": "0048ca88",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004af8d8",
      "PARAM",
      [
        "storage",
        "0028f969",
        null,
        "string"
      ]
    ],
    [
      "004af910",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004af914",
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
      "004af8d8",
      "PARAM",
      [
        "storage",
        "0029eda9",
        null,
        "string"
      ]
    ],
    [
      "004af910",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004af914",
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

- 旧版 [`0048ca48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c9bc.md#insn-0048ca48) · [`0048ca88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c9bc.md#insn-0048ca88) · [`0048c9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c9bc.md#insn-0048c9ec)
- 新版 [`004af8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af854.md#insn-004af8e0) · [`004af920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af854.md#insn-004af920) · [`004af884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af854.md#insn-004af884)

~~~diff
- 0048ca48 ["INT_ADD", "register:40f0:8", ["const:48ca48:8", "const:4:8"]]
- 0048ca48 ["CALL", null, ["callee:0043dd98:8"]]
+ 004af8e0 ["INT_ADD", "register:40f0:8", ["const:4af8e0:8", "const:4:8"]]
+ 004af8e0 ["CALL", null, ["callee:0043dd98:8"]]
- 0048ca48 bytes 143afe97
+ 004af8e0 bytes 2e39fe97
- 0048ca88 ["INT_ADD", "register:40f0:8", ["const:48ca88:8", "const:4:8"]]
- 0048ca88 ["CALL", null, ["callee:00c57b10:8"]]
+ 004af920 ["INT_ADD", "register:40f0:8", ["const:4af920:8", "const:4:8"]]
+ 004af920 ["CALL", null, ["callee:00c57b10:8"]]
- 0048ca88 bytes 8e391d94
+ 004af920 bytes 7ca01e94
- 0048c9ec ["COPY", "register:0:8", ["register:4040:8"]]
- 0048c9ec ["INT_ADD", "register:40f0:8", ["const:48c9ec:8", "const:4:8"]]
- 0048c9ec ["CALLIND", null, ["register:0:8"]]
+ 004af884 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004af884 ["INT_ADD", "register:40f0:8", ["const:4af884:8", "const:4:8"]]
+ 004af884 ["CALLIND", null, ["register:0:8"]]
- 0048c9ec bytes 00013fd6
+ 004af884 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-979e6a100c2ab1cc02c57e21dcee3677"></a>

### [`0048cb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cb40.md) → [`004af9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md) FUN_004af9d8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00485a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485a10.md) [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 2件 [`004a88a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md) [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.39% / 新版 94.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "0048cc48",
      "incomplete_value": false,
      "site": "0048cc50",
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
            "const:b5d:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004afaf8",
      "value": [
        "leaf",
        "ram:c58450:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048cc60",
      "value": [
        "leaf",
        "ram:bdba00:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "0048cc80",
      "incomplete_value": true,
      "site": "0048cc8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb8:8"
              ]
            ]
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
      "004afae0",
      "PARAM",
      [
        "storage",
        "00291b5d",
        null,
        "string"
      ]
    ],
    [
      "004afaf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba00"
      ]
    ],
    [
      "004afb14",
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
      "004afae0",
      "PARAM",
      [
        "storage",
        "002a1176",
        null,
        "string"
      ]
    ],
    [
      "004afaf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58450"
      ]
    ],
    [
      "004afb14",
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

- 旧版 [`0048cc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cb40.md#insn-0048cc50) · [`0048cc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cb40.md#insn-0048cc60) · [`0048cc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cb40.md#insn-0048cc8c)
- 新版 [`004afae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md#insn-004afae8) · [`004afaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md#insn-004afaf8) · [`004afb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md#insn-004afb24)

~~~diff
- 0048cc50 ["INT_ADD", "register:40f0:8", ["const:48cc50:8", "const:4:8"]]
- 0048cc50 ["CALL", null, ["callee:0043dd98:8"]]
+ 004afae8 ["INT_ADD", "register:40f0:8", ["const:4afae8:8", "const:4:8"]]
+ 004afae8 ["CALL", null, ["callee:0043dd98:8"]]
- 0048cc50 bytes 9239fe97
+ 004afae8 bytes ac38fe97
- 0048cc60 ["INT_ADD", "register:40f0:8", ["const:48cc60:8", "const:4:8"]]
- 0048cc60 ["CALL", null, ["ram:bdba00:8"]]
+ 004afaf8 ["INT_ADD", "register:40f0:8", ["const:4afaf8:8", "const:4:8"]]
+ 004afaf8 ["CALL", null, ["ram:c58450:8"]]
- 0048cc60 bytes 683b1d94
+ 004afaf8 bytes 56a21e94
- 0048cc8c ["INT_ADD", "register:40f0:8", ["const:48cc8c:8", "const:4:8"]]
- 0048cc8c ["CALL", null, ["callee:00c57b10:8"]]
+ 004afb24 ["INT_ADD", "register:40f0:8", ["const:4afb24:8", "const:4:8"]]
+ 004afb24 ["CALL", null, ["callee:00c57b10:8"]]
- 0048cc8c bytes 0d391d94
+ 004afb24 bytes fb9f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac77bf4f63c65902f6a334ce21374eb8"></a>

### [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) → [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) FUN_004afbd0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00485a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485a10.md) [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) · 呼出先 18件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048cb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cb40.md) [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) [`004d6b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6b48.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)
- 新版 呼出元 2件 [`004a88a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a8/004a88a8.md) [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) · 呼出先 18件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004af9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004af9d8.md) [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) [`004f99e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f99e0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.39% / 新版 92.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `call_target` 9件

アドレスに依存する影響 `call_argument_candidate` 8件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "0048ced8",
      "incomplete_value": true,
      "site": "0048ced8",
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
    "old": {
      "definition_site": "0048cfc0",
      "incomplete_value": true,
      "site": "0048cfc0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048cfec",
      "incomplete_value": true,
      "site": "0048cfec",
      "value": [
        "LOAD",
        "8",
        [
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
      "004afd60",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "004afd70",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004afdf4",
      "READ",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004afd60",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004afd70",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004afdf4",
      "READ",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048cfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md#insn-0048cfc0) · [`0048cfec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md#insn-0048cfec) · [`0048d018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md#insn-0048d018)
- 新版 [`004afe58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md#insn-004afe58) · [`004afe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md#insn-004afe84) · [`004afeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md#insn-004afeb0)

~~~diff
- 0048cfc0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048cfc0 ["INT_ADD", "register:40f0:8", ["const:48cfc0:8", "const:4:8"]]
- 0048cfc0 ["CALLIND", null, ["register:0:8"]]
+ 004afe58 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004afe58 ["INT_ADD", "register:40f0:8", ["const:4afe58:8", "const:4:8"]]
+ 004afe58 ["CALLIND", null, ["register:0:8"]]
- 0048cfc0 bytes 20013fd6
+ 004afe58 bytes 20013fd6
- 0048cfec ["COPY", "register:0:8", ["register:4048:8"]]
- 0048cfec ["INT_ADD", "register:40f0:8", ["const:48cfec:8", "const:4:8"]]
- 0048cfec ["CALLIND", null, ["register:0:8"]]
+ 004afe84 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004afe84 ["INT_ADD", "register:40f0:8", ["const:4afe84:8", "const:4:8"]]
+ 004afe84 ["CALLIND", null, ["register:0:8"]]
- 0048cfec bytes 20013fd6
+ 004afe84 bytes 20013fd6
- 0048d018 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048d018 ["INT_ADD", "register:40f0:8", ["const:48d018:8", "const:4:8"]]
- 0048d018 ["CALLIND", null, ["register:0:8"]]
+ 004afeb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004afeb0 ["INT_ADD", "register:40f0:8", ["const:4afeb0:8", "const:4:8"]]
+ 004afeb0 ["CALLIND", null, ["register:0:8"]]
- 0048d018 bytes 20013fd6
+ 004afeb0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14d7238af64a9caaa7ea2dfd363377fe"></a>

### [`0048d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d518.md) → [`004b03b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b03b0.md) _ZN5Botan11BER_Decoder9push_backERKNS_10BER_ObjectE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc10.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00520980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520980.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c58660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58660.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00543818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543818.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "0048d5cc",
      "incomplete_value": false,
      "site": "0048d5d4",
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
            "const:ae5:8"
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
    "old": {
      "definition_site": "0048d608",
      "incomplete_value": true,
      "site": "0048d614",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b049c",
      "incomplete_value": false,
      "site": "004b04ac",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048d604",
      "incomplete_value": false,
      "site": "0048d614",
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
      "004b0464",
      "PARAM",
      [
        "storage",
        "00299ae5",
        null,
        "string"
      ]
    ],
    [
      "004b049c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004b04a0",
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
      "004b0464",
      "PARAM",
      [
        "storage",
        "002a99be",
        null,
        "string"
      ]
    ],
    [
      "004b049c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b04a0",
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

- 旧版 [`0048d5d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d518.md#insn-0048d5d4) · [`0048d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d518.md#insn-0048d614) · [`0048d5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d518.md#insn-0048d5c0)
- 新版 [`004b046c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b03b0.md#insn-004b046c) · [`004b04ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b03b0.md#insn-004b04ac) · [`004b0458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b03b0.md#insn-004b0458)

~~~diff
- 0048d5d4 ["INT_ADD", "register:40f0:8", ["const:48d5d4:8", "const:4:8"]]
- 0048d5d4 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b046c ["INT_ADD", "register:40f0:8", ["const:4b046c:8", "const:4:8"]]
+ 004b046c ["CALL", null, ["callee:0043dd98:8"]]
- 0048d5d4 bytes 3137fe97
+ 004b046c bytes 4b36fe97
- 0048d614 ["INT_ADD", "register:40f0:8", ["const:48d614:8", "const:4:8"]]
- 0048d614 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b04ac ["INT_ADD", "register:40f0:8", ["const:4b04ac:8", "const:4:8"]]
+ 004b04ac ["CALL", null, ["callee:00c57b10:8"]]
- 0048d614 bytes ab361d94
+ 004b04ac bytes 999d1e94
- 0048d5c0 ["INT_ADD", "register:40f0:8", ["const:48d5c0:8", "const:4:8"]]
- 0048d5c0 ["CALL", null, ["callee:00c57af0:8"]]
+ 004b0458 ["INT_ADD", "register:40f0:8", ["const:4b0458:8", "const:4:8"]]
+ 004b0458 ["CALL", null, ["callee:00c57af0:8"]]
- 0048d5c0 bytes b8361d94
+ 004b0458 bytes a69d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8436b3084dcb33a6bf0ac5063083433e"></a>

### [`0048d684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d684.md) → [`004b051c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b051c.md) _ZN5Botan11BER_DecoderC1EPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8f0.md) · 呼出先 2件 [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c58340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58340.md) · 呼出先 2件 [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "site": "0048d6c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0048d6c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "0048d6c4",
      "incomplete_value": true,
      "site": "0048d6c8",
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
      "004b0554",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "004b0560",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004b0554",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004b0560",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d684.md#insn-0048d6c0) · [`0048d6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d684.md#insn-0048d6b0)
- 新版 [`004b0558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b051c.md#insn-004b0558) · [`004b0548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b051c.md#insn-004b0548)

~~~diff
- 0048d6c0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0048d6c0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0048d6c0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0048d6c0 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0048d6c0 bytes 1f7c01a9
+ 004b0558 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 004b0558 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 004b0558 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 004b0558 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 004b0558 bytes 1f7c01a9
- 0048d6b0 ["INT_ADD", "register:40f0:8", ["const:48d6b0:8", "const:4:8"]]
- 0048d6b0 ["CALL", null, ["callee:00c57a90:8"]]
+ 004b0548 ["INT_ADD", "register:40f0:8", ["const:4b0548:8", "const:4:8"]]
+ 004b0548 ["CALL", null, ["callee:00c57a90:8"]]
- 0048d6b0 bytes 64361d94
+ 004b0548 bytes 529d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-894f7231cdcc595ae14980e50adf4a63"></a>

### [`0048d760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d760.md) → [`004b05f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b05f8.md) _ZN5Botan11BER_DecoderC2ERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdba40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba40.md) · 呼出先 2件 [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c58490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58490.md) · 呼出先 2件 [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "site": "0048d79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0048d79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "0048d7a0",
      "incomplete_value": true,
      "site": "0048d7a4",
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
      "004b062c",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "004b063c",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004b062c",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004b063c",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d79c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d760.md#insn-0048d79c) · [`0048d788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d760.md#insn-0048d788)
- 新版 [`004b0634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b05f8.md#insn-004b0634) · [`004b0620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b05f8.md#insn-004b0620)

~~~diff
- 0048d79c ["COPY", "tmp:0:8", ["const:0:8"]]
- 0048d79c ["COPY", "tmp:1:8", ["const:0:8"]]
- 0048d79c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0048d79c ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0048d79c bytes 1f7c01a9
+ 004b0634 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 004b0634 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 004b0634 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 004b0634 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 004b0634 bytes 1f7c01a9
- 0048d788 ["INT_ADD", "register:40f0:8", ["const:48d788:8", "const:4:8"]]
- 0048d788 ["CALL", null, ["callee:00c57a90:8"]]
+ 004b0620 ["INT_ADD", "register:40f0:8", ["const:4b0620:8", "const:4:8"]]
+ 004b0620 ["CALL", null, ["callee:00c57a90:8"]]
- 0048d788 bytes 2e361d94
+ 004b0620 bytes 1c9d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-784a87013a4bb9247fa7af6421141301"></a>

### [`0048d834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d834.md) → [`004b06cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b06cc.md) _ZN5Botan11BER_DecoderC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdba30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba30.md) · 呼出先 2件 [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c58480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58480.md) · 呼出先 2件 [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "site": "0048d870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0048d870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "0048d874",
      "incomplete_value": true,
      "site": "0048d878",
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
      "004b0700",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "004b0710",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004b0700",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004b0710",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d834.md#insn-0048d870) · [`0048d85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d834.md#insn-0048d85c)
- 新版 [`004b0708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b06cc.md#insn-004b0708) · [`004b06f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b06cc.md#insn-004b06f4)

~~~diff
- 0048d870 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0048d870 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0048d870 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0048d870 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0048d870 bytes 1f7c01a9
+ 004b0708 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 004b0708 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 004b0708 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 004b0708 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 004b0708 bytes 1f7c01a9
- 0048d85c ["INT_ADD", "register:40f0:8", ["const:48d85c:8", "const:4:8"]]
- 0048d85c ["CALL", null, ["callee:00c57a90:8"]]
+ 004b06f4 ["INT_ADD", "register:40f0:8", ["const:4b06f4:8", "const:4:8"]]
+ 004b06f4 ["CALL", null, ["callee:00c57a90:8"]]
- 0048d85c bytes f9351d94
+ 004b06f4 bytes e79c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75707f1ca9317d4d9a40403c80ca0131"></a>

### [`0048d940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d940.md) → [`004b07d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b07d8.md) _ZN5Botan11BER_Decoder11decode_nullEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048d9a4",
      "incomplete_value": true,
      "site": "0048d9a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "0048d9e8",
      "incomplete_value": false,
      "site": "0048d9f0",
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
            "const:705:8"
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
      "site": "004b0898",
      "value": [
        "leaf",
        "ram:c58450:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048da00",
      "value": [
        "leaf",
        "ram:bdba00:8"
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
      "004b082c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b0880",
      "PARAM",
      [
        "storage",
        "002ae705",
        null,
        "string"
      ]
    ],
    [
      "004b0898",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba00"
      ]
    ]
  ],
  "added": [
    [
      "004b082c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b0880",
      "PARAM",
      [
        "storage",
        "002bfbe9",
        null,
        "string"
      ]
    ],
    [
      "004b0898",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58450"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d9a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d940.md#insn-0048d9a4) · [`0048d9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d940.md#insn-0048d9f0) · [`0048da00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d940.md#insn-0048da00)
- 新版 [`004b083c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b07d8.md#insn-004b083c) · [`004b0888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b07d8.md#insn-004b0888) · [`004b0898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b07d8.md#insn-004b0898)

~~~diff
- 0048d9a4 ["COPY", "register:0:8", ["register:4050:8"]]
- 0048d9a4 ["INT_ADD", "register:40f0:8", ["const:48d9a4:8", "const:4:8"]]
- 0048d9a4 ["CALLIND", null, ["register:0:8"]]
+ 004b083c ["COPY", "register:0:8", ["register:4050:8"]]
+ 004b083c ["INT_ADD", "register:40f0:8", ["const:4b083c:8", "const:4:8"]]
+ 004b083c ["CALLIND", null, ["register:0:8"]]
- 0048d9a4 bytes 40013fd6
+ 004b083c bytes 40013fd6
- 0048d9f0 ["INT_ADD", "register:40f0:8", ["const:48d9f0:8", "const:4:8"]]
- 0048d9f0 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b0888 ["INT_ADD", "register:40f0:8", ["const:4b0888:8", "const:4:8"]]
+ 004b0888 ["CALL", null, ["callee:0043dd98:8"]]
- 0048d9f0 bytes 2a36fe97
+ 004b0888 bytes 4435fe97
- 0048da00 ["INT_ADD", "register:40f0:8", ["const:48da00:8", "const:4:8"]]
- 0048da00 ["CALL", null, ["ram:bdba00:8"]]
+ 004b0898 ["INT_ADD", "register:40f0:8", ["const:4b0898:8", "const:4:8"]]
+ 004b0898 ["CALL", null, ["ram:c58450:8"]]
- 0048da00 bytes 00381d94
+ 004b0898 bytes ee9e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58e236bd9405446ead6437bb5c264166"></a>

### [`0048da90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048da90.md) → [`004b0928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0928.md) _ZN5Botan11BER_Decoder6decodeERbNS_8ASN1_TagES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdba90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba90.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c584e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584e0.md) · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.96% / 新版 92.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048db18",
      "incomplete_value": true,
      "site": "0048db18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "0048db60",
      "incomplete_value": false,
      "site": "0048db68",
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
            "const:722:8"
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
      "site": "004b0a10",
      "value": [
        "leaf",
        "ram:c58450:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048db78",
      "value": [
        "leaf",
        "ram:bdba00:8"
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
      "004b09a0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b09f8",
      "PARAM",
      [
        "storage",
        "002ae722",
        null,
        "string"
      ]
    ],
    [
      "004b0a10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba00"
      ]
    ]
  ],
  "added": [
    [
      "004b09a0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b09f8",
      "PARAM",
      [
        "storage",
        "002bfc06",
        null,
        "string"
      ]
    ],
    [
      "004b0a10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58450"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048db18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048da90.md#insn-0048db18) · [`0048db68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048da90.md#insn-0048db68) · [`0048db78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048da90.md#insn-0048db78)
- 新版 [`004b09b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0928.md#insn-004b09b0) · [`004b0a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0928.md#insn-004b0a00) · [`004b0a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0928.md#insn-004b0a10)

~~~diff
- 0048db18 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048db18 ["INT_ADD", "register:40f0:8", ["const:48db18:8", "const:4:8"]]
- 0048db18 ["CALLIND", null, ["register:0:8"]]
+ 004b09b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b09b0 ["INT_ADD", "register:40f0:8", ["const:4b09b0:8", "const:4:8"]]
+ 004b09b0 ["CALLIND", null, ["register:0:8"]]
- 0048db18 bytes 20013fd6
+ 004b09b0 bytes 20013fd6
- 0048db68 ["INT_ADD", "register:40f0:8", ["const:48db68:8", "const:4:8"]]
- 0048db68 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b0a00 ["INT_ADD", "register:40f0:8", ["const:4b0a00:8", "const:4:8"]]
+ 004b0a00 ["CALL", null, ["callee:0043dd98:8"]]
- 0048db68 bytes cc35fe97
+ 004b0a00 bytes e634fe97
- 0048db78 ["INT_ADD", "register:40f0:8", ["const:48db78:8", "const:4:8"]]
- 0048db78 ["CALL", null, ["ram:bdba00:8"]]
+ 004b0a10 ["INT_ADD", "register:40f0:8", ["const:4b0a10:8", "const:4:8"]]
+ 004b0a10 ["CALL", null, ["ram:c58450:8"]]
- 0048db78 bytes a2371d94
+ 004b0a10 bytes 909e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cb4ff3938cec7f82073b0efd7fb6899"></a>

### [`0048dc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048dc14.md) → [`004b0aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0aac.md) _ZN5Botan11BER_Decoder6decodeERmNS_8ASN1_TagES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc20.md) · 呼出先 9件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58670.md) · 呼出先 9件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048dd04",
      "incomplete_value": true,
      "site": "0048dd04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "0048dd48",
      "incomplete_value": false,
      "site": "0048dd50",
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
            "const:87d:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b0bf8",
      "value": [
        "leaf",
        "ram:c58450:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048dd60",
      "value": [
        "leaf",
        "ram:bdba00:8"
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
      "004b0b8c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b0be0",
      "PARAM",
      [
        "storage",
        "0029687d",
        null,
        "string"
      ]
    ],
    [
      "004b0bf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba00"
      ]
    ]
  ],
  "added": [
    [
      "004b0b8c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b0be0",
      "PARAM",
      [
        "storage",
        "002a63b2",
        null,
        "string"
      ]
    ],
    [
      "004b0bf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58450"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048dd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048dc14.md#insn-0048dd04) · [`0048dd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048dc14.md#insn-0048dd50) · [`0048dd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048dc14.md#insn-0048dd60)
- 新版 [`004b0b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0aac.md#insn-004b0b9c) · [`004b0be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0aac.md#insn-004b0be8) · [`004b0bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0aac.md#insn-004b0bf8)

~~~diff
- 0048dd04 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048dd04 ["INT_ADD", "register:40f0:8", ["const:48dd04:8", "const:4:8"]]
- 0048dd04 ["CALLIND", null, ["register:0:8"]]
+ 004b0b9c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0b9c ["INT_ADD", "register:40f0:8", ["const:4b0b9c:8", "const:4:8"]]
+ 004b0b9c ["CALLIND", null, ["register:0:8"]]
- 0048dd04 bytes 20013fd6
+ 004b0b9c bytes 20013fd6
- 0048dd50 ["INT_ADD", "register:40f0:8", ["const:48dd50:8", "const:4:8"]]
- 0048dd50 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b0be8 ["INT_ADD", "register:40f0:8", ["const:4b0be8:8", "const:4:8"]]
+ 004b0be8 ["CALL", null, ["callee:0043dd98:8"]]
- 0048dd50 bytes 5235fe97
+ 004b0be8 bytes 6c34fe97
- 0048dd60 ["INT_ADD", "register:40f0:8", ["const:48dd60:8", "const:4:8"]]
- 0048dd60 ["CALL", null, ["ram:bdba00:8"]]
+ 004b0bf8 ["INT_ADD", "register:40f0:8", ["const:4b0bf8:8", "const:4:8"]]
+ 004b0bf8 ["CALL", null, ["ram:c58450:8"]]
- 0048dd60 bytes 28371d94
+ 004b0bf8 bytes 169e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb32ecf14167bc3068699708f38d43bd"></a>

### [`0048ddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048ddf0.md) → [`004b0c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0c88.md) _ZN5Botan11BER_Decoder26decode_octet_string_bigintERNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc30.md) [`00bdbc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc40.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58680.md) [`00c58690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58690.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
    "old": {
      "definition_site": "0048deb8",
      "incomplete_value": true,
      "site": "0048deb8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048dee4",
      "incomplete_value": true,
      "site": "0048dee4",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b0d40",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b0d6c",
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
      "004b0d40",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b0d6c",
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

- 旧版 [`0048deb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048ddf0.md#insn-0048deb8) · [`0048dee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048ddf0.md#insn-0048dee4) · [`0048de34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048ddf0.md#insn-0048de34)
- 新版 [`004b0d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0c88.md#insn-004b0d50) · [`004b0d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0c88.md#insn-004b0d7c) · [`004b0ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0c88.md#insn-004b0ccc)

~~~diff
- 0048deb8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048deb8 ["INT_ADD", "register:40f0:8", ["const:48deb8:8", "const:4:8"]]
- 0048deb8 ["CALLIND", null, ["register:0:8"]]
+ 004b0d50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0d50 ["INT_ADD", "register:40f0:8", ["const:4b0d50:8", "const:4:8"]]
+ 004b0d50 ["CALLIND", null, ["register:0:8"]]
- 0048deb8 bytes 20013fd6
+ 004b0d50 bytes 20013fd6
- 0048dee4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048dee4 ["INT_ADD", "register:40f0:8", ["const:48dee4:8", "const:4:8"]]
- 0048dee4 ["CALLIND", null, ["register:0:8"]]
+ 004b0d7c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0d7c ["INT_ADD", "register:40f0:8", ["const:4b0d7c:8", "const:4:8"]]
+ 004b0d7c ["CALLIND", null, ["register:0:8"]]
- 0048dee4 bytes 20013fd6
+ 004b0d7c bytes 20013fd6
- 0048de34 ["INT_ADD", "register:40f0:8", ["const:48de34:8", "const:4:8"]]
- 0048de34 ["CALL", null, ["callee:00c58680:8"]]
+ 004b0ccc ["INT_ADD", "register:40f0:8", ["const:4b0ccc:8", "const:4:8"]]
+ 004b0ccc ["CALL", null, ["callee:00c58680:8"]]
- 0048de34 bytes 7f371d94
+ 004b0ccc bytes 6d9e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-250433ba802435cb11fe56c3e423311d"></a>

### [`0048df5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048df5c.md) → [`004b0df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0df4.md) _ZN5Botan6BigInt6decodeEPKhmNS0_4BaseE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc50.md) · 呼出先 20件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md)
- 新版 呼出元 1件 [`00c586a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586a0.md) · 呼出先 20件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048e054",
      "incomplete_value": true,
      "site": "0048e054",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "0048e098",
      "incomplete_value": true,
      "site": "0048e098",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "old": {
      "definition_site": "0048e19c",
      "incomplete_value": true,
      "site": "0048e19c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004b0edc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b0f20",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b1024",
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
      "004b0edc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b0f20",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b1024",
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

- 旧版 [`0048e054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048df5c.md#insn-0048e054) · [`0048e098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048df5c.md#insn-0048e098) · [`0048e19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048df5c.md#insn-0048e19c)
- 新版 [`004b0eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0df4.md#insn-004b0eec) · [`004b0f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0df4.md#insn-004b0f30) · [`004b1034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0df4.md#insn-004b1034)

~~~diff
- 0048e054 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048e054 ["INT_ADD", "register:40f0:8", ["const:48e054:8", "const:4:8"]]
- 0048e054 ["CALLIND", null, ["register:0:8"]]
+ 004b0eec ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0eec ["INT_ADD", "register:40f0:8", ["const:4b0eec:8", "const:4:8"]]
+ 004b0eec ["CALLIND", null, ["register:0:8"]]
- 0048e054 bytes 20013fd6
+ 004b0eec bytes 20013fd6
- 0048e098 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048e098 ["INT_ADD", "register:40f0:8", ["const:48e098:8", "const:4:8"]]
- 0048e098 ["CALLIND", null, ["register:0:8"]]
+ 004b0f30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0f30 ["INT_ADD", "register:40f0:8", ["const:4b0f30:8", "const:4:8"]]
+ 004b0f30 ["CALLIND", null, ["register:0:8"]]
- 0048e098 bytes 20013fd6
+ 004b0f30 bytes 20013fd6
- 0048e19c ["COPY", "register:0:8", ["register:4048:8"]]
- 0048e19c ["INT_ADD", "register:40f0:8", ["const:48e19c:8", "const:4:8"]]
- 0048e19c ["CALLIND", null, ["register:0:8"]]
+ 004b1034 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b1034 ["INT_ADD", "register:40f0:8", ["const:4b1034:8", "const:4:8"]]
+ 004b1034 ["CALLIND", null, ["register:0:8"]]
- 0048e19c bytes 20013fd6
+ 004b1034 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f9b1c9894394ee4fff12c0e66f2c81e"></a>

### [`0048e640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e640.md) → [`004b14d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b14d8.md) _ZN5Botan11BER_Decoder26decode_constrained_integerENS_8ASN1_TagES1_m

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048e798",
      "incomplete_value": true,
      "site": "0048e798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "0048e800",
      "incomplete_value": false,
      "site": "0048e808",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b16b0",
      "value": [
        "leaf",
        "ram:c58450:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048e818",
      "value": [
        "leaf",
        "ram:bdba00:8"
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
      "004b1620",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b1698",
      "PARAM",
      [
        "storage",
        "002979a8",
        null,
        "string"
      ]
    ],
    [
      "004b16b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba00"
      ]
    ]
  ],
  "added": [
    [
      "004b1620",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b1698",
      "PARAM",
      [
        "storage",
        "002a7601",
        null,
        "string"
      ]
    ],
    [
      "004b16b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58450"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048e798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e640.md#insn-0048e798) · [`0048e808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e640.md#insn-0048e808) · [`0048e818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e640.md#insn-0048e818)
- 新版 [`004b1630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b14d8.md#insn-004b1630) · [`004b16a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b14d8.md#insn-004b16a0) · [`004b16b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b14d8.md#insn-004b16b0)

~~~diff
- 0048e798 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048e798 ["INT_ADD", "register:40f0:8", ["const:48e798:8", "const:4:8"]]
- 0048e798 ["CALLIND", null, ["register:0:8"]]
+ 004b1630 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b1630 ["INT_ADD", "register:40f0:8", ["const:4b1630:8", "const:4:8"]]
+ 004b1630 ["CALLIND", null, ["register:0:8"]]
- 0048e798 bytes 20013fd6
+ 004b1630 bytes 20013fd6
- 0048e808 ["INT_ADD", "register:40f0:8", ["const:48e808:8", "const:4:8"]]
- 0048e808 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b16a0 ["INT_ADD", "register:40f0:8", ["const:4b16a0:8", "const:4:8"]]
+ 004b16a0 ["CALL", null, ["callee:0043dd98:8"]]
- 0048e808 bytes a432fe97
+ 004b16a0 bytes be31fe97
- 0048e818 ["INT_ADD", "register:40f0:8", ["const:48e818:8", "const:4:8"]]
- 0048e818 ["CALL", null, ["ram:bdba00:8"]]
+ 004b16b0 ["INT_ADD", "register:40f0:8", ["const:4b16b0:8", "const:4:8"]]
+ 004b16b0 ["CALL", null, ["ram:c58450:8"]]
- 0048e818 bytes 7a341d94
+ 004b16b0 bytes 689b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f82bf6d680b3541de618418f8e00b971"></a>

### [`0048e994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e994.md) → [`004b182c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b182c.md) _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEENS_8ASN1_TagES7_S7_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc30.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`0051e054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e054.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c58680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58680.md) · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00540eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540eec.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.96% / 新版 93.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 3件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048eaa0",
      "incomplete_value": true,
      "site": "0048eaa0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0048eae8",
      "incomplete_value": false,
      "site": "0048eaf0",
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
            "const:8a9:8"
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
      "site": "004b199c",
      "value": [
        "leaf",
        "ram:c586f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048eb04",
      "value": [
        "leaf",
        "ram:bdbca0:8"
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
      "004b1928",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b1980",
      "PARAM",
      [
        "storage",
        "002958a9",
        null,
        "string"
      ]
    ],
    [
      "004b199c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbca0"
      ]
    ]
  ],
  "added": [
    [
      "004b1928",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b1980",
      "PARAM",
      [
        "storage",
        "002a52e2",
        null,
        "string"
      ]
    ],
    [
      "004b199c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c586f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048eaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e994.md#insn-0048eaa0) · [`0048eaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e994.md#insn-0048eaf0) · [`0048eb04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e994.md#insn-0048eb04)
- 新版 [`004b1938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b182c.md#insn-004b1938) · [`004b1988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b182c.md#insn-004b1988) · [`004b199c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b182c.md#insn-004b199c)

~~~diff
- 0048eaa0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048eaa0 ["INT_ADD", "register:40f0:8", ["const:48eaa0:8", "const:4:8"]]
- 0048eaa0 ["CALLIND", null, ["register:0:8"]]
+ 004b1938 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b1938 ["INT_ADD", "register:40f0:8", ["const:4b1938:8", "const:4:8"]]
+ 004b1938 ["CALLIND", null, ["register:0:8"]]
- 0048eaa0 bytes 20013fd6
+ 004b1938 bytes 20013fd6
- 0048eaf0 ["INT_ADD", "register:40f0:8", ["const:48eaf0:8", "const:4:8"]]
- 0048eaf0 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b1988 ["INT_ADD", "register:40f0:8", ["const:4b1988:8", "const:4:8"]]
+ 004b1988 ["CALL", null, ["callee:0043dd98:8"]]
- 0048eaf0 bytes ea31fe97
+ 004b1988 bytes 0431fe97
- 0048eb04 ["INT_ADD", "register:40f0:8", ["const:48eb04:8", "const:4:8"]]
- 0048eb04 ["CALL", null, ["ram:bdbca0:8"]]
+ 004b199c ["INT_ADD", "register:40f0:8", ["const:4b199c:8", "const:4:8"]]
+ 004b199c ["CALL", null, ["ram:c586f0:8"]]
- 0048eb04 bytes 67341d94
+ 004b199c bytes 559b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c80de62055b87716ea2ec81ce86856bc"></a>

### [`0048ec7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048ec7c.md) → [`004b1b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1b14.md) _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS1_9allocatorIhEEEENS_8ASN1_TagES7_S7_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdba50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba50.md) · 呼出先 18件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051e1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e1b4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c584a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c584a0.md) · 呼出先 18件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`0054104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/0054104c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.34% / 新版 95.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 3件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048ee18",
      "incomplete_value": true,
      "site": "0048ee18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "0048ee68",
      "incomplete_value": false,
      "site": "0048ee70",
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
            "const:8a9:8"
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
      "site": "004b1d1c",
      "value": [
        "leaf",
        "ram:c586f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048ee84",
      "value": [
        "leaf",
        "ram:bdbca0:8"
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
      "004b1ca0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b1d00",
      "PARAM",
      [
        "storage",
        "002958a9",
        null,
        "string"
      ]
    ],
    [
      "004b1d1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbca0"
      ]
    ]
  ],
  "added": [
    [
      "004b1ca0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b1d00",
      "PARAM",
      [
        "storage",
        "002a52e2",
        null,
        "string"
      ]
    ],
    [
      "004b1d1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c586f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048ee18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048ec7c.md#insn-0048ee18) · [`0048ee70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048ec7c.md#insn-0048ee70) · [`0048ee84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048ec7c.md#insn-0048ee84)
- 新版 [`004b1cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1b14.md#insn-004b1cb0) · [`004b1d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1b14.md#insn-004b1d08) · [`004b1d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1b14.md#insn-004b1d1c)

~~~diff
- 0048ee18 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048ee18 ["INT_ADD", "register:40f0:8", ["const:48ee18:8", "const:4:8"]]
- 0048ee18 ["CALLIND", null, ["register:0:8"]]
+ 004b1cb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b1cb0 ["INT_ADD", "register:40f0:8", ["const:4b1cb0:8", "const:4:8"]]
+ 004b1cb0 ["CALLIND", null, ["register:0:8"]]
- 0048ee18 bytes 20013fd6
+ 004b1cb0 bytes 20013fd6
- 0048ee70 ["INT_ADD", "register:40f0:8", ["const:48ee70:8", "const:4:8"]]
- 0048ee70 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b1d08 ["INT_ADD", "register:40f0:8", ["const:4b1d08:8", "const:4:8"]]
+ 004b1d08 ["CALL", null, ["callee:0043dd98:8"]]
- 0048ee70 bytes 0a31fe97
+ 004b1d08 bytes 2430fe97
- 0048ee84 ["INT_ADD", "register:40f0:8", ["const:48ee84:8", "const:4:8"]]
- 0048ee84 ["CALL", null, ["ram:bdbca0:8"]]
+ 004b1d1c ["INT_ADD", "register:40f0:8", ["const:4b1d1c:8", "const:4:8"]]
+ 004b1d1c ["CALL", null, ["ram:c586f0:8"]]
- 0048ee84 bytes 87331d94
+ 004b1d1c bytes 759a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ad034f5092a22320aedabdbcf9f70a9"></a>

### [`0048f014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f014.md) → [`004b1eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md) _ZN5Botan11DER_Encoder12DER_Sequence12get_contentsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8a0.md) · 呼出先 8件 [`0048f37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f37c.md) [`0048f6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f6e8.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`0051e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c582f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582f0.md) · 呼出先 8件 [`004b2214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md) [`004b2580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2580.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "0048f174",
      "incomplete_value": true,
      "site": "0048f174",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048f20c",
      "incomplete_value": true,
      "site": "0048f20c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048f298",
      "incomplete_value": true,
      "site": "0048f298",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b1ffc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b2094",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b2120",
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
      "004b1ffc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b2094",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b2120",
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

- 旧版 [`0048f174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f014.md#insn-0048f174) · [`0048f20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f014.md#insn-0048f20c) · [`0048f298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f014.md#insn-0048f298)
- 新版 [`004b200c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md#insn-004b200c) · [`004b20a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md#insn-004b20a4) · [`004b2130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md#insn-004b2130)

~~~diff
- 0048f174 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048f174 ["INT_ADD", "register:40f0:8", ["const:48f174:8", "const:4:8"]]
- 0048f174 ["CALLIND", null, ["register:0:8"]]
+ 004b200c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b200c ["INT_ADD", "register:40f0:8", ["const:4b200c:8", "const:4:8"]]
+ 004b200c ["CALLIND", null, ["register:0:8"]]
- 0048f174 bytes 20013fd6
+ 004b200c bytes 20013fd6
- 0048f20c ["COPY", "register:0:8", ["register:4048:8"]]
- 0048f20c ["INT_ADD", "register:40f0:8", ["const:48f20c:8", "const:4:8"]]
- 0048f20c ["CALLIND", null, ["register:0:8"]]
+ 004b20a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b20a4 ["INT_ADD", "register:40f0:8", ["const:4b20a4:8", "const:4:8"]]
+ 004b20a4 ["CALLIND", null, ["register:0:8"]]
- 0048f20c bytes 20013fd6
+ 004b20a4 bytes 20013fd6
- 0048f298 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048f298 ["INT_ADD", "register:40f0:8", ["const:48f298:8", "const:4:8"]]
- 0048f298 ["CALLIND", null, ["register:0:8"]]
+ 004b2130 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2130 ["INT_ADD", "register:40f0:8", ["const:4b2130:8", "const:4:8"]]
+ 004b2130 ["CALLIND", null, ["register:0:8"]]
- 0048f298 bytes 20013fd6
+ 004b2130 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05b4fd273d8260ebba6f6c991a25ffd2"></a>

### [`0048f37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f37c.md) → [`004b2214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md) FUN_004b2214

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0048a5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a5d8.md) [`0048f014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f014.md) · 呼出先 9件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051e2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e2cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 2件 [`004ad470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad470.md) [`004b1eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md) · 呼出先 9件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00541164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
    "old": {
      "definition_site": "0048f408",
      "incomplete_value": false,
      "site": "0048f428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:4b2:8"
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
    "old": {
      "definition_site": "0048f410",
      "incomplete_value": false,
      "site": "0048f428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:6f3:8"
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
    "old": {
      "definition_site": "0048f418",
      "incomplete_value": false,
      "site": "0048f428",
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
            "const:e88:8"
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
      "004b22a0",
      "PARAM",
      [
        "storage",
        "002aa4b2",
        null,
        "string"
      ]
    ],
    [
      "004b22a8",
      "PARAM",
      [
        "storage",
        "002926f3",
        null,
        "string"
      ]
    ],
    [
      "004b22b0",
      "PARAM",
      [
        "storage",
        "00298e88",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b22a0",
      "PARAM",
      [
        "storage",
        "002bb22e",
        null,
        "string"
      ]
    ],
    [
      "004b22a8",
      "PARAM",
      [
        "storage",
        "002a1e03",
        null,
        "string"
      ]
    ],
    [
      "004b22b0",
      "PARAM",
      [
        "storage",
        "002a8c46",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048f428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f37c.md#insn-0048f428) · [`0048f5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f37c.md#insn-0048f5fc) · [`0048f650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f37c.md#insn-0048f650)
- 新版 [`004b22c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md#insn-004b22c0) · [`004b2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md#insn-004b2494) · [`004b24e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2214.md#insn-004b24e8)

~~~diff
- 0048f428 ["INT_ADD", "register:40f0:8", ["const:48f428:8", "const:4:8"]]
- 0048f428 ["CALL", null, ["callee:00c58250:8"]]
+ 004b22c0 ["INT_ADD", "register:40f0:8", ["const:4b22c0:8", "const:4:8"]]
+ 004b22c0 ["CALL", null, ["callee:00c58250:8"]]
- 0048f428 bytes f6301d94
+ 004b22c0 bytes e4971e94
- 0048f5fc ["INT_ADD", "register:40f0:8", ["const:48f5fc:8", "const:4:8"]]
- 0048f5fc ["CALL", null, ["callee:00c57b60:8"]]
+ 004b2494 ["INT_ADD", "register:40f0:8", ["const:4b2494:8", "const:4:8"]]
+ 004b2494 ["CALL", null, ["callee:00c57b60:8"]]
- 0048f5fc bytes c52e1d94
+ 004b2494 bytes b3951e94
- 0048f650 ["INT_ADD", "register:40f0:8", ["const:48f650:8", "const:4:8"]]
- 0048f650 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b24e8 ["INT_ADD", "register:40f0:8", ["const:4b24e8:8", "const:4:8"]]
+ 004b24e8 ["CALL", null, ["callee:00c57b10:8"]]
- 0048f650 bytes 9c2e1d94
+ 004b24e8 bytes 8a951e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fab21e92da46e8069ad507aa4de47044"></a>

### [`0048fa0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fa0c.md) → [`004b28a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b28a4.md) _ZN5Botan11DER_Encoder12get_contentsEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb950.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c583a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583a0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

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
    "old": {
      "definition_site": "0048fa88",
      "incomplete_value": false,
      "site": "0048fa90",
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
            "const:17c:8"
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
    "old": {
      "definition_site": "0048fac4",
      "incomplete_value": true,
      "site": "0048fad0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b2958",
      "incomplete_value": false,
      "site": "004b2968",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048fac0",
      "incomplete_value": false,
      "site": "0048fad0",
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
      "004b2920",
      "PARAM",
      [
        "storage",
        "002a817c",
        null,
        "string"
      ]
    ],
    [
      "004b2958",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004b295c",
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
      "004b2920",
      "PARAM",
      [
        "storage",
        "002b8e1e",
        null,
        "string"
      ]
    ],
    [
      "004b2958",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b295c",
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

- 旧版 [`0048fa90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fa0c.md#insn-0048fa90) · [`0048fad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fa0c.md#insn-0048fad0) · [`0048fa7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fa0c.md#insn-0048fa7c)
- 新版 [`004b2928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b28a4.md#insn-004b2928) · [`004b2968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b28a4.md#insn-004b2968) · [`004b2914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b28a4.md#insn-004b2914)

~~~diff
- 0048fa90 ["INT_ADD", "register:40f0:8", ["const:48fa90:8", "const:4:8"]]
- 0048fa90 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b2928 ["INT_ADD", "register:40f0:8", ["const:4b2928:8", "const:4:8"]]
+ 004b2928 ["CALL", null, ["callee:0043dd98:8"]]
- 0048fa90 bytes 022efe97
+ 004b2928 bytes 1c2dfe97
- 0048fad0 ["INT_ADD", "register:40f0:8", ["const:48fad0:8", "const:4:8"]]
- 0048fad0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b2968 ["INT_ADD", "register:40f0:8", ["const:4b2968:8", "const:4:8"]]
+ 004b2968 ["CALL", null, ["callee:00c57b10:8"]]
- 0048fad0 bytes 7c2d1d94
+ 004b2968 bytes 6a941e94
- 0048fa7c ["INT_ADD", "register:40f0:8", ["const:48fa7c:8", "const:4:8"]]
- 0048fa7c ["CALL", null, ["callee:00c57af0:8"]]
+ 004b2914 ["INT_ADD", "register:40f0:8", ["const:4b2914:8", "const:4:8"]]
+ 004b2914 ["CALL", null, ["callee:00c57af0:8"]]
- 0048fa7c bytes 892d1d94
+ 004b2914 bytes 77941e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b816f58eb10127d446d53120a858cdc5"></a>

### [`0048fb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fb24.md) → [`004b29bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b29bc.md) FUN_004b29bc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
    "old": {
      "definition_site": "0048fb8c",
      "incomplete_value": true,
      "site": "0048fb8c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0048fbc8",
      "incomplete_value": true,
      "site": "0048fbc8",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b2a14",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b2a50",
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
      "004b2a14",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b2a50",
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

- 旧版 [`0048fb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fb24.md#insn-0048fb8c) · [`0048fbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fb24.md#insn-0048fbc8) · [`0048fb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fb24.md#insn-0048fb40)
- 新版 [`004b2a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b29bc.md#insn-004b2a24) · [`004b2a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b29bc.md#insn-004b2a60) · [`004b29d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b29bc.md#insn-004b29d8)

~~~diff
- 0048fb8c ["COPY", "register:0:8", ["register:4048:8"]]
- 0048fb8c ["INT_ADD", "register:40f0:8", ["const:48fb8c:8", "const:4:8"]]
- 0048fb8c ["CALLIND", null, ["register:0:8"]]
+ 004b2a24 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2a24 ["INT_ADD", "register:40f0:8", ["const:4b2a24:8", "const:4:8"]]
+ 004b2a24 ["CALLIND", null, ["register:0:8"]]
- 0048fb8c bytes 20013fd6
+ 004b2a24 bytes 20013fd6
- 0048fbc8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048fbc8 ["INT_ADD", "register:40f0:8", ["const:48fbc8:8", "const:4:8"]]
- 0048fbc8 ["CALLIND", null, ["register:0:8"]]
+ 004b2a60 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2a60 ["INT_ADD", "register:40f0:8", ["const:4b2a60:8", "const:4:8"]]
+ 004b2a60 ["CALLIND", null, ["register:0:8"]]
- 0048fbc8 bytes 20013fd6
+ 004b2a60 bytes 20013fd6
- 0048fb40 ["COPY", "register:40a8:8", ["const:bea000:8"]]
+ 004b29d8 ["COPY", "register:40a8:8", ["const:c67000:8"]]
- 0048fb40 bytes d53a00f0
+ 004b29d8 bytes b53d00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdb7240e5d87d10ab09a09fb0eb6e071"></a>

### [`0048fc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fc00.md) → [`004b2a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2a98.md) _ZN5Botan11DER_Encoder14start_explicitEt

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
    "old": {
      "definition_site": "0048fc68",
      "incomplete_value": false,
      "site": "0048fc70",
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
            "const:454:8"
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
    "old": {
      "definition_site": "0048fca4",
      "incomplete_value": true,
      "site": "0048fcb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8:8"
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
      "definition_site": "004b2b38",
      "incomplete_value": false,
      "site": "004b2b48",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0048fca0",
      "incomplete_value": false,
      "site": "0048fcb0",
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
      "004b2b00",
      "PARAM",
      [
        "storage",
        "0029f454",
        null,
        "string"
      ]
    ],
    [
      "004b2b38",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004b2b3c",
      "READ",
      [
        "storage",
        "00c1b008",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b2b00",
      "PARAM",
      [
        "storage",
        "002af867",
        null,
        "string"
      ]
    ],
    [
      "004b2b38",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b2b3c",
      "READ",
      [
        "storage",
        "00c9a9f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048fc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fc00.md#insn-0048fc70) · [`0048fcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fc00.md#insn-0048fcb0) · [`0048fc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fc00.md#insn-0048fc5c)
- 新版 [`004b2b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2a98.md#insn-004b2b08) · [`004b2b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2a98.md#insn-004b2b48) · [`004b2af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2a98.md#insn-004b2af4)

~~~diff
- 0048fc70 ["INT_ADD", "register:40f0:8", ["const:48fc70:8", "const:4:8"]]
- 0048fc70 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b2b08 ["INT_ADD", "register:40f0:8", ["const:4b2b08:8", "const:4:8"]]
+ 004b2b08 ["CALL", null, ["callee:0043dd98:8"]]
- 0048fc70 bytes 8a2dfe97
+ 004b2b08 bytes a42cfe97
- 0048fcb0 ["INT_ADD", "register:40f0:8", ["const:48fcb0:8", "const:4:8"]]
- 0048fcb0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b2b48 ["INT_ADD", "register:40f0:8", ["const:4b2b48:8", "const:4:8"]]
+ 004b2b48 ["CALL", null, ["callee:00c57b10:8"]]
- 0048fcb0 bytes 042d1d94
+ 004b2b48 bytes f2931e94
- 0048fc5c ["INT_ADD", "register:40f0:8", ["const:48fc5c:8", "const:4:8"]]
- 0048fc5c ["CALL", null, ["callee:00c57af0:8"]]
+ 004b2af4 ["INT_ADD", "register:40f0:8", ["const:4b2af4:8", "const:4:8"]]
+ 004b2af4 ["CALL", null, ["callee:00c57af0:8"]]
- 0048fc5c bytes 112d1d94
+ 004b2af4 bytes ff931e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1557e0e11f7acada0b94a6b7282784cc"></a>

### [`0048ff2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048ff2c.md) → [`004b2dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2dc4.md) _ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcc0.md) · 呼出先 8件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md)
- 新版 呼出元 1件 [`00c58710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58710.md) · 呼出先 8件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58420.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md)

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
    "old": {
      "definition_site": "0048ffa8",
      "incomplete_value": true,
      "site": "0048ffa8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "old": {
      "definition_site": "0049013c",
      "incomplete_value": true,
      "site": "0049013c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
    "old": {
      "definition_site": "004901e8",
      "incomplete_value": true,
      "site": "004901e8",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b2e30",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b2fc4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b3070",
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
      "004b2e30",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b2fc4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b3070",
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

- 旧版 [`0048ffa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048ff2c.md#insn-0048ffa8) · [`0049013c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048ff2c.md#insn-0049013c) · [`004901e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048ff2c.md#insn-004901e8)
- 新版 [`004b2e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2dc4.md#insn-004b2e40) · [`004b2fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2dc4.md#insn-004b2fd4) · [`004b3080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2dc4.md#insn-004b3080)

~~~diff
- 0048ffa8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0048ffa8 ["INT_ADD", "register:40f0:8", ["const:48ffa8:8", "const:4:8"]]
- 0048ffa8 ["CALLIND", null, ["register:0:8"]]
+ 004b2e40 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2e40 ["INT_ADD", "register:40f0:8", ["const:4b2e40:8", "const:4:8"]]
+ 004b2e40 ["CALLIND", null, ["register:0:8"]]
- 0048ffa8 bytes 20013fd6
+ 004b2e40 bytes 20013fd6
- 0049013c ["COPY", "register:0:8", ["register:4048:8"]]
- 0049013c ["INT_ADD", "register:40f0:8", ["const:49013c:8", "const:4:8"]]
- 0049013c ["CALLIND", null, ["register:0:8"]]
+ 004b2fd4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2fd4 ["INT_ADD", "register:40f0:8", ["const:4b2fd4:8", "const:4:8"]]
+ 004b2fd4 ["CALLIND", null, ["register:0:8"]]
- 0049013c bytes 20013fd6
+ 004b2fd4 bytes 20013fd6
- 004901e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004901e8 ["INT_ADD", "register:40f0:8", ["const:4901e8:8", "const:4:8"]]
- 004901e8 ["CALLIND", null, ["register:0:8"]]
+ 004b3080 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b3080 ["INT_ADD", "register:40f0:8", ["const:4b3080:8", "const:4:8"]]
+ 004b3080 ["CALLIND", null, ["register:0:8"]]
- 004901e8 bytes 20013fd6
+ 004b3080 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19cd8d0a5f215a02407c23b043367c64"></a>

### [`00490274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490274.md) → [`004b310c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b310c.md) _ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbce0.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`0051e2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e2cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c58730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58730.md) · 呼出先 12件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00541164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "00490384",
      "incomplete_value": true,
      "site": "00490384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004903d0",
      "incomplete_value": false,
      "site": "004903d8",
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
            "const:5d7:8"
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
    "old": {
      "definition_site": "00490408",
      "incomplete_value": true,
      "site": "00490414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004b320c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b3268",
      "PARAM",
      [
        "storage",
        "002945d7",
        null,
        "string"
      ]
    ],
    [
      "004b329c",
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
      "004b320c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b3268",
      "PARAM",
      [
        "storage",
        "002a3eed",
        null,
        "string"
      ]
    ],
    [
      "004b329c",
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

- 旧版 [`00490384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490274.md#insn-00490384) · [`004903d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490274.md#insn-004903d8) · [`00490414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490274.md#insn-00490414)
- 新版 [`004b321c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b310c.md#insn-004b321c) · [`004b3270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b310c.md#insn-004b3270) · [`004b32ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b310c.md#insn-004b32ac)

~~~diff
- 00490384 ["COPY", "register:0:8", ["register:4048:8"]]
- 00490384 ["INT_ADD", "register:40f0:8", ["const:490384:8", "const:4:8"]]
- 00490384 ["CALLIND", null, ["register:0:8"]]
+ 004b321c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b321c ["INT_ADD", "register:40f0:8", ["const:4b321c:8", "const:4:8"]]
+ 004b321c ["CALLIND", null, ["register:0:8"]]
- 00490384 bytes 20013fd6
+ 004b321c bytes 20013fd6
- 004903d8 ["INT_ADD", "register:40f0:8", ["const:4903d8:8", "const:4:8"]]
- 004903d8 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b3270 ["INT_ADD", "register:40f0:8", ["const:4b3270:8", "const:4:8"]]
+ 004b3270 ["CALL", null, ["callee:0043dd98:8"]]
- 004903d8 bytes b02bfe97
+ 004b3270 bytes ca2afe97
- 00490414 ["INT_ADD", "register:40f0:8", ["const:490414:8", "const:4:8"]]
- 00490414 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b32ac ["INT_ADD", "register:40f0:8", ["const:4b32ac:8", "const:4:8"]]
+ 004b32ac ["CALL", null, ["callee:00c57b10:8"]]
- 00490414 bytes 2b2b1d94
+ 004b32ac bytes 19921e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-395067149f573108fc4f5598cda0b406"></a>

### [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) → [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) FUN_004b34c8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 55件 [`0048df5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048df5c.md) [`0048ff2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048ff2c.md) [`00490728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490728.md) [`00491f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491f34.md) [`00492804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492804.md) · 呼出先 7件 [`00513fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513fb0.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 55件 [`004b0df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0df4.md) [`004b2dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b2dc4.md) [`004b35c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b35c0.md) [`004b4dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4dcc.md) [`004b569c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b569c.md) · 呼出先 7件 [`00536e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536e48.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b357c",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004906e4",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004906f4",
      "incomplete_value": true,
      "site": "004906fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
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
    "old": {
      "definition_site": "004906f8",
      "incomplete_value": true,
      "site": "004906fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:c1b000:8"
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
      "004b357c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "004b358c",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004b358c",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004b357c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "004b358c",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004b358c",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004906e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md#insn-004906e4) · [`004906fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md#insn-004906fc) · [`00490678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md#insn-00490678)
- 新版 [`004b357c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md#insn-004b357c) · [`004b3594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md#insn-004b3594) · [`004b3510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md#insn-004b3510)

~~~diff
- 004906e4 ["INT_ADD", "register:40f0:8", ["const:4906e4:8", "const:4:8"]]
- 004906e4 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004b357c ["INT_ADD", "register:40f0:8", ["const:4b357c:8", "const:4:8"]]
+ 004b357c ["CALL", null, ["ram:c58640:8"]]
- 004906e4 bytes 432d1d94
+ 004b357c bytes 31941e94
- 004906fc ["INT_ADD", "register:40f0:8", ["const:4906fc:8", "const:4:8"]]
- 004906fc ["CALL", null, ["callee:00c57b10:8"]]
+ 004b3594 ["INT_ADD", "register:40f0:8", ["const:4b3594:8", "const:4:8"]]
+ 004b3594 ["CALL", null, ["callee:00c57b10:8"]]
- 004906fc bytes 712a1d94
+ 004b3594 bytes 5f911e94
- 00490678 ["INT_ADD", "register:40f0:8", ["const:490678:8", "const:4:8"]]
- 00490678 ["CALL", null, ["callee:00c58630:8"]]
+ 004b3510 ["INT_ADD", "register:40f0:8", ["const:4b3510:8", "const:4:8"]]
+ 004b3510 ["CALL", null, ["callee:00c58630:8"]]
- 00490678 bytes 5a2d1d94
+ 004b3510 bytes 48941e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1a5dddf38ef85d70ff9bfc4d41992ec"></a>

### [`00490728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490728.md) → [`004b35c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b35c0.md) _ZN5Botan6BigInt6encodeEPhRKS0_NS0_4BaseE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb00.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58550.md) · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00490a68",
      "incomplete_value": true,
      "site": "00490a68",
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b3668",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004907d0",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "00490a1c",
      "incomplete_value": true,
      "site": "00490a1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004b3668",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004b387c",
      "DATA",
      [
        "storage",
        "002b0bc0",
        null,
        null
      ]
    ],
    [
      "004b3884",
      "DATA",
      [
        "storage",
        "002b0bc0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b3668",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004b387c",
      "DATA",
      [
        "storage",
        "002c21b0",
        null,
        null
      ]
    ],
    [
      "004b3884",
      "DATA",
      [
        "storage",
        "002c21b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004907d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490728.md#insn-004907d0) · [`00490a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490728.md#insn-00490a1c) · [`00490ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490728.md#insn-00490ab8)
- 新版 [`004b3668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b35c0.md#insn-004b3668) · [`004b38b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b35c0.md#insn-004b38b4) · [`004b3950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b35c0.md#insn-004b3950)

~~~diff
- 004907d0 ["INT_ADD", "register:40f0:8", ["const:4907d0:8", "const:4:8"]]
- 004907d0 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004b3668 ["INT_ADD", "register:40f0:8", ["const:4b3668:8", "const:4:8"]]
+ 004b3668 ["CALL", null, ["ram:c58740:8"]]
- 004907d0 bytes 482d1d94
+ 004b3668 bytes 36941e94
- 00490a1c ["COPY", "register:0:8", ["register:4048:8"]]
- 00490a1c ["INT_ADD", "register:40f0:8", ["const:490a1c:8", "const:4:8"]]
- 00490a1c ["CALLIND", null, ["register:0:8"]]
+ 004b38b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b38b4 ["INT_ADD", "register:40f0:8", ["const:4b38b4:8", "const:4:8"]]
+ 004b38b4 ["CALLIND", null, ["register:0:8"]]
- 00490a1c bytes 20013fd6
+ 004b38b4 bytes 20013fd6
- 00490ab8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00490ab8 ["INT_ADD", "register:40f0:8", ["const:490ab8:8", "const:4:8"]]
- 00490ab8 ["CALLIND", null, ["register:0:8"]]
+ 004b3950 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b3950 ["INT_ADD", "register:40f0:8", ["const:4b3950:8", "const:4:8"]]
+ 004b3950 ["CALLIND", null, ["register:0:8"]]
- 00490ab8 bytes 20013fd6
+ 004b3950 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef4c8fb16bcb5426310eae3de630b13e"></a>

### [`0049100c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/0049100c.md) → [`004b3ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md) _ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bdbd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd30.md) [`00bdbef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbef0.md) · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`0045efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045efa8.md) [`004918d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/004918d4.md)
- 新版 呼出元 2件 [`00c58780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58780.md) [`00c58940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58940.md) · 呼出先 19件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00481e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md) [`004b476c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b476c.md)

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
    "old": {
      "definition_site": "004910a0",
      "incomplete_value": false,
      "site": "004910ac",
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
            "const:9a2:8"
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
    "old": {
      "definition_site": "004910b4",
      "incomplete_value": false,
      "site": "004910bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:7e1:8"
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
    "old": {
      "definition_site": "00491624",
      "incomplete_value": false,
      "site": "00491630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:57b:8"
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
      "004b3f38",
      "PARAM",
      [
        "storage",
        "002959a2",
        null,
        "string"
      ]
    ],
    [
      "004b3f4c",
      "PARAM",
      [
        "storage",
        "002ac7e1",
        null,
        null
      ]
    ],
    [
      "004b3fd0",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004b3f38",
      "PARAM",
      [
        "storage",
        "002a53db",
        null,
        "string"
      ]
    ],
    [
      "004b3f4c",
      "PARAM",
      [
        "storage",
        "002bd859",
        null,
        null
      ]
    ],
    [
      "004b3fd0",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004910ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/0049100c.md#insn-004910ac) · [`004910bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/0049100c.md#insn-004910bc) · [`00491630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/0049100c.md#insn-00491630)
- 新版 [`004b3f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md#insn-004b3f44) · [`004b3f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md#insn-004b3f54) · [`004b44c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md#insn-004b44c8)

~~~diff
- 004910ac ["INT_ADD", "register:40f0:8", ["const:4910ac:8", "const:4:8"]]
- 004910ac ["CALL", null, ["callee:00c57cb0:8"]]
+ 004b3f44 ["INT_ADD", "register:40f0:8", ["const:4b3f44:8", "const:4:8"]]
+ 004b3f44 ["CALL", null, ["callee:00c57cb0:8"]]
- 004910ac bytes 6d281d94
+ 004b3f44 bytes 5b8f1e94
- 004910bc ["INT_ADD", "register:40f0:8", ["const:4910bc:8", "const:4:8"]]
- 004910bc ["CALL", null, ["callee:00c57b70:8"]]
+ 004b3f54 ["INT_ADD", "register:40f0:8", ["const:4b3f54:8", "const:4:8"]]
+ 004b3f54 ["CALL", null, ["callee:00c57b70:8"]]
- 004910bc bytes 19281d94
+ 004b3f54 bytes 078f1e94
- 00491630 ["INT_ADD", "register:40f0:8", ["const:491630:8", "const:4:8"]]
- 00491630 ["CALL", null, ["callee:00481e40:8"]]
+ 004b44c8 ["INT_ADD", "register:40f0:8", ["const:4b44c8:8", "const:4:8"]]
+ 004b44c8 ["CALL", null, ["callee:00481e40:8"]]
- 00491630 bytes 5e36ff97
+ 004b44c8 bytes 5e36ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a6485b765aa33c83517541e5441f714"></a>

### [`004918d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/004918d4.md) → [`004b476c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b476c.md) FUN_004b476c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049100c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/0049100c.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`004b3ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

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
    "old": {
      "definition_site": "00491a18",
      "incomplete_value": false,
      "site": "00491a1c",
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
            "const:5c9:8"
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
    "old": {
      "definition_site": "00491a88",
      "incomplete_value": false,
      "site": "00491a8c",
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
      "004b4860",
      "PARAM",
      [
        "storage",
        "0029f5cf",
        null,
        null
      ]
    ],
    [
      "004b48b0",
      "PARAM",
      [
        "storage",
        "002a25c9",
        null,
        null
      ]
    ],
    [
      "004b4920",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b4860",
      "PARAM",
      [
        "storage",
        "002af9e2",
        null,
        null
      ]
    ],
    [
      "004b48b0",
      "PARAM",
      [
        "storage",
        "002b2c8a",
        null,
        null
      ]
    ],
    [
      "004b4920",
      "PARAM",
      [
        "storage",
        "002a998f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00491a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/004918d4.md#insn-00491a1c) · [`00491a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/004918d4.md#insn-00491a8c) · [`00491938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/004918d4.md#insn-00491938)
- 新版 [`004b48b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b476c.md#insn-004b48b4) · [`004b4924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b476c.md#insn-004b4924) · [`004b47d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b476c.md#insn-004b47d0)

~~~diff
- 00491a1c ["INT_ADD", "register:40f0:8", ["const:491a1c:8", "const:4:8"]]
- 00491a1c ["CALL", null, ["callee:00c57cb0:8"]]
+ 004b48b4 ["INT_ADD", "register:40f0:8", ["const:4b48b4:8", "const:4:8"]]
+ 004b48b4 ["CALL", null, ["callee:00c57cb0:8"]]
- 00491a1c bytes 11261d94
+ 004b48b4 bytes ff8c1e94
- 00491a8c ["INT_ADD", "register:40f0:8", ["const:491a8c:8", "const:4:8"]]
- 00491a8c ["CALL", null, ["callee:00c57b70:8"]]
+ 004b4924 ["INT_ADD", "register:40f0:8", ["const:4b4924:8", "const:4:8"]]
+ 004b4924 ["CALL", null, ["callee:00c57b70:8"]]
- 00491a8c bytes a5251d94
+ 004b4924 bytes 938c1e94
- 00491938 ["INT_ADD", "register:40f0:8", ["const:491938:8", "const:4:8"]]
- 00491938 ["CALL", null, ["callee:0043bae0:8"]]
+ 004b47d0 ["INT_ADD", "register:40f0:8", ["const:4b47d0:8", "const:4:8"]]
+ 004b47d0 ["CALL", null, ["callee:0043bae0:8"]]
- 00491938 bytes aa1dfe97
+ 004b47d0 bytes c41cfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a4e096dfde168889738d8cfe00bf5ca"></a>

### [`00491be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491be0.md) → [`004b4a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4a78.md) _ZNK5Botan9SCAN_Name3argEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd40.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58790.md) · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

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
    "old": {
      "definition_site": "00491cb4",
      "incomplete_value": false,
      "site": "00491cc0",
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
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00491ce0",
      "incomplete_value": false,
      "site": "00491ce8",
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
            "const:337:8"
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
    "old": {
      "definition_site": "00491d18",
      "incomplete_value": false,
      "site": "00491d20",
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
            "const:87b:8"
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
      "004b4b4c",
      "PARAM",
      [
        "storage",
        "002ab5a2",
        null,
        "string"
      ]
    ],
    [
      "004b4b78",
      "PARAM",
      [
        "storage",
        "002a3337",
        null,
        "string"
      ]
    ],
    [
      "004b4bb0",
      "PARAM",
      [
        "storage",
        "0029687b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b4b4c",
      "PARAM",
      [
        "storage",
        "002bc4c5",
        null,
        "string"
      ]
    ],
    [
      "004b4b78",
      "PARAM",
      [
        "storage",
        "002b3a11",
        null,
        "string"
      ]
    ],
    [
      "004b4bb0",
      "PARAM",
      [
        "storage",
        "002a63b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00491cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491be0.md#insn-00491cc0) · [`00491ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491be0.md#insn-00491ce8) · [`00491d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491be0.md#insn-00491d20)
- 新版 [`004b4b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4a78.md#insn-004b4b58) · [`004b4b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4a78.md#insn-004b4b80) · [`004b4bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b4/004b4a78.md#insn-004b4bb8)

~~~diff
- 00491cc0 ["INT_ADD", "register:40f0:8", ["const:491cc0:8", "const:4:8"]]
- 00491cc0 ["CALL", null, ["callee:00c57b60:8"]]
+ 004b4b58 ["INT_ADD", "register:40f0:8", ["const:4b4b58:8", "const:4:8"]]
+ 004b4b58 ["CALL", null, ["callee:00c57b60:8"]]
- 00491cc0 bytes 14251d94
+ 004b4b58 bytes 028c1e94
- 00491ce8 ["INT_ADD", "register:40f0:8", ["const:491ce8:8", "const:4:8"]]
- 00491ce8 ["CALL", null, ["callee:00c57b70:8"]]
+ 004b4b80 ["INT_ADD", "register:40f0:8", ["const:4b4b80:8", "const:4:8"]]
+ 004b4b80 ["CALL", null, ["callee:00c57b70:8"]]
- 00491ce8 bytes 0e251d94
+ 004b4b80 bytes fc8b1e94
- 00491d20 ["INT_ADD", "register:40f0:8", ["const:491d20:8", "const:4:8"]]
- 00491d20 ["CALL", null, ["callee:00c57b70:8"]]
+ 004b4bb8 ["INT_ADD", "register:40f0:8", ["const:4b4bb8:8", "const:4:8"]]
+ 004b4bb8 ["CALL", null, ["callee:00c57b70:8"]]
- 00491d20 bytes 00251d94
+ 004b4bb8 bytes ee8b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddc4dd1cddc0c18aa9d8e0edc1a96ae7"></a>

### [`00492480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492480.md) → [`004b5318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5318.md) _ZN5BotaneqERKNS_11OctetStringES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd60.md) · 呼出先 5件 [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00c587b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587b0.md) · 呼出先 5件 [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
    "old": {
      "definition_site": "00492538",
      "incomplete_value": true,
      "site": "00492538",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "00492564",
      "incomplete_value": true,
      "site": "00492564",
      "value": [
        "LOAD",
        "8",
        [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b53c0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b53ec",
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
      "004b53c0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b53ec",
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

- 旧版 [`00492538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492480.md#insn-00492538) · [`00492564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492480.md#insn-00492564) · [`004924bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492480.md#insn-004924bc)
- 新版 [`004b53d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5318.md#insn-004b53d0) · [`004b53fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5318.md#insn-004b53fc) · [`004b5354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5318.md#insn-004b5354)

~~~diff
- 00492538 ["COPY", "register:0:8", ["register:4048:8"]]
- 00492538 ["INT_ADD", "register:40f0:8", ["const:492538:8", "const:4:8"]]
- 00492538 ["CALLIND", null, ["register:0:8"]]
+ 004b53d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b53d0 ["INT_ADD", "register:40f0:8", ["const:4b53d0:8", "const:4:8"]]
+ 004b53d0 ["CALLIND", null, ["register:0:8"]]
- 00492538 bytes 20013fd6
+ 004b53d0 bytes 20013fd6
- 00492564 ["COPY", "register:0:8", ["register:4048:8"]]
- 00492564 ["INT_ADD", "register:40f0:8", ["const:492564:8", "const:4:8"]]
- 00492564 ["CALLIND", null, ["register:0:8"]]
+ 004b53fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b53fc ["INT_ADD", "register:40f0:8", ["const:4b53fc:8", "const:4:8"]]
+ 004b53fc ["CALLIND", null, ["register:0:8"]]
- 00492564 bytes 20013fd6
+ 004b53fc bytes 20013fd6
- 004924bc ["INT_ADD", "register:40f0:8", ["const:4924bc:8", "const:4:8"]]
- 004924bc ["CALL", null, ["callee:00540264:8"]]
+ 004b5354 ["INT_ADD", "register:40f0:8", ["const:4b5354:8", "const:4:8"]]
+ 004b5354 ["CALL", null, ["callee:00540264:8"]]
- 004924bc bytes c42b0294
+ 004b5354 bytes c42b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77c937d4c223338e843c7f8c870c3dd0"></a>

### [`004925e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/004925e8.md) → [`004b5480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5480.md) _ZN5BotanplERKNS_11OctetStringES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

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
    "old": {
      "definition_site": "004926a8",
      "incomplete_value": true,
      "site": "004926a8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0049273c",
      "incomplete_value": true,
      "site": "0049273c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "00492780",
      "incomplete_value": true,
      "site": "00492780",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b5530",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b55c4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b5608",
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
      "004b5530",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b55c4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b5608",
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

- 旧版 [`004926a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/004925e8.md#insn-004926a8) · [`0049273c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/004925e8.md#insn-0049273c) · [`00492780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/004925e8.md#insn-00492780)
- 新版 [`004b5540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5480.md#insn-004b5540) · [`004b55d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5480.md#insn-004b55d4) · [`004b5618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5480.md#insn-004b5618)

~~~diff
- 004926a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004926a8 ["INT_ADD", "register:40f0:8", ["const:4926a8:8", "const:4:8"]]
- 004926a8 ["CALLIND", null, ["register:0:8"]]
+ 004b5540 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b5540 ["INT_ADD", "register:40f0:8", ["const:4b5540:8", "const:4:8"]]
+ 004b5540 ["CALLIND", null, ["register:0:8"]]
- 004926a8 bytes 20013fd6
+ 004b5540 bytes 20013fd6
- 0049273c ["COPY", "register:0:8", ["register:4048:8"]]
- 0049273c ["INT_ADD", "register:40f0:8", ["const:49273c:8", "const:4:8"]]
- 0049273c ["CALLIND", null, ["register:0:8"]]
+ 004b55d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b55d4 ["INT_ADD", "register:40f0:8", ["const:4b55d4:8", "const:4:8"]]
+ 004b55d4 ["CALLIND", null, ["register:0:8"]]
- 0049273c bytes 20013fd6
+ 004b55d4 bytes 20013fd6
- 00492780 ["COPY", "register:0:8", ["register:4048:8"]]
- 00492780 ["INT_ADD", "register:40f0:8", ["const:492780:8", "const:4:8"]]
- 00492780 ["CALLIND", null, ["register:0:8"]]
+ 004b5618 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b5618 ["INT_ADD", "register:40f0:8", ["const:4b5618:8", "const:4:8"]]
+ 004b5618 ["CALLIND", null, ["register:0:8"]]
- 00492780 bytes 20013fd6
+ 004b5618 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c23f1f05e03087069efc721f35e320bd"></a>

### [`00492b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492b90.md) → [`004b5a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5a28.md) _ZN5Botan13base64_encodeEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd80.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 1件 [`00c587d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587d0.md) · 呼出先 6件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

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
    "old": {
      "definition_site": "00492d3c",
      "incomplete_value": false,
      "site": "00492d48",
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
            "const:988:8"
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
    "old": {
      "definition_site": "00492d44",
      "incomplete_value": false,
      "site": "00492d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:3d2:8"
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
      "004b5b98",
      "PARAM",
      [
        "storage",
        "002a75c2",
        null,
        "string"
      ]
    ],
    [
      "004b5ba4",
      "PARAM",
      [
        "storage",
        "00299bcc",
        null,
        "string"
      ]
    ],
    [
      "004b5bb0",
      "PARAM",
      [
        "storage",
        "002aa58d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b5b98",
      "PARAM",
      [
        "storage",
        "002b8131",
        null,
        "string"
      ]
    ],
    [
      "004b5ba4",
      "PARAM",
      [
        "storage",
        "002a9aa5",
        null,
        "string"
      ]
    ],
    [
      "004b5bb0",
      "PARAM",
      [
        "storage",
        "002bb309",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00492d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492b90.md#insn-00492d48) · [`00492c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492b90.md#insn-00492c40) · [`00492c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492b90.md#insn-00492c60)
- 新版 [`004b5be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5a28.md#insn-004b5be0) · [`004b5ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5a28.md#insn-004b5ad8) · [`004b5af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5a28.md#insn-004b5af8)

~~~diff
- 00492d48 ["INT_ADD", "register:40f0:8", ["const:492d48:8", "const:4:8"]]
- 00492d48 ["CALL", null, ["callee:00c58250:8"]]
+ 004b5be0 ["INT_ADD", "register:40f0:8", ["const:4b5be0:8", "const:4:8"]]
+ 004b5be0 ["CALL", null, ["callee:00c58250:8"]]
- 00492d48 bytes ae221d94
+ 004b5be0 bytes 9c891e94
- 00492c40 ["INT_ADD", "register:40f0:8", ["const:492c40:8", "const:4:8"]]
- 00492c40 ["CALL", null, ["callee:00c57a90:8"]]
+ 004b5ad8 ["INT_ADD", "register:40f0:8", ["const:4b5ad8:8", "const:4:8"]]
+ 004b5ad8 ["CALL", null, ["callee:00c57a90:8"]]
- 00492c40 bytes 00211d94
+ 004b5ad8 bytes ee871e94
- 00492c60 ["INT_ADD", "register:40f0:8", ["const:492c60:8", "const:4:8"]]
- 00492c60 ["CALL", null, ["callee:00c57c90:8"]]
+ 004b5af8 ["INT_ADD", "register:40f0:8", ["const:4b5af8:8", "const:4:8"]]
+ 004b5af8 ["CALL", null, ["callee:00c57c90:8"]]
- 00492c60 bytes 78211d94
+ 004b5af8 bytes 66881e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd4e0a4afd788718bbf33608249a531b"></a>

### [`00492db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492db0.md) → [`004b5c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5c48.md) _ZN5Botan13base64_decodeEPhPKcmRmbb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd90.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c587e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587e0.md) · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "00492f8c",
      "incomplete_value": false,
      "site": "00492fa0",
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
            "const:457:8"
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
    "old": {
      "definition_site": "00492fb8",
      "incomplete_value": false,
      "site": "00492fc0",
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
            "const:333:8"
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
    "old": {
      "definition_site": "00492fd8",
      "incomplete_value": false,
      "site": "00492fe0",
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
            "const:986:8"
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
      "004b5d40",
      "DATA",
      [
        "storage",
        "002b95cc",
        null,
        null
      ]
    ],
    [
      "004b5dc0",
      "DATA",
      [
        "storage",
        "002b95cc",
        null,
        null
      ]
    ],
    [
      "004b5e24",
      "PARAM",
      [
        "storage",
        "0029e457",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b5d40",
      "DATA",
      [
        "storage",
        "002cacdc",
        null,
        null
      ]
    ],
    [
      "004b5dc0",
      "DATA",
      [
        "storage",
        "002cacdc",
        null,
        null
      ]
    ],
    [
      "004b5e24",
      "PARAM",
      [
        "storage",
        "002ae7dc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00492fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492db0.md#insn-00492fa0) · [`00492fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492db0.md#insn-00492fc0) · [`00492fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492db0.md#insn-00492fe0)
- 新版 [`004b5e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5c48.md#insn-004b5e38) · [`004b5e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5c48.md#insn-004b5e58) · [`004b5e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5c48.md#insn-004b5e78)

~~~diff
- 00492fa0 ["INT_ADD", "register:40f0:8", ["const:492fa0:8", "const:4:8"]]
- 00492fa0 ["CALL", null, ["callee:00441e54:8"]]
+ 004b5e38 ["INT_ADD", "register:40f0:8", ["const:4b5e38:8", "const:4:8"]]
+ 004b5e38 ["CALL", null, ["callee:00441e54:8"]]
- 00492fa0 bytes ed30fe97
+ 004b5e38 bytes 0730fe97
- 00492fc0 ["INT_ADD", "register:40f0:8", ["const:492fc0:8", "const:4:8"]]
- 00492fc0 ["CALL", null, ["callee:00441e54:8"]]
+ 004b5e58 ["INT_ADD", "register:40f0:8", ["const:4b5e58:8", "const:4:8"]]
+ 004b5e58 ["CALL", null, ["callee:00441e54:8"]]
- 00492fc0 bytes e530fe97
+ 004b5e58 bytes ff2ffe97
- 00492fe0 ["INT_ADD", "register:40f0:8", ["const:492fe0:8", "const:4:8"]]
- 00492fe0 ["CALL", null, ["callee:00441e54:8"]]
+ 004b5e78 ["INT_ADD", "register:40f0:8", ["const:4b5e78:8", "const:4:8"]]
+ 004b5e78 ["CALL", null, ["callee:00441e54:8"]]
- 00492fe0 bytes dd30fe97
+ 004b5e78 bytes f72ffe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2961ef14052dcbe5d57146342ef884b4"></a>

### [`00493150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493150.md) → [`004b5fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5fe8.md) _ZN5Botan13base64_decodeEPhPKcmb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbda0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c587f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587f0.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
    "old": {
      "definition_site": "004931cc",
      "incomplete_value": false,
      "site": "004931d4",
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
            "const:d68:8"
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
    "old": {
      "definition_site": "00493208",
      "incomplete_value": true,
      "site": "00493214",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b609c",
      "incomplete_value": false,
      "site": "004b60ac",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00493204",
      "incomplete_value": false,
      "site": "00493214",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004b6064",
      "PARAM",
      [
        "storage",
        "00298d68",
        null,
        "string"
      ]
    ],
    [
      "004b609c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004b60a0",
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
      "004b6064",
      "PARAM",
      [
        "storage",
        "002a8b26",
        null,
        "string"
      ]
    ],
    [
      "004b609c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b60a0",
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

- 旧版 [`004931d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493150.md#insn-004931d4) · [`00493214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493150.md#insn-00493214) · [`00493184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493150.md#insn-00493184)
- 新版 [`004b606c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5fe8.md#insn-004b606c) · [`004b60ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5fe8.md#insn-004b60ac) · [`004b601c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5fe8.md#insn-004b601c)

~~~diff
- 004931d4 ["INT_ADD", "register:40f0:8", ["const:4931d4:8", "const:4:8"]]
- 004931d4 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b606c ["INT_ADD", "register:40f0:8", ["const:4b606c:8", "const:4:8"]]
+ 004b606c ["CALL", null, ["callee:0043dd98:8"]]
- 004931d4 bytes 3120fe97
+ 004b606c bytes 4b1ffe97
- 00493214 ["INT_ADD", "register:40f0:8", ["const:493214:8", "const:4:8"]]
- 00493214 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b60ac ["INT_ADD", "register:40f0:8", ["const:4b60ac:8", "const:4:8"]]
+ 004b60ac ["CALL", null, ["callee:00c57b10:8"]]
- 00493214 bytes ab1f1d94
+ 004b60ac bytes 99861e94
- 00493184 ["INT_ADD", "register:40f0:8", ["const:493184:8", "const:4:8"]]
- 00493184 ["CALL", null, ["callee:00c587e0:8"]]
+ 004b601c ["INT_ADD", "register:40f0:8", ["const:4b601c:8", "const:4:8"]]
+ 004b601c ["CALL", null, ["callee:00c587e0:8"]]
- 00493184 bytes 03231d94
+ 004b601c bytes f1891e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47932c3fa0d698397a36c9bd29b8da42"></a>

### [`004934f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/004934f4.md) → [`004b638c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b638c.md) _ZNK5Botan6BigInt12encoded_sizeENS0_4BaseE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbaf0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58540.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
    "old": {
      "definition_site": "0049371c",
      "incomplete_value": false,
      "site": "00493724",
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
            "const:535:8"
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
    "old": {
      "definition_site": "00493758",
      "incomplete_value": true,
      "site": "00493764",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b65ec",
      "incomplete_value": false,
      "site": "004b65fc",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00493754",
      "incomplete_value": false,
      "site": "00493764",
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
      "004b652c",
      "READ",
      [
        "storage",
        "002b2b40",
        null,
        "undefined8"
      ]
    ],
    [
      "004b65b4",
      "PARAM",
      [
        "storage",
        "002a5535",
        null,
        "string"
      ]
    ],
    [
      "004b65ec",
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
      "004b652c",
      "READ",
      [
        "storage",
        "002c4248",
        null,
        "undefined8"
      ]
    ],
    [
      "004b65b4",
      "PARAM",
      [
        "storage",
        "002b5f63",
        null,
        "string"
      ]
    ],
    [
      "004b65ec",
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

- 旧版 [`00493724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/004934f4.md#insn-00493724) · [`00493764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/004934f4.md#insn-00493764) · [`0049368c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/004934f4.md#insn-0049368c)
- 新版 [`004b65bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b638c.md#insn-004b65bc) · [`004b65fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b638c.md#insn-004b65fc) · [`004b6524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b638c.md#insn-004b6524)

~~~diff
- 00493724 ["INT_ADD", "register:40f0:8", ["const:493724:8", "const:4:8"]]
- 00493724 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b65bc ["INT_ADD", "register:40f0:8", ["const:4b65bc:8", "const:4:8"]]
+ 004b65bc ["CALL", null, ["callee:0043dd98:8"]]
- 00493724 bytes dd1efe97
+ 004b65bc bytes f71dfe97
- 00493764 ["INT_ADD", "register:40f0:8", ["const:493764:8", "const:4:8"]]
- 00493764 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b65fc ["INT_ADD", "register:40f0:8", ["const:4b65fc:8", "const:4:8"]]
+ 004b65fc ["CALL", null, ["callee:00c57b10:8"]]
- 00493764 bytes 571e1d94
+ 004b65fc bytes 45851e94
- 0049368c ["COPY", "register:4048:8", ["const:2b2000:8"]]
+ 004b6524 ["COPY", "register:4048:8", ["const:2c4000:8"]]
- 0049368c bytes e9f0fff0
+ 004b6524 bytes 69f0ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-602c69b083ce7a10cea8fe82a6d45580"></a>

### [`00493850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493850.md) → [`004b66e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md) _ZN5Botan6divideERKNS_6BigIntES2_RS0_S3_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd00.md) · 呼出先 21件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004989ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004989ec.md) [`00498c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 1件 [`00c58750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58750.md) · 呼出先 21件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004bb884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb884.md) [`004bbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.13% / 新版 98.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 7件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "0049391c",
      "incomplete_value": true,
      "site": "00493920",
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
    "old": {
      "definition_site": "00493940",
      "incomplete_value": true,
      "site": "00493944",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:18:8"
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
      "definition_site": "004b67d4",
      "incomplete_value": false,
      "site": "004b67dc",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0049393c",
      "incomplete_value": false,
      "site": "00493944",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004b67a0",
      "READ",
      [
        "storage",
        "00c1b010",
        null,
        "pointer"
      ]
    ],
    [
      "004b67b8",
      "DATA",
      [
        "storage",
        "00becca0",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b67d4",
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
      "004b67a0",
      "READ",
      [
        "storage",
        "00c9aa00",
        null,
        "pointer"
      ]
    ],
    [
      "004b67b8",
      "DATA",
      [
        "storage",
        "00c69860",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b67d4",
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

- 旧版 [`00493944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493850.md#insn-00493944) · [`00493950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493850.md#insn-00493950) · [`00493a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493850.md#insn-00493a0c)
- 新版 [`004b67dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md#insn-004b67dc) · [`004b67e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md#insn-004b67e8) · [`004b68a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md#insn-004b68a4)

~~~diff
- 00493944 ["INT_ADD", "register:40f0:8", ["const:493944:8", "const:4:8"]]
- 00493944 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b67dc ["INT_ADD", "register:40f0:8", ["const:4b67dc:8", "const:4:8"]]
+ 004b67dc ["CALL", null, ["callee:00c57b10:8"]]
- 00493944 bytes df1d1d94
+ 004b67dc bytes cd841e94
- 00493950 ["INT_ADD", "register:40f0:8", ["const:493950:8", "const:4:8"]]
- 00493950 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004b67e8 ["INT_ADD", "register:40f0:8", ["const:4b67e8:8", "const:4:8"]]
+ 004b67e8 ["CALL", null, ["ram:c58740:8"]]
- 00493950 bytes e8201d94
+ 004b67e8 bytes d6871e94
- 00493a0c ["COPY", "register:0:8", ["register:4048:8"]]
- 00493a0c ["INT_ADD", "register:40f0:8", ["const:493a0c:8", "const:4:8"]]
- 00493a0c ["CALLIND", null, ["register:0:8"]]
+ 004b68a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b68a4 ["INT_ADD", "register:40f0:8", ["const:4b68a4:8", "const:4:8"]]
+ 004b68a4 ["CALLIND", null, ["register:0:8"]]
- 00493a0c bytes 20013fd6
+ 004b68a4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a67cdf0fe982a2d6c88b17c935e07512"></a>

### [`00494440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494440.md) → [`004b72d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b72d8.md) _ZN5Botan7Charset10digit2charEh

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd10.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58760.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
    "old": {
      "definition_site": "004944a8",
      "incomplete_value": false,
      "site": "004944b0",
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
            "const:7ef:8"
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
    "old": {
      "definition_site": "004944e4",
      "incomplete_value": true,
      "site": "004944f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b7378",
      "incomplete_value": false,
      "site": "004b7388",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004944e0",
      "incomplete_value": false,
      "site": "004944f0",
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
      "004b7340",
      "PARAM",
      [
        "storage",
        "002947ef",
        null,
        "string"
      ]
    ],
    [
      "004b7378",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004b737c",
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
      "004b7340",
      "PARAM",
      [
        "storage",
        "002a4105",
        null,
        "string"
      ]
    ],
    [
      "004b7378",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b737c",
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

- 旧版 [`004944b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494440.md#insn-004944b0) · [`004944f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494440.md#insn-004944f0) · [`0049449c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494440.md#insn-0049449c)
- 新版 [`004b7348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b72d8.md#insn-004b7348) · [`004b7388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b72d8.md#insn-004b7388) · [`004b7334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b72d8.md#insn-004b7334)

~~~diff
- 004944b0 ["INT_ADD", "register:40f0:8", ["const:4944b0:8", "const:4:8"]]
- 004944b0 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b7348 ["INT_ADD", "register:40f0:8", ["const:4b7348:8", "const:4:8"]]
+ 004b7348 ["CALL", null, ["callee:0043dd98:8"]]
- 004944b0 bytes 7a1bfe97
+ 004b7348 bytes 941afe97
- 004944f0 ["INT_ADD", "register:40f0:8", ["const:4944f0:8", "const:4:8"]]
- 004944f0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b7388 ["INT_ADD", "register:40f0:8", ["const:4b7388:8", "const:4:8"]]
+ 004b7388 ["CALL", null, ["callee:00c57b10:8"]]
- 004944f0 bytes f41a1d94
+ 004b7388 bytes e2811e94
- 0049449c ["INT_ADD", "register:40f0:8", ["const:49449c:8", "const:4:8"]]
- 0049449c ["CALL", null, ["callee:00c57af0:8"]]
+ 004b7334 ["INT_ADD", "register:40f0:8", ["const:4b7334:8", "const:4:8"]]
+ 004b7334 ["CALL", null, ["callee:00c57af0:8"]]
- 0049449c bytes 011b1d94
+ 004b7334 bytes ef811e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d94efcf677c769159b78fd7010cde58b"></a>

### [`00494634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494634.md) → [`004b74cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b74cc.md) _ZN5Botan6BigInt11encode_1363EPhmRKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbe10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe10.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58860.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
    "old": {
      "definition_site": "00494730",
      "incomplete_value": false,
      "site": "00494738",
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
            "const:506:8"
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
    "old": {
      "definition_site": "0049476c",
      "incomplete_value": true,
      "site": "00494778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b7600",
      "incomplete_value": false,
      "site": "004b7610",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00494768",
      "incomplete_value": false,
      "site": "00494778",
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
      "004b75c8",
      "PARAM",
      [
        "storage",
        "002a5506",
        null,
        "string"
      ]
    ],
    [
      "004b7600",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004b7604",
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
      "004b75c8",
      "PARAM",
      [
        "storage",
        "002b5f34",
        null,
        "string"
      ]
    ],
    [
      "004b7600",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b7604",
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

- 旧版 [`00494738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494634.md#insn-00494738) · [`00494778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494634.md#insn-00494778) · [`00494724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494634.md#insn-00494724)
- 新版 [`004b75d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b74cc.md#insn-004b75d0) · [`004b7610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b74cc.md#insn-004b7610) · [`004b75bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b74cc.md#insn-004b75bc)

~~~diff
- 00494738 ["INT_ADD", "register:40f0:8", ["const:494738:8", "const:4:8"]]
- 00494738 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b75d0 ["INT_ADD", "register:40f0:8", ["const:4b75d0:8", "const:4:8"]]
+ 004b75d0 ["CALL", null, ["callee:0043dd98:8"]]
- 00494738 bytes d81afe97
+ 004b75d0 bytes f219fe97
- 00494778 ["INT_ADD", "register:40f0:8", ["const:494778:8", "const:4:8"]]
- 00494778 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b7610 ["INT_ADD", "register:40f0:8", ["const:4b7610:8", "const:4:8"]]
+ 004b7610 ["CALL", null, ["callee:00c57b10:8"]]
- 00494778 bytes 521a1d94
+ 004b7610 bytes 40811e94
- 00494724 ["INT_ADD", "register:40f0:8", ["const:494724:8", "const:4:8"]]
- 00494724 ["CALL", null, ["callee:00c57af0:8"]]
+ 004b75bc ["INT_ADD", "register:40f0:8", ["const:4b75bc:8", "const:4:8"]]
+ 004b75bc ["CALL", null, ["callee:00c57af0:8"]]
- 00494724 bytes 5f1a1d94
+ 004b75bc bytes 4d811e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d44d7d1f154371daf592804c7045824"></a>

### [`00494c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494c34.md) → [`004b7acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7acc.md) _ZN5Botan7Charset10char2digitEc

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc60.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c586b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586b0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
      "definition_site": "004b7b34",
      "incomplete_value": false,
      "site": "004b7b3c",
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
            "const:3c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494c9c",
      "incomplete_value": false,
      "site": "00494ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:64b:8"
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
      "definition_site": "004b7b70",
      "incomplete_value": true,
      "site": "004b7b7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00494cd8",
      "incomplete_value": true,
      "site": "00494ce4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b7b6c",
      "incomplete_value": false,
      "site": "004b7b7c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00494cd4",
      "incomplete_value": false,
      "site": "00494ce4",
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
      "004b7b34",
      "PARAM",
      [
        "storage",
        "002aa64b",
        null,
        "string"
      ]
    ],
    [
      "004b7b6c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004b7b70",
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
      "004b7b34",
      "PARAM",
      [
        "storage",
        "002bb3c7",
        null,
        "string"
      ]
    ],
    [
      "004b7b6c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b7b70",
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

- 旧版 [`00494ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494c34.md#insn-00494ca4) · [`00494ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494c34.md#insn-00494ce4) · [`00494c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494c34.md#insn-00494c90)
- 新版 [`004b7b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7acc.md#insn-004b7b3c) · [`004b7b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7acc.md#insn-004b7b7c) · [`004b7b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7acc.md#insn-004b7b28)

~~~diff
- 00494ca4 ["INT_ADD", "register:40f0:8", ["const:494ca4:8", "const:4:8"]]
- 00494ca4 ["CALL", null, ["callee:0043dd98:8"]]
+ 004b7b3c ["INT_ADD", "register:40f0:8", ["const:4b7b3c:8", "const:4:8"]]
+ 004b7b3c ["CALL", null, ["callee:0043dd98:8"]]
- 00494ca4 bytes 7d19fe97
+ 004b7b3c bytes 9718fe97
- 00494ce4 ["INT_ADD", "register:40f0:8", ["const:494ce4:8", "const:4:8"]]
- 00494ce4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b7b7c ["INT_ADD", "register:40f0:8", ["const:4b7b7c:8", "const:4:8"]]
+ 004b7b7c ["CALL", null, ["callee:00c57b10:8"]]
- 00494ce4 bytes f7181d94
+ 004b7b7c bytes e57f1e94
- 00494c90 ["INT_ADD", "register:40f0:8", ["const:494c90:8", "const:4:8"]]
- 00494c90 ["CALL", null, ["callee:00c57af0:8"]]
+ 004b7b28 ["INT_ADD", "register:40f0:8", ["const:4b7b28:8", "const:4:8"]]
+ 004b7b28 ["CALL", null, ["callee:00c57af0:8"]]
- 00494c90 bytes 04191d94
+ 004b7b28 bytes f27f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-128e9a72ac409a177ea0066d3c1f4451"></a>

### [`00494d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494d38.md) → [`004b7bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md) _ZN5Botan6BigIntmLERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc70.md) · 呼出先 10件 [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`00496208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496208.md) [`00496308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496308.md) [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 1件 [`00c586c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586c0.md) · 呼出先 10件 [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004b90a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b90a0.md) [`004b91a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b91a0.md) [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.76% / 新版 97.76%

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
      "site": "004b7e4c",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00494fb4",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b7ee8",
      "incomplete_value": true,
      "site": "004b7ee8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00495050",
      "incomplete_value": true,
      "site": "00495050",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b7f14",
      "incomplete_value": true,
      "site": "004b7f14",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0049507c",
      "incomplete_value": true,
      "site": "0049507c",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b7e4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004b7ed8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b7f04",
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
      "004b7e4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004b7ed8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b7f04",
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

- 旧版 [`00494fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494d38.md#insn-00494fb4) · [`00495050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494d38.md#insn-00495050) · [`0049507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494d38.md#insn-0049507c)
- 新版 [`004b7e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md#insn-004b7e4c) · [`004b7ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md#insn-004b7ee8) · [`004b7f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md#insn-004b7f14)

~~~diff
- 00494fb4 ["INT_ADD", "register:40f0:8", ["const:494fb4:8", "const:4:8"]]
- 00494fb4 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004b7e4c ["INT_ADD", "register:40f0:8", ["const:4b7e4c:8", "const:4:8"]]
+ 004b7e4c ["CALL", null, ["ram:c58740:8"]]
- 00494fb4 bytes 4f1b1d94
+ 004b7e4c bytes 3d821e94
- 00495050 ["COPY", "register:0:8", ["register:4048:8"]]
- 00495050 ["INT_ADD", "register:40f0:8", ["const:495050:8", "const:4:8"]]
- 00495050 ["CALLIND", null, ["register:0:8"]]
+ 004b7ee8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b7ee8 ["INT_ADD", "register:40f0:8", ["const:4b7ee8:8", "const:4:8"]]
+ 004b7ee8 ["CALLIND", null, ["register:0:8"]]
- 00495050 bytes 20013fd6
+ 004b7ee8 bytes 20013fd6
- 0049507c ["COPY", "register:0:8", ["register:4048:8"]]
- 0049507c ["INT_ADD", "register:40f0:8", ["const:49507c:8", "const:4:8"]]
- 0049507c ["CALLIND", null, ["register:0:8"]]
+ 004b7f14 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b7f14 ["INT_ADD", "register:40f0:8", ["const:4b7f14:8", "const:4:8"]]
+ 004b7f14 ["CALLIND", null, ["register:0:8"]]
- 0049507c bytes 20013fd6
+ 004b7f14 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2662e576cbf92ac29042c0edcef85db2"></a>

### [`004950f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) → [`004b7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) _ZN5Botan6BigIntpLERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdbc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc80.md) · 呼出先 10件 [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`00495a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md) [`00495c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495c94.md) [`004b3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3cec.md)
- 新版 呼出元 1件 [`00c586d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586d0.md) · 呼出先 10件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004b890c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md) [`004b8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md) [`004d6b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b81a8",
      "incomplete_value": true,
      "site": "004b81a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00495310",
      "incomplete_value": true,
      "site": "00495310",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004b819c",
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
      "004b819c",
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

- 旧版 [`00495310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md#insn-00495310) · [`004951ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md#insn-004951ac) · [`004951e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md#insn-004951e8)
- 新版 [`004b81a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md#insn-004b81a8) · [`004b8044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md#insn-004b8044) · [`004b8080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md#insn-004b8080)

~~~diff
- 00495310 ["COPY", "register:0:8", ["register:4048:8"]]
- 00495310 ["INT_ADD", "register:40f0:8", ["const:495310:8", "const:4:8"]]
- 00495310 ["CALLIND", null, ["register:0:8"]]
+ 004b81a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b81a8 ["INT_ADD", "register:40f0:8", ["const:4b81a8:8", "const:4:8"]]
+ 004b81a8 ["CALLIND", null, ["register:0:8"]]
- 00495310 bytes 20013fd6
+ 004b81a8 bytes 20013fd6
- 004951ac ["INT_ADD", "register:40f0:8", ["const:4951ac:8", "const:4:8"]]
- 004951ac ["CALL", null, ["callee:005408e0:8"]]
+ 004b8044 ["INT_ADD", "register:40f0:8", ["const:4b8044:8", "const:4:8"]]
+ 004b8044 ["CALL", null, ["callee:005408e0:8"]]
- 004951ac bytes 27220294
+ 004b8044 bytes 27220294
- 004951e8 ["INT_ADD", "register:40f0:8", ["const:4951e8:8", "const:4:8"]]
- 004951e8 ["CALL", null, ["callee:004d6b84:8"]]
+ 004b8080 ["INT_ADD", "register:40f0:8", ["const:4b8080:8", "const:4:8"]]
+ 004b8080 ["CALL", null, ["callee:004d6b84:8"]]
- 004951e8 bytes c17a0094
+ 004b8080 bytes c17a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26fd7f59f7491993f324dc8b93d1d239"></a>

### [`00495378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495378.md) → [`004b8210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8210.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERKNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.67% / 新版 93.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b82a8",
      "incomplete_value": true,
      "site": "004b82a8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00495410",
      "incomplete_value": true,
      "site": "00495410",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b82f8",
      "incomplete_value": true,
      "site": "004b82f8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00495460",
      "incomplete_value": true,
      "site": "00495460",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b830c",
      "incomplete_value": false,
      "site": "004b8318",
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
            "const:f1f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495474",
      "incomplete_value": false,
      "site": "00495480",
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
            "const:27d:8"
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
      "004b8298",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b82e8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004b830c",
      "PARAM",
      [
        "storage",
        "002a827d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b8298",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b82e8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b830c",
      "PARAM",
      [
        "storage",
        "002b8f1f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495378.md#insn-00495410) · [`00495460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495378.md#insn-00495460) · [`00495480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495378.md#insn-00495480)
- 新版 [`004b82a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8210.md#insn-004b82a8) · [`004b82f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8210.md#insn-004b82f8) · [`004b8318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8210.md#insn-004b8318)

~~~diff
- 00495410 ["COPY", "register:0:8", ["register:4048:8"]]
- 00495410 ["INT_ADD", "register:40f0:8", ["const:495410:8", "const:4:8"]]
- 00495410 ["CALLIND", null, ["register:0:8"]]
+ 004b82a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b82a8 ["INT_ADD", "register:40f0:8", ["const:4b82a8:8", "const:4:8"]]
+ 004b82a8 ["CALLIND", null, ["register:0:8"]]
- 00495410 bytes 20013fd6
+ 004b82a8 bytes 20013fd6
- 00495460 ["COPY", "register:0:8", ["register:4048:8"]]
- 00495460 ["INT_ADD", "register:40f0:8", ["const:495460:8", "const:4:8"]]
- 00495460 ["CALLIND", null, ["register:0:8"]]
+ 004b82f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b82f8 ["INT_ADD", "register:40f0:8", ["const:4b82f8:8", "const:4:8"]]
+ 004b82f8 ["CALLIND", null, ["register:0:8"]]
- 00495460 bytes 20013fd6
+ 004b82f8 bytes 20013fd6
- 00495480 ["INT_ADD", "register:40f0:8", ["const:495480:8", "const:4:8"]]
- 00495480 ["CALL", null, ["callee:00c58870:8"]]
+ 004b8318 ["INT_ADD", "register:40f0:8", ["const:4b8318:8", "const:4:8"]]
+ 004b8318 ["CALL", null, ["callee:00c58870:8"]]
- 00495480 bytes 681a1d94
+ 004b8318 bytes 56811e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96583a56153d66f437259cff8b7a5233"></a>

### [`00495668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495668.md) → [`004b8500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8500.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00520650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520650.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005434e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/005434e8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.33% / 新版 96.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b8550",
      "incomplete_value": true,
      "site": "004b8554",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004956b8",
      "incomplete_value": true,
      "site": "004956bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b8570",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004956d8",
      "value": [
        "leaf",
        "ram:bdb440:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b8610",
      "incomplete_value": true,
      "site": "004b8610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00495778",
      "incomplete_value": true,
      "site": "00495778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004b8550",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004b8550",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004b8570",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "004b8550",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "004b8550",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004b8570",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004956bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495668.md#insn-004956bc) · [`004956d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495668.md#insn-004956d8) · [`00495778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495668.md#insn-00495778)
- 新版 [`004b8554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8500.md#insn-004b8554) · [`004b8570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8500.md#insn-004b8570) · [`004b8610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8500.md#insn-004b8610)

~~~diff
- 004956bc ["INT_ADD", "register:40f0:8", ["const:4956bc:8", "const:4:8"]]
- 004956bc ["CALL", null, ["callee:00c57e80:8"]]
+ 004b8554 ["INT_ADD", "register:40f0:8", ["const:4b8554:8", "const:4:8"]]
+ 004b8554 ["CALL", null, ["callee:00c57e80:8"]]
- 004956bc bytes 5d171d94
+ 004b8554 bytes 4b7e1e94
- 004956d8 ["INT_ADD", "register:40f0:8", ["const:4956d8:8", "const:4:8"]]
- 004956d8 ["CALL", null, ["ram:bdb440:8"]]
+ 004b8570 ["INT_ADD", "register:40f0:8", ["const:4b8570:8", "const:4:8"]]
+ 004b8570 ["CALL", null, ["ram:c57e90:8"]]
- 004956d8 bytes 5a171d94
+ 004b8570 bytes 487e1e94
- 00495778 ["COPY", "register:0:8", ["register:4048:8"]]
- 00495778 ["INT_ADD", "register:40f0:8", ["const:495778:8", "const:4:8"]]
- 00495778 ["CALLIND", null, ["register:0:8"]]
+ 004b8610 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b8610 ["INT_ADD", "register:40f0:8", ["const:4b8610:8", "const:4:8"]]
+ 004b8610 ["CALLIND", null, ["register:0:8"]]
- 00495778 bytes 20013fd6
+ 004b8610 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f0185f0fe4badd2f3348dba32f7bd5"></a>

### [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) → [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) FUN_004b8810

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`0047e47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047e47c.md) [`00494d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494d38.md) [`004950f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) [`0049731c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/0049731c.md) [`004b868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b868c.md) · 呼出先 7件 [`0051345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051345c.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 8件 [`004a1314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1314.md) [`004b7bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md) [`004b7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) [`004ba1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba1b4.md) [`004db524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db524.md) · 呼出先 7件 [`005362f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b88c8",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00495a30",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b88d8",
      "incomplete_value": true,
      "site": "004b88e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00495a40",
      "incomplete_value": true,
      "site": "00495a48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
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
      "definition_site": "004b88dc",
      "incomplete_value": true,
      "site": "004b88e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00495a44",
      "incomplete_value": true,
      "site": "00495a48",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:c1b000:8"
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
      "004b88c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "004b88d8",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004b88d8",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004b88c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "004b88d8",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004b88d8",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md#insn-00495a30) · [`00495a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md#insn-00495a48) · [`004959c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md#insn-004959c4)
- 新版 [`004b88c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md#insn-004b88c8) · [`004b88e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md#insn-004b88e0) · [`004b885c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md#insn-004b885c)

~~~diff
- 00495a30 ["INT_ADD", "register:40f0:8", ["const:495a30:8", "const:4:8"]]
- 00495a30 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004b88c8 ["INT_ADD", "register:40f0:8", ["const:4b88c8:8", "const:4:8"]]
+ 004b88c8 ["CALL", null, ["ram:c58640:8"]]
- 00495a30 bytes 70181d94
+ 004b88c8 bytes 5e7f1e94
- 00495a48 ["INT_ADD", "register:40f0:8", ["const:495a48:8", "const:4:8"]]
- 00495a48 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b88e0 ["INT_ADD", "register:40f0:8", ["const:4b88e0:8", "const:4:8"]]
+ 004b88e0 ["CALL", null, ["callee:00c57b10:8"]]
- 00495a48 bytes 9e151d94
+ 004b88e0 bytes 8c7c1e94
- 004959c4 ["INT_ADD", "register:40f0:8", ["const:4959c4:8", "const:4:8"]]
- 004959c4 ["CALL", null, ["callee:00c58630:8"]]
+ 004b885c ["INT_ADD", "register:40f0:8", ["const:4b885c:8", "const:4:8"]]
+ 004b885c ["CALL", null, ["callee:00c58630:8"]]
- 004959c4 bytes 87181d94
+ 004b885c bytes 757f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e15eb43ee59165e553f0f57abfb6c30b"></a>

### [`00495a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md) → [`004b890c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md) FUN_004b890c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`004950f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) [`00496ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496ee0.md) [`00497068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497068.md) [`004b44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) [`004b4a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md) · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 5件 [`004b7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) [`004b9d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9d78.md) [`004b9f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9f00.md) [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.52% / 新版 96.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b8ab4",
      "incomplete_value": false,
      "site": "004b8ad4",
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
            "const:504:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495c1c",
      "incomplete_value": false,
      "site": "00495c3c",
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
            "const:9cf:8"
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
      "definition_site": "004b8abc",
      "incomplete_value": false,
      "site": "004b8ad4",
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
            "const:6d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495c24",
      "incomplete_value": false,
      "site": "00495c3c",
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
            "const:63f:8"
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
      "definition_site": "004b8ac4",
      "incomplete_value": false,
      "site": "004b8ad4",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495c2c",
      "incomplete_value": false,
      "site": "00495c3c",
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
            "const:4eb:8"
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
      "004b8ab4",
      "PARAM",
      [
        "storage",
        "002969cf",
        null,
        "string"
      ]
    ],
    [
      "004b8abc",
      "PARAM",
      [
        "storage",
        "002a563f",
        null,
        "string"
      ]
    ],
    [
      "004b8ac4",
      "PARAM",
      [
        "storage",
        "002a44eb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b8ab4",
      "PARAM",
      [
        "storage",
        "002a6504",
        null,
        "string"
      ]
    ],
    [
      "004b8abc",
      "PARAM",
      [
        "storage",
        "002b606d",
        null,
        "string"
      ]
    ],
    [
      "004b8ac4",
      "PARAM",
      [
        "storage",
        "002b4d58",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md#insn-00495c3c) · [`00495c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md#insn-00495c18) · [`00495c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md#insn-00495c1c)
- 新版 [`004b8ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md#insn-004b8ad4) · [`004b8ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md#insn-004b8ab0) · [`004b8ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md#insn-004b8ab4)

~~~diff
- 00495c3c ["INT_ADD", "register:40f0:8", ["const:495c3c:8", "const:4:8"]]
- 00495c3c ["CALL", null, ["callee:00c58250:8"]]
+ 004b8ad4 ["INT_ADD", "register:40f0:8", ["const:4b8ad4:8", "const:4:8"]]
+ 004b8ad4 ["CALL", null, ["callee:00c58250:8"]]
- 00495c3c bytes f1161d94
+ 004b8ad4 bytes df7d1e94
- 00495c18 ["COPY", "register:4000:8", ["const:296000:8"]]
+ 004b8ab0 ["COPY", "register:4000:8", ["const:2a6000:8"]]
- 00495c18 bytes 00f0ffb0
+ 004b8ab0 bytes 60efffd0
- 00495c1c ["COPY", "tmp:0:8", ["const:9cf:8"]]
- 00495c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00495c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00495c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004b8ab4 ["COPY", "tmp:0:8", ["const:504:8"]]
+ 004b8ab4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8ab4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8ab4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00495c1c bytes 003c2791
+ 004b8ab4 bytes 00101491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fd74585b12add917c88fa4049f083e1"></a>

### [`00495c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495c94.md) → [`004b8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md) FUN_004b8b2c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004950f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) [`00495e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495e3c.md) [`004b44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) [`004b4a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md) · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 4件 [`004b7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) [`004b8cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md) [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b8cb0",
      "incomplete_value": false,
      "site": "004b8cd0",
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
            "const:504:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495e18",
      "incomplete_value": false,
      "site": "00495e38",
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
            "const:9cf:8"
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
      "definition_site": "004b8cb8",
      "incomplete_value": false,
      "site": "004b8cd0",
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
            "const:6d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495e20",
      "incomplete_value": false,
      "site": "00495e38",
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
            "const:63f:8"
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
      "definition_site": "004b8cc0",
      "incomplete_value": false,
      "site": "004b8cd0",
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
            "const:951:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495e28",
      "incomplete_value": false,
      "site": "00495e38",
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
            "const:53e:8"
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
      "004b8cb0",
      "PARAM",
      [
        "storage",
        "002969cf",
        null,
        "string"
      ]
    ],
    [
      "004b8cb8",
      "PARAM",
      [
        "storage",
        "002a563f",
        null,
        "string"
      ]
    ],
    [
      "004b8cc0",
      "PARAM",
      [
        "storage",
        "0029f53e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b8cb0",
      "PARAM",
      [
        "storage",
        "002a6504",
        null,
        "string"
      ]
    ],
    [
      "004b8cb8",
      "PARAM",
      [
        "storage",
        "002b606d",
        null,
        "string"
      ]
    ],
    [
      "004b8cc0",
      "PARAM",
      [
        "storage",
        "002af951",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495c94.md#insn-00495e38) · [`00495e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495c94.md#insn-00495e14) · [`00495e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495c94.md#insn-00495e18)
- 新版 [`004b8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md#insn-004b8cd0) · [`004b8cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md#insn-004b8cac) · [`004b8cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md#insn-004b8cb0)

~~~diff
- 00495e38 ["INT_ADD", "register:40f0:8", ["const:495e38:8", "const:4:8"]]
- 00495e38 ["CALL", null, ["callee:00c58250:8"]]
+ 004b8cd0 ["INT_ADD", "register:40f0:8", ["const:4b8cd0:8", "const:4:8"]]
+ 004b8cd0 ["CALL", null, ["callee:00c58250:8"]]
- 00495e38 bytes 72161d94
+ 004b8cd0 bytes 607d1e94
- 00495e14 ["COPY", "register:4000:8", ["const:296000:8"]]
+ 004b8cac ["COPY", "register:4000:8", ["const:2a6000:8"]]
- 00495e14 bytes 00f0ffb0
+ 004b8cac bytes 60efffd0
- 00495e18 ["COPY", "tmp:0:8", ["const:9cf:8"]]
- 00495e18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00495e18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00495e18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004b8cb0 ["COPY", "tmp:0:8", ["const:504:8"]]
+ 004b8cb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8cb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8cb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00495e18 bytes 003c2791
+ 004b8cb0 bytes 00101491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-147ea9e42af684f0476d55ae168987e6"></a>

### [`00495e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495e3c.md) → [`004b8cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md) _ZN5Botan6BigIntmIERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdf0.md) · 呼出先 6件 [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00495c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495c94.md) [`0049607c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/0049607c.md) [`004b3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3cec.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 1件 [`00c58840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58840.md) · 呼出先 6件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md) [`004b8f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8f14.md) [`004d6b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.31% / 新版 99.31%

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
      "site": "004b8e04",
      "value": [
        "leaf",
        "ram:4b8f14:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00495f6c",
      "value": [
        "leaf",
        "ram:49607c:8"
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
      "004b8e04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0049607c"
      ]
    ]
  ],
  "added": [
    [
      "004b8e04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004b8f14"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495e3c.md#insn-00495f6c) · [`00495ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495e3c.md#insn-00495ebc) · [`00495efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495e3c.md#insn-00495efc)
- 新版 [`004b8e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md#insn-004b8e04) · [`004b8d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md#insn-004b8d54) · [`004b8d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md#insn-004b8d94)

~~~diff
- 00495f6c ["INT_ADD", "register:40f0:8", ["const:495f6c:8", "const:4:8"]]
- 00495f6c ["CALL", null, ["ram:49607c:8"]]
+ 004b8e04 ["INT_ADD", "register:40f0:8", ["const:4b8e04:8", "const:4:8"]]
+ 004b8e04 ["CALL", null, ["ram:4b8f14:8"]]
- 00495f6c bytes 44000094
+ 004b8e04 bytes 44000094
- 00495ebc ["INT_ADD", "register:40f0:8", ["const:495ebc:8", "const:4:8"]]
- 00495ebc ["CALL", null, ["callee:004b8774:8"]]
+ 004b8d54 ["INT_ADD", "register:40f0:8", ["const:4b8d54:8", "const:4:8"]]
+ 004b8d54 ["CALL", null, ["callee:004b8774:8"]]
- 00495ebc bytes 88feff97
+ 004b8d54 bytes 88feff97
- 00495efc ["INT_ADD", "register:40f0:8", ["const:495efc:8", "const:4:8"]]
- 00495efc ["CALL", null, ["callee:005408e0:8"]]
+ 004b8d94 ["INT_ADD", "register:40f0:8", ["const:4b8d94:8", "const:4:8"]]
+ 004b8d94 ["CALL", null, ["callee:005408e0:8"]]
- 00495efc bytes d31e0294
+ 004b8d94 bytes d31e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ac2a91f0a8dc471a068c0e743469378"></a>

### [`004967a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/004967a4.md) → [`004b963c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b963c.md) _ZN5BotanrmERKNS_6BigIntES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbe50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe50.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c588a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588a0.md) · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, call_target, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 94.81% / 新版 94.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b96f0",
      "incomplete_value": true,
      "site": "004b96f4",
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
      "definition_site": "00496858",
      "incomplete_value": true,
      "site": "0049685c",
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
      "definition_site": "004b9714",
      "incomplete_value": true,
      "site": "004b9718",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0049687c",
      "incomplete_value": true,
      "site": "00496880",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:18:8"
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
      "definition_site": "004b9710",
      "incomplete_value": false,
      "site": "004b9718",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00496878",
      "incomplete_value": false,
      "site": "00496880",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004b96dc",
      "READ",
      [
        "storage",
        "00c1b010",
        null,
        "pointer"
      ]
    ],
    [
      "004b96f4",
      "DATA",
      [
        "storage",
        "00becca0",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b9710",
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
      "004b96dc",
      "READ",
      [
        "storage",
        "00c9aa00",
        null,
        "pointer"
      ]
    ],
    [
      "004b96f4",
      "DATA",
      [
        "storage",
        "00c69860",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b9710",
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

- 旧版 [`00496880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/004967a4.md#insn-00496880) · [`00496908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/004967a4.md#insn-00496908) · [`0049697c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/004967a4.md#insn-0049697c)
- 新版 [`004b9718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b963c.md#insn-004b9718) · [`004b97a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b963c.md#insn-004b97a0) · [`004b9814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b963c.md#insn-004b9814)

~~~diff
- 00496880 ["INT_ADD", "register:40f0:8", ["const:496880:8", "const:4:8"]]
- 00496880 ["CALL", null, ["callee:00c57b10:8"]]
+ 004b9718 ["INT_ADD", "register:40f0:8", ["const:4b9718:8", "const:4:8"]]
+ 004b9718 ["CALL", null, ["callee:00c57b10:8"]]
- 00496880 bytes 10121d94
+ 004b9718 bytes fe781e94
- 00496908 ["COPY", "register:0:8", ["register:4048:8"]]
- 00496908 ["INT_ADD", "register:40f0:8", ["const:496908:8", "const:4:8"]]
- 00496908 ["CALLIND", null, ["register:0:8"]]
+ 004b97a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b97a0 ["INT_ADD", "register:40f0:8", ["const:4b97a0:8", "const:4:8"]]
+ 004b97a0 ["CALLIND", null, ["register:0:8"]]
- 00496908 bytes 20013fd6
+ 004b97a0 bytes 20013fd6
- 0049697c ["INT_ADD", "register:40f0:8", ["const:49697c:8", "const:4:8"]]
- 0049697c ["CALL", null, ["callee:0043dd98:8"]]
+ 004b9814 ["INT_ADD", "register:40f0:8", ["const:4b9814:8", "const:4:8"]]
+ 004b9814 ["CALL", null, ["callee:0043dd98:8"]]
- 0049697c bytes 4712fe97
+ 004b9814 bytes 6111fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3bbee468ff41bbe18d44f5cd2e4046c"></a>

### [`00496a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496a24.md) → [`004b98bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b98bc.md) _ZN5Botan6BigIntrMEj

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00498c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004bbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.95% / 新版 96.95%

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
      "definition_site": "004b9ab8",
      "incomplete_value": true,
      "site": "004b9abc",
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
      "definition_site": "00496c20",
      "incomplete_value": true,
      "site": "00496c24",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b9ac0",
      "incomplete_value": true,
      "site": "004b9ac4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00496c28",
      "incomplete_value": true,
      "site": "00496c2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:18:8"
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
      "definition_site": "004b9aac",
      "incomplete_value": false,
      "site": "004b9ac4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00496c14",
      "incomplete_value": false,
      "site": "00496c2c",
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
      "004b9a98",
      "READ",
      [
        "storage",
        "00c1b010",
        null,
        "pointer"
      ]
    ],
    [
      "004b9aac",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004b9abc",
      "DATA",
      [
        "storage",
        "00becca0",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004b9a98",
      "READ",
      [
        "storage",
        "00c9aa00",
        null,
        "pointer"
      ]
    ],
    [
      "004b9aac",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b9abc",
      "DATA",
      [
        "storage",
        "00c69860",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00496c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496a24.md#insn-00496c2c) · [`00496a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496a24.md#insn-00496a78) · [`00496acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496a24.md#insn-00496acc)
- 新版 [`004b9ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b98bc.md#insn-004b9ac4) · [`004b9910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b98bc.md#insn-004b9910) · [`004b9964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b98bc.md#insn-004b9964)

~~~diff
- 00496c2c ["INT_ADD", "register:40f0:8", ["const:496c2c:8", "const:4:8"]]
- 00496c2c ["CALL", null, ["callee:00c57b10:8"]]
+ 004b9ac4 ["INT_ADD", "register:40f0:8", ["const:4b9ac4:8", "const:4:8"]]
+ 004b9ac4 ["CALL", null, ["callee:00c57b10:8"]]
- 00496c2c bytes 25111d94
+ 004b9ac4 bytes 13781e94
- 00496a78 ["INT_ADD", "register:40f0:8", ["const:496a78:8", "const:4:8"]]
- 00496a78 ["CALL", null, ["callee:00c57c90:8"]]
+ 004b9910 ["INT_ADD", "register:40f0:8", ["const:4b9910:8", "const:4:8"]]
+ 004b9910 ["CALL", null, ["callee:00c57c90:8"]]
- 00496a78 bytes f2111d94
+ 004b9910 bytes e0781e94
- 00496acc ["INT_ADD", "register:40f0:8", ["const:496acc:8", "const:4:8"]]
- 00496acc ["CALL", null, ["callee:004bbb2c:8"]]
+ 004b9964 ["INT_ADD", "register:40f0:8", ["const:4b9964:8", "const:4:8"]]
+ 004b9964 ["CALL", null, ["callee:004bbb2c:8"]]
- 00496acc bytes 72080094
+ 004b9964 bytes 72080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-427600eb7c4f4051145205ebe549b502"></a>

### [`00496ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496ee0.md) → [`004b9d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9d78.md) _ZN5BotanplERKNS_6BigIntES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbe60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe60.md) · 呼出先 4件 [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00495a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md) [`004b3e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3e3c.md) [`00bdbdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdd0.md)
- 新版 呼出元 1件 [`00c588b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588b0.md) · 呼出先 4件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b890c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md) [`004d6cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6cd4.md) [`00c58820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58820.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.92% / 新版 98.92%

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
      "site": "004b9df4",
      "value": [
        "leaf",
        "ram:c58820:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00496f5c",
      "value": [
        "leaf",
        "ram:bdbdd0:8"
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
      "004b9df4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbdd0"
      ]
    ]
  ],
  "added": [
    [
      "004b9df4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58820"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00496f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496ee0.md#insn-00496f5c) · [`00496f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496ee0.md#insn-00496f88) · [`00496fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496ee0.md#insn-00496fb8)
- 新版 [`004b9df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9d78.md#insn-004b9df4) · [`004b9e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9d78.md#insn-004b9e20) · [`004b9e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9d78.md#insn-004b9e50)

~~~diff
- 00496f5c ["INT_ADD", "register:40f0:8", ["const:496f5c:8", "const:4:8"]]
- 00496f5c ["CALL", null, ["ram:bdbdd0:8"]]
+ 004b9df4 ["INT_ADD", "register:40f0:8", ["const:4b9df4:8", "const:4:8"]]
+ 004b9df4 ["CALL", null, ["ram:c58820:8"]]
- 00496f5c bytes 9d131d94
+ 004b9df4 bytes 8b7a1e94
- 00496f88 ["INT_ADD", "register:40f0:8", ["const:496f88:8", "const:4:8"]]
- 00496f88 ["CALL", null, ["callee:004d6cd4:8"]]
+ 004b9e20 ["INT_ADD", "register:40f0:8", ["const:4b9e20:8", "const:4:8"]]
+ 004b9e20 ["CALL", null, ["callee:004d6cd4:8"]]
- 00496f88 bytes ad730094
+ 004b9e20 bytes ad730094
- 00496fb8 ["INT_ADD", "register:40f0:8", ["const:496fb8:8", "const:4:8"]]
- 00496fb8 ["CALL", null, ["callee:004b8774:8"]]
+ 004b9e50 ["INT_ADD", "register:40f0:8", ["const:4b9e50:8", "const:4:8"]]
+ 004b9e50 ["CALL", null, ["callee:004b8774:8"]]
- 00496fb8 bytes 49faff97
+ 004b9e50 bytes 49faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b95c1530b0e21871bfc1e402517ca8cd"></a>

### [`00497068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497068.md) → [`004b9f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9f00.md) _ZN5BotanmiERKNS_6BigIntES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbe70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe70.md) · 呼出先 4件 [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00495a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md) [`004b3e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3e3c.md) [`00bdbdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdd0.md)
- 新版 呼出元 1件 [`00c588c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588c0.md) · 呼出先 4件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b890c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md) [`004d6cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6cd4.md) [`00c58820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58820.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.40% / 新版 99.40%

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
      "site": "004b9f94",
      "value": [
        "leaf",
        "ram:c58820:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004970fc",
      "value": [
        "leaf",
        "ram:bdbdd0:8"
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
      "004b9f94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbdd0"
      ]
    ]
  ],
  "added": [
    [
      "004b9f94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58820"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004970fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497068.md#insn-004970fc) · [`004970e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497068.md#insn-004970e0) · [`00497130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497068.md#insn-00497130)
- 新版 [`004b9f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9f00.md#insn-004b9f94) · [`004b9f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9f00.md#insn-004b9f78) · [`004b9fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9f00.md#insn-004b9fc8)

~~~diff
- 004970fc ["INT_ADD", "register:40f0:8", ["const:4970fc:8", "const:4:8"]]
- 004970fc ["CALL", null, ["ram:bdbdd0:8"]]
+ 004b9f94 ["INT_ADD", "register:40f0:8", ["const:4b9f94:8", "const:4:8"]]
+ 004b9f94 ["CALL", null, ["ram:c58820:8"]]
- 004970fc bytes 35131d94
+ 004b9f94 bytes 237a1e94
- 004970e0 ["INT_ADD", "register:40f0:8", ["const:4970e0:8", "const:4:8"]]
- 004970e0 ["CALL", null, ["callee:004b8774:8"]]
+ 004b9f78 ["INT_ADD", "register:40f0:8", ["const:4b9f78:8", "const:4:8"]]
+ 004b9f78 ["CALL", null, ["callee:004b8774:8"]]
- 004970e0 bytes fff9ff97
+ 004b9f78 bytes fff9ff97
- 00497130 ["INT_ADD", "register:40f0:8", ["const:497130:8", "const:4:8"]]
- 00497130 ["CALL", null, ["callee:004b890c:8"]]
+ 004b9fc8 ["INT_ADD", "register:40f0:8", ["const:4b9fc8:8", "const:4:8"]]
+ 004b9fc8 ["CALL", null, ["callee:004b890c:8"]]
- 00497130 bytes 51faff97
+ 004b9fc8 bytes 51faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1967d4606906068875df0f71d6b52388"></a>

### [`0049731c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/0049731c.md) → [`004ba1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba1b4.md) _ZN5BotanmlERKNS_6BigIntES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbe00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe00.md) · 呼出先 7件 [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`00496208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496208.md) [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 1件 [`00c58850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58850.md) · 呼出先 7件 [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004b90a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b90a0.md) [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.35% / 新版 99.35%

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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ba254",
      "value": [
        "leaf",
        "ram:c58820:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004973bc",
      "value": [
        "leaf",
        "ram:bdbdd0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ba360",
      "incomplete_value": true,
      "site": "004ba360",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004974c8",
      "incomplete_value": true,
      "site": "004974c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ba254",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbdd0"
      ]
    ],
    [
      "004ba350",
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
      "004ba254",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58820"
      ]
    ],
    [
      "004ba350",
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

- 旧版 [`004973bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/0049731c.md#insn-004973bc) · [`004974c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/0049731c.md#insn-004974c8) · [`0049742c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/0049731c.md#insn-0049742c)
- 新版 [`004ba254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba1b4.md#insn-004ba254) · [`004ba360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba1b4.md#insn-004ba360) · [`004ba2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba1b4.md#insn-004ba2c4)

~~~diff
- 004973bc ["INT_ADD", "register:40f0:8", ["const:4973bc:8", "const:4:8"]]
- 004973bc ["CALL", null, ["ram:bdbdd0:8"]]
+ 004ba254 ["INT_ADD", "register:40f0:8", ["const:4ba254:8", "const:4:8"]]
+ 004ba254 ["CALL", null, ["ram:c58820:8"]]
- 004973bc bytes 85121d94
+ 004ba254 bytes 73791e94
- 004974c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004974c8 ["INT_ADD", "register:40f0:8", ["const:4974c8:8", "const:4:8"]]
- 004974c8 ["CALLIND", null, ["register:0:8"]]
+ 004ba360 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ba360 ["INT_ADD", "register:40f0:8", ["const:4ba360:8", "const:4:8"]]
+ 004ba360 ["CALLIND", null, ["register:0:8"]]
- 004974c8 bytes 20013fd6
+ 004ba360 bytes 20013fd6
- 0049742c ["INT_ADD", "register:40f0:8", ["const:49742c:8", "const:4:8"]]
- 0049742c ["CALL", null, ["callee:004b8810:8"]]
+ 004ba2c4 ["INT_ADD", "register:40f0:8", ["const:4ba2c4:8", "const:4:8"]]
+ 004ba2c4 ["CALL", null, ["callee:004b8810:8"]]
- 0049742c bytes 53f9ff97
+ 004ba2c4 bytes 53f9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08af7264421e14783b046889e8c60b76"></a>

### [`004975c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/004975c0.md) → [`004ba458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba458.md) _ZN5BotanrmERKNS_6BigIntEj

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbe80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe80.md) · 呼出先 4件 [`00498c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c588d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588d0.md) · 呼出先 4件 [`004bbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.51% / 新版 95.51%

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
      "definition_site": "004ba5ac",
      "incomplete_value": true,
      "site": "004ba5b0",
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
      "definition_site": "00497714",
      "incomplete_value": true,
      "site": "00497718",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ba5b4",
      "incomplete_value": true,
      "site": "004ba5b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0049771c",
      "incomplete_value": true,
      "site": "00497720",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:18:8"
              ]
            ]
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
      "definition_site": "004ba5a0",
      "incomplete_value": false,
      "site": "004ba5b8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00497708",
      "incomplete_value": false,
      "site": "00497720",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004ba58c",
      "READ",
      [
        "storage",
        "00c1b010",
        null,
        "pointer"
      ]
    ],
    [
      "004ba5a0",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004ba5b0",
      "DATA",
      [
        "storage",
        "00becca0",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004ba58c",
      "READ",
      [
        "storage",
        "00c9aa00",
        null,
        "pointer"
      ]
    ],
    [
      "004ba5a0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ba5b0",
      "DATA",
      [
        "storage",
        "00c69860",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/004975c0.md#insn-00497720) · [`0049765c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/004975c0.md#insn-0049765c) · [`004976bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/004975c0.md#insn-004976bc)
- 新版 [`004ba5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba458.md#insn-004ba5b8) · [`004ba4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba458.md#insn-004ba4f4) · [`004ba554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba458.md#insn-004ba554)

~~~diff
- 00497720 ["INT_ADD", "register:40f0:8", ["const:497720:8", "const:4:8"]]
- 00497720 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ba5b8 ["INT_ADD", "register:40f0:8", ["const:4ba5b8:8", "const:4:8"]]
+ 004ba5b8 ["CALL", null, ["callee:00c57b10:8"]]
- 00497720 bytes 680e1d94
+ 004ba5b8 bytes 56751e94
- 0049765c ["INT_ADD", "register:40f0:8", ["const:49765c:8", "const:4:8"]]
- 0049765c ["CALL", null, ["callee:004bbb2c:8"]]
+ 004ba4f4 ["INT_ADD", "register:40f0:8", ["const:4ba4f4:8", "const:4:8"]]
+ 004ba4f4 ["CALL", null, ["callee:004bbb2c:8"]]
- 0049765c bytes 8e050094
+ 004ba4f4 bytes 8e050094
- 004976bc ["INT_ADD", "register:40f0:8", ["const:4976bc:8", "const:4:8"]]
- 004976bc ["CALL", null, ["callee:00c57af0:8"]]
+ 004ba554 ["INT_ADD", "register:40f0:8", ["const:4ba554:8", "const:4:8"]]
+ 004ba554 ["CALL", null, ["callee:00c57af0:8"]]
- 004976bc bytes 790e1d94
+ 004ba554 bytes 67751e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5f1d0ca9e2709b9d73d4873529160d7"></a>

### [`00497724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497724.md) → [`004ba5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba5bc.md) _ZN5BotanlsERKNS_6BigIntEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdbcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md) [`00bdbdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md) [`00c58820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58820.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

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
      "site": "004ba61c",
      "value": [
        "leaf",
        "ram:c58820:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00497784",
      "value": [
        "leaf",
        "ram:bdbdd0:8"
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
      "004ba61c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbdd0"
      ]
    ],
    [
      "004ba6d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ]
  ],
  "added": [
    [
      "004ba61c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58820"
      ]
    ],
    [
      "004ba6d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497724.md#insn-00497784) · [`0049783c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497724.md#insn-0049783c)
- 新版 [`004ba61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba5bc.md#insn-004ba61c) · [`004ba6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba5bc.md#insn-004ba6d4)

~~~diff
- 00497784 ["INT_ADD", "register:40f0:8", ["const:497784:8", "const:4:8"]]
- 00497784 ["CALL", null, ["ram:bdbdd0:8"]]
+ 004ba61c ["INT_ADD", "register:40f0:8", ["const:4ba61c:8", "const:4:8"]]
+ 004ba61c ["CALL", null, ["ram:c58820:8"]]
- 00497784 bytes 93111d94
+ 004ba61c bytes 81781e94
- 0049783c ["BRANCH", null, ["ram:bdbcf0:8"]]
+ 004ba6d4 ["BRANCH", null, ["ram:c58740:8"]]
- 0049783c bytes 2d111d14
+ 004ba6d4 bytes 1b781e14
~~~


<a id="compare-c0947923ce1bb42e055f0614ee8f8c74"></a>

### [`00497874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497874.md) → [`004ba70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba70c.md) _ZN5BotanrsERKNS_6BigIntEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbe90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe90.md) · 呼出先 3件 [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md) [`00bdbdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdd0.md)
- 新版 呼出元 1件 [`00c588e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588e0.md) · 呼出先 3件 [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md) [`00c58820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58820.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

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
      "site": "004ba7e8",
      "value": [
        "leaf",
        "ram:c58820:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00497950",
      "value": [
        "leaf",
        "ram:bdbdd0:8"
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
      "004ba788",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004ba7e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbdd0"
      ]
    ]
  ],
  "added": [
    [
      "004ba788",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004ba7e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58820"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497874.md#insn-00497950) · [`004978f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497874.md#insn-004978f0)
- 新版 [`004ba7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba70c.md#insn-004ba7e8) · [`004ba788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba70c.md#insn-004ba788)

~~~diff
- 00497950 ["INT_ADD", "register:40f0:8", ["const:497950:8", "const:4:8"]]
- 00497950 ["CALL", null, ["ram:bdbdd0:8"]]
+ 004ba7e8 ["INT_ADD", "register:40f0:8", ["const:4ba7e8:8", "const:4:8"]]
+ 004ba7e8 ["CALL", null, ["ram:c58820:8"]]
- 00497950 bytes 20111d94
+ 004ba7e8 bytes 0e781e94
- 004978f0 ["BRANCH", null, ["ram:bdbcf0:8"]]
+ 004ba788 ["BRANCH", null, ["ram:c58740:8"]]
- 004978f0 bytes 00111d14
+ 004ba788 bytes ee771e14
~~~


<a id="compare-86eebcd1063992229ef0125f3ea920d8"></a>

### [`00498254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498254.md) → [`004bb0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb0ec.md) _ZNK5Botan6BigInt13get_substringEmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbec0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58910.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.52% / 新版 98.52%

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
      "definition_site": "004bb2b8",
      "incomplete_value": false,
      "site": "004bb2c0",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498420",
      "incomplete_value": false,
      "site": "00498428",
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
            "const:a84:8"
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
      "definition_site": "004bb2f4",
      "incomplete_value": true,
      "site": "004bb300",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049845c",
      "incomplete_value": true,
      "site": "00498468",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb2f0",
      "incomplete_value": false,
      "site": "004bb300",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00498458",
      "incomplete_value": false,
      "site": "00498468",
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
      "004bb2b8",
      "PARAM",
      [
        "storage",
        "0028fa84",
        null,
        "string"
      ]
    ],
    [
      "004bb2f0",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004bb2f4",
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
      "004bb2b8",
      "PARAM",
      [
        "storage",
        "0029eec4",
        null,
        "string"
      ]
    ],
    [
      "004bb2f0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bb2f4",
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

- 旧版 [`00498428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498254.md#insn-00498428) · [`00498468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498254.md#insn-00498468) · [`00498414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498254.md#insn-00498414)
- 新版 [`004bb2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb0ec.md#insn-004bb2c0) · [`004bb300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb0ec.md#insn-004bb300) · [`004bb2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb0ec.md#insn-004bb2ac)

~~~diff
- 00498428 ["INT_ADD", "register:40f0:8", ["const:498428:8", "const:4:8"]]
- 00498428 ["CALL", null, ["callee:0043dd98:8"]]
+ 004bb2c0 ["INT_ADD", "register:40f0:8", ["const:4bb2c0:8", "const:4:8"]]
+ 004bb2c0 ["CALL", null, ["callee:0043dd98:8"]]
- 00498428 bytes 9c0bfe97
+ 004bb2c0 bytes b60afe97
- 00498468 ["INT_ADD", "register:40f0:8", ["const:498468:8", "const:4:8"]]
- 00498468 ["CALL", null, ["callee:00c57b10:8"]]
+ 004bb300 ["INT_ADD", "register:40f0:8", ["const:4bb300:8", "const:4:8"]]
+ 004bb300 ["CALL", null, ["callee:00c57b10:8"]]
- 00498468 bytes 160b1d94
+ 004bb300 bytes 04721e94
- 00498414 ["INT_ADD", "register:40f0:8", ["const:498414:8", "const:4:8"]]
- 00498414 ["CALL", null, ["callee:00c57af0:8"]]
+ 004bb2ac ["INT_ADD", "register:40f0:8", ["const:4bb2ac:8", "const:4:8"]]
+ 004bb2ac ["CALL", null, ["callee:00c57af0:8"]]
- 00498414 bytes 230b1d94
+ 004bb2ac bytes 11721e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e27e91408fd91d212d2fd1839c152edf"></a>

### [`004984bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004984bc.md) → [`004bb354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb354.md) _ZNK5Botan6BigInt9to_u32bitEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

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
      "definition_site": "004bb43c",
      "incomplete_value": false,
      "site": "004bb444",
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
            "const:85d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004985a4",
      "incomplete_value": false,
      "site": "004985ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:7e5:8"
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
      "definition_site": "004bb478",
      "incomplete_value": true,
      "site": "004bb484",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004985e0",
      "incomplete_value": true,
      "site": "004985ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb474",
      "incomplete_value": false,
      "site": "004bb484",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004985dc",
      "incomplete_value": false,
      "site": "004985ec",
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
      "004bb43c",
      "PARAM",
      [
        "storage",
        "002ac7e5",
        null,
        "string"
      ]
    ],
    [
      "004bb474",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004bb478",
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
      "004bb43c",
      "PARAM",
      [
        "storage",
        "002bd85d",
        null,
        "string"
      ]
    ],
    [
      "004bb474",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bb478",
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

- 旧版 [`004985ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004984bc.md#insn-004985ac) · [`004985ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004984bc.md#insn-004985ec) · [`00498610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004984bc.md#insn-00498610)
- 新版 [`004bb444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb354.md#insn-004bb444) · [`004bb484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb354.md#insn-004bb484) · [`004bb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb354.md#insn-004bb4a8)

~~~diff
- 004985ac ["INT_ADD", "register:40f0:8", ["const:4985ac:8", "const:4:8"]]
- 004985ac ["CALL", null, ["callee:0043dd98:8"]]
+ 004bb444 ["INT_ADD", "register:40f0:8", ["const:4bb444:8", "const:4:8"]]
+ 004bb444 ["CALL", null, ["callee:0043dd98:8"]]
- 004985ac bytes 3b0bfe97
+ 004bb444 bytes 550afe97
- 004985ec ["INT_ADD", "register:40f0:8", ["const:4985ec:8", "const:4:8"]]
- 004985ec ["CALL", null, ["callee:00c57b10:8"]]
+ 004bb484 ["INT_ADD", "register:40f0:8", ["const:4bb484:8", "const:4:8"]]
+ 004bb484 ["CALL", null, ["callee:00c57b10:8"]]
- 004985ec bytes b50a1d94
+ 004bb484 bytes a3711e94
- 00498610 ["INT_ADD", "register:40f0:8", ["const:498610:8", "const:4:8"]]
- 00498610 ["CALL", null, ["callee:0043dd98:8"]]
+ 004bb4a8 ["INT_ADD", "register:40f0:8", ["const:4bb4a8:8", "const:4:8"]]
+ 004bb4a8 ["CALL", null, ["callee:0043dd98:8"]]
- 00498610 bytes 220bfe97
+ 004bb4a8 bytes 3c0afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-016aeb5ee5722e24d6779ac6a6b8ea30"></a>

### [`00498754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498754.md) → [`004bb5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb5ec.md) _ZNK5Botan6BigIntngEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdbcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md)

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
      "site": "004bb604",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0049876c",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
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
      "004bb604",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ]
  ],
  "added": [
    [
      "004bb604",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049876c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498754.md#insn-0049876c)
- 新版 [`004bb604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb5ec.md#insn-004bb604)

~~~diff
- 0049876c ["INT_ADD", "register:40f0:8", ["const:49876c:8", "const:4:8"]]
- 0049876c ["CALL", null, ["ram:bdbcf0:8"]]
+ 004bb604 ["INT_ADD", "register:40f0:8", ["const:4bb604:8", "const:4:8"]]
+ 004bb604 ["CALL", null, ["ram:c58740:8"]]
- 0049876c bytes 610d1d94
+ 004bb604 bytes 4f741e94
~~~


<a id="compare-24852f9c21df18f1a5140fdb2ef2cca1"></a>

### [`004987cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004987cc.md) → [`004bb664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb664.md) _ZNK5Botan6BigInt3absEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdbcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md)

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
      "site": "004bb67c",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004987e4",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
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
      "004bb67c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ]
  ],
  "added": [
    [
      "004bb67c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004987e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004987cc.md#insn-004987e4)
- 新版 [`004bb67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb664.md#insn-004bb67c)

~~~diff
- 004987e4 ["INT_ADD", "register:40f0:8", ["const:4987e4:8", "const:4:8"]]
- 004987e4 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004bb67c ["INT_ADD", "register:40f0:8", ["const:4bb67c:8", "const:4:8"]]
+ 004bb67c ["CALL", null, ["ram:c58740:8"]]
- 004987e4 bytes 430d1d94
+ 004bb67c bytes 31741e94
~~~


<a id="compare-68c77ad4a4ae86c91b249a8783e57a6c"></a>

### [`00498858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498858.md) → [`004bb6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb6f0.md) _ZN5Botan6BigInt17const_time_lookupERNSt6__ndk16vectorIjNS_16secure_allocatorIjEEEERKNS2_IS0_NS1_9allocatorIS0_EEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbed0.md) · 呼出先 2件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 1件 [`00c58920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58920.md) · 呼出先 2件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.04% / 新版 96.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb860",
      "incomplete_value": false,
      "site": "004bb880",
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
            "const:14b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004989c8",
      "incomplete_value": false,
      "site": "004989e8",
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
            "const:5dc:8"
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
      "definition_site": "004bb868",
      "incomplete_value": false,
      "site": "004bb880",
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
            "const:ef2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004989d0",
      "incomplete_value": false,
      "site": "004989e8",
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
            "const:ab2:8"
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
      "definition_site": "004bb870",
      "incomplete_value": false,
      "site": "004bb880",
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
            "const:4f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004989d8",
      "incomplete_value": false,
      "site": "004989e8",
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
            "const:5d4:8"
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
      "004bb860",
      "PARAM",
      [
        "storage",
        "002a75dc",
        null,
        "string"
      ]
    ],
    [
      "004bb868",
      "PARAM",
      [
        "storage",
        "0028fab2",
        null,
        "string"
      ]
    ],
    [
      "004bb870",
      "PARAM",
      [
        "storage",
        "002ab5d4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bb860",
      "PARAM",
      [
        "storage",
        "002b814b",
        null,
        "string"
      ]
    ],
    [
      "004bb868",
      "PARAM",
      [
        "storage",
        "0029eef2",
        null,
        "string"
      ]
    ],
    [
      "004bb870",
      "PARAM",
      [
        "storage",
        "002bc4f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004989e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498858.md#insn-004989e8) · [`00498890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498858.md#insn-00498890) · [`004989c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498858.md#insn-004989c4)
- 新版 [`004bb880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb6f0.md#insn-004bb880) · [`004bb728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb6f0.md#insn-004bb728) · [`004bb85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb6f0.md#insn-004bb85c)

~~~diff
- 004989e8 ["INT_ADD", "register:40f0:8", ["const:4989e8:8", "const:4:8"]]
- 004989e8 ["CALL", null, ["callee:00c58250:8"]]
+ 004bb880 ["INT_ADD", "register:40f0:8", ["const:4bb880:8", "const:4:8"]]
+ 004bb880 ["CALL", null, ["callee:00c58250:8"]]
- 004989e8 bytes 860b1d94
+ 004bb880 bytes 74721e94
- 00498890 ["INT_ADD", "register:40f0:8", ["const:498890:8", "const:4:8"]]
- 00498890 ["CALL", null, ["callee:00c57c90:8"]]
+ 004bb728 ["INT_ADD", "register:40f0:8", ["const:4bb728:8", "const:4:8"]]
+ 004bb728 ["CALL", null, ["callee:00c57c90:8"]]
- 00498890 bytes 6c0a1d94
+ 004bb728 bytes 5a711e94
- 004989c4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 004bb85c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 004989c4 bytes 60f0fff0
+ 004bb85c bytes e0efffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-489d2be46c6d882cec5564202850fbde"></a>

### [`004989ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004989ec.md) → [`004bb884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb884.md) FUN_004bb884

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00493850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493850.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md) [`00bdbdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdf0.md)
- 新版 呼出元 1件 [`004b66e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md) · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md) [`00c58840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58840.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.48% / 新版 95.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bba14",
      "incomplete_value": true,
      "site": "004bba14",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "00498b7c",
      "incomplete_value": true,
      "site": "00498b7c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004bba28",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00498b90",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bbaa4",
      "incomplete_value": true,
      "site": "004bbaa4",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "00498c0c",
      "incomplete_value": true,
      "site": "00498c0c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:778:8"
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
      "004bba04",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bba28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004bba94",
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
      "004bba04",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004bba28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004bba94",
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

- 旧版 [`00498b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004989ec.md#insn-00498b7c) · [`00498b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004989ec.md#insn-00498b90) · [`00498c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004989ec.md#insn-00498c0c)
- 新版 [`004bba14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb884.md#insn-004bba14) · [`004bba28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb884.md#insn-004bba28) · [`004bbaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb884.md#insn-004bbaa4)

~~~diff
- 00498b7c ["COPY", "register:0:8", ["register:4048:8"]]
- 00498b7c ["INT_ADD", "register:40f0:8", ["const:498b7c:8", "const:4:8"]]
- 00498b7c ["CALLIND", null, ["register:0:8"]]
+ 004bba14 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bba14 ["INT_ADD", "register:40f0:8", ["const:4bba14:8", "const:4:8"]]
+ 004bba14 ["CALLIND", null, ["register:0:8"]]
- 00498b7c bytes 20013fd6
+ 004bba14 bytes 20013fd6
- 00498b90 ["INT_ADD", "register:40f0:8", ["const:498b90:8", "const:4:8"]]
- 00498b90 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004bba28 ["INT_ADD", "register:40f0:8", ["const:4bba28:8", "const:4:8"]]
+ 004bba28 ["CALL", null, ["ram:c58740:8"]]
- 00498b90 bytes 580c1d94
+ 004bba28 bytes 46731e94
- 00498c0c ["COPY", "register:0:8", ["register:4048:8"]]
- 00498c0c ["INT_ADD", "register:40f0:8", ["const:498c0c:8", "const:4:8"]]
- 00498c0c ["CALLIND", null, ["register:0:8"]]
+ 004bbaa4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bbaa4 ["INT_ADD", "register:40f0:8", ["const:4bbaa4:8", "const:4:8"]]
+ 004bbaa4 ["CALLIND", null, ["register:0:8"]]
- 00498c0c bytes 20013fd6
+ 004bbaa4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe66a75aacfa32d94c36b393708c5ab3"></a>

### [`00498c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md) → [`004bbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md) FUN_004bbb2c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00493850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493850.md) [`00496a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496a24.md) [`004975c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/004975c0.md) [`004bb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb030.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 4件 [`004b66e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md) [`004b98bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b98bc.md) [`004ba458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba458.md) [`004ddec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004ddec8.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

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
      "definition_site": "004bbb98",
      "incomplete_value": false,
      "site": "004bbba0",
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
            "const:d64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498d00",
      "incomplete_value": false,
      "site": "00498d08",
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
            "const:4f7:8"
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
      "definition_site": "004bbbd4",
      "incomplete_value": true,
      "site": "004bbbe0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00498d3c",
      "incomplete_value": true,
      "site": "00498d48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bbbd0",
      "incomplete_value": false,
      "site": "004bbbe0",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00498d38",
      "incomplete_value": false,
      "site": "00498d48",
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
      "004bbb98",
      "PARAM",
      [
        "storage",
        "002a44f7",
        null,
        "string"
      ]
    ],
    [
      "004bbbd0",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004bbbd4",
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
      "004bbb98",
      "PARAM",
      [
        "storage",
        "002b4d64",
        null,
        "string"
      ]
    ],
    [
      "004bbbd0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bbbd4",
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

- 旧版 [`00498d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md#insn-00498d08) · [`00498d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md#insn-00498d48) · [`00498cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md#insn-00498cf4)
- 新版 [`004bbba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md#insn-004bbba0) · [`004bbbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md#insn-004bbbe0) · [`004bbb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md#insn-004bbb8c)

~~~diff
- 00498d08 ["INT_ADD", "register:40f0:8", ["const:498d08:8", "const:4:8"]]
- 00498d08 ["CALL", null, ["callee:0043dd98:8"]]
+ 004bbba0 ["INT_ADD", "register:40f0:8", ["const:4bbba0:8", "const:4:8"]]
+ 004bbba0 ["CALL", null, ["callee:0043dd98:8"]]
- 00498d08 bytes 6409fe97
+ 004bbba0 bytes 7e08fe97
- 00498d48 ["INT_ADD", "register:40f0:8", ["const:498d48:8", "const:4:8"]]
- 00498d48 ["CALL", null, ["callee:00c57b10:8"]]
+ 004bbbe0 ["INT_ADD", "register:40f0:8", ["const:4bbbe0:8", "const:4:8"]]
+ 004bbbe0 ["CALL", null, ["callee:00c57b10:8"]]
- 00498d48 bytes de081d94
+ 004bbbe0 bytes cc6f1e94
- 00498cf4 ["INT_ADD", "register:40f0:8", ["const:498cf4:8", "const:4:8"]]
- 00498cf4 ["CALL", null, ["callee:00c57af0:8"]]
+ 004bbb8c ["INT_ADD", "register:40f0:8", ["const:4bbb8c:8", "const:4:8"]]
+ 004bbb8c ["CALL", null, ["callee:00c57af0:8"]]
- 00498cf4 bytes eb081d94
+ 004bbb8c bytes d96f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1710d2682570a2749d8663e6060749"></a>

### [`00499128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499128.md) → [`004bbfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbfc0.md) _ZN5Botan11BlockCipher15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
      "definition_site": "004bc038",
      "incomplete_value": false,
      "site": "004bc040",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004991a0",
      "incomplete_value": false,
      "site": "004991a8",
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
            "const:72a:8"
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
      "definition_site": "004bc078",
      "incomplete_value": true,
      "site": "004bc084",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004991e0",
      "incomplete_value": true,
      "site": "004991ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38:8"
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
      "definition_site": "004bc074",
      "incomplete_value": false,
      "site": "004bc084",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004991dc",
      "incomplete_value": false,
      "site": "004991ec",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004bc038",
      "PARAM",
      [
        "storage",
        "0029472a",
        null,
        "string"
      ]
    ],
    [
      "004bc074",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004bc078",
      "READ",
      [
        "storage",
        "00c1b038",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bc038",
      "PARAM",
      [
        "storage",
        "002a4040",
        null,
        "string"
      ]
    ],
    [
      "004bc074",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bc078",
      "READ",
      [
        "storage",
        "00c9aa28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004991a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499128.md#insn-004991a8) · [`004991ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499128.md#insn-004991ec) · [`0049915c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499128.md#insn-0049915c)
- 新版 [`004bc040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbfc0.md#insn-004bc040) · [`004bc084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbfc0.md#insn-004bc084) · [`004bbff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbfc0.md#insn-004bbff4)

~~~diff
- 004991a8 ["INT_ADD", "register:40f0:8", ["const:4991a8:8", "const:4:8"]]
- 004991a8 ["CALL", null, ["callee:0043dd98:8"]]
+ 004bc040 ["INT_ADD", "register:40f0:8", ["const:4bc040:8", "const:4:8"]]
+ 004bc040 ["CALL", null, ["callee:0043dd98:8"]]
- 004991a8 bytes 3c08fe97
+ 004bc040 bytes 5607fe97
- 004991ec ["INT_ADD", "register:40f0:8", ["const:4991ec:8", "const:4:8"]]
- 004991ec ["CALL", null, ["callee:00c57b10:8"]]
+ 004bc084 ["INT_ADD", "register:40f0:8", ["const:4bc084:8", "const:4:8"]]
+ 004bc084 ["CALL", null, ["callee:00c57b10:8"]]
- 004991ec bytes b5071d94
+ 004bc084 bytes a36e1e94
- 0049915c ["INT_ADD", "register:40f0:8", ["const:49915c:8", "const:4:8"]]
- 0049915c ["CALL", null, ["callee:00c58930:8"]]
+ 004bbff4 ["INT_ADD", "register:40f0:8", ["const:4bbff4:8", "const:4:8"]]
+ 004bbff4 ["CALL", null, ["callee:00c58930:8"]]
- 0049915c bytes 610b1d94
+ 004bbff4 bytes 4f721e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-735701b48a47b7f68c4d4105f4122a97"></a>

### [`004994e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004994e0.md) → [`004bc378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc378.md) _ZN5Botan8CBC_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf10.md) · 呼出先 9件 [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58960.md) · 呼出先 9件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.64% / 新版 93.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004bc3b0",
      "incomplete_value": true,
      "site": "004bc3b0",
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
      "definition_site": "00499518",
      "incomplete_value": true,
      "site": "00499518",
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
      "definition_site": "004bc454",
      "incomplete_value": false,
      "site": "004bc460",
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
            "const:347:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004995bc",
      "incomplete_value": false,
      "site": "004995c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:5cb:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bc480",
      "incomplete_value": false,
      "site": "004bc488",
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
            "const:abe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004995e8",
      "incomplete_value": false,
      "site": "004995f0",
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
            "const:be5:8"
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
      "004bc3a0",
      "READ",
      [
        "storage",
        "00c1b040",
        null,
        "pointer"
      ]
    ],
    [
      "004bc3b0",
      "DATA",
      [
        "storage",
        "00be9460",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bc454",
      "PARAM",
      [
        "storage",
        "002aa5cb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bc3a0",
      "READ",
      [
        "storage",
        "00c9aa30",
        null,
        "pointer"
      ]
    ],
    [
      "004bc3b0",
      "DATA",
      [
        "storage",
        "00c66020",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bc454",
      "PARAM",
      [
        "storage",
        "002bb347",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004995c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004994e0.md#insn-004995c8) · [`004995f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004994e0.md#insn-004995f0) · [`0049963c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004994e0.md#insn-0049963c)
- 新版 [`004bc460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc378.md#insn-004bc460) · [`004bc488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc378.md#insn-004bc488) · [`004bc4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc378.md#insn-004bc4d4)

~~~diff
- 004995c8 ["INT_ADD", "register:40f0:8", ["const:4995c8:8", "const:4:8"]]
- 004995c8 ["CALL", null, ["callee:00c57b60:8"]]
+ 004bc460 ["INT_ADD", "register:40f0:8", ["const:4bc460:8", "const:4:8"]]
+ 004bc460 ["CALL", null, ["callee:00c57b60:8"]]
- 004995c8 bytes d2061d94
+ 004bc460 bytes c06d1e94
- 004995f0 ["INT_ADD", "register:40f0:8", ["const:4995f0:8", "const:4:8"]]
- 004995f0 ["CALL", null, ["callee:00c57b70:8"]]
+ 004bc488 ["INT_ADD", "register:40f0:8", ["const:4bc488:8", "const:4:8"]]
+ 004bc488 ["CALL", null, ["callee:00c57b70:8"]]
- 004995f0 bytes cc061d94
+ 004bc488 bytes ba6d1e94
- 0049963c ["INT_ADD", "register:40f0:8", ["const:49963c:8", "const:4:8"]]
- 0049963c ["CALL", null, ["callee:00c57b70:8"]]
+ 004bc4d4 ["INT_ADD", "register:40f0:8", ["const:4bc4d4:8", "const:4:8"]]
+ 004bc4d4 ["CALL", null, ["callee:00c57b70:8"]]
- 0049963c bytes b9061d94
+ 004bc4d4 bytes a76d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5d50e97d74e1af7ce7760917a864b7b"></a>

### [`00499860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499860.md) → [`004bc6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc6f8.md) _ZNK5Botan8CBC_Mode4nameEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf20.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 1件 [`00c58970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58970.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bc740",
      "incomplete_value": false,
      "site": "004bc748",
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
            "const:4d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004998a8",
      "incomplete_value": false,
      "site": "004998b0",
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
            "const:737:8"
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
      "definition_site": "004bc7ec",
      "incomplete_value": false,
      "site": "004bc7f4",
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
            "const:f5d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499954",
      "incomplete_value": false,
      "site": "0049995c",
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
            "const:a1b:8"
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
      "definition_site": "004bc880",
      "incomplete_value": false,
      "site": "004bc8a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:862:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004999e8",
      "incomplete_value": false,
      "site": "00499a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:6c9:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004bc740",
      "PARAM",
      [
        "storage",
        "00294737",
        null,
        "string"
      ]
    ],
    [
      "004bc7ec",
      "PARAM",
      [
        "storage",
        "00290a1b",
        null,
        "string"
      ]
    ],
    [
      "004bc880",
      "PARAM",
      [
        "storage",
        "0029c6c9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bc740",
      "PARAM",
      [
        "storage",
        "002a404d",
        null,
        "string"
      ]
    ],
    [
      "004bc7ec",
      "PARAM",
      [
        "storage",
        "0029ff5d",
        null,
        "string"
      ]
    ],
    [
      "004bc880",
      "PARAM",
      [
        "storage",
        "002ac862",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004998b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499860.md#insn-004998b0) · [`0049995c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499860.md#insn-0049995c) · [`00499a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499860.md#insn-00499a08)
- 新版 [`004bc748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc6f8.md#insn-004bc748) · [`004bc7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc6f8.md#insn-004bc7f4) · [`004bc8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc6f8.md#insn-004bc8a0)

~~~diff
- 004998b0 ["INT_ADD", "register:40f0:8", ["const:4998b0:8", "const:4:8"]]
- 004998b0 ["CALL", null, ["callee:00c57b70:8"]]
+ 004bc748 ["INT_ADD", "register:40f0:8", ["const:4bc748:8", "const:4:8"]]
+ 004bc748 ["CALL", null, ["callee:00c57b70:8"]]
- 004998b0 bytes 1c061d94
+ 004bc748 bytes 0a6d1e94
- 0049995c ["INT_ADD", "register:40f0:8", ["const:49995c:8", "const:4:8"]]
- 0049995c ["CALL", null, ["callee:00c57b70:8"]]
+ 004bc7f4 ["INT_ADD", "register:40f0:8", ["const:4bc7f4:8", "const:4:8"]]
+ 004bc7f4 ["CALL", null, ["callee:00c57b70:8"]]
- 0049995c bytes f1051d94
+ 004bc7f4 bytes df6c1e94
- 00499a08 ["INT_ADD", "register:40f0:8", ["const:499a08:8", "const:4:8"]]
- 00499a08 ["CALL", null, ["callee:00c58250:8"]]
+ 004bc8a0 ["INT_ADD", "register:40f0:8", ["const:4bc8a0:8", "const:4:8"]]
+ 004bc8a0 ["CALL", null, ["callee:00c58250:8"]]
- 00499a08 bytes 7e071d94
+ 004bc8a0 bytes 6c6e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d75cdd14fcd05345b8f156d01203c033"></a>

### [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) → [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) FUN_004bc9c0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`00499b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b20.md) [`0049c56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c56c.md) [`004a1190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1190.md) [`004a15d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a15d0.md) [`004a1e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1e34.md) · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf30.md)
- 新版 呼出元 10件 [`004bc9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9b8.md) [`004bf404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf404.md) [`004c4028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4028.md) [`004c4468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4468.md) [`004c4ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4ccc.md) · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58980.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

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
      "definition_site": "004bcab8",
      "incomplete_value": true,
      "site": "004bcac4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499c20",
      "incomplete_value": true,
      "site": "00499c2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:48:8"
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
      "definition_site": "004bcab4",
      "incomplete_value": false,
      "site": "004bcac4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00499c1c",
      "incomplete_value": false,
      "site": "00499c2c",
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
      "004bcab4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004bcab8",
      "READ",
      [
        "storage",
        "00c1b048",
        null,
        "pointer"
      ]
    ],
    [
      "004bcab8",
      "PARAM",
      [
        "storage",
        "00be9e68",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bcab4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bcab8",
      "READ",
      [
        "storage",
        "00c9aa38",
        null,
        "pointer"
      ]
    ],
    [
      "004bcab8",
      "PARAM",
      [
        "storage",
        "00c66a28",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00499c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md#insn-00499c2c) · [`00499b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md#insn-00499b60) · [`00499ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md#insn-00499ba0)
- 新版 [`004bcac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md#insn-004bcac4) · [`004bc9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md#insn-004bc9f8) · [`004bca38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md#insn-004bca38)

~~~diff
- 00499c2c ["INT_ADD", "register:40f0:8", ["const:499c2c:8", "const:4:8"]]
- 00499c2c ["CALL", null, ["callee:00c57b10:8"]]
+ 004bcac4 ["INT_ADD", "register:40f0:8", ["const:4bcac4:8", "const:4:8"]]
+ 004bcac4 ["CALL", null, ["callee:00c57b10:8"]]
- 00499c2c bytes 25051d94
+ 004bcac4 bytes 136c1e94
- 00499b60 ["COPY", "register:0:8", ["register:4048:8"]]
- 00499b60 ["INT_ADD", "register:40f0:8", ["const:499b60:8", "const:4:8"]]
- 00499b60 ["CALLIND", null, ["register:0:8"]]
+ 004bc9f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bc9f8 ["INT_ADD", "register:40f0:8", ["const:4bc9f8:8", "const:4:8"]]
+ 004bc9f8 ["CALLIND", null, ["register:0:8"]]
- 00499b60 bytes 20013fd6
+ 004bc9f8 bytes 20013fd6
- 00499ba0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00499ba0 ["INT_ADD", "register:40f0:8", ["const:499ba0:8", "const:4:8"]]
- 00499ba0 ["CALLIND", null, ["register:0:8"]]
+ 004bca38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bca38 ["INT_ADD", "register:40f0:8", ["const:4bca38:8", "const:4:8"]]
+ 004bca38 ["CALLIND", null, ["register:0:8"]]
- 00499ba0 bytes 00013fd6
+ 004bca38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13cbfb0f724c7d27c1eac6e66187fca6"></a>

### [`00499c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499c7c.md) → [`004bcb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcb14.md) _ZN5Botan8CBC_Mode9start_msgEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`005204e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005204e8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00543380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543380.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

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
      "definition_site": "004bcc04",
      "incomplete_value": true,
      "site": "004bcc10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499d6c",
      "incomplete_value": true,
      "site": "00499d78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
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
      "definition_site": "004bcc00",
      "incomplete_value": false,
      "site": "004bcc10",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "00499d68",
      "incomplete_value": false,
      "site": "00499d78",
      "value": [
        "leaf",
        "const:512990:8"
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
      "004bcc00",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004bcc04",
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ],
    [
      "004bcc04",
      "PARAM",
      [
        "storage",
        "00be94f0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bcc00",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bcc04",
      "READ",
      [
        "storage",
        "00c9aa40",
        null,
        "pointer"
      ]
    ],
    [
      "004bcc04",
      "PARAM",
      [
        "storage",
        "00c660b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00499d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499c7c.md#insn-00499d78) · [`00499cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499c7c.md#insn-00499cb4) · [`00499d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499c7c.md#insn-00499d1c)
- 新版 [`004bcc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcb14.md#insn-004bcc10) · [`004bcb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcb14.md#insn-004bcb4c) · [`004bcbb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcb14.md#insn-004bcbb4)

~~~diff
- 00499d78 ["INT_ADD", "register:40f0:8", ["const:499d78:8", "const:4:8"]]
- 00499d78 ["CALL", null, ["callee:00c57b10:8"]]
+ 004bcc10 ["INT_ADD", "register:40f0:8", ["const:4bcc10:8", "const:4:8"]]
+ 004bcc10 ["CALL", null, ["callee:00c57b10:8"]]
- 00499d78 bytes d2041d94
+ 004bcc10 bytes c06b1e94
- 00499cb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00499cb4 ["INT_ADD", "register:40f0:8", ["const:499cb4:8", "const:4:8"]]
- 00499cb4 ["CALLIND", null, ["register:0:8"]]
+ 004bcb4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bcb4c ["INT_ADD", "register:40f0:8", ["const:4bcb4c:8", "const:4:8"]]
+ 004bcb4c ["CALLIND", null, ["register:0:8"]]
- 00499cb4 bytes 00013fd6
+ 004bcb4c bytes 00013fd6
- 00499d1c ["INT_ADD", "register:40f0:8", ["const:499d1c:8", "const:4:8"]]
- 00499d1c ["CALL", null, ["callee:00c57af0:8"]]
+ 004bcbb4 ["INT_ADD", "register:40f0:8", ["const:4bcbb4:8", "const:4:8"]]
+ 004bcbb4 ["CALL", null, ["callee:00c57af0:8"]]
- 00499d1c bytes e1041d94
+ 004bcbb4 bytes cf6b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dde837d3ff9f189aa08c05498a73827"></a>

### [`00499dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499dd0.md) → [`004bcc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcc68.md) _ZNK5Botan14CBC_Encryption13output_lengthEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bcca8",
      "incomplete_value": false,
      "site": "004bccc8",
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
            "const:ff2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499e10",
      "incomplete_value": false,
      "site": "00499e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:8e2:8"
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
      "definition_site": "004bccb0",
      "incomplete_value": false,
      "site": "004bccc8",
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
            "const:57d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499e18",
      "incomplete_value": false,
      "site": "00499e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:50f:8"
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
      "definition_site": "004bccb8",
      "incomplete_value": false,
      "site": "004bccc8",
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
            "const:265:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499e20",
      "incomplete_value": false,
      "site": "00499e30",
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
            "const:6f6:8"
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
      "004bcca8",
      "PARAM",
      [
        "storage",
        "002928e2",
        null,
        "string"
      ]
    ],
    [
      "004bccb0",
      "PARAM",
      [
        "storage",
        "0029b50f",
        null,
        "string"
      ]
    ],
    [
      "004bccb8",
      "PARAM",
      [
        "storage",
        "002a76f6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bcca8",
      "PARAM",
      [
        "storage",
        "002a1ff2",
        null,
        "string"
      ]
    ],
    [
      "004bccb0",
      "PARAM",
      [
        "storage",
        "002ab57d",
        null,
        "string"
      ]
    ],
    [
      "004bccb8",
      "PARAM",
      [
        "storage",
        "002b8265",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00499e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499dd0.md#insn-00499e30) · [`00499e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499dd0.md#insn-00499e0c) · [`00499e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499dd0.md#insn-00499e10)
- 新版 [`004bccc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcc68.md#insn-004bccc8) · [`004bcca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcc68.md#insn-004bcca4) · [`004bcca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcc68.md#insn-004bcca8)

~~~diff
- 00499e30 ["INT_ADD", "register:40f0:8", ["const:499e30:8", "const:4:8"]]
- 00499e30 ["CALL", null, ["callee:00c58250:8"]]
+ 004bccc8 ["INT_ADD", "register:40f0:8", ["const:4bccc8:8", "const:4:8"]]
+ 004bccc8 ["CALL", null, ["callee:00c58250:8"]]
- 00499e30 bytes 74061d94
+ 004bccc8 bytes 626d1e94
- 00499e0c ["COPY", "register:4000:8", ["const:292000:8"]]
+ 004bcca4 ["COPY", "register:4000:8", ["const:2a1000:8"]]
- 00499e0c bytes c0efffb0
+ 004bcca4 bytes 20efffb0
- 00499e10 ["COPY", "tmp:0:8", ["const:8e2:8"]]
- 00499e10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00499e10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00499e10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004bcca8 ["COPY", "tmp:0:8", ["const:ff2:8"]]
+ 004bcca8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004bcca8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004bcca8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00499e10 bytes 00882391
+ 004bcca8 bytes 00c83f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2018d8d7edeecfdd42c9777035fd49c6"></a>

### [`00499e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499e34.md) → [`004bcccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcccc.md) _ZN5Botan14CBC_Encryption7processEPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00520980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520980.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00543818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543818.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.42% / 新版 97.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bcf14",
      "incomplete_value": false,
      "site": "004bcf34",
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
            "const:b53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a07c",
      "incomplete_value": false,
      "site": "0049a09c",
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
            "const:d95:8"
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
      "definition_site": "004bcf1c",
      "incomplete_value": false,
      "site": "004bcf34",
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
            "const:f66:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a084",
      "incomplete_value": false,
      "site": "0049a09c",
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
            "const:a24:8"
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
      "definition_site": "004bcf24",
      "incomplete_value": false,
      "site": "004bcf34",
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
            "const:53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a08c",
      "incomplete_value": false,
      "site": "0049a09c",
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
            "const:73d:8"
          ]
        ]
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
      "004bcf14",
      "PARAM",
      [
        "storage",
        "00298d95",
        null,
        "string"
      ]
    ],
    [
      "004bcf1c",
      "PARAM",
      [
        "storage",
        "00290a24",
        null,
        "string"
      ]
    ],
    [
      "004bcf24",
      "PARAM",
      [
        "storage",
        "0029473d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bcf14",
      "PARAM",
      [
        "storage",
        "002a8b53",
        null,
        "string"
      ]
    ],
    [
      "004bcf1c",
      "PARAM",
      [
        "storage",
        "0029ff66",
        null,
        "string"
      ]
    ],
    [
      "004bcf24",
      "PARAM",
      [
        "storage",
        "002a4053",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049a09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499e34.md#insn-0049a09c) · [`00499f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499e34.md#insn-00499f14) · [`00499f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499e34.md#insn-00499f30)
- 新版 [`004bcf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcccc.md#insn-004bcf34) · [`004bcdac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcccc.md#insn-004bcdac) · [`004bcdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcccc.md#insn-004bcdc8)

~~~diff
- 0049a09c ["INT_ADD", "register:40f0:8", ["const:49a09c:8", "const:4:8"]]
- 0049a09c ["CALL", null, ["callee:00c58250:8"]]
+ 004bcf34 ["INT_ADD", "register:40f0:8", ["const:4bcf34:8", "const:4:8"]]
+ 004bcf34 ["CALL", null, ["callee:00c58250:8"]]
- 0049a09c bytes d9051d94
+ 004bcf34 bytes c76c1e94
- 00499f14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00499f14 ["INT_ADD", "register:40f0:8", ["const:499f14:8", "const:4:8"]]
- 00499f14 ["CALLIND", null, ["register:0:8"]]
+ 004bcdac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bcdac ["INT_ADD", "register:40f0:8", ["const:4bcdac:8", "const:4:8"]]
+ 004bcdac ["CALLIND", null, ["register:0:8"]]
- 00499f14 bytes 00013fd6
+ 004bcdac bytes 00013fd6
- 00499f30 ["INT_ADD", "register:40f0:8", ["const:499f30:8", "const:4:8"]]
- 00499f30 ["CALL", null, ["callee:00543818:8"]]
+ 004bcdc8 ["INT_ADD", "register:40f0:8", ["const:4bcdc8:8", "const:4:8"]]
+ 004bcdc8 ["CALL", null, ["callee:00543818:8"]]
- 00499f30 bytes 941a0294
+ 004bcdc8 bytes 941a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f83fa8638b371e144f7bf8b4ace46bf4"></a>

### [`0049a0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a0a0.md) → [`004bcf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcf38.md) _ZN5Botan14CBC_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.34% / 新版 90.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bd05c",
      "incomplete_value": false,
      "site": "004bd07c",
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
            "const:725:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a1c4",
      "incomplete_value": false,
      "site": "0049a1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:49b:8"
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
      "definition_site": "004bd064",
      "incomplete_value": false,
      "site": "004bd07c",
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
            "const:cdd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a1cc",
      "incomplete_value": false,
      "site": "0049a1e4",
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
            "const:470:8"
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
      "definition_site": "004bd06c",
      "incomplete_value": false,
      "site": "004bd07c",
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
            "const:20d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a1d4",
      "incomplete_value": false,
      "site": "0049a1e4",
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
            "const:56a:8"
          ]
        ]
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
      "004bd05c",
      "PARAM",
      [
        "storage",
        "0029d49b",
        null,
        "string"
      ]
    ],
    [
      "004bd064",
      "PARAM",
      [
        "storage",
        "002a4470",
        null,
        "string"
      ]
    ],
    [
      "004bd06c",
      "PARAM",
      [
        "storage",
        "002a956a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd05c",
      "PARAM",
      [
        "storage",
        "002ad725",
        null,
        "string"
      ]
    ],
    [
      "004bd064",
      "PARAM",
      [
        "storage",
        "002b4cdd",
        null,
        "string"
      ]
    ],
    [
      "004bd06c",
      "PARAM",
      [
        "storage",
        "002ba20d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049a1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a0a0.md#insn-0049a1e4) · [`0049a21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a0a0.md#insn-0049a21c) · [`0049a250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a0a0.md#insn-0049a250)
- 新版 [`004bd07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcf38.md#insn-004bd07c) · [`004bd0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcf38.md#insn-004bd0b4) · [`004bd0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcf38.md#insn-004bd0e8)

~~~diff
- 0049a1e4 ["INT_ADD", "register:40f0:8", ["const:49a1e4:8", "const:4:8"]]
- 0049a1e4 ["CALL", null, ["callee:00c58250:8"]]
+ 004bd07c ["INT_ADD", "register:40f0:8", ["const:4bd07c:8", "const:4:8"]]
+ 004bd07c ["CALL", null, ["callee:00c58250:8"]]
- 0049a1e4 bytes 87051d94
+ 004bd07c bytes 756c1e94
- 0049a21c ["INT_ADD", "register:40f0:8", ["const:49a21c:8", "const:4:8"]]
- 0049a21c ["CALL", null, ["callee:00c58250:8"]]
+ 004bd0b4 ["INT_ADD", "register:40f0:8", ["const:4bd0b4:8", "const:4:8"]]
+ 004bd0b4 ["CALL", null, ["callee:00c58250:8"]]
- 0049a21c bytes 79051d94
+ 004bd0b4 bytes 676c1e94
- 0049a250 ["INT_ADD", "register:40f0:8", ["const:49a250:8", "const:4:8"]]
- 0049a250 ["CALL", null, ["callee:00c57b60:8"]]
+ 004bd0e8 ["INT_ADD", "register:40f0:8", ["const:4bd0e8:8", "const:4:8"]]
+ 004bd0e8 ["CALL", null, ["callee:00c57b60:8"]]
- 0049a250 bytes b0031d94
+ 004bd0e8 bytes 9e6a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41d91fec76bbfdb9a49d66b93f91ddd1"></a>

### [`0049a380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a380.md) → [`004bd218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd218.md) _ZN5Botan14CTS_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bd4d0",
      "incomplete_value": true,
      "site": "004bd4d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049a638",
      "incomplete_value": true,
      "site": "0049a638",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bd590",
      "incomplete_value": false,
      "site": "004bd5b0",
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
            "const:725:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a6f8",
      "incomplete_value": false,
      "site": "0049a718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:49b:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bd598",
      "incomplete_value": false,
      "site": "004bd5b0",
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
            "const:cdd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049a700",
      "incomplete_value": false,
      "site": "0049a718",
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
            "const:470:8"
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
      "004bd4c0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004bd590",
      "PARAM",
      [
        "storage",
        "0029d49b",
        null,
        "string"
      ]
    ],
    [
      "004bd598",
      "PARAM",
      [
        "storage",
        "002a4470",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd4c0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004bd590",
      "PARAM",
      [
        "storage",
        "002ad725",
        null,
        "string"
      ]
    ],
    [
      "004bd598",
      "PARAM",
      [
        "storage",
        "002b4cdd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a380.md#insn-0049a638) · [`0049a718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a380.md#insn-0049a718) · [`0049a740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a380.md#insn-0049a740)
- 新版 [`004bd4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd218.md#insn-004bd4d0) · [`004bd5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd218.md#insn-004bd5b0) · [`004bd5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd218.md#insn-004bd5d8)

~~~diff
- 0049a638 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049a638 ["INT_ADD", "register:40f0:8", ["const:49a638:8", "const:4:8"]]
- 0049a638 ["CALLIND", null, ["register:0:8"]]
+ 004bd4d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bd4d0 ["INT_ADD", "register:40f0:8", ["const:4bd4d0:8", "const:4:8"]]
+ 004bd4d0 ["CALLIND", null, ["register:0:8"]]
- 0049a638 bytes 20013fd6
+ 004bd4d0 bytes 20013fd6
- 0049a718 ["INT_ADD", "register:40f0:8", ["const:49a718:8", "const:4:8"]]
- 0049a718 ["CALL", null, ["callee:00c58250:8"]]
+ 004bd5b0 ["INT_ADD", "register:40f0:8", ["const:4bd5b0:8", "const:4:8"]]
+ 004bd5b0 ["CALL", null, ["callee:00c58250:8"]]
- 0049a718 bytes 3a041d94
+ 004bd5b0 bytes 286b1e94
- 0049a740 ["INT_ADD", "register:40f0:8", ["const:49a740:8", "const:4:8"]]
- 0049a740 ["CALL", null, ["callee:00c57b70:8"]]
+ 004bd5d8 ["INT_ADD", "register:40f0:8", ["const:4bd5d8:8", "const:4:8"]]
+ 004bd5d8 ["CALL", null, ["callee:00c57b70:8"]]
- 0049a740 bytes 78021d94
+ 004bd5d8 bytes 66691e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-829fb3e4f6eccadb6cf5466af1672d16"></a>

### [`0049a8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a8a4.md) → [`004bd73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd73c.md) _ZN5Botan14CBC_Decryption7processEPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.32% / 新版 97.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bd96c",
      "incomplete_value": false,
      "site": "004bd98c",
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
            "const:b53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049aad4",
      "incomplete_value": false,
      "site": "0049aaf4",
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
            "const:d95:8"
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
      "definition_site": "004bd974",
      "incomplete_value": false,
      "site": "004bd98c",
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
            "const:ae7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049aadc",
      "incomplete_value": false,
      "site": "0049aaf4",
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
            "const:52d:8"
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
      "definition_site": "004bd97c",
      "incomplete_value": false,
      "site": "004bd98c",
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
            "const:53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049aae4",
      "incomplete_value": false,
      "site": "0049aaf4",
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
            "const:73d:8"
          ]
        ]
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
      "004bd96c",
      "PARAM",
      [
        "storage",
        "00298d95",
        null,
        "string"
      ]
    ],
    [
      "004bd974",
      "PARAM",
      [
        "storage",
        "002a052d",
        null,
        "string"
      ]
    ],
    [
      "004bd97c",
      "PARAM",
      [
        "storage",
        "0029473d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd96c",
      "PARAM",
      [
        "storage",
        "002a8b53",
        null,
        "string"
      ]
    ],
    [
      "004bd974",
      "PARAM",
      [
        "storage",
        "002b0ae7",
        null,
        "string"
      ]
    ],
    [
      "004bd97c",
      "PARAM",
      [
        "storage",
        "002a4053",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049aaf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a8a4.md#insn-0049aaf4) · [`0049a93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a8a4.md#insn-0049a93c) · [`0049aa44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049a8a4.md#insn-0049aa44)
- 新版 [`004bd98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd73c.md#insn-004bd98c) · [`004bd7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd73c.md#insn-004bd7d4) · [`004bd8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd73c.md#insn-004bd8dc)

~~~diff
- 0049aaf4 ["INT_ADD", "register:40f0:8", ["const:49aaf4:8", "const:4:8"]]
- 0049aaf4 ["CALL", null, ["callee:00c58250:8"]]
+ 004bd98c ["INT_ADD", "register:40f0:8", ["const:4bd98c:8", "const:4:8"]]
+ 004bd98c ["CALL", null, ["callee:00c58250:8"]]
- 0049aaf4 bytes 43031d94
+ 004bd98c bytes 316a1e94
- 0049a93c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049a93c ["INT_ADD", "register:40f0:8", ["const:49a93c:8", "const:4:8"]]
- 0049a93c ["CALLIND", null, ["register:0:8"]]
+ 004bd7d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bd7d4 ["INT_ADD", "register:40f0:8", ["const:4bd7d4:8", "const:4:8"]]
+ 004bd7d4 ["CALLIND", null, ["register:0:8"]]
- 0049a93c bytes 00013fd6
+ 004bd7d4 bytes 00013fd6
- 0049aa44 ["INT_ADD", "register:40f0:8", ["const:49aa44:8", "const:4:8"]]
- 0049aa44 ["CALL", null, ["callee:00c57b40:8"]]
+ 004bd8dc ["INT_ADD", "register:40f0:8", ["const:4bd8dc:8", "const:4:8"]]
+ 004bd8dc ["CALL", null, ["callee:00c57b40:8"]]
- 0049aa44 bytes ab011d94
+ 004bd8dc bytes 99681e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00c10a2a12d777fe108d6d9d415af339"></a>

### [`0049aaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049aaf8.md) → [`004bd990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd990.md) _ZN5Botan14CBC_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.30% / 新版 94.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bdb60",
      "incomplete_value": false,
      "site": "004bdb68",
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
            "const:13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049acc8",
      "incomplete_value": false,
      "site": "0049acd0",
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
            "const:9ef:8"
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
      "definition_site": "004bdbb0",
      "incomplete_value": true,
      "site": "004bdbbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049ad18",
      "incomplete_value": true,
      "site": "0049ad24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bdbac",
      "incomplete_value": false,
      "site": "004bdbbc",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0049ad14",
      "incomplete_value": false,
      "site": "0049ad24",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 10,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004bdb60",
      "PARAM",
      [
        "storage",
        "002af9ef",
        null,
        "string"
      ]
    ],
    [
      "004bdbac",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004bdbb0",
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
      "004bdb60",
      "PARAM",
      [
        "storage",
        "002c1013",
        null,
        "string"
      ]
    ],
    [
      "004bdbac",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bdbb0",
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

- 旧版 [`0049acd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049aaf8.md#insn-0049acd0) · [`0049ad24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049aaf8.md#insn-0049ad24) · [`0049ad60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049aaf8.md#insn-0049ad60)
- 新版 [`004bdb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd990.md#insn-004bdb68) · [`004bdbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd990.md#insn-004bdbbc) · [`004bdbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd990.md#insn-004bdbf8)

~~~diff
- 0049acd0 ["INT_ADD", "register:40f0:8", ["const:49acd0:8", "const:4:8"]]
- 0049acd0 ["CALL", null, ["callee:00c57b70:8"]]
+ 004bdb68 ["INT_ADD", "register:40f0:8", ["const:4bdb68:8", "const:4:8"]]
+ 004bdb68 ["CALL", null, ["callee:00c57b70:8"]]
- 0049acd0 bytes 14011d94
+ 004bdb68 bytes 02681e94
- 0049ad24 ["INT_ADD", "register:40f0:8", ["const:49ad24:8", "const:4:8"]]
- 0049ad24 ["CALL", null, ["callee:00c57b10:8"]]
+ 004bdbbc ["INT_ADD", "register:40f0:8", ["const:4bdbbc:8", "const:4:8"]]
+ 004bdbbc ["CALL", null, ["callee:00c57b10:8"]]
- 0049ad24 bytes e7001d94
+ 004bdbbc bytes d5671e94
- 0049ad60 ["INT_ADD", "register:40f0:8", ["const:49ad60:8", "const:4:8"]]
- 0049ad60 ["CALL", null, ["callee:00c58250:8"]]
+ 004bdbf8 ["INT_ADD", "register:40f0:8", ["const:4bdbf8:8", "const:4:8"]]
+ 004bdbf8 ["CALL", null, ["callee:00c58250:8"]]
- 0049ad60 bytes a8021d94
+ 004bdbf8 bytes 96691e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

