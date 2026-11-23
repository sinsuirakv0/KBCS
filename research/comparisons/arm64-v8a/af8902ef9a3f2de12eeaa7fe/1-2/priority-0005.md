# v15.7.4 → v16.0.0 · 最優先の変更候補 (5)

[一覧の目次](README.md)

<a id="compare-21adbbcaa0eff184144b7f2373394d2b"></a>

### [`00454f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454f34.md) → [`00477dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md) FUN_00477dcc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004532cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004532cc.md) · 呼出先 10件 [`00428a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428a44.md) [`00455db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455db8.md) [`00455dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455dbc.md) [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00476164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476164.md) · 呼出先 10件 [`0044b544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b544.md) [`00478c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c50.md) [`00478c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c54.md) [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00477ed0",
      "incomplete_value": false,
      "site": "00477ed0",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455038",
      "incomplete_value": false,
      "site": "00455038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00477e08",
      "incomplete_value": false,
      "site": "00477e10",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454f70",
      "incomplete_value": false,
      "site": "00454f78",
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
            "const:823:8"
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
      "definition_site": "00477e8c",
      "incomplete_value": true,
      "site": "00477e94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454ff4",
      "incomplete_value": true,
      "site": "00454ffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00477e08",
      "PARAM",
      [
        "storage",
        "00296823",
        null,
        "string"
      ]
    ],
    [
      "00477e8c",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "00477e8c",
      "PARAM",
      [
        "storage",
        "00c25e28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00477e08",
      "PARAM",
      [
        "storage",
        "002a6358",
        null,
        "string"
      ]
    ],
    [
      "00477e8c",
      "READ",
      [
        "storage",
        "00c9a808",
        null,
        "pointer"
      ]
    ],
    [
      "00477e8c",
      "PARAM",
      [
        "storage",
        "00ca58e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00454f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454f34.md#insn-00454f78) · [`00454ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454f34.md#insn-00454ffc) · [`00454f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454f34.md#insn-00454f68)
- 新版 [`00477e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md#insn-00477e10) · [`00477e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md#insn-00477e94) · [`00477e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md#insn-00477e00)

~~~diff
- 00454f78 ["INT_ADD", "register:40f0:8", ["const:454f78:8", "const:4:8"]]
- 00454f78 ["CALL", null, ["callee:00c57b70:8"]]
+ 00477e10 ["INT_ADD", "register:40f0:8", ["const:477e10:8", "const:4:8"]]
+ 00477e10 ["CALL", null, ["callee:00c57b70:8"]]
- 00454f78 bytes 6a181e94
+ 00477e10 bytes 587f1f94
- 00454ffc ["INT_ADD", "register:40f0:8", ["const:454ffc:8", "const:4:8"]]
- 00454ffc ["CALL", null, ["callee:00561cf4:8"]]
+ 00477e94 ["INT_ADD", "register:40f0:8", ["const:477e94:8", "const:4:8"]]
+ 00477e94 ["CALL", null, ["callee:00561cf4:8"]]
- 00454ffc bytes 98a70394
+ 00477e94 bytes 98a70394
- 00454f68 ["INT_ADD", "register:40f0:8", ["const:454f68:8", "const:4:8"]]
- 00454f68 ["CALL", null, ["callee:0044b544:8"]]
+ 00477e00 ["INT_ADD", "register:40f0:8", ["const:477e00:8", "const:4:8"]]
+ 00477e00 ["CALL", null, ["callee:0044b544:8"]]
- 00454f68 bytes b74eff97
+ 00477e00 bytes d14dff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d204dae5d2fc01311935491758e3549"></a>

### [`00455270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455270.md) → [`00478108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md) FUN_00478108

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004537f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md) [`00454af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454af4.md) · 呼出先 8件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 2件 [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0047798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/0047798c.md) · 呼出先 8件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

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
      "site": "00478164",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004552cc",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "site": "004781fc",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00455364",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "00478164",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ],
    [
      "004781fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "00478164",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ],
    [
      "004781fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004552cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455270.md#insn-004552cc) · [`00455364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455270.md#insn-00455364) · [`004552ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455270.md#insn-004552ac)
- 新版 [`00478164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md#insn-00478164) · [`004781fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md#insn-004781fc) · [`00478144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md#insn-00478144)

~~~diff
- 004552cc ["INT_ADD", "register:40f0:8", ["const:4552cc:8", "const:4:8"]]
- 004552cc ["CALL", null, ["ram:bdb4a0:8"]]
+ 00478164 ["INT_ADD", "register:40f0:8", ["const:478164:8", "const:4:8"]]
+ 00478164 ["CALL", null, ["ram:c57ef0:8"]]
- 004552cc bytes 75181e94
+ 00478164 bytes 637f1f94
- 00455364 ["INT_ADD", "register:40f0:8", ["const:455364:8", "const:4:8"]]
- 00455364 ["CALL", null, ["ram:bdb4a0:8"]]
+ 004781fc ["INT_ADD", "register:40f0:8", ["const:4781fc:8", "const:4:8"]]
+ 004781fc ["CALL", null, ["ram:c57ef0:8"]]
- 00455364 bytes 4f181e94
+ 004781fc bytes 3d7f1f94
- 004552ac ["INT_ADD", "register:40f0:8", ["const:4552ac:8", "const:4:8"]]
- 004552ac ["CALL", null, ["callee:00c57ce0:8"]]
+ 00478144 ["INT_ADD", "register:40f0:8", ["const:478144:8", "const:4:8"]]
+ 00478144 ["CALL", null, ["callee:00c57ce0:8"]]
- 004552ac bytes f9171e94
+ 00478144 bytes e77e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0bd21e4712efdbdea4a945a40ec596d"></a>

### [`0045543c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/0045543c.md) → [`004782d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md) FUN_004782d4

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00453c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md) [`00469fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fe0.md) · 呼出先 13件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md)
- 新版 呼出元 2件 [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) [`0048ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce78.md) · 呼出先 13件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)

変更の種類 call, call_argument_candidate, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.82% / 新版 87.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 2件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00478344",
      "incomplete_value": true,
      "site": "00478348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004554ac",
      "incomplete_value": true,
      "site": "004554b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00478340",
      "incomplete_value": true,
      "site": "00478350",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004554a8",
      "incomplete_value": true,
      "site": "004554b8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00478358",
      "incomplete_value": true,
      "site": "00478358",
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
      "definition_site": "004554c0",
      "incomplete_value": true,
      "site": "004554c0",
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
      "00478328",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "0047832c",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00478340",
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
      "00478328",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "0047832c",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00478340",
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

- 旧版 [`00455550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/0045543c.md#insn-00455550) · [`00455568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/0045543c.md#insn-00455568) · [`00455484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/0045543c.md#insn-00455484)
- 新版 [`004783e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md#insn-004783e8) · [`00478400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md#insn-00478400) · [`0047831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/004782d4.md#insn-0047831c)

~~~diff
- 00455550 ["INT_ADD", "register:40f0:8", ["const:455550:8", "const:4:8"]]
- 00455550 ["CALL", null, ["callee:00c57e80:8"]]
+ 004783e8 ["INT_ADD", "register:40f0:8", ["const:4783e8:8", "const:4:8"]]
+ 004783e8 ["CALL", null, ["callee:00c57e80:8"]]
- 00455550 bytes b8171e94
+ 004783e8 bytes a67e1f94
- 00455568 ["INT_ADD", "register:40f0:8", ["const:455568:8", "const:4:8"]]
- 00455568 ["CALL", null, ["ram:bdb440:8"]]
+ 00478400 ["INT_ADD", "register:40f0:8", ["const:478400:8", "const:4:8"]]
+ 00478400 ["CALL", null, ["ram:c57e90:8"]]
- 00455568 bytes b6171e94
+ 00478400 bytes a47e1f94
- 00455484 ["COPY", "register:40d0:8", ["const:c1a000:8"]]
+ 0047831c ["COPY", "register:40d0:8", ["const:c9a000:8"]]
- 00455484 bytes 3a3e00b0
+ 0047831c bytes 1a4100d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c421bdf83416fb31b3e10729d6458a9c"></a>

### [`004557b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/004557b8.md) → [`00478650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478650.md) FUN_00478650

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00453c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md) [`00469fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fe0.md) · 呼出先 6件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00455cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 2件 [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) [`0048ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce78.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00478b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b50.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, store_destination, store_value

命令の説明率　旧版 85.62% / 新版 85.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 7件, `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_condition` 7件, `store_destination` 10件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0047869c",
      "incomplete_value": true,
      "site": "0047869c",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455804",
      "incomplete_value": true,
      "site": "00455804",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00478740",
      "incomplete_value": true,
      "site": "00478740",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004558a8",
      "incomplete_value": true,
      "site": "004558a8",
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
            "const:f30:8"
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
      "definition_site": "004787e4",
      "incomplete_value": true,
      "site": "004787e4",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045594c",
      "incomplete_value": true,
      "site": "0045594c",
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
            "const:f30:8"
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
      "0047866c",
      "READ",
      [
        "storage",
        "00c24f48",
        null,
        "undefined1"
      ]
    ],
    [
      "00478678",
      "READ",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00478690",
      "READ",
      [
        "storage",
        "00c24f38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0047866c",
      "READ",
      [
        "storage",
        "00ca4a08",
        null,
        "undefined1"
      ]
    ],
    [
      "00478678",
      "READ",
      [
        "storage",
        "00ca4a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00478690",
      "READ",
      [
        "storage",
        "00ca49f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00455804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/004557b8.md#insn-00455804) · [`004558a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/004557b8.md#insn-004558a8) · [`0045594c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/004557b8.md#insn-0045594c)
- 新版 [`0047869c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478650.md#insn-0047869c) · [`00478740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478650.md#insn-00478740) · [`004787e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478650.md#insn-004787e4)

~~~diff
- 00455804 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f30:8"]]
- 00455804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0047869c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 0047869c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00455804 bytes 689a07f9
+ 0047869c bytes 68fa04f9
- 004558a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f30:8"]]
- 004558a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00478740 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00478740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 004558a8 bytes 689a07f9
+ 00478740 bytes 68fa04f9
- 0045594c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f30:8"]]
- 0045594c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 004787e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 004787e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0045594c bytes 689a07f9
+ 004787e4 bytes 68fa04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5518a9503df40e9cc92c48e2029bde3"></a>

### [`00455cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455cc0.md) → [`00478b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b58.md) FUN_00478b58

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 67.74% / 新版 67.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00478b7c",
      "incomplete_value": true,
      "site": "00478b84",
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
      "definition_site": "00455ce4",
      "incomplete_value": true,
      "site": "00455cec",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00478b90",
      "incomplete_value": true,
      "site": "00478b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "definition_site": "00455cf8",
      "incomplete_value": true,
      "site": "00455cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00478b90",
      "incomplete_value": true,
      "site": "00478b90",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455cf8",
      "incomplete_value": true,
      "site": "00455cf8",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
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
      "00478b74",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00478b7c",
      "READ",
      [
        "storage",
        "00c13458",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00478b80",
      "READ",
      [
        "storage",
        "00c13470",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "00478b74",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00478b7c",
      "READ",
      [
        "storage",
        "00c92e00",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00478b80",
      "READ",
      [
        "storage",
        "00c92e18",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00455cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455cc0.md#insn-00455cd0) · [`00455cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455cc0.md#insn-00455cd4) · [`00455cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455cc0.md#insn-00455cdc)
- 新版 [`00478b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b58.md#insn-00478b68) · [`00478b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b58.md#insn-00478b6c) · [`00478b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478b58.md#insn-00478b74)

~~~diff
- 00455cd0 ["COPY", "register:40a8:8", ["const:c1a000:8"]]
+ 00478b68 ["COPY", "register:40a8:8", ["const:c9a000:8"]]
- 00455cd0 bytes 353e00b0
+ 00478b68 bytes 154100d0
- 00455cd4 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 00478b6c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00455cd4 bytes 293e00b0
+ 00478b6c bytes 094100d0
- 00455cdc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
- 00455cdc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00478b74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7b8:8"]]
+ 00478b74 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00455cdc bytes b5e646f9
+ 00478b74 bytes b5de43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca653df500376ef4d8a6fe30d26140cb"></a>

### [`00455d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455d84.md) → [`00478c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c1c.md) FUN_00478c1c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00478c30",
      "incomplete_value": false,
      "site": "00478c34",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455d98",
      "incomplete_value": false,
      "site": "00455d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "00478c34",
      "DATA",
      [
        "storage",
        "00be7f20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00478c34",
      "DATA",
      [
        "storage",
        "00c64ae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00455d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455d84.md#insn-00455d90) · [`00455d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455d84.md#insn-00455d94) · [`00455d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455d84.md#insn-00455d98)
- 新版 [`00478c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c1c.md#insn-00478c28) · [`00478c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c1c.md#insn-00478c2c) · [`00478c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c1c.md#insn-00478c30)

~~~diff
- 00455d90 ["INT_ADD", "register:40f0:8", ["const:455d90:8", "const:4:8"]]
- 00455d90 ["CALL", null, ["callee:00c57a90:8"]]
+ 00478c28 ["INT_ADD", "register:40f0:8", ["const:478c28:8", "const:4:8"]]
+ 00478c28 ["CALL", null, ["callee:00c57a90:8"]]
- 00455d90 bytes ac141e94
+ 00478c28 bytes 9a7b1f94
- 00455d94 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00478c2c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00455d94 bytes 883c00d0
+ 00478c2c bytes 683f0090
- 00455d98 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00455d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00455d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00455d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00478c30 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 00478c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00478c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00478c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00455d98 bytes 08813c91
+ 00478c30 bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8829fbe997814173135528c679b382d1"></a>

### [`00455da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455da8.md) → [`00478c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c40.md) FUN_00478c40

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00478c44",
      "incomplete_value": false,
      "site": "00478c48",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455dac",
      "incomplete_value": false,
      "site": "00455db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "00478c48",
      "DATA",
      [
        "storage",
        "00be7f20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00478c48",
      "DATA",
      [
        "storage",
        "00c64ae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00455da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455da8.md#insn-00455da8) · [`00455dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455da8.md#insn-00455dac)
- 新版 [`00478c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c40.md#insn-00478c40) · [`00478c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478c40.md#insn-00478c44)

~~~diff
- 00455da8 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00478c40 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00455da8 bytes 883c00d0
+ 00478c40 bytes 683f0090
- 00455dac ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00455dac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00455dac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00455dac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00478c44 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 00478c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00478c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00478c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00455dac bytes 08813c91
+ 00478c44 bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a081ccc6d703e40ace1986ef985bdff"></a>

### [`0045683c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/0045683c.md) → [`004796d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004796d4.md) FUN_004796d4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004796f8",
      "incomplete_value": false,
      "site": "004796f8",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456860",
      "incomplete_value": false,
      "site": "00456860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
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
      "004796f8",
      "DATA",
      [
        "storage",
        "00be7fa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004796f8",
      "DATA",
      [
        "storage",
        "00c64b60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/0045683c.md#insn-00456850) · [`00456858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/0045683c.md#insn-00456858) · [`0045685c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/0045683c.md#insn-0045685c)
- 新版 [`004796e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004796d4.md#insn-004796e8) · [`004796f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004796d4.md#insn-004796f0) · [`004796f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004796d4.md#insn-004796f4)

~~~diff
- 00456850 ["INT_ADD", "register:40f0:8", ["const:456850:8", "const:4:8"]]
- 00456850 ["CALL", null, ["callee:00c57a90:8"]]
+ 004796e8 ["INT_ADD", "register:40f0:8", ["const:4796e8:8", "const:4:8"]]
+ 004796e8 ["CALL", null, ["callee:00c57a90:8"]]
- 00456850 bytes fc111e94
+ 004796e8 bytes ea781f94
- 00456858 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004796f0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00456858 bytes 883c00b0
+ 004796f0 bytes 483f00f0
- 0045685c ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 0045685c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045685c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045685c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004796f4 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 004796f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004796f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004796f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045685c bytes 08813e91
+ 004796f4 bytes 08812d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-280a12a8ba1755e77ca16a4cbeeca8d4"></a>

### [`00456870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456870.md) → [`00479708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479708.md) FUN_00479708

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00479714",
      "incomplete_value": false,
      "site": "00479714",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045687c",
      "incomplete_value": false,
      "site": "0045687c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
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
      "00479714",
      "DATA",
      [
        "storage",
        "00be7fa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479714",
      "DATA",
      [
        "storage",
        "00c64b60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456870.md#insn-00456874) · [`00456878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456870.md#insn-00456878)
- 新版 [`0047970c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479708.md#insn-0047970c) · [`00479710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479708.md#insn-00479710)

~~~diff
- 00456874 ["COPY", "register:4048:8", ["const:be7000:8"]]
+ 0047970c ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00456874 bytes 893c00b0
+ 0047970c bytes 493f00f0
- 00456878 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 00456878 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00456878 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00456878 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479710 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 00479710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00456878 bytes 29813e91
+ 00479710 bytes 29812d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4539f7f73fc0961d5fb2c006673e826c"></a>

### [`004568f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004568f4.md) → [`0047978c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047978c.md) FUN_0047978c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004797b0",
      "incomplete_value": false,
      "site": "004797b0",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456918",
      "incomplete_value": false,
      "site": "00456918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:30:8"
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
      "004797b0",
      "DATA",
      [
        "storage",
        "00be8030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004797b0",
      "DATA",
      [
        "storage",
        "00c64bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004568f4.md#insn-00456908) · [`00456910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004568f4.md#insn-00456910) · [`00456914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004568f4.md#insn-00456914)
- 新版 [`004797a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047978c.md#insn-004797a0) · [`004797a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047978c.md#insn-004797a8) · [`004797ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047978c.md#insn-004797ac)

~~~diff
- 00456908 ["INT_ADD", "register:40f0:8", ["const:456908:8", "const:4:8"]]
- 00456908 ["CALL", null, ["callee:00c57a90:8"]]
+ 004797a0 ["INT_ADD", "register:40f0:8", ["const:4797a0:8", "const:4:8"]]
+ 004797a0 ["CALL", null, ["callee:00c57a90:8"]]
- 00456908 bytes ce111e94
+ 004797a0 bytes bc781f94
- 00456910 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 004797a8 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00456910 bytes 883c00d0
+ 004797a8 bytes 483f00f0
- 00456914 ["COPY", "tmp:0:8", ["const:30:8"]]
- 00456914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00456914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00456914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004797ac ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 004797ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004797ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004797ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00456914 bytes 08c10091
+ 004797ac bytes 08c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-919ac723b91411fc02f9af32400e75cd"></a>

### [`00456928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456928.md) → [`004797c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004797c0.md) FUN_004797c0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004797cc",
      "incomplete_value": false,
      "site": "004797cc",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456934",
      "incomplete_value": false,
      "site": "00456934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:30:8"
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
      "004797cc",
      "DATA",
      [
        "storage",
        "00be8030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004797cc",
      "DATA",
      [
        "storage",
        "00c64bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045692c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456928.md#insn-0045692c) · [`00456930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456928.md#insn-00456930)
- 新版 [`004797c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004797c0.md#insn-004797c4) · [`004797c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004797c0.md#insn-004797c8)

~~~diff
- 0045692c ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 004797c4 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045692c bytes 893c00d0
+ 004797c4 bytes 493f00f0
- 00456930 ["COPY", "tmp:0:8", ["const:30:8"]]
- 00456930 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00456930 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00456930 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004797c8 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 004797c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004797c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004797c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00456930 bytes 29c10091
+ 004797c8 bytes 29c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-562f905335940221a41f74eb8a78b3aa"></a>

### [`004569a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004569a4.md) → [`0047983c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047983c.md) FUN_0047983c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00479854",
      "incomplete_value": false,
      "site": "00479858",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004569bc",
      "incomplete_value": false,
      "site": "004569c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "00479858",
      "DATA",
      [
        "storage",
        "00be80b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479858",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004569b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004569a4.md#insn-004569b8) · [`004569bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004569a4.md#insn-004569bc) · [`004569cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/004569a4.md#insn-004569cc)
- 新版 [`00479850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047983c.md#insn-00479850) · [`00479854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047983c.md#insn-00479854) · [`00479864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/0047983c.md#insn-00479864)

~~~diff
- 004569b8 ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 00479850 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 004569b8 bytes 893c00d0
+ 00479850 bytes 493f00f0
- 004569bc ["COPY", "tmp:0:8", ["const:b0:8"]]
- 004569bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004569bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004569bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479854 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00479854 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479854 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479854 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004569bc bytes 29c10291
+ 00479854 bytes 29c13191
- 004569cc ["INT_ADD", "register:40f0:8", ["const:4569cc:8", "const:4:8"]]
- 004569cc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00479864 ["INT_ADD", "register:40f0:8", ["const:479864:8", "const:4:8"]]
+ 00479864 ["CALL", null, ["callee:00c57ab0:8"]]
- 004569cc bytes a5111e94
+ 00479864 bytes 93781f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccfa6aaf6ff5428d5db946798d072253"></a>

### [`00456a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456a14.md) → [`004798ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004798ac.md) FUN_004798ac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004798c4",
      "incomplete_value": false,
      "site": "004798c8",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456a2c",
      "incomplete_value": false,
      "site": "00456a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "004798c8",
      "DATA",
      [
        "storage",
        "00be80b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004798c8",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456a14.md#insn-00456a28) · [`00456a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456a14.md#insn-00456a2c) · [`00456a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456a14.md#insn-00456a3c)
- 新版 [`004798c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004798ac.md#insn-004798c0) · [`004798c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004798ac.md#insn-004798c4) · [`004798d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004798ac.md#insn-004798d4)

~~~diff
- 00456a28 ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 004798c0 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00456a28 bytes 893c00d0
+ 004798c0 bytes 493f00f0
- 00456a2c ["COPY", "tmp:0:8", ["const:b0:8"]]
- 00456a2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00456a2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00456a2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004798c4 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 004798c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004798c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004798c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00456a2c bytes 29c10291
+ 004798c4 bytes 29c13191
- 00456a3c ["INT_ADD", "register:40f0:8", ["const:456a3c:8", "const:4:8"]]
- 00456a3c ["CALL", null, ["callee:00c57ab0:8"]]
+ 004798d4 ["INT_ADD", "register:40f0:8", ["const:4798d4:8", "const:4:8"]]
+ 004798d4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00456a3c bytes 89111e94
+ 004798d4 bytes 77781f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd42e294d9f18143661f3a74629c7ab7"></a>

### [`00456a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456a80.md) → [`00479918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479918.md) FUN_00479918

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479940",
      "incomplete_value": false,
      "site": "00479944",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456aa8",
      "incomplete_value": false,
      "site": "00456aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "00479944",
      "DATA",
      [
        "storage",
        "00be80b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479944",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456a80.md#insn-00456a94) · [`00456aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456a80.md#insn-00456aa4) · [`00456aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456a80.md#insn-00456aa8)
- 新版 [`0047992c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479918.md#insn-0047992c) · [`0047993c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479918.md#insn-0047993c) · [`00479940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479918.md#insn-00479940)

~~~diff
- 00456a94 ["INT_ADD", "register:40f0:8", ["const:456a94:8", "const:4:8"]]
- 00456a94 ["CALL", null, ["callee:00c57a90:8"]]
+ 0047992c ["INT_ADD", "register:40f0:8", ["const:47992c:8", "const:4:8"]]
+ 0047992c ["CALL", null, ["callee:00c57a90:8"]]
- 00456a94 bytes 6b111e94
+ 0047992c bytes 59781f94
- 00456aa4 ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 0047993c ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00456aa4 bytes 893c00d0
+ 0047993c bytes 493f00f0
- 00456aa8 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 00456aa8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00456aa8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00456aa8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479940 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00479940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00456aa8 bytes 29c10291
+ 00479940 bytes 29c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2cf0ab19c490c6e3623e28de85343bf"></a>

### [`00456b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456b20.md) → [`004799b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004799b8.md) FUN_004799b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "004799d4",
      "incomplete_value": false,
      "site": "004799e0",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456b3c",
      "incomplete_value": false,
      "site": "00456b48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "004799e0",
      "DATA",
      [
        "storage",
        "00be80b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004799e0",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456b20.md#insn-00456b38) · [`00456b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456b20.md#insn-00456b3c) · [`00456b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456b20.md#insn-00456b5c)
- 新版 [`004799d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004799b8.md#insn-004799d0) · [`004799d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004799b8.md#insn-004799d4) · [`004799f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/004799b8.md#insn-004799f4)

~~~diff
- 00456b38 ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 004799d0 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00456b38 bytes 893c00d0
+ 004799d0 bytes 493f00f0
- 00456b3c ["COPY", "tmp:0:8", ["const:b0:8"]]
- 00456b3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00456b3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00456b3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004799d4 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 004799d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004799d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004799d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00456b3c bytes 29c10291
+ 004799d4 bytes 29c13191
- 00456b5c ["INT_ADD", "register:40f0:8", ["const:456b5c:8", "const:4:8"]]
- 00456b5c ["CALL", null, ["callee:00c538b0:8"]]
+ 004799f4 ["INT_ADD", "register:40f0:8", ["const:4799f4:8", "const:4:8"]]
+ 004799f4 ["CALL", null, ["callee:00c538b0:8"]]
- 00456b5c bytes c1001e94
+ 004799f4 bytes af671f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bf9e834ababc46bc2a2e181c8436054"></a>

### [`00456c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456c70.md) → [`00479b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479b08.md) FUN_00479b08

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00456ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456ed0.md) [`0052dab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dab8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00479d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d68.md) [`00550950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550950.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.26% / 新版 93.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479ba0",
      "incomplete_value": false,
      "site": "00479ba8",
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
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456d08",
      "incomplete_value": false,
      "site": "00456d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:120:8"
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
      "definition_site": "00479bb8",
      "incomplete_value": false,
      "site": "00479bb8",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456d20",
      "incomplete_value": false,
      "site": "00456d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "site": "00479b74",
      "value": [
        "leaf",
        "ram:550950:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00456cdc",
      "value": [
        "leaf",
        "ram:52dab8:8"
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
      "00479b74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0052dab8"
      ]
    ],
    [
      "00479ba8",
      "DATA",
      [
        "storage",
        "00be8120",
        null,
        "pointer"
      ]
    ],
    [
      "00479bb8",
      "DATA",
      [
        "storage",
        "00be8170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479b74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00550950"
      ]
    ],
    [
      "00479ba8",
      "DATA",
      [
        "storage",
        "00c64ce0",
        null,
        "pointer"
      ]
    ],
    [
      "00479bb8",
      "DATA",
      [
        "storage",
        "00c64d30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456c70.md#insn-00456cdc) · [`00456cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456c70.md#insn-00456cb0) · [`00456ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456c70.md#insn-00456ccc)
- 新版 [`00479b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479b08.md#insn-00479b74) · [`00479b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479b08.md#insn-00479b48) · [`00479b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479b08.md#insn-00479b64)

~~~diff
- 00456cdc ["INT_ADD", "register:40f0:8", ["const:456cdc:8", "const:4:8"]]
- 00456cdc ["CALL", null, ["ram:52dab8:8"]]
+ 00479b74 ["INT_ADD", "register:40f0:8", ["const:479b74:8", "const:4:8"]]
+ 00479b74 ["CALL", null, ["ram:550950:8"]]
- 00456cdc bytes 775b0394
+ 00479b74 bytes 775b0394
- 00456cb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00456cb0 ["INT_ADD", "register:40f0:8", ["const:456cb0:8", "const:4:8"]]
- 00456cb0 ["CALLIND", null, ["register:0:8"]]
+ 00479b48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479b48 ["INT_ADD", "register:40f0:8", ["const:479b48:8", "const:4:8"]]
+ 00479b48 ["CALLIND", null, ["register:0:8"]]
- 00456cb0 bytes 00013fd6
+ 00479b48 bytes 00013fd6
- 00456ccc ["COPY", "register:0:8", ["register:4048:8"]]
- 00456ccc ["INT_ADD", "register:40f0:8", ["const:456ccc:8", "const:4:8"]]
- 00456ccc ["CALLIND", null, ["register:0:8"]]
+ 00479b64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00479b64 ["INT_ADD", "register:40f0:8", ["const:479b64:8", "const:4:8"]]
+ 00479b64 ["CALLIND", null, ["register:0:8"]]
- 00456ccc bytes 20013fd6
+ 00479b64 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c4e87a9f2303f03301f50c280a3adc6"></a>

### [`00456f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456f28.md) → [`00479dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479dc0.md) FUN_00479dc0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "00479dd4",
      "incomplete_value": false,
      "site": "00479dd8",
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
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456f3c",
      "incomplete_value": false,
      "site": "00456f40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "00479dd8",
      "DATA",
      [
        "storage",
        "00be8208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479dd8",
      "DATA",
      [
        "storage",
        "00c64dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456f28.md#insn-00456f38) · [`00456f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456f28.md#insn-00456f3c) · [`00456f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456f28.md#insn-00456f50)
- 新版 [`00479dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479dc0.md#insn-00479dd0) · [`00479dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479dc0.md#insn-00479dd4) · [`00479de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479dc0.md#insn-00479de8)

~~~diff
- 00456f38 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00479dd0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00456f38 bytes 883c00d0
+ 00479dd0 bytes 483f00f0
- 00456f3c ["COPY", "tmp:0:8", ["const:208:8"]]
- 00456f3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00456f3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00456f3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479dd4 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00479dd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479dd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479dd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00456f3c bytes 08210891
+ 00479dd4 bytes 08213791
- 00456f50 ["INT_ADD", "register:40f0:8", ["const:456f50:8", "const:4:8"]]
- 00456f50 ["CALL", null, ["callee:00c538e0:8"]]
+ 00479de8 ["INT_ADD", "register:40f0:8", ["const:479de8:8", "const:4:8"]]
+ 00479de8 ["CALL", null, ["callee:00c538e0:8"]]
- 00456f50 bytes d0ff1d94
+ 00479de8 bytes be661f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc2bc7e09c7f4ca3f3172b8c9cbfb584"></a>

### [`00456f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456f84.md) → [`00479e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e1c.md) FUN_00479e1c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00479e34",
      "incomplete_value": false,
      "site": "00479e38",
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
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456f9c",
      "incomplete_value": false,
      "site": "00456fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
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
      "00479e38",
      "DATA",
      [
        "storage",
        "00be8208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479e38",
      "DATA",
      [
        "storage",
        "00c64dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456f84.md#insn-00456f98) · [`00456f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456f84.md#insn-00456f9c) · [`00456fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456f84.md#insn-00456fb0)
- 新版 [`00479e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e1c.md#insn-00479e30) · [`00479e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e1c.md#insn-00479e34) · [`00479e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e1c.md#insn-00479e48)

~~~diff
- 00456f98 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00479e30 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00456f98 bytes 883c00d0
+ 00479e30 bytes 483f00f0
- 00456f9c ["COPY", "tmp:0:8", ["const:208:8"]]
- 00456f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00456f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00456f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479e34 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00479e34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479e34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479e34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00456f9c bytes 08210891
+ 00479e34 bytes 08213791
- 00456fb0 ["INT_ADD", "register:40f0:8", ["const:456fb0:8", "const:4:8"]]
- 00456fb0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00479e48 ["INT_ADD", "register:40f0:8", ["const:479e48:8", "const:4:8"]]
+ 00479e48 ["CALL", null, ["callee:00c538e0:8"]]
- 00456fb0 bytes b8ff1d94
+ 00479e48 bytes a6661f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d8fca2084c66294d639e00bd35c55a9"></a>

### [`00456fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456fe0.md) → [`00479e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e78.md) FUN_00479e78

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00479e9c",
      "incomplete_value": false,
      "site": "00479ea0",
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
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00457004",
      "incomplete_value": false,
      "site": "00457008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "00479ea0",
      "DATA",
      [
        "storage",
        "00be8208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479ea0",
      "DATA",
      [
        "storage",
        "00c64dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456fe0.md#insn-00456ff4) · [`00457000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456fe0.md#insn-00457000) · [`00457004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456fe0.md#insn-00457004)
- 新版 [`00479e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e78.md#insn-00479e8c) · [`00479e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e78.md#insn-00479e98) · [`00479e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479e78.md#insn-00479e9c)

~~~diff
- 00456ff4 ["INT_ADD", "register:40f0:8", ["const:456ff4:8", "const:4:8"]]
- 00456ff4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00479e8c ["INT_ADD", "register:40f0:8", ["const:479e8c:8", "const:4:8"]]
+ 00479e8c ["CALL", null, ["callee:00c57a90:8"]]
- 00456ff4 bytes 13101e94
+ 00479e8c bytes 01771f94
- 00457000 ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 00479e98 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00457000 bytes 893c00b0
+ 00479e98 bytes 493f00f0
- 00457004 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00457004 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00457004 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00457004 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479e9c ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00479e9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479e9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479e9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00457004 bytes 29210891
+ 00479e9c bytes 29213791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f17a4d27ccbfc1943cbc37b1d61f22bd"></a>

### [`00457038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457038.md) → [`00479ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479ed0.md) FUN_00479ed0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "00479ed8",
      "incomplete_value": false,
      "site": "00479edc",
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
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00457040",
      "incomplete_value": false,
      "site": "00457044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "00479edc",
      "DATA",
      [
        "storage",
        "00be8208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479edc",
      "DATA",
      [
        "storage",
        "00c64dc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045703c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457038.md#insn-0045703c) · [`00457040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457038.md#insn-00457040) · [`00457068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457038.md#insn-00457068)
- 新版 [`00479ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479ed0.md#insn-00479ed4) · [`00479ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479ed0.md#insn-00479ed8) · [`00479f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479ed0.md#insn-00479f00)

~~~diff
- 0045703c ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 00479ed4 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045703c bytes 893c00b0
+ 00479ed4 bytes 493f00f0
- 00457040 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00457040 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00457040 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00457040 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479ed8 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00479ed8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479ed8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479ed8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00457040 bytes 29210891
+ 00479ed8 bytes 29213791
- 00457068 ["INT_ADD", "register:40f0:8", ["const:457068:8", "const:4:8"]]
- 00457068 ["CALL", null, ["callee:00c538b0:8"]]
+ 00479f00 ["INT_ADD", "register:40f0:8", ["const:479f00:8", "const:4:8"]]
+ 00479f00 ["CALL", null, ["callee:00c538b0:8"]]
- 00457068 bytes 7eff1d94
+ 00479f00 bytes 6c661f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6da21866f87ad041b88915c16e58818d"></a>

### [`00457114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457114.md) → [`00479fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479fac.md) FUN_00479fac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`004572a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004572a0.md) [`004572a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004572a4.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`004709fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/004709fc.md) [`0052dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dabc.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047a138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a138.md) [`0047a13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a13c.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`00493894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493894.md) [`00550954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550954.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a008",
      "incomplete_value": false,
      "site": "0047a010",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00457170",
      "incomplete_value": false,
      "site": "00457178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:288:8"
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
      "site": "00479fe0",
      "value": [
        "leaf",
        "ram:550954:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00457148",
      "value": [
        "leaf",
        "ram:52dabc:8"
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
      "site": "0047a000",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00457168",
      "value": [
        "leaf",
        "ram:469e20:8"
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
      "00479fe0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0052dabc"
      ]
    ],
    [
      "0047a000",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      "0047a010",
      "DATA",
      [
        "storage",
        "00be8288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479fe0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00550954"
      ]
    ],
    [
      "0047a000",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0047a010",
      "DATA",
      [
        "storage",
        "00c64e48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00457148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457114.md#insn-00457148) · [`00457168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457114.md#insn-00457168) · [`00457158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457114.md#insn-00457158)
- 新版 [`00479fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479fac.md#insn-00479fe0) · [`0047a000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479fac.md#insn-0047a000) · [`00479ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479fac.md#insn-00479ff0)

~~~diff
- 00457148 ["INT_ADD", "register:40f0:8", ["const:457148:8", "const:4:8"]]
- 00457148 ["CALL", null, ["ram:52dabc:8"]]
+ 00479fe0 ["INT_ADD", "register:40f0:8", ["const:479fe0:8", "const:4:8"]]
+ 00479fe0 ["CALL", null, ["ram:550954:8"]]
- 00457148 bytes 5d5a0394
+ 00479fe0 bytes 5d5a0394
- 00457168 ["INT_ADD", "register:40f0:8", ["const:457168:8", "const:4:8"]]
- 00457168 ["CALL", null, ["ram:469e20:8"]]
+ 0047a000 ["INT_ADD", "register:40f0:8", ["const:47a000:8", "const:4:8"]]
+ 0047a000 ["CALL", null, ["ram:48ccb8:8"]]
- 00457168 bytes 2e4b0094
+ 0047a000 bytes 2e4b0094
- 00457158 ["INT_ADD", "register:40f0:8", ["const:457158:8", "const:4:8"]]
- 00457158 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00479ff0 ["INT_ADD", "register:40f0:8", ["const:479ff0:8", "const:4:8"]]
+ 00479ff0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00457158 bytes c20f1e94
+ 00479ff0 bytes b0761f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-228dbda337644de1214c5c01e793e75c"></a>

### [`0045726c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045726c.md) → [`0047a104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a104.md) FUN_0047a104

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047a118",
      "incomplete_value": false,
      "site": "0047a11c",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00457280",
      "incomplete_value": false,
      "site": "00457284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:288:8"
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
      "0047a11c",
      "DATA",
      [
        "storage",
        "00be8288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a11c",
      "DATA",
      [
        "storage",
        "00c64e48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00457278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045726c.md#insn-00457278) · [`0045727c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045726c.md#insn-0045727c) · [`00457280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045726c.md#insn-00457280)
- 新版 [`0047a110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a104.md#insn-0047a110) · [`0047a114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a104.md#insn-0047a114) · [`0047a118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a104.md#insn-0047a118)

~~~diff
- 00457278 ["INT_ADD", "register:40f0:8", ["const:457278:8", "const:4:8"]]
- 00457278 ["CALL", null, ["callee:00c57a90:8"]]
+ 0047a110 ["INT_ADD", "register:40f0:8", ["const:47a110:8", "const:4:8"]]
+ 0047a110 ["CALL", null, ["callee:00c57a90:8"]]
- 00457278 bytes 720f1e94
+ 0047a110 bytes 60761f94
- 0045727c ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 0047a114 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045727c bytes 883c00b0
+ 0047a114 bytes 483f00d0
- 00457280 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00457280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00457280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00457280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a118 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0047a118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00457280 bytes 08210a91
+ 0047a118 bytes 08213991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0be05c0d7699d60876aa368f8439190f"></a>

### [`00457290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457290.md) → [`0047a128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a128.md) FUN_0047a128

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047a12c",
      "incomplete_value": false,
      "site": "0047a130",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00457294",
      "incomplete_value": false,
      "site": "00457298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
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
      "0047a130",
      "DATA",
      [
        "storage",
        "00be8288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a130",
      "DATA",
      [
        "storage",
        "00c64e48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00457290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457290.md#insn-00457290) · [`00457294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457290.md#insn-00457294)
- 新版 [`0047a128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a128.md#insn-0047a128) · [`0047a12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a128.md#insn-0047a12c)

~~~diff
- 00457290 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 0047a128 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00457290 bytes 883c00b0
+ 0047a128 bytes 483f00d0
- 00457294 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00457294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00457294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00457294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a12c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0047a12c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a12c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a12c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00457294 bytes 08210a91
+ 0047a12c bytes 08213991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36f7032aabd3ab660334973a13376590"></a>

### [`004572a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004572a8.md) → [`0047a140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md) FUN_0047a140

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`0045786c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045786c.md) [`004578bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004578bc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0047a704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a704.md) [`0047a754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a754.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a164",
      "incomplete_value": true,
      "site": "0047a180",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b6a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004572cc",
      "incomplete_value": true,
      "site": "004572e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2fd:8"
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
      "definition_site": "0047a2b4",
      "incomplete_value": false,
      "site": "0047a2b4",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045741c",
      "incomplete_value": false,
      "site": "0045741c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "0047a164",
      "READ",
      [
        "storage",
        "002a42fd",
        null,
        "string"
      ]
    ],
    [
      "0047a2b4",
      "DATA",
      [
        "storage",
        "00be82f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0047a344",
      "READ",
      [
        "storage",
        "00be8318",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047a164",
      "READ",
      [
        "storage",
        "002b4b6a",
        null,
        "string"
      ]
    ],
    [
      "0047a2b4",
      "DATA",
      [
        "storage",
        "00c64eb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0047a344",
      "READ",
      [
        "storage",
        "00c64ed8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004572c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004572a8.md#insn-004572c0) · [`004572c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004572a8.md#insn-004572c4) · [`004572f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004572a8.md#insn-004572f8)
- 新版 [`0047a158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md#insn-0047a158) · [`0047a15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md#insn-0047a15c) · [`0047a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a140.md#insn-0047a190)

~~~diff
- 004572c0 ["COPY", "register:4050:8", ["const:2a4000:8"]]
+ 0047a158 ["COPY", "register:4050:8", ["const:2b4000:8"]]
- 004572c0 bytes 6af2ffb0
+ 0047a158 bytes caf1ffd0
- 004572c4 ["COPY", "tmp:0:8", ["const:2fd:8"]]
- 004572c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004572c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004572c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047a15c ["COPY", "tmp:0:8", ["const:b6a:8"]]
+ 0047a15c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047a15c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047a15c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004572c4 bytes 4af50b91
+ 0047a15c bytes 4aa92d91
- 004572f8 ["INT_ADD", "register:40f0:8", ["const:4572f8:8", "const:4:8"]]
- 004572f8 ["CALL", null, ["callee:0048ce14:8"]]
+ 0047a190 ["INT_ADD", "register:40f0:8", ["const:47a190:8", "const:4:8"]]
+ 0047a190 ["CALL", null, ["callee:0048ce14:8"]]
- 004572f8 bytes 214b0094
+ 0047a190 bytes 214b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5667b6b8452ea57d2c241ceacc084fa4"></a>

### [`00457730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457730.md) → [`0047a5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a5c8.md) FUN_0047a5c8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "0047a5dc",
      "incomplete_value": false,
      "site": "0047a5e0",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00457744",
      "incomplete_value": false,
      "site": "00457748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "0047a5e0",
      "DATA",
      [
        "storage",
        "00be82f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a5e0",
      "DATA",
      [
        "storage",
        "00c64eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00457740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457730.md#insn-00457740) · [`00457744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457730.md#insn-00457744) · [`00457758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457730.md#insn-00457758)
- 新版 [`0047a5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a5c8.md#insn-0047a5d8) · [`0047a5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a5c8.md#insn-0047a5dc) · [`0047a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a5c8.md#insn-0047a5f0)

~~~diff
- 00457740 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 0047a5d8 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00457740 bytes 883c00b0
+ 0047a5d8 bytes 483f00d0
- 00457744 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 00457744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00457744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00457744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a5dc ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 0047a5dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a5dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a5dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00457744 bytes 08e10b91
+ 0047a5dc bytes 08e13a91
- 00457758 ["INT_ADD", "register:40f0:8", ["const:457758:8", "const:4:8"]]
- 00457758 ["CALL", null, ["callee:00c538e0:8"]]
+ 0047a5f0 ["INT_ADD", "register:40f0:8", ["const:47a5f0:8", "const:4:8"]]
+ 0047a5f0 ["CALL", null, ["callee:00c538e0:8"]]
- 00457758 bytes cefd1d94
+ 0047a5f0 bytes bc641f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93300950b77f1c9822b33fb217f2c3f8"></a>

### [`0045778c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045778c.md) → [`0047a624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a624.md) FUN_0047a624

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0047a63c",
      "incomplete_value": false,
      "site": "0047a640",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004577a4",
      "incomplete_value": false,
      "site": "004577a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "0047a640",
      "DATA",
      [
        "storage",
        "00be82f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a640",
      "DATA",
      [
        "storage",
        "00c64eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004577a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045778c.md#insn-004577a0) · [`004577a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045778c.md#insn-004577a4) · [`004577b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/0045778c.md#insn-004577b8)
- 新版 [`0047a638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a624.md#insn-0047a638) · [`0047a63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a624.md#insn-0047a63c) · [`0047a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a624.md#insn-0047a650)

~~~diff
- 004577a0 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 0047a638 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 004577a0 bytes 883c00b0
+ 0047a638 bytes 483f00d0
- 004577a4 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 004577a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004577a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004577a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a63c ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 0047a63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004577a4 bytes 08e10b91
+ 0047a63c bytes 08e13a91
- 004577b8 ["INT_ADD", "register:40f0:8", ["const:4577b8:8", "const:4:8"]]
- 004577b8 ["CALL", null, ["callee:00c538e0:8"]]
+ 0047a650 ["INT_ADD", "register:40f0:8", ["const:47a650:8", "const:4:8"]]
+ 0047a650 ["CALL", null, ["callee:00c538e0:8"]]
- 004577b8 bytes b6fd1d94
+ 0047a650 bytes a4641f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8632ad1ba48c7aaadcaf85ae6691a138"></a>

### [`004577e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004577e8.md) → [`0047a680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a680.md) FUN_0047a680

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0047a6a4",
      "incomplete_value": false,
      "site": "0047a6a4",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045780c",
      "incomplete_value": false,
      "site": "0045780c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "0047a6a4",
      "DATA",
      [
        "storage",
        "00be82f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a6a4",
      "DATA",
      [
        "storage",
        "00c64eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004577fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004577e8.md#insn-004577fc) · [`00457804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004577e8.md#insn-00457804) · [`00457808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/004577e8.md#insn-00457808)
- 新版 [`0047a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a680.md#insn-0047a694) · [`0047a69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a680.md#insn-0047a69c) · [`0047a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a680.md#insn-0047a6a0)

~~~diff
- 004577fc ["INT_ADD", "register:40f0:8", ["const:4577fc:8", "const:4:8"]]
- 004577fc ["CALL", null, ["callee:00c57a90:8"]]
+ 0047a694 ["INT_ADD", "register:40f0:8", ["const:47a694:8", "const:4:8"]]
+ 0047a694 ["CALL", null, ["callee:00c57a90:8"]]
- 004577fc bytes 110e1e94
+ 0047a694 bytes ff741f94
- 00457804 ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 0047a69c ["COPY", "register:4048:8", ["const:c64000:8"]]
- 00457804 bytes 893c00b0
+ 0047a69c bytes 493f00d0
- 00457808 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 00457808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00457808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00457808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047a6a0 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 0047a6a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a6a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a6a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00457808 bytes 29e10b91
+ 0047a6a0 bytes 29e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3136a93d766dbf9332d483970deee27"></a>

### [`00457838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457838.md) → [`0047a6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a6d0.md) FUN_0047a6d0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "0047a6dc",
      "incomplete_value": false,
      "site": "0047a6dc",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00457844",
      "incomplete_value": false,
      "site": "00457844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "0047a6dc",
      "DATA",
      [
        "storage",
        "00be82f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a6dc",
      "DATA",
      [
        "storage",
        "00c64eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045783c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457838.md#insn-0045783c) · [`00457840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457838.md#insn-00457840) · [`00457860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457838.md#insn-00457860)
- 新版 [`0047a6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a6d0.md#insn-0047a6d4) · [`0047a6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a6d0.md#insn-0047a6d8) · [`0047a6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a6d0.md#insn-0047a6f8)

~~~diff
- 0045783c ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 0047a6d4 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045783c bytes 893c00b0
+ 0047a6d4 bytes 493f00d0
- 00457840 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 00457840 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00457840 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00457840 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047a6d8 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 0047a6d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a6d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a6d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00457840 bytes 29e10b91
+ 0047a6d8 bytes 29e13a91
- 00457860 ["INT_ADD", "register:40f0:8", ["const:457860:8", "const:4:8"]]
- 00457860 ["CALL", null, ["callee:00c538b0:8"]]
+ 0047a6f8 ["INT_ADD", "register:40f0:8", ["const:47a6f8:8", "const:4:8"]]
+ 0047a6f8 ["CALL", null, ["callee:00c538b0:8"]]
- 00457860 bytes 80fd1d94
+ 0047a6f8 bytes 6e641f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c972b085df587aad10b198e0ca01393a"></a>

### [`00457a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457a8c.md) → [`0047a924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a924.md) _INIT_16

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a960",
      "incomplete_value": true,
      "site": "0047a97c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00457ac8",
      "incomplete_value": true,
      "site": "00457ae4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
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
      "definition_site": "0047a984",
      "incomplete_value": true,
      "site": "0047a9a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00457aec",
      "incomplete_value": true,
      "site": "00457b08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
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
      "definition_site": "0047a9a4",
      "incomplete_value": true,
      "site": "0047a9c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00457b0c",
      "incomplete_value": true,
      "site": "00457b28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
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
      "0047a960",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0047a984",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0047a9a4",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047a960",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0047a984",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0047a9a4",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00457bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457a8c.md#insn-00457bec) · [`00457cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457a8c.md#insn-00457cc0) · [`00457ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457a8c.md#insn-00457ab4)
- 新版 [`0047aa84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a924.md#insn-0047aa84) · [`0047ab58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a924.md#insn-0047ab58) · [`0047a94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047a924.md#insn-0047a94c)

~~~diff
- 00457bec ["INT_ADD", "register:40f0:8", ["const:457bec:8", "const:4:8"]]
- 00457bec ["CALL", null, ["callee:0043b7b8:8"]]
+ 0047aa84 ["INT_ADD", "register:40f0:8", ["const:47aa84:8", "const:4:8"]]
+ 0047aa84 ["CALL", null, ["callee:0043b7b8:8"]]
- 00457bec bytes 3304ff97
+ 0047aa84 bytes 4d03ff97
- 00457cc0 ["INT_ADD", "register:40f0:8", ["const:457cc0:8", "const:4:8"]]
- 00457cc0 ["CALL", null, ["callee:00c57a30:8"]]
+ 0047ab58 ["INT_ADD", "register:40f0:8", ["const:47ab58:8", "const:4:8"]]
+ 0047ab58 ["CALL", null, ["callee:00c57a30:8"]]
- 00457cc0 bytes c80c1e94
+ 0047ab58 bytes b6731f94
- 00457ab4 ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 0047a94c ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 00457ab4 bytes 733e00b0
+ 0047a94c bytes 534100d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c458bfa63f3ff99801486ac03e18afe5"></a>

### [`00458038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458038.md) → [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) FUN_0047aed0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d83c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00458634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458634.md) [`0045a3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a3a4.md)
- 新版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 23件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004706d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706d4.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0047b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md) [`0047d23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d23c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047af18",
      "incomplete_value": false,
      "site": "0047af28",
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
    "old": {
      "definition_site": "00458080",
      "incomplete_value": false,
      "site": "00458090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "definition_site": "0047b378",
      "incomplete_value": true,
      "site": "0047b37c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004584e0",
      "incomplete_value": true,
      "site": "004584e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047b374",
      "incomplete_value": true,
      "site": "0047b380",
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
      "definition_site": "004584dc",
      "incomplete_value": true,
      "site": "004584e8",
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
    "ordinal": 47,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047af28",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0047b368",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "0047b36c",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047af28",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0047b368",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "0047b36c",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00458074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458038.md#insn-00458074) · [`0045807c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458038.md#insn-0045807c) · [`00458080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458038.md#insn-00458080)
- 新版 [`0047af0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md#insn-0047af0c) · [`0047af14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md#insn-0047af14) · [`0047af18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md#insn-0047af18)

~~~diff
- 00458074 ["INT_ADD", "register:40f0:8", ["const:458074:8", "const:4:8"]]
- 00458074 ["CALL", null, ["callee:00487de0:8"]]
+ 0047af0c ["INT_ADD", "register:40f0:8", ["const:47af0c:8", "const:4:8"]]
+ 0047af0c ["CALL", null, ["callee:00487de0:8"]]
- 00458074 bytes b5330094
+ 0047af0c bytes b5330094
- 0045807c ["COPY", "register:4050:8", ["const:be7000:8"]]
+ 0047af14 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0045807c bytes 6a3c00f0
+ 0047af14 bytes 4a3f00d0
- 00458080 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00458080 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00458080 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00458080 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047af18 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 0047af18 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047af18 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047af18 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00458080 bytes 4ae13591
+ 0047af18 bytes 4ae12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31f80c0250cd1fa5588be183e929389f"></a>

### [`00458974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458974.md) → [`0047b80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md) FUN_0047b80c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0045cb74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cb74.md) [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) [`00844bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) · 呼出先 13件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0052dd48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd48.md) [`0052dd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd4c.md) [`0052dd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd50.md)
- 新版 呼出元 3件 [`0047fa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fa0c.md) [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 13件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00550be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be0.md) [`00550be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be4.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047b864",
      "incomplete_value": true,
      "site": "0047b864",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004589cc",
      "incomplete_value": true,
      "site": "004589cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:471:8"
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
      "definition_site": "0047b988",
      "incomplete_value": true,
      "site": "0047b988",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:80e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458af0",
      "incomplete_value": true,
      "site": "00458af0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3fb:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047bb18",
      "incomplete_value": false,
      "site": "0047bb1c",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458c80",
      "incomplete_value": false,
      "site": "00458c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047b850",
      "READ",
      [
        "storage",
        "002a7471",
        null,
        "string"
      ]
    ],
    [
      "0047b974",
      "READ",
      [
        "storage",
        "0029f3fb",
        null,
        "string"
      ]
    ],
    [
      "0047bb18",
      "PARAM",
      [
        "storage",
        "00c24a18",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047b850",
      "READ",
      [
        "storage",
        "002b7fe0",
        null,
        "string"
      ]
    ],
    [
      "0047b974",
      "READ",
      [
        "storage",
        "002af80e",
        null,
        "string"
      ]
    ],
    [
      "0047bb18",
      "PARAM",
      [
        "storage",
        "00ca44d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00458c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458974.md#insn-00458c84) · [`00458d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458974.md#insn-00458d10) · [`004589a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458974.md#insn-004589a8)
- 新版 [`0047bb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md#insn-0047bb1c) · [`0047bba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md#insn-0047bba8) · [`0047b840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md#insn-0047b840)

~~~diff
- 00458c84 ["INT_ADD", "register:40f0:8", ["const:458c84:8", "const:4:8"]]
- 00458c84 ["CALL", null, ["callee:00c57ce0:8"]]
+ 0047bb1c ["INT_ADD", "register:40f0:8", ["const:47bb1c:8", "const:4:8"]]
+ 0047bb1c ["CALL", null, ["callee:00c57ce0:8"]]
- 00458c84 bytes 83091e94
+ 0047bb1c bytes 71701f94
- 00458d10 ["INT_ADD", "register:40f0:8", ["const:458d10:8", "const:4:8"]]
- 00458d10 ["CALL", null, ["callee:00c57cf0:8"]]
+ 0047bba8 ["INT_ADD", "register:40f0:8", ["const:47bba8:8", "const:4:8"]]
+ 0047bba8 ["CALL", null, ["callee:00c57cf0:8"]]
- 00458d10 bytes 64091e94
+ 0047bba8 bytes 52701f94
- 004589a8 ["INT_ADD", "register:40f0:8", ["const:4589a8:8", "const:4:8"]]
- 004589a8 ["CALL", null, ["callee:00550be8:8"]]
+ 0047b840 ["INT_ADD", "register:40f0:8", ["const:47b840:8", "const:4:8"]]
+ 0047b840 ["CALL", null, ["callee:00550be8:8"]]
- 004589a8 bytes ea540394
+ 0047b840 bytes ea540394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-041aa3bc96db79effbad716ac97c142c"></a>

### [`00458e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458e28.md) → [`0047bcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bcc0.md) FUN_0047bcc0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008226b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/008226b4.md) · 呼出先 4件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 1件 [`00854630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/00854630.md) · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047bcd8",
      "incomplete_value": false,
      "site": "0047bce0",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458e40",
      "incomplete_value": false,
      "site": "00458e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a18:8"
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
      "0047bcd8",
      "PARAM",
      [
        "storage",
        "00c24a18",
        null,
        null
      ]
    ],
    [
      "0047bd8c",
      "PARAM",
      [
        "storage",
        "00c24a18",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047bcd8",
      "PARAM",
      [
        "storage",
        "00ca44d8",
        null,
        null
      ]
    ],
    [
      "0047bd8c",
      "PARAM",
      [
        "storage",
        "00ca44d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00458e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458e28.md#insn-00458e48) · [`00458e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458e28.md#insn-00458e3c) · [`00458e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458e28.md#insn-00458e40)
- 新版 [`0047bce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bcc0.md#insn-0047bce0) · [`0047bcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bcc0.md#insn-0047bcd4) · [`0047bcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bcc0.md#insn-0047bcd8)

~~~diff
- 00458e48 ["INT_ADD", "register:40f0:8", ["const:458e48:8", "const:4:8"]]
- 00458e48 ["CALL", null, ["callee:00c57ce0:8"]]
+ 0047bce0 ["INT_ADD", "register:40f0:8", ["const:47bce0:8", "const:4:8"]]
+ 0047bce0 ["CALL", null, ["callee:00c57ce0:8"]]
- 00458e48 bytes 12091e94
+ 0047bce0 bytes 00701f94
- 00458e3c ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 0047bcd4 ["COPY", "register:4000:8", ["const:ca4000:8"]]
- 00458e3c bytes 603e0090
+ 0047bcd4 bytes 404100b0
- 00458e40 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 00458e40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00458e40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00458e40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047bcd8 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 0047bcd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047bcd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047bcd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00458e40 bytes 00602891
+ 0047bcd8 bytes 00601391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76ae2ed05f9746b7b023c966190371aa"></a>

### [`00458f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458f08.md) → [`0047bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md) FUN_0047bda0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00459170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459170.md) · 呼出先 9件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0045a844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a844.md) [`0045a848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a848.md) [`0045a84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a84c.md) [`00548364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548364.md)
- 新版 呼出元 1件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) · 呼出先 9件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6dc.md) [`0047d6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6e0.md) [`0047d6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6e4.md) [`0056b1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b1fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.47% / 新版 98.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047bdd4",
      "incomplete_value": false,
      "site": "0047bdd4",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458f3c",
      "incomplete_value": false,
      "site": "00458f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "0047bdd4",
      "DATA",
      [
        "storage",
        "00be8398",
        null,
        "undefined *"
      ]
    ],
    [
      "0047be84",
      "READ",
      [
        "storage",
        "00be83c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0047bef8",
      "READ",
      [
        "storage",
        "00be83b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047bdd4",
      "DATA",
      [
        "storage",
        "00c64f58",
        null,
        "undefined *"
      ]
    ],
    [
      "0047be84",
      "READ",
      [
        "storage",
        "00c64f88",
        null,
        "undefined *"
      ]
    ],
    [
      "0047bef8",
      "READ",
      [
        "storage",
        "00c64f78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00458f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458f08.md#insn-00458f34) · [`00458f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458f08.md#insn-00458f38) · [`00458f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458f08.md#insn-00458f4c)
- 新版 [`0047bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md#insn-0047bdcc) · [`0047bdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md#insn-0047bdd0) · [`0047bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md#insn-0047bde4)

~~~diff
- 00458f34 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 0047bdcc ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00458f34 bytes 883c0090
+ 0047bdcc bytes 483f00b0
- 00458f38 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00458f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00458f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00458f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047bdd0 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 0047bdd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047bdd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047bdd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00458f38 bytes 08610e91
+ 0047bdd0 bytes 08613d91
- 00458f4c ["INT_ADD", "register:40f0:8", ["const:458f4c:8", "const:4:8"]]
- 00458f4c ["CALL", null, ["callee:0047d6e4:8"]]
+ 0047bde4 ["INT_ADD", "register:40f0:8", ["const:47bde4:8", "const:4:8"]]
+ 0047bde4 ["CALL", null, ["callee:0047d6e4:8"]]
- 00458f4c bytes 40060094
+ 0047bde4 bytes 40060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aee2ce3c3a8ca6b472ebd0707b1b07fb"></a>

### [`00459170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459170.md) → [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) FUN_0047c008

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00459f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f04.md) [`0045a030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a030.md) [`0045cb74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cb74.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00458f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458f08.md) [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`00459bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459bb4.md)
- 新版 呼出元 4件 [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047cd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd9c.md) [`0047cec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cec8.md) [`0047fa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fa0c.md) · 呼出先 22件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0047bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md) [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047ca4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047ca4c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 4件, `store_condition` 2件, `store_destination` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0047c1c4",
      "incomplete_value": true,
      "site": "0047c1c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:2730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045932c",
      "incomplete_value": true,
      "site": "0045932c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:2640:8"
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0047c1dc",
      "incomplete_value": true,
      "site": "0047c1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:2740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459344",
      "incomplete_value": true,
      "site": "00459344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:2650:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047c1d8",
      "incomplete_value": true,
      "site": "0047c1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459340",
      "incomplete_value": true,
      "site": "00459344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1:8"
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
      "0047c25c",
      "READ",
      [
        "storage",
        "0029092c",
        null,
        "string"
      ]
    ],
    [
      "0047c6d8",
      "PARAM",
      [
        "storage",
        "00c24a18",
        null,
        null
      ]
    ],
    [
      "0047c714",
      "PARAM",
      [
        "storage",
        "00c24a18",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047c25c",
      "READ",
      [
        "storage",
        "0029fe6e",
        null,
        "string"
      ]
    ],
    [
      "0047c6d8",
      "PARAM",
      [
        "storage",
        "00ca44d8",
        null,
        null
      ]
    ],
    [
      "0047c714",
      "PARAM",
      [
        "storage",
        "00ca44d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045932c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459170.md#insn-0045932c) · [`00459338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459170.md#insn-00459338) · [`00459344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459170.md#insn-00459344)
- 新版 [`0047c1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md#insn-0047c1c4) · [`0047c1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md#insn-0047c1d0) · [`0047c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md#insn-0047c1dc)

~~~diff
- 0045932c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:2640:8"]]
- 0045932c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0047c1c4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:2730:8"]]
+ 0047c1c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0045932c bytes c82213f9
+ 0047c1c4 bytes c89a13f9
- 00459338 ["INT_ADD", "register:40f0:8", ["const:459338:8", "const:4:8"]]
- 00459338 ["CALL", null, ["callee:0043bb64:8"]]
+ 0047c1d0 ["INT_ADD", "register:40f0:8", ["const:47c1d0:8", "const:4:8"]]
+ 0047c1d0 ["CALL", null, ["callee:0043bb64:8"]]
- 00459338 bytes 4bfffe97
+ 0047c1d0 bytes 65fefe97
- 00459344 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:2650:8"]]
- 00459344 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0047c1dc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:2740:8"]]
+ 0047c1dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00459344 bytes c82a13f9
+ 0047c1dc bytes c8a213f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-526049b038efe63966fc3d9b9a4ede04"></a>

### [`00459f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f04.md) → [`0047cd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd9c.md) FUN_0047cd9c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`005ccda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005ccda8.md) [`005cd3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cd3e0.md) [`005cd614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cd614.md) [`005cda6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cda6c.md) [`005d3af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d3/005d3af8.md) · 呼出先 2件 [`00459170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459170.md) [`005bc058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc058.md)
- 新版 呼出元 9件 [`005f1a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f1a94.md) [`005f20cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f20cc.md) [`005f2300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2300.md) [`005f2758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2758.md) [`005f87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f87e0.md) · 呼出先 2件 [`0047c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c008.md) [`005e0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0d28.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

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
      "site": "0047cdb0",
      "value": [
        "leaf",
        "ram:5e0d28:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00459f18",
      "value": [
        "leaf",
        "ram:5bc058:8"
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
      "0047cdb0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005bc058"
      ]
    ]
  ],
  "added": [
    [
      "0047cdb0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e0d28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f04.md#insn-00459f18)
- 新版 [`0047cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd9c.md#insn-0047cdb0)

~~~diff
- 00459f18 ["INT_ADD", "register:40f0:8", ["const:459f18:8", "const:4:8"]]
- 00459f18 ["CALL", null, ["ram:5bc058:8"]]
+ 0047cdb0 ["INT_ADD", "register:40f0:8", ["const:47cdb0:8", "const:4:8"]]
+ 0047cdb0 ["CALL", null, ["ram:5e0d28:8"]]
- 00459f18 bytes 50880594
+ 0047cdb0 bytes de8f0594
~~~


<a id="compare-c2c537ed80e8f493781a9536a8fce081"></a>

### [`0045a320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a320.md) → [`0047d1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d1b8.md) FUN_0047d1b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00821cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cbc.md) · 呼出先 2件 [`0045b334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b334.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00853c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c38.md) · 呼出先 2件 [`0047e1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "0047d1e8",
      "incomplete_value": false,
      "site": "0047d1f4",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a350",
      "incomplete_value": false,
      "site": "0045a35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "0047d1f4",
      "DATA",
      [
        "storage",
        "00be8428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047d1f4",
      "DATA",
      [
        "storage",
        "00c64fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a320.md#insn-0045a344) · [`0045a34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a320.md#insn-0045a34c) · [`0045a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a320.md#insn-0045a350)
- 新版 [`0047d1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d1b8.md#insn-0047d1dc) · [`0047d1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d1b8.md#insn-0047d1e4) · [`0047d1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d1b8.md#insn-0047d1e8)

~~~diff
- 0045a344 ["INT_ADD", "register:40f0:8", ["const:45a344:8", "const:4:8"]]
- 0045a344 ["CALL", null, ["callee:00c57a90:8"]]
+ 0047d1dc ["INT_ADD", "register:40f0:8", ["const:47d1dc:8", "const:4:8"]]
+ 0047d1dc ["CALL", null, ["callee:00c57a90:8"]]
- 0045a344 bytes 3f031e94
+ 0047d1dc bytes 2d6a1f94
- 0045a34c ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 0047d1e4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045a34c bytes 683c00d0
+ 0047d1e4 bytes 283f00f0
- 0045a350 ["COPY", "tmp:0:8", ["const:428:8"]]
- 0045a350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045a350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045a350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047d1e8 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0047d1e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d1e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d1e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045a350 bytes 08a11091
+ 0047d1e8 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4511ac88d5db5af4227fd5eab5d1b16d"></a>

### [`0045a52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a52c.md) → [`0047d3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3c4.md) FUN_0047d3c4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045a3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a3a4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0047d23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d23c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0047d3d4",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045a53c",
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
      "definition_site": "0047d3d0",
      "incomplete_value": false,
      "site": "0047d3d4",
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
      "definition_site": "0045a538",
      "incomplete_value": false,
      "site": "0045a53c",
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
      "0047d3d0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0047d3d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0047d3d0",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0047d3d4",
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

- 旧版 [`0045a53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a52c.md#insn-0045a53c) · [`0045a534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a52c.md#insn-0045a534) · [`0045a538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a52c.md#insn-0045a538)
- 新版 [`0047d3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3c4.md#insn-0047d3d4) · [`0047d3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3c4.md#insn-0047d3cc) · [`0047d3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3c4.md#insn-0047d3d0)

~~~diff
- 0045a53c ["INT_ADD", "register:40f0:8", ["const:45a53c:8", "const:4:8"]]
- 0045a53c ["CALL", null, ["ram:418c38:8"]]
+ 0047d3d4 ["INT_ADD", "register:40f0:8", ["const:47d3d4:8", "const:4:8"]]
+ 0047d3d4 ["CALL", null, ["ram:43b738:8"]]
- 0045a53c bytes bff9fe97
+ 0047d3d4 bytes d9f8fe97
- 0045a534 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0047d3cc ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0045a534 bytes 60f2ffb0
+ 0047d3cc bytes c0f1ffd0
- 0045a538 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0045a538 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0045a538 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0045a538 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047d3d0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0047d3d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d3d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d3d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0045a538 bytes 00740e91
+ 0047d3d0 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88bfb105eacae178ce5268268c09b675"></a>

### [`0045a6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6c8.md) → [`0047d560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d560.md) FUN_0047d560

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045a540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a540.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0047d3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d3d8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0047d570",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045a6d8",
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
      "definition_site": "0047d56c",
      "incomplete_value": false,
      "site": "0047d570",
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
      "definition_site": "0045a6d4",
      "incomplete_value": false,
      "site": "0045a6d8",
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
      "0047d56c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0047d570",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0047d56c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0047d570",
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

- 旧版 [`0045a6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6c8.md#insn-0045a6d8) · [`0045a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6c8.md#insn-0045a6d0) · [`0045a6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6c8.md#insn-0045a6d4)
- 新版 [`0047d570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d560.md#insn-0047d570) · [`0047d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d560.md#insn-0047d568) · [`0047d56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d560.md#insn-0047d56c)

~~~diff
- 0045a6d8 ["INT_ADD", "register:40f0:8", ["const:45a6d8:8", "const:4:8"]]
- 0045a6d8 ["CALL", null, ["ram:418c38:8"]]
+ 0047d570 ["INT_ADD", "register:40f0:8", ["const:47d570:8", "const:4:8"]]
+ 0047d570 ["CALL", null, ["ram:43b738:8"]]
- 0045a6d8 bytes 58f9fe97
+ 0047d570 bytes 72f8fe97
- 0045a6d0 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0047d568 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0045a6d0 bytes 60f2ffb0
+ 0047d568 bytes c0f1ffd0
- 0045a6d4 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0045a6d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0045a6d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0045a6d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047d56c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0047d56c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d56c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d56c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0045a6d4 bytes 00740e91
+ 0047d56c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0885ca4698d96357b4507d799497113b"></a>

### [`0045a7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7e0.md) → [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) FUN_0047d678

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`00458634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458634.md) [`0045a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a6dc.md) [`004785c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004785c8.md) [`00478d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/00478d84.md) [`0047bcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047b/0047bcc8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 8件 [`0047b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md) [`0047d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) [`0049eb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049eb60.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0047d688",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045a7f0",
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
      "definition_site": "0047d684",
      "incomplete_value": false,
      "site": "0047d688",
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
      "definition_site": "0045a7ec",
      "incomplete_value": false,
      "site": "0045a7f0",
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
      "0047d684",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0047d688",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0047d684",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0047d688",
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

- 旧版 [`0045a7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7e0.md#insn-0045a7f0) · [`0045a7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7e0.md#insn-0045a7e8) · [`0045a7ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7e0.md#insn-0045a7ec)
- 新版 [`0047d688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md#insn-0047d688) · [`0047d680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md#insn-0047d680) · [`0047d684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md#insn-0047d684)

~~~diff
- 0045a7f0 ["INT_ADD", "register:40f0:8", ["const:45a7f0:8", "const:4:8"]]
- 0045a7f0 ["CALL", null, ["ram:418c38:8"]]
+ 0047d688 ["INT_ADD", "register:40f0:8", ["const:47d688:8", "const:4:8"]]
+ 0047d688 ["CALL", null, ["ram:43b738:8"]]
- 0045a7f0 bytes 12f9fe97
+ 0047d688 bytes 2cf8fe97
- 0045a7e8 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0047d680 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0045a7e8 bytes 60f2ffb0
+ 0047d680 bytes c0f1ffd0
- 0045a7ec ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0045a7ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0045a7ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0045a7ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047d684 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0047d684 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d684 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d684 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0045a7ec bytes 00740e91
+ 0047d684 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f47cbbff7381b4844156c50785deec8"></a>

### [`0045a7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7fc.md) → [`0047d694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d694.md) FUN_0047d694

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047d6b8",
      "incomplete_value": false,
      "site": "0047d6b8",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a820",
      "incomplete_value": false,
      "site": "0045a820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "0047d6b8",
      "DATA",
      [
        "storage",
        "00be8398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047d6b8",
      "DATA",
      [
        "storage",
        "00c64f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7fc.md#insn-0045a810) · [`0045a818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7fc.md#insn-0045a818) · [`0045a81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a7fc.md#insn-0045a81c)
- 新版 [`0047d6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d694.md#insn-0047d6a8) · [`0047d6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d694.md#insn-0047d6b0) · [`0047d6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d694.md#insn-0047d6b4)

~~~diff
- 0045a810 ["INT_ADD", "register:40f0:8", ["const:45a810:8", "const:4:8"]]
- 0045a810 ["CALL", null, ["callee:00c57a90:8"]]
+ 0047d6a8 ["INT_ADD", "register:40f0:8", ["const:47d6a8:8", "const:4:8"]]
+ 0047d6a8 ["CALL", null, ["callee:00c57a90:8"]]
- 0045a810 bytes 0c021e94
+ 0047d6a8 bytes fa681f94
- 0045a818 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 0047d6b0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045a818 bytes 683c00d0
+ 0047d6b0 bytes 283f00f0
- 0045a81c ["COPY", "tmp:0:8", ["const:398:8"]]
- 0045a81c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045a81c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045a81c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047d6b4 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 0047d6b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d6b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d6b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045a81c bytes 08610e91
+ 0047d6b4 bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f46fe30754f2537550417f0d5a58e50"></a>

### [`0045a830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a830.md) → [`0047d6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6c8.md) FUN_0047d6c8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047d6d4",
      "incomplete_value": false,
      "site": "0047d6d4",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a83c",
      "incomplete_value": false,
      "site": "0045a83c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
      "0047d6d4",
      "DATA",
      [
        "storage",
        "00be8398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047d6d4",
      "DATA",
      [
        "storage",
        "00c64f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a830.md#insn-0045a834) · [`0045a838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a830.md#insn-0045a838)
- 新版 [`0047d6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6c8.md#insn-0047d6cc) · [`0047d6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d6c8.md#insn-0047d6d0)

~~~diff
- 0045a834 ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 0047d6cc ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045a834 bytes 693c00d0
+ 0047d6cc bytes 293f00f0
- 0045a838 ["COPY", "tmp:0:8", ["const:398:8"]]
- 0045a838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045a838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045a838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047d6d0 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 0047d6d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047d6d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047d6d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045a838 bytes 29610e91
+ 0047d6d0 bytes 29613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75d38e811821787f5e91344ab3989965"></a>

### [`0045a988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a988.md) → [`0047d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md) FUN_0047d820

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`0045a988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a988.md) [`0063136c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00631/0063136c.md) [`00756ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756ba0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md) [`00656e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00656/00656e50.md) [`00781004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781004.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047d97c",
      "incomplete_value": false,
      "site": "0047d984",
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
    "old": {
      "definition_site": "0045aae4",
      "incomplete_value": false,
      "site": "0045aaec",
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
            "const:3a4:8"
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
      "definition_site": "0047d9a0",
      "incomplete_value": false,
      "site": "0047d9ac",
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
    "old": {
      "definition_site": "0045ab08",
      "incomplete_value": false,
      "site": "0045ab14",
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
            "const:885:8"
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
      "definition_site": "0047dad4",
      "incomplete_value": false,
      "site": "0047dadc",
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
    "old": {
      "definition_site": "0045ac3c",
      "incomplete_value": false,
      "site": "0045ac44",
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
            "const:379:8"
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
      "0047d97c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0047d9a0",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0047dad4",
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
      "0047d97c",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0047d9a0",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0047dad4",
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

- 旧版 [`0045aaec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a988.md#insn-0045aaec) · [`0045ab14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a988.md#insn-0045ab14) · [`0045ac44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a988.md#insn-0045ac44)
- 新版 [`0047d984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md#insn-0047d984) · [`0047d9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md#insn-0047d9ac) · [`0047dadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md#insn-0047dadc)

~~~diff
- 0045aaec ["INT_ADD", "register:40f0:8", ["const:45aaec:8", "const:4:8"]]
- 0045aaec ["CALL", null, ["callee:00441e54:8"]]
+ 0047d984 ["INT_ADD", "register:40f0:8", ["const:47d984:8", "const:4:8"]]
+ 0047d984 ["CALL", null, ["callee:00441e54:8"]]
- 0045aaec bytes 1a12ff97
+ 0047d984 bytes 3411ff97
- 0045ab14 ["INT_ADD", "register:40f0:8", ["const:45ab14:8", "const:4:8"]]
- 0045ab14 ["CALL", null, ["callee:004427b4:8"]]
+ 0047d9ac ["INT_ADD", "register:40f0:8", ["const:47d9ac:8", "const:4:8"]]
+ 0047d9ac ["CALL", null, ["callee:004427b4:8"]]
- 0045ab14 bytes 6814ff97
+ 0047d9ac bytes 8213ff97
- 0045ac44 ["INT_ADD", "register:40f0:8", ["const:45ac44:8", "const:4:8"]]
- 0045ac44 ["CALL", null, ["callee:00441e54:8"]]
+ 0047dadc ["INT_ADD", "register:40f0:8", ["const:47dadc:8", "const:4:8"]]
+ 0047dadc ["CALL", null, ["callee:00441e54:8"]]
- 0045ac44 bytes c411ff97
+ 0047dadc bytes de10ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-012913b1c7b3c93c0192949542710561"></a>

### [`0045b334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b334.md) → [`0047e1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md) FUN_0047e1cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0045a320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a320.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`0047d1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d1b8.md) · 呼出先 12件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.86% / 新版 84.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 7件, `store_value` 6件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047e20c",
      "incomplete_value": false,
      "site": "0047e20c",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b374",
      "incomplete_value": false,
      "site": "0045b374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "definition_site": "0047e274",
      "incomplete_value": true,
      "site": "0047e274",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0045b3dc",
      "incomplete_value": true,
      "site": "0045b3dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3a0:8"
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
      "definition_site": "0047e28c",
      "incomplete_value": true,
      "site": "0047e28c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0045b3f4",
      "incomplete_value": true,
      "site": "0045b3f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:47d:8"
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
      "0047e20c",
      "DATA",
      [
        "storage",
        "00be8478",
        null,
        "undefined *"
      ]
    ],
    [
      "0047e22c",
      "PARAM",
      [
        "storage",
        "002b7d86",
        null,
        "string"
      ]
    ],
    [
      "0047e240",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0047e20c",
      "DATA",
      [
        "storage",
        "00c65038",
        null,
        "undefined *"
      ]
    ],
    [
      "0047e22c",
      "PARAM",
      [
        "storage",
        "002c9496",
        null,
        "string"
      ]
    ],
    [
      "0047e240",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b334.md#insn-0045b39c) · [`0045b418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b334.md#insn-0045b418) · [`0045b524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b334.md#insn-0045b524)
- 新版 [`0047e234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md#insn-0047e234) · [`0047e2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md#insn-0047e2b0) · [`0047e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md#insn-0047e3bc)

~~~diff
- 0045b39c ["INT_ADD", "register:40f0:8", ["const:45b39c:8", "const:4:8"]]
- 0045b39c ["CALL", null, ["callee:00c57d90:8"]]
+ 0047e234 ["INT_ADD", "register:40f0:8", ["const:47e234:8", "const:4:8"]]
+ 0047e234 ["CALL", null, ["callee:00c57d90:8"]]
- 0045b39c bytes e9ff1d94
+ 0047e234 bytes d7661f94
- 0045b418 ["INT_ADD", "register:40f0:8", ["const:45b418:8", "const:4:8"]]
- 0045b418 ["CALL", null, ["callee:0047e5cc:8"]]
+ 0047e2b0 ["INT_ADD", "register:40f0:8", ["const:47e2b0:8", "const:4:8"]]
+ 0047e2b0 ["CALL", null, ["callee:0047e5cc:8"]]
- 0045b418 bytes c7000094
+ 0047e2b0 bytes c7000094
- 0045b524 ["INT_ADD", "register:40f0:8", ["const:45b524:8", "const:4:8"]]
- 0045b524 ["CALL", null, ["callee:0047e89c:8"]]
+ 0047e3bc ["INT_ADD", "register:40f0:8", ["const:47e3bc:8", "const:4:8"]]
+ 0047e3bc ["CALL", null, ["callee:0047e89c:8"]]
- 0045b524 bytes 38010094
+ 0047e3bc bytes 38010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6da037a1026e2656ab32c1e3e0b3d91"></a>

### [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) → [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) FUN_0047e5cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 117件 [`0045b334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b334.md) [`00595ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595ca0.md) [`0059fbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059fbec.md) [`005a74e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a74e4.md) [`005bcea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bcea8.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0045c034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c034.md) [`0045c178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c178.md) [`0045c274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c274.md)
- 新版 呼出元 118件 [`0047e1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md) [`005ba2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba2d0.md) [`005c421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c421c.md) [`005cc174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc174.md) [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`0047eecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eecc.md) [`0047f010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f010.md) [`0047f10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f10c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047e694",
      "incomplete_value": false,
      "site": "0047e6a0",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b7fc",
      "incomplete_value": false,
      "site": "0045b808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
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
      "0047e6a0",
      "DATA",
      [
        "storage",
        "00be84e8",
        null,
        "pointer"
      ]
    ],
    [
      "0047e7e8",
      "READ",
      [
        "storage",
        "00be84f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047e6a0",
      "DATA",
      [
        "storage",
        "00c650a8",
        null,
        "pointer"
      ]
    ],
    [
      "0047e7e8",
      "READ",
      [
        "storage",
        "00c650b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md#insn-0045b780) · [`0045b78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md#insn-0045b78c) · [`0045b7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md#insn-0045b7a0)
- 新版 [`0047e618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md#insn-0047e618) · [`0047e624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md#insn-0047e624) · [`0047e638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md#insn-0047e638)

~~~diff
- 0045b780 ["INT_ADD", "register:40f0:8", ["const:45b780:8", "const:4:8"]]
- 0045b780 ["CALL", null, ["callee:00440f30:8"]]
+ 0047e618 ["INT_ADD", "register:40f0:8", ["const:47e618:8", "const:4:8"]]
+ 0047e618 ["CALL", null, ["callee:00440f30:8"]]
- 0045b780 bytes 2c0bff97
+ 0047e618 bytes 460aff97
- 0045b78c ["INT_ADD", "register:40f0:8", ["const:45b78c:8", "const:4:8"]]
- 0045b78c ["CALL", null, ["callee:0047eecc:8"]]
+ 0047e624 ["INT_ADD", "register:40f0:8", ["const:47e624:8", "const:4:8"]]
+ 0047e624 ["CALL", null, ["callee:0047eecc:8"]]
- 0045b78c bytes 2a020094
+ 0047e624 bytes 2a020094
- 0045b7a0 ["INT_ADD", "register:40f0:8", ["const:45b7a0:8", "const:4:8"]]
- 0045b7a0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0047e638 ["INT_ADD", "register:40f0:8", ["const:47e638:8", "const:4:8"]]
+ 0047e638 ["CALL", null, ["callee:00c57ab0:8"]]
- 0045b7a0 bytes 30fe1d94
+ 0047e638 bytes 1e651f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2ef8669ebf87ee582ab4fc1f28010b5"></a>

### [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) → [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) FUN_0047e89c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 92件 [`0045b334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b334.md) [`00595ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/00595ca0.md) [`005d5afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d5/005d5afc.md) [`005eb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005eb/005eb040.md) [`005fed64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fe/005fed64.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0045c378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c378.md) [`0045c584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c584.md) [`00466290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/00466290.md) [`00467930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467930.md)
- 新版 呼出元 92件 [`0047e1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e1cc.md) [`005ba2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba2d0.md) [`005fa7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fa/005fa7e4.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`00624768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624768.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0047f210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f210.md) [`0047f41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f41c.md) [`00489128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489128.md) [`0048a7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a7c8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047e9e4",
      "incomplete_value": false,
      "site": "0047e9f0",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bb4c",
      "incomplete_value": false,
      "site": "0045bb58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047ea60",
      "incomplete_value": false,
      "site": "0047ea70",
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
    "old": {
      "definition_site": "0045bbc8",
      "incomplete_value": false,
      "site": "0045bbd8",
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
            "const:fa5:8"
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
      "0047e9f0",
      "DATA",
      [
        "storage",
        "00be84e8",
        null,
        "pointer"
      ]
    ],
    [
      "0047ea60",
      "PARAM",
      [
        "storage",
        "002b6fa5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047e9f0",
      "DATA",
      [
        "storage",
        "00c650a8",
        null,
        "pointer"
      ]
    ],
    [
      "0047ea60",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bbd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md#insn-0045bbd8) · [`0045ba78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md#insn-0045ba78) · [`0045baa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md#insn-0045baa4)
- 新版 [`0047ea70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md#insn-0047ea70) · [`0047e910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md#insn-0047e910) · [`0047e93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md#insn-0047e93c)

~~~diff
- 0045bbd8 ["INT_ADD", "register:40f0:8", ["const:45bbd8:8", "const:4:8"]]
- 0045bbd8 ["CALL", null, ["callee:0047f41c:8"]]
+ 0047ea70 ["INT_ADD", "register:40f0:8", ["const:47ea70:8", "const:4:8"]]
+ 0047ea70 ["CALL", null, ["callee:0047f41c:8"]]
- 0045bbd8 bytes 6b020094
+ 0047ea70 bytes 6b020094
- 0045ba78 ["INT_ADD", "register:40f0:8", ["const:45ba78:8", "const:4:8"]]
- 0045ba78 ["CALL", null, ["callee:0043bae0:8"]]
+ 0047e910 ["INT_ADD", "register:40f0:8", ["const:47e910:8", "const:4:8"]]
+ 0047e910 ["CALL", null, ["callee:0043bae0:8"]]
- 0045ba78 bytes 5af5fe97
+ 0047e910 bytes 74f4fe97
- 0045baa4 ["INT_ADD", "register:40f0:8", ["const:45baa4:8", "const:4:8"]]
- 0045baa4 ["CALL", null, ["callee:0043bae0:8"]]
+ 0047e93c ["INT_ADD", "register:40f0:8", ["const:47e93c:8", "const:4:8"]]
+ 0047e93c ["CALL", null, ["callee:0043bae0:8"]]
- 0045baa4 bytes 4ff5fe97
+ 0047e93c bytes 69f4fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-514a92223f1389b70a30428f51a175f1"></a>

### [`0045bccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bccc.md) → [`0047eb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eb64.md) FUN_0047eb64

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb690.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c580e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580e0.md)

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
      "definition_site": "0047eb7c",
      "incomplete_value": false,
      "site": "0047eb80",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bce4",
      "incomplete_value": false,
      "site": "0045bce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "0047eb80",
      "DATA",
      [
        "storage",
        "00be8478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047eb80",
      "DATA",
      [
        "storage",
        "00c65038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bccc.md#insn-0045bce0) · [`0045bce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bccc.md#insn-0045bce4) · [`0045bcf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bccc.md#insn-0045bcf4)
- 新版 [`0047eb78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eb64.md#insn-0047eb78) · [`0047eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eb64.md#insn-0047eb7c) · [`0047eb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eb64.md#insn-0047eb8c)

~~~diff
- 0045bce0 ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 0047eb78 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0045bce0 bytes 693c00b0
+ 0047eb78 bytes 293f00f0
- 0045bce4 ["COPY", "tmp:0:8", ["const:478:8"]]
- 0045bce4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045bce4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045bce4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047eb7c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0047eb7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047eb7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047eb7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045bce4 bytes 29e11191
+ 0047eb7c bytes 29e10091
- 0045bcf4 ["INT_ADD", "register:40f0:8", ["const:45bcf4:8", "const:4:8"]]
- 0045bcf4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0047eb8c ["INT_ADD", "register:40f0:8", ["const:47eb8c:8", "const:4:8"]]
+ 0047eb8c ["CALL", null, ["callee:00c57ab0:8"]]
- 0045bcf4 bytes dbfc1d94
+ 0047eb8c bytes c9631f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84cbd0286328b2cbe3acadac1a547c74"></a>

### [`0045bd68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bd68.md) → [`0047ec00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ec00.md) FUN_0047ec00

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb690.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c580e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047ec18",
      "incomplete_value": false,
      "site": "0047ec1c",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bd80",
      "incomplete_value": false,
      "site": "0045bd84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "0047ec1c",
      "DATA",
      [
        "storage",
        "00be8478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047ec1c",
      "DATA",
      [
        "storage",
        "00c65038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bd68.md#insn-0045bd7c) · [`0045bd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bd68.md#insn-0045bd80) · [`0045bd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bd68.md#insn-0045bd90)
- 新版 [`0047ec14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ec00.md#insn-0047ec14) · [`0047ec18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ec00.md#insn-0047ec18) · [`0047ec28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ec00.md#insn-0047ec28)

~~~diff
- 0045bd7c ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 0047ec14 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0045bd7c bytes 693c00b0
+ 0047ec14 bytes 293f00f0
- 0045bd80 ["COPY", "tmp:0:8", ["const:478:8"]]
- 0045bd80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045bd80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045bd80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047ec18 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0047ec18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047ec18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047ec18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045bd80 bytes 29e11191
+ 0047ec18 bytes 29e10091
- 0045bd90 ["INT_ADD", "register:40f0:8", ["const:45bd90:8", "const:4:8"]]
- 0045bd90 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0047ec28 ["INT_ADD", "register:40f0:8", ["const:47ec28:8", "const:4:8"]]
+ 0047ec28 ["CALL", null, ["callee:00c57ab0:8"]]
- 0045bd90 bytes b4fc1d94
+ 0047ec28 bytes a2631f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-514cbc7efcea752317f9a7187e7ac8bd"></a>

### [`0045c7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c7fc.md) → [`0047f694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md) FUN_0047f694

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0045be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045be0c.md) · 呼出先 8件 [`0045c944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c944.md) [`0045caa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045caa4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0047eca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047eca4.md) · 呼出先 8件 [`0047f7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md) [`0047f93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f93c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.71% / 新版 88.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047f6d4",
      "incomplete_value": false,
      "site": "0047f6e0",
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
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c83c",
      "incomplete_value": false,
      "site": "0045c848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:538:8"
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
      "definition_site": "0047f708",
      "incomplete_value": true,
      "site": "0047f710",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c870",
      "incomplete_value": true,
      "site": "0045c878",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6b0:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047f73c",
      "value": [
        "leaf",
        "ram:c58120:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045c8a4",
      "value": [
        "leaf",
        "ram:bdb6d0:8"
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
      "0047f6e0",
      "DATA",
      [
        "storage",
        "00be8538",
        null,
        "pointer"
      ]
    ],
    [
      "0047f708",
      "READ",
      [
        "storage",
        "002b16b0",
        null,
        null
      ]
    ],
    [
      "0047f73c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb6d0"
      ]
    ]
  ],
  "added": [
    [
      "0047f6e0",
      "DATA",
      [
        "storage",
        "00c650f8",
        null,
        "pointer"
      ]
    ],
    [
      "0047f708",
      "READ",
      [
        "storage",
        "002c2d10",
        null,
        null
      ]
    ],
    [
      "0047f73c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58120"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c7fc.md#insn-0045c8a4) · [`0045c82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c7fc.md#insn-0045c82c) · [`0045c838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c7fc.md#insn-0045c838)
- 新版 [`0047f73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md#insn-0047f73c) · [`0047f6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md#insn-0047f6c4) · [`0047f6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md#insn-0047f6d0)

~~~diff
- 0045c8a4 ["INT_ADD", "register:40f0:8", ["const:45c8a4:8", "const:4:8"]]
- 0045c8a4 ["CALL", null, ["ram:bdb6d0:8"]]
+ 0047f73c ["INT_ADD", "register:40f0:8", ["const:47f73c:8", "const:4:8"]]
+ 0047f73c ["CALL", null, ["ram:c58120:8"]]
- 0045c8a4 bytes 8bfb1d94
+ 0047f73c bytes 79621f94
- 0045c82c ["INT_ADD", "register:40f0:8", ["const:45c82c:8", "const:4:8"]]
- 0045c82c ["CALL", null, ["callee:00c57a90:8"]]
+ 0047f6c4 ["INT_ADD", "register:40f0:8", ["const:47f6c4:8", "const:4:8"]]
+ 0047f6c4 ["CALL", null, ["callee:00c57a90:8"]]
- 0045c82c bytes 05fa1d94
+ 0047f6c4 bytes f3601f94
- 0045c838 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 0047f6d0 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0045c838 bytes 683c0090
+ 0047f6d0 bytes 283f00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08a0571191e797b674eb13ca9bb0b4c2"></a>

### [`0045c944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c944.md) → [`0047f7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md) FUN_0047f7dc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0045c7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c7fc.md) · 呼出先 6件 [`0045cd94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cd94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) [`00bdb2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2c0.md)
- 新版 呼出元 1件 [`0047f694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f694.md) · 呼出先 6件 [`0047fc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fc2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d00.md) [`00c57d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

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
      "definition_site": "0047f848",
      "incomplete_value": false,
      "site": "0047f854",
      "value": [
        "leaf",
        "const:47fc2c:8"
      ]
    },
    "old": {
      "definition_site": "0045c9b0",
      "incomplete_value": false,
      "site": "0045c9bc",
      "value": [
        "leaf",
        "const:45cd94:8"
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047f898",
      "incomplete_value": false,
      "site": "0047f89c",
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
    "old": {
      "definition_site": "0045ca00",
      "incomplete_value": false,
      "site": "0045ca04",
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
            "const:544:8"
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
      "0047f848",
      "PARAM",
      [
        "storage",
        "0045cd94",
        null,
        null
      ]
    ],
    [
      "0047f898",
      "PARAM",
      [
        "storage",
        "00294544",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047f848",
      "PARAM",
      [
        "storage",
        "0047fc2c",
        null,
        null
      ]
    ],
    [
      "0047f898",
      "PARAM",
      [
        "storage",
        "002a3e5a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c944.md#insn-0045c9bc) · [`0045ca04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c944.md#insn-0045ca04) · [`0045c978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c944.md#insn-0045c978)
- 新版 [`0047f854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md#insn-0047f854) · [`0047f89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md#insn-0047f89c) · [`0047f810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md#insn-0047f810)

~~~diff
- 0045c9bc ["INT_ADD", "register:40f0:8", ["const:45c9bc:8", "const:4:8"]]
- 0045c9bc ["CALL", null, ["callee:00c57d10:8"]]
+ 0047f854 ["INT_ADD", "register:40f0:8", ["const:47f854:8", "const:4:8"]]
+ 0047f854 ["CALL", null, ["callee:00c57d10:8"]]
- 0045c9bc bytes 41fa1d94
+ 0047f854 bytes 2f611f94
- 0045ca04 ["INT_ADD", "register:40f0:8", ["const:45ca04:8", "const:4:8"]]
- 0045ca04 ["CALL", null, ["callee:00c57d20:8"]]
+ 0047f89c ["INT_ADD", "register:40f0:8", ["const:47f89c:8", "const:4:8"]]
+ 0047f89c ["CALL", null, ["callee:00c57d20:8"]]
- 0045ca04 bytes 33fa1d94
+ 0047f89c bytes 21611f94
- 0045c978 ["INT_ADD", "register:40f0:8", ["const:45c978:8", "const:4:8"]]
- 0045c978 ["CALL", null, ["callee:00c57a90:8"]]
+ 0047f810 ["INT_ADD", "register:40f0:8", ["const:47f810:8", "const:4:8"]]
+ 0047f810 ["CALL", null, ["callee:00c57a90:8"]]
- 0045c978 bytes b2f91d94
+ 0047f810 bytes a0601f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-418f63da22e2bc304d62a8d9292865eb"></a>

### [`0045cacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cacc.md) → [`0047f964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f964.md) FUN_0047f964

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0045cb74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cb74.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb700.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047fa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fa0c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58150.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

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
      "site": "0047f988",
      "value": [
        "leaf",
        "ram:47fa0c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045caf0",
      "value": [
        "leaf",
        "ram:45cb74:8"
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
      "0047f988",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0045cb74"
      ]
    ]
  ],
  "added": [
    [
      "0047f988",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047fa0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045caf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cacc.md#insn-0045caf0) · [`0045caf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cacc.md#insn-0045caf8) · [`0045cb6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cacc.md#insn-0045cb6c)
- 新版 [`0047f988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f964.md#insn-0047f988) · [`0047f990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f964.md#insn-0047f990) · [`0047fa04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f964.md#insn-0047fa04)

~~~diff
- 0045caf0 ["INT_ADD", "register:40f0:8", ["const:45caf0:8", "const:4:8"]]
- 0045caf0 ["CALL", null, ["ram:45cb74:8"]]
+ 0047f988 ["INT_ADD", "register:40f0:8", ["const:47f988:8", "const:4:8"]]
+ 0047f988 ["CALL", null, ["ram:47fa0c:8"]]
- 0045caf0 bytes 21000094
+ 0047f988 bytes 21000094
- 0045caf8 ["INT_ADD", "register:40f0:8", ["const:45caf8:8", "const:4:8"]]
- 0045caf8 ["CALL", null, ["callee:00c58150:8"]]
+ 0047f990 ["INT_ADD", "register:40f0:8", ["const:47f990:8", "const:4:8"]]
+ 0047f990 ["CALL", null, ["callee:00c58150:8"]]
- 0045caf8 bytes 02fb1d94
+ 0047f990 bytes f0611f94
- 0045cb6c ["INT_ADD", "register:40f0:8", ["const:45cb6c:8", "const:4:8"]]
- 0045cb6c ["CALL", null, ["callee:00c57ae0:8"]]
+ 0047fa04 ["INT_ADD", "register:40f0:8", ["const:47fa04:8", "const:4:8"]]
+ 0047fa04 ["CALL", null, ["callee:00c57ae0:8"]]
- 0045cb6c bytes 49f91d94
+ 0047fa04 bytes 37601f94
~~~


<a id="compare-53cb7dd91e7c0b267de2b73e20cd1c71"></a>

### [`0045cd94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cd94.md) → [`0047fc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fc2c.md) FUN_0047fc2c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045c944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c944.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2e0.md) [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bdb300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb300.md)
- 新版 呼出元 1件 [`0047f7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047f7dc.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)

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
      "site": "0047fc94",
      "value": [
        "leaf",
        "ram:c57d50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045cdfc",
      "value": [
        "leaf",
        "ram:bdb300:8"
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
      "0047fc94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb300"
      ]
    ]
  ],
  "added": [
    [
      "0047fc94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57d50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cd94.md#insn-0045cdfc) · [`0045cdbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cd94.md#insn-0045cdbc) · [`0045cdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045cd94.md#insn-0045cdcc)
- 新版 [`0047fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fc2c.md#insn-0047fc94) · [`0047fc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fc2c.md#insn-0047fc54) · [`0047fc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fc2c.md#insn-0047fc64)

~~~diff
- 0045cdfc ["INT_ADD", "register:40f0:8", ["const:45cdfc:8", "const:4:8"]]
- 0045cdfc ["CALL", null, ["ram:bdb300:8"]]
+ 0047fc94 ["INT_ADD", "register:40f0:8", ["const:47fc94:8", "const:4:8"]]
+ 0047fc94 ["CALL", null, ["ram:c57d50:8"]]
- 0045cdfc bytes 41f91d94
+ 0047fc94 bytes 2f601f94
- 0045cdbc ["INT_ADD", "register:40f0:8", ["const:45cdbc:8", "const:4:8"]]
- 0045cdbc ["CALL", null, ["callee:00c57d30:8"]]
+ 0047fc54 ["INT_ADD", "register:40f0:8", ["const:47fc54:8", "const:4:8"]]
+ 0047fc54 ["CALL", null, ["callee:00c57d30:8"]]
- 0045cdbc bytes 49f91d94
+ 0047fc54 bytes 37601f94
- 0045cdcc ["INT_ADD", "register:40f0:8", ["const:45cdcc:8", "const:4:8"]]
- 0045cdcc ["CALL", null, ["callee:00c57d40:8"]]
+ 0047fc64 ["INT_ADD", "register:40f0:8", ["const:47fc64:8", "const:4:8"]]
+ 0047fc64 ["CALL", null, ["callee:00c57d40:8"]]
- 0045cdcc bytes 49f91d94
+ 0047fc64 bytes 37601f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8e8b61f990bb2bb2331de1e6404f03a"></a>

### [`0045ceb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045ceb0.md) → [`0047fd48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fd48.md) _INIT_17

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047fd84",
      "incomplete_value": true,
      "site": "0047fda0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0045ceec",
      "incomplete_value": true,
      "site": "0045cf08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
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
      "definition_site": "0047fda8",
      "incomplete_value": true,
      "site": "0047fdc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0045cf10",
      "incomplete_value": true,
      "site": "0045cf2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
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
      "definition_site": "0047fdc8",
      "incomplete_value": true,
      "site": "0047fde4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0045cf30",
      "incomplete_value": true,
      "site": "0045cf4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
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
      "0047fd84",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0047fda8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0047fdc8",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047fd84",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0047fda8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0047fdc8",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045ceb0.md#insn-0045d010) · [`0045d0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045ceb0.md#insn-0045d0e4) · [`0045ced8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045ceb0.md#insn-0045ced8)
- 新版 [`0047fea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fd48.md#insn-0047fea8) · [`0047ff7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fd48.md#insn-0047ff7c) · [`0047fd70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047f/0047fd48.md#insn-0047fd70)

~~~diff
- 0045d010 ["INT_ADD", "register:40f0:8", ["const:45d010:8", "const:4:8"]]
- 0045d010 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0047fea8 ["INT_ADD", "register:40f0:8", ["const:47fea8:8", "const:4:8"]]
+ 0047fea8 ["CALL", null, ["callee:0043b7b8:8"]]
- 0045d010 bytes 2aeffe97
+ 0047fea8 bytes 44eefe97
- 0045d0e4 ["INT_ADD", "register:40f0:8", ["const:45d0e4:8", "const:4:8"]]
- 0045d0e4 ["CALL", null, ["callee:00c57a30:8"]]
+ 0047ff7c ["INT_ADD", "register:40f0:8", ["const:47ff7c:8", "const:4:8"]]
+ 0047ff7c ["CALL", null, ["callee:00c57a30:8"]]
- 0045d0e4 bytes bff71d94
+ 0047ff7c bytes ad5e1f94
- 0045ced8 ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 0047fd70 ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 0045ced8 bytes 533e0090
+ 0047fd70 bytes 334100b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f557ff03f6609957a741f12e7049ec1"></a>

### [`0045e558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md) → [`004813f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md) FUN_004813f0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 18件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`0044e05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e05c.md) [`00611d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00611/00611d18.md) · 呼出先 0件 
- 新版 呼出元 18件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) [`00637810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/00637810.md) · 呼出先 0件 

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
      "definition_site": "00481404",
      "incomplete_value": false,
      "site": "00481408",
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
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e56c",
      "incomplete_value": false,
      "site": "0045e570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:580:8"
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
      "00481408",
      "DATA",
      [
        "storage",
        "00be8580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00481408",
      "DATA",
      [
        "storage",
        "00c65140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md#insn-0045e568) · [`0045e56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md#insn-0045e56c)
- 新版 [`00481400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md#insn-00481400) · [`00481404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md#insn-00481404)

~~~diff
- 0045e568 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00481400 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0045e568 bytes 483c00d0
+ 00481400 bytes 283f0090
- 0045e56c ["COPY", "tmp:0:8", ["const:580:8"]]
- 0045e56c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045e56c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045e56c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00481404 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 00481404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00481404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00481404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045e56c bytes 08011691
+ 00481404 bytes 08010591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ad83ff186f5d0ff06af6383c9ffa572"></a>

### [`0045e588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e588.md) → [`00481420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md) FUN_00481420

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0045fc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045fc34.md) [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`0083b3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b3f0.md) [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) [`0084e780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e780.md) · 呼出先 25件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`00462c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/00462c48.md)
- 新版 呼出元 7件 [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`0086d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d6dc.md) [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) · 呼出先 25件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00485ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00481af4",
      "incomplete_value": true,
      "site": "00481af4",
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
            "const:3414:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ec5c",
      "incomplete_value": true,
      "site": "0045ec5c",
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
            "const:3324:8"
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00481c74",
      "incomplete_value": true,
      "site": "00481c74",
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
            "const:3414:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045eddc",
      "incomplete_value": true,
      "site": "0045eddc",
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
            "const:3324:8"
          ]
        ]
      ]
    },
    "ordinal": 66,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00481ad0",
      "value": [
        "leaf",
        "ram:aa3264:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045ec38",
      "value": [
        "leaf",
        "ram:a45360:8"
      ]
    },
    "ordinal": 54,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00481ad0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a45360"
      ]
    ],
    [
      "00481c3c",
      "DATA",
      [
        "storage",
        "003c3408",
        null,
        "byte[59]"
      ]
    ],
    [
      "00481c58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a45360"
      ]
    ]
  ],
  "added": [
    [
      "00481ad0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00aa3264"
      ]
    ],
    [
      "00481c3c",
      "DATA",
      [
        "storage",
        "003c76e8",
        null,
        "dword"
      ]
    ],
    [
      "00481c58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00aa3264"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ec38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e588.md#insn-0045ec38) · [`0045ec5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e588.md#insn-0045ec5c) · [`0045edc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e588.md#insn-0045edc0)
- 新版 [`00481ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md#insn-00481ad0) · [`00481af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md#insn-00481af4) · [`00481c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md#insn-00481c58)

~~~diff
- 0045ec38 ["INT_ADD", "register:40f0:8", ["const:45ec38:8", "const:4:8"]]
- 0045ec38 ["CALL", null, ["ram:a45360:8"]]
+ 00481ad0 ["INT_ADD", "register:40f0:8", ["const:481ad0:8", "const:4:8"]]
+ 00481ad0 ["CALL", null, ["ram:aa3264:8"]]
- 0045ec38 bytes ca991794
+ 00481ad0 bytes e5851894
- 0045ec5c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3324:8"]]
- 0045ec5c ["COPY", "tmp:1:4", ["const:0:4"]]
- 0045ec5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
+ 00481af4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3414:8"]]
+ 00481af4 ["COPY", "tmp:1:4", ["const:0:4"]]
+ 00481af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 0045ec5c bytes 1f2433b9
+ 00481af4 bytes 1f1434b9
- 0045edc0 ["INT_ADD", "register:40f0:8", ["const:45edc0:8", "const:4:8"]]
- 0045edc0 ["CALL", null, ["ram:a45360:8"]]
+ 00481c58 ["INT_ADD", "register:40f0:8", ["const:481c58:8", "const:4:8"]]
+ 00481c58 ["CALL", null, ["ram:aa3264:8"]]
- 0045edc0 bytes 68991794
+ 00481c58 bytes 83851894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a59d38d47d367fe4edfd87b2540abe8"></a>

### [`0045f708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f708.md) → [`004825a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004825a0.md) FUN_004825a0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`00611d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00611/00611d18.md) [`0084e780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e780.md) [`00949ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00949/00949ed8.md) · 呼出先 11件 [`0053b998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b998.md) [`0053d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d580.md) [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 8件 [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00637810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/00637810.md) [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) [`0097f984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f984.md) · 呼出先 11件 [`0055e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e830.md) [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md) [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 98.95% / 新版 98.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004827c8",
      "incomplete_value": true,
      "site": "004827c8",
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
            "const:3414:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f930",
      "incomplete_value": true,
      "site": "0045f930",
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
            "const:3324:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004827ec",
      "incomplete_value": true,
      "site": "004827ec",
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
            "const:3414:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f954",
      "incomplete_value": true,
      "site": "0045f954",
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
            "const:3324:8"
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
      "definition_site": "0048286c",
      "incomplete_value": true,
      "site": "0048286c",
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
            "const:3414:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f9d4",
      "incomplete_value": true,
      "site": "0045f9d4",
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
            "const:3324:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0045f930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f708.md#insn-0045f930) · [`0045f954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f708.md#insn-0045f954) · [`0045f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f708.md#insn-0045f9d4)
- 新版 [`004827c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004825a0.md#insn-004827c8) · [`004827ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004825a0.md#insn-004827ec) · [`0048286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/004825a0.md#insn-0048286c)

~~~diff
- 0045f930 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3324:8"]]
- 0045f930 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 004827c8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3414:8"]]
+ 004827c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 0045f930 bytes 082433b9
+ 004827c8 bytes 081434b9
- 0045f954 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3324:8"]]
- 0045f954 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 004827ec ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3414:8"]]
+ 004827ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 0045f954 bytes 082433b9
+ 004827ec bytes 081434b9
- 0045f9d4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3324:8"]]
- 0045f9d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 0048286c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3414:8"]]
+ 0048286c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 0045f9d4 bytes 082433b9
+ 0048286c bytes 081434b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09efa2d1327f979cc89be555f26a60f3"></a>

### [`004609f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00460/004609f4.md) → [`0048388c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md) FUN_0048388c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) [`009c5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c5/009c5344.md) · 呼出先 18件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00463ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ef4.md) [`00463fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463fcc.md) [`00464250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464250.md) [`0052dd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd50.md)
- 新版 呼出元 2件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 18件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00486d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d8c.md) [`00486e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e64.md) [`004870e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004870e8.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.11% / 新版 97.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00483a80",
      "incomplete_value": false,
      "site": "00483a88",
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
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460be8",
      "incomplete_value": false,
      "site": "00460bf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "definition_site": "00483aa8",
      "incomplete_value": false,
      "site": "00483aa8",
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
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460c10",
      "incomplete_value": false,
      "site": "00460c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00483ad0",
      "incomplete_value": false,
      "site": "00483ae0",
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
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460c38",
      "incomplete_value": false,
      "site": "00460c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "00483a88",
      "DATA",
      [
        "storage",
        "00be8670",
        null,
        "pointer"
      ]
    ],
    [
      "00483aa8",
      "DATA",
      [
        "storage",
        "00be86c0",
        null,
        null
      ]
    ],
    [
      "00483ae0",
      "DATA",
      [
        "storage",
        "00be8700",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00483a88",
      "DATA",
      [
        "storage",
        "00c65230",
        null,
        "pointer"
      ]
    ],
    [
      "00483aa8",
      "DATA",
      [
        "storage",
        "00c65280",
        null,
        null
      ]
    ],
    [
      "00483ae0",
      "DATA",
      [
        "storage",
        "00c652c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00460/004609f4.md#insn-00460a28) · [`00460a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00460/004609f4.md#insn-00460a38) · [`00460a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00460/004609f4.md#insn-00460a48)
- 新版 [`004838c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md#insn-004838c0) · [`004838d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md#insn-004838d0) · [`004838e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md#insn-004838e0)

~~~diff
- 00460a28 ["INT_ADD", "register:40f0:8", ["const:460a28:8", "const:4:8"]]
- 00460a28 ["CALL", null, ["callee:00550be8:8"]]
+ 004838c0 ["INT_ADD", "register:40f0:8", ["const:4838c0:8", "const:4:8"]]
+ 004838c0 ["CALL", null, ["callee:00550be8:8"]]
- 00460a28 bytes ca340394
+ 004838c0 bytes ca340394
- 00460a38 ["INT_ADD", "register:40f0:8", ["const:460a38:8", "const:4:8"]]
- 00460a38 ["CALL", null, ["callee:0043db64:8"]]
+ 004838d0 ["INT_ADD", "register:40f0:8", ["const:4838d0:8", "const:4:8"]]
+ 004838d0 ["CALL", null, ["callee:0043db64:8"]]
- 00460a38 bytes 8be9fe97
+ 004838d0 bytes a5e8fe97
- 00460a48 ["INT_ADD", "register:40f0:8", ["const:460a48:8", "const:4:8"]]
- 00460a48 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004838e0 ["INT_ADD", "register:40f0:8", ["const:4838e0:8", "const:4:8"]]
+ 004838e0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00460a48 bytes 86e91d94
+ 004838e0 bytes 74501f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf2f37d9ab292a23403b337e59ad2487"></a>

### [`004618e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/004618e8.md) → [`00484780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md) FUN_00484780

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00840274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840274.md) [`0099fe4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099f/0099fe4c.md) [`009a3a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a3/009a3a30.md) [`00a5a6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a6f0.md) · 呼出先 14件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0044df7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044df7c.md) [`0044e84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e84c.md) [`0044ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ea58.md) [`0045f0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f0ac.md)
- 新版 呼出元 4件 [`00872560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872560.md) [`009d5b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d5b5c.md) [`009d9790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d9/009d9790.md) [`00ab86a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab86a8.md) · 呼出先 14件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00470e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470e14.md) [`004716e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004716e4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) [`00481f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481f44.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.23% / 新版 98.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00484838",
      "incomplete_value": false,
      "site": "00484844",
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
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004619a0",
      "incomplete_value": false,
      "site": "004619ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:580:8"
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
      "site": "004847b0",
      "value": [
        "leaf",
        "ram:470e14:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00461918",
      "value": [
        "leaf",
        "ram:44df7c:8"
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
      "site": "0048490c",
      "value": [
        "leaf",
        "ram:482acc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00461a74",
      "value": [
        "leaf",
        "ram:45fc34:8"
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
      "004847b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044df7c"
      ]
    ],
    [
      "00484844",
      "DATA",
      [
        "storage",
        "00be8580",
        null,
        "undefined *"
      ]
    ],
    [
      "004848cc",
      "DATA",
      [
        "storage",
        "00be8580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004847b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e14"
      ]
    ],
    [
      "00484844",
      "DATA",
      [
        "storage",
        "00c65140",
        null,
        "undefined *"
      ]
    ],
    [
      "004848cc",
      "DATA",
      [
        "storage",
        "00c65140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00461918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/004618e8.md#insn-00461918) · [`00461a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/004618e8.md#insn-00461a74) · [`00461b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/004618e8.md#insn-00461b74)
- 新版 [`004847b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md#insn-004847b0) · [`0048490c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md#insn-0048490c) · [`00484a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md#insn-00484a0c)

~~~diff
- 00461918 ["INT_ADD", "register:40f0:8", ["const:461918:8", "const:4:8"]]
- 00461918 ["CALL", null, ["ram:44df7c:8"]]
+ 004847b0 ["INT_ADD", "register:40f0:8", ["const:4847b0:8", "const:4:8"]]
+ 004847b0 ["CALL", null, ["ram:470e14:8"]]
- 00461918 bytes 99b1ff97
+ 004847b0 bytes 99b1ff97
- 00461a74 ["INT_ADD", "register:40f0:8", ["const:461a74:8", "const:4:8"]]
- 00461a74 ["CALL", null, ["ram:45fc34:8"]]
+ 0048490c ["INT_ADD", "register:40f0:8", ["const:48490c:8", "const:4:8"]]
+ 0048490c ["CALL", null, ["ram:482acc:8"]]
- 00461a74 bytes 70f8ff97
+ 0048490c bytes 70f8ff97
- 00461b74 ["INT_ADD", "register:40f0:8", ["const:461b74:8", "const:4:8"]]
- 00461b74 ["CALL", null, ["ram:44df7c:8"]]
+ 00484a0c ["INT_ADD", "register:40f0:8", ["const:484a0c:8", "const:4:8"]]
+ 00484a0c ["CALL", null, ["ram:470e14:8"]]
- 00461b74 bytes 02b1ff97
+ 00484a0c bytes 02b1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ab5bd731355ccc5746132fa592b28cc"></a>

### [`00461e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/00461e04.md) → [`00484c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484c9c.md) FUN_00484c9c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) [`009b79f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009b7/009b79f4.md) · 呼出先 4件 [`00574738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574738.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`00a148e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a14/00a148e4.md) · 呼出先 4件 [`005975d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00484cd0",
      "incomplete_value": false,
      "site": "00484cd8",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00461e38",
      "incomplete_value": false,
      "site": "00461e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "00484cd8",
      "DATA",
      [
        "storage",
        "00be85d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00484cd8",
      "DATA",
      [
        "storage",
        "00c65198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00461e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/00461e04.md#insn-00461e34) · [`00461e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/00461e04.md#insn-00461e38) · [`00461e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/00461e04.md#insn-00461e54)
- 新版 [`00484ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484c9c.md#insn-00484ccc) · [`00484cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484c9c.md#insn-00484cd0) · [`00484cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484c9c.md#insn-00484cec)

~~~diff
- 00461e34 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00484ccc ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00461e34 bytes 283c00f0
+ 00484ccc bytes 083f00b0
- 00461e38 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00461e38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00461e38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00461e38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00484cd0 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00484cd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00484cd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00484cd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00461e38 bytes 08611791
+ 00484cd0 bytes 08610691
- 00461e54 ["INT_ADD", "register:40f0:8", ["const:461e54:8", "const:4:8"]]
- 00461e54 ["CALL", null, ["callee:005975d0:8"]]
+ 00484cec ["INT_ADD", "register:40f0:8", ["const:484cec:8", "const:4:8"]]
+ 00484cec ["CALL", null, ["callee:005975d0:8"]]
- 00461e54 bytes 394a0494
+ 00484cec bytes 394a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b561aac8ae18dad05b6688326b08932"></a>

### [`004624d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/004624d8.md) → [`00485370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485370.md) FUN_00485370

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00462748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/00462748.md) · 呼出先 8件 [`0053b998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b998.md) [`0053d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d580.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`004855e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/004855e0.md) · 呼出先 8件 [`0055e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e830.md) [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.24% / 新版 99.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048554c",
      "incomplete_value": false,
      "site": "00485554",
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
            "const:30e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004626b4",
      "incomplete_value": false,
      "site": "004626bc",
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
            "const:7d9:8"
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
      "0048554c",
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
      "0048554c",
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

- 旧版 [`004626bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/004624d8.md#insn-004626bc) · [`00462528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/004624d8.md#insn-00462528) · [`00462540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/004624d8.md#insn-00462540)
- 新版 [`00485554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485370.md#insn-00485554) · [`004853c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485370.md#insn-004853c0) · [`004853d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485370.md#insn-004853d8)

~~~diff
- 004626bc ["INT_ADD", "register:40f0:8", ["const:4626bc:8", "const:4:8"]]
- 004626bc ["CALL", null, ["callee:00c57d90:8"]]
+ 00485554 ["INT_ADD", "register:40f0:8", ["const:485554:8", "const:4:8"]]
+ 00485554 ["CALL", null, ["callee:00c57d90:8"]]
- 004626bc bytes 21e31d94
+ 00485554 bytes 0f4a1f94
- 00462528 ["INT_ADD", "register:40f0:8", ["const:462528:8", "const:4:8"]]
- 00462528 ["CALL", null, ["callee:0055e830:8"]]
+ 004853c0 ["INT_ADD", "register:40f0:8", ["const:4853c0:8", "const:4:8"]]
+ 004853c0 ["CALL", null, ["callee:0055e830:8"]]
- 00462528 bytes 1c650394
+ 004853c0 bytes 1c650394
- 00462540 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462540 ["INT_ADD", "register:40f0:8", ["const:462540:8", "const:4:8"]]
- 00462540 ["CALLIND", null, ["register:0:8"]]
+ 004853d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004853d8 ["INT_ADD", "register:40f0:8", ["const:4853d8:8", "const:4:8"]]
+ 004853d8 ["CALLIND", null, ["register:0:8"]]
- 00462540 bytes 20013fd6
+ 004853d8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eea7a560f3e6083d2d09a610b67d7fb4"></a>

### [`00462c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/00462c48.md) → [`00485ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md) FUN_00485ae0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0045e588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e588.md) [`00462c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/00462c48.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00481420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481420.md) [`00485ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00485c38",
      "incomplete_value": false,
      "site": "00485c40",
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
    "old": {
      "definition_site": "00462da0",
      "incomplete_value": false,
      "site": "00462da8",
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
            "const:3a4:8"
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
      "definition_site": "00485cf4",
      "incomplete_value": false,
      "site": "00485cfc",
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
    "old": {
      "definition_site": "00462e5c",
      "incomplete_value": false,
      "site": "00462e64",
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
            "const:379:8"
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
      "definition_site": "00485d0c",
      "incomplete_value": false,
      "site": "00485d18",
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
    "old": {
      "definition_site": "00462e74",
      "incomplete_value": false,
      "site": "00462e80",
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
            "const:885:8"
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
      "00485c38",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00485cf4",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00485d0c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00485c38",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00485cf4",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "00485d0c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/00462c48.md#insn-00462da8) · [`00462e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/00462c48.md#insn-00462e64) · [`00462e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/00462c48.md#insn-00462e80)
- 新版 [`00485c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md#insn-00485c40) · [`00485cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md#insn-00485cfc) · [`00485d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md#insn-00485d18)

~~~diff
- 00462da8 ["INT_ADD", "register:40f0:8", ["const:462da8:8", "const:4:8"]]
- 00462da8 ["CALL", null, ["callee:00441e54:8"]]
+ 00485c40 ["INT_ADD", "register:40f0:8", ["const:485c40:8", "const:4:8"]]
+ 00485c40 ["CALL", null, ["callee:00441e54:8"]]
- 00462da8 bytes 6bf1fe97
+ 00485c40 bytes 85f0fe97
- 00462e64 ["INT_ADD", "register:40f0:8", ["const:462e64:8", "const:4:8"]]
- 00462e64 ["CALL", null, ["callee:00441e54:8"]]
+ 00485cfc ["INT_ADD", "register:40f0:8", ["const:485cfc:8", "const:4:8"]]
+ 00485cfc ["CALL", null, ["callee:00441e54:8"]]
- 00462e64 bytes 3cf1fe97
+ 00485cfc bytes 56f0fe97
- 00462e80 ["INT_ADD", "register:40f0:8", ["const:462e80:8", "const:4:8"]]
- 00462e80 ["CALL", null, ["callee:004427b4:8"]]
+ 00485d18 ["INT_ADD", "register:40f0:8", ["const:485d18:8", "const:4:8"]]
+ 00485d18 ["CALL", null, ["callee:004427b4:8"]]
- 00462e80 bytes 8df3fe97
+ 00485d18 bytes a7f2fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec80eda5a98001b65899d7ec6e9b80c7"></a>

### [`00463580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463580.md) → [`00486418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486418.md) FUN_00486418

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00462c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/00462c48.md) [`00463580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463580.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00485ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/00485ae0.md) [`00486418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486418.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00486568",
      "incomplete_value": false,
      "site": "00486570",
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
    "old": {
      "definition_site": "004636d0",
      "incomplete_value": false,
      "site": "004636d8",
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
            "const:3a4:8"
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
      "definition_site": "00486624",
      "incomplete_value": false,
      "site": "0048662c",
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
    "old": {
      "definition_site": "0046378c",
      "incomplete_value": false,
      "site": "00463794",
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
            "const:379:8"
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
      "definition_site": "0048663c",
      "incomplete_value": false,
      "site": "00486648",
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
    "old": {
      "definition_site": "004637a4",
      "incomplete_value": false,
      "site": "004637b0",
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
            "const:885:8"
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
      "00486568",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00486624",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "0048663c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00486568",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00486624",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0048663c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004636d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463580.md#insn-004636d8) · [`00463794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463580.md#insn-00463794) · [`004637b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463580.md#insn-004637b0)
- 新版 [`00486570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486418.md#insn-00486570) · [`0048662c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486418.md#insn-0048662c) · [`00486648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486418.md#insn-00486648)

~~~diff
- 004636d8 ["INT_ADD", "register:40f0:8", ["const:4636d8:8", "const:4:8"]]
- 004636d8 ["CALL", null, ["callee:00441e54:8"]]
+ 00486570 ["INT_ADD", "register:40f0:8", ["const:486570:8", "const:4:8"]]
+ 00486570 ["CALL", null, ["callee:00441e54:8"]]
- 004636d8 bytes 1feffe97
+ 00486570 bytes 39eefe97
- 00463794 ["INT_ADD", "register:40f0:8", ["const:463794:8", "const:4:8"]]
- 00463794 ["CALL", null, ["callee:00441e54:8"]]
+ 0048662c ["INT_ADD", "register:40f0:8", ["const:48662c:8", "const:4:8"]]
+ 0048662c ["CALL", null, ["callee:00441e54:8"]]
- 00463794 bytes f0eefe97
+ 0048662c bytes 0aeefe97
- 004637b0 ["INT_ADD", "register:40f0:8", ["const:4637b0:8", "const:4:8"]]
- 004637b0 ["CALL", null, ["callee:004427b4:8"]]
+ 00486648 ["INT_ADD", "register:40f0:8", ["const:486648:8", "const:4:8"]]
+ 00486648 ["CALL", null, ["callee:004427b4:8"]]
- 004637b0 bytes 41f1fe97
+ 00486648 bytes 5bf0fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c9fa05c214e770a539a0c503776026c"></a>

### [`00463ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ea0.md) → [`00486d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d38.md) FUN_00486d38

採用 · 移動量 `+0x22e98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0045fc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045fc34.md) [`004e548c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e548c.md) [`0086a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) [`00a09968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09968.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 4件 [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) [`00508324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508324.md) [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) [`00a67638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67638.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "00486d48",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00463eb0",
      "value": [
        "leaf",
        "ram:41fdf0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00486d44",
      "incomplete_value": false,
      "site": "00486d48",
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
      "definition_site": "00463eac",
      "incomplete_value": false,
      "site": "00463eb0",
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
      "00486d44",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00486d48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00486d44",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00486d48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ea0.md#insn-00463eb0) · [`00463ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ea0.md#insn-00463ea8) · [`00463eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ea0.md#insn-00463eac)
- 新版 [`00486d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d38.md#insn-00486d48) · [`00486d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d38.md#insn-00486d40) · [`00486d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d38.md#insn-00486d44)

~~~diff
- 00463eb0 ["INT_ADD", "register:40f0:8", ["const:463eb0:8", "const:4:8"]]
- 00463eb0 ["CALL", null, ["ram:41fdf0:8"]]
+ 00486d48 ["INT_ADD", "register:40f0:8", ["const:486d48:8", "const:4:8"]]
+ 00486d48 ["CALL", null, ["ram:4428f0:8"]]
- 00463eb0 bytes d0effe97
+ 00486d48 bytes eaeefe97
- 00463ea8 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00486d40 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00463ea8 bytes 20f2ff90
+ 00486d40 bytes 80f1ffb0
- 00463eac ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00463eac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00463eac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00463eac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00486d44 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00486d44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00486d44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00486d44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00463eac bytes 00740e91
+ 00486d44 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dbda5a1dc04099df6aaf3bbf1e0e2de"></a>

### [`00463ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ef4.md) → [`00486d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d8c.md) FUN_00486d8c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004609f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00460/004609f4.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0048388c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "00486da0",
      "incomplete_value": false,
      "site": "00486da4",
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
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463f08",
      "incomplete_value": false,
      "site": "00463f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "00486da4",
      "DATA",
      [
        "storage",
        "00be86c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00486da4",
      "DATA",
      [
        "storage",
        "00c65280",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ef4.md#insn-00463f04) · [`00463f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ef4.md#insn-00463f08) · [`00463f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463ef4.md#insn-00463f1c)
- 新版 [`00486d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d8c.md#insn-00486d9c) · [`00486da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d8c.md#insn-00486da0) · [`00486db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d8c.md#insn-00486db4)

~~~diff
- 00463f04 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00486d9c ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00463f04 bytes 283c00b0
+ 00486d9c bytes e83e00f0
- 00463f08 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00463f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486da0 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 00486da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463f08 bytes 08011b91
+ 00486da0 bytes 08010a91
- 00463f1c ["INT_ADD", "register:40f0:8", ["const:463f1c:8", "const:4:8"]]
- 00463f1c ["CALL", null, ["callee:00c538e0:8"]]
+ 00486db4 ["INT_ADD", "register:40f0:8", ["const:486db4:8", "const:4:8"]]
+ 00486db4 ["CALL", null, ["callee:00c538e0:8"]]
- 00463f1c bytes ddcb1d94
+ 00486db4 bytes cb321f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64f5b62ecd23a6e0ff54e732b566aa94"></a>

### [`00463fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463fcc.md) → [`00486e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e64.md) FUN_00486e64

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004609f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00460/004609f4.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0048388c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00486e7c",
      "incomplete_value": false,
      "site": "00486e80",
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
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463fe4",
      "incomplete_value": false,
      "site": "00463fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00486eb8",
      "incomplete_value": false,
      "site": "00486ebc",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464020",
      "incomplete_value": false,
      "site": "00464024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "00486e80",
      "DATA",
      [
        "storage",
        "00be8750",
        null,
        null
      ]
    ],
    [
      "00486ebc",
      "DATA",
      [
        "storage",
        "00be8798",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00486e80",
      "DATA",
      [
        "storage",
        "00c65310",
        null,
        null
      ]
    ],
    [
      "00486ebc",
      "DATA",
      [
        "storage",
        "00c65358",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463fcc.md#insn-00463fe0) · [`00463fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463fcc.md#insn-00463fe4) · [`00463ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00463/00463fcc.md#insn-00463ff8)
- 新版 [`00486e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e64.md#insn-00486e78) · [`00486e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e64.md#insn-00486e7c) · [`00486e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486e64.md#insn-00486e90)

~~~diff
- 00463fe0 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00486e78 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00463fe0 bytes 283c00b0
+ 00486e78 bytes e83e00f0
- 00463fe4 ["COPY", "tmp:0:8", ["const:750:8"]]
- 00463fe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463fe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463fe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486e7c ["COPY", "tmp:0:8", ["const:310:8"]]
+ 00486e7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486e7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486e7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463fe4 bytes 08411d91
+ 00486e7c bytes 08410c91
- 00463ff8 ["INT_ADD", "register:40f0:8", ["const:463ff8:8", "const:4:8"]]
- 00463ff8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00486e90 ["INT_ADD", "register:40f0:8", ["const:486e90:8", "const:4:8"]]
+ 00486e90 ["CALL", null, ["callee:00c538e0:8"]]
- 00463ff8 bytes a6cb1d94
+ 00486e90 bytes 94321f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aeeff10357f18c6852996e0c15b6f22"></a>

### [`00464250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464250.md) → [`004870e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004870e8.md) FUN_004870e8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004609f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00460/004609f4.md) · 呼出先 5件 [`0052dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0048388c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00483/0048388c.md) · 呼出先 5件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00487128",
      "incomplete_value": false,
      "site": "0048712c",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464290",
      "incomplete_value": false,
      "site": "00464294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "definition_site": "0048713c",
      "incomplete_value": false,
      "site": "0048713c",
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
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004642a4",
      "incomplete_value": false,
      "site": "004642a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "definition_site": "0048715c",
      "incomplete_value": false,
      "site": "00487160",
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
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004642c4",
      "incomplete_value": false,
      "site": "004642c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "0048712c",
      "DATA",
      [
        "storage",
        "00be87b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0048713c",
      "DATA",
      [
        "storage",
        "00be8840",
        null,
        "pointer"
      ]
    ],
    [
      "00487160",
      "DATA",
      [
        "storage",
        "00be8800",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0048712c",
      "DATA",
      [
        "storage",
        "00c65370",
        null,
        "undefined *"
      ]
    ],
    [
      "0048713c",
      "DATA",
      [
        "storage",
        "00c65400",
        null,
        "pointer"
      ]
    ],
    [
      "00487160",
      "DATA",
      [
        "storage",
        "00c653c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046427c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464250.md#insn-0046427c) · [`00464280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464250.md#insn-00464280) · [`0046428c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464250.md#insn-0046428c)
- 新版 [`00487114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004870e8.md#insn-00487114) · [`00487118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004870e8.md#insn-00487118) · [`00487124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004870e8.md#insn-00487124)

~~~diff
- 0046427c ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 00487114 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0046427c bytes 293c0090
+ 00487114 bytes e93e00d0
- 00464280 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00464280 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00464280 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00464280 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00487118 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 00487118 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00487118 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00487118 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00464280 bytes 29012191
+ 00487118 bytes 29011091
- 0046428c ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00487124 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0046428c bytes 283c0090
+ 00487124 bytes e83e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b9d10f3e600b8239b14a3704b01a333"></a>

### [`004643cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/004643cc.md) → [`00487264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487264.md) FUN_00487264

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0048727c",
      "incomplete_value": false,
      "site": "00487280",
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
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004643e4",
      "incomplete_value": false,
      "site": "004643e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004872b8",
      "incomplete_value": false,
      "site": "004872bc",
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
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464420",
      "incomplete_value": false,
      "site": "00464424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "00487280",
      "DATA",
      [
        "storage",
        "00be8800",
        null,
        null
      ]
    ],
    [
      "004872bc",
      "DATA",
      [
        "storage",
        "00be8840",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00487280",
      "DATA",
      [
        "storage",
        "00c653c0",
        null,
        null
      ]
    ],
    [
      "004872bc",
      "DATA",
      [
        "storage",
        "00c65400",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004643e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/004643cc.md#insn-004643e0) · [`004643e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/004643cc.md#insn-004643e4) · [`004643f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/004643cc.md#insn-004643f8)
- 新版 [`00487278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487264.md#insn-00487278) · [`0048727c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487264.md#insn-0048727c) · [`00487290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487264.md#insn-00487290)

~~~diff
- 004643e0 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00487278 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 004643e0 bytes 283c0090
+ 00487278 bytes e83e00d0
- 004643e4 ["COPY", "tmp:0:8", ["const:800:8"]]
- 004643e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004643e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004643e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0048727c ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 0048727c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0048727c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0048727c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004643e4 bytes 08012091
+ 0048727c bytes 08010f91
- 004643f8 ["INT_ADD", "register:40f0:8", ["const:4643f8:8", "const:4:8"]]
- 004643f8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00487290 ["INT_ADD", "register:40f0:8", ["const:487290:8", "const:4:8"]]
+ 00487290 ["CALL", null, ["callee:00c538e0:8"]]
- 004643f8 bytes a6ca1d94
+ 00487290 bytes 94311f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cfd2574ca9bb8e0e670ba06f6f40009"></a>

### [`0046446c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/0046446c.md) → [`00487304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487304.md) FUN_00487304

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "00487318",
      "incomplete_value": false,
      "site": "0048731c",
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
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464480",
      "incomplete_value": false,
      "site": "00464484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "0048731c",
      "DATA",
      [
        "storage",
        "00be8840",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048731c",
      "DATA",
      [
        "storage",
        "00c65400",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046447c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/0046446c.md#insn-0046447c) · [`00464480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/0046446c.md#insn-00464480) · [`00464494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/0046446c.md#insn-00464494)
- 新版 [`00487314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487304.md#insn-00487314) · [`00487318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487304.md#insn-00487318) · [`0048732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487304.md#insn-0048732c)

~~~diff
- 0046447c ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00487314 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0046447c bytes 283c0090
+ 00487314 bytes e83e00d0
- 00464480 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00464480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00464480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00464480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00487318 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 00487318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00487318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00487318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00464480 bytes 08012191
+ 00487318 bytes 08011091
- 00464494 ["INT_ADD", "register:40f0:8", ["const:464494:8", "const:4:8"]]
- 00464494 ["CALL", null, ["callee:00c538e0:8"]]
+ 0048732c ["INT_ADD", "register:40f0:8", ["const:48732c:8", "const:4:8"]]
+ 0048732c ["CALL", null, ["callee:00c538e0:8"]]
- 00464494 bytes 7fca1d94
+ 0048732c bytes 6d311f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ceb8d618980c3ee3c6c516165f81a84"></a>

### [`004646b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/004646b4.md) → [`0048754c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048754c.md) _INIT_18

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00487588",
      "incomplete_value": true,
      "site": "004875a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "004646f0",
      "incomplete_value": true,
      "site": "0046470c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
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
      "definition_site": "004875ac",
      "incomplete_value": true,
      "site": "004875c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00464714",
      "incomplete_value": true,
      "site": "00464730",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
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
      "definition_site": "004875cc",
      "incomplete_value": true,
      "site": "004875e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00464734",
      "incomplete_value": true,
      "site": "00464750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
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
      "00487588",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "004875ac",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "004875cc",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00487588",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "004875ac",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "004875cc",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/004646b4.md#insn-00464814) · [`004648e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/004646b4.md#insn-004648e8) · [`004646dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/004646b4.md#insn-004646dc)
- 新版 [`004876ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048754c.md#insn-004876ac) · [`00487780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048754c.md#insn-00487780) · [`00487574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048754c.md#insn-00487574)

~~~diff
- 00464814 ["INT_ADD", "register:40f0:8", ["const:464814:8", "const:4:8"]]
- 00464814 ["CALL", null, ["callee:0043b7b8:8"]]
+ 004876ac ["INT_ADD", "register:40f0:8", ["const:4876ac:8", "const:4:8"]]
+ 004876ac ["CALL", null, ["callee:0043b7b8:8"]]
- 00464814 bytes 29d1fe97
+ 004876ac bytes 43d0fe97
- 004648e8 ["INT_ADD", "register:40f0:8", ["const:4648e8:8", "const:4:8"]]
- 004648e8 ["CALL", null, ["callee:00c57a30:8"]]
+ 00487780 ["INT_ADD", "register:40f0:8", ["const:487780:8", "const:4:8"]]
+ 00487780 ["CALL", null, ["callee:00c57a30:8"]]
- 004648e8 bytes bed91d94
+ 00487780 bytes ac401f94
- 004646dc ["COPY", "register:4098:8", ["const:c25000:8"]]
+ 00487574 ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 004646dc bytes 133e00b0
+ 00487574 bytes f34000b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e32dbd860b01a8cde66f56328469fcbb"></a>

### [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) → [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) FUN_00487de0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 144件 [`0041ac3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) [`00422098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/00422098.md) [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`0044a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a248.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) · 呼出先 2件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3a0.md)
- 新版 呼出元 153件 [`0043d73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`00444b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`0046d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) · 呼出先 2件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 68.33% / 新版 68.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00487e30",
      "incomplete_value": true,
      "site": "00487e30",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00464f98",
      "incomplete_value": true,
      "site": "00464f98",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00487e10",
      "incomplete_value": false,
      "site": "00487e38",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464f78",
      "incomplete_value": false,
      "site": "00464fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "definition_site": "00487e3c",
      "incomplete_value": true,
      "site": "00487e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00464fa4",
      "incomplete_value": true,
      "site": "00464fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00487e04",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00487e08",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "00487e1c",
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
      "00487e04",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00487e08",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "00487e1c",
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

- 旧版 [`00464f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md#insn-00464f60) · [`00464f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md#insn-00464f68) · [`00464f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md#insn-00464f6c)
- 新版 [`00487df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md#insn-00487df8) · [`00487e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md#insn-00487e00) · [`00487e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md#insn-00487e04)

~~~diff
- 00464f60 ["COPY", "register:40c0:8", ["const:c1a000:8"]]
+ 00487df8 ["COPY", "register:40c0:8", ["const:c9a000:8"]]
- 00464f60 bytes b83d00d0
+ 00487df8 bytes 984000f0
- 00464f68 ["COPY", "register:40c8:8", ["const:c1a000:8"]]
+ 00487e00 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
- 00464f68 bytes b93d00d0
+ 00487e00 bytes 994000f0
- 00464f6c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:dc8:8"]]
- 00464f6c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00487e04 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:7b8:8"]]
+ 00487e04 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00464f6c bytes 18e746f9
+ 00487e04 bytes 18df43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dda25614df0c38d9ca499342cb3eabb6"></a>

### [`004657b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004657b8.md) → [`00488650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488650.md) FUN_00488650

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00ab1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md) · 呼出先 1件 [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md) · 呼出先 1件 [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)

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
      "definition_site": "00488668",
      "incomplete_value": false,
      "site": "00488670",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004657d0",
      "incomplete_value": false,
      "site": "004657d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
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
      "00488670",
      "DATA",
      [
        "storage",
        "00be88b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00488670",
      "DATA",
      [
        "storage",
        "00c65478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004657c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004657b8.md#insn-004657c8) · [`004657cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004657b8.md#insn-004657cc) · [`004657d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004657b8.md#insn-004657d0)
- 新版 [`00488660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488650.md#insn-00488660) · [`00488664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488650.md#insn-00488664) · [`00488668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488650.md#insn-00488668)

~~~diff
- 004657c8 ["INT_ADD", "register:40f0:8", ["const:4657c8:8", "const:4:8"]]
- 004657c8 ["CALL", null, ["callee:00487de0:8"]]
+ 00488660 ["INT_ADD", "register:40f0:8", ["const:488660:8", "const:4:8"]]
+ 00488660 ["CALL", null, ["callee:00487de0:8"]]
- 004657c8 bytes e0fdff97
+ 00488660 bytes e0fdff97
- 004657cc ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00488664 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 004657cc bytes 083c00f0
+ 00488664 bytes e83e00b0
- 004657d0 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 004657d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004657d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004657d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00488668 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00488668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00488668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00488668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004657d0 bytes 08e12291
+ 00488668 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ad9f03f0651ed0c000352fa23ac86b2"></a>

### [`004658b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004658b8.md) → [`00488750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md) FUN_00488750

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00422098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/00422098.md) [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`005be404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) · 呼出先 14件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0044df7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044df7c.md) [`0044e84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e84c.md) [`0044ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ea58.md) [`0046517c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/0046517c.md)
- 新版 呼出元 3件 [`00444b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) · 呼出先 14件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00470e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470e14.md) [`004716e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004716e4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) [`00488014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488014.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004888f0",
      "incomplete_value": true,
      "site": "004888f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465a58",
      "incomplete_value": true,
      "site": "00465a58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c5:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00488780",
      "value": [
        "leaf",
        "ram:470e14:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004658e8",
      "value": [
        "leaf",
        "ram:44df7c:8"
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
      "site": "00488864",
      "value": [
        "leaf",
        "ram:470e14:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004659cc",
      "value": [
        "leaf",
        "ram:44df7c:8"
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
      "00488780",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044df7c"
      ]
    ],
    [
      "00488864",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044df7c"
      ]
    ],
    [
      "004888d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ]
  ],
  "added": [
    [
      "00488780",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e14"
      ]
    ],
    [
      "00488864",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e14"
      ]
    ],
    [
      "004888d0",
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

- 旧版 [`004658e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004658b8.md#insn-004658e8) · [`004659cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004658b8.md#insn-004659cc) · [`00465a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004658b8.md#insn-00465a38)
- 新版 [`00488780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md#insn-00488780) · [`00488864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md#insn-00488864) · [`004888d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md#insn-004888d0)

~~~diff
- 004658e8 ["INT_ADD", "register:40f0:8", ["const:4658e8:8", "const:4:8"]]
- 004658e8 ["CALL", null, ["ram:44df7c:8"]]
+ 00488780 ["INT_ADD", "register:40f0:8", ["const:488780:8", "const:4:8"]]
+ 00488780 ["CALL", null, ["ram:470e14:8"]]
- 004658e8 bytes a5a1ff97
+ 00488780 bytes a5a1ff97
- 004659cc ["INT_ADD", "register:40f0:8", ["const:4659cc:8", "const:4:8"]]
- 004659cc ["CALL", null, ["ram:44df7c:8"]]
+ 00488864 ["INT_ADD", "register:40f0:8", ["const:488864:8", "const:4:8"]]
+ 00488864 ["CALL", null, ["ram:470e14:8"]]
- 004659cc bytes 6ca1ff97
+ 00488864 bytes 6ca1ff97
- 00465a38 ["INT_ADD", "register:40f0:8", ["const:465a38:8", "const:4:8"]]
- 00465a38 ["CALL", null, ["ram:469e20:8"]]
+ 004888d0 ["INT_ADD", "register:40f0:8", ["const:4888d0:8", "const:4:8"]]
+ 004888d0 ["CALL", null, ["ram:48ccb8:8"]]
- 00465a38 bytes fa100094
+ 004888d0 bytes fa100094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a34852b517e55266e275f2862bb16fad"></a>

### [`00465d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465d3c.md) → [`00488bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488bd4.md) FUN_00488bd4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00488bec",
      "incomplete_value": false,
      "site": "00488bf8",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465d54",
      "incomplete_value": false,
      "site": "00465d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "definition_site": "00488c0c",
      "incomplete_value": true,
      "site": "00488c0c",
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
      "definition_site": "00465d74",
      "incomplete_value": true,
      "site": "00465d74",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00488c1c",
      "incomplete_value": true,
      "site": "00488c1c",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "00465d84",
      "incomplete_value": true,
      "site": "00465d84",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "00488bf0",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00488bf8",
      "DATA",
      [
        "storage",
        "00be8858",
        null,
        "undefined *"
      ]
    ],
    [
      "00488c04",
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
      "00488bf0",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00488bf8",
      "DATA",
      [
        "storage",
        "00c65418",
        null,
        "undefined *"
      ]
    ],
    [
      "00488c04",
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

- 旧版 [`00465d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465d3c.md#insn-00465d4c) · [`00465d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465d3c.md#insn-00465d50) · [`00465d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465d3c.md#insn-00465d54)
- 新版 [`00488be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488bd4.md#insn-00488be4) · [`00488be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488bd4.md#insn-00488be8) · [`00488bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488bd4.md#insn-00488bec)

~~~diff
- 00465d4c ["COPY", "register:40b0:8", ["const:c1a000:8"]]
+ 00488be4 ["COPY", "register:40b0:8", ["const:c9a000:8"]]
- 00465d4c bytes b63d00b0
+ 00488be4 bytes 964000d0
- 00465d50 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00488be8 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00465d50 bytes 083c00f0
+ 00488be8 bytes e83e00b0
- 00465d54 ["COPY", "tmp:0:8", ["const:858:8"]]
- 00465d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00465d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00465d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00488bec ["COPY", "tmp:0:8", ["const:418:8"]]
+ 00488bec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00488bec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00488bec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00465d54 bytes 08612191
+ 00488bec bytes 08611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78a223f5a3067fe92f8efff26ae07a15"></a>

### [`00465df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465df0.md) → [`00488c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488c88.md) FUN_00488c88

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00465ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465ec8.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)
- 新版 呼出元 1件 [`00488d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d60.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.93% / 新版 75.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00488ca4",
      "incomplete_value": false,
      "site": "00488ca8",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465e0c",
      "incomplete_value": false,
      "site": "00465e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00488cc0",
      "incomplete_value": false,
      "site": "00488ccc",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465e28",
      "incomplete_value": false,
      "site": "00465e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "definition_site": "00488cdc",
      "incomplete_value": true,
      "site": "00488cdc",
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
      "definition_site": "00465e44",
      "incomplete_value": true,
      "site": "00465e44",
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
      "00488ca8",
      "DATA",
      [
        "storage",
        "00be88b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00488cc4",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00488ccc",
      "DATA",
      [
        "storage",
        "00be8858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00488ca8",
      "DATA",
      [
        "storage",
        "00c65478",
        null,
        "undefined *"
      ]
    ],
    [
      "00488cc4",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00488ccc",
      "DATA",
      [
        "storage",
        "00c65418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465df0.md#insn-00465e08) · [`00465e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465df0.md#insn-00465e0c) · [`00465e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465df0.md#insn-00465e1c)
- 新版 [`00488ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488c88.md#insn-00488ca0) · [`00488ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488c88.md#insn-00488ca4) · [`00488cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488c88.md#insn-00488cb4)

~~~diff
- 00465e08 ["COPY", "register:4048:8", ["const:be8000:8"]]
+ 00488ca0 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 00465e08 bytes 093c00f0
+ 00488ca0 bytes e93e00b0
- 00465e0c ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 00465e0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00465e0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00465e0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00488ca4 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00488ca4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00488ca4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00488ca4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00465e0c bytes 29e12291
+ 00488ca4 bytes 29e11191
- 00465e1c ["INT_ADD", "register:40f0:8", ["const:465e1c:8", "const:4:8"]]
- 00465e1c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00488cb4 ["INT_ADD", "register:40f0:8", ["const:488cb4:8", "const:4:8"]]
+ 00488cb4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00465e1c bytes 91d41d94
+ 00488cb4 bytes 7f3b1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbf5a1c36a4e3d0e8c66b861d3fbeee7"></a>

### [`00465eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465eec.md) → [`00488d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d84.md) FUN_00488d84

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00465414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465414.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`004882ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004882ac.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00488d94",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00465efc",
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
      "definition_site": "00488d90",
      "incomplete_value": false,
      "site": "00488d94",
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
      "definition_site": "00465ef8",
      "incomplete_value": false,
      "site": "00465efc",
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
      "00488d90",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00488d94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00488d90",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00488d94",
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

- 旧版 [`00465efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465eec.md#insn-00465efc) · [`00465ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465eec.md#insn-00465ef4) · [`00465ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465eec.md#insn-00465ef8)
- 新版 [`00488d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d84.md#insn-00488d94) · [`00488d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d84.md#insn-00488d8c) · [`00488d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d84.md#insn-00488d90)

~~~diff
- 00465efc ["INT_ADD", "register:40f0:8", ["const:465efc:8", "const:4:8"]]
- 00465efc ["CALL", null, ["ram:418c38:8"]]
+ 00488d94 ["INT_ADD", "register:40f0:8", ["const:488d94:8", "const:4:8"]]
+ 00488d94 ["CALL", null, ["ram:43b738:8"]]
- 00465efc bytes 4fcbfe97
+ 00488d94 bytes 69cafe97
- 00465ef4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00488d8c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00465ef4 bytes 00f2ffd0
+ 00488d8c bytes 60f1fff0
- 00465ef8 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00465ef8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00465ef8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00465ef8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00488d90 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00488d90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00488d90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00488d90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00465ef8 bytes 00740e91
+ 00488d90 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be2cfcf38e98d1a296cf9339081d2ec3"></a>

### [`00465f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465f00.md) → [`00488d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d98.md) _INIT_19

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00488dd4",
      "incomplete_value": true,
      "site": "00488df0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00465f3c",
      "incomplete_value": true,
      "site": "00465f58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
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
      "definition_site": "00488df8",
      "incomplete_value": true,
      "site": "00488e14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00465f60",
      "incomplete_value": true,
      "site": "00465f7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
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
      "definition_site": "00488e18",
      "incomplete_value": true,
      "site": "00488e34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00465f80",
      "incomplete_value": true,
      "site": "00465f9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
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
      "00488dd4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00488df8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00488e18",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00488dd4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00488df8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00488e18",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465f00.md#insn-00466060) · [`00466134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465f00.md#insn-00466134) · [`00465f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465f00.md#insn-00465f28)
- 新版 [`00488ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d98.md#insn-00488ef8) · [`00488fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d98.md#insn-00488fcc) · [`00488dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d98.md#insn-00488dc0)

~~~diff
- 00466060 ["INT_ADD", "register:40f0:8", ["const:466060:8", "const:4:8"]]
- 00466060 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00488ef8 ["INT_ADD", "register:40f0:8", ["const:488ef8:8", "const:4:8"]]
+ 00488ef8 ["CALL", null, ["callee:0043b7b8:8"]]
- 00466060 bytes 16cbfe97
+ 00488ef8 bytes 30cafe97
- 00466134 ["INT_ADD", "register:40f0:8", ["const:466134:8", "const:4:8"]]
- 00466134 ["CALL", null, ["callee:00c57a30:8"]]
+ 00488fcc ["INT_ADD", "register:40f0:8", ["const:488fcc:8", "const:4:8"]]
+ 00488fcc ["CALL", null, ["callee:00c57a30:8"]]
- 00466134 bytes abd31d94
+ 00488fcc bytes 993a1f94
- 00465f28 ["COPY", "register:4098:8", ["const:c25000:8"]]
+ 00488dc0 ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 00465f28 bytes 133e0090
+ 00488dc0 bytes f3400090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fc0846e04681e168f969fce3107c2af"></a>

### [`00466290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/00466290.md) → [`00489128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489128.md) FUN_00489128

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`0060dcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md) [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) · 呼出先 0件 
- 新版 呼出元 6件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00489134",
      "incomplete_value": true,
      "site": "0048913c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046629c",
      "incomplete_value": true,
      "site": "004662a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ac0:8"
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
      "00489134",
      "READ",
      [
        "storage",
        "002b2ac0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00489134",
      "READ",
      [
        "storage",
        "002c41c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/00466290.md#insn-00466294) · [`0046629c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/00466290.md#insn-0046629c)
- 新版 [`0048912c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489128.md#insn-0048912c) · [`00489134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489128.md#insn-00489134)

~~~diff
- 00466294 ["COPY", "register:4040:8", ["const:2b2000:8"]]
+ 0048912c ["COPY", "register:4040:8", ["const:2c4000:8"]]
- 00466294 bytes 68f2ff90
+ 0048912c bytes c8f1fff0
- 0046629c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ac0:8"]]
- 0046629c ["LOAD", "register:5020:8", ["const:1b1:8", "tmp:0:8"]]
- 0046629c ["COPY", "register:5028:8", ["const:0:8"]]
- 0046629c ["COPY", "register:5030:8", ["const:0:8"]]
+ 00489134 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
+ 00489134 ["LOAD", "register:5020:8", ["const:1b1:8", "tmp:0:8"]]
+ 00489134 ["COPY", "register:5028:8", ["const:0:8"]]
+ 00489134 ["COPY", "register:5030:8", ["const:0:8"]]
- 0046629c bytes 016145fd
+ 00489134 bytes 01e140fd
~~~


<a id="compare-dc05f55c9e29f596663e8dcbf12f99d7"></a>

### [`004662ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004662ec.md) → [`00489184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md) FUN_00489184

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004662bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004662bc.md) [`0060ffa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060ffa8.md) · 呼出先 15件 [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`004652a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004652a0.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)
- 新版 呼出元 2件 [`00489154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489154.md) [`00635aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635aa0.md) · 呼出先 15件 [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.57% / 新版 93.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004891c4",
      "incomplete_value": false,
      "site": "004891cc",
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
    "old": {
      "definition_site": "0046632c",
      "incomplete_value": false,
      "site": "00466334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "definition_site": "0048938c",
      "incomplete_value": true,
      "site": "00489390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004664f4",
      "incomplete_value": true,
      "site": "004664f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00489388",
      "incomplete_value": true,
      "site": "00489394",
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
      "definition_site": "004664f0",
      "incomplete_value": true,
      "site": "004664fc",
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
      "004891cc",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00489378",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "0048937c",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004891cc",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00489378",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "0048937c",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004662ec.md#insn-00466324) · [`00466328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004662ec.md#insn-00466328) · [`0046632c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004662ec.md#insn-0046632c)
- 新版 [`004891bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md#insn-004891bc) · [`004891c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md#insn-004891c0) · [`004891c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md#insn-004891c4)

~~~diff
- 00466324 ["INT_ADD", "register:40f0:8", ["const:466324:8", "const:4:8"]]
- 00466324 ["CALL", null, ["callee:00487de0:8"]]
+ 004891bc ["INT_ADD", "register:40f0:8", ["const:4891bc:8", "const:4:8"]]
+ 004891bc ["CALL", null, ["callee:00487de0:8"]]
- 00466324 bytes 09fbff97
+ 004891bc bytes 09fbff97
- 00466328 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 004891c0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00466328 bytes 083c00b0
+ 004891c0 bytes c83e00f0
- 0046632c ["COPY", "tmp:0:8", ["const:d78:8"]]
- 0046632c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046632c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046632c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004891c4 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 004891c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004891c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004891c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046632c bytes 08e13591
+ 004891c4 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ce6590697b24b61661914196a21b05"></a>

### [`004667c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004667c4.md) → [`0048965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md) FUN_0048965c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004662ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004662ec.md) [`00467d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467d48.md) [`00838c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/00838c74.md) · 呼出先 17件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0044df7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044df7c.md) [`0044e84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044e84c.md) [`0044ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044e/0044ea58.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md)
- 新版 呼出元 3件 [`00489184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md) [`0048abe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048abe0.md) [`0086af14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086af14.md) · 呼出先 17件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00470e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470e14.md) [`004716e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004716e4.md) [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.83% / 新版 96.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00489688",
      "value": [
        "leaf",
        "ram:470e14:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004667f0",
      "value": [
        "leaf",
        "ram:44df7c:8"
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
      "site": "004896f4",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0046685c",
      "value": [
        "leaf",
        "ram:469e20:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004896fc",
      "incomplete_value": false,
      "site": "00489704",
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
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466864",
      "incomplete_value": false,
      "site": "0046686c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00489688",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044df7c"
      ]
    ],
    [
      "004896f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      "004896fc",
      "PARAM",
      [
        "storage",
        "00c250e8",
        null,
        "undefined2"
      ]
    ]
  ],
  "added": [
    [
      "00489688",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e14"
      ]
    ],
    [
      "004896f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "004896fc",
      "PARAM",
      [
        "storage",
        "00ca4ba8",
        null,
        "undefined2"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004667f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004667c4.md#insn-004667f0) · [`0046685c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004667c4.md#insn-0046685c) · [`0046686c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004667c4.md#insn-0046686c)
- 新版 [`00489688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md#insn-00489688) · [`004896f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md#insn-004896f4) · [`00489704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md#insn-00489704)

~~~diff
- 004667f0 ["INT_ADD", "register:40f0:8", ["const:4667f0:8", "const:4:8"]]
- 004667f0 ["CALL", null, ["ram:44df7c:8"]]
+ 00489688 ["INT_ADD", "register:40f0:8", ["const:489688:8", "const:4:8"]]
+ 00489688 ["CALL", null, ["ram:470e14:8"]]
- 004667f0 bytes e39dff97
+ 00489688 bytes e39dff97
- 0046685c ["INT_ADD", "register:40f0:8", ["const:46685c:8", "const:4:8"]]
- 0046685c ["CALL", null, ["ram:469e20:8"]]
+ 004896f4 ["INT_ADD", "register:40f0:8", ["const:4896f4:8", "const:4:8"]]
+ 004896f4 ["CALL", null, ["ram:48ccb8:8"]]
- 0046685c bytes 710d0094
+ 004896f4 bytes 710d0094
- 0046686c ["INT_ADD", "register:40f0:8", ["const:46686c:8", "const:4:8"]]
- 0046686c ["CALL", null, ["callee:0048d330:8"]]
+ 00489704 ["INT_ADD", "register:40f0:8", ["const:489704:8", "const:4:8"]]
+ 00489704 ["CALL", null, ["callee:0048d330:8"]]
- 0046686c bytes 0b0f0094
+ 00489704 bytes 0b0f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d2f7af1b1390681637cade2f1749f15"></a>

### [`00467098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467098.md) → [`00489f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md) FUN_00489f30

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00467864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467864.md) [`0046795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/0046795c.md) · 呼出先 21件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004677b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/004677b8.md) [`00467814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467814.md) [`0046870c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/0046870c.md) [`00468920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/00468920.md)
- 新版 呼出元 2件 [`0048a6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6fc.md) [`0048a7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a7f4.md) · 呼出先 21件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0048a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a650.md) [`0048a6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6ac.md) [`0048b5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b5a4.md) [`0048b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b7b8.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 79.91% / 新版 79.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 9件, `call_target` 2件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0048a140",
      "incomplete_value": true,
      "site": "0048a144",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4000:8"
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
      "definition_site": "004672a8",
      "incomplete_value": true,
      "site": "004672ac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4000:8"
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
    "ordinal": 22,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00489f64",
      "incomplete_value": false,
      "site": "00489f70",
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
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004670cc",
      "incomplete_value": false,
      "site": "004670d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:190:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00489f80",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004670e8",
      "value": [
        "leaf",
        "ram:469e20:8"
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
      "00489f64",
      "PARAM",
      [
        "storage",
        "00c25190",
        null,
        null
      ]
    ],
    [
      "00489f80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      "00489f9c",
      "READ",
      [
        "storage",
        "00c25100",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00489f64",
      "PARAM",
      [
        "storage",
        "00ca4c50",
        null,
        null
      ]
    ],
    [
      "00489f80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00489f9c",
      "READ",
      [
        "storage",
        "00ca4bc0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004670d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467098.md#insn-004670d8) · [`004670e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467098.md#insn-004670e8) · [`0046729c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467098.md#insn-0046729c)
- 新版 [`00489f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md#insn-00489f70) · [`00489f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md#insn-00489f80) · [`0048a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md#insn-0048a134)

~~~diff
- 004670d8 ["INT_ADD", "register:40f0:8", ["const:4670d8:8", "const:4:8"]]
- 004670d8 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00489f70 ["INT_ADD", "register:40f0:8", ["const:489f70:8", "const:4:8"]]
+ 00489f70 ["CALL", null, ["callee:00c57ce0:8"]]
- 004670d8 bytes 6ed01d94
+ 00489f70 bytes 5c371f94
- 004670e8 ["INT_ADD", "register:40f0:8", ["const:4670e8:8", "const:4:8"]]
- 004670e8 ["CALL", null, ["ram:469e20:8"]]
+ 00489f80 ["INT_ADD", "register:40f0:8", ["const:489f80:8", "const:4:8"]]
+ 00489f80 ["CALL", null, ["ram:48ccb8:8"]]
- 004670e8 bytes 4e0b0094
+ 00489f80 bytes 4e0b0094
- 0046729c ["INT_ADD", "register:40f0:8", ["const:46729c:8", "const:4:8"]]
- 0046729c ["CALL", null, ["callee:0048b5a4:8"]]
+ 0048a134 ["INT_ADD", "register:40f0:8", ["const:48a134:8", "const:4:8"]]
+ 0048a134 ["CALL", null, ["callee:0048b5a4:8"]]
- 0046729c bytes 1c050094
+ 0048a134 bytes 1c050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c82eeb01f81c3b4bdc7189a274c8cc1"></a>

### [`00467864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467864.md) → [`0048a6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6fc.md) FUN_0048a6fc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`0060b7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b7bc.md) [`00647388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00647/00647388.md) [`00714cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00714/00714cf0.md) [`007226e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00722/007226e4.md) [`0072967c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00729/0072967c.md) · 呼出先 4件 [`00467098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467098.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 11件 [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) [`0066d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md) [`0073edf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073e/0073edf4.md) [`0074c890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074c/0074c890.md) [`00753834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753834.md) · 呼出先 4件 [`00489f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048a71c",
      "incomplete_value": false,
      "site": "0048a72c",
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
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467884",
      "incomplete_value": false,
      "site": "00467894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:100:8"
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
      "0048a71c",
      "PARAM",
      [
        "storage",
        "00c25100",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0048a71c",
      "PARAM",
      [
        "storage",
        "00ca4bc0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467864.md#insn-00467894) · [`00467880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467864.md#insn-00467880) · [`00467884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467864.md#insn-00467884)
- 新版 [`0048a72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6fc.md#insn-0048a72c) · [`0048a718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6fc.md#insn-0048a718) · [`0048a71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6fc.md#insn-0048a71c)

~~~diff
- 00467894 ["INT_ADD", "register:40f0:8", ["const:467894:8", "const:4:8"]]
- 00467894 ["CALL", null, ["callee:00489f30:8"]]
+ 0048a72c ["INT_ADD", "register:40f0:8", ["const:48a72c:8", "const:4:8"]]
+ 0048a72c ["CALL", null, ["callee:00489f30:8"]]
- 00467894 bytes 01feff97
+ 0048a72c bytes 01feff97
- 00467880 ["COPY", "register:4000:8", ["const:c25000:8"]]
+ 0048a718 ["COPY", "register:4000:8", ["const:ca4000:8"]]
- 00467880 bytes e03d00d0
+ 0048a718 bytes c04000d0
- 00467884 ["COPY", "tmp:0:8", ["const:100:8"]]
- 00467884 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00467884 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00467884 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0048a71c ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 0048a71c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0048a71c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0048a71c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00467884 bytes 00000491
+ 0048a71c bytes 00002f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ecf63e0faa3b1faaa79b01e73900eec"></a>

### [`004684b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/004684b8.md) → [`0048b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b350.md) FUN_0048b350

採用 · 移動量 `+0x22e98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0081f9ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f9ac.md) [`00acc348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc348.md) · 呼出先 1件 [`00bdb5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5e0.md)
- 新版 呼出元 2件 [`00851914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/00851914.md) [`00b2bdd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bdd8.md) · 呼出先 1件 [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048b368",
      "incomplete_value": true,
      "site": "0048b368",
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
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004684d0",
      "incomplete_value": true,
      "site": "004684d0",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048b384",
      "incomplete_value": true,
      "site": "0048b384",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004684ec",
      "incomplete_value": true,
      "site": "004684ec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048b388",
      "incomplete_value": false,
      "site": "0048b388",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004684f0",
      "incomplete_value": false,
      "site": "004684f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "0048b358",
      "READ",
      [
        "storage",
        "00c250e8",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b364",
      "PARAM",
      [
        "storage",
        "00c250e8",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b368",
      "WRITE",
      [
        "storage",
        "00c250e8",
        null,
        "undefined2"
      ]
    ]
  ],
  "added": [
    [
      "0048b358",
      "READ",
      [
        "storage",
        "00ca4ba8",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b364",
      "PARAM",
      [
        "storage",
        "00ca4ba8",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b368",
      "WRITE",
      [
        "storage",
        "00ca4ba8",
        null,
        "undefined2"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004684d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/004684b8.md#insn-004684d0) · [`004684b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/004684b8.md#insn-004684b8) · [`004684c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/004684b8.md#insn-004684c0)
- 新版 [`0048b368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b350.md#insn-0048b368) · [`0048b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b350.md#insn-0048b350) · [`0048b358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b350.md#insn-0048b358)

~~~diff
- 004684d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e8:8"]]
- 004684d0 ["COPY", "tmp:1:4", ["const:0:4"]]
- 004684d0 ["COPY", "tmp:2:4", ["tmp:1:4"]]
- 004684d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:2:2"]]
+ 0048b368 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ba8:8"]]
+ 0048b368 ["COPY", "tmp:1:4", ["const:0:4"]]
+ 0048b368 ["COPY", "tmp:2:4", ["tmp:1:4"]]
+ 0048b368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:2:2"]]
- 004684d0 bytes 1fd10179
+ 0048b368 bytes 1f511779
- 004684b8 ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 0048b350 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 004684b8 bytes e83d00b0
+ 0048b350 bytes c84000b0
- 004684c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e8:8"]]
- 004684c0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 004684c0 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
+ 0048b358 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ba8:8"]]
+ 0048b358 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0048b358 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
- 004684c0 bytes 09a14339
+ 0048b358 bytes 09a16e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-537d5d23d48d33190cf1487e2c67bf0a"></a>

### [`0046866c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/0046866c.md) → [`0048b504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b504.md) FUN_0048b504

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004684f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/004684f8.md) [`008458f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/008458f4.md) [`00a6a58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a58c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`0048b390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b390.md) [`00877be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877be0.md) [`00ac8520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8520.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0048b514",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0046867c",
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
      "definition_site": "0048b510",
      "incomplete_value": false,
      "site": "0048b514",
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
      "definition_site": "00468678",
      "incomplete_value": false,
      "site": "0046867c",
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
      "0048b510",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0048b514",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0048b510",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0048b514",
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

- 旧版 [`0046867c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/0046866c.md#insn-0046867c) · [`00468674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/0046866c.md#insn-00468674) · [`00468678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/0046866c.md#insn-00468678)
- 新版 [`0048b514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b504.md#insn-0048b514) · [`0048b50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b504.md#insn-0048b50c) · [`0048b510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b504.md#insn-0048b510)

~~~diff
- 0046867c ["INT_ADD", "register:40f0:8", ["const:46867c:8", "const:4:8"]]
- 0046867c ["CALL", null, ["ram:418c38:8"]]
+ 0048b514 ["INT_ADD", "register:40f0:8", ["const:48b514:8", "const:4:8"]]
+ 0048b514 ["CALL", null, ["ram:43b738:8"]]
- 0046867c bytes 6fc1fe97
+ 0048b514 bytes 89c0fe97
- 00468674 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0048b50c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00468674 bytes e0f1fff0
+ 0048b50c bytes 60f1ff90
- 00468678 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00468678 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00468678 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00468678 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0048b510 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0048b510 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0048b510 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0048b510 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00468678 bytes 00740e91
+ 0048b510 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e24686c74f2113a5cbd853023442d47"></a>

### [`00469128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469128.md) → [`0048bfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md) FUN_0048bfc0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00469128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469128.md) [`008818a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00881/008818a8.md) [`0090f708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0090f/0090f708.md) [`00971a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00971/00971a68.md) [`0097a888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a888.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 6件 [`0048bfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md) [`008b4a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b4/008b4a48.md) [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) [`00944614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944614.md) [`009a754c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a7/009a754c.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048c118",
      "incomplete_value": false,
      "site": "0048c120",
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
    "old": {
      "definition_site": "00469280",
      "incomplete_value": false,
      "site": "00469288",
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
            "const:3a4:8"
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
      "definition_site": "0048c1d4",
      "incomplete_value": false,
      "site": "0048c1dc",
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
    "old": {
      "definition_site": "0046933c",
      "incomplete_value": false,
      "site": "00469344",
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
            "const:379:8"
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
      "definition_site": "0048c1ec",
      "incomplete_value": false,
      "site": "0048c1f8",
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
    "old": {
      "definition_site": "00469354",
      "incomplete_value": false,
      "site": "00469360",
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
            "const:885:8"
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
      "0048c118",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0048c1d4",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "0048c1ec",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0048c118",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0048c1d4",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0048c1ec",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00469288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469128.md#insn-00469288) · [`00469344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469128.md#insn-00469344) · [`00469360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469128.md#insn-00469360)
- 新版 [`0048c120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md#insn-0048c120) · [`0048c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md#insn-0048c1dc) · [`0048c1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md#insn-0048c1f8)

~~~diff
- 00469288 ["INT_ADD", "register:40f0:8", ["const:469288:8", "const:4:8"]]
- 00469288 ["CALL", null, ["callee:00441e54:8"]]
+ 0048c120 ["INT_ADD", "register:40f0:8", ["const:48c120:8", "const:4:8"]]
+ 0048c120 ["CALL", null, ["callee:00441e54:8"]]
- 00469288 bytes 33d8fe97
+ 0048c120 bytes 4dd7fe97
- 00469344 ["INT_ADD", "register:40f0:8", ["const:469344:8", "const:4:8"]]
- 00469344 ["CALL", null, ["callee:00441e54:8"]]
+ 0048c1dc ["INT_ADD", "register:40f0:8", ["const:48c1dc:8", "const:4:8"]]
+ 0048c1dc ["CALL", null, ["callee:00441e54:8"]]
- 00469344 bytes 04d8fe97
+ 0048c1dc bytes 1ed7fe97
- 00469360 ["INT_ADD", "register:40f0:8", ["const:469360:8", "const:4:8"]]
- 00469360 ["CALL", null, ["callee:004427b4:8"]]
+ 0048c1f8 ["INT_ADD", "register:40f0:8", ["const:48c1f8:8", "const:4:8"]]
+ 0048c1f8 ["CALL", null, ["callee:004427b4:8"]]
- 00469360 bytes 55dafe97
+ 0048c1f8 bytes 6fd9fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b895d4d861333e2ed6d0c6011d869a8"></a>

### [`00469a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469a60.md) → [`0048c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048c8f8.md) _INIT_21

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048c934",
      "incomplete_value": true,
      "site": "0048c950",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00469a9c",
      "incomplete_value": true,
      "site": "00469ab8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
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
      "definition_site": "0048c958",
      "incomplete_value": true,
      "site": "0048c974",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00469ac0",
      "incomplete_value": true,
      "site": "00469adc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
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
      "definition_site": "0048c978",
      "incomplete_value": true,
      "site": "0048c994",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00469ae0",
      "incomplete_value": true,
      "site": "00469afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
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
      "0048c934",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0048c958",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0048c978",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0048c934",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0048c958",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0048c978",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00469bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469a60.md#insn-00469bc0) · [`00469c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469a60.md#insn-00469c94) · [`00469a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469a60.md#insn-00469a88)
- 新版 [`0048ca58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048c8f8.md#insn-0048ca58) · [`0048cb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048c8f8.md#insn-0048cb2c) · [`0048c920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048c8f8.md#insn-0048c920)

~~~diff
- 00469bc0 ["INT_ADD", "register:40f0:8", ["const:469bc0:8", "const:4:8"]]
- 00469bc0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0048ca58 ["INT_ADD", "register:40f0:8", ["const:48ca58:8", "const:4:8"]]
+ 0048ca58 ["CALL", null, ["callee:0043b7b8:8"]]
- 00469bc0 bytes 3ebcfe97
+ 0048ca58 bytes 58bbfe97
- 00469c94 ["INT_ADD", "register:40f0:8", ["const:469c94:8", "const:4:8"]]
- 00469c94 ["CALL", null, ["callee:00c57a30:8"]]
+ 0048cb2c ["INT_ADD", "register:40f0:8", ["const:48cb2c:8", "const:4:8"]]
+ 0048cb2c ["CALL", null, ["callee:00c57a30:8"]]
- 00469c94 bytes d3c41d94
+ 0048cb2c bytes c12b1f94
- 00469a88 ["COPY", "register:4098:8", ["const:c25000:8"]]
+ 0048c920 ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 00469a88 bytes f33d0090
+ 0048c920 bytes d3400090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a251c20bdb2286b791de6497fe32ebd"></a>

### [`0046a090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a090.md) → [`0048cf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf28.md) FUN_0048cf28

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0046a08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a08c.md) · 呼出先 12件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`0048cf24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf24.md) · 呼出先 12件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)

変更の種類 call, call_argument_candidate, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.95% / 新版 91.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048cf90",
      "incomplete_value": true,
      "site": "0048cf94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "0046a0f8",
      "incomplete_value": true,
      "site": "0046a0fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048cf8c",
      "incomplete_value": true,
      "site": "0048cf98",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0046a0f4",
      "incomplete_value": true,
      "site": "0046a100",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048cfa0",
      "incomplete_value": true,
      "site": "0048cfa0",
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
                "const:10:8"
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
      "definition_site": "0046a108",
      "incomplete_value": true,
      "site": "0046a108",
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
                "const:10:8"
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
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048cf7c",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "0048cf80",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "0048cf8c",
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
      "0048cf7c",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "0048cf80",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "0048cf8c",
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

- 旧版 [`0046a19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a090.md#insn-0046a19c) · [`0046a1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a090.md#insn-0046a1b4) · [`0046a0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a090.md#insn-0046a0d8)
- 新版 [`0048d034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf28.md#insn-0048d034) · [`0048d04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf28.md#insn-0048d04c) · [`0048cf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf28.md#insn-0048cf70)

~~~diff
- 0046a19c ["INT_ADD", "register:40f0:8", ["const:46a19c:8", "const:4:8"]]
- 0046a19c ["CALL", null, ["callee:00c57e80:8"]]
+ 0048d034 ["INT_ADD", "register:40f0:8", ["const:48d034:8", "const:4:8"]]
+ 0048d034 ["CALL", null, ["callee:00c57e80:8"]]
- 0046a19c bytes a5c41d94
+ 0048d034 bytes 932b1f94
- 0046a1b4 ["INT_ADD", "register:40f0:8", ["const:46a1b4:8", "const:4:8"]]
- 0046a1b4 ["CALL", null, ["ram:bdb440:8"]]
+ 0048d04c ["INT_ADD", "register:40f0:8", ["const:48d04c:8", "const:4:8"]]
+ 0048d04c ["CALL", null, ["ram:c57e90:8"]]
- 0046a1b4 bytes a3c41d94
+ 0048d04c bytes 912b1f94
- 0046a0d8 ["COPY", "register:40c8:8", ["const:c1a000:8"]]
+ 0048cf70 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
- 0046a0d8 bytes 993d0090
+ 0048cf70 bytes 794000d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff75b06f0c2f681cd9f73e30b2f5f4d5"></a>

### [`0046a658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a658.md) → [`0048d4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d4f0.md) FUN_0048d4f0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`009db014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009db/009db014.md) · 呼出先 6件 [`0053c1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c1bc.md) [`00574730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574730.md) [`00574740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574740.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md) · 呼出先 6件 [`0055f054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f054.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`005975d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.35% / 新版 99.35%

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
      "site": "0048d53c",
      "value": [
        "leaf",
        "ram:55f054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0046a6a4",
      "value": [
        "leaf",
        "ram:53c1bc:8"
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
      "0048d53c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0053c1bc"
      ]
    ]
  ],
  "added": [
    [
      "0048d53c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055f054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046a6a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a658.md#insn-0046a6a4) · [`0046a68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a658.md#insn-0046a68c) · [`0046a6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a658.md#insn-0046a6b8)
- 新版 [`0048d53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d4f0.md#insn-0048d53c) · [`0048d524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d4f0.md#insn-0048d524) · [`0048d550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d4f0.md#insn-0048d550)

~~~diff
- 0046a6a4 ["INT_ADD", "register:40f0:8", ["const:46a6a4:8", "const:4:8"]]
- 0046a6a4 ["CALL", null, ["ram:53c1bc:8"]]
+ 0048d53c ["INT_ADD", "register:40f0:8", ["const:48d53c:8", "const:4:8"]]
+ 0048d53c ["CALL", null, ["ram:55f054:8"]]
- 0046a6a4 bytes c6460394
+ 0048d53c bytes c6460394
- 0046a68c ["INT_ADD", "register:40f0:8", ["const:46a68c:8", "const:4:8"]]
- 0046a68c ["CALL", null, ["callee:005975c8:8"]]
+ 0048d524 ["INT_ADD", "register:40f0:8", ["const:48d524:8", "const:4:8"]]
+ 0048d524 ["CALL", null, ["callee:005975c8:8"]]
- 0046a68c bytes 29280494
+ 0048d524 bytes 29280494
- 0046a6b8 ["INT_ADD", "register:40f0:8", ["const:46a6b8:8", "const:4:8"]]
- 0046a6b8 ["CALL", null, ["callee:00c538e0:8"]]
+ 0048d550 ["INT_ADD", "register:40f0:8", ["const:48d550:8", "const:4:8"]]
+ 0048d550 ["CALL", null, ["callee:00c538e0:8"]]
- 0046a6b8 bytes f6b11d94
+ 0048d550 bytes e4181f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-107b2e102a4c59a511d73e97192cb3e5"></a>

### [`0046c018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c018.md) → [`0048eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md) FUN_0048eeb0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 22件 [`005a2308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a2/005a2308.md) [`006091c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/006091c4.md) [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) [`00632468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/00632468.md) [`006833dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00683/006833dc.md) · 呼出先 17件 [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c4c0.md) [`0046c588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md)
- 新版 呼出元 22件 [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) [`0062ecbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062ecbc.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`00657f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657f4c.md) [`006a9724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a9/006a9724.md) · 呼出先 17件 [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) [`0048ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048ebc8.md) [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md) [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.94% / 新版 85.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `call_target` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048ef64",
      "incomplete_value": false,
      "site": "0048ef64",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046c0cc",
      "incomplete_value": false,
      "site": "0046c0cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "definition_site": "0048f034",
      "incomplete_value": true,
      "site": "0048f034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046c19c",
      "incomplete_value": true,
      "site": "0046c19c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0048f034",
      "incomplete_value": false,
      "site": "0048f034",
      "value": [
        "leaf",
        "const:48f358:8"
      ]
    },
    "old": {
      "definition_site": "0046c19c",
      "incomplete_value": false,
      "site": "0046c19c",
      "value": [
        "leaf",
        "const:46c4c0:8"
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
      "0048ef5c",
      "READ",
      [
        "storage",
        "00c25258",
        null,
        "undefined8"
      ]
    ],
    [
      "0048ef64",
      "WRITE",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "0048efd0",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048ef5c",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "0048ef64",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "0048efd0",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046c1cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c018.md#insn-0046c1cc) · [`0046c314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c018.md#insn-0046c314) · [`0046c05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c018.md#insn-0046c05c)
- 新版 [`0048f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md#insn-0048f064) · [`0048f1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md#insn-0048f1ac) · [`0048eef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md#insn-0048eef4)

~~~diff
- 0046c1cc ["INT_ADD", "register:40f0:8", ["const:46c1cc:8", "const:4:8"]]
- 0046c1cc ["CALL", null, ["callee:005509c4:8"]]
+ 0048f064 ["INT_ADD", "register:40f0:8", ["const:48f064:8", "const:4:8"]]
+ 0048f064 ["CALL", null, ["callee:005509c4:8"]]
- 0046c1cc bytes 58060394
+ 0048f064 bytes 58060394
- 0046c314 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046c314 ["INT_ADD", "register:40f0:8", ["const:46c314:8", "const:4:8"]]
- 0046c314 ["CALLIND", null, ["register:0:8"]]
+ 0048f1ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048f1ac ["INT_ADD", "register:40f0:8", ["const:48f1ac:8", "const:4:8"]]
+ 0048f1ac ["CALLIND", null, ["register:0:8"]]
- 0046c314 bytes 00013fd6
+ 0048f1ac bytes 00013fd6
- 0046c05c ["INT_ADD", "register:40f0:8", ["const:46c05c:8", "const:4:8"]]
- 0046c05c ["CALL", null, ["callee:005509c0:8"]]
+ 0048eef4 ["INT_ADD", "register:40f0:8", ["const:48eef4:8", "const:4:8"]]
+ 0048eef4 ["CALL", null, ["callee:005509c0:8"]]
- 0046c05c bytes b3060394
+ 0048eef4 bytes b3060394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faf7d21f986e9532d6caf1723399a1a1"></a>

### [`0046c4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c4c0.md) → [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md) FUN_0048f358

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`0046c018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c018.md) [`0046d29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d29c.md) [`0046d7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d7c4.md) [`0046ede4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046ede4.md) [`0046f248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f248.md) · 呼出先 3件 [`0052db24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db24.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 9件 [`0048eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md) [`00490134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md) [`0049065c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md) [`00491c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491c7c.md) [`004920e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md) · 呼出先 3件 [`005509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509bc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048f374",
      "incomplete_value": false,
      "site": "0048f374",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046c4dc",
      "incomplete_value": false,
      "site": "0046c4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048f374",
      "incomplete_value": false,
      "site": "0048f374",
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
                "const:d10:8"
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
      "definition_site": "0046c4dc",
      "incomplete_value": false,
      "site": "0046c4dc",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:250:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0048f378",
      "incomplete_value": true,
      "site": "0048f378",
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
      "definition_site": "0046c4e0",
      "incomplete_value": true,
      "site": "0046c4e0",
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
      "0048f370",
      "READ",
      [
        "storage",
        "00c25258",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f374",
      "WRITE",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f374",
      "WRITE",
      [
        "storage",
        "00c25258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0048f370",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f374",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f374",
      "WRITE",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046c4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c4c0.md#insn-0046c4cc) · [`0046c4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c4c0.md#insn-0046c4d0) · [`0046c4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c4c0.md#insn-0046c4d4)
- 新版 [`0048f364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md#insn-0048f364) · [`0048f368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md#insn-0048f368) · [`0048f36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md#insn-0048f36c)

~~~diff
- 0046c4cc ["INT_ADD", "register:40f0:8", ["const:46c4cc:8", "const:4:8"]]
- 0046c4cc ["CALL", null, ["callee:005509bc:8"]]
+ 0048f364 ["INT_ADD", "register:40f0:8", ["const:48f364:8", "const:4:8"]]
+ 0048f364 ["CALL", null, ["callee:005509bc:8"]]
- 0046c4cc bytes 96050394
+ 0048f364 bytes 96050394
- 0046c4d0 ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 0048f368 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0046c4d0 bytes c83d00b0
+ 0048f368 bytes a84000b0
- 0046c4d4 ["COPY", "tmp:0:8", ["const:250:8"]]
- 0046c4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046c4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046c4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0048f36c ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 0048f36c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0048f36c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0048f36c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046c4d4 bytes 08410991
+ 0048f36c bytes 08413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24f9efbba7c3de066709f81ad1399242"></a>

### [`0046c588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md) → [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md) FUN_0048f420

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 8件 [`0046c018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c018.md) [`0046d29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d29c.md) [`0046d7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d7c4.md) [`0046dc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046dc5c.md) [`0046e4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046e4f8.md) · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00423878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423878.md) [`00426cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426cec.md) [`00426e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md) [`0052db30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db30.md)
- 新版 呼出元 8件 [`0048eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md) [`00490134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md) [`0049065c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md) [`00490af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md) [`00491390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491390.md) · 呼出先 17件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00446378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446378.md) [`004497ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/004497ec.md) [`0044998c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/0044998c.md) [`005509c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509c8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.81% / 新版 93.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 16件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048f784",
      "incomplete_value": true,
      "site": "0048f798",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:234:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046c8ec",
      "incomplete_value": true,
      "site": "0046c900",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:253:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0048f788",
      "incomplete_value": true,
      "site": "0048f79c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0046c8f0",
      "incomplete_value": true,
      "site": "0046c904",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048f78c",
      "incomplete_value": true,
      "site": "0048f7a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0046c8f4",
      "incomplete_value": true,
      "site": "0046c908",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4c0:8"
              ]
            ]
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
      "0048f538",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f604",
      "PARAM",
      [
        "storage",
        "0029e2ce",
        null,
        "string"
      ]
    ],
    [
      "0048f610",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00423878"
      ]
    ]
  ],
  "added": [
    [
      "0048f538",
      "READ",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f604",
      "PARAM",
      [
        "storage",
        "002ae653",
        null,
        "string"
      ]
    ],
    [
      "0048f610",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00446378"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md#insn-0046c6c4) · [`0046c778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md#insn-0046c778) · [`0046c650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md#insn-0046c650)
- 新版 [`0048f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md#insn-0048f55c) · [`0048f610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md#insn-0048f610) · [`0048f4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md#insn-0048f4e8)

~~~diff
- 0046c6c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046c6c4 ["INT_ADD", "register:40f0:8", ["const:46c6c4:8", "const:4:8"]]
- 0046c6c4 ["CALLIND", null, ["register:0:8"]]
+ 0048f55c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048f55c ["INT_ADD", "register:40f0:8", ["const:48f55c:8", "const:4:8"]]
+ 0048f55c ["CALLIND", null, ["register:0:8"]]
- 0046c6c4 bytes 00013fd6
+ 0048f55c bytes 00013fd6
- 0046c778 ["INT_ADD", "register:40f0:8", ["const:46c778:8", "const:4:8"]]
- 0046c778 ["CALL", null, ["ram:423878:8"]]
+ 0048f610 ["INT_ADD", "register:40f0:8", ["const:48f610:8", "const:4:8"]]
+ 0048f610 ["CALL", null, ["ram:446378:8"]]
- 0046c778 bytes 40dcfe97
+ 0048f610 bytes 5adbfe97
- 0046c650 ["INT_ADD", "register:40f0:8", ["const:46c650:8", "const:4:8"]]
- 0046c650 ["CALL", null, ["callee:00c57bd0:8"]]
+ 0048f4e8 ["INT_ADD", "register:40f0:8", ["const:48f4e8:8", "const:4:8"]]
+ 0048f4e8 ["CALL", null, ["callee:00c57bd0:8"]]
- 0046c650 bytes ccba1d94
+ 0048f4e8 bytes ba211f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea4b79ed44b46ae8bad4d8253b36f0d1"></a>

### [`0046d29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d29c.md) → [`00490134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md) FUN_00490134

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 21件 [`00449c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c2c.md) [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c4c0.md)
- 新版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 21件 [`0046cac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cac4.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) [`0048ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048ebc8.md) [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.52% / 新版 86.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00490198",
      "incomplete_value": true,
      "site": "004901ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:186:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d300",
      "incomplete_value": true,
      "site": "0046d314",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:695:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00490270",
      "incomplete_value": false,
      "site": "00490270",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d3d8",
      "incomplete_value": false,
      "site": "0046d3d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00490318",
      "incomplete_value": true,
      "site": "00490318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046d480",
      "incomplete_value": true,
      "site": "0046d480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00490198",
      "READ",
      [
        "storage",
        "002a6695",
        null,
        "string"
      ]
    ],
    [
      "004901bc",
      "READ",
      [
        "storage",
        "002b2690",
        null,
        "undefined8"
      ]
    ],
    [
      "004901e4",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00490198",
      "READ",
      [
        "storage",
        "002b7186",
        null,
        "string"
      ]
    ],
    [
      "004901bc",
      "READ",
      [
        "storage",
        "002c3d68",
        null,
        "undefined8"
      ]
    ],
    [
      "004901e4",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046d328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d29c.md#insn-0046d328) · [`0046d354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d29c.md#insn-0046d354) · [`0046d4b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d29c.md#insn-0046d4b4)
- 新版 [`004901c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md#insn-004901c0) · [`004901ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md#insn-004901ec) · [`0049034c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md#insn-0049034c)

~~~diff
- 0046d328 ["INT_ADD", "register:40f0:8", ["const:46d328:8", "const:4:8"]]
- 0046d328 ["CALL", null, ["callee:009365bc:8"]]
+ 004901c0 ["INT_ADD", "register:40f0:8", ["const:4901c0:8", "const:4:8"]]
+ 004901c0 ["CALL", null, ["callee:009365bc:8"]]
- 0046d328 bytes 18521294
+ 004901c0 bytes ff981294
- 0046d354 ["INT_ADD", "register:40f0:8", ["const:46d354:8", "const:4:8"]]
- 0046d354 ["CALL", null, ["ram:449c2c:8"]]
+ 004901ec ["INT_ADD", "register:40f0:8", ["const:4901ec:8", "const:4:8"]]
+ 004901ec ["CALL", null, ["ram:46cac4:8"]]
- 0046d354 bytes 3672ff97
+ 004901ec bytes 3672ff97
- 0046d4b4 ["INT_ADD", "register:40f0:8", ["const:46d4b4:8", "const:4:8"]]
- 0046d4b4 ["CALL", null, ["callee:005509c4:8"]]
+ 0049034c ["INT_ADD", "register:40f0:8", ["const:49034c:8", "const:4:8"]]
+ 0049034c ["CALL", null, ["callee:005509c4:8"]]
- 0046d4b4 bytes 9e010394
+ 0049034c bytes 9e010394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c12198fd10adbec680a0fecf98dcf21b"></a>

### [`0046d7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d7c4.md) → [`0049065c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md) FUN_0049065c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0094ac20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094a/0094ac20.md) · 呼出先 17件 [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c4c0.md) [`0046c588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md)
- 新版 呼出元 1件 [`009806cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/009806cc.md) · 呼出先 17件 [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) [`0048ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048ebc8.md) [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md) [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 4件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00490740",
      "incomplete_value": false,
      "site": "00490740",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d8a8",
      "incomplete_value": false,
      "site": "0046d8a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "definition_site": "004907d4",
      "incomplete_value": true,
      "site": "004907d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046d93c",
      "incomplete_value": true,
      "site": "0046d93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004907d4",
      "incomplete_value": false,
      "site": "004907d4",
      "value": [
        "leaf",
        "const:48f358:8"
      ]
    },
    "old": {
      "definition_site": "0046d93c",
      "incomplete_value": false,
      "site": "0046d93c",
      "value": [
        "leaf",
        "const:46c4c0:8"
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
      "004906cc",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "004906d4",
      "READ",
      [
        "storage",
        "00c24dd4",
        null,
        "undefined4"
      ]
    ],
    [
      "00490738",
      "READ",
      [
        "storage",
        "00c25258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004906cc",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "004906d4",
      "READ",
      [
        "storage",
        "00ca4894",
        null,
        "undefined4"
      ]
    ],
    [
      "00490738",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046d890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d7c4.md#insn-0046d890) · [`0046dab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d7c4.md#insn-0046dab0) · [`0046d808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046d7c4.md#insn-0046d808)
- 新版 [`00490728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md#insn-00490728) · [`00490948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md#insn-00490948) · [`004906a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md#insn-004906a0)

~~~diff
- 0046d890 ["INT_ADD", "register:40f0:8", ["const:46d890:8", "const:4:8"]]
- 0046d890 ["CALL", null, ["callee:005509cc:8"]]
+ 00490728 ["INT_ADD", "register:40f0:8", ["const:490728:8", "const:4:8"]]
+ 00490728 ["CALL", null, ["callee:005509cc:8"]]
- 0046d890 bytes a9000394
+ 00490728 bytes a9000394
- 0046dab0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046dab0 ["INT_ADD", "register:40f0:8", ["const:46dab0:8", "const:4:8"]]
- 0046dab0 ["CALLIND", null, ["register:0:8"]]
+ 00490948 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00490948 ["INT_ADD", "register:40f0:8", ["const:490948:8", "const:4:8"]]
+ 00490948 ["CALLIND", null, ["register:0:8"]]
- 0046dab0 bytes 00013fd6
+ 00490948 bytes 00013fd6
- 0046d808 ["INT_ADD", "register:40f0:8", ["const:46d808:8", "const:4:8"]]
- 0046d808 ["CALL", null, ["callee:005509c0:8"]]
+ 004906a0 ["INT_ADD", "register:40f0:8", ["const:4906a0:8", "const:4:8"]]
+ 004906a0 ["CALL", null, ["callee:005509c0:8"]]
- 0046d808 bytes c8000394
+ 004906a0 bytes c8000394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-547a3bd1f2eaa543fe14d8ee3c35302b"></a>

### [`0046dc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046dc5c.md) → [`00490af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md) FUN_00490af4

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`008594d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/008594d4.md) · 呼出先 21件 [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md) [`00449c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c84.md) [`0046ae68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ae68.md) [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md) [`0046b618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b618.md)
- 新版 呼出元 3件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0088c46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c46c.md) · 呼出先 21件 [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) [`0046cb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cb1c.md) [`0048dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e4b0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.87% / 新版 88.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00490b7c",
      "incomplete_value": false,
      "site": "00490b7c",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046dce4",
      "incomplete_value": false,
      "site": "0046dce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00490ec0",
      "incomplete_value": false,
      "site": "00490ec0",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046e028",
      "incomplete_value": false,
      "site": "0046e028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "definition_site": "00490f80",
      "incomplete_value": true,
      "site": "00490f94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0046e0e8",
      "incomplete_value": true,
      "site": "0046e0fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a7:8"
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
      "00490b74",
      "READ",
      [
        "storage",
        "00c25258",
        null,
        "undefined8"
      ]
    ],
    [
      "00490b7c",
      "WRITE",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "00490c20",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00490b74",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00490b7c",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00490c20",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046e308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046dc5c.md#insn-0046e308) · [`0046dc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046dc5c.md#insn-0046dc9c) · [`0046dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046d/0046dc5c.md#insn-0046dccc)
- 新版 [`004911a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md#insn-004911a0) · [`00490b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md#insn-00490b34) · [`00490b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md#insn-00490b64)

~~~diff
- 0046e308 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046e308 ["INT_ADD", "register:40f0:8", ["const:46e308:8", "const:4:8"]]
- 0046e308 ["CALLIND", null, ["register:0:8"]]
+ 004911a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004911a0 ["INT_ADD", "register:40f0:8", ["const:4911a0:8", "const:4:8"]]
+ 004911a0 ["CALLIND", null, ["register:0:8"]]
- 0046e308 bytes 00013fd6
+ 004911a0 bytes 00013fd6
- 0046dc9c ["INT_ADD", "register:40f0:8", ["const:46dc9c:8", "const:4:8"]]
- 0046dc9c ["CALL", null, ["callee:005509c0:8"]]
+ 00490b34 ["INT_ADD", "register:40f0:8", ["const:490b34:8", "const:4:8"]]
+ 00490b34 ["CALL", null, ["callee:005509c0:8"]]
- 0046dc9c bytes a3ff0294
+ 00490b34 bytes a3ff0294
- 0046dccc ["INT_ADD", "register:40f0:8", ["const:46dccc:8", "const:4:8"]]
- 0046dccc ["CALL", null, ["callee:005509cc:8"]]
+ 00490b64 ["INT_ADD", "register:40f0:8", ["const:490b64:8", "const:4:8"]]
+ 00490b64 ["CALL", null, ["callee:005509cc:8"]]
- 0046dccc bytes 9aff0294
+ 00490b64 bytes 9aff0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33caed4d94aa650da084d8482fa4f19c"></a>

### [`0046e4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046e4f8.md) → [`00491390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491390.md) FUN_00491390

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0080d900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080d900.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`0083d5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083d/0083d5f0.md) · 呼出先 20件 [`0046ae68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ae68.md) [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md) [`0046b618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b618.md) [`0046c588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md) [`004710d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004710d8.md)
- 新版 呼出元 3件 [`0083f428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f428.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0086f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8dc.md) · 呼出先 20件 [`0048dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e4b0.md) [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md) [`00493f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493f70.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.45% / 新版 87.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00491444",
      "incomplete_value": false,
      "site": "00491444",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046e5ac",
      "incomplete_value": false,
      "site": "0046e5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004917bc",
      "incomplete_value": false,
      "site": "004917bc",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046e924",
      "incomplete_value": false,
      "site": "0046e924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00491868",
      "incomplete_value": true,
      "site": "00491884",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0046e9d0",
      "incomplete_value": true,
      "site": "0046e9ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049143c",
      "READ",
      [
        "storage",
        "00c25258",
        null,
        "undefined8"
      ]
    ],
    [
      "00491444",
      "WRITE",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "004914d0",
      "READ",
      [
        "storage",
        "002b2c70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0049143c",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00491444",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "004914d0",
      "READ",
      [
        "storage",
        "002c4380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046ebdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046e4f8.md#insn-0046ebdc) · [`0046e53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046e4f8.md#insn-0046e53c) · [`0046e594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046e4f8.md#insn-0046e594)
- 新版 [`00491a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491390.md#insn-00491a74) · [`004913d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491390.md#insn-004913d4) · [`0049142c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491390.md#insn-0049142c)

~~~diff
- 0046ebdc ["COPY", "register:0:8", ["register:4040:8"]]
- 0046ebdc ["INT_ADD", "register:40f0:8", ["const:46ebdc:8", "const:4:8"]]
- 0046ebdc ["CALLIND", null, ["register:0:8"]]
+ 00491a74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00491a74 ["INT_ADD", "register:40f0:8", ["const:491a74:8", "const:4:8"]]
+ 00491a74 ["CALLIND", null, ["register:0:8"]]
- 0046ebdc bytes 00013fd6
+ 00491a74 bytes 00013fd6
- 0046e53c ["INT_ADD", "register:40f0:8", ["const:46e53c:8", "const:4:8"]]
- 0046e53c ["CALL", null, ["callee:005509c0:8"]]
+ 004913d4 ["INT_ADD", "register:40f0:8", ["const:4913d4:8", "const:4:8"]]
+ 004913d4 ["CALL", null, ["callee:005509c0:8"]]
- 0046e53c bytes 7bfd0294
+ 004913d4 bytes 7bfd0294
- 0046e594 ["INT_ADD", "register:40f0:8", ["const:46e594:8", "const:4:8"]]
- 0046e594 ["CALL", null, ["callee:005509cc:8"]]
+ 0049142c ["INT_ADD", "register:40f0:8", ["const:49142c:8", "const:4:8"]]
+ 0049142c ["CALL", null, ["callee:005509cc:8"]]
- 0046e594 bytes 68fd0294
+ 0049142c bytes 68fd0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48cc8f0d65980cd435e5f5712a1a260a"></a>

### [`0046ede4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046ede4.md) → [`00491c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491c7c.md) FUN_00491c7c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00605bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/00605bdc.md) · 呼出先 17件 [`00449c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c84.md) [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c4c0.md)
- 新版 呼出元 1件 [`0062b6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b6d4.md) · 呼出先 17件 [`0046cb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cb1c.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) [`0048ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048ebc8.md) [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.15% / 新版 86.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00491d00",
      "incomplete_value": false,
      "site": "00491d00",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046ee68",
      "incomplete_value": false,
      "site": "0046ee68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00491dc4",
      "incomplete_value": true,
      "site": "00491dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046ef2c",
      "incomplete_value": true,
      "site": "0046ef2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00491dc4",
      "incomplete_value": false,
      "site": "00491dc4",
      "value": [
        "leaf",
        "const:48f358:8"
      ]
    },
    "old": {
      "definition_site": "0046ef2c",
      "incomplete_value": false,
      "site": "0046ef2c",
      "value": [
        "leaf",
        "const:46c4c0:8"
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
      "00491cf8",
      "READ",
      [
        "storage",
        "00c25258",
        null,
        "undefined8"
      ]
    ],
    [
      "00491d00",
      "WRITE",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "00491d6c",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00491cf8",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00491d00",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00491d6c",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046ef00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046ede4.md#insn-0046ef00) · [`0046f080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046ede4.md#insn-0046f080) · [`0046ee24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046e/0046ede4.md#insn-0046ee24)
- 新版 [`00491d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491c7c.md#insn-00491d98) · [`00491f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491c7c.md#insn-00491f18) · [`00491cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491c7c.md#insn-00491cbc)

~~~diff
- 0046ef00 ["INT_ADD", "register:40f0:8", ["const:46ef00:8", "const:4:8"]]
- 0046ef00 ["CALL", null, ["callee:0046cb1c:8"]]
+ 00491d98 ["INT_ADD", "register:40f0:8", ["const:491d98:8", "const:4:8"]]
+ 00491d98 ["CALL", null, ["callee:0046cb1c:8"]]
- 0046ef00 bytes 616bff97
+ 00491d98 bytes 616bff97
- 0046f080 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046f080 ["INT_ADD", "register:40f0:8", ["const:46f080:8", "const:4:8"]]
- 0046f080 ["CALLIND", null, ["register:0:8"]]
+ 00491f18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00491f18 ["INT_ADD", "register:40f0:8", ["const:491f18:8", "const:4:8"]]
+ 00491f18 ["CALLIND", null, ["register:0:8"]]
- 0046f080 bytes 00013fd6
+ 00491f18 bytes 00013fd6
- 0046ee24 ["INT_ADD", "register:40f0:8", ["const:46ee24:8", "const:4:8"]]
- 0046ee24 ["CALL", null, ["callee:005509c0:8"]]
+ 00491cbc ["INT_ADD", "register:40f0:8", ["const:491cbc:8", "const:4:8"]]
+ 00491cbc ["CALL", null, ["callee:005509c0:8"]]
- 0046ee24 bytes 41fb0294
+ 00491cbc bytes 41fb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e7cf4362c9c3a050743477b10f98ec1"></a>

### [`0046f248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f248.md) → [`004920e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md) FUN_004920e0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`006b0874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0874.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00868124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) [`008a5bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5bd0.md) · 呼出先 17件 [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md) [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c4c0.md)
- 新版 呼出元 6件 [`006da630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da630.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) [`008d9a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md) · 呼出先 17件 [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) [`0048ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048ebc8.md) [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.22% / 新版 86.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00492158",
      "incomplete_value": false,
      "site": "00492158",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046f2c0",
      "incomplete_value": false,
      "site": "0046f2c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00492210",
      "incomplete_value": true,
      "site": "00492210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046f378",
      "incomplete_value": true,
      "site": "0046f378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00492210",
      "incomplete_value": false,
      "site": "00492210",
      "value": [
        "leaf",
        "const:48f358:8"
      ]
    },
    "old": {
      "definition_site": "0046f378",
      "incomplete_value": false,
      "site": "0046f378",
      "value": [
        "leaf",
        "const:46c4c0:8"
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
      "00492150",
      "READ",
      [
        "storage",
        "00c25258",
        null,
        "undefined8"
      ]
    ],
    [
      "00492158",
      "WRITE",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "004921c4",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00492150",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00492158",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "004921c4",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046f34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f248.md#insn-0046f34c) · [`0046f4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f248.md#insn-0046f4d0) · [`0046f27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f248.md#insn-0046f27c)
- 新版 [`004921e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md#insn-004921e4) · [`00492368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md#insn-00492368) · [`00492114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md#insn-00492114)

~~~diff
- 0046f34c ["INT_ADD", "register:40f0:8", ["const:46f34c:8", "const:4:8"]]
- 0046f34c ["CALL", null, ["callee:0046cacc:8"]]
+ 004921e4 ["INT_ADD", "register:40f0:8", ["const:4921e4:8", "const:4:8"]]
+ 004921e4 ["CALL", null, ["callee:0046cacc:8"]]
- 0046f34c bytes 3a6aff97
+ 004921e4 bytes 3a6aff97
- 0046f4d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046f4d0 ["INT_ADD", "register:40f0:8", ["const:46f4d0:8", "const:4:8"]]
- 0046f4d0 ["CALLIND", null, ["register:0:8"]]
+ 00492368 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00492368 ["INT_ADD", "register:40f0:8", ["const:492368:8", "const:4:8"]]
+ 00492368 ["CALLIND", null, ["register:0:8"]]
- 0046f4d0 bytes 00013fd6
+ 00492368 bytes 00013fd6
- 0046f27c ["INT_ADD", "register:40f0:8", ["const:46f27c:8", "const:4:8"]]
- 0046f27c ["CALL", null, ["callee:005509c0:8"]]
+ 00492114 ["INT_ADD", "register:40f0:8", ["const:492114:8", "const:4:8"]]
+ 00492114 ["CALL", null, ["callee:005509c0:8"]]
- 0046f27c bytes 2bfa0294
+ 00492114 bytes 2bfa0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-659ecf9f9006f201f061c72544e90d69"></a>

### [`0046f694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f694.md) → [`0049252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049252c.md) FUN_0049252c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00accf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md) · 呼出先 1件 [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md)
- 新版 呼出元 1件 [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md) · 呼出先 1件 [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0049254c",
      "incomplete_value": true,
      "site": "0049254c",
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
      "definition_site": "0046f6b4",
      "incomplete_value": true,
      "site": "0046f6b4",
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
      "definition_site": "0049260c",
      "incomplete_value": false,
      "site": "00492610",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046f774",
      "incomplete_value": false,
      "site": "0046f778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "definition_site": "00492648",
      "incomplete_value": false,
      "site": "0049264c",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046f7b0",
      "incomplete_value": false,
      "site": "0046f7b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "00492548",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "00492558",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00492560",
      "READ",
      [
        "storage",
        "00c24ddc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00492548",
      "READ",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00492558",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "00492560",
      "READ",
      [
        "storage",
        "00ca489c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046f778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f694.md#insn-0046f778) · [`0046f7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f694.md#insn-0046f7b4) · [`0046f84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f694.md#insn-0046f84c)
- 新版 [`00492610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049252c.md#insn-00492610) · [`0049264c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049252c.md#insn-0049264c) · [`004926e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049252c.md#insn-004926e4)

~~~diff
- 0046f778 ["INT_ADD", "register:40f0:8", ["const:46f778:8", "const:4:8"]]
- 0046f778 ["CALL", null, ["callee:0046cacc:8"]]
+ 00492610 ["INT_ADD", "register:40f0:8", ["const:492610:8", "const:4:8"]]
+ 00492610 ["CALL", null, ["callee:0046cacc:8"]]
- 0046f778 bytes 2f69ff97
+ 00492610 bytes 2f69ff97
- 0046f7b4 ["INT_ADD", "register:40f0:8", ["const:46f7b4:8", "const:4:8"]]
- 0046f7b4 ["CALL", null, ["callee:0046cacc:8"]]
+ 0049264c ["INT_ADD", "register:40f0:8", ["const:49264c:8", "const:4:8"]]
+ 0049264c ["CALL", null, ["callee:0046cacc:8"]]
- 0046f7b4 bytes 2069ff97
+ 0049264c bytes 2069ff97
- 0046f84c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046f84c ["INT_ADD", "register:40f0:8", ["const:46f84c:8", "const:4:8"]]
- 0046f84c ["CALLIND", null, ["register:0:8"]]
+ 004926e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004926e4 ["INT_ADD", "register:40f0:8", ["const:4926e4:8", "const:4:8"]]
+ 004926e4 ["CALLIND", null, ["register:0:8"]]
- 0046f84c bytes 00013fd6
+ 004926e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d91de68caf83bba0f89ab9274890a44a"></a>

### [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) → [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) FUN_0049286c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 28件 [`00833158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/00833158.md) [`0083fcf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083fcf4.md) [`0083ff24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083f/0083ff24.md) [`0084c134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c134.md) [`0084c290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c290.md) · 呼出先 9件 [`0046ae68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ae68.md) [`0046b1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b1e0.md) [`0046b618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b618.md) [`0046c588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md) [`004710d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004710d8.md)
- 新版 呼出元 29件 [`007aecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aecf8.md) [`008650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/008650d0.md) [`00871fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871fe0.md) [`00872210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872210.md) [`0087f0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f0cc.md) · 呼出先 9件 [`0048dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e4b0.md) [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md) [`00493f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493f70.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.64% / 新版 82.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00492928",
      "incomplete_value": true,
      "site": "00492928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046fa90",
      "incomplete_value": true,
      "site": "0046fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00492928",
      "incomplete_value": false,
      "site": "00492928",
      "value": [
        "leaf",
        "const:48e4b0:8"
      ]
    },
    "old": {
      "definition_site": "0046fa90",
      "incomplete_value": false,
      "site": "0046fa90",
      "value": [
        "leaf",
        "const:46b618:8"
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00492940",
      "incomplete_value": true,
      "site": "00492940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046faa8",
      "incomplete_value": true,
      "site": "0046faa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0049290c",
      "READ",
      [
        "storage",
        "00c1aed8",
        null,
        "pointer"
      ]
    ],
    [
      "00492910",
      "READ",
      [
        "storage",
        "00c1aee0",
        null,
        "pointer"
      ]
    ],
    [
      "00492928",
      "DATA",
      [
        "storage",
        "00be8a38",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "0049290c",
      "READ",
      [
        "storage",
        "00c9a8c8",
        null,
        "pointer"
      ]
    ],
    [
      "00492910",
      "READ",
      [
        "storage",
        "00c9a8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00492928",
      "DATA",
      [
        "storage",
        "00c655f8",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046fac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md#insn-0046fac4) · [`0046fa28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md#insn-0046fa28) · [`0046fa60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md#insn-0046fa60)
- 新版 [`0049295c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md#insn-0049295c) · [`004928c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md#insn-004928c0) · [`004928f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md#insn-004928f8)

~~~diff
- 0046fac4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0046fac4 ["INT_ADD", "register:40f0:8", ["const:46fac4:8", "const:4:8"]]
- 0046fac4 ["CALLIND", null, ["register:0:8"]]
+ 0049295c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049295c ["INT_ADD", "register:40f0:8", ["const:49295c:8", "const:4:8"]]
+ 0049295c ["CALLIND", null, ["register:0:8"]]
- 0046fac4 bytes 00013fd6
+ 0049295c bytes 00013fd6
- 0046fa28 ["INT_ADD", "register:40f0:8", ["const:46fa28:8", "const:4:8"]]
- 0046fa28 ["CALL", null, ["callee:0048e078:8"]]
+ 004928c0 ["INT_ADD", "register:40f0:8", ["const:4928c0:8", "const:4:8"]]
+ 004928c0 ["CALL", null, ["callee:0048e078:8"]]
- 0046fa28 bytes eeedff97
+ 004928c0 bytes eeedff97
- 0046fa60 ["INT_ADD", "register:40f0:8", ["const:46fa60:8", "const:4:8"]]
- 0046fa60 ["CALL", null, ["callee:0048e078:8"]]
+ 004928f8 ["INT_ADD", "register:40f0:8", ["const:4928f8:8", "const:4:8"]]
+ 004928f8 ["CALL", null, ["callee:0048e078:8"]]
- 0046fa60 bytes e0edff97
+ 004928f8 bytes e0edff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20e74b322a8d52d799326f0475433746"></a>

### [`0046fc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fc48.md) → [`00492ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ae0.md) FUN_00492ae0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00860ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/00860ba8.md) · 呼出先 3件 [`0052db24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db24.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00893b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893b40.md) · 呼出先 3件 [`005509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509bc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 83.93% / 新版 83.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00492b30",
      "incomplete_value": false,
      "site": "00492b30",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046fc98",
      "incomplete_value": false,
      "site": "0046fc98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00492b30",
      "incomplete_value": false,
      "site": "00492b30",
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
                "const:d10:8"
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
      "definition_site": "0046fc98",
      "incomplete_value": false,
      "site": "0046fc98",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:250:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00492af8",
      "incomplete_value": true,
      "site": "00492af8",
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
      "definition_site": "0046fc60",
      "incomplete_value": true,
      "site": "0046fc60",
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
      "00492af4",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "00492b10",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "00492b2c",
      "READ",
      [
        "storage",
        "00c25258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00492af4",
      "READ",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00492b10",
      "READ",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00492b2c",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046fc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fc48.md#insn-0046fc54) · [`0046fc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fc48.md#insn-0046fc5c) · [`0046fc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fc48.md#insn-0046fc70)
- 新版 [`00492aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ae0.md#insn-00492aec) · [`00492af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ae0.md#insn-00492af4) · [`00492b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ae0.md#insn-00492b08)

~~~diff
- 0046fc54 ["COPY", "register:40a0:8", ["const:c25000:8"]]
+ 00492aec ["COPY", "register:40a0:8", ["const:ca4000:8"]]
- 0046fc54 bytes b43d00d0
+ 00492aec bytes 944000d0
- 0046fc5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:250:8"]]
- 0046fc5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00492af4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
+ 00492af4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0046fc5c bytes 882a41f9
+ 00492af4 bytes 888a46f9
- 0046fc70 ["COPY", "register:0:8", ["register:4048:8"]]
- 0046fc70 ["INT_ADD", "register:40f0:8", ["const:46fc70:8", "const:4:8"]]
- 0046fc70 ["CALLIND", null, ["register:0:8"]]
+ 00492b08 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00492b08 ["INT_ADD", "register:40f0:8", ["const:492b08:8", "const:4:8"]]
+ 00492b08 ["CALLIND", null, ["register:0:8"]]
- 0046fc70 bytes 20013fd6
+ 00492b08 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-067d3d3cf4b0f0e262ad4ee74d94012a"></a>

### [`0046fd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fd28.md) → [`00492bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md) FUN_00492bc0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) [`0084d1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d1b4.md) [`0084e780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e780.md) [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) [`008609f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00860/008609f4.md) · 呼出先 3件 [`0052db24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db24.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 11件 [`007ac380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md) [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`0088014c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md) [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 3件 [`005509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509bc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00492be0",
      "incomplete_value": false,
      "site": "00492be0",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046fd48",
      "incomplete_value": false,
      "site": "0046fd48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00492be0",
      "incomplete_value": false,
      "site": "00492be0",
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
                "const:d10:8"
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
      "definition_site": "0046fd48",
      "incomplete_value": false,
      "site": "0046fd48",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:250:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00492be4",
      "incomplete_value": true,
      "site": "00492be4",
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
      "definition_site": "0046fd4c",
      "incomplete_value": true,
      "site": "0046fd4c",
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
      "00492bdc",
      "READ",
      [
        "storage",
        "00c25258",
        null,
        "undefined8"
      ]
    ],
    [
      "00492be0",
      "WRITE",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "00492be0",
      "WRITE",
      [
        "storage",
        "00c25258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00492bdc",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00492be0",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00492be0",
      "WRITE",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046fd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fd28.md#insn-0046fd38) · [`0046fd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fd28.md#insn-0046fd3c) · [`0046fd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fd28.md#insn-0046fd40)
- 新版 [`00492bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md#insn-00492bd0) · [`00492bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md#insn-00492bd4) · [`00492bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md#insn-00492bd8)

~~~diff
- 0046fd38 ["INT_ADD", "register:40f0:8", ["const:46fd38:8", "const:4:8"]]
- 0046fd38 ["CALL", null, ["callee:005509bc:8"]]
+ 00492bd0 ["INT_ADD", "register:40f0:8", ["const:492bd0:8", "const:4:8"]]
+ 00492bd0 ["CALL", null, ["callee:005509bc:8"]]
- 0046fd38 bytes 7bf70294
+ 00492bd0 bytes 7bf70294
- 0046fd3c ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 00492bd4 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0046fd3c bytes a83d00d0
+ 00492bd4 bytes 884000d0
- 0046fd40 ["COPY", "tmp:0:8", ["const:250:8"]]
- 0046fd40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046fd40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046fd40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00492bd8 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00492bd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00492bd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00492bd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046fd40 bytes 08410991
+ 00492bd8 bytes 08413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0f4e9e98052975b87e9bdba6792234f"></a>

### [`00470130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470130.md) → [`00492fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492fc8.md) FUN_00492fc8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00470050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470050.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00844bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004703fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/004703fc.md) [`004715ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004715ac.md) [`004715b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/004715b0.md) [`0052db38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db38.md)
- 新版 呼出元 5件 [`00492ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00493294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493294.md) [`00494444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494444.md) [`00494448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494448.md) [`005509d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 5件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00493018",
      "incomplete_value": false,
      "site": "00493018",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00470180",
      "incomplete_value": false,
      "site": "00470180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00493034",
      "incomplete_value": false,
      "site": "00493034",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047019c",
      "incomplete_value": false,
      "site": "0047019c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00493100",
      "incomplete_value": true,
      "site": "00493100",
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
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00470268",
      "incomplete_value": true,
      "site": "00470268",
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
            "const:2c8:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00493004",
      "READ",
      [
        "storage",
        "00c252e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00493010",
      "READ",
      [
        "storage",
        "00c252c0",
        null,
        "undefined4"
      ]
    ],
    [
      "00493018",
      "WRITE",
      [
        "storage",
        "00c252c0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00493004",
      "READ",
      [
        "storage",
        "00ca4da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00493010",
      "READ",
      [
        "storage",
        "00ca4d80",
        null,
        "undefined4"
      ]
    ],
    [
      "00493018",
      "WRITE",
      [
        "storage",
        "00ca4d80",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00470180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470130.md#insn-00470180) · [`00470268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470130.md#insn-00470268) · [`00470334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470130.md#insn-00470334)
- 新版 [`00493018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492fc8.md#insn-00493018) · [`00493100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492fc8.md#insn-00493100) · [`004931cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492fc8.md#insn-004931cc)

~~~diff
- 00470180 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c0:8"]]
- 00470180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:4"]]
+ 00493018 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 00493018 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:4"]]
- 00470180 bytes 15c102b9
+ 00493018 bytes 15810db9
- 00470268 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c8:8"]]
- 00470268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00493100 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d88:8"]]
+ 00493100 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00470268 bytes 096501f9
+ 00493100 bytes 09c506f9
- 00470334 ["INT_ADD", "register:40f0:8", ["const:470334:8", "const:4:8"]]
- 00470334 ["CALL", null, ["callee:00c57a50:8"]]
+ 004931cc ["INT_ADD", "register:40f0:8", ["const:4931cc:8", "const:4:8"]]
+ 004931cc ["CALL", null, ["callee:00c57a50:8"]]
- 00470334 bytes 33ab1d94
+ 004931cc bytes 21121f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

