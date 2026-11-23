# v15.7.4 → v16.0.0 · 最優先の変更候補 (1)

[一覧の目次](README.md)

<a id="compare-7509f196a2233dea8035ba720c17de88"></a>

### [`00418338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418338.md) → [`0043ae38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae38.md) _INIT_3

採用 · 移動量 `+0x22b00` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b7d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2a0.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bf9ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ce8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 65.22% / 新版 65.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043ae54",
      "incomplete_value": false,
      "site": "0043ae58",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418354",
      "incomplete_value": false,
      "site": "00418358",
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
            "const:a40:8"
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
      "definition_site": "0043ae6c",
      "incomplete_value": true,
      "site": "0043ae78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:760:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041836c",
      "incomplete_value": true,
      "site": "00418378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
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
      "definition_site": "0043ae68",
      "incomplete_value": false,
      "site": "0043ae78",
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
      "definition_site": "00418368",
      "incomplete_value": false,
      "site": "00418378",
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
      "0043ae48",
      "READ",
      [
        "storage",
        "00c24a40",
        null,
        "undefined1"
      ]
    ],
    [
      "0043ae54",
      "PARAM",
      [
        "storage",
        "00c24a40",
        null,
        "undefined1"
      ]
    ],
    [
      "0043ae68",
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
      "0043ae48",
      "READ",
      [
        "storage",
        "00ca4500",
        null,
        "undefined1"
      ]
    ],
    [
      "0043ae54",
      "PARAM",
      [
        "storage",
        "00ca4500",
        null,
        "undefined1"
      ]
    ],
    [
      "0043ae68",
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

- 旧版 [`00418358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418338.md#insn-00418358) · [`00418378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418338.md#insn-00418378) · [`00418340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418338.md#insn-00418340)
- 新版 `0043ae58`（命令位置の公開資料なし） · `0043ae78`（命令位置の公開資料なし） · `0043ae40`（命令位置の公開資料なし）

~~~diff
- 00418358 ["INT_ADD", "register:40f0:8", ["const:418358:8", "const:4:8"]]
- 00418358 ["CALL", null, ["callee:00c57a50:8"]]
+ 0043ae58 ["INT_ADD", "register:40f0:8", ["const:43ae58:8", "const:4:8"]]
+ 0043ae58 ["CALL", null, ["callee:00c57a50:8"]]
- 00418358 bytes 2a0b1f94
+ 0043ae58 bytes fe722094
- 00418378 ["INT_ADD", "register:40f0:8", ["const:418378:8", "const:4:8"]]
- 00418378 ["CALL", null, ["callee:00c57a30:8"]]
+ 0043ae78 ["INT_ADD", "register:40f0:8", ["const:43ae78:8", "const:4:8"]]
+ 0043ae78 ["CALL", null, ["callee:00c57a30:8"]]
- 00418378 bytes 1a0b1f94
+ 0043ae78 bytes ee722094
- 00418340 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043ae40 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00418340 bytes 68400090
+ 0043ae40 bytes 484300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a93b45fb81c33a700d6e28aa115d2607"></a>

### [`004183ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183ec.md) → [`0043aeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043aeec.md) Java_jp_co_ponos_battlecats_MyActivity_appInit

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0053c5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5e8.md) [`00547c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547c90.md) [`00acba34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acba34.md) [`00acc348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc348.md) [`00accf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0055f480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f480.md) [`0056ab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) [`00b2b4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4c4.md) [`00b2bdd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bdd8.md) [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043af30",
      "incomplete_value": false,
      "site": "0043af3c",
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
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418430",
      "incomplete_value": false,
      "site": "0041843c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043af54",
      "incomplete_value": false,
      "site": "0043af54",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418454",
      "incomplete_value": false,
      "site": "00418454",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043af54",
      "incomplete_value": false,
      "site": "0043af54",
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
                "const:510:8"
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
      "definition_site": "00418454",
      "incomplete_value": false,
      "site": "00418454",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:a50:8"
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
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043af00",
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      "0043af3c",
      "DATA",
      [
        "storage",
        "00be5fe8",
        null,
        "undefined *"
      ]
    ],
    [
      "0043af50",
      "READ",
      [
        "storage",
        "00c24a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043af00",
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      "0043af3c",
      "DATA",
      [
        "storage",
        "00c62ba8",
        null,
        "undefined *"
      ]
    ],
    [
      "0043af50",
      "READ",
      [
        "storage",
        "00ca4518",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183ec.md#insn-00418488) · [`004183fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183ec.md#insn-004183fc) · [`00418400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183ec.md#insn-00418400)
- 新版 `0043af88`（命令位置の公開資料なし） · `0043aefc`（命令位置の公開資料なし） · `0043af00`（命令位置の公開資料なし）

~~~diff
- 00418488 ["INT_ADD", "register:40f0:8", ["const:418488:8", "const:4:8"]]
- 00418488 ["CALL", null, ["ram:accf90:8"]]
+ 0043af88 ["INT_ADD", "register:40f0:8", ["const:43af88:8", "const:4:8"]]
+ 0043af88 ["CALL", null, ["ram:b2ca20:8"]]
- 00418488 bytes c2d21a94
+ 0043af88 bytes a6c61b94
- 004183fc ["COPY", "register:40b0:8", ["const:c24000:8"]]
+ 0043aefc ["COPY", "register:40b0:8", ["const:ca4000:8"]]
- 004183fc bytes 76400090
+ 0043aefc bytes 564300d0
- 00418400 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a50:8"]]
- 00418400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043af00 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:510:8"]]
+ 0043af00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00418400 bytes c82a45f9
+ 0043af00 bytes c88a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f681d49df4ec2b70d3f9b52a208cd4b"></a>

### [`004184bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004184bc.md) → [`0043afbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043afbc.md) Java_jp_co_ponos_battlecats_MyActivity_appUpdateDraw

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0053257c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053257c.md) [`0056cb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cb70.md) [`00acba3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acba3c.md) [`00acd468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd468.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00555414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555414.md) [`0058fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md) [`00b2b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md) [`00b2cf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cf0c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 77.19% / 新版 77.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b028",
      "incomplete_value": true,
      "site": "0043b028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418528",
      "incomplete_value": true,
      "site": "00418528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "definition_site": "0043b088",
      "incomplete_value": true,
      "site": "0043b088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418588",
      "incomplete_value": true,
      "site": "00418588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0043b01c",
      "value": [
        "leaf",
        "ram:b2cf0c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0041851c",
      "value": [
        "leaf",
        "ram:acd468:8"
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
      "0043afe8",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined1"
      ]
    ],
    [
      "0043aff4",
      "READ",
      [
        "storage",
        "00c24a60",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b004",
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043afe8",
      "READ",
      [
        "storage",
        "00ca4528",
        null,
        "undefined1"
      ]
    ],
    [
      "0043aff4",
      "READ",
      [
        "storage",
        "00ca4520",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b004",
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041851c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004184bc.md#insn-0041851c) · [`00418528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004184bc.md#insn-00418528) · [`0041854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004184bc.md#insn-0041854c)
- 新版 `0043b01c`（命令位置の公開資料なし） · `0043b028`（命令位置の公開資料なし） · `0043b04c`（命令位置の公開資料なし）

~~~diff
- 0041851c ["INT_ADD", "register:40f0:8", ["const:41851c:8", "const:4:8"]]
- 0041851c ["CALL", null, ["ram:acd468:8"]]
+ 0043b01c ["INT_ADD", "register:40f0:8", ["const:43b01c:8", "const:4:8"]]
+ 0043b01c ["CALL", null, ["ram:b2cf0c:8"]]
- 0041851c bytes d3d31a94
+ 0043b01c bytes bcc71b94
- 00418528 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a60:8"]]
- 00418528 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043b028 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:520:8"]]
+ 0043b028 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00418528 bytes b33205f9
+ 0043b028 bytes b39202f9
- 0041854c ["INT_ADD", "register:40f0:8", ["const:41854c:8", "const:4:8"]]
- 0041854c ["CALL", null, ["callee:00b2b4cc:8"]]
+ 0043b04c ["INT_ADD", "register:40f0:8", ["const:43b04c:8", "const:4:8"]]
+ 0043b04c ["CALL", null, ["callee:00b2b4cc:8"]]
- 0041854c bytes 3ccd1a94
+ 0043b04c bytes 20c11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f879a9350a7923ed45c5fb0e8d678646"></a>

### [`004185a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004185a8.md) → [`0043b0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b0a8.md) Java_jp_co_ponos_battlecats_MyActivity_gfxInit

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`004186bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004186bc.md) [`0056c8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c8a4.md) [`0056f4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056f/0056f4d8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043b1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b1bc.md) [`0058f73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f73c.md) [`00592370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00592/00592370.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.51% / 新版 85.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b0f0",
      "incomplete_value": false,
      "site": "0043b0f0",
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
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004185f0",
      "incomplete_value": false,
      "site": "004185f0",
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
            "const:a70:8"
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
      "definition_site": "0043b0f4",
      "incomplete_value": true,
      "site": "0043b0f4",
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
      "definition_site": "004185f4",
      "incomplete_value": true,
      "site": "004185f4",
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
      "definition_site": "0043b154",
      "incomplete_value": true,
      "site": "0043b158",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418654",
      "incomplete_value": true,
      "site": "00418658",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:a70:8"
              ]
            ]
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
      "0043b0cc",
      "READ",
      [
        "storage",
        "00c24a80",
        null,
        "undefined1"
      ]
    ],
    [
      "0043b0e8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b0f0",
      "WRITE",
      [
        "storage",
        "00c24a70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043b0cc",
      "READ",
      [
        "storage",
        "00ca4540",
        null,
        "undefined1"
      ]
    ],
    [
      "0043b0e8",
      "READ",
      [
        "storage",
        "00ca4538",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b0f0",
      "WRITE",
      [
        "storage",
        "00ca4530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004185a8.md#insn-00418658) · [`00418684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004185a8.md#insn-00418684) · [`004186a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004185a8.md#insn-004186a4)
- 新版 `0043b158`（命令位置の公開資料なし） · `0043b184`（命令位置の公開資料なし） · `0043b1a4`（命令位置の公開資料なし）

~~~diff
- 00418658 ["INT_ADD", "register:40f0:8", ["const:418658:8", "const:4:8"]]
- 00418658 ["CALL", null, ["callee:0058f73c:8"]]
+ 0043b158 ["INT_ADD", "register:40f0:8", ["const:43b158:8", "const:4:8"]]
+ 0043b158 ["CALL", null, ["callee:0058f73c:8"]]
- 00418658 bytes 93500594
+ 0043b158 bytes 79510594
- 00418684 ["INT_ADD", "register:40f0:8", ["const:418684:8", "const:4:8"]]
- 00418684 ["CALL", null, ["callee:00c57a50:8"]]
+ 0043b184 ["INT_ADD", "register:40f0:8", ["const:43b184:8", "const:4:8"]]
+ 0043b184 ["CALL", null, ["callee:00c57a50:8"]]
- 00418684 bytes 5f0a1f94
+ 0043b184 bytes 33722094
- 004186a4 ["INT_ADD", "register:40f0:8", ["const:4186a4:8", "const:4:8"]]
- 004186a4 ["CALL", null, ["callee:00c57a30:8"]]
+ 0043b1a4 ["INT_ADD", "register:40f0:8", ["const:43b1a4:8", "const:4:8"]]
+ 0043b1a4 ["CALL", null, ["callee:00c57a30:8"]]
- 004186a4 bytes 4f0a1f94
+ 0043b1a4 bytes 23722094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-491f70982a915bc09e129eace195f180"></a>

### [`0041870c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041870c.md) → [`0043b20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b20c.md) Java_jp_co_ponos_battlecats_MyActivity_getDrawableWidth

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b214",
      "incomplete_value": true,
      "site": "0043b218",
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
      "definition_site": "00418714",
      "incomplete_value": true,
      "site": "00418718",
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
      "0043b214",
      "READ",
      [
        "storage",
        "00c24dc8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b214",
      "READ",
      [
        "storage",
        "00ca4888",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041870c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041870c.md#insn-0041870c) · [`00418710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041870c.md#insn-00418710)
- 新版 `0043b20c`（命令位置の公開資料なし） · `0043b210`（命令位置の公開資料なし）

~~~diff
- 0041870c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043b20c ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0041870c bytes 68400090
+ 0043b20c bytes 484300b0
- 00418710 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00418710 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418710 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418710 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b210 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 0043b210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418710 bytes 08c13691
+ 0043b210 bytes 08c12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b1630ccfe38fdef40aede574245217b"></a>

### [`0041871c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041871c.md) → [`0043b21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b21c.md) Java_jp_co_ponos_battlecats_MyActivity_getDrawableHeight

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b224",
      "incomplete_value": true,
      "site": "0043b228",
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
      "definition_site": "00418724",
      "incomplete_value": true,
      "site": "00418728",
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
      "0043b224",
      "READ",
      [
        "storage",
        "00c24dcc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b224",
      "READ",
      [
        "storage",
        "00ca488c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041871c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041871c.md#insn-0041871c) · [`00418720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041871c.md#insn-00418720)
- 新版 `0043b21c`（命令位置の公開資料なし） · `0043b220`（命令位置の公開資料なし）

~~~diff
- 0041871c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043b21c ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0041871c bytes 68400090
+ 0043b21c bytes 484300b0
- 00418720 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00418720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b220 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 0043b220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418720 bytes 08c13691
+ 0043b220 bytes 08c12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e925c06765f9b0c1f1a1b7f0e3015e0"></a>

### [`0041872c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041872c.md) → [`0043b22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b22c.md) Java_jp_co_ponos_battlecats_MyActivity_getWindowWidth

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b234",
      "incomplete_value": true,
      "site": "0043b238",
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
      "definition_site": "00418734",
      "incomplete_value": true,
      "site": "00418738",
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
      "0043b234",
      "READ",
      [
        "storage",
        "00c24db8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b234",
      "READ",
      [
        "storage",
        "00ca4878",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041872c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041872c.md#insn-0041872c) · [`00418730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041872c.md#insn-00418730)
- 新版 `0043b22c`（命令位置の公開資料なし） · `0043b230`（命令位置の公開資料なし）

~~~diff
- 0041872c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043b22c ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0041872c bytes 68400090
+ 0043b22c bytes 484300b0
- 00418730 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00418730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b230 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 0043b230 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b230 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b230 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418730 bytes 08c13691
+ 0043b230 bytes 08c12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47c9f93dc54a40fc680f878782c8e94a"></a>

### [`0041873c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041873c.md) → [`0043b23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b23c.md) Java_jp_co_ponos_battlecats_MyActivity_getWindowHeight

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b244",
      "incomplete_value": true,
      "site": "0043b248",
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
      "definition_site": "00418744",
      "incomplete_value": true,
      "site": "00418748",
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
      "0043b244",
      "READ",
      [
        "storage",
        "00c24dbc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b244",
      "READ",
      [
        "storage",
        "00ca487c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041873c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041873c.md#insn-0041873c) · [`00418740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041873c.md#insn-00418740)
- 新版 `0043b23c`（命令位置の公開資料なし） · `0043b240`（命令位置の公開資料なし）

~~~diff
- 0041873c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043b23c ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0041873c bytes 68400090
+ 0043b23c bytes 484300b0
- 00418740 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00418740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b240 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 0043b240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418740 bytes 08c13691
+ 0043b240 bytes 08c12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3de8a2e552ab627eed3bd60c4358008"></a>

### [`0041874c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041874c.md) → [`0043b24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b24c.md) Java_jp_co_ponos_battlecats_MyActivity_getSizeWidth

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b254",
      "incomplete_value": true,
      "site": "0043b258",
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
      "definition_site": "00418754",
      "incomplete_value": true,
      "site": "00418758",
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
      "0043b254",
      "READ",
      [
        "storage",
        "00c24dc0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b254",
      "READ",
      [
        "storage",
        "00ca4880",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041874c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041874c.md#insn-0041874c) · [`00418750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041874c.md#insn-00418750)
- 新版 `0043b24c`（命令位置の公開資料なし） · `0043b250`（命令位置の公開資料なし）

~~~diff
- 0041874c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043b24c ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0041874c bytes 68400090
+ 0043b24c bytes 484300b0
- 00418750 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00418750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b250 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 0043b250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418750 bytes 08c13691
+ 0043b250 bytes 08c12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f21864e0b7dfba1ffab0987eb8685b05"></a>

### [`0041875c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041875c.md) → [`0043b25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b25c.md) Java_jp_co_ponos_battlecats_MyActivity_getSizeHeight

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0043b264",
      "incomplete_value": true,
      "site": "0043b268",
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
      "definition_site": "00418764",
      "incomplete_value": true,
      "site": "00418768",
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
      "0043b264",
      "READ",
      [
        "storage",
        "00c24dc4",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b264",
      "READ",
      [
        "storage",
        "00ca4884",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041875c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041875c.md#insn-0041875c) · [`00418760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041875c.md#insn-00418760)
- 新版 `0043b25c`（命令位置の公開資料なし） · `0043b260`（命令位置の公開資料なし）

~~~diff
- 0041875c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043b25c ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0041875c bytes 68400090
+ 0043b25c bytes 484300b0
- 00418760 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00418760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b260 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 0043b260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418760 bytes 08c13691
+ 0043b260 bytes 08c12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16dc9854cc230088ce024c165e132fe8"></a>

### [`0041876c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041876c.md) → [`0043b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b26c.md) Java_jp_co_ponos_battlecats_MyActivity_gfxResize

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056cb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cb70.md) [`00accf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fa08.md) [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md)

変更の種類 branch_value, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 72.34% / 新版 72.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b2c8",
      "incomplete_value": true,
      "site": "0043b2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004187c8",
      "incomplete_value": true,
      "site": "004187c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:2c:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b2c8",
      "incomplete_value": true,
      "site": "0043b2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:2c:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004187c8",
      "incomplete_value": true,
      "site": "004187c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:2c:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b2f4",
      "incomplete_value": true,
      "site": "0043b2f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004187f4",
      "incomplete_value": true,
      "site": "004187f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:2c:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043b284",
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ],
    [
      "0043b288",
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      "0043b294",
      "READ",
      [
        "storage",
        "00c2659c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b284",
      "READ",
      [
        "storage",
        "00c9a770",
        null,
        "pointer"
      ]
    ],
    [
      "0043b288",
      "READ",
      [
        "storage",
        "00c9a778",
        null,
        "pointer"
      ]
    ],
    [
      "0043b294",
      "READ",
      [
        "storage",
        "00ca605c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041876c.md#insn-00418778) · [`0041877c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041876c.md#insn-0041877c) · [`00418780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/0041876c.md#insn-00418780)
- 新版 `0043b278`（命令位置の公開資料なし） · `0043b27c`（命令位置の公開資料なし） · `0043b280`（命令位置の公開資料なし）

~~~diff
- 00418778 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0043b278 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00418778 bytes 084000d0
+ 0043b278 bytes e84200f0
- 0041877c ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 0043b27c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0041877c bytes 094000d0
+ 0043b27c bytes e94200f0
- 00418780 ["COPY", "register:4050:8", ["const:c1a000:8"]]
+ 0043b280 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 00418780 bytes 0a4000d0
+ 0043b280 bytes ea4200f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9c4fe8cbb6d08a96942e18a3d209af5"></a>

### [`00418828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md) → [`0043b328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b328.md) Java_jp_co_ponos_battlecats_MyActivity_appTouch

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00acd390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd390.md) [`00acd3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd3d8.md) [`00acd420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd420.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b2ce34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce34.md) [`00b2ce7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce7c.md) [`00b2cec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cec4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b3d0",
      "incomplete_value": true,
      "site": "0043b3d0",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004188d0",
      "incomplete_value": true,
      "site": "004188d0",
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
            "const:a88:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b3d4",
      "incomplete_value": true,
      "site": "0043b3d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:54c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004188d4",
      "incomplete_value": true,
      "site": "004188d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a8c:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043b374",
      "incomplete_value": true,
      "site": "0043b37c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:510:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418874",
      "incomplete_value": true,
      "site": "0041887c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
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
      "0043b374",
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b398",
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b3a8",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0043b374",
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b398",
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b3a8",
      "READ",
      [
        "storage",
        "00ca4548",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041887c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md#insn-0041887c) · [`004188a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md#insn-004188a0) · [`004188cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418828.md#insn-004188cc)
- 新版 `0043b37c`（命令位置の公開資料なし） · `0043b3a0`（命令位置の公開資料なし） · `0043b3cc`（命令位置の公開資料なし）

~~~diff
- 0041887c ["INT_ADD", "register:40f0:8", ["const:41887c:8", "const:4:8"]]
- 0041887c ["CALL", null, ["callee:00b2ce7c:8"]]
+ 0043b37c ["INT_ADD", "register:40f0:8", ["const:43b37c:8", "const:4:8"]]
+ 0043b37c ["CALL", null, ["callee:00b2ce7c:8"]]
- 0041887c bytes d7d21a94
+ 0043b37c bytes c0c61b94
- 004188a0 ["INT_ADD", "register:40f0:8", ["const:4188a0:8", "const:4:8"]]
- 004188a0 ["CALL", null, ["callee:00b2cec4:8"]]
+ 0043b3a0 ["INT_ADD", "register:40f0:8", ["const:43b3a0:8", "const:4:8"]]
+ 0043b3a0 ["CALL", null, ["callee:00b2cec4:8"]]
- 004188a0 bytes e0d21a94
+ 0043b3a0 bytes c9c61b94
- 004188cc ["INT_ADD", "register:40f0:8", ["const:4188cc:8", "const:4:8"]]
- 004188cc ["CALL", null, ["callee:00b2ce34:8"]]
+ 0043b3cc ["INT_ADD", "register:40f0:8", ["const:43b3cc:8", "const:4:8"]]
+ 0043b3cc ["CALL", null, ["callee:00b2ce34:8"]]
- 004188cc bytes b1d21a94
+ 0043b3cc bytes 9ac61b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1ae1ee5f36f1d08558343443aec4fcf"></a>

### [`004188e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004188e8.md) → [`0043b3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b3e8.md) Java_jp_co_ponos_battlecats_MyActivity_appKey

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00acbd78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd78.md) [`00acbd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd7c.md) [`00acd38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd38c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00b2b808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b808.md) [`00b2b80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b80c.md) [`00b2ce30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ce30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "site": "0043b4c4",
      "value": [
        "leaf",
        "ram:b2b80c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004189c4",
      "value": [
        "leaf",
        "ram:acbd7c:8"
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
      "site": "0043b4ec",
      "value": [
        "leaf",
        "ram:b2ce30:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004189ec",
      "value": [
        "leaf",
        "ram:acd38c:8"
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
      "0043b424",
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b460",
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b474",
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043b424",
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b460",
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b474",
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004189c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004188e8.md#insn-004189c4) · [`004189ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004188e8.md#insn-004189ec) · [`00418920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004188e8.md#insn-00418920)
- 新版 `0043b4c4`（命令位置の公開資料なし） · `0043b4ec`（命令位置の公開資料なし） · `0043b420`（命令位置の公開資料なし）

~~~diff
- 004189c4 ["INT_ADD", "register:40f0:8", ["const:4189c4:8", "const:4:8"]]
- 004189c4 ["CALL", null, ["ram:acbd7c:8"]]
+ 0043b4c4 ["INT_ADD", "register:40f0:8", ["const:43b4c4:8", "const:4:8"]]
+ 0043b4c4 ["CALL", null, ["ram:b2b80c:8"]]
- 004189c4 bytes eecc1a94
+ 0043b4c4 bytes d2c01b94
- 004189ec ["INT_ADD", "register:40f0:8", ["const:4189ec:8", "const:4:8"]]
- 004189ec ["CALL", null, ["ram:acd38c:8"]]
+ 0043b4ec ["INT_ADD", "register:40f0:8", ["const:43b4ec:8", "const:4:8"]]
+ 0043b4ec ["CALL", null, ["ram:b2ce30:8"]]
- 004189ec bytes 68d21a94
+ 0043b4ec bytes 51c61b94
- 00418920 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043b420 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00418920 bytes 68400090
+ 0043b420 bytes 484300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-166715ca571e398ec925242e8d54ab8b"></a>

### [`00418b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b18.md) → [`0043b618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b618.md) Java_jp_co_ponos_battlecats_MyActivity_kill

採用 · 移動量 `+0x22b00` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00acbd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbd14.md) [`00acc56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc56c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b2b7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md) [`00b2bffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bffc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043b630",
      "incomplete_value": true,
      "site": "0043b634",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:510:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418b30",
      "incomplete_value": true,
      "site": "00418b34",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
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
      "0043b630",
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b638",
      "READ",
      [
        "storage",
        "00c24a50",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b640",
      "READ",
      [
        "storage",
        "00c24a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043b630",
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b638",
      "READ",
      [
        "storage",
        "00ca4510",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b640",
      "READ",
      [
        "storage",
        "00ca4518",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b18.md#insn-00418b34) · [`00418b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b18.md#insn-00418b24) · [`00418b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b18.md#insn-00418b28)
- 新版 `0043b634`（命令位置の公開資料なし） · `0043b624`（命令位置の公開資料なし） · `0043b628`（命令位置の公開資料なし）

~~~diff
- 00418b34 ["INT_ADD", "register:40f0:8", ["const:418b34:8", "const:4:8"]]
- 00418b34 ["CALL", null, ["callee:00b2b7a4:8"]]
+ 0043b634 ["INT_ADD", "register:40f0:8", ["const:43b634:8", "const:4:8"]]
+ 0043b634 ["CALL", null, ["callee:00b2b7a4:8"]]
- 00418b34 bytes 78cc1a94
+ 0043b634 bytes 5cc01b94
- 00418b24 ["COPY", "register:40a0:8", ["const:c24000:8"]]
+ 0043b624 ["COPY", "register:40a0:8", ["const:ca4000:8"]]
- 00418b24 bytes 74400090
+ 0043b624 bytes 544300b0
- 00418b28 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 00418b28 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00418b28 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00418b28 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 0043b628 ["COPY", "tmp:0:8", ["const:510:8"]]
+ 0043b628 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 0043b628 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 0043b628 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00418b28 bytes 94422991
+ 0043b628 bytes 94421491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-724b4be842a97559f3177b73c3cd0163"></a>

### [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) → [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) FUN_0043b724

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 272件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041ac3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 272件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043d73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440c0c.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0043b734",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00418c34",
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
      "definition_site": "0043b730",
      "incomplete_value": false,
      "site": "0043b734",
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
            "const:ee3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418c30",
      "incomplete_value": false,
      "site": "00418c34",
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
            "const:24c:8"
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
      "0043b730",
      "PARAM",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ],
    [
      "0043b734",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0043b730",
      "PARAM",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ],
    [
      "0043b734",
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

- 旧版 [`00418c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md#insn-00418c34) · [`00418c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md#insn-00418c2c) · [`00418c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md#insn-00418c30)
- 新版 `0043b734`（命令位置の公開資料なし） · `0043b72c`（命令位置の公開資料なし） · `0043b730`（命令位置の公開資料なし）

~~~diff
- 00418c34 ["INT_ADD", "register:40f0:8", ["const:418c34:8", "const:4:8"]]
- 00418c34 ["CALL", null, ["ram:418c38:8"]]
+ 0043b734 ["INT_ADD", "register:40f0:8", ["const:43b734:8", "const:4:8"]]
+ 0043b734 ["CALL", null, ["ram:43b738:8"]]
- 00418c34 bytes 01000094
+ 0043b734 bytes 01000094
- 00418c2c ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 0043b72c ["COPY", "register:4000:8", ["const:2b9000:8"]]
- 00418c2c bytes 80f4ffb0
+ 0043b72c bytes e0f3ffd0
- 00418c30 ["COPY", "tmp:0:8", ["const:24c:8"]]
- 00418c30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00418c30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00418c30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0043b730 ["COPY", "tmp:0:8", ["const:ee3:8"]]
+ 0043b730 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0043b730 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0043b730 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00418c30 bytes 00300991
+ 0043b730 bytes 008c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef3aaa7c2f7e7fc353865c9dfeecfa69"></a>

### [`00419294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419294.md) → [`0043bd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bd94.md) _INIT_4

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418394.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043ae94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae94.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043bdd0",
      "incomplete_value": true,
      "site": "0043bdec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004192d0",
      "incomplete_value": true,
      "site": "004192ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0043bdf4",
      "incomplete_value": true,
      "site": "0043be10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004192f4",
      "incomplete_value": true,
      "site": "00419310",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0043be14",
      "incomplete_value": true,
      "site": "0043be30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00419314",
      "incomplete_value": true,
      "site": "00419330",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0043bdd0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0043bdf4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0043be14",
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
      "0043bdd0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0043bdf4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0043be14",
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

- 旧版 [`004193f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419294.md#insn-004193f4) · [`004194cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419294.md#insn-004194cc) · [`004194e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419294.md#insn-004194e4)
- 新版 `0043bef4`（命令位置の公開資料なし） · `0043bfcc`（命令位置の公開資料なし） · `0043bfe4`（命令位置の公開資料なし）

~~~diff
- 004193f4 ["INT_ADD", "register:40f0:8", ["const:4193f4:8", "const:4:8"]]
- 004193f4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0043bef4 ["INT_ADD", "register:40f0:8", ["const:43bef4:8", "const:4:8"]]
+ 0043bef4 ["CALL", null, ["callee:0043b7b8:8"]]
- 004193f4 bytes 31feff97
+ 0043bef4 bytes 31feff97
- 004194cc ["INT_ADD", "register:40f0:8", ["const:4194cc:8", "const:4:8"]]
- 004194cc ["CALL", null, ["callee:00c57a30:8"]]
+ 0043bfcc ["INT_ADD", "register:40f0:8", ["const:43bfcc:8", "const:4:8"]]
+ 0043bfcc ["CALL", null, ["callee:00c57a30:8"]]
- 004194cc bytes c5061f94
+ 0043bfcc bytes 996e2094
- 004194e4 ["INT_ADD", "register:40f0:8", ["const:4194e4:8", "const:4:8"]]
- 004194e4 ["CALL", null, ["callee:00c57a30:8"]]
+ 0043bfe4 ["INT_ADD", "register:40f0:8", ["const:43bfe4:8", "const:4:8"]]
+ 0043bfe4 ["CALL", null, ["callee:00c57a30:8"]]
- 004194e4 bytes bf061f94
+ 0043bfe4 bytes 936e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed7c06bfaec14921fc338f6b2a2dbe1f"></a>

### [`00419640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419640.md) → [`0043c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c140.md) _INIT_5

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041969c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/0041969c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043c19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c19c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 69.57% / 新版 69.57%

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
      "definition_site": "0043c15c",
      "incomplete_value": false,
      "site": "0043c160",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041965c",
      "incomplete_value": false,
      "site": "00419660",
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
            "const:ab0:8"
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
      "definition_site": "0043c16c",
      "incomplete_value": false,
      "site": "0043c180",
      "value": [
        "leaf",
        "const:43c19c:8"
      ]
    },
    "old": {
      "definition_site": "0041966c",
      "incomplete_value": false,
      "site": "00419680",
      "value": [
        "leaf",
        "const:41969c:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043c174",
      "incomplete_value": false,
      "site": "0043c180",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00419674",
      "incomplete_value": false,
      "site": "00419680",
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
            "const:aa8:8"
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
      "0043c150",
      "READ",
      [
        "storage",
        "00c24ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c15c",
      "PARAM",
      [
        "storage",
        "00c24ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c16c",
      "PARAM",
      [
        "storage",
        "0041969c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0043c150",
      "READ",
      [
        "storage",
        "00ca4570",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c15c",
      "PARAM",
      [
        "storage",
        "00ca4570",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c16c",
      "PARAM",
      [
        "storage",
        "0043c19c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00419660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419640.md#insn-00419660) · [`00419680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419640.md#insn-00419680) · [`00419648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419640.md#insn-00419648)
- 新版 `0043c160`（命令位置の公開資料なし） · `0043c180`（命令位置の公開資料なし） · `0043c148`（命令位置の公開資料なし）

~~~diff
- 00419660 ["INT_ADD", "register:40f0:8", ["const:419660:8", "const:4:8"]]
- 00419660 ["CALL", null, ["callee:00c57a50:8"]]
+ 0043c160 ["INT_ADD", "register:40f0:8", ["const:43c160:8", "const:4:8"]]
+ 0043c160 ["CALL", null, ["callee:00c57a50:8"]]
- 00419660 bytes 68061f94
+ 0043c160 bytes 3c6e2094
- 00419680 ["INT_ADD", "register:40f0:8", ["const:419680:8", "const:4:8"]]
- 00419680 ["CALL", null, ["callee:00c57a30:8"]]
+ 0043c180 ["INT_ADD", "register:40f0:8", ["const:43c180:8", "const:4:8"]]
+ 0043c180 ["CALL", null, ["callee:00c57a30:8"]]
- 00419680 bytes 58061f94
+ 0043c180 bytes 2c6e2094
- 00419648 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043c148 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00419648 bytes 484000f0
+ 0043c148 bytes 48430090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe645b50ee217722ee4fc21c03141d4d"></a>

### [`004196bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/004196bc.md) → [`0043c1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c1bc.md) _INIT_6

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041969c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/0041969c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043c19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c19c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 69.57% / 新版 69.57%

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
      "definition_site": "0043c1d8",
      "incomplete_value": false,
      "site": "0043c1dc",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004196d8",
      "incomplete_value": false,
      "site": "004196dc",
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
            "const:ac0:8"
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
      "definition_site": "0043c1e8",
      "incomplete_value": false,
      "site": "0043c1fc",
      "value": [
        "leaf",
        "const:43c19c:8"
      ]
    },
    "old": {
      "definition_site": "004196e8",
      "incomplete_value": false,
      "site": "004196fc",
      "value": [
        "leaf",
        "const:41969c:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043c1f0",
      "incomplete_value": false,
      "site": "0043c1fc",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004196f0",
      "incomplete_value": false,
      "site": "004196fc",
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
            "const:ab8:8"
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
      "0043c1cc",
      "READ",
      [
        "storage",
        "00c24ac0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c1d8",
      "PARAM",
      [
        "storage",
        "00c24ac0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c1e8",
      "PARAM",
      [
        "storage",
        "0041969c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0043c1cc",
      "READ",
      [
        "storage",
        "00ca4580",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c1d8",
      "PARAM",
      [
        "storage",
        "00ca4580",
        null,
        "undefined1"
      ]
    ],
    [
      "0043c1e8",
      "PARAM",
      [
        "storage",
        "0043c19c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004196dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/004196bc.md#insn-004196dc) · [`004196fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/004196bc.md#insn-004196fc) · [`004196c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/004196bc.md#insn-004196c4)
- 新版 `0043c1dc`（命令位置の公開資料なし） · `0043c1fc`（命令位置の公開資料なし） · `0043c1c4`（命令位置の公開資料なし）

~~~diff
- 004196dc ["INT_ADD", "register:40f0:8", ["const:4196dc:8", "const:4:8"]]
- 004196dc ["CALL", null, ["callee:00c57a50:8"]]
+ 0043c1dc ["INT_ADD", "register:40f0:8", ["const:43c1dc:8", "const:4:8"]]
+ 0043c1dc ["CALL", null, ["callee:00c57a50:8"]]
- 004196dc bytes 49061f94
+ 0043c1dc bytes 1d6e2094
- 004196fc ["INT_ADD", "register:40f0:8", ["const:4196fc:8", "const:4:8"]]
- 004196fc ["CALL", null, ["callee:00c57a30:8"]]
+ 0043c1fc ["INT_ADD", "register:40f0:8", ["const:43c1fc:8", "const:4:8"]]
+ 0043c1fc ["CALL", null, ["callee:00c57a30:8"]]
- 004196fc bytes 39061f94
+ 0043c1fc bytes 0d6e2094
- 004196c4 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0043c1c4 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 004196c4 bytes 484000f0
+ 0043c1c4 bytes 48430090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8c57ab87b1ea48b388786829cbacf4"></a>

### [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) → [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) FUN_0043c218

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00420580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420580.md) [`00420858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420858.md) · 呼出先 49件 [`0041aa74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041aa74.md) [`0041ac3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041b470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`0041ba38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041ba38.md)
- 新版 呼出元 2件 [`00443080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443080.md) [`00443358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443358.md) · 呼出先 49件 [`0043d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d574.md) [`0043d73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0043df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) [`0043e538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e538.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 89.22% / 新版 89.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 22件, `call_target` 6件, `store_condition` 1件, `store_destination` 7件, `store_value` 10件, `unresolved_call_alignment` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c3a0",
      "incomplete_value": true,
      "site": "0043c3a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004198a0",
      "incomplete_value": true,
      "site": "004198a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c484",
      "incomplete_value": false,
      "site": "0043c484",
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
    "old": {
      "definition_site": "00419984",
      "incomplete_value": false,
      "site": "00419984",
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
                "const:be8000:8"
              ],
              [
                "leaf",
                "const:570:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0043c5c0",
      "incomplete_value": true,
      "site": "0043c5c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00419ac0",
      "incomplete_value": true,
      "site": "00419ac0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:66b:8"
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
      "0043c2ac",
      "PARAM",
      [
        "storage",
        "002af87e",
        null,
        "string"
      ]
    ],
    [
      "0043c2e4",
      "PARAM",
      [
        "storage",
        "002a9259",
        null,
        null
      ]
    ],
    [
      "0043c390",
      "READ",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043c2ac",
      "PARAM",
      [
        "storage",
        "002c0ea2",
        null,
        "string"
      ]
    ],
    [
      "0043c2e4",
      "PARAM",
      [
        "storage",
        "002b9ef0",
        null,
        null
      ]
    ],
    [
      "0043c390",
      "READ",
      [
        "storage",
        "002a7500",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004197b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md#insn-004197b8) · [`004197ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md#insn-004197ec) · [`00419970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md#insn-00419970)
- 新版 `0043c2b8`（命令位置の公開資料なし） · `0043c2ec`（命令位置の公開資料なし） · `0043c470`（命令位置の公開資料なし）

~~~diff
- 004197b8 ["INT_ADD", "register:40f0:8", ["const:4197b8:8", "const:4:8"]]
- 004197b8 ["CALL", null, ["callee:00c57b60:8"]]
+ 0043c2b8 ["INT_ADD", "register:40f0:8", ["const:43c2b8:8", "const:4:8"]]
+ 0043c2b8 ["CALL", null, ["callee:00c57b60:8"]]
- 004197b8 bytes 56061f94
+ 0043c2b8 bytes 2a6e2094
- 004197ec ["INT_ADD", "register:40f0:8", ["const:4197ec:8", "const:4:8"]]
- 004197ec ["CALL", null, ["callee:00c57b70:8"]]
+ 0043c2ec ["INT_ADD", "register:40f0:8", ["const:43c2ec:8", "const:4:8"]]
+ 0043c2ec ["CALL", null, ["callee:00c57b70:8"]]
- 004197ec bytes 4d061f94
+ 0043c2ec bytes 216e2094
- 00419970 ["INT_ADD", "register:40f0:8", ["const:419970:8", "const:4:8"]]
- 00419970 ["CALL", null, ["ram:45fc34:8"]]
+ 0043c470 ["INT_ADD", "register:40f0:8", ["const:43c470:8", "const:4:8"]]
+ 0043c470 ["CALL", null, ["ram:482acc:8"]]
- 00419970 bytes b1180194
+ 0043c470 bytes 97190194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2aa9546399b257d97f400ce882e4360"></a>

### [`0041ac3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) → [`0043d73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) FUN_0043d73c

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) · 呼出先 13件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041e10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`0046517c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/0046517c.md) [`004652a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004652a0.md)
- 新版 呼出元 2件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) · 呼出先 13件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00440c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440c0c.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488014.md) [`00488138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.81% / 新版 95.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043d9d8",
      "incomplete_value": true,
      "site": "0043d9dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0041aed8",
      "incomplete_value": true,
      "site": "0041aedc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "0043d9d4",
      "incomplete_value": true,
      "site": "0043d9e0",
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
      "definition_site": "0041aed4",
      "incomplete_value": true,
      "site": "0041aee0",
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043d9ec",
      "incomplete_value": true,
      "site": "0043d9ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
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
      "definition_site": "0041aeec",
      "incomplete_value": true,
      "site": "0041aeec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
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
    "ordinal": 37,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043d9c8",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "0043d9cc",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "0043d9d4",
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
      "0043d9c8",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "0043d9cc",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "0043d9d4",
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

- 旧版 [`0041ac6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md#insn-0041ac6c) · [`0041ac78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md#insn-0041ac78) · [`0041aca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md#insn-0041aca4)
- 新版 `0043d76c`（命令位置の公開資料なし） · `0043d778`（命令位置の公開資料なし） · `0043d7a4`（命令位置の公開資料なし）

~~~diff
- 0041ac6c ["INT_ADD", "register:40f0:8", ["const:41ac6c:8", "const:4:8"]]
- 0041ac6c ["CALL", null, ["callee:00487de0:8"]]
+ 0043d76c ["INT_ADD", "register:40f0:8", ["const:43d76c:8", "const:4:8"]]
+ 0043d76c ["CALL", null, ["callee:00487de0:8"]]
- 0041ac6c bytes b7280194
+ 0043d76c bytes 9d290194
- 0041ac78 ["INT_ADD", "register:40f0:8", ["const:41ac78:8", "const:4:8"]]
- 0041ac78 ["CALL", null, ["callee:00488014:8"]]
+ 0043d778 ["INT_ADD", "register:40f0:8", ["const:43d778:8", "const:4:8"]]
+ 0043d778 ["CALL", null, ["callee:00488014:8"]]
- 0041ac78 bytes 41290194
+ 0043d778 bytes 272a0194
- 0041aca4 ["INT_ADD", "register:40f0:8", ["const:41aca4:8", "const:4:8"]]
- 0041aca4 ["CALL", null, ["callee:00488138:8"]]
+ 0043d7a4 ["INT_ADD", "register:40f0:8", ["const:43d7a4:8", "const:4:8"]]
+ 0043d7a4 ["CALL", null, ["callee:00488138:8"]]
- 0041aca4 bytes 7f290194
+ 0043d7a4 bytes 652a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25f9d9b9955db5c50ec88d48d2a7e602"></a>

### [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) → [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) FUN_0043db64

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 39件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041b470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`00421b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 39件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00444640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444640.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.23% / 新版 99.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043dd14",
      "incomplete_value": false,
      "site": "0043dd1c",
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
      "definition_site": "0041b214",
      "incomplete_value": false,
      "site": "0041b21c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043dd14",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0043dd14",
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041b21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md#insn-0041b21c) · [`0041b0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md#insn-0041b0fc) · [`0041b14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md#insn-0041b14c)
- 新版 `0043dd1c`（命令位置の公開資料なし） · `0043dbfc`（命令位置の公開資料なし） · `0043dc4c`（命令位置の公開資料なし）

~~~diff
- 0041b21c ["INT_ADD", "register:40f0:8", ["const:41b21c:8", "const:4:8"]]
- 0041b21c ["CALL", null, ["callee:00c57b70:8"]]
+ 0043dd1c ["INT_ADD", "register:40f0:8", ["const:43dd1c:8", "const:4:8"]]
+ 0043dd1c ["CALL", null, ["callee:00c57b70:8"]]
- 0041b21c bytes c1ff1e94
+ 0043dd1c bytes 95672094
- 0041b0fc ["INT_ADD", "register:40f0:8", ["const:41b0fc:8", "const:4:8"]]
- 0041b0fc ["CALL", null, ["callee:0043bae0:8"]]
+ 0043dbfc ["INT_ADD", "register:40f0:8", ["const:43dbfc:8", "const:4:8"]]
+ 0043dbfc ["CALL", null, ["callee:0043bae0:8"]]
- 0041b0fc bytes b9f7ff97
+ 0043dbfc bytes b9f7ff97
- 0041b14c ["INT_ADD", "register:40f0:8", ["const:41b14c:8", "const:4:8"]]
- 0041b14c ["CALL", null, ["callee:00c57bd0:8"]]
+ 0043dc4c ["INT_ADD", "register:40f0:8", ["const:43dc4c:8", "const:4:8"]]
+ 0043dc4c ["CALL", null, ["callee:00c57bd0:8"]]
- 0041b14c bytes 0d001f94
+ 0043dc4c bytes e1672094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d18823cdd19b4cce37b088986ea2297e"></a>

### [`0041b338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b338.md) → [`0043de38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043de38.md) FUN_0043de38

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045fc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045fc34.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00482acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00482/00482acc.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043de54",
      "incomplete_value": true,
      "site": "0043de58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0041b354",
      "incomplete_value": true,
      "site": "0041b358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0043de4c",
      "READ",
      [
        "storage",
        "00c1adb8",
        null,
        "pointer"
      ]
    ],
    [
      "0043de58",
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
      "0043de4c",
      "READ",
      [
        "storage",
        "00c9a7a8",
        null,
        "pointer"
      ]
    ],
    [
      "0043de58",
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

- 旧版 [`0041b344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b338.md#insn-0041b344) · [`0041b34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b338.md#insn-0041b34c) · [`0041b368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b338.md#insn-0041b368)
- 新版 `0043de44`（命令位置の公開資料なし） · `0043de4c`（命令位置の公開資料なし） · `0043de68`（命令位置の公開資料なし）

~~~diff
- 0041b344 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0043de44 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0041b344 bytes e83f00f0
+ 0043de44 bytes e84200b0
- 0041b34c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 0041b34c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043de4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7a8:8"]]
+ 0043de4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0041b34c bytes 08dd46f9
+ 0043de4c bytes 08d543f9
- 0041b368 ["INT_ADD", "register:40f0:8", ["const:41b368:8", "const:4:8"]]
- 0041b368 ["CALL", null, ["callee:00c538e0:8"]]
+ 0043de68 ["INT_ADD", "register:40f0:8", ["const:43de68:8", "const:4:8"]]
+ 0043de68 ["CALL", null, ["callee:00c538e0:8"]]
- 0041b368 bytes caee1e94
+ 0043de68 bytes 9e562094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ab433cff746c494d6fa8ffa75a1ef07"></a>

### [`0041b470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) → [`0043df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) FUN_0043df70

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) · 呼出先 20件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00420674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420674.md) [`00420678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420678.md) [`00420704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420704.md) [`00420708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420708.md)
- 新版 呼出元 2件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) · 呼出先 20件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00443174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443174.md) [`00443178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443178.md) [`00443204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443204.md) [`00443208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443208.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.90% / 新版 95.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043e164",
      "incomplete_value": false,
      "site": "0043e164",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041b664",
      "incomplete_value": false,
      "site": "0041b664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "definition_site": "0043e188",
      "incomplete_value": false,
      "site": "0043e188",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041b688",
      "incomplete_value": false,
      "site": "0041b688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "definition_site": "0043e19c",
      "incomplete_value": false,
      "site": "0043e19c",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041b69c",
      "incomplete_value": false,
      "site": "0041b69c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "0043df9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00428cb4"
      ]
    ],
    [
      "0043dfc0",
      "PARAM",
      [
        "storage",
        "0029583f",
        null,
        "undefined4"
      ]
    ],
    [
      "0043dff0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073ab94"
      ]
    ]
  ],
  "added": [
    [
      "0043df9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b804"
      ]
    ],
    [
      "0043dfc0",
      "PARAM",
      [
        "storage",
        "002a5278",
        null,
        "undefined4"
      ]
    ],
    [
      "0043dff0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041b49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md#insn-0041b49c) · [`0041b4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md#insn-0041b4c8) · [`0041b4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md#insn-0041b4f0)
- 新版 `0043df9c`（命令位置の公開資料なし） · `0043dfc8`（命令位置の公開資料なし） · `0043dff0`（命令位置の公開資料なし）

~~~diff
- 0041b49c ["INT_ADD", "register:40f0:8", ["const:41b49c:8", "const:4:8"]]
- 0041b49c ["CALL", null, ["ram:428cb4:8"]]
+ 0043df9c ["INT_ADD", "register:40f0:8", ["const:43df9c:8", "const:4:8"]]
+ 0043df9c ["CALL", null, ["ram:44b804:8"]]
- 0041b49c bytes 06360094
+ 0043df9c bytes 1a360094
- 0041b4c8 ["INT_ADD", "register:40f0:8", ["const:41b4c8:8", "const:4:8"]]
- 0041b4c8 ["CALL", null, ["callee:00c57b70:8"]]
+ 0043dfc8 ["INT_ADD", "register:40f0:8", ["const:43dfc8:8", "const:4:8"]]
+ 0043dfc8 ["CALL", null, ["callee:00c57b70:8"]]
- 0041b4c8 bytes 16ff1e94
+ 0043dfc8 bytes ea662094
- 0041b4f0 ["INT_ADD", "register:40f0:8", ["const:41b4f0:8", "const:4:8"]]
- 0041b4f0 ["CALL", null, ["ram:73ab94:8"]]
+ 0043dff0 ["INT_ADD", "register:40f0:8", ["const:43dff0:8", "const:4:8"]]
+ 0043dff0 ["CALL", null, ["ram:764ea0:8"]]
- 0041b4f0 bytes a97d0c94
+ 0043dff0 bytes ac9b0c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5225d4aecf8d07937ff693b6de341d5"></a>

### [`0041ba38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041ba38.md) → [`0043e538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e538.md) FUN_0043e538

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) · 呼出先 11件 [`004203a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203a4.md) [`004203a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203a8.md) [`00420430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420430.md) [`00420434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420434.md) [`00420578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420578.md)
- 新版 呼出元 1件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) · 呼出先 11件 [`00442ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442ea4.md) [`00442ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442ea8.md) [`00442f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442f30.md) [`00442f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442f34.md) [`00443078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443078.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.40% / 新版 94.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043e5f0",
      "incomplete_value": false,
      "site": "0043e5f0",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041baf0",
      "incomplete_value": false,
      "site": "0041baf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "definition_site": "0043e614",
      "incomplete_value": false,
      "site": "0043e614",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bb14",
      "incomplete_value": false,
      "site": "0041bb14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "definition_site": "0043e628",
      "incomplete_value": false,
      "site": "0043e628",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bb28",
      "incomplete_value": false,
      "site": "0041bb28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "0043e568",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "0043e568",
      "PARAM",
      [
        "storage",
        "00c25e10",
        null,
        "undefined1"
      ]
    ],
    [
      "0043e5f0",
      "DATA",
      [
        "storage",
        "00be60c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043e568",
      "READ",
      [
        "storage",
        "00c9a7c8",
        null,
        "pointer"
      ]
    ],
    [
      "0043e568",
      "PARAM",
      [
        "storage",
        "00ca58d0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043e5f0",
      "DATA",
      [
        "storage",
        "00c62c88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041ba6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041ba38.md#insn-0041ba6c) · [`0041ba54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041ba38.md#insn-0041ba54) · [`0041ba68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041ba38.md#insn-0041ba68)
- 新版 `0043e56c`（命令位置の公開資料なし） · `0043e554`（命令位置の公開資料なし） · `0043e568`（命令位置の公開資料なし）

~~~diff
- 0041ba6c ["INT_ADD", "register:40f0:8", ["const:41ba6c:8", "const:4:8"]]
- 0041ba6c ["CALL", null, ["callee:00561cf4:8"]]
+ 0043e56c ["INT_ADD", "register:40f0:8", ["const:43e56c:8", "const:4:8"]]
+ 0043e56c ["CALL", null, ["callee:00561cf4:8"]]
- 0041ba6c bytes fc8c0494
+ 0043e56c bytes e28d0494
- 0041ba54 ["COPY", "register:4000:8", ["const:c1a000:8"]]
+ 0043e554 ["COPY", "register:4000:8", ["const:c9a000:8"]]
- 0041ba54 bytes e03f00f0
+ 0043e554 bytes e0420090
- 0041ba68 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:dd8:8"]]
- 0041ba68 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043e568 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7c8:8"]]
+ 0043e568 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0041ba68 bytes 00ec46f9
+ 0043e568 bytes 00e443f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aea6f67ed5fa49d106cc1cb7466ccc46"></a>

### [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) → [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) FUN_0043e90c

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 38件 [`0060468c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/0060468c.md) [`00651720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651720.md) [`006584d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md) [`0068d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d484.md) [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 5件 [`0041be9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be9c.md) [`0041bf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 38件 [`0062a184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a184.md) [`00677a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) [`006b37cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b37cc.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 5件 [`0043e99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e99c.md) [`0043ea20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ea20.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043e940",
      "incomplete_value": false,
      "site": "0043e944",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041be40",
      "incomplete_value": false,
      "site": "0041be44",
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
            "const:b20:8"
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
      "definition_site": "0043e950",
      "incomplete_value": false,
      "site": "0043e954",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041be50",
      "incomplete_value": false,
      "site": "0041be54",
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
            "const:ac8:8"
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
      "definition_site": "0043e95c",
      "incomplete_value": false,
      "site": "0043e970",
      "value": [
        "leaf",
        "const:43e99c:8"
      ]
    },
    "old": {
      "definition_site": "0041be5c",
      "incomplete_value": false,
      "site": "0041be70",
      "value": [
        "leaf",
        "const:41be9c:8"
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
      "0043e920",
      "READ",
      [
        "storage",
        "00c24b20",
        null,
        "undefined1"
      ]
    ],
    [
      "0043e92c",
      "DATA",
      [
        "storage",
        "00c24ac8",
        null,
        null
      ]
    ],
    [
      "0043e940",
      "PARAM",
      [
        "storage",
        "00c24b20",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0043e920",
      "READ",
      [
        "storage",
        "00ca45e0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043e92c",
      "DATA",
      [
        "storage",
        "00ca4588",
        null,
        null
      ]
    ],
    [
      "0043e940",
      "PARAM",
      [
        "storage",
        "00ca45e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041be44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md#insn-0041be44) · [`0041be54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md#insn-0041be54) · [`0041be70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md#insn-0041be70)
- 新版 `0043e944`（命令位置の公開資料なし） · `0043e954`（命令位置の公開資料なし） · `0043e970`（命令位置の公開資料なし）

~~~diff
- 0041be44 ["INT_ADD", "register:40f0:8", ["const:41be44:8", "const:4:8"]]
- 0041be44 ["CALL", null, ["callee:00c57a50:8"]]
+ 0043e944 ["INT_ADD", "register:40f0:8", ["const:43e944:8", "const:4:8"]]
+ 0043e944 ["CALL", null, ["callee:00c57a50:8"]]
- 0041be44 bytes 6ffc1e94
+ 0043e944 bytes 43642094
- 0041be54 ["INT_ADD", "register:40f0:8", ["const:41be54:8", "const:4:8"]]
- 0041be54 ["CALL", null, ["callee:0043ea20:8"]]
+ 0043e954 ["INT_ADD", "register:40f0:8", ["const:43e954:8", "const:4:8"]]
+ 0043e954 ["CALL", null, ["callee:0043ea20:8"]]
- 0041be54 bytes 33000094
+ 0043e954 bytes 33000094
- 0041be70 ["INT_ADD", "register:40f0:8", ["const:41be70:8", "const:4:8"]]
- 0041be70 ["CALL", null, ["callee:00c57a30:8"]]
+ 0043e970 ["INT_ADD", "register:40f0:8", ["const:43e970:8", "const:4:8"]]
+ 0043e970 ["CALL", null, ["callee:00c57a30:8"]]
- 0041be70 bytes 5cfc1e94
+ 0043e970 bytes 30642094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7c4d1e49b2e014cc7f94b4b9c11f06b"></a>

### [`0041bf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md) → [`0043ea20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ea20.md) FUN_0043ea20

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`00420940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420940.md) · 呼出先 4件 [`00ad3bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3bf8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`00443440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443440.md) · 呼出先 4件 [`00b336b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b336b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043ea8c",
      "incomplete_value": true,
      "site": "0043ea98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bf8c",
      "incomplete_value": true,
      "site": "0041bf98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:300:8"
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
      "definition_site": "0043ea88",
      "incomplete_value": true,
      "site": "0043ea9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:62c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bf88",
      "incomplete_value": true,
      "site": "0041bf9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a7:8"
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
      "definition_site": "0043ea88",
      "incomplete_value": true,
      "site": "0043ea9c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0041bf88",
      "incomplete_value": true,
      "site": "0041bf9c",
      "value": [
        "LOAD",
        "16",
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
      "0043ea88",
      "READ",
      [
        "storage",
        "0029e2a7",
        null,
        "string"
      ]
    ],
    [
      "0043ea88",
      "READ",
      [
        "storage",
        "0029e2b7",
        null,
        "string"
      ]
    ],
    [
      "0043ea8c",
      "READ",
      [
        "storage",
        "002b1300",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0043ea88",
      "READ",
      [
        "storage",
        "002ae62c",
        null,
        "string"
      ]
    ],
    [
      "0043ea88",
      "READ",
      [
        "storage",
        "002ae63c",
        null,
        "string"
      ]
    ],
    [
      "0043ea8c",
      "READ",
      [
        "storage",
        "002c2940",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041bf78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md#insn-0041bf78) · [`0041bf7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md#insn-0041bf7c) · [`0041bf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md#insn-0041bf80)
- 新版 `0043ea78`（命令位置の公開資料なし） · `0043ea7c`（命令位置の公開資料なし） · `0043ea80`（命令位置の公開資料なし）

~~~diff
- 0041bf78 ["INT_ADD", "register:40f0:8", ["const:41bf78:8", "const:4:8"]]
- 0041bf78 ["CALL", null, ["callee:00c57a90:8"]]
+ 0043ea78 ["INT_ADD", "register:40f0:8", ["const:43ea78:8", "const:4:8"]]
+ 0043ea78 ["CALL", null, ["callee:00c57a90:8"]]
- 0041bf78 bytes 32fc1e94
+ 0043ea78 bytes 06642094
- 0041bf7c ["COPY", "register:4040:8", ["const:29e000:8"]]
+ 0043ea7c ["COPY", "register:4040:8", ["const:2ae000:8"]]
- 0041bf7c bytes 08f4fff0
+ 0043ea7c bytes 88f3ff90
- 0041bf80 ["COPY", "tmp:0:8", ["const:2a7:8"]]
- 0041bf80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0041bf80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0041bf80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043ea80 ["COPY", "tmp:0:8", ["const:62c:8"]]
+ 0043ea80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ea80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ea80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0041bf80 bytes 089d0a91
+ 0043ea80 bytes 08b11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a24268fdb5086df717b63537e3cf3a7b"></a>

### [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) → [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) FUN_0043ec20

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 9件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`0081fa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081fa64.md) [`00821350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821350.md) [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) [`0084f35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f35c.md) · 呼出先 24件 [`0041ac3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041a/0041ac3c.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041b470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`00428d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428d08.md) [`0045e558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md)
- 新版 呼出元 9件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`008532c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/008532c8.md) [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`008822f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/008822f4.md) · 呼出先 24件 [`0043d73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043d73c.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0043df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) [`0044b858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b858.md) [`004813f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043eecc",
      "incomplete_value": true,
      "site": "0043eed4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0041c3cc",
      "incomplete_value": true,
      "site": "0041c3d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0043efa8",
      "value": [
        "leaf",
        "ram:482acc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0041c4a8",
      "value": [
        "leaf",
        "ram:45fc34:8"
      ]
    },
    "ordinal": 35,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043f134",
      "incomplete_value": false,
      "site": "0043f13c",
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
            "const:5a5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041c634",
      "incomplete_value": false,
      "site": "0041c63c",
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
            "const:37f:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043ed68",
      "READ",
      [
        "storage",
        "00c1adb8",
        null,
        "pointer"
      ]
    ],
    [
      "0043eda4",
      "PARAM",
      [
        "storage",
        "002af87e",
        null,
        "string"
      ]
    ],
    [
      "0043edd4",
      "PARAM",
      [
        "storage",
        "002a9259",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0043ed68",
      "READ",
      [
        "storage",
        "00c9a7a8",
        null,
        "pointer"
      ]
    ],
    [
      "0043eda4",
      "PARAM",
      [
        "storage",
        "002c0ea2",
        null,
        "string"
      ]
    ],
    [
      "0043edd4",
      "PARAM",
      [
        "storage",
        "002b9ef0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041c4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md#insn-0041c4a8) · [`0041c63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md#insn-0041c63c) · [`0041c15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md#insn-0041c15c)
- 新版 `0043efa8`（命令位置の公開資料なし） · `0043f13c`（命令位置の公開資料なし） · `0043ec5c`（命令位置の公開資料なし）

~~~diff
- 0041c4a8 ["INT_ADD", "register:40f0:8", ["const:41c4a8:8", "const:4:8"]]
- 0041c4a8 ["CALL", null, ["ram:45fc34:8"]]
+ 0043efa8 ["INT_ADD", "register:40f0:8", ["const:43efa8:8", "const:4:8"]]
+ 0043efa8 ["CALL", null, ["ram:482acc:8"]]
- 0041c4a8 bytes e30d0194
+ 0043efa8 bytes c90e0194
- 0041c63c ["INT_ADD", "register:40f0:8", ["const:41c63c:8", "const:4:8"]]
- 0041c63c ["CALL", null, ["callee:00c57b70:8"]]
+ 0043f13c ["INT_ADD", "register:40f0:8", ["const:43f13c:8", "const:4:8"]]
+ 0043f13c ["CALL", null, ["callee:00c57b70:8"]]
- 0041c63c bytes b9fa1e94
+ 0043f13c bytes 8d622094
- 0041c15c ["INT_ADD", "register:40f0:8", ["const:41c15c:8", "const:4:8"]]
- 0041c15c ["CALL", null, ["callee:0048ce10:8"]]
+ 0043ec5c ["INT_ADD", "register:40f0:8", ["const:43ec5c:8", "const:4:8"]]
+ 0043ec5c ["CALL", null, ["callee:0048ce10:8"]]
- 0041c15c bytes 87370194
+ 0043ec5c bytes 6d380194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba4818b80de8a6c3c9deaad4eaa0a85e"></a>

### [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) → [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) FUN_0043f3f8

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 25件 [`0060468c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/0060468c.md) [`00651720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651720.md) [`006584d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md) [`0068d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d484.md) [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 4件 [`00420b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b98.md) [`00420b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b9c.md) [`00ad3e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3e98.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 25件 [`0062a184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a184.md) [`00677a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00677/00677a00.md) [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) [`006b37cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b37cc.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 4件 [`00443698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443698.md) [`0044369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044369c.md) [`00b33950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33950.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
      "definition_site": "0043f424",
      "incomplete_value": false,
      "site": "0043f42c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041c924",
      "incomplete_value": false,
      "site": "0041c92c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "0043f42c",
      "DATA",
      [
        "storage",
        "00be6518",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f460",
      "READ",
      [
        "storage",
        "00be6538",
        null,
        "pointer"
      ]
    ],
    [
      "0043f460",
      "READ",
      [
        "storage",
        "00be6540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f42c",
      "DATA",
      [
        "storage",
        "00c630d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f460",
      "READ",
      [
        "storage",
        "00c630f8",
        null,
        "pointer"
      ]
    ],
    [
      "0043f460",
      "READ",
      [
        "storage",
        "00c63100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041c920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md#insn-0041c920) · [`0041c924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md#insn-0041c924) · [`0041c938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md#insn-0041c938)
- 新版 `0043f420`（命令位置の公開資料なし） · `0043f424`（命令位置の公開資料なし） · `0043f438`（命令位置の公開資料なし）

~~~diff
- 0041c920 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0043f420 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 0041c920 bytes 483e00d0
+ 0043f420 bytes 28410090
- 0041c924 ["COPY", "tmp:0:8", ["const:518:8"]]
- 0041c924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0041c924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0041c924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f424 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 0043f424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0041c924 bytes 08611491
+ 0043f424 bytes 08610391
- 0041c938 ["INT_ADD", "register:40f0:8", ["const:41c938:8", "const:4:8"]]
- 0041c938 ["CALL", null, ["callee:00b33950:8"]]
+ 0043f438 ["INT_ADD", "register:40f0:8", ["const:43f438:8", "const:4:8"]]
+ 0043f438 ["CALL", null, ["callee:00b33950:8"]]
- 0041c938 bytes 58dd1a94
+ 0043f438 bytes 46d11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79d9b39efeb3c75d47a366813423d48f"></a>

### [`0041c9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c9f4.md) → [`0043f4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f4f4.md) FUN_0043f4f4

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00acc56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00acc56c.md) · 呼出先 4件 [`00420b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b98.md) [`00420b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b9c.md) [`00ad3e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3e98.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00b2bffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bffc.md) · 呼出先 4件 [`00443698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443698.md) [`0044369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044369c.md) [`00b33950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b33950.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043f514",
      "incomplete_value": false,
      "site": "0043f524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041ca14",
      "incomplete_value": false,
      "site": "0041ca24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "0043f524",
      "DATA",
      [
        "storage",
        "00be6518",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f558",
      "READ",
      [
        "storage",
        "00be6538",
        null,
        "pointer"
      ]
    ],
    [
      "0043f558",
      "READ",
      [
        "storage",
        "00be6540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f524",
      "DATA",
      [
        "storage",
        "00c630d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f558",
      "READ",
      [
        "storage",
        "00c630f8",
        null,
        "pointer"
      ]
    ],
    [
      "0043f558",
      "READ",
      [
        "storage",
        "00c63100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041ca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c9f4.md#insn-0041ca10) · [`0041ca14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c9f4.md#insn-0041ca14) · [`0041ca30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c9f4.md#insn-0041ca30)
- 新版 `0043f510`（命令位置の公開資料なし） · `0043f514`（命令位置の公開資料なし） · `0043f530`（命令位置の公開資料なし）

~~~diff
- 0041ca10 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0043f510 ["COPY", "register:4048:8", ["const:c63000:8"]]
- 0041ca10 bytes 493e00d0
+ 0043f510 bytes 29410090
- 0041ca14 ["COPY", "tmp:0:8", ["const:518:8"]]
- 0041ca14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0041ca14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0041ca14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043f514 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 0043f514 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f514 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f514 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0041ca14 bytes 29611491
+ 0043f514 bytes 29610391
- 0041ca30 ["INT_ADD", "register:40f0:8", ["const:41ca30:8", "const:4:8"]]
- 0041ca30 ["CALL", null, ["callee:00b33950:8"]]
+ 0043f530 ["INT_ADD", "register:40f0:8", ["const:43f530:8", "const:4:8"]]
+ 0043f530 ["CALL", null, ["callee:00b33950:8"]]
- 0041ca30 bytes 1add1a94
+ 0043f530 bytes 08d11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47c85103edca294075fd10e1bc9844af"></a>

### [`0041cad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cad8.md) → [`0043f5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f5d8.md) FUN_0043f5d8

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0041c8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8ec.md) · 呼出先 6件 [`00420938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420938.md) [`0042093c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042093c.md) [`00420b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b18.md) [`00420b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b1c.md) [`00ad3bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad3/00ad3bfc.md)
- 新版 呼出元 1件 [`0043f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3ec.md) · 呼出先 6件 [`00443438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443438.md) [`0044343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044343c.md) [`00443618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443618.md) [`0044361c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044361c.md) [`00b336b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b33/00b336b4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043f5f8",
      "incomplete_value": false,
      "site": "0043f61c",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041caf8",
      "incomplete_value": false,
      "site": "0041cb1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "definition_site": "0043f614",
      "incomplete_value": false,
      "site": "0043f620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041cb14",
      "incomplete_value": false,
      "site": "0041cb20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "definition_site": "0043f62c",
      "incomplete_value": false,
      "site": "0043f640",
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
            "const:62c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041cb2c",
      "incomplete_value": false,
      "site": "0041cb40",
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
            "const:2a7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043f61c",
      "DATA",
      [
        "storage",
        "00be63f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f620",
      "DATA",
      [
        "storage",
        "00be6488",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f62c",
      "PARAM",
      [
        "storage",
        "0029e2a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043f61c",
      "DATA",
      [
        "storage",
        "00c62fb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f620",
      "DATA",
      [
        "storage",
        "00c63048",
        null,
        "undefined *"
      ]
    ],
    [
      "0043f62c",
      "PARAM",
      [
        "storage",
        "002ae62c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041cb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cad8.md#insn-0041cb40) · [`0041caf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cad8.md#insn-0041caf4) · [`0041caf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cad8.md#insn-0041caf8)
- 新版 `0043f640`（命令位置の公開資料なし） · `0043f5f4`（命令位置の公開資料なし） · `0043f5f8`（命令位置の公開資料なし）

~~~diff
- 0041cb40 ["INT_ADD", "register:40f0:8", ["const:41cb40:8", "const:4:8"]]
- 0041cb40 ["CALL", null, ["callee:00b336b4:8"]]
+ 0043f640 ["INT_ADD", "register:40f0:8", ["const:43f640:8", "const:4:8"]]
+ 0043f640 ["CALL", null, ["callee:00b336b4:8"]]
- 0041cb40 bytes 2fdc1a94
+ 0043f640 bytes 1dd01b94
- 0041caf4 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 0043f5f4 ["COPY", "register:4048:8", ["const:c62000:8"]]
- 0041caf4 bytes 493e00d0
+ 0043f5f4 bytes 094100f0
- 0041caf8 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 0041caf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0041caf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0041caf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043f5f8 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0043f5f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f5f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f5f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0041caf8 bytes 29e10f91
+ 0043f5f8 bytes 29e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7fbc3ed2292b1a420d44bdfc520a95f"></a>

### [`0041cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) → [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) FUN_0043f8dc

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a2ba68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2b/00a2ba68.md) [`00ab1dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1dc8.md) · 呼出先 23件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00420bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bd8.md) [`0045e558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md)
- 新版 呼出元 2件 [`00a898d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a89/00a898d8.md) [`00b11858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11858.md) · 呼出先 23件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`004436d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004436d8.md) [`004813f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/004813f0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.93% / 新版 96.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043fa60",
      "incomplete_value": true,
      "site": "0043fa60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0041cf60",
      "incomplete_value": true,
      "site": "0041cf60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043fdb4",
      "incomplete_value": true,
      "site": "0043fdc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041d2b4",
      "incomplete_value": true,
      "site": "0041d2c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:900:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 71,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043fec8",
      "incomplete_value": true,
      "site": "0043fed4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041d3c8",
      "incomplete_value": true,
      "site": "0041d3d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 84,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043f948",
      "PARAM",
      [
        "storage",
        "002a9259",
        null,
        null
      ]
    ],
    [
      "0043fa50",
      "READ",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ],
    [
      "0043fb94",
      "READ",
      [
        "storage",
        "00294539",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043f948",
      "PARAM",
      [
        "storage",
        "002b9ef0",
        null,
        null
      ]
    ],
    [
      "0043fa50",
      "READ",
      [
        "storage",
        "002a7500",
        null,
        "string"
      ]
    ],
    [
      "0043fb94",
      "READ",
      [
        "storage",
        "002a3e4f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041ce50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md#insn-0041ce50) · [`0041db44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md#insn-0041db44) · [`0041ce14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md#insn-0041ce14)
- 新版 `0043f950`（命令位置の公開資料なし） · `00440644`（命令位置の公開資料なし） · `0043f914`（命令位置の公開資料なし）

~~~diff
- 0041ce50 ["INT_ADD", "register:40f0:8", ["const:41ce50:8", "const:4:8"]]
- 0041ce50 ["CALL", null, ["callee:00c57b70:8"]]
+ 0043f950 ["INT_ADD", "register:40f0:8", ["const:43f950:8", "const:4:8"]]
+ 0043f950 ["CALL", null, ["callee:00c57b70:8"]]
- 0041ce50 bytes b4f81e94
+ 0043f950 bytes 88602094
- 0041db44 ["INT_ADD", "register:40f0:8", ["const:41db44:8", "const:4:8"]]
- 0041db44 ["CALL", null, ["ram:45fc34:8"]]
+ 00440644 ["INT_ADD", "register:40f0:8", ["const:440644:8", "const:4:8"]]
+ 00440644 ["CALL", null, ["ram:482acc:8"]]
- 0041db44 bytes 3c080194
+ 00440644 bytes 22090194
- 0041ce14 ["INT_ADD", "register:40f0:8", ["const:41ce14:8", "const:4:8"]]
- 0041ce14 ["CALL", null, ["callee:004813f0:8"]]
+ 0043f914 ["INT_ADD", "register:40f0:8", ["const:43f914:8", "const:4:8"]]
+ 0043f914 ["CALL", null, ["callee:004813f0:8"]]
- 0041ce14 bytes d1050194
+ 0043f914 bytes b7060194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b5988f99513a30e6a13dd2d1e9d9350"></a>

### [`0041e03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e03c.md) → [`00440b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440b3c.md) FUN_00440b3c

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00692224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/00692224.md) [`007da86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007da/007da86c.md) [`007e5fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007e5/007e5fa4.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)
- 新版 呼出元 4件 [`006b8578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8578.md) [`0080f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080f/0080f0e8.md) [`0081a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081a/0081a7d4.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00440b6c",
      "incomplete_value": true,
      "site": "00440b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0041e06c",
      "incomplete_value": true,
      "site": "0041e074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00440b78",
      "incomplete_value": true,
      "site": "00440b78",
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
      "definition_site": "0041e078",
      "incomplete_value": true,
      "site": "0041e078",
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
      "definition_site": "00440b88",
      "incomplete_value": true,
      "site": "00440b88",
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
      "definition_site": "0041e088",
      "incomplete_value": true,
      "site": "0041e088",
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
      "00440b58",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "00440b5c",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00440b68",
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
      "00440b58",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "00440b5c",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00440b68",
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

- 旧版 [`0041e04c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e03c.md#insn-0041e04c) · [`0041e050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e03c.md#insn-0041e050) · [`0041e058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e03c.md#insn-0041e058)
- 新版 `00440b4c`（命令位置の公開資料なし） · `00440b50`（命令位置の公開資料なし） · `00440b58`（命令位置の公開資料なし）

~~~diff
- 0041e04c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00440b4c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0041e04c bytes e83f0090
+ 00440b4c bytes c84200d0
- 0041e050 ["COPY", "register:40b0:8", ["const:c1a000:8"]]
+ 00440b50 ["COPY", "register:40b0:8", ["const:c9a000:8"]]
- 0041e050 bytes f63f0090
+ 00440b50 bytes d64200d0
- 0041e058 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 0041e058 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00440b58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7b0:8"]]
+ 00440b58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0041e058 bytes 08e146f9
+ 00440b58 bytes 08d943f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38c3f930cdd0c553b3f3bfe9408fa16f"></a>

### [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) → [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) FUN_00440e80

採用 · 移動量 `+0x22b00` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 535件 [`0041cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`0041e10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`00439bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439bc0.md) [`0043aca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aca0.md) [`0043ec60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043ec60.md) · 呼出先 4件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1e0.md)
- 新版 呼出元 573件 [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00440c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440c0c.md) [`0045ca58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045c/0045ca58.md) [`0045db38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045d/0045db38.md) [`00461af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461af8.md) · 呼出先 4件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00440ea8",
      "incomplete_value": true,
      "site": "00440eb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041e3a8",
      "incomplete_value": true,
      "site": "0041e3b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
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
      "definition_site": "00440eac",
      "incomplete_value": true,
      "site": "00440eb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041e3ac",
      "incomplete_value": true,
      "site": "0041e3b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
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
      "00440ea8",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "00440ea8",
      "PARAM",
      [
        "storage",
        "00c16908",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00440eac",
      "READ",
      [
        "storage",
        "00c1ade8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00440ea8",
      "READ",
      [
        "storage",
        "00c9a7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00440ea8",
      "PARAM",
      [
        "storage",
        "00c962b0",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00440eac",
      "READ",
      [
        "storage",
        "00c9a7d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041e3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md#insn-0041e3b0) · [`0041e390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md#insn-0041e390) · [`0041e398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md#insn-0041e398)
- 新版 `00440eb0`（命令位置の公開資料なし） · `00440e90`（命令位置の公開資料なし） · `00440e98`（命令位置の公開資料なし）

~~~diff
- 0041e3b0 ["INT_ADD", "register:40f0:8", ["const:41e3b0:8", "const:4:8"]]
- 0041e3b0 ["CALL", null, ["callee:00c57b10:8"]]
+ 00440eb0 ["INT_ADD", "register:40f0:8", ["const:440eb0:8", "const:4:8"]]
+ 00440eb0 ["CALL", null, ["callee:00c57b10:8"]]
- 0041e3b0 bytes 44f31e94
+ 00440eb0 bytes 185b2094
- 0041e390 ["INT_ADD", "register:40f0:8", ["const:41e390:8", "const:4:8"]]
- 0041e390 ["CALL", null, ["callee:00c57af0:8"]]
+ 00440e90 ["INT_ADD", "register:40f0:8", ["const:440e90:8", "const:4:8"]]
+ 00440e90 ["CALL", null, ["callee:00c57af0:8"]]
- 0041e390 bytes 44f31e94
+ 00440e90 bytes 185b2094
- 0041e398 ["INT_ADD", "register:40f0:8", ["const:41e398:8", "const:4:8"]]
- 0041e398 ["CALL", null, ["callee:00c57c30:8"]]
+ 00440e98 ["INT_ADD", "register:40f0:8", ["const:440e98:8", "const:4:8"]]
+ 00440e98 ["CALL", null, ["callee:00c57c30:8"]]
- 0041e398 bytes 92f31e94
+ 00440e98 bytes 665b2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69ed08326102ab3241b020aa2e723da4"></a>

### [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) → [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) FUN_00440f1c

採用 · 移動量 `+0x22b00` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 43件 [`0041e10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e10c.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004629d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00462/004629d4.md) [`0049100c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/0049100c.md) [`0049b54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049b54c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 42件 [`00440c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440c0c.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`0048586c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00485/0048586c.md) [`004b3ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b3ea4.md) [`004be3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004be3e4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00440f2c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0041e42c",
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
      "definition_site": "00440f28",
      "incomplete_value": false,
      "site": "00440f2c",
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
      "definition_site": "0041e428",
      "incomplete_value": false,
      "site": "0041e42c",
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
      "00440f28",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00440f2c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00440f28",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00440f2c",
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

- 旧版 [`0041e42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md#insn-0041e42c) · [`0041e424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md#insn-0041e424) · [`0041e428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md#insn-0041e428)
- 新版 `00440f2c`（命令位置の公開資料なし） · `00440f24`（命令位置の公開資料なし） · `00440f28`（命令位置の公開資料なし）

~~~diff
- 0041e42c ["INT_ADD", "register:40f0:8", ["const:41e42c:8", "const:4:8"]]
- 0041e42c ["CALL", null, ["ram:418c38:8"]]
+ 00440f2c ["INT_ADD", "register:40f0:8", ["const:440f2c:8", "const:4:8"]]
+ 00440f2c ["CALL", null, ["ram:43b738:8"]]
- 0041e42c bytes 03eaff97
+ 00440f2c bytes 03eaff97
- 0041e424 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00440f24 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0041e424 bytes 40f4ffb0
+ 00440f24 bytes a0f3fff0
- 0041e428 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0041e428 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0041e428 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0041e428 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00440f28 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00440f28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00440f28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00440f28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0041e428 bytes 00740e91
+ 00440f28 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41b958458bf5a5cc40a00ac509d54013"></a>

### [`0041e778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) → [`00441278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md) FUN_00441278

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0041e650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e650.md) [`0041e778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) [`005f1af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1af0.md) [`005f5668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f5/005f5668.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041e778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md)
- 新版 呼出元 4件 [`00441150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441150.md) [`00441278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md) [`00617330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/00617330.md) [`0061aeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061aeb8.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.80% / 新版 98.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004413e8",
      "incomplete_value": false,
      "site": "004413f0",
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
      "definition_site": "0041e8e8",
      "incomplete_value": false,
      "site": "0041e8f0",
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
      "definition_site": "004414a0",
      "incomplete_value": false,
      "site": "004414a8",
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
      "definition_site": "0041e9a0",
      "incomplete_value": false,
      "site": "0041e9a8",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004414bc",
      "incomplete_value": false,
      "site": "004414c8",
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
      "definition_site": "0041e9bc",
      "incomplete_value": false,
      "site": "0041e9c8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004413e8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "004414a0",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "004414bc",
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
      "004413e8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "004414a0",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "004414bc",
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

- 旧版 [`0041e8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md#insn-0041e8f0) · [`0041e9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md#insn-0041e9a8) · [`0041e9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md#insn-0041e9c8)
- 新版 `004413f0`（命令位置の公開資料なし） · `004414a8`（命令位置の公開資料なし） · `004414c8`（命令位置の公開資料なし）

~~~diff
- 0041e8f0 ["INT_ADD", "register:40f0:8", ["const:41e8f0:8", "const:4:8"]]
- 0041e8f0 ["CALL", null, ["callee:00441e54:8"]]
+ 004413f0 ["INT_ADD", "register:40f0:8", ["const:4413f0:8", "const:4:8"]]
+ 004413f0 ["CALL", null, ["callee:00441e54:8"]]
- 0041e8f0 bytes 99020094
+ 004413f0 bytes 99020094
- 0041e9a8 ["INT_ADD", "register:40f0:8", ["const:41e9a8:8", "const:4:8"]]
- 0041e9a8 ["CALL", null, ["callee:00441e54:8"]]
+ 004414a8 ["INT_ADD", "register:40f0:8", ["const:4414a8:8", "const:4:8"]]
+ 004414a8 ["CALL", null, ["callee:00441e54:8"]]
- 0041e9a8 bytes 6b020094
+ 004414a8 bytes 6b020094
- 0041e9c8 ["INT_ADD", "register:40f0:8", ["const:41e9c8:8", "const:4:8"]]
- 0041e9c8 ["CALL", null, ["callee:004427b4:8"]]
+ 004414c8 ["INT_ADD", "register:40f0:8", ["const:4414c8:8", "const:4:8"]]
+ 004414c8 ["CALL", null, ["callee:004427b4:8"]]
- 0041e9c8 bytes bb040094
+ 004414c8 bytes bb040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22dc25e20c86baf9f19712e306d0b02f"></a>

### [`0041f3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md) → [`00441ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441ed4.md) FUN_00441ed4

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0041e778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) [`0041f3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md) [`0045a988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a988.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`00710214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00710/00710214.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 7件 [`00441278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md) [`00441ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441ed4.md) [`0047d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d820.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`0073a314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a314.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.62% / 新版 98.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044203c",
      "incomplete_value": false,
      "site": "00442044",
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
      "definition_site": "0041f53c",
      "incomplete_value": false,
      "site": "0041f544",
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
      "definition_site": "004420f4",
      "incomplete_value": false,
      "site": "004420fc",
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
      "definition_site": "0041f5f4",
      "incomplete_value": false,
      "site": "0041f5fc",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00442110",
      "incomplete_value": false,
      "site": "0044211c",
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
      "definition_site": "0041f610",
      "incomplete_value": false,
      "site": "0041f61c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0044203c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "004420f4",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00442110",
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
      "0044203c",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "004420f4",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "00442110",
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

- 旧版 [`0041f544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md#insn-0041f544) · [`0041f5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md#insn-0041f5fc) · [`0041f61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md#insn-0041f61c)
- 新版 `00442044`（命令位置の公開資料なし） · `004420fc`（命令位置の公開資料なし） · `0044211c`（命令位置の公開資料なし）

~~~diff
- 0041f544 ["INT_ADD", "register:40f0:8", ["const:41f544:8", "const:4:8"]]
- 0041f544 ["CALL", null, ["callee:00441e54:8"]]
+ 00442044 ["INT_ADD", "register:40f0:8", ["const:442044:8", "const:4:8"]]
+ 00442044 ["CALL", null, ["callee:00441e54:8"]]
- 0041f544 bytes 84ffff97
+ 00442044 bytes 84ffff97
- 0041f5fc ["INT_ADD", "register:40f0:8", ["const:41f5fc:8", "const:4:8"]]
- 0041f5fc ["CALL", null, ["callee:00441e54:8"]]
+ 004420fc ["INT_ADD", "register:40f0:8", ["const:4420fc:8", "const:4:8"]]
+ 004420fc ["CALL", null, ["callee:00441e54:8"]]
- 0041f5fc bytes 56ffff97
+ 004420fc bytes 56ffff97
- 0041f61c ["INT_ADD", "register:40f0:8", ["const:41f61c:8", "const:4:8"]]
- 0041f61c ["CALL", null, ["callee:004427b4:8"]]
+ 0044211c ["INT_ADD", "register:40f0:8", ["const:44211c:8", "const:4:8"]]
+ 0044211c ["CALL", null, ["callee:004427b4:8"]]
- 0041f61c bytes a6010094
+ 0044211c bytes a6010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dca0f32e7282835f75abbb727e1075a"></a>

### [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) → [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) FUN_004428dc

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 130件 [`0041e778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e778.md) [`0041f280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f280.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`0041f3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f3d4.md) [`00424280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 129件 [`00441278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441278.md) [`00441d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441d80.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`00441ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441ed4.md) [`00446d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d80.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "004428ec",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0041fdec",
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
      "definition_site": "004428e8",
      "incomplete_value": false,
      "site": "004428ec",
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
            "const:ee3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041fde8",
      "incomplete_value": false,
      "site": "0041fdec",
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
            "const:24c:8"
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
      "004428e8",
      "PARAM",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ],
    [
      "004428ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "004428e8",
      "PARAM",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ],
    [
      "004428ec",
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

- 旧版 [`0041fdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md#insn-0041fdec) · [`0041fde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md#insn-0041fde4) · [`0041fde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md#insn-0041fde8)
- 新版 `004428ec`（命令位置の公開資料なし） · `004428e4`（命令位置の公開資料なし） · `004428e8`（命令位置の公開資料なし）

~~~diff
- 0041fdec ["INT_ADD", "register:40f0:8", ["const:41fdec:8", "const:4:8"]]
- 0041fdec ["CALL", null, ["ram:41fdf0:8"]]
+ 004428ec ["INT_ADD", "register:40f0:8", ["const:4428ec:8", "const:4:8"]]
+ 004428ec ["CALL", null, ["ram:4428f0:8"]]
- 0041fdec bytes 01000094
+ 004428ec bytes 01000094
- 0041fde4 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 004428e4 ["COPY", "register:4000:8", ["const:2b9000:8"]]
- 0041fde4 bytes 40f4ffd0
+ 004428e4 bytes a0f3fff0
- 0041fde8 ["COPY", "tmp:0:8", ["const:24c:8"]]
- 0041fde8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0041fde8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0041fde8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004428e8 ["COPY", "tmp:0:8", ["const:ee3:8"]]
+ 004428e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004428e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004428e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0041fde8 bytes 00300991
+ 004428e8 bytes 008c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cbda03c074f1fea54df23195b4882eb"></a>

### [`00420234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420234.md) → [`00442d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442d34.md) FUN_00442d34

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00442d48",
      "incomplete_value": false,
      "site": "00442d4c",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420248",
      "incomplete_value": false,
      "site": "0042024c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "00442d4c",
      "DATA",
      [
        "storage",
        "00be6038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00442d4c",
      "DATA",
      [
        "storage",
        "00c62bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420234.md#insn-00420240) · [`00420244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420234.md#insn-00420244) · [`00420248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420234.md#insn-00420248)
- 新版 `00442d40`（命令位置の公開資料なし） · `00442d44`（命令位置の公開資料なし） · `00442d48`（命令位置の公開資料なし）

~~~diff
- 00420240 ["INT_ADD", "register:40f0:8", ["const:420240:8", "const:4:8"]]
- 00420240 ["CALL", null, ["callee:00c57a90:8"]]
+ 00442d40 ["INT_ADD", "register:40f0:8", ["const:442d40:8", "const:4:8"]]
+ 00442d40 ["CALL", null, ["callee:00c57a90:8"]]
- 00420240 bytes 80eb1e94
+ 00442d40 bytes 54532094
- 00420244 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00442d44 ["COPY", "register:4040:8", ["const:c62000:8"]]
- 00420244 bytes 283e00d0
+ 00442d44 bytes 08410090
- 00420248 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00420248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00442d48 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00442d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00442d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00442d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420248 bytes 08e10091
+ 00442d48 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b9d44507b993461c9a337978a1f3f76"></a>

### [`00420258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420258.md) → [`00442d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442d58.md) FUN_00442d58

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00442d5c",
      "incomplete_value": false,
      "site": "00442d60",
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
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042025c",
      "incomplete_value": false,
      "site": "00420260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "00442d60",
      "DATA",
      [
        "storage",
        "00be6038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00442d60",
      "DATA",
      [
        "storage",
        "00c62bf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420258.md#insn-00420258) · [`0042025c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420258.md#insn-0042025c)
- 新版 `00442d58`（命令位置の公開資料なし） · `00442d5c`（命令位置の公開資料なし）

~~~diff
- 00420258 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00442d58 ["COPY", "register:4040:8", ["const:c62000:8"]]
- 00420258 bytes 283e00d0
+ 00442d58 bytes 08410090
- 0042025c ["COPY", "tmp:0:8", ["const:38:8"]]
- 0042025c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042025c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042025c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00442d5c ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00442d5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00442d5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00442d5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042025c bytes 08e10091
+ 00442d5c bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47c8a2acf86336e76ab90dc5fd2c1b0d"></a>

### [`0042035c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042035c.md) → [`00442e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442e5c.md) FUN_00442e5c

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00442e80",
      "incomplete_value": false,
      "site": "00442e80",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420380",
      "incomplete_value": false,
      "site": "00420380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "00442e80",
      "DATA",
      [
        "storage",
        "00be60c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00442e80",
      "DATA",
      [
        "storage",
        "00c62c88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042035c.md#insn-00420370) · [`00420378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042035c.md#insn-00420378) · [`0042037c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042035c.md#insn-0042037c)
- 新版 `00442e70`（命令位置の公開資料なし） · `00442e78`（命令位置の公開資料なし） · `00442e7c`（命令位置の公開資料なし）

~~~diff
- 00420370 ["INT_ADD", "register:40f0:8", ["const:420370:8", "const:4:8"]]
- 00420370 ["CALL", null, ["callee:00c57a90:8"]]
+ 00442e70 ["INT_ADD", "register:40f0:8", ["const:442e70:8", "const:4:8"]]
+ 00442e70 ["CALL", null, ["callee:00c57a90:8"]]
- 00420370 bytes 34eb1e94
+ 00442e70 bytes 08532094
- 00420378 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00442e78 ["COPY", "register:4040:8", ["const:c62000:8"]]
- 00420378 bytes 283e00d0
+ 00442e78 bytes 08410090
- 0042037c ["COPY", "tmp:0:8", ["const:c8:8"]]
- 0042037c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042037c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042037c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00442e7c ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 00442e7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00442e7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00442e7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042037c bytes 08210391
+ 00442e7c bytes 08213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e4cca38cc3c7591bde05f1ca37ecffa"></a>

### [`00420390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420390.md) → [`00442e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442e90.md) FUN_00442e90

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00442e9c",
      "incomplete_value": false,
      "site": "00442e9c",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042039c",
      "incomplete_value": false,
      "site": "0042039c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "00442e9c",
      "DATA",
      [
        "storage",
        "00be60c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00442e9c",
      "DATA",
      [
        "storage",
        "00c62c88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420390.md#insn-00420394) · [`00420398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420390.md#insn-00420398)
- 新版 `00442e94`（命令位置の公開資料なし） · `00442e98`（命令位置の公開資料なし）

~~~diff
- 00420394 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 00442e94 ["COPY", "register:4048:8", ["const:c62000:8"]]
- 00420394 bytes 293e00d0
+ 00442e94 bytes 09410090
- 00420398 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 00420398 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00420398 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00420398 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00442e98 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 00442e98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00442e98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00442e98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00420398 bytes 29210391
+ 00442e98 bytes 29213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99ba7d436e522f1a5f568bca2fa77afe"></a>

### [`004203e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203e8.md) → [`00442ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442ee8.md) FUN_00442ee8

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00442f0c",
      "incomplete_value": false,
      "site": "00442f0c",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042040c",
      "incomplete_value": false,
      "site": "0042040c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "00442f0c",
      "DATA",
      [
        "storage",
        "00be6158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00442f0c",
      "DATA",
      [
        "storage",
        "00c62d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004203fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203e8.md#insn-004203fc) · [`00420404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203e8.md#insn-00420404) · [`00420408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004203e8.md#insn-00420408)
- 新版 `00442efc`（命令位置の公開資料なし） · `00442f04`（命令位置の公開資料なし） · `00442f08`（命令位置の公開資料なし）

~~~diff
- 004203fc ["INT_ADD", "register:40f0:8", ["const:4203fc:8", "const:4:8"]]
- 004203fc ["CALL", null, ["callee:00c57a90:8"]]
+ 00442efc ["INT_ADD", "register:40f0:8", ["const:442efc:8", "const:4:8"]]
+ 00442efc ["CALL", null, ["callee:00c57a90:8"]]
- 004203fc bytes 11eb1e94
+ 00442efc bytes e5522094
- 00420404 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00442f04 ["COPY", "register:4040:8", ["const:c62000:8"]]
- 00420404 bytes 283e00d0
+ 00442f04 bytes 08410090
- 00420408 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00420408 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420408 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00442f08 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00442f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00442f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00442f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420408 bytes 08610591
+ 00442f08 bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd6f0b6ac14e18dfcfdc9f4da7f395e6"></a>

### [`0042041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042041c.md) → [`00442f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442f1c.md) FUN_00442f1c

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00442f28",
      "incomplete_value": false,
      "site": "00442f28",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420428",
      "incomplete_value": false,
      "site": "00420428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00442f28",
      "DATA",
      [
        "storage",
        "00be6158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00442f28",
      "DATA",
      [
        "storage",
        "00c62d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042041c.md#insn-00420420) · [`00420424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042041c.md#insn-00420424)
- 新版 `00442f20`（命令位置の公開資料なし） · `00442f24`（命令位置の公開資料なし）

~~~diff
- 00420420 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 00442f20 ["COPY", "register:4048:8", ["const:c62000:8"]]
- 00420420 bytes 293e00d0
+ 00442f20 bytes 09410090
- 00420424 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00420424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00420424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00420424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00442f24 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00442f24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00442f24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00442f24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00420424 bytes 29610591
+ 00442f24 bytes 29613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e455bbfdcad3c8a1257aff61f233e66c"></a>

### [`00420530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420530.md) → [`00443030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443030.md) FUN_00443030

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00443054",
      "incomplete_value": false,
      "site": "00443054",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420554",
      "incomplete_value": false,
      "site": "00420554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "00443054",
      "DATA",
      [
        "storage",
        "00be61e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443054",
      "DATA",
      [
        "storage",
        "00c62da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420530.md#insn-00420544) · [`0042054c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420530.md#insn-0042054c) · [`00420550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420530.md#insn-00420550)
- 新版 `00443044`（命令位置の公開資料なし） · `0044304c`（命令位置の公開資料なし） · `00443050`（命令位置の公開資料なし）

~~~diff
- 00420544 ["INT_ADD", "register:40f0:8", ["const:420544:8", "const:4:8"]]
- 00420544 ["CALL", null, ["callee:00c57a90:8"]]
+ 00443044 ["INT_ADD", "register:40f0:8", ["const:443044:8", "const:4:8"]]
+ 00443044 ["CALL", null, ["callee:00c57a90:8"]]
- 00420544 bytes bfea1e94
+ 00443044 bytes 93522094
- 0042054c ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0044304c ["COPY", "register:4040:8", ["const:c62000:8"]]
- 0042054c bytes 283e00d0
+ 0044304c bytes e84000f0
- 00420550 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00420550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00443050 ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 00443050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00443050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00443050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420550 bytes 08a10791
+ 00443050 bytes 08a13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64b462bab2163204752e26ef149d2538"></a>

### [`00420564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420564.md) → [`00443064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443064.md) FUN_00443064

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00443070",
      "incomplete_value": false,
      "site": "00443070",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420570",
      "incomplete_value": false,
      "site": "00420570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "00443070",
      "DATA",
      [
        "storage",
        "00be61e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443070",
      "DATA",
      [
        "storage",
        "00c62da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420564.md#insn-00420568) · [`0042056c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420564.md#insn-0042056c)
- 新版 `00443068`（命令位置の公開資料なし） · `0044306c`（命令位置の公開資料なし）

~~~diff
- 00420568 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 00443068 ["COPY", "register:4048:8", ["const:c62000:8"]]
- 00420568 bytes 293e00d0
+ 00443068 bytes e94000f0
- 0042056c ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0042056c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042056c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042056c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0044306c ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 0044306c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0044306c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0044306c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042056c bytes 29a10791
+ 0044306c bytes 29a13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a467a7931654916b353faa1d0dd7dcdb"></a>

### [`0042062c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042062c.md) → [`0044312c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044312c.md) FUN_0044312c

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00443150",
      "incomplete_value": false,
      "site": "00443150",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420650",
      "incomplete_value": false,
      "site": "00420650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00443150",
      "DATA",
      [
        "storage",
        "00be6278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443150",
      "DATA",
      [
        "storage",
        "00c62e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042062c.md#insn-00420640) · [`00420648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042062c.md#insn-00420648) · [`0042064c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042062c.md#insn-0042064c)
- 新版 `00443140`（命令位置の公開資料なし） · `00443148`（命令位置の公開資料なし） · `0044314c`（命令位置の公開資料なし）

~~~diff
- 00420640 ["INT_ADD", "register:40f0:8", ["const:420640:8", "const:4:8"]]
- 00420640 ["CALL", null, ["callee:00c57a90:8"]]
+ 00443140 ["INT_ADD", "register:40f0:8", ["const:443140:8", "const:4:8"]]
+ 00443140 ["CALL", null, ["callee:00c57a90:8"]]
- 00420640 bytes 80ea1e94
+ 00443140 bytes 54522094
- 00420648 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00443148 ["COPY", "register:4040:8", ["const:c62000:8"]]
- 00420648 bytes 283e00d0
+ 00443148 bytes e84000f0
- 0042064c ["COPY", "tmp:0:8", ["const:278:8"]]
- 0042064c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042064c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042064c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044314c ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 0044314c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044314c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044314c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042064c bytes 08e10991
+ 0044314c bytes 08e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-893aa3379f48fd2275a6855e25ecc163"></a>

### [`00420660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420660.md) → [`00443160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443160.md) FUN_00443160

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044316c",
      "incomplete_value": false,
      "site": "0044316c",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042066c",
      "incomplete_value": false,
      "site": "0042066c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "0044316c",
      "DATA",
      [
        "storage",
        "00be6278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044316c",
      "DATA",
      [
        "storage",
        "00c62e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420660.md#insn-00420664) · [`00420668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420660.md#insn-00420668)
- 新版 `00443164`（命令位置の公開資料なし） · `00443168`（命令位置の公開資料なし）

~~~diff
- 00420664 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 00443164 ["COPY", "register:4048:8", ["const:c62000:8"]]
- 00420664 bytes 293e00d0
+ 00443164 bytes e94000f0
- 00420668 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00420668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00420668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00420668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00443168 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 00443168 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00443168 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00443168 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00420668 bytes 29e10991
+ 00443168 bytes 29e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f8ecd75c33c30567f8996d4a74c285f"></a>

### [`004206bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004206bc.md) → [`004431bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004431bc.md) FUN_004431bc

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004431e0",
      "incomplete_value": false,
      "site": "004431e0",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004206e0",
      "incomplete_value": false,
      "site": "004206e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "004431e0",
      "DATA",
      [
        "storage",
        "00be62f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004431e0",
      "DATA",
      [
        "storage",
        "00c62eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004206d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004206bc.md#insn-004206d0) · [`004206d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004206bc.md#insn-004206d8) · [`004206dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004206bc.md#insn-004206dc)
- 新版 `004431d0`（命令位置の公開資料なし） · `004431d8`（命令位置の公開資料なし） · `004431dc`（命令位置の公開資料なし）

~~~diff
- 004206d0 ["INT_ADD", "register:40f0:8", ["const:4206d0:8", "const:4:8"]]
- 004206d0 ["CALL", null, ["callee:00c57a90:8"]]
+ 004431d0 ["INT_ADD", "register:40f0:8", ["const:4431d0:8", "const:4:8"]]
+ 004431d0 ["CALL", null, ["callee:00c57a90:8"]]
- 004206d0 bytes 5cea1e94
+ 004431d0 bytes 30522094
- 004206d8 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 004431d8 ["COPY", "register:4040:8", ["const:c62000:8"]]
- 004206d8 bytes 283e00d0
+ 004431d8 bytes e84000f0
- 004206dc ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 004206dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004206dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004206dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004431dc ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 004431dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004431dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004431dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004206dc bytes 08e10b91
+ 004431dc bytes 08e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3bae524c85fd1119b08f4b1d89e42d4"></a>

### [`004206f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004206f0.md) → [`004431f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004431f0.md) FUN_004431f0

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004431fc",
      "incomplete_value": false,
      "site": "004431fc",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004206fc",
      "incomplete_value": false,
      "site": "004206fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "004431fc",
      "DATA",
      [
        "storage",
        "00be62f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004431fc",
      "DATA",
      [
        "storage",
        "00c62eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004206f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004206f0.md#insn-004206f4) · [`004206f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/004206f0.md#insn-004206f8)
- 新版 `004431f4`（命令位置の公開資料なし） · `004431f8`（命令位置の公開資料なし）

~~~diff
- 004206f4 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 004431f4 ["COPY", "register:4048:8", ["const:c62000:8"]]
- 004206f4 bytes 293e00d0
+ 004431f4 bytes e94000f0
- 004206f8 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 004206f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004206f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004206f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004431f8 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 004431f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004431f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004431f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004206f8 bytes 29e10b91
+ 004431f8 bytes 29e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d14177d933a00bbe486baf5d8d6bc32c"></a>

### [`00420808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420808.md) → [`00443308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443308.md) FUN_00443308

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044332c",
      "incomplete_value": false,
      "site": "0044332c",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042082c",
      "incomplete_value": false,
      "site": "0042082c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "0044332c",
      "DATA",
      [
        "storage",
        "00be6378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044332c",
      "DATA",
      [
        "storage",
        "00c62f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042081c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420808.md#insn-0042081c) · [`00420824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420808.md#insn-00420824) · [`00420828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420808.md#insn-00420828)
- 新版 `0044331c`（命令位置の公開資料なし） · `00443324`（命令位置の公開資料なし） · `00443328`（命令位置の公開資料なし）

~~~diff
- 0042081c ["INT_ADD", "register:40f0:8", ["const:42081c:8", "const:4:8"]]
- 0042081c ["CALL", null, ["callee:00c57a90:8"]]
+ 0044331c ["INT_ADD", "register:40f0:8", ["const:44331c:8", "const:4:8"]]
+ 0044331c ["CALL", null, ["callee:00c57a90:8"]]
- 0042081c bytes 09ea1e94
+ 0044331c bytes dd512094
- 00420824 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00443324 ["COPY", "register:4040:8", ["const:c62000:8"]]
- 00420824 bytes 283e00d0
+ 00443324 bytes e84000f0
- 00420828 ["COPY", "tmp:0:8", ["const:378:8"]]
- 00420828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00443328 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00443328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00443328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00443328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420828 bytes 08e10d91
+ 00443328 bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0595b0556d3296e8a14569262ad84ede"></a>

### [`0042083c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042083c.md) → [`0044333c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/0044333c.md) FUN_0044333c

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00443348",
      "incomplete_value": false,
      "site": "00443348",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420848",
      "incomplete_value": false,
      "site": "00420848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "00443348",
      "DATA",
      [
        "storage",
        "00be6378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443348",
      "DATA",
      [
        "storage",
        "00c62f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042083c.md#insn-00420840) · [`00420844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/0042083c.md#insn-00420844)
- 新版 `00443340`（命令位置の公開資料なし） · `00443344`（命令位置の公開資料なし）

~~~diff
- 00420840 ["COPY", "register:4048:8", ["const:be6000:8"]]
+ 00443340 ["COPY", "register:4048:8", ["const:c62000:8"]]
- 00420840 bytes 293e00d0
+ 00443340 bytes e94000f0
- 00420844 ["COPY", "tmp:0:8", ["const:378:8"]]
- 00420844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00420844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00420844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00443344 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00443344 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00443344 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00443344 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00420844 bytes 29e10d91
+ 00443344 bytes 29e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5447a525d6dad70696c111dc6d34185e"></a>

### [`00420904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420904.md) → [`00443404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443404.md) FUN_00443404

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00443418",
      "incomplete_value": false,
      "site": "0044341c",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420918",
      "incomplete_value": false,
      "site": "0042091c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "0044341c",
      "DATA",
      [
        "storage",
        "00be63f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044341c",
      "DATA",
      [
        "storage",
        "00c62fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420904.md#insn-00420910) · [`00420914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420904.md#insn-00420914) · [`00420918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420904.md#insn-00420918)
- 新版 `00443410`（命令位置の公開資料なし） · `00443414`（命令位置の公開資料なし） · `00443418`（命令位置の公開資料なし）

~~~diff
- 00420910 ["INT_ADD", "register:40f0:8", ["const:420910:8", "const:4:8"]]
- 00420910 ["CALL", null, ["callee:00c57a90:8"]]
+ 00443410 ["INT_ADD", "register:40f0:8", ["const:443410:8", "const:4:8"]]
+ 00443410 ["CALL", null, ["callee:00c57a90:8"]]
- 00420910 bytes cce91e94
+ 00443410 bytes a0512094
- 00420914 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00443414 ["COPY", "register:4040:8", ["const:c62000:8"]]
- 00420914 bytes 283e00d0
+ 00443414 bytes e84000f0
- 00420918 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 00420918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00443418 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00443418 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00443418 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00443418 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420918 bytes 08e10f91
+ 00443418 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18072e59104bc93fd2f870f05814d7db"></a>

### [`00420928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420928.md) → [`00443428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443428.md) FUN_00443428

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044342c",
      "incomplete_value": false,
      "site": "00443430",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042092c",
      "incomplete_value": false,
      "site": "00420930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "00443430",
      "DATA",
      [
        "storage",
        "00be63f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443430",
      "DATA",
      [
        "storage",
        "00c62fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420928.md#insn-00420928) · [`0042092c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420928.md#insn-0042092c)
- 新版 `00443428`（命令位置の公開資料なし） · `0044342c`（命令位置の公開資料なし）

~~~diff
- 00420928 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00443428 ["COPY", "register:4040:8", ["const:c62000:8"]]
- 00420928 bytes 283e00d0
+ 00443428 bytes e84000f0
- 0042092c ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 0042092c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042092c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042092c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044342c ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0044342c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044342c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044342c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042092c bytes 08e10f91
+ 0044342c bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f8b1e4701ccd947fb77f16e962ff41b"></a>

### [`00420940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420940.md) → [`00443440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443440.md) FUN_00443440

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041be9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be9c.md) [`0041bf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bf20.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043e99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e99c.md) [`0043ea20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ea20.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 78.31% / 新版 78.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004434d4",
      "incomplete_value": false,
      "site": "004434d4",
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
            "const:5bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004209d4",
      "incomplete_value": false,
      "site": "004209d4",
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
            "const:afc:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004434fc",
      "incomplete_value": false,
      "site": "00443500",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004209fc",
      "incomplete_value": false,
      "site": "00420a00",
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
            "const:b20:8"
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
      "definition_site": "0044350c",
      "incomplete_value": false,
      "site": "00443510",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420a0c",
      "incomplete_value": false,
      "site": "00420a10",
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
            "const:ac8:8"
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
      "00443490",
      "READ",
      [
        "storage",
        "00c24b20",
        null,
        "undefined1"
      ]
    ],
    [
      "004434c4",
      "READ",
      [
        "storage",
        "00c24b20",
        null,
        "undefined1"
      ]
    ],
    [
      "004434d4",
      "WRITE",
      [
        "storage",
        "00c24afc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00443490",
      "READ",
      [
        "storage",
        "00ca45e0",
        null,
        "undefined1"
      ]
    ],
    [
      "004434c4",
      "READ",
      [
        "storage",
        "00ca45e0",
        null,
        "undefined1"
      ]
    ],
    [
      "004434d4",
      "WRITE",
      [
        "storage",
        "00ca45bc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004209d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420940.md#insn-004209d4) · [`00420a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420940.md#insn-00420a00) · [`00420a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420940.md#insn-00420a10)
- 新版 `004434d4`（命令位置の公開資料なし） · `00443500`（命令位置の公開資料なし） · `00443510`（命令位置の公開資料なし）

~~~diff
- 004209d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:afc:8"]]
- 004209d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 004434d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5bc:8"]]
+ 004434d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 004209d4 bytes 28fd0ab9
+ 004434d4 bytes 28bd05b9
- 00420a00 ["INT_ADD", "register:40f0:8", ["const:420a00:8", "const:4:8"]]
- 00420a00 ["CALL", null, ["callee:00c57a50:8"]]
+ 00443500 ["INT_ADD", "register:40f0:8", ["const:443500:8", "const:4:8"]]
+ 00443500 ["CALL", null, ["callee:00c57a50:8"]]
- 00420a00 bytes 80e91e94
+ 00443500 bytes 54512094
- 00420a10 ["INT_ADD", "register:40f0:8", ["const:420a10:8", "const:4:8"]]
- 00420a10 ["CALL", null, ["callee:0043ea20:8"]]
+ 00443510 ["INT_ADD", "register:40f0:8", ["const:443510:8", "const:4:8"]]
+ 00443510 ["CALL", null, ["callee:0043ea20:8"]]
- 00420a10 bytes 44edff97
+ 00443510 bytes 44edff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a10eef903c31384d5d726a6e47ea8f5"></a>

### [`00420ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420ae4.md) → [`004435e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004435e4.md) FUN_004435e4

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004435f8",
      "incomplete_value": false,
      "site": "004435fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420af8",
      "incomplete_value": false,
      "site": "00420afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "004435fc",
      "DATA",
      [
        "storage",
        "00be6488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004435fc",
      "DATA",
      [
        "storage",
        "00c63048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420ae4.md#insn-00420af0) · [`00420af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420ae4.md#insn-00420af4) · [`00420af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420ae4.md#insn-00420af8)
- 新版 `004435f0`（命令位置の公開資料なし） · `004435f4`（命令位置の公開資料なし） · `004435f8`（命令位置の公開資料なし）

~~~diff
- 00420af0 ["INT_ADD", "register:40f0:8", ["const:420af0:8", "const:4:8"]]
- 00420af0 ["CALL", null, ["callee:00c57a90:8"]]
+ 004435f0 ["INT_ADD", "register:40f0:8", ["const:4435f0:8", "const:4:8"]]
+ 004435f0 ["CALL", null, ["callee:00c57a90:8"]]
- 00420af0 bytes 54e91e94
+ 004435f0 bytes 28512094
- 00420af4 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 004435f4 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00420af4 bytes 283e00d0
+ 004435f4 bytes 08410090
- 00420af8 ["COPY", "tmp:0:8", ["const:488:8"]]
- 00420af8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420af8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420af8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004435f8 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 004435f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004435f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004435f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420af8 bytes 08211291
+ 004435f8 bytes 08210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-269e14af3cc0b6b5ca77346c7e48e1c5"></a>

### [`00420b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b08.md) → [`00443608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443608.md) FUN_00443608

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044360c",
      "incomplete_value": false,
      "site": "00443610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b0c",
      "incomplete_value": false,
      "site": "00420b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "00443610",
      "DATA",
      [
        "storage",
        "00be6488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443610",
      "DATA",
      [
        "storage",
        "00c63048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b08.md#insn-00420b08) · [`00420b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b08.md#insn-00420b0c)
- 新版 `00443608`（命令位置の公開資料なし） · `0044360c`（命令位置の公開資料なし）

~~~diff
- 00420b08 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00443608 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00420b08 bytes 283e00d0
+ 00443608 bytes 08410090
- 00420b0c ["COPY", "tmp:0:8", ["const:488:8"]]
- 00420b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044360c ["COPY", "tmp:0:8", ["const:48:8"]]
+ 0044360c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044360c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044360c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420b0c bytes 08211291
+ 0044360c bytes 08210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9e34aac8de5f447c5358cff5e277334"></a>

### [`00420b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b20.md) → [`00443620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443620.md) FUN_00443620

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044362c",
      "incomplete_value": true,
      "site": "0044362c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b2c",
      "incomplete_value": true,
      "site": "00420b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:44:8"
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
      "00443628",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "0044362c",
      "WRITE",
      [
        "storage",
        "00c24df4",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00443628",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "0044362c",
      "WRITE",
      [
        "storage",
        "00ca48b4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b20.md#insn-00420b20) · [`00420b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b20.md#insn-00420b28)
- 新版 `00443620`（命令位置の公開資料なし） · `00443628`（命令位置の公開資料なし）

~~~diff
- 00420b20 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00443620 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00420b20 bytes c83f00d0
+ 00443620 bytes a84200f0
- 00420b28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d78:8"]]
- 00420b28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00443628 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:768:8"]]
+ 00443628 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00420b28 bytes 08bd46f9
+ 00443628 bytes 08b543f9
~~~


<a id="compare-f0d5c3eca3daac5e2b31372316209b3e"></a>

### [`00420b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b64.md) → [`00443664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443664.md) FUN_00443664

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00443678",
      "incomplete_value": false,
      "site": "0044367c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b78",
      "incomplete_value": false,
      "site": "00420b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "0044367c",
      "DATA",
      [
        "storage",
        "00be6518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044367c",
      "DATA",
      [
        "storage",
        "00c630d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b64.md#insn-00420b70) · [`00420b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b64.md#insn-00420b74) · [`00420b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b64.md#insn-00420b78)
- 新版 `00443670`（命令位置の公開資料なし） · `00443674`（命令位置の公開資料なし） · `00443678`（命令位置の公開資料なし）

~~~diff
- 00420b70 ["INT_ADD", "register:40f0:8", ["const:420b70:8", "const:4:8"]]
- 00420b70 ["CALL", null, ["callee:00c57a90:8"]]
+ 00443670 ["INT_ADD", "register:40f0:8", ["const:443670:8", "const:4:8"]]
+ 00443670 ["CALL", null, ["callee:00c57a90:8"]]
- 00420b70 bytes 34e91e94
+ 00443670 bytes 08512094
- 00420b74 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00443674 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00420b74 bytes 283e00d0
+ 00443674 bytes 08410090
- 00420b78 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00420b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00443678 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 00443678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00443678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00443678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420b78 bytes 08611491
+ 00443678 bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d2c9961705b371bb81684c6be3de8af"></a>

### [`00420b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b88.md) → [`00443688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443688.md) FUN_00443688

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044368c",
      "incomplete_value": false,
      "site": "00443690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b8c",
      "incomplete_value": false,
      "site": "00420b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "00443690",
      "DATA",
      [
        "storage",
        "00be6518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00443690",
      "DATA",
      [
        "storage",
        "00c630d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b88.md#insn-00420b88) · [`00420b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420b88.md#insn-00420b8c)
- 新版 `00443688`（命令位置の公開資料なし） · `0044368c`（命令位置の公開資料なし）

~~~diff
- 00420b88 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00443688 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00420b88 bytes 283e00d0
+ 00443688 bytes 08410090
- 00420b8c ["COPY", "tmp:0:8", ["const:518:8"]]
- 00420b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044368c ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 0044368c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044368c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044368c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420b8c bytes 08611491
+ 0044368c bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53aafb567e7577b1a93cae9a3cbfc8ab"></a>

### [`00420ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420ba0.md) → [`004436a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004436a0.md) FUN_004436a0

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004436a8",
      "incomplete_value": false,
      "site": "004436a8",
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
                "const:870:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420ba8",
      "incomplete_value": false,
      "site": "00420ba8",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:db0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:44:8"
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
      "004436a8",
      "WRITE",
      [
        "storage",
        "00c24df4",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004436a8",
      "WRITE",
      [
        "storage",
        "00ca48b4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420ba0.md#insn-00420ba0) · [`00420ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420ba0.md#insn-00420ba4)
- 新版 `004436a0`（命令位置の公開資料なし） · `004436a4`（命令位置の公開資料なし）

~~~diff
- 00420ba0 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 004436a0 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00420ba0 bytes 28400090
+ 004436a0 bytes 084300b0
- 00420ba4 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00420ba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420ba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420ba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004436a4 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 004436a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004436a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004436a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420ba4 bytes 08c13691
+ 004436a4 bytes 08c12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a95eeb8f6fcae22ed66a89cec04c594"></a>

### [`00420bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bd8.md) → [`004436d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004436d8.md) FUN_004436d8

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0041cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "004436e8",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00420be8",
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
      "definition_site": "004436e4",
      "incomplete_value": false,
      "site": "004436e8",
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
      "definition_site": "00420be4",
      "incomplete_value": false,
      "site": "00420be8",
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
      "004436e4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "004436e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "004436e4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "004436e8",
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

- 旧版 [`00420be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bd8.md#insn-00420be8) · [`00420be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bd8.md#insn-00420be0) · [`00420be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bd8.md#insn-00420be4)
- 新版 `004436e8`（命令位置の公開資料なし） · `004436e0`（命令位置の公開資料なし） · `004436e4`（命令位置の公開資料なし）

~~~diff
- 00420be8 ["INT_ADD", "register:40f0:8", ["const:420be8:8", "const:4:8"]]
- 00420be8 ["CALL", null, ["ram:418c38:8"]]
+ 004436e8 ["INT_ADD", "register:40f0:8", ["const:4436e8:8", "const:4:8"]]
+ 004436e8 ["CALL", null, ["ram:43b738:8"]]
- 00420be8 bytes 14e0ff97
+ 004436e8 bytes 14e0ff97
- 00420be0 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 004436e0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00420be0 bytes 20f4fff0
+ 004436e0 bytes a0f3ff90
- 00420be4 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00420be4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00420be4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00420be4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004436e4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 004436e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004436e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004436e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00420be4 bytes 00740e91
+ 004436e4 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3aaa0bdb6a8e663fb84f1c3ca5c394a"></a>

### [`00420bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bec.md) → [`004436ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/004436ec.md) _INIT_7

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00443728",
      "incomplete_value": true,
      "site": "00443744",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00420c28",
      "incomplete_value": true,
      "site": "00420c44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044374c",
      "incomplete_value": true,
      "site": "00443768",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00420c4c",
      "incomplete_value": true,
      "site": "00420c68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044376c",
      "incomplete_value": true,
      "site": "00443788",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00420c6c",
      "incomplete_value": true,
      "site": "00420c88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00443728",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0044374c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0044376c",
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
      "00443728",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0044374c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0044376c",
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

- 旧版 [`00420d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bec.md#insn-00420d4c) · [`00420e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bec.md#insn-00420e20) · [`00420c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420bec.md#insn-00420c14)
- 新版 `0044384c`（命令位置の公開資料なし） · `00443920`（命令位置の公開資料なし） · `00443714`（命令位置の公開資料なし）

~~~diff
- 00420d4c ["INT_ADD", "register:40f0:8", ["const:420d4c:8", "const:4:8"]]
- 00420d4c ["CALL", null, ["callee:0043b7b8:8"]]
+ 0044384c ["INT_ADD", "register:40f0:8", ["const:44384c:8", "const:4:8"]]
+ 0044384c ["CALL", null, ["callee:0043b7b8:8"]]
- 00420d4c bytes dbdfff97
+ 0044384c bytes dbdfff97
- 00420e20 ["INT_ADD", "register:40f0:8", ["const:420e20:8", "const:4:8"]]
- 00420e20 ["CALL", null, ["callee:00c57a30:8"]]
+ 00443920 ["INT_ADD", "register:40f0:8", ["const:443920:8", "const:4:8"]]
+ 00443920 ["CALL", null, ["callee:00c57a30:8"]]
- 00420e20 bytes 70e81e94
+ 00443920 bytes 44502094
- 00420c14 ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 00443714 ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 00420c14 bytes 33400090
+ 00443714 bytes 134300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8529c9ea55008fbf1784c071d0a4c0bb"></a>

### [`00420f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420f7c.md) → [`00443a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443a7c.md) _INIT_8

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00443ab8",
      "incomplete_value": true,
      "site": "00443ad4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00420fb8",
      "incomplete_value": true,
      "site": "00420fd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00443adc",
      "incomplete_value": true,
      "site": "00443af8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00420fdc",
      "incomplete_value": true,
      "site": "00420ff8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00443afc",
      "incomplete_value": true,
      "site": "00443b18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00420ffc",
      "incomplete_value": true,
      "site": "00421018",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00443ab8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00443adc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00443afc",
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
      "00443ab8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00443adc",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00443afc",
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

- 旧版 [`004210dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420f7c.md#insn-004210dc) · [`004211b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420f7c.md#insn-004211b0) · [`00420fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00420/00420f7c.md#insn-00420fa4)
- 新版 `00443bdc`（命令位置の公開資料なし） · `00443cb0`（命令位置の公開資料なし） · `00443aa4`（命令位置の公開資料なし）

~~~diff
- 004210dc ["INT_ADD", "register:40f0:8", ["const:4210dc:8", "const:4:8"]]
- 004210dc ["CALL", null, ["callee:0043b7b8:8"]]
+ 00443bdc ["INT_ADD", "register:40f0:8", ["const:443bdc:8", "const:4:8"]]
+ 00443bdc ["CALL", null, ["callee:0043b7b8:8"]]
- 004210dc bytes f7deff97
+ 00443bdc bytes f7deff97
- 004211b0 ["INT_ADD", "register:40f0:8", ["const:4211b0:8", "const:4:8"]]
- 004211b0 ["CALL", null, ["callee:00c57a30:8"]]
+ 00443cb0 ["INT_ADD", "register:40f0:8", ["const:443cb0:8", "const:4:8"]]
+ 00443cb0 ["CALL", null, ["callee:00c57a30:8"]]
- 004211b0 bytes 8ce71e94
+ 00443cb0 bytes 604f2094
- 00420fa4 ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 00443aa4 ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 00420fa4 bytes 33400090
+ 00443aa4 bytes 134300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23d2917179c4c81bc6a86332a38ff30a"></a>

### [`0042130c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/0042130c.md) → [`00443e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00443/00443e0c.md) FUN_00443e0c

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00428010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428010.md) · 呼出先 8件 [`00421ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 1件 [`0044ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab10.md) · 呼出先 8件 [`004445d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.64% / 新版 75.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 22件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00443ed0",
      "incomplete_value": false,
      "site": "00443ed0",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004213d0",
      "incomplete_value": false,
      "site": "004213d0",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00443f08",
      "incomplete_value": false,
      "site": "00443f08",
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
            "const:634:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00421408",
      "incomplete_value": false,
      "site": "00421408",
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
            "const:b74:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00443f5c",
      "incomplete_value": false,
      "site": "00443f5c",
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
                "const:618:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042145c",
      "incomplete_value": false,
      "site": "0042145c",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00443e3c",
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      "00443e48",
      "READ",
      [
        "storage",
        "00c24b60",
        null,
        "undefined8"
      ]
    ],
    [
      "00443e50",
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00443e3c",
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      "00443e48",
      "READ",
      [
        "storage",
        "00ca4620",
        null,
        "undefined8"
      ]
    ],
    [
      "00443e50",
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004213d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/0042130c.md#insn-004213d0) · [`00421408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/0042130c.md#insn-00421408) · [`0042143c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/0042130c.md#insn-0042143c)
- 新版 `00443ed0`（命令位置の公開資料なし） · `00443f08`（命令位置の公開資料なし） · `00443f3c`（命令位置の公開資料なし）

~~~diff
- 004213d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b70:8"]]
- 004213d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00443ed0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:630:8"]]
+ 00443ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 004213d0 bytes 09710bb9
+ 00443ed0 bytes 093106b9
- 00421408 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00421408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:b74:8"]]
- 00421408 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00443f08 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00443f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:634:8"]]
+ 00443f08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00421408 bytes 09d12d39
+ 00443f08 bytes 09d11839
- 0042143c ["INT_ADD", "register:40f0:8", ["const:42143c:8", "const:4:8"]]
- 0042143c ["CALL", null, ["callee:00c57a50:8"]]
+ 00443f3c ["INT_ADD", "register:40f0:8", ["const:443f3c:8", "const:4:8"]]
+ 00443f3c ["CALL", null, ["callee:00c57a50:8"]]
- 0042143c bytes f1e61e94
+ 00443f3c bytes c54e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c4d002601107ecd7f41916339759905"></a>

### [`004215a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md) → [`004440a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004440a0.md) FUN_004440a0

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0081f58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f58c.md) [`0084004c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/0084004c.md) [`008406e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md) [`00840b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840b80.md) [`00844bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) · 呼出先 4件 [`00421ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 6件 [`008514c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514c4.md) [`00872338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872338.md) [`008729d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729d0.md) [`00872e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872e6c.md) [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 4件 [`004445d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004440f0",
      "incomplete_value": false,
      "site": "004440f0",
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
                "const:618:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004215f0",
      "incomplete_value": false,
      "site": "004215f0",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004440f4",
      "incomplete_value": false,
      "site": "004440f4",
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
                "const:618:8"
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
      "definition_site": "004215f4",
      "incomplete_value": false,
      "site": "004215f4",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004440f4",
      "incomplete_value": false,
      "site": "004440f4",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004215f4",
      "incomplete_value": false,
      "site": "004215f4",
      "value": [
        "INT_ADD",
        "8",
        [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004440b0",
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      "004440bc",
      "DATA",
      [
        "storage",
        "00c24b58",
        null,
        "undefined8"
      ]
    ],
    [
      "004440cc",
      "PARAM",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004440b0",
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      "004440bc",
      "DATA",
      [
        "storage",
        "00ca4618",
        null,
        "undefined8"
      ]
    ],
    [
      "004440cc",
      "PARAM",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004215d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md#insn-004215d0) · [`00421600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md#insn-00421600) · [`0042160c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/004215a0.md#insn-0042160c)
- 新版 `004440d0`（命令位置の公開資料なし） · `00444100`（命令位置の公開資料なし） · `0044410c`（命令位置の公開資料なし）

~~~diff
- 004215d0 ["INT_ADD", "register:40f0:8", ["const:4215d0:8", "const:4:8"]]
- 004215d0 ["CALL", null, ["callee:00c57a50:8"]]
+ 004440d0 ["INT_ADD", "register:40f0:8", ["const:4440d0:8", "const:4:8"]]
+ 004440d0 ["CALL", null, ["callee:00c57a50:8"]]
- 004215d0 bytes 8ce61e94
+ 004440d0 bytes 604e2094
- 00421600 ["INT_ADD", "register:40f0:8", ["const:421600:8", "const:4:8"]]
- 00421600 ["CALL", null, ["callee:00c57a30:8"]]
+ 00444100 ["INT_ADD", "register:40f0:8", ["const:444100:8", "const:4:8"]]
+ 00444100 ["CALL", null, ["callee:00c57a30:8"]]
- 00421600 bytes 78e61e94
+ 00444100 bytes 4c4e2094
- 0042160c ["INT_ADD", "register:40f0:8", ["const:42160c:8", "const:4:8"]]
- 0042160c ["CALL", null, ["callee:00c57a70:8"]]
+ 0044410c ["INT_ADD", "register:40f0:8", ["const:44410c:8", "const:4:8"]]
+ 0044410c ["CALL", null, ["callee:00c57a70:8"]]
- 0042160c bytes 85e61e94
+ 0044410c bytes 594e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7345e688e9995926242346b8be2dcaa"></a>

### [`00421614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421614.md) → [`00444114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444114.md) FUN_00444114

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00428080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md) · 呼出先 6件 [`00421ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`0044ab80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab80.md) · 呼出先 6件 [`004445d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 29件, `call_target` 1件, `store_destination` 38件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444168",
      "incomplete_value": false,
      "site": "00444168",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00421668",
      "incomplete_value": false,
      "site": "00421668",
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
            "const:b60:8"
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
      "definition_site": "00444168",
      "incomplete_value": false,
      "site": "00444168",
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
                "const:620:8"
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
      "definition_site": "00421668",
      "incomplete_value": false,
      "site": "00421668",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b60:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "004441ec",
      "incomplete_value": true,
      "site": "004441ec",
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
            "const:634:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004216ec",
      "incomplete_value": true,
      "site": "004216ec",
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
            "const:b74:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00444128",
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      "00444134",
      "READ",
      [
        "storage",
        "00c24b60",
        null,
        "undefined8"
      ]
    ],
    [
      "0044413c",
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00444128",
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      "00444134",
      "READ",
      [
        "storage",
        "00ca4620",
        null,
        "undefined8"
      ]
    ],
    [
      "0044413c",
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004216ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421614.md#insn-004216ec) · [`00421620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421614.md#insn-00421620) · [`00421624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421614.md#insn-00421624)
- 新版 `004441ec`（命令位置の公開資料なし） · `00444120`（命令位置の公開資料なし） · `00444124`（命令位置の公開資料なし）

~~~diff
- 004216ec ["COPY", "tmp:0:4", ["const:0:4"]]
- 004216ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 004216ec ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:b74:8"]]
- 004216ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 004441ec ["COPY", "tmp:0:4", ["const:0:4"]]
+ 004441ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 004441ec ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:634:8"]]
+ 004441ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 004216ec bytes 7fd22d39
+ 004441ec bytes 7fd21839
- 00421620 ["COPY", "register:40a0:8", ["const:c24000:8"]]
+ 00444120 ["COPY", "register:40a0:8", ["const:ca4000:8"]]
- 00421620 bytes 144000f0
+ 00444120 bytes 14430090
- 00421624 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00421624 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00421624 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00421624 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00444124 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 00444124 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00444124 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00444124 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00421624 bytes 94222e91
+ 00444124 bytes 94221991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fda7027e729e8d16684d012260db21f"></a>

### [`00421924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) → [`00444424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444424.md) FUN_00444424

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004235ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) [`00428080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md) · 呼出先 10件 [`00421ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00423798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`00423ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423ad4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 2件 [`004460ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004460ac.md) [`0044ab80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab80.md) · 呼出先 10件 [`004445d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00446298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446298.md) [`004465d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004465d4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.69% / 新版 89.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444580",
      "incomplete_value": false,
      "site": "00444580",
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
                "const:618:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00421a80",
      "incomplete_value": false,
      "site": "00421a80",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444584",
      "incomplete_value": false,
      "site": "00444584",
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
                "const:618:8"
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
      "definition_site": "00421a84",
      "incomplete_value": false,
      "site": "00421a84",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00444584",
      "incomplete_value": false,
      "site": "00444584",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00421a84",
      "incomplete_value": false,
      "site": "00421a84",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004444f4",
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      "0044455c",
      "PARAM",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      "0044456c",
      "PARAM",
      [
        "storage",
        "00c24b58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004444f4",
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      "0044455c",
      "PARAM",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      "0044456c",
      "PARAM",
      [
        "storage",
        "00ca4618",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00421a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md#insn-00421a60) · [`00421a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md#insn-00421a90) · [`00421a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md#insn-00421a9c)
- 新版 `00444560`（命令位置の公開資料なし） · `00444590`（命令位置の公開資料なし） · `0044459c`（命令位置の公開資料なし）

~~~diff
- 00421a60 ["INT_ADD", "register:40f0:8", ["const:421a60:8", "const:4:8"]]
- 00421a60 ["CALL", null, ["callee:00c57a50:8"]]
+ 00444560 ["INT_ADD", "register:40f0:8", ["const:444560:8", "const:4:8"]]
+ 00444560 ["CALL", null, ["callee:00c57a50:8"]]
- 00421a60 bytes 68e51e94
+ 00444560 bytes 3c4d2094
- 00421a90 ["INT_ADD", "register:40f0:8", ["const:421a90:8", "const:4:8"]]
- 00421a90 ["CALL", null, ["callee:00c57a30:8"]]
+ 00444590 ["INT_ADD", "register:40f0:8", ["const:444590:8", "const:4:8"]]
+ 00444590 ["CALL", null, ["callee:00c57a30:8"]]
- 00421a90 bytes 54e51e94
+ 00444590 bytes 284d2094
- 00421a9c ["INT_ADD", "register:40f0:8", ["const:421a9c:8", "const:4:8"]]
- 00421a9c ["CALL", null, ["callee:00c57a70:8"]]
+ 0044459c ["INT_ADD", "register:40f0:8", ["const:44459c:8", "const:4:8"]]
+ 0044459c ["CALL", null, ["callee:00c57a70:8"]]
- 00421a9c bytes 61e51e94
+ 0044459c bytes 354d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1541716c2746fb2a0ac9f57ee7ba9de"></a>

### [`00421b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md) → [`00444640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444640.md) FUN_00444640

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084004c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/0084004c.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00422098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/00422098.md) [`00424230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424230.md) [`0052dd44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd44.md)
- 新版 呼出元 1件 [`00872338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872338.md) · 呼出先 13件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00444b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) [`00446d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d30.md) [`00550bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bdc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.64% / 新版 99.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004448cc",
      "incomplete_value": false,
      "site": "004448d0",
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
            "const:ef5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00421dcc",
      "incomplete_value": false,
      "site": "00421dd0",
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
            "const:25e:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004448cc",
      "PARAM",
      [
        "storage",
        "002a925e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004448cc",
      "PARAM",
      [
        "storage",
        "002b9ef5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00421dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md#insn-00421dd0) · [`00421b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md#insn-00421b94) · [`00421ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md#insn-00421ba0)
- 新版 `004448d0`（命令位置の公開資料なし） · `00444694`（命令位置の公開資料なし） · `004446a0`（命令位置の公開資料なし）

~~~diff
- 00421dd0 ["INT_ADD", "register:40f0:8", ["const:421dd0:8", "const:4:8"]]
- 00421dd0 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004448d0 ["INT_ADD", "register:40f0:8", ["const:4448d0:8", "const:4:8"]]
+ 004448d0 ["CALL", null, ["callee:00c57cb0:8"]]
- 00421dd0 bytes 24e51e94
+ 004448d0 bytes f84c2094
- 00421b94 ["INT_ADD", "register:40f0:8", ["const:421b94:8", "const:4:8"]]
- 00421b94 ["CALL", null, ["callee:00444b98:8"]]
+ 00444694 ["INT_ADD", "register:40f0:8", ["const:444694:8", "const:4:8"]]
+ 00444694 ["CALL", null, ["callee:00444b98:8"]]
- 00421b94 bytes 41010094
+ 00444694 bytes 41010094
- 00421ba0 ["INT_ADD", "register:40f0:8", ["const:421ba0:8", "const:4:8"]]
- 00421ba0 ["CALL", null, ["callee:00550be8:8"]]
+ 004446a0 ["INT_ADD", "register:40f0:8", ["const:4446a0:8", "const:4:8"]]
+ 004446a0 ["CALL", null, ["callee:00550be8:8"]]
- 00421ba0 bytes 6c300494
+ 004446a0 bytes 52310494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4fa812a7decc4f33d16ac676cd99c0c"></a>

### [`00422098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/00422098.md) → [`00444b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) FUN_00444b98

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00421b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421b40.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0042818c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/0042818c.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md)
- 新版 呼出元 4件 [`00444640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444640.md) [`006e42d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e42d4.md) [`006ef704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ef/006ef704.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0044ac8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ac8c.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.47% / 新版 91.47%

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
      "definition_site": "00444bd8",
      "incomplete_value": false,
      "site": "00444bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004220d8",
      "incomplete_value": false,
      "site": "004220dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:598:8"
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
      "definition_site": "00444cf4",
      "incomplete_value": true,
      "site": "00444cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004221f4",
      "incomplete_value": true,
      "site": "004221f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00444cf0",
      "incomplete_value": true,
      "site": "00444cfc",
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
      "definition_site": "004221f0",
      "incomplete_value": true,
      "site": "004221fc",
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
      "00444bdc",
      "DATA",
      [
        "storage",
        "00be6598",
        null,
        "undefined *"
      ]
    ],
    [
      "00444ce4",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "00444ce8",
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
      "00444bdc",
      "DATA",
      [
        "storage",
        "00c63158",
        null,
        "undefined *"
      ]
    ],
    [
      "00444ce4",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "00444ce8",
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

- 旧版 [`004220d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/00422098.md#insn-004220d0) · [`004220d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/00422098.md#insn-004220d4) · [`004220d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/00422098.md#insn-004220d8)
- 新版 `00444bd0`（命令位置の公開資料なし） · `00444bd4`（命令位置の公開資料なし） · `00444bd8`（命令位置の公開資料なし）

~~~diff
- 004220d0 ["INT_ADD", "register:40f0:8", ["const:4220d0:8", "const:4:8"]]
- 004220d0 ["CALL", null, ["callee:00487de0:8"]]
+ 00444bd0 ["INT_ADD", "register:40f0:8", ["const:444bd0:8", "const:4:8"]]
+ 00444bd0 ["CALL", null, ["callee:00487de0:8"]]
- 004220d0 bytes 9e0b0194
+ 00444bd0 bytes 840c0194
- 004220d4 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 00444bd4 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 004220d4 bytes 283e0090
+ 00444bd4 bytes e84000f0
- 004220d8 ["COPY", "tmp:0:8", ["const:598:8"]]
- 004220d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004220d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004220d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00444bd8 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00444bd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00444bd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00444bd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004220d8 bytes 08611691
+ 00444bd8 bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f34290ff548a5f65aef7e73ad128561"></a>

### [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) → [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) FUN_00444de0

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008406e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/008406e4.md) [`00844bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) · 呼出先 42件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004235ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) [`00423798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`00423878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423878.md) [`00424280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md)
- 新版 呼出元 2件 [`008729d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/008729d0.md) [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 42件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004460ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004460ac.md) [`00446298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446298.md) [`00446378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446378.md) [`00446d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d80.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.23% / 新版 92.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `store_destination` 1件, `store_value` 26件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00444e2c",
      "incomplete_value": false,
      "site": "00444e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042232c",
      "incomplete_value": false,
      "site": "00422330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:598:8"
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
      "definition_site": "00444e84",
      "incomplete_value": true,
      "site": "00444e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00422384",
      "incomplete_value": true,
      "site": "00422388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00444e80",
      "incomplete_value": true,
      "site": "00444e8c",
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
      "definition_site": "00422380",
      "incomplete_value": true,
      "site": "0042238c",
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
      "00444e30",
      "DATA",
      [
        "storage",
        "00be6598",
        null,
        "undefined *"
      ]
    ],
    [
      "00444e74",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "00444e78",
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
      "00444e30",
      "DATA",
      [
        "storage",
        "00c63158",
        null,
        "undefined *"
      ]
    ],
    [
      "00444e74",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "00444e78",
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

- 旧版 [`004224c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md#insn-004224c0) · [`00422528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md#insn-00422528) · [`00422598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md#insn-00422598)
- 新版 `00444fc0`（命令位置の公開資料なし） · `00445028`（命令位置の公開資料なし） · `00445098`（命令位置の公開資料なし）

~~~diff
- 004224c0 ["INT_ADD", "register:40f0:8", ["const:4224c0:8", "const:4:8"]]
- 004224c0 ["CALL", null, ["callee:00446d80:8"]]
+ 00444fc0 ["INT_ADD", "register:40f0:8", ["const:444fc0:8", "const:4:8"]]
+ 00444fc0 ["CALL", null, ["callee:00446d80:8"]]
- 004224c0 bytes 70070094
+ 00444fc0 bytes 70070094
- 00422528 ["INT_ADD", "register:40f0:8", ["const:422528:8", "const:4:8"]]
- 00422528 ["CALL", null, ["callee:004486a0:8"]]
+ 00445028 ["INT_ADD", "register:40f0:8", ["const:445028:8", "const:4:8"]]
+ 00445028 ["CALL", null, ["callee:004486a0:8"]]
- 00422528 bytes 9e0d0094
+ 00445028 bytes 9e0d0094
- 00422598 ["INT_ADD", "register:40f0:8", ["const:422598:8", "const:4:8"]]
- 00422598 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00445098 ["INT_ADD", "register:40f0:8", ["const:445098:8", "const:4:8"]]
+ 00445098 ["CALL", null, ["callee:00c57cb0:8"]]
- 00422598 bytes 32e31e94
+ 00445098 bytes 064b2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4e74b64bb256475084f1ad9475b0d2b"></a>

### [`004235ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) → [`004460ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004460ac.md) FUN_004460ac

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) · 呼出先 11件 [`00421924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) [`00421ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00423798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`0052dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) · 呼出先 11件 [`00444424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444424.md) [`004445d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00446298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446298.md) [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.09% / 新版 90.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446168",
      "incomplete_value": false,
      "site": "00446168",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00423668",
      "incomplete_value": false,
      "site": "00423668",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044623c",
      "incomplete_value": false,
      "site": "0044623c",
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
                "const:618:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042373c",
      "incomplete_value": false,
      "site": "0042373c",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446240",
      "incomplete_value": false,
      "site": "00446240",
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
                "const:618:8"
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
      "definition_site": "00423740",
      "incomplete_value": false,
      "site": "00423740",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00446158",
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      "00446168",
      "WRITE",
      [
        "storage",
        "00c24b70",
        null,
        "undefined4"
      ]
    ],
    [
      "00446210",
      "PARAM",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00446158",
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      "00446168",
      "WRITE",
      [
        "storage",
        "00ca4630",
        null,
        "undefined4"
      ]
    ],
    [
      "00446210",
      "PARAM",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00423668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md#insn-00423668) · [`00423714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md#insn-00423714) · [`0042374c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md#insn-0042374c)
- 新版 `00446168`（命令位置の公開資料なし） · `00446214`（命令位置の公開資料なし） · `0044624c`（命令位置の公開資料なし）

~~~diff
- 00423668 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b70:8"]]
- 00423668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 00446168 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:630:8"]]
+ 00446168 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 00423668 bytes 20710bb9
+ 00446168 bytes 203106b9
- 00423714 ["INT_ADD", "register:40f0:8", ["const:423714:8", "const:4:8"]]
- 00423714 ["CALL", null, ["callee:00c57a50:8"]]
+ 00446214 ["INT_ADD", "register:40f0:8", ["const:446214:8", "const:4:8"]]
+ 00446214 ["CALL", null, ["callee:00c57a50:8"]]
- 00423714 bytes 3bde1e94
+ 00446214 bytes 0f462094
- 0042374c ["INT_ADD", "register:40f0:8", ["const:42374c:8", "const:4:8"]]
- 0042374c ["CALL", null, ["callee:00c57a30:8"]]
+ 0044624c ["INT_ADD", "register:40f0:8", ["const:44624c:8", "const:4:8"]]
+ 0044624c ["CALL", null, ["callee:00c57a30:8"]]
- 0042374c bytes 25de1e94
+ 0044624c bytes f9452094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efdda580f5aee8cfea1877fca750dd1f"></a>

### [`00423798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) → [`00446298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446298.md) FUN_00446298

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00421924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`004235ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/004235ac.md) [`00423bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bbc.md) · 呼出先 4件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0052dd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd5c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 4件 [`00444424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444424.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`004460ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004460ac.md) [`004466bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004466bc.md) · 呼出先 4件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00550bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bf4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004462e0",
      "incomplete_value": true,
      "site": "004462e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:991:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004237e0",
      "incomplete_value": true,
      "site": "004237e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:bd3:8"
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
      "004462cc",
      "READ",
      [
        "storage",
        "00298bd3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004462cc",
      "READ",
      [
        "storage",
        "002a8991",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004237bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md#insn-004237bc) · [`004237c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md#insn-004237c0) · [`004237c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md#insn-004237c4)
- 新版 `004462bc`（命令位置の公開資料なし） · `004462c0`（命令位置の公開資料なし） · `004462c4`（命令位置の公開資料なし）

~~~diff
- 004237bc ["INT_ADD", "register:40f0:8", ["const:4237bc:8", "const:4:8"]]
- 004237bc ["CALL", null, ["callee:00550bf4:8"]]
+ 004462bc ["INT_ADD", "register:40f0:8", ["const:4462bc:8", "const:4:8"]]
+ 004462bc ["CALL", null, ["callee:00550bf4:8"]]
- 004237bc bytes 68290494
+ 004462bc bytes 4e2a0494
- 004237c0 ["COPY", "register:4048:8", ["const:298000:8"]]
+ 004462c0 ["COPY", "register:4048:8", ["const:2a8000:8"]]
- 004237c0 bytes a9f3ffb0
+ 004462c0 bytes 09f3ffd0
- 004237c4 ["COPY", "tmp:0:8", ["const:bd3:8"]]
- 004237c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004237c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004237c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004462c4 ["COPY", "tmp:0:8", ["const:991:8"]]
+ 004462c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004462c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004462c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004237c4 bytes 294d2f91
+ 004462c4 bytes 29452691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45fb50caa18447858a41384210d2a61a"></a>

### [`00423bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bbc.md) → [`004466bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004466bc.md) FUN_004466bc

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00423fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423fe4.md) · 呼出先 16件 [`00421ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00423798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423798.md) [`004782e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00478/004782e4.md) [`0052dd44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd44.md) [`0052dd48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd48.md)
- 新版 呼出元 1件 [`00446ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446ae4.md) · 呼出先 16件 [`004445d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00446298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446298.md) [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) [`00550bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bdc.md) [`00550be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 20件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446880",
      "incomplete_value": false,
      "site": "00446880",
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
                "const:618:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00423d80",
      "incomplete_value": false,
      "site": "00423d80",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446884",
      "incomplete_value": false,
      "site": "00446884",
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
                "const:618:8"
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
      "definition_site": "00423d84",
      "incomplete_value": false,
      "site": "00423d84",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00446884",
      "incomplete_value": false,
      "site": "00446884",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00423d84",
      "incomplete_value": false,
      "site": "00423d84",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004466f0",
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      "00446700",
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      "00446738",
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004466f0",
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      "00446700",
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      "00446738",
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00423d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bbc.md#insn-00423d60) · [`00423d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bbc.md#insn-00423d90) · [`00423d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423bbc.md#insn-00423d9c)
- 新版 `00446860`（命令位置の公開資料なし） · `00446890`（命令位置の公開資料なし） · `0044689c`（命令位置の公開資料なし）

~~~diff
- 00423d60 ["INT_ADD", "register:40f0:8", ["const:423d60:8", "const:4:8"]]
- 00423d60 ["CALL", null, ["callee:00c57a50:8"]]
+ 00446860 ["INT_ADD", "register:40f0:8", ["const:446860:8", "const:4:8"]]
+ 00446860 ["CALL", null, ["callee:00c57a50:8"]]
- 00423d60 bytes a8dc1e94
+ 00446860 bytes 7c442094
- 00423d90 ["INT_ADD", "register:40f0:8", ["const:423d90:8", "const:4:8"]]
- 00423d90 ["CALL", null, ["callee:00c57a30:8"]]
+ 00446890 ["INT_ADD", "register:40f0:8", ["const:446890:8", "const:4:8"]]
+ 00446890 ["CALL", null, ["callee:00c57a30:8"]]
- 00423d90 bytes 94dc1e94
+ 00446890 bytes 68442094
- 00423d9c ["INT_ADD", "register:40f0:8", ["const:423d9c:8", "const:4:8"]]
- 00423d9c ["CALL", null, ["callee:00c57a70:8"]]
+ 0044689c ["INT_ADD", "register:40f0:8", ["const:44689c:8", "const:4:8"]]
+ 0044689c ["CALL", null, ["callee:00c57a70:8"]]
- 00423d9c bytes a1dc1e94
+ 0044689c bytes 75442094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d7e5ce02eead7869ba7f93a98bdc225"></a>

### [`00423f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423f2c.md) → [`00446a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446a2c.md) FUN_00446a2c

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 73.91% / 新版 73.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00446a5c",
      "incomplete_value": true,
      "site": "00446a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00423f5c",
      "incomplete_value": true,
      "site": "00423f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00446a68",
      "incomplete_value": true,
      "site": "00446a68",
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
      "definition_site": "00423f68",
      "incomplete_value": true,
      "site": "00423f68",
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
      "definition_site": "00446a78",
      "incomplete_value": true,
      "site": "00446a78",
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
      "definition_site": "00423f78",
      "incomplete_value": true,
      "site": "00423f78",
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
      "00446a48",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "00446a4c",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00446a58",
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
      "00446a48",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "00446a4c",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00446a58",
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

- 旧版 [`00423f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423f2c.md#insn-00423f3c) · [`00423f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423f2c.md#insn-00423f40) · [`00423f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423f2c.md#insn-00423f48)
- 新版 `00446a3c`（命令位置の公開資料なし） · `00446a40`（命令位置の公開資料なし） · `00446a48`（命令位置の公開資料なし）

~~~diff
- 00423f3c ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00446a3c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00423f3c bytes a83f00f0
+ 00446a3c bytes a8420090
- 00423f40 ["COPY", "register:40b0:8", ["const:c1a000:8"]]
+ 00446a40 ["COPY", "register:40b0:8", ["const:c9a000:8"]]
- 00423f40 bytes b63f00f0
+ 00446a40 bytes b6420090
- 00423f48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 00423f48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00446a48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7b0:8"]]
+ 00446a48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00423f48 bytes 08e146f9
+ 00446a48 bytes 08d943f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-107369b70db3e4140762dec63bf38254"></a>

### [`00423fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423fe8.md) → [`00446ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446ae8.md) FUN_00446ae8

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00423ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423ad4.md) · 呼出先 6件 [`004240ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/004240ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) [`00bdb2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2c0.md)
- 新版 呼出元 1件 [`004465d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004465d4.md) · 呼出先 6件 [`00446bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446bec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d00.md) [`00c57d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

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
      "definition_site": "00446b4c",
      "incomplete_value": false,
      "site": "00446b58",
      "value": [
        "leaf",
        "const:446bec:8"
      ]
    },
    "old": {
      "definition_site": "0042404c",
      "incomplete_value": false,
      "site": "00424058",
      "value": [
        "leaf",
        "const:4240ec:8"
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00446b9c",
      "incomplete_value": false,
      "site": "00446ba0",
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
      "definition_site": "0042409c",
      "incomplete_value": false,
      "site": "004240a0",
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
      "00446b4c",
      "PARAM",
      [
        "storage",
        "004240ec",
        null,
        null
      ]
    ],
    [
      "00446b9c",
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
      "00446b4c",
      "PARAM",
      [
        "storage",
        "00446bec",
        null,
        null
      ]
    ],
    [
      "00446b9c",
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

- 旧版 [`00424058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423fe8.md#insn-00424058) · [`004240a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423fe8.md#insn-004240a0) · [`0042401c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423fe8.md#insn-0042401c)
- 新版 `00446b58`（命令位置の公開資料なし） · `00446ba0`（命令位置の公開資料なし） · `00446b1c`（命令位置の公開資料なし）

~~~diff
- 00424058 ["INT_ADD", "register:40f0:8", ["const:424058:8", "const:4:8"]]
- 00424058 ["CALL", null, ["callee:00c57d10:8"]]
+ 00446b58 ["INT_ADD", "register:40f0:8", ["const:446b58:8", "const:4:8"]]
+ 00446b58 ["CALL", null, ["callee:00c57d10:8"]]
- 00424058 bytes 9adc1e94
+ 00446b58 bytes 6e442094
- 004240a0 ["INT_ADD", "register:40f0:8", ["const:4240a0:8", "const:4:8"]]
- 004240a0 ["CALL", null, ["callee:00c57d20:8"]]
+ 00446ba0 ["INT_ADD", "register:40f0:8", ["const:446ba0:8", "const:4:8"]]
+ 00446ba0 ["CALL", null, ["callee:00c57d20:8"]]
- 004240a0 bytes 8cdc1e94
+ 00446ba0 bytes 60442094
- 0042401c ["INT_ADD", "register:40f0:8", ["const:42401c:8", "const:4:8"]]
- 0042401c ["CALL", null, ["callee:00c57a90:8"]]
+ 00446b1c ["INT_ADD", "register:40f0:8", ["const:446b1c:8", "const:4:8"]]
+ 00446b1c ["CALL", null, ["callee:00c57a90:8"]]
- 0042401c bytes 09dc1e94
+ 00446b1c bytes dd432094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6d4aa82eeff3d278351dfb3700d0d94"></a>

### [`004240ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/004240ec.md) → [`00446bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446bec.md) FUN_00446bec

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00423fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423fe8.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2e0.md) [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bdb300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb300.md)
- 新版 呼出元 1件 [`00446ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446ae8.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

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
      "site": "00446c40",
      "value": [
        "leaf",
        "ram:c57d50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00424140",
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
      "00446c40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb300"
      ]
    ]
  ],
  "added": [
    [
      "00446c40",
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

- 旧版 [`00424140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/004240ec.md#insn-00424140) · [`00424114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/004240ec.md#insn-00424114) · [`00424124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/004240ec.md#insn-00424124)
- 新版 `00446c40`（命令位置の公開資料なし） · `00446c14`（命令位置の公開資料なし） · `00446c24`（命令位置の公開資料なし）

~~~diff
- 00424140 ["INT_ADD", "register:40f0:8", ["const:424140:8", "const:4:8"]]
- 00424140 ["CALL", null, ["ram:bdb300:8"]]
+ 00446c40 ["INT_ADD", "register:40f0:8", ["const:446c40:8", "const:4:8"]]
+ 00446c40 ["CALL", null, ["ram:c57d50:8"]]
- 00424140 bytes 70dc1e94
+ 00446c40 bytes 44442094
- 00424114 ["INT_ADD", "register:40f0:8", ["const:424114:8", "const:4:8"]]
- 00424114 ["CALL", null, ["callee:00c57d30:8"]]
+ 00446c14 ["INT_ADD", "register:40f0:8", ["const:446c14:8", "const:4:8"]]
+ 00446c14 ["CALL", null, ["callee:00c57d30:8"]]
- 00424114 bytes 73dc1e94
+ 00446c14 bytes 47442094
- 00424124 ["INT_ADD", "register:40f0:8", ["const:424124:8", "const:4:8"]]
- 00424124 ["CALL", null, ["callee:00c57d40:8"]]
+ 00446c24 ["INT_ADD", "register:40f0:8", ["const:446c24:8", "const:4:8"]]
+ 00446c24 ["CALL", null, ["callee:00c57d40:8"]]
- 00424124 bytes 73dc1e94
+ 00446c24 bytes 47442094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-177c1a8451f8c20eca21dc646aba79d3"></a>

### [`00424280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) → [`00446d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d80.md) FUN_00446d80

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00424280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`00446d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d80.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

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
      "definition_site": "00446ed4",
      "incomplete_value": false,
      "site": "00446edc",
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
      "definition_site": "004243d4",
      "incomplete_value": false,
      "site": "004243dc",
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
      "definition_site": "00446f90",
      "incomplete_value": false,
      "site": "00446f98",
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
      "definition_site": "00424490",
      "incomplete_value": false,
      "site": "00424498",
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
      "definition_site": "00446fa8",
      "incomplete_value": false,
      "site": "00446fb4",
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
      "definition_site": "004244a8",
      "incomplete_value": false,
      "site": "004244b4",
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
      "00446ed4",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00446f90",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00446fa8",
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
      "00446ed4",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00446f90",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "00446fa8",
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

- 旧版 [`004243dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md#insn-004243dc) · [`00424498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md#insn-00424498) · [`004244b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md#insn-004244b4)
- 新版 `00446edc`（命令位置の公開資料なし） · `00446f98`（命令位置の公開資料なし） · `00446fb4`（命令位置の公開資料なし）

~~~diff
- 004243dc ["INT_ADD", "register:40f0:8", ["const:4243dc:8", "const:4:8"]]
- 004243dc ["CALL", null, ["callee:00441e54:8"]]
+ 00446edc ["INT_ADD", "register:40f0:8", ["const:446edc:8", "const:4:8"]]
+ 00446edc ["CALL", null, ["callee:00441e54:8"]]
- 004243dc bytes deebff97
+ 00446edc bytes deebff97
- 00424498 ["INT_ADD", "register:40f0:8", ["const:424498:8", "const:4:8"]]
- 00424498 ["CALL", null, ["callee:00441e54:8"]]
+ 00446f98 ["INT_ADD", "register:40f0:8", ["const:446f98:8", "const:4:8"]]
+ 00446f98 ["CALL", null, ["callee:00441e54:8"]]
- 00424498 bytes afebff97
+ 00446f98 bytes afebff97
- 004244b4 ["INT_ADD", "register:40f0:8", ["const:4244b4:8", "const:4:8"]]
- 004244b4 ["CALL", null, ["callee:004427b4:8"]]
+ 00446fb4 ["INT_ADD", "register:40f0:8", ["const:446fb4:8", "const:4:8"]]
+ 00446fb4 ["CALL", null, ["callee:004427b4:8"]]
- 004244b4 bytes 00eeff97
+ 00446fb4 bytes 00eeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cb8659ef0e09426957c5f2701e4e0c1"></a>

### [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) → [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) FUN_004476b4

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 27件 [`00424280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424280.md) [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004264e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md) [`00426e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md) [`005be404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 27件 [`00446d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d80.md) [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00448fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/00448fe8.md) [`0044998c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/0044998c.md) [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00447808",
      "incomplete_value": false,
      "site": "00447810",
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
      "definition_site": "00424d08",
      "incomplete_value": false,
      "site": "00424d10",
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
      "definition_site": "0044782c",
      "incomplete_value": false,
      "site": "00447838",
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
      "definition_site": "00424d2c",
      "incomplete_value": false,
      "site": "00424d38",
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
      "definition_site": "00447960",
      "incomplete_value": false,
      "site": "00447968",
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
      "definition_site": "00424e60",
      "incomplete_value": false,
      "site": "00424e68",
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
      "00447808",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0044782c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00447960",
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
      "00447808",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0044782c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00447960",
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

- 旧版 [`00424d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md#insn-00424d10) · [`00424d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md#insn-00424d38) · [`00424e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md#insn-00424e68)
- 新版 `00447810`（命令位置の公開資料なし） · `00447838`（命令位置の公開資料なし） · `00447968`（命令位置の公開資料なし）

~~~diff
- 00424d10 ["INT_ADD", "register:40f0:8", ["const:424d10:8", "const:4:8"]]
- 00424d10 ["CALL", null, ["callee:00441e54:8"]]
+ 00447810 ["INT_ADD", "register:40f0:8", ["const:447810:8", "const:4:8"]]
+ 00447810 ["CALL", null, ["callee:00441e54:8"]]
- 00424d10 bytes 91e9ff97
+ 00447810 bytes 91e9ff97
- 00424d38 ["INT_ADD", "register:40f0:8", ["const:424d38:8", "const:4:8"]]
- 00424d38 ["CALL", null, ["callee:004427b4:8"]]
+ 00447838 ["INT_ADD", "register:40f0:8", ["const:447838:8", "const:4:8"]]
+ 00447838 ["CALL", null, ["callee:004427b4:8"]]
- 00424d38 bytes dfebff97
+ 00447838 bytes dfebff97
- 00424e68 ["INT_ADD", "register:40f0:8", ["const:424e68:8", "const:4:8"]]
- 00424e68 ["CALL", null, ["callee:00441e54:8"]]
+ 00447968 ["INT_ADD", "register:40f0:8", ["const:447968:8", "const:4:8"]]
+ 00447968 ["CALL", null, ["callee:00441e54:8"]]
- 00424e68 bytes 3be9ff97
+ 00447968 bytes 3be9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00b541f35b5675eb59970b836f516c2f"></a>

### [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) → [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) FUN_00447eb4

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 170件 [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00458974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458974.md) [`0059fbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059fbec.md) [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 177件 [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047b80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b80c.md) [`005c421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c421c.md) [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00448004",
      "incomplete_value": false,
      "site": "0044800c",
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
      "definition_site": "00425504",
      "incomplete_value": false,
      "site": "0042550c",
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
      "definition_site": "00448028",
      "incomplete_value": false,
      "site": "00448034",
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
      "definition_site": "00425528",
      "incomplete_value": false,
      "site": "00425534",
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
      "definition_site": "0044815c",
      "incomplete_value": false,
      "site": "00448164",
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
      "definition_site": "0042565c",
      "incomplete_value": false,
      "site": "00425664",
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
      "00448004",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00448028",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0044815c",
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
      "00448004",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00448028",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0044815c",
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

- 旧版 [`0042550c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md#insn-0042550c) · [`00425534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md#insn-00425534) · [`00425664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md#insn-00425664)
- 新版 `0044800c`（命令位置の公開資料なし） · `00448034`（命令位置の公開資料なし） · `00448164`（命令位置の公開資料なし）

~~~diff
- 0042550c ["INT_ADD", "register:40f0:8", ["const:42550c:8", "const:4:8"]]
- 0042550c ["CALL", null, ["callee:00441e54:8"]]
+ 0044800c ["INT_ADD", "register:40f0:8", ["const:44800c:8", "const:4:8"]]
+ 0044800c ["CALL", null, ["callee:00441e54:8"]]
- 0042550c bytes 92e7ff97
+ 0044800c bytes 92e7ff97
- 00425534 ["INT_ADD", "register:40f0:8", ["const:425534:8", "const:4:8"]]
- 00425534 ["CALL", null, ["callee:004427b4:8"]]
+ 00448034 ["INT_ADD", "register:40f0:8", ["const:448034:8", "const:4:8"]]
+ 00448034 ["CALL", null, ["callee:004427b4:8"]]
- 00425534 bytes e0e9ff97
+ 00448034 bytes e0e9ff97
- 00425664 ["INT_ADD", "register:40f0:8", ["const:425664:8", "const:4:8"]]
- 00425664 ["CALL", null, ["callee:00441e54:8"]]
+ 00448164 ["INT_ADD", "register:40f0:8", ["const:448164:8", "const:4:8"]]
+ 00448164 ["CALL", null, ["callee:00441e54:8"]]
- 00425664 bytes 3ce7ff97
+ 00448164 bytes 3ce7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e059ce07b26d1389500312f7bab071c"></a>

### [`00425ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md) → [`004486a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/004486a0.md) FUN_004486a0

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00425ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`004486a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/004486a0.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004487f8",
      "incomplete_value": false,
      "site": "00448800",
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
      "definition_site": "00425cf8",
      "incomplete_value": false,
      "site": "00425d00",
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
      "definition_site": "004488b4",
      "incomplete_value": false,
      "site": "004488bc",
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
      "definition_site": "00425db4",
      "incomplete_value": false,
      "site": "00425dbc",
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
      "definition_site": "004488cc",
      "incomplete_value": false,
      "site": "004488d8",
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
      "definition_site": "00425dcc",
      "incomplete_value": false,
      "site": "00425dd8",
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
      "004487f8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "004488b4",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "004488cc",
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
      "004487f8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "004488b4",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "004488cc",
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

- 旧版 [`00425d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md#insn-00425d00) · [`00425dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md#insn-00425dbc) · [`00425dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md#insn-00425dd8)
- 新版 `00448800`（命令位置の公開資料なし） · `004488bc`（命令位置の公開資料なし） · `004488d8`（命令位置の公開資料なし）

~~~diff
- 00425d00 ["INT_ADD", "register:40f0:8", ["const:425d00:8", "const:4:8"]]
- 00425d00 ["CALL", null, ["callee:00441e54:8"]]
+ 00448800 ["INT_ADD", "register:40f0:8", ["const:448800:8", "const:4:8"]]
+ 00448800 ["CALL", null, ["callee:00441e54:8"]]
- 00425d00 bytes 95e5ff97
+ 00448800 bytes 95e5ff97
- 00425dbc ["INT_ADD", "register:40f0:8", ["const:425dbc:8", "const:4:8"]]
- 00425dbc ["CALL", null, ["callee:00441e54:8"]]
+ 004488bc ["INT_ADD", "register:40f0:8", ["const:4488bc:8", "const:4:8"]]
+ 004488bc ["CALL", null, ["callee:00441e54:8"]]
- 00425dbc bytes 66e5ff97
+ 004488bc bytes 66e5ff97
- 00425dd8 ["INT_ADD", "register:40f0:8", ["const:425dd8:8", "const:4:8"]]
- 00425dd8 ["CALL", null, ["callee:004427b4:8"]]
+ 004488d8 ["INT_ADD", "register:40f0:8", ["const:4488d8:8", "const:4:8"]]
+ 004488d8 ["CALL", null, ["callee:004427b4:8"]]
- 00425dd8 bytes b7e7ff97
+ 004488d8 bytes b7e7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ddd612c2fbf0abbdcfbeef2a3f7a823"></a>

### [`004264e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md) → [`00448fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/00448fe8.md) FUN_00448fe8

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00425ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/00425ba0.md) [`004264e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md) [`005be404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) [`005fa9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fa/005fa9ec.md) [`005fd41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005fd/005fd41c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 10件 [`004486a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/004486a0.md) [`00448fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00448/00448fe8.md) [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`006203f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00620/006203f0.md) [`00622e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00622/00622e20.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449140",
      "incomplete_value": false,
      "site": "00449148",
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
      "definition_site": "00426640",
      "incomplete_value": false,
      "site": "00426648",
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
      "definition_site": "00449164",
      "incomplete_value": false,
      "site": "00449170",
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
      "definition_site": "00426664",
      "incomplete_value": false,
      "site": "00426670",
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
      "definition_site": "00449298",
      "incomplete_value": false,
      "site": "004492a0",
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
      "definition_site": "00426798",
      "incomplete_value": false,
      "site": "004267a0",
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
      "00449140",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00449164",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00449298",
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
      "00449140",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00449164",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00449298",
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

- 旧版 [`00426648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md#insn-00426648) · [`00426670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md#insn-00426670) · [`004267a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/004264e8.md#insn-004267a0)
- 新版 `00449148`（命令位置の公開資料なし） · `00449170`（命令位置の公開資料なし） · `004492a0`（命令位置の公開資料なし）

~~~diff
- 00426648 ["INT_ADD", "register:40f0:8", ["const:426648:8", "const:4:8"]]
- 00426648 ["CALL", null, ["callee:00441e54:8"]]
+ 00449148 ["INT_ADD", "register:40f0:8", ["const:449148:8", "const:4:8"]]
+ 00449148 ["CALL", null, ["callee:00441e54:8"]]
- 00426648 bytes 43e3ff97
+ 00449148 bytes 43e3ff97
- 00426670 ["INT_ADD", "register:40f0:8", ["const:426670:8", "const:4:8"]]
- 00426670 ["CALL", null, ["callee:004427b4:8"]]
+ 00449170 ["INT_ADD", "register:40f0:8", ["const:449170:8", "const:4:8"]]
+ 00449170 ["CALL", null, ["callee:004427b4:8"]]
- 00426670 bytes 91e5ff97
+ 00449170 bytes 91e5ff97
- 004267a0 ["INT_ADD", "register:40f0:8", ["const:4267a0:8", "const:4:8"]]
- 004267a0 ["CALL", null, ["callee:00441e54:8"]]
+ 004492a0 ["INT_ADD", "register:40f0:8", ["const:4492a0:8", "const:4:8"]]
+ 004492a0 ["CALL", null, ["callee:00441e54:8"]]
- 004267a0 bytes ede2ff97
+ 004492a0 bytes ede2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-647816e3f36d18a5b09f680661bb0d61"></a>

### [`00426e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) → [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) FUN_00449978

採用 · 移動量 `+0x22b00` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00426cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426cec.md) [`004c2f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2f88.md) [`005aca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005aca98.md) [`005af810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af810.md) [`0073ea18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ea18.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 8件 [`004497ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/004497ec.md) [`004e5e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5e20.md) [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d44dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md) [`00768d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768d24.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00449988",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00426e88",
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
      "definition_site": "00449984",
      "incomplete_value": false,
      "site": "00449988",
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
      "definition_site": "00426e84",
      "incomplete_value": false,
      "site": "00426e88",
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
      "00449984",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00449988",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00449984",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00449988",
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

- 旧版 [`00426e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md#insn-00426e88) · [`00426e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md#insn-00426e80) · [`00426e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md#insn-00426e84)
- 新版 `00449988`（命令位置の公開資料なし） · `00449980`（命令位置の公開資料なし） · `00449984`（命令位置の公開資料なし）

~~~diff
- 00426e88 ["INT_ADD", "register:40f0:8", ["const:426e88:8", "const:4:8"]]
- 00426e88 ["CALL", null, ["ram:418c38:8"]]
+ 00449988 ["INT_ADD", "register:40f0:8", ["const:449988:8", "const:4:8"]]
+ 00449988 ["CALL", null, ["ram:43b738:8"]]
- 00426e88 bytes 6cc7ff97
+ 00449988 bytes 6cc7ff97
- 00426e80 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00449980 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00426e80 bytes 00f4ffb0
+ 00449980 bytes 60f3ffd0
- 00426e84 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00426e84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00426e84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00426e84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00449984 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00449984 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00449984 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00449984 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00426e84 bytes 00740e91
+ 00449984 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd6005ec2168ac09e5d5101260079246"></a>

### [`00426e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md) → [`0044998c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/0044998c.md) FUN_0044998c

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00426e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md) [`0046c588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md) [`005b7004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7004.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`0044998c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/0044998c.md) [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md) [`005dbcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbcd4.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449af8",
      "incomplete_value": false,
      "site": "00449b00",
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
      "definition_site": "00426ff8",
      "incomplete_value": false,
      "site": "00427000",
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
      "definition_site": "00449bb8",
      "incomplete_value": false,
      "site": "00449bc0",
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
      "definition_site": "004270b8",
      "incomplete_value": false,
      "site": "004270c0",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00449bd4",
      "incomplete_value": false,
      "site": "00449be0",
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
      "definition_site": "004270d4",
      "incomplete_value": false,
      "site": "004270e0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00449af8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00449bb8",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00449bd4",
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
      "00449af8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00449bb8",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "00449bd4",
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

- 旧版 [`00427000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md#insn-00427000) · [`004270c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md#insn-004270c0) · [`004270e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e8c.md#insn-004270e0)
- 新版 `00449b00`（命令位置の公開資料なし） · `00449bc0`（命令位置の公開資料なし） · `00449be0`（命令位置の公開資料なし）

~~~diff
- 00427000 ["INT_ADD", "register:40f0:8", ["const:427000:8", "const:4:8"]]
- 00427000 ["CALL", null, ["callee:00441e54:8"]]
+ 00449b00 ["INT_ADD", "register:40f0:8", ["const:449b00:8", "const:4:8"]]
+ 00449b00 ["CALL", null, ["callee:00441e54:8"]]
- 00427000 bytes d5e0ff97
+ 00449b00 bytes d5e0ff97
- 004270c0 ["INT_ADD", "register:40f0:8", ["const:4270c0:8", "const:4:8"]]
- 004270c0 ["CALL", null, ["callee:00441e54:8"]]
+ 00449bc0 ["INT_ADD", "register:40f0:8", ["const:449bc0:8", "const:4:8"]]
+ 00449bc0 ["CALL", null, ["callee:00441e54:8"]]
- 004270c0 bytes a5e0ff97
+ 00449bc0 bytes a5e0ff97
- 004270e0 ["INT_ADD", "register:40f0:8", ["const:4270e0:8", "const:4:8"]]
- 004270e0 ["CALL", null, ["callee:004427b4:8"]]
+ 00449be0 ["INT_ADD", "register:40f0:8", ["const:449be0:8", "const:4:8"]]
+ 00449be0 ["CALL", null, ["callee:004427b4:8"]]
- 004270e0 bytes f5e2ff97
+ 00449be0 bytes f5e2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a0e78f1a3fea2437ce20ce758361d2f"></a>

### [`00427778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427778.md) → [`0044a278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044a278.md) FUN_0044a278

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00427778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427778.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`0044a278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044a278.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044a3c8",
      "incomplete_value": false,
      "site": "0044a3d0",
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
      "definition_site": "004278c8",
      "incomplete_value": false,
      "site": "004278d0",
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
      "definition_site": "0044a3ec",
      "incomplete_value": false,
      "site": "0044a3f8",
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
      "definition_site": "004278ec",
      "incomplete_value": false,
      "site": "004278f8",
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
      "definition_site": "0044a520",
      "incomplete_value": false,
      "site": "0044a528",
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
      "definition_site": "00427a20",
      "incomplete_value": false,
      "site": "00427a28",
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
      "0044a3c8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0044a3ec",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0044a520",
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
      "0044a3c8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0044a3ec",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0044a520",
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

- 旧版 [`004278d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427778.md#insn-004278d0) · [`004278f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427778.md#insn-004278f8) · [`00427a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427778.md#insn-00427a28)
- 新版 `0044a3d0`（命令位置の公開資料なし） · `0044a3f8`（命令位置の公開資料なし） · `0044a528`（命令位置の公開資料なし）

~~~diff
- 004278d0 ["INT_ADD", "register:40f0:8", ["const:4278d0:8", "const:4:8"]]
- 004278d0 ["CALL", null, ["callee:00441e54:8"]]
+ 0044a3d0 ["INT_ADD", "register:40f0:8", ["const:44a3d0:8", "const:4:8"]]
+ 0044a3d0 ["CALL", null, ["callee:00441e54:8"]]
- 004278d0 bytes a1deff97
+ 0044a3d0 bytes a1deff97
- 004278f8 ["INT_ADD", "register:40f0:8", ["const:4278f8:8", "const:4:8"]]
- 004278f8 ["CALL", null, ["callee:004427b4:8"]]
+ 0044a3f8 ["INT_ADD", "register:40f0:8", ["const:44a3f8:8", "const:4:8"]]
+ 0044a3f8 ["CALL", null, ["callee:004427b4:8"]]
- 004278f8 bytes efe0ff97
+ 0044a3f8 bytes efe0ff97
- 00427a28 ["INT_ADD", "register:40f0:8", ["const:427a28:8", "const:4:8"]]
- 00427a28 ["CALL", null, ["callee:00441e54:8"]]
+ 0044a528 ["INT_ADD", "register:40f0:8", ["const:44a528:8", "const:4:8"]]
+ 0044a528 ["CALL", null, ["callee:00441e54:8"]]
- 00427a28 bytes 4bdeff97
+ 0044a528 bytes 4bdeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00345a5605c0e5e38b861f7c78c65df5"></a>

### [`00427f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427f68.md) → [`0044aa68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044aa68.md) FUN_0044aa68

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044aa7c",
      "incomplete_value": false,
      "site": "0044aa80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427f7c",
      "incomplete_value": false,
      "site": "00427f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:610:8"
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
      "0044aa80",
      "DATA",
      [
        "storage",
        "00be6610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044aa80",
      "DATA",
      [
        "storage",
        "00c631d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00427f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427f68.md#insn-00427f74) · [`00427f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427f68.md#insn-00427f78) · [`00427f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427f68.md#insn-00427f7c)
- 新版 `0044aa74`（命令位置の公開資料なし） · `0044aa78`（命令位置の公開資料なし） · `0044aa7c`（命令位置の公開資料なし）

~~~diff
- 00427f74 ["INT_ADD", "register:40f0:8", ["const:427f74:8", "const:4:8"]]
- 00427f74 ["CALL", null, ["callee:00c57a90:8"]]
+ 0044aa74 ["INT_ADD", "register:40f0:8", ["const:44aa74:8", "const:4:8"]]
+ 0044aa74 ["CALL", null, ["callee:00c57a90:8"]]
- 00427f74 bytes 33cc1e94
+ 0044aa74 bytes 07342094
- 00427f78 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0044aa78 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00427f78 bytes e83d00f0
+ 0044aa78 bytes c84000b0
- 00427f7c ["COPY", "tmp:0:8", ["const:610:8"]]
- 00427f7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00427f7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00427f7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044aa7c ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 0044aa7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044aa7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044aa7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00427f7c bytes 08411891
+ 0044aa7c bytes 08410791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90edb1e36538e4e4be2ed454752ce35a"></a>

### [`00427f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427f8c.md) → [`0044aa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044aa8c.md) FUN_0044aa8c

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044aa90",
      "incomplete_value": false,
      "site": "0044aa94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427f90",
      "incomplete_value": false,
      "site": "00427f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:610:8"
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
      "0044aa94",
      "DATA",
      [
        "storage",
        "00be6610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044aa94",
      "DATA",
      [
        "storage",
        "00c631d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00427f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427f8c.md#insn-00427f8c) · [`00427f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427f8c.md#insn-00427f90)
- 新版 `0044aa8c`（命令位置の公開資料なし） · `0044aa90`（命令位置の公開資料なし）

~~~diff
- 00427f8c ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0044aa8c ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00427f8c bytes e83d00f0
+ 0044aa8c bytes c84000b0
- 00427f90 ["COPY", "tmp:0:8", ["const:610:8"]]
- 00427f90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00427f90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00427f90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044aa90 ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 0044aa90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044aa90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044aa90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00427f90 bytes 08411891
+ 0044aa90 bytes 08410791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6170313d1aac7dd00b3a1ba05f98e899"></a>

### [`00427fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427fd4.md) → [`0044aad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044aad4.md) FUN_0044aad4

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044aae8",
      "incomplete_value": false,
      "site": "0044aaec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427fe8",
      "incomplete_value": false,
      "site": "00427fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:690:8"
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
      "0044aaec",
      "DATA",
      [
        "storage",
        "00be6690",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044aaec",
      "DATA",
      [
        "storage",
        "00c63250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00427fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427fd4.md#insn-00427fe0) · [`00427fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427fd4.md#insn-00427fe4) · [`00427fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427fd4.md#insn-00427fe8)
- 新版 `0044aae0`（命令位置の公開資料なし） · `0044aae4`（命令位置の公開資料なし） · `0044aae8`（命令位置の公開資料なし）

~~~diff
- 00427fe0 ["INT_ADD", "register:40f0:8", ["const:427fe0:8", "const:4:8"]]
- 00427fe0 ["CALL", null, ["callee:00c57a90:8"]]
+ 0044aae0 ["INT_ADD", "register:40f0:8", ["const:44aae0:8", "const:4:8"]]
+ 0044aae0 ["CALL", null, ["callee:00c57a90:8"]]
- 00427fe0 bytes 18cc1e94
+ 0044aae0 bytes ec332094
- 00427fe4 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0044aae4 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00427fe4 bytes e83d00f0
+ 0044aae4 bytes c84000b0
- 00427fe8 ["COPY", "tmp:0:8", ["const:690:8"]]
- 00427fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00427fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00427fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044aae8 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 0044aae8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044aae8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044aae8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00427fe8 bytes 08411a91
+ 0044aae8 bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02ba260a0aff99253e0e210ec55b0b10"></a>

### [`00427ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427ff8.md) → [`0044aaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044aaf8.md) FUN_0044aaf8

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044aafc",
      "incomplete_value": false,
      "site": "0044ab00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427ffc",
      "incomplete_value": false,
      "site": "00428000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:690:8"
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
      "0044ab00",
      "DATA",
      [
        "storage",
        "00be6690",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044ab00",
      "DATA",
      [
        "storage",
        "00c63250",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00427ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427ff8.md#insn-00427ff8) · [`00427ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00427/00427ff8.md#insn-00427ffc)
- 新版 `0044aaf8`（命令位置の公開資料なし） · `0044aafc`（命令位置の公開資料なし）

~~~diff
- 00427ff8 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0044aaf8 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00427ff8 bytes e83d00f0
+ 0044aaf8 bytes c84000b0
- 00427ffc ["COPY", "tmp:0:8", ["const:690:8"]]
- 00427ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00427ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00427ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044aafc ["COPY", "tmp:0:8", ["const:250:8"]]
+ 0044aafc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044aafc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044aafc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00427ffc bytes 08411a91
+ 0044aafc bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d153e63d81d3ed65e670eab2f75da38"></a>

### [`00428044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428044.md) → [`0044ab44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab44.md) FUN_0044ab44

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0044ab58",
      "incomplete_value": false,
      "site": "0044ab5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428058",
      "incomplete_value": false,
      "site": "0042805c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      "0044ab5c",
      "DATA",
      [
        "storage",
        "00be6710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044ab5c",
      "DATA",
      [
        "storage",
        "00c632d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428044.md#insn-00428050) · [`00428054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428044.md#insn-00428054) · [`00428058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428044.md#insn-00428058)
- 新版 `0044ab50`（命令位置の公開資料なし） · `0044ab54`（命令位置の公開資料なし） · `0044ab58`（命令位置の公開資料なし）

~~~diff
- 00428050 ["INT_ADD", "register:40f0:8", ["const:428050:8", "const:4:8"]]
- 00428050 ["CALL", null, ["callee:00c57a90:8"]]
+ 0044ab50 ["INT_ADD", "register:40f0:8", ["const:44ab50:8", "const:4:8"]]
+ 0044ab50 ["CALL", null, ["callee:00c57a90:8"]]
- 00428050 bytes fccb1e94
+ 0044ab50 bytes d0332094
- 00428054 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0044ab54 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00428054 bytes e83d00d0
+ 0044ab54 bytes c84000b0
- 00428058 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00428058 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428058 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428058 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044ab58 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 0044ab58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044ab58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044ab58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428058 bytes 08411c91
+ 0044ab58 bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f2a087f5bc40e74bef45aa55d05d444"></a>

### [`00428068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428068.md) → [`0044ab68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab68.md) FUN_0044ab68

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 1件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 0件 

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
      "definition_site": "0044ab6c",
      "incomplete_value": false,
      "site": "0044ab70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042806c",
      "incomplete_value": false,
      "site": "00428070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      "0044ab70",
      "DATA",
      [
        "storage",
        "00be6710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0044ab70",
      "DATA",
      [
        "storage",
        "00c632d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428068.md#insn-00428068) · [`0042806c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428068.md#insn-0042806c)
- 新版 `0044ab68`（命令位置の公開資料なし） · `0044ab6c`（命令位置の公開資料なし）

~~~diff
- 00428068 ["COPY", "register:4040:8", ["const:be6000:8"]]
+ 0044ab68 ["COPY", "register:4040:8", ["const:c63000:8"]]
- 00428068 bytes e83d00d0
+ 0044ab68 bytes c84000b0
- 0042806c ["COPY", "tmp:0:8", ["const:710:8"]]
- 0042806c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042806c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042806c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044ab6c ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 0044ab6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044ab6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044ab6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042806c bytes 08411c91
+ 0044ab6c bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d0291a329af8b679e8b31bfea9831a6"></a>

### [`00428080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md) → [`0044ab80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ab80.md) FUN_0044ab80

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00421614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421614.md) [`00421924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421924.md) [`00421ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 1件 [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 6件 [`00444114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444114.md) [`00444424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444424.md) [`004445d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 65.62% / 新版 65.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044abdc",
      "incomplete_value": false,
      "site": "0044abdc",
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
                "const:618:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004280dc",
      "incomplete_value": false,
      "site": "004280dc",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044abe0",
      "incomplete_value": false,
      "site": "0044abe0",
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
                "const:618:8"
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
      "definition_site": "004280e0",
      "incomplete_value": false,
      "site": "004280e0",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:b58:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0044abe0",
      "incomplete_value": false,
      "site": "0044abe0",
      "value": [
        "INT_ADD",
        "8",
        [
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
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004280e0",
      "incomplete_value": false,
      "site": "004280e0",
      "value": [
        "INT_ADD",
        "8",
        [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0044ab9c",
      "READ",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ],
    [
      "0044aba8",
      "PARAM",
      [
        "storage",
        "00c24b58",
        null,
        "undefined8"
      ]
    ],
    [
      "0044abb8",
      "PARAM",
      [
        "storage",
        "00c24b88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044ab9c",
      "READ",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ],
    [
      "0044aba8",
      "PARAM",
      [
        "storage",
        "00ca4618",
        null,
        "undefined8"
      ]
    ],
    [
      "0044abb8",
      "PARAM",
      [
        "storage",
        "00ca4648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004280bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md#insn-004280bc) · [`004280ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md#insn-004280ec) · [`004280f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428080.md#insn-004280f8)
- 新版 `0044abbc`（命令位置の公開資料なし） · `0044abec`（命令位置の公開資料なし） · `0044abf8`（命令位置の公開資料なし）

~~~diff
- 004280bc ["INT_ADD", "register:40f0:8", ["const:4280bc:8", "const:4:8"]]
- 004280bc ["CALL", null, ["callee:00c57a50:8"]]
+ 0044abbc ["INT_ADD", "register:40f0:8", ["const:44abbc:8", "const:4:8"]]
+ 0044abbc ["CALL", null, ["callee:00c57a50:8"]]
- 004280bc bytes d1cb1e94
+ 0044abbc bytes a5332094
- 004280ec ["INT_ADD", "register:40f0:8", ["const:4280ec:8", "const:4:8"]]
- 004280ec ["CALL", null, ["callee:00c57a30:8"]]
+ 0044abec ["INT_ADD", "register:40f0:8", ["const:44abec:8", "const:4:8"]]
+ 0044abec ["CALL", null, ["callee:00c57a30:8"]]
- 004280ec bytes bdcb1e94
+ 0044abec bytes 91332094
- 004280f8 ["INT_ADD", "register:40f0:8", ["const:4280f8:8", "const:4:8"]]
- 004280f8 ["CALL", null, ["callee:00c57a70:8"]]
+ 0044abf8 ["INT_ADD", "register:40f0:8", ["const:44abf8:8", "const:4:8"]]
+ 0044abf8 ["CALL", null, ["callee:00c57a70:8"]]
- 004280f8 bytes cacb1e94
+ 0044abf8 bytes 9e332094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc96689a0a0c8a12e97a6b41bffa1bff"></a>

### [`00428128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428128.md) → [`0044ac28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ac28.md) FUN_0044ac28

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00421ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00421/00421ad4.md) [`00423ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423ad4.md) · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 2件 [`004445d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/004445d4.md) [`004465d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004465d4.md) · 呼出先 7件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

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
      "site": "0044ac60",
      "value": [
        "leaf",
        "ram:c57cd0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00428160",
      "value": [
        "leaf",
        "ram:bdb280:8"
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
      "0044ac60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb280"
      ]
    ]
  ],
  "added": [
    [
      "0044ac60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57cd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428128.md#insn-00428160) · [`00428140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428128.md#insn-00428140) · [`00428148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428128.md#insn-00428148)
- 新版 `0044ac60`（命令位置の公開資料なし） · `0044ac40`（命令位置の公開資料なし） · `0044ac48`（命令位置の公開資料なし）

~~~diff
- 00428160 ["INT_ADD", "register:40f0:8", ["const:428160:8", "const:4:8"]]
- 00428160 ["CALL", null, ["ram:bdb280:8"]]
+ 0044ac60 ["INT_ADD", "register:40f0:8", ["const:44ac60:8", "const:4:8"]]
+ 0044ac60 ["CALL", null, ["ram:c57cd0:8"]]
- 00428160 bytes 48cc1e94
+ 0044ac60 bytes 1c342094
- 00428140 ["INT_ADD", "register:40f0:8", ["const:428140:8", "const:4:8"]]
- 00428140 ["CALL", null, ["callee:00c57ce0:8"]]
+ 0044ac40 ["INT_ADD", "register:40f0:8", ["const:44ac40:8", "const:4:8"]]
+ 0044ac40 ["CALL", null, ["callee:00c57ce0:8"]]
- 00428140 bytes 54cc1e94
+ 0044ac40 bytes 28342094
- 00428148 ["INT_ADD", "register:40f0:8", ["const:428148:8", "const:4:8"]]
- 00428148 ["CALL", null, ["callee:00c57cf0:8"]]
+ 0044ac48 ["INT_ADD", "register:40f0:8", ["const:44ac48:8", "const:4:8"]]
+ 0044ac48 ["CALL", null, ["callee:00c57cf0:8"]]
- 00428148 bytes 56cc1e94
+ 0044ac48 bytes 2a342094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5a720f4fa331df6af58c3d3c7540569"></a>

### [`00428290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428290.md) → [`0044ad90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ad90.md) _INIT_9

採用 · 移動量 `+0x22b00` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "0044adcc",
      "incomplete_value": true,
      "site": "0044ade8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004282cc",
      "incomplete_value": true,
      "site": "004282e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044adf0",
      "incomplete_value": true,
      "site": "0044ae0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004282f0",
      "incomplete_value": true,
      "site": "0042830c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044ae10",
      "incomplete_value": true,
      "site": "0044ae2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00428310",
      "incomplete_value": true,
      "site": "0042832c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0044adcc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0044adf0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0044ae10",
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
      "0044adcc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0044adf0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0044ae10",
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

- 旧版 [`004283f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428290.md#insn-004283f0) · [`004284c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428290.md#insn-004284c4) · [`004282b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428290.md#insn-004282b8)
- 新版 `0044aef0`（命令位置の公開資料なし） · `0044afc4`（命令位置の公開資料なし） · `0044adb8`（命令位置の公開資料なし）

~~~diff
- 004283f0 ["INT_ADD", "register:40f0:8", ["const:4283f0:8", "const:4:8"]]
- 004283f0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0044aef0 ["INT_ADD", "register:40f0:8", ["const:44aef0:8", "const:4:8"]]
+ 0044aef0 ["CALL", null, ["callee:0043b7b8:8"]]
- 004283f0 bytes 32c2ff97
+ 0044aef0 bytes 32c2ff97
- 004284c4 ["INT_ADD", "register:40f0:8", ["const:4284c4:8", "const:4:8"]]
- 004284c4 ["CALL", null, ["callee:00c57a30:8"]]
+ 0044afc4 ["INT_ADD", "register:40f0:8", ["const:44afc4:8", "const:4:8"]]
+ 0044afc4 ["CALL", null, ["callee:00c57a30:8"]]
- 004284c4 bytes c7ca1e94
+ 0044afc4 bytes 9b322094
- 004282b8 ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 0044adb8 ["COPY", "register:4098:8", ["const:ca4000:8"]]
- 004282b8 bytes f33f0090
+ 0044adb8 bytes d34200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cbd16330f59cb22b53886878f0e16cf"></a>

### [`00428620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428620.md) → [`0044b120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b120.md) FUN_0044b120

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0042d2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d2a8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00450140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b12c",
      "incomplete_value": true,
      "site": "0044b13c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042862c",
      "incomplete_value": true,
      "site": "0042863c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:675:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b140",
      "incomplete_value": true,
      "site": "0044b140",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00428640",
      "incomplete_value": true,
      "site": "00428640",
      "value": [
        "LOAD",
        "8",
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
      "0044b12c",
      "READ",
      [
        "storage",
        "002ac675",
        null,
        "string"
      ]
    ],
    [
      "0044b134",
      "READ",
      [
        "storage",
        "002ac683",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b12c",
      "READ",
      [
        "storage",
        "002bd6ed",
        null,
        "string"
      ]
    ],
    [
      "0044b134",
      "READ",
      [
        "storage",
        "002bd6fb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428620.md#insn-00428624) · [`00428628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428620.md#insn-00428628)
- 新版 `0044b124`（命令位置の公開資料なし） · `0044b128`（命令位置の公開資料なし）

~~~diff
- 00428624 ["COPY", "register:4050:8", ["const:2ac000:8"]]
+ 0044b124 ["COPY", "register:4050:8", ["const:2bd000:8"]]
- 00428624 bytes 2af4ff90
+ 0044b124 bytes 8af3ffd0
- 00428628 ["COPY", "tmp:0:8", ["const:675:8"]]
- 00428628 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00428628 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00428628 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0044b128 ["COPY", "tmp:0:8", ["const:6ed:8"]]
+ 0044b128 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0044b128 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0044b128 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00428628 bytes 4ad51991
+ 0044b128 bytes 4ab51b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb5129912b350c7cbac0e036309f7ebc"></a>

### [`00428648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428648.md) → [`0044b148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b148.md) FUN_0044b148

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00605bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/00605bdc.md) [`006091c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/006091c4.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 3件 [`0062b6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b6d4.md) [`0062ecbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062ecbc.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b170",
      "incomplete_value": true,
      "site": "0044b180",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428670",
      "incomplete_value": true,
      "site": "00428680",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044b184",
      "incomplete_value": true,
      "site": "0044b184",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00428684",
      "incomplete_value": true,
      "site": "00428684",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b190",
      "incomplete_value": false,
      "site": "0044b198",
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
            "const:d09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428690",
      "incomplete_value": false,
      "site": "00428698",
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
            "const:5f9:8"
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
      "0044b170",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044b178",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044b190",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b170",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044b178",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044b190",
      "PARAM",
      [
        "storage",
        "002a1d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428648.md#insn-00428698) · [`00428660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428648.md#insn-00428660) · [`00428664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428648.md#insn-00428664)
- 新版 `0044b198`（命令位置の公開資料なし） · `0044b160`（命令位置の公開資料なし） · `0044b164`（命令位置の公開資料なし）

~~~diff
- 00428698 ["INT_ADD", "register:40f0:8", ["const:428698:8", "const:4:8"]]
- 00428698 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044b198 ["INT_ADD", "register:40f0:8", ["const:44b198:8", "const:4:8"]]
+ 0044b198 ["CALL", null, ["callee:00c57b70:8"]]
- 00428698 bytes a2ca1e94
+ 0044b198 bytes 76322094
- 00428660 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044b160 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 00428660 bytes 29f4ffd0
+ 0044b160 bytes a9f3ff90
- 00428664 ["COPY", "tmp:0:8", ["const:676:8"]]
- 00428664 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00428664 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00428664 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0044b164 ["COPY", "tmp:0:8", ["const:b5a:8"]]
+ 0044b164 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0044b164 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0044b164 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00428664 bytes 29d91991
+ 0044b164 bytes 29692d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bafe2e1d613df15034f62bea3d3b24e8"></a>

### [`00428714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428714.md) → [`0044b214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b214.md) FUN_0044b214

採用 · 移動量 `+0x22b00` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00429a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429a14.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00868124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) · 呼出先 5件 [`00574744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574744.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 4件 [`0044c794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044c/0044c794.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) · 呼出先 5件 [`005975dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975dc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b240",
      "incomplete_value": true,
      "site": "0044b250",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428740",
      "incomplete_value": true,
      "site": "00428750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:676:8"
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
      "definition_site": "0044b254",
      "incomplete_value": true,
      "site": "0044b254",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00428754",
      "incomplete_value": true,
      "site": "00428754",
      "value": [
        "LOAD",
        "8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b260",
      "incomplete_value": false,
      "site": "0044b268",
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
            "const:f16:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428760",
      "incomplete_value": false,
      "site": "00428768",
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
            "const:3a7:8"
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
      "0044b240",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "0044b248",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "0044b260",
      "PARAM",
      [
        "storage",
        "002a73a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b240",
      "READ",
      [
        "storage",
        "002bfb5a",
        null,
        "string"
      ]
    ],
    [
      "0044b248",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "0044b260",
      "PARAM",
      [
        "storage",
        "002b7f16",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428714.md#insn-00428768) · [`00428730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428714.md#insn-00428730) · [`00428734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428714.md#insn-00428734)
- 新版 `0044b268`（命令位置の公開資料なし） · `0044b230`（命令位置の公開資料なし） · `0044b234`（命令位置の公開資料なし）

~~~diff
- 00428768 ["INT_ADD", "register:40f0:8", ["const:428768:8", "const:4:8"]]
- 00428768 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044b268 ["INT_ADD", "register:40f0:8", ["const:44b268:8", "const:4:8"]]
+ 0044b268 ["CALL", null, ["callee:00c57b70:8"]]
- 00428768 bytes 6eca1e94
+ 0044b268 bytes 42322094
- 00428730 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 0044b230 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 00428730 bytes 29f4ffd0
+ 0044b230 bytes a9f3ff90
- 00428734 ["COPY", "tmp:0:8", ["const:676:8"]]
- 00428734 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00428734 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00428734 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0044b234 ["COPY", "tmp:0:8", ["const:b5a:8"]]
+ 0044b234 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0044b234 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0044b234 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00428734 bytes 29d91991
+ 0044b234 bytes 29692d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08cdef4763d5d9644889a355f22c0044"></a>

### [`004288b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004288b4.md) → [`0044b3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b3b4.md) FUN_0044b3b4

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`0042f000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`00432904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432904.md) [`00432e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432e80.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 10件 [`00451e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`0045579c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md) [`00455d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/00455d18.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b3d8",
      "incomplete_value": true,
      "site": "0044b3ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004288d8",
      "incomplete_value": true,
      "site": "004288ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b80:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b3e4",
      "incomplete_value": true,
      "site": "0044b3f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:918:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004288e4",
      "incomplete_value": true,
      "site": "004288f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2cc:8"
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
      "definition_site": "0044b3e4",
      "incomplete_value": true,
      "site": "0044b3f0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004288e4",
      "incomplete_value": true,
      "site": "004288f0",
      "value": [
        "LOAD",
        "16",
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
      "0044b3d8",
      "READ",
      [
        "storage",
        "002b1b80",
        null,
        null
      ]
    ],
    [
      "0044b3e4",
      "READ",
      [
        "storage",
        "002a12cc",
        null,
        "string"
      ]
    ],
    [
      "0044b3e4",
      "READ",
      [
        "storage",
        "002a12dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b3d8",
      "READ",
      [
        "storage",
        "002c3260",
        null,
        null
      ]
    ],
    [
      "0044b3e4",
      "READ",
      [
        "storage",
        "002b1918",
        null,
        "string"
      ]
    ],
    [
      "0044b3e4",
      "READ",
      [
        "storage",
        "002b1928",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004288c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004288b4.md#insn-004288c8) · [`004288cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004288b4.md#insn-004288cc) · [`004288d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004288b4.md#insn-004288d8)
- 新版 `0044b3c8`（命令位置の公開資料なし） · `0044b3cc`（命令位置の公開資料なし） · `0044b3d8`（命令位置の公開資料なし）

~~~diff
- 004288c8 ["INT_ADD", "register:40f0:8", ["const:4288c8:8", "const:4:8"]]
- 004288c8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0044b3c8 ["INT_ADD", "register:40f0:8", ["const:44b3c8:8", "const:4:8"]]
+ 0044b3c8 ["CALL", null, ["callee:00c57a90:8"]]
- 004288c8 bytes dec91e94
+ 0044b3c8 bytes b2312094
- 004288cc ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 0044b3cc ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 004288cc bytes 48f4ffb0
+ 0044b3cc bytes c8f3ff90
- 004288d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b80:8"]]
- 004288d8 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 004288d8 ["COPY", "register:5010:8", ["const:0:8"]]
- 004288d8 ["COPY", "register:5018:8", ["const:0:8"]]
+ 0044b3d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
+ 0044b3d8 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0044b3d8 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0044b3d8 ["COPY", "register:5018:8", ["const:0:8"]]
- 004288d8 bytes 00e1c23d
+ 0044b3d8 bytes 0099c03d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3541d469a2c69e3e973f4a0e4295116"></a>

### [`004289a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289a4.md) → [`0044b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4a4.md) FUN_0044b4a4

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`0043344c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/0043344c.md) [`00434024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434024.md) [`00434528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/00434528.md) [`004349a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00434/004349a0.md) [`00435358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435358.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 7件 [`004562e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md) [`00456ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/00456ebc.md) [`004573c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md) [`00457838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/00457838.md) [`004581f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/004581f0.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b4c8",
      "incomplete_value": true,
      "site": "0044b4dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004289c8",
      "incomplete_value": true,
      "site": "004289dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b80:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b4d4",
      "incomplete_value": true,
      "site": "0044b4e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:131:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004289d4",
      "incomplete_value": true,
      "site": "004289e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:640:8"
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
      "definition_site": "0044b4d4",
      "incomplete_value": true,
      "site": "0044b4e0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "004289d4",
      "incomplete_value": true,
      "site": "004289e0",
      "value": [
        "LOAD",
        "16",
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
      "0044b4c8",
      "READ",
      [
        "storage",
        "002b1b80",
        null,
        null
      ]
    ],
    [
      "0044b4d4",
      "READ",
      [
        "storage",
        "002a6640",
        null,
        "string"
      ]
    ],
    [
      "0044b4d4",
      "READ",
      [
        "storage",
        "002a6650",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b4c8",
      "READ",
      [
        "storage",
        "002c3260",
        null,
        null
      ]
    ],
    [
      "0044b4d4",
      "READ",
      [
        "storage",
        "002b7131",
        null,
        "string"
      ]
    ],
    [
      "0044b4d4",
      "READ",
      [
        "storage",
        "002b7141",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004289b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289a4.md#insn-004289b8) · [`004289bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289a4.md#insn-004289bc) · [`004289c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289a4.md#insn-004289c8)
- 新版 `0044b4b8`（命令位置の公開資料なし） · `0044b4bc`（命令位置の公開資料なし） · `0044b4c8`（命令位置の公開資料なし）

~~~diff
- 004289b8 ["INT_ADD", "register:40f0:8", ["const:4289b8:8", "const:4:8"]]
- 004289b8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0044b4b8 ["INT_ADD", "register:40f0:8", ["const:44b4b8:8", "const:4:8"]]
+ 0044b4b8 ["CALL", null, ["callee:00c57a90:8"]]
- 004289b8 bytes a2c91e94
+ 0044b4b8 bytes 76312094
- 004289bc ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 0044b4bc ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 004289bc bytes 48f4ffb0
+ 0044b4bc bytes c8f3ff90
- 004289c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b80:8"]]
- 004289c8 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 004289c8 ["COPY", "register:5010:8", ["const:0:8"]]
- 004289c8 ["COPY", "register:5018:8", ["const:0:8"]]
+ 0044b4c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
+ 0044b4c8 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0044b4c8 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0044b4c8 ["COPY", "register:5018:8", ["const:0:8"]]
- 004289c8 bytes 00e1c23d
+ 0044b4c8 bytes 0099c03d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a6566501d00a65a00536ed27ab96745"></a>

### [`004289f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289f4.md) → [`0044b4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b4f4.md) FUN_0044b4f4

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00419718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419718.md) [`0042ca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca70.md) [`0042ce34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ce34.md) [`00431534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md) [`00a26e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a26/00a26e20.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 5件 [`0043c218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043c/0043c218.md) [`0044f908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md) [`0044fccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md) [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) [`00a84cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84cb0.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b51c",
      "incomplete_value": true,
      "site": "0044b528",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428a1c",
      "incomplete_value": true,
      "site": "00428a28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:300:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b518",
      "incomplete_value": true,
      "site": "0044b52c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:99e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428a18",
      "incomplete_value": true,
      "site": "00428a2c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:be0:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0044b518",
      "incomplete_value": true,
      "site": "0044b52c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00428a18",
      "incomplete_value": true,
      "site": "00428a2c",
      "value": [
        "LOAD",
        "16",
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
      "0044b518",
      "READ",
      [
        "storage",
        "00298be0",
        null,
        "string"
      ]
    ],
    [
      "0044b518",
      "READ",
      [
        "storage",
        "00298bf0",
        null,
        "string"
      ]
    ],
    [
      "0044b51c",
      "READ",
      [
        "storage",
        "002b1300",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0044b518",
      "READ",
      [
        "storage",
        "002a899e",
        null,
        "string"
      ]
    ],
    [
      "0044b518",
      "READ",
      [
        "storage",
        "002a89ae",
        null,
        "string"
      ]
    ],
    [
      "0044b51c",
      "READ",
      [
        "storage",
        "002c2940",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289f4.md#insn-00428a08) · [`00428a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289f4.md#insn-00428a0c) · [`00428a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/004289f4.md#insn-00428a10)
- 新版 `0044b508`（命令位置の公開資料なし） · `0044b50c`（命令位置の公開資料なし） · `0044b510`（命令位置の公開資料なし）

~~~diff
- 00428a08 ["INT_ADD", "register:40f0:8", ["const:428a08:8", "const:4:8"]]
- 00428a08 ["CALL", null, ["callee:00c57a90:8"]]
+ 0044b508 ["INT_ADD", "register:40f0:8", ["const:44b508:8", "const:4:8"]]
+ 0044b508 ["CALL", null, ["callee:00c57a90:8"]]
- 00428a08 bytes 8ec91e94
+ 0044b508 bytes 62312094
- 00428a0c ["COPY", "register:4040:8", ["const:298000:8"]]
+ 0044b50c ["COPY", "register:4040:8", ["const:2a8000:8"]]
- 00428a0c bytes 88f3ff90
+ 0044b50c bytes e8f2ffb0
- 00428a10 ["COPY", "tmp:0:8", ["const:be0:8"]]
- 00428a10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428a10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428a10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044b510 ["COPY", "tmp:0:8", ["const:99e:8"]]
+ 0044b510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044b510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044b510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428a10 bytes 08812f91
+ 0044b510 bytes 08792691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45ab45d7fb590d237a89fdd189525757"></a>

### [`00428a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428a44.md) → [`0044b544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044b544.md) FUN_0044b544

採用 · 移動量 `+0x22b00` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) [`00454f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00454/00454f34.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb100.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 2件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) [`00477dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00477/00477dcc.md) · 呼出先 6件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 83.64% / 新版 83.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b584",
      "incomplete_value": true,
      "site": "0044b590",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00428a84",
      "incomplete_value": true,
      "site": "00428a90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f20:8"
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
      "definition_site": "0044b580",
      "incomplete_value": true,
      "site": "0044b594",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:eb4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428a80",
      "incomplete_value": true,
      "site": "00428a94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0044b580",
      "incomplete_value": true,
      "site": "0044b594",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00428a80",
      "incomplete_value": true,
      "site": "00428a94",
      "value": [
        "LOAD",
        "16",
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
      "0044b580",
      "READ",
      [
        "storage",
        "002af890",
        null,
        "string"
      ]
    ],
    [
      "0044b580",
      "READ",
      [
        "storage",
        "002af8a0",
        null,
        "string"
      ]
    ],
    [
      "0044b584",
      "READ",
      [
        "storage",
        "002b0f20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0044b580",
      "READ",
      [
        "storage",
        "002c0eb4",
        null,
        "string"
      ]
    ],
    [
      "0044b580",
      "READ",
      [
        "storage",
        "002c0ec4",
        null,
        "string"
      ]
    ],
    [
      "0044b584",
      "READ",
      [
        "storage",
        "002c2510",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428a44.md#insn-00428ab4) · [`00428a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428a44.md#insn-00428a70) · [`00428a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428a44.md#insn-00428a74)
- 新版 `0044b5b4`（命令位置の公開資料なし） · `0044b570`（命令位置の公開資料なし） · `0044b574`（命令位置の公開資料なし）

~~~diff
- 00428ab4 ["INT_ADD", "register:40f0:8", ["const:428ab4:8", "const:4:8"]]
- 00428ab4 ["CALL", null, ["callee:00c57b70:8"]]
+ 0044b5b4 ["INT_ADD", "register:40f0:8", ["const:44b5b4:8", "const:4:8"]]
+ 0044b5b4 ["CALL", null, ["callee:00c57b70:8"]]
- 00428ab4 bytes 9bc91e94
+ 0044b5b4 bytes 6f312094
- 00428a70 ["INT_ADD", "register:40f0:8", ["const:428a70:8", "const:4:8"]]
- 00428a70 ["CALL", null, ["callee:00c57a90:8"]]
+ 0044b570 ["INT_ADD", "register:40f0:8", ["const:44b570:8", "const:4:8"]]
+ 0044b570 ["CALL", null, ["callee:00c57a90:8"]]
- 00428a70 bytes 74c91e94
+ 0044b570 bytes 48312094
- 00428a74 ["COPY", "register:4040:8", ["const:2af000:8"]]
+ 0044b574 ["COPY", "register:4040:8", ["const:2c0000:8"]]
- 00428a74 bytes 28f4fff0
+ 0044b574 bytes a8f3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

