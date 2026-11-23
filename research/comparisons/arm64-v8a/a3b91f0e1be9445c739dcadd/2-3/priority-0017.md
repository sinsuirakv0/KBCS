# v15.7.4 → v16.0.0 · 最優先の変更候補 (17)

[一覧の目次](README.md)

<a id="compare-cec158ada73958d363cab0ddad0aee6c"></a>

### [`00542b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md) → [`00565a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565a18.md) FUN_00565a18

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00545aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545aa4.md) [`005463e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/005463e4.md) [`00546608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/00546608.md) [`0054729c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054729c.md) [`00547a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547a3c.md) · 呼出先 9件 [`00549b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549b88.md) [`00549f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549f74.md) [`0054a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a194.md) [`0054a8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a8fc.md) [`0054aaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054aaa4.md)
- 新版 呼出元 5件 [`0056893c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/0056893c.md) [`0056927c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/0056927c.md) [`005694a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005694a0.md) [`0056a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md) [`0056a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a8d4.md) · 呼出先 9件 [`0056ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ca20.md) [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md) [`0056d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d02c.md) [`0056d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d794.md) [`0056d93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d93c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00565bfc",
      "incomplete_value": true,
      "site": "00565bfc",
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
      "definition_site": "00542d64",
      "incomplete_value": true,
      "site": "00542d64",
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
      "00565bec",
      "DATA",
      [
        "storage",
        "002b0b7c",
        null,
        null
      ]
    ],
    [
      "00565c04",
      "DATA",
      [
        "storage",
        "002b19f0",
        null,
        "string"
      ]
    ],
    [
      "00566614",
      "DATA",
      [
        "storage",
        "002bfda8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00565bec",
      "DATA",
      [
        "storage",
        "002c216c",
        null,
        null
      ]
    ],
    [
      "00565c04",
      "DATA",
      [
        "storage",
        "002c30a0",
        null,
        "string"
      ]
    ],
    [
      "00566614",
      "DATA",
      [
        "storage",
        "002d14e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00542bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md#insn-00542bcc) · [`00542cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md#insn-00542cdc) · [`00542d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542b80.md#insn-00542d38)
- 新版 `00565a64`（命令位置の公開資料なし） · `00565b74`（命令位置の公開資料なし） · `00565bd0`（命令位置の公開資料なし）

~~~diff
- 00542bcc ["INT_ADD", "register:40f0:8", ["const:542bcc:8", "const:4:8"]]
- 00542bcc ["CALL", null, ["callee:0056ca20:8"]]
+ 00565a64 ["INT_ADD", "register:40f0:8", ["const:565a64:8", "const:4:8"]]
+ 00565a64 ["CALL", null, ["callee:0056ca20:8"]]
- 00542bcc bytes ef1b0094
+ 00565a64 bytes ef1b0094
- 00542cdc ["INT_ADD", "register:40f0:8", ["const:542cdc:8", "const:4:8"]]
- 00542cdc ["CALL", null, ["callee:0056d02c:8"]]
+ 00565b74 ["INT_ADD", "register:40f0:8", ["const:565b74:8", "const:4:8"]]
+ 00565b74 ["CALL", null, ["callee:0056d02c:8"]]
- 00542cdc bytes 2e1d0094
+ 00565b74 bytes 2e1d0094
- 00542d38 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 00565bd0 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 00542d38 bytes 69ebffd0
+ 00565bd0 bytes e9eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da3f88eb02dae04ec82a0785068edce5"></a>

### [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) → [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) FUN_00566bc0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054729c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054729c.md) · 呼出先 28件 [`00542a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/00542a44.md) [`00545a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00545/00545a50.md) [`0054709c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/0054709c.md) [`00547138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547138.md) [`00549f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549f74.md)
- 新版 呼出元 1件 [`0056a134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056a134.md) · 呼出先 28件 [`005658dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005658dc.md) [`005688e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00568/005688e8.md) [`00569f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569f34.md) [`00569fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md) [`0056ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056ce0c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.73% / 新版 99.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00567a78",
      "incomplete_value": true,
      "site": "00567a88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00544be0",
      "incomplete_value": true,
      "site": "00544bf0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 113,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0056702c",
      "value": [
        "leaf",
        "ram:56f670:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00544194",
      "value": [
        "leaf",
        "ram:54c7d8:8"
      ]
    },
    "ordinal": 39,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00567600",
      "value": [
        "leaf",
        "ram:56f734:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00544768",
      "value": [
        "leaf",
        "ram:54c89c:8"
      ]
    },
    "ordinal": 75,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00566ce4",
      "READ",
      [
        "storage",
        "00c23f0c",
        null,
        "string"
      ]
    ],
    [
      "00566cec",
      "READ",
      [
        "storage",
        "00c23f10",
        null,
        "string"
      ]
    ],
    [
      "00566e90",
      "READ",
      [
        "storage",
        "00c23f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00566ce4",
      "READ",
      [
        "storage",
        "00ca39f4",
        null,
        "string"
      ]
    ],
    [
      "00566cec",
      "READ",
      [
        "storage",
        "00ca39f8",
        null,
        "string"
      ]
    ],
    [
      "00566e90",
      "READ",
      [
        "storage",
        "00ca39f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00544194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md#insn-00544194) · [`00544768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md#insn-00544768) · [`00544e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md#insn-00544e8c)
- 新版 `0056702c`（命令位置の公開資料なし） · `00567600`（命令位置の公開資料なし） · `00567d24`（命令位置の公開資料なし）

~~~diff
- 00544194 ["INT_ADD", "register:40f0:8", ["const:544194:8", "const:4:8"]]
- 00544194 ["CALL", null, ["ram:54c7d8:8"]]
+ 0056702c ["INT_ADD", "register:40f0:8", ["const:56702c:8", "const:4:8"]]
+ 0056702c ["CALL", null, ["ram:56f670:8"]]
- 00544194 bytes 91210094
+ 0056702c bytes 91210094
- 00544768 ["INT_ADD", "register:40f0:8", ["const:544768:8", "const:4:8"]]
- 00544768 ["CALL", null, ["ram:54c89c:8"]]
+ 00567600 ["INT_ADD", "register:40f0:8", ["const:567600:8", "const:4:8"]]
+ 00567600 ["CALL", null, ["ram:56f734:8"]]
- 00544768 bytes 4d200094
+ 00567600 bytes 4d200094
- 00544e8c ["INT_ADD", "register:40f0:8", ["const:544e8c:8", "const:4:8"]]
- 00544e8c ["CALL", null, ["callee:00c59c40:8"]]
+ 00567d24 ["INT_ADD", "register:40f0:8", ["const:567d24:8", "const:4:8"]]
+ 00567d24 ["CALL", null, ["callee:00c59c40:8"]]
- 00544e8c bytes d9601a94
+ 00567d24 bytes c7c71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-052ebec766423a2b1f304f2b79594ceb"></a>

### [`00547c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547c90.md) → [`0056ab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) FUN_0056ab28

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004183ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183ec.md) · 呼出先 11件 [`00548094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548094.md) [`00548104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548104.md) [`0054841c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/0054841c.md) [`0054df60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054df60.md) [`0054df6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054df6c.md)
- 新版 呼出元 1件 [`0043aeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043aeec.md) · 呼出先 11件 [`0056af2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af2c.md) [`0056af9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056af9c.md) [`0056b2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b2b4.md) [`00570df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570df8.md) [`00570e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 82.63% / 新版 82.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 12件, `call_target` 4件, `store_condition` 5件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056ac70",
      "incomplete_value": false,
      "site": "0056ac7c",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00547dd8",
      "incomplete_value": false,
      "site": "00547de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056acec",
      "incomplete_value": false,
      "site": "0056acec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00547e54",
      "incomplete_value": false,
      "site": "00547e54",
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
            "const:e78:8"
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
      "definition_site": "0056ada0",
      "incomplete_value": false,
      "site": "0056ada0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00547f08",
      "incomplete_value": false,
      "site": "00547f08",
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
            "const:e78:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056ab58",
      "READ",
      [
        "storage",
        "00c25e88",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ab70",
      "PARAM",
      [
        "storage",
        "00c25e88",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ab94",
      "READ",
      [
        "storage",
        "00c25e88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056ab58",
      "READ",
      [
        "storage",
        "00ca5948",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ab70",
      "PARAM",
      [
        "storage",
        "00ca5948",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ab94",
      "READ",
      [
        "storage",
        "00ca5948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00547cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547c90.md#insn-00547cf4) · [`00547d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547c90.md#insn-00547d0c) · [`00547d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547c90.md#insn-00547d34)
- 新版 `0056ab8c`（命令位置の公開資料なし） · `0056aba4`（命令位置の公開資料なし） · `0056abcc`（命令位置の公開資料なし）

~~~diff
- 00547cf4 ["INT_ADD", "register:40f0:8", ["const:547cf4:8", "const:4:8"]]
- 00547cf4 ["CALL", null, ["callee:00c59cb0:8"]]
+ 0056ab8c ["INT_ADD", "register:40f0:8", ["const:56ab8c:8", "const:4:8"]]
+ 0056ab8c ["CALL", null, ["callee:00c59cb0:8"]]
- 00547cf4 bytes 5b551a94
+ 0056ab8c bytes 49bc1b94
- 00547d0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00547d0c ["INT_ADD", "register:40f0:8", ["const:547d0c:8", "const:4:8"]]
- 00547d0c ["CALLIND", null, ["register:0:8"]]
+ 0056aba4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056aba4 ["INT_ADD", "register:40f0:8", ["const:56aba4:8", "const:4:8"]]
+ 0056aba4 ["CALLIND", null, ["register:0:8"]]
- 00547d0c bytes 00013fd6
+ 0056aba4 bytes 00013fd6
- 00547d34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00547d34 ["INT_ADD", "register:40f0:8", ["const:547d34:8", "const:4:8"]]
- 00547d34 ["CALLIND", null, ["register:0:8"]]
+ 0056abcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056abcc ["INT_ADD", "register:40f0:8", ["const:56abcc:8", "const:4:8"]]
+ 0056abcc ["CALLIND", null, ["register:0:8"]]
- 00547d34 bytes 00013fd6
+ 0056abcc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69217d39ea4478881517e4f6baabeb96"></a>

### [`00548364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548364.md) → [`0056b1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b1fc.md) FUN_0056b1fc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00458f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00458/00458f08.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0047bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047bda0.md) · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056b218",
      "incomplete_value": true,
      "site": "0056b21c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00548380",
      "incomplete_value": true,
      "site": "00548384",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "0056b214",
      "READ",
      [
        "storage",
        "00c25e58",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b214",
      "READ",
      [
        "storage",
        "00c25e60",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b260",
      "READ",
      [
        "storage",
        "00c25e70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056b214",
      "READ",
      [
        "storage",
        "00ca5918",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b214",
      "READ",
      [
        "storage",
        "00ca5920",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b260",
      "READ",
      [
        "storage",
        "00ca5930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00548374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548364.md#insn-00548374) · [`00548378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548364.md#insn-00548378) · [`005483ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548364.md#insn-005483ac)
- 新版 `0056b20c`（命令位置の公開資料なし） · `0056b210`（命令位置の公開資料なし） · `0056b244`（命令位置の公開資料なし）

~~~diff
- 00548374 ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 0056b20c ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 00548374 bytes e83600b0
+ 0056b20c bytes c83900d0
- 00548378 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00548378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00548378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00548378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b210 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 0056b210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00548378 bytes 08613991
+ 0056b210 bytes 08612491
- 005483ac ["COPY", "register:0:8", ["register:4040:8"]]
- 005483ac ["INT_ADD", "register:40f0:8", ["const:5483ac:8", "const:4:8"]]
- 005483ac ["CALLIND", null, ["register:0:8"]]
+ 0056b244 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b244 ["INT_ADD", "register:40f0:8", ["const:56b244:8", "const:4:8"]]
+ 0056b244 ["CALLIND", null, ["register:0:8"]]
- 005483ac bytes 00013fd6
+ 0056b244 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-826dcfd052d7098c1597878f13b4132b"></a>

### [`0054841c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/0054841c.md) → [`0056b2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b2b4.md) FUN_0056b2b4

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00547c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547c90.md) · 呼出先 3件 [`0054873c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/0054873c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd270.md)
- 新版 呼出元 1件 [`0056ab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056ab28.md) · 呼出先 3件 [`0056b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b5d4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cc0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.78% / 新版 82.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b2f0",
      "incomplete_value": false,
      "site": "0056b2f4",
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
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00548458",
      "incomplete_value": false,
      "site": "0054845c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "definition_site": "0056b36c",
      "incomplete_value": true,
      "site": "0056b374",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2d1000:8"
              ],
              [
                "leaf",
                "const:48c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005484d4",
      "incomplete_value": true,
      "site": "005484dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d4c:8"
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
      "definition_site": "0056b378",
      "incomplete_value": true,
      "site": "0056b390",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005484e0",
      "incomplete_value": true,
      "site": "005484f8",
      "value": [
        "LOAD",
        "16",
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
      "0056b2f4",
      "DATA",
      [
        "storage",
        "00bee730",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b320",
      "READ",
      [
        "storage",
        "00c25e98",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b36c",
      "READ",
      [
        "storage",
        "002bfd4c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0056b2f4",
      "DATA",
      [
        "storage",
        "00c6b2f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b320",
      "READ",
      [
        "storage",
        "00ca5958",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b36c",
      "READ",
      [
        "storage",
        "002d148c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005485a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/0054841c.md#insn-005485a4) · [`005485f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/0054841c.md#insn-005485f4) · [`005486d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/0054841c.md#insn-005486d0)
- 新版 `0056b43c`（命令位置の公開資料なし） · `0056b48c`（命令位置の公開資料なし） · `0056b568`（命令位置の公開資料なし）

~~~diff
- 005485a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005485a4 ["INT_ADD", "register:40f0:8", ["const:5485a4:8", "const:4:8"]]
- 005485a4 ["CALLIND", null, ["register:0:8"]]
+ 0056b43c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b43c ["INT_ADD", "register:40f0:8", ["const:56b43c:8", "const:4:8"]]
+ 0056b43c ["CALLIND", null, ["register:0:8"]]
- 005485a4 bytes 00013fd6
+ 0056b43c bytes 00013fd6
- 005485f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005485f4 ["INT_ADD", "register:40f0:8", ["const:5485f4:8", "const:4:8"]]
- 005485f4 ["CALLIND", null, ["register:0:8"]]
+ 0056b48c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b48c ["INT_ADD", "register:40f0:8", ["const:56b48c:8", "const:4:8"]]
+ 0056b48c ["CALLIND", null, ["register:0:8"]]
- 005485f4 bytes 00013fd6
+ 0056b48c bytes 00013fd6
- 005486d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005486d0 ["INT_ADD", "register:40f0:8", ["const:5486d0:8", "const:4:8"]]
- 005486d0 ["CALLIND", null, ["register:0:8"]]
+ 0056b568 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b568 ["INT_ADD", "register:40f0:8", ["const:56b568:8", "const:4:8"]]
+ 0056b568 ["CALLIND", null, ["register:0:8"]]
- 005486d0 bytes 00013fd6
+ 0056b568 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7957c043a51dbdf8b5fe4b8e7dcb5d7f"></a>

### [`005488c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005488c4.md) → [`0056b75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056b75c.md) FUN_0056b75c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054df60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054df60.md) · 呼出先 8件 [`005426ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005426ac.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 1件 [`00570df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570df8.md) · 呼出先 8件 [`00565544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/00565544.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b774",
      "incomplete_value": false,
      "site": "0056b778",
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
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005488dc",
      "incomplete_value": false,
      "site": "005488e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056b7c8",
      "incomplete_value": false,
      "site": "0056b7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00548930",
      "incomplete_value": false,
      "site": "00548930",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056b778",
      "DATA",
      [
        "storage",
        "00bee730",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b7c0",
      "READ",
      [
        "storage",
        "00c25ea0",
        null,
        "undefined4"
      ]
    ],
    [
      "0056b7c8",
      "WRITE",
      [
        "storage",
        "00c25ea0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0056b778",
      "DATA",
      [
        "storage",
        "00c6b2f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b7c0",
      "READ",
      [
        "storage",
        "00ca5960",
        null,
        "undefined4"
      ]
    ],
    [
      "0056b7c8",
      "WRITE",
      [
        "storage",
        "00ca5960",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00548930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005488c4.md#insn-00548930) · [`005488d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005488c4.md#insn-005488d8) · [`005488dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/005488c4.md#insn-005488dc)
- 新版 `0056b7c8`（命令位置の公開資料なし） · `0056b770`（命令位置の公開資料なし） · `0056b774`（命令位置の公開資料なし）

~~~diff
- 00548930 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00548930 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 0056b7c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:960:8"]]
+ 0056b7c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00548930 bytes 09a10eb9
+ 0056b7c8 bytes 096109b9
- 005488d8 ["COPY", "register:4048:8", ["const:bee000:8"]]
+ 0056b770 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 005488d8 bytes 293500d0
+ 0056b770 bytes 09380090
- 005488dc ["COPY", "tmp:0:8", ["const:730:8"]]
- 005488dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005488dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005488dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056b774 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 0056b774 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056b774 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056b774 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005488dc bytes 29c11c91
+ 0056b774 bytes 29c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23de55bf56242bdfda6a16f1967cce9f"></a>

### [`00549624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549624.md) → [`0056c4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c4bc.md) FUN_0056c4bc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00549864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549864.md) [`00549868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549868.md) · 呼出先 8件 [`00548e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00548/00548e1c.md) [`00bd6980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6980.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`0056c6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c6fc.md) [`0056c700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056c700.md) · 呼出先 8件 [`0056bcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056b/0056bcb4.md) [`00c533d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c533d0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.08% / 新版 92.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056c62c",
      "incomplete_value": false,
      "site": "0056c62c",
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
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00549794",
      "incomplete_value": false,
      "site": "00549794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056c4f8",
      "incomplete_value": true,
      "site": "0056c4fc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00549660",
      "incomplete_value": true,
      "site": "00549664",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056c560",
      "incomplete_value": false,
      "site": "0056c56c",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005496c8",
      "incomplete_value": false,
      "site": "005496d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
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
      "0056c4f4",
      "READ",
      [
        "storage",
        "00c25e58",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c4f4",
      "READ",
      [
        "storage",
        "00c25e60",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c560",
      "PARAM",
      [
        "storage",
        "00bee8b8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0056c4f4",
      "READ",
      [
        "storage",
        "00ca5918",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c4f4",
      "READ",
      [
        "storage",
        "00ca5920",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c560",
      "PARAM",
      [
        "storage",
        "00c6b478",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005496d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549624.md#insn-005496d4) · [`00549654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549624.md#insn-00549654) · [`00549658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00549/00549624.md#insn-00549658)
- 新版 `0056c56c`（命令位置の公開資料なし） · `0056c4ec`（命令位置の公開資料なし） · `0056c4f0`（命令位置の公開資料なし）

~~~diff
- 005496d4 ["INT_ADD", "register:40f0:8", ["const:5496d4:8", "const:4:8"]]
- 005496d4 ["CALL", null, ["callee:00c58210:8"]]
+ 0056c56c ["INT_ADD", "register:40f0:8", ["const:56c56c:8", "const:4:8"]]
+ 0056c56c ["CALL", null, ["callee:00c58210:8"]]
- 005496d4 bytes 3b481a94
+ 0056c56c bytes 29af1b94
- 00549654 ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 0056c4ec ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 00549654 bytes e8360090
+ 0056c4ec bytes c83900b0
- 00549658 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00549658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00549658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00549658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056c4f0 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 0056c4f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c4f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c4f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00549658 bytes 08613991
+ 0056c4f0 bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21d25484b94aed7ff1b211563c8dce18"></a>

### [`0054a0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a0a0.md) → [`0056cf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056c/0056cf38.md) FUN_0056cf38

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 77.05% / 新版 77.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0056cf54",
      "incomplete_value": true,
      "site": "0056cf58",
      "value": [
        "INT_SEXT",
        "8",
        [
          [
            "LOAD",
            "1",
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
      "definition_site": "0054a0bc",
      "incomplete_value": true,
      "site": "0054a0c0",
      "value": [
        "INT_SEXT",
        "8",
        [
          [
            "LOAD",
            "1",
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
      "0056cf54",
      "DATA",
      [
        "storage",
        "002b19f0",
        null,
        "string"
      ]
    ],
    [
      "0056cf84",
      "DATA",
      [
        "storage",
        "002b19f0",
        null,
        "string"
      ]
    ],
    [
      "0056cfa8",
      "DATA",
      [
        "storage",
        "002b19f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056cf54",
      "DATA",
      [
        "storage",
        "002c30a0",
        null,
        "string"
      ]
    ],
    [
      "0056cf84",
      "DATA",
      [
        "storage",
        "002c30a0",
        null,
        "string"
      ]
    ],
    [
      "0056cfa8",
      "DATA",
      [
        "storage",
        "002c30a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054a0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a0a0.md#insn-0054a0b4) · [`0054a0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a0a0.md#insn-0054a0b8) · [`0054a0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a0a0.md#insn-0054a0e0)
- 新版 `0056cf4c`（命令位置の公開資料なし） · `0056cf50`（命令位置の公開資料なし） · `0056cf78`（命令位置の公開資料なし）

~~~diff
- 0054a0b4 ["COPY", "register:4040:8", ["const:2b1000:8"]]
+ 0056cf4c ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 0054a0b4 bytes 28ebfff0
+ 0056cf4c bytes a8eafff0
- 0054a0b8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0054a0b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054a0b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054a0b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056cf50 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 0056cf50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056cf50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056cf50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054a0b8 bytes 08c12791
+ 0056cf50 bytes 08810291
- 0054a0e0 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0056cf78 ["COPY", "register:4048:8", ["const:2c3000:8"]]
- 0054a0e0 bytes 29ebfff0
+ 0056cf78 bytes a9eafff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ae62a86a0fcc4a7a63cea9d5569bec2"></a>

### [`0054a560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a560.md) → [`0056d3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d3f8.md) FUN_0056d3f8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0054645c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00546/0054645c.md) [`0054a408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a408.md) · 呼出先 5件 [`00547138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547138.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd200.md) [`00bdd220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd220.md) [`00bdd230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd230.md)
- 新版 呼出元 2件 [`005692f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/005692f4.md) [`0056d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056d/0056d2a0.md) · 呼出先 5件 [`00569fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00569/00569fd0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c50.md) [`00c59c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c70.md) [`00c59c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.13% / 新版 99.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056d63c",
      "incomplete_value": true,
      "site": "0056d640",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054a7a4",
      "incomplete_value": true,
      "site": "0054a7a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e8:8"
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
      "0056d63c",
      "READ",
      [
        "storage",
        "002b28e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056d63c",
      "READ",
      [
        "storage",
        "002c3fd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054a5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a560.md#insn-0054a5e8) · [`0054a608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a560.md#insn-0054a608) · [`0054a640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054a/0054a560.md#insn-0054a640)
- 新版 `0056d480`（命令位置の公開資料なし） · `0056d4a0`（命令位置の公開資料なし） · `0056d4d8`（命令位置の公開資料なし）

~~~diff
- 0054a5e8 ["INT_ADD", "register:40f0:8", ["const:54a5e8:8", "const:4:8"]]
- 0054a5e8 ["CALL", null, ["callee:00c59c50:8"]]
+ 0056d480 ["INT_ADD", "register:40f0:8", ["const:56d480:8", "const:4:8"]]
+ 0056d480 ["CALL", null, ["callee:00c59c50:8"]]
- 0054a5e8 bytes 064b1a94
+ 0056d480 bytes f4b11b94
- 0054a608 ["INT_ADD", "register:40f0:8", ["const:54a608:8", "const:4:8"]]
- 0054a608 ["CALL", null, ["callee:00c59c70:8"]]
+ 0056d4a0 ["INT_ADD", "register:40f0:8", ["const:56d4a0:8", "const:4:8"]]
+ 0056d4a0 ["CALL", null, ["callee:00c59c70:8"]]
- 0054a608 bytes 064b1a94
+ 0056d4a0 bytes f4b11b94
- 0054a640 ["INT_ADD", "register:40f0:8", ["const:54a640:8", "const:4:8"]]
- 0054a640 ["CALL", null, ["callee:00c59c70:8"]]
+ 0056d4d8 ["INT_ADD", "register:40f0:8", ["const:56d4d8:8", "const:4:8"]]
+ 0056d4d8 ["CALL", null, ["callee:00c59c70:8"]]
- 0054a640 bytes f84a1a94
+ 0056d4d8 bytes e6b11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c53b44cd96f808b463153cc4c0e0ed31"></a>

### [`0054cec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cec8.md) → [`0056fd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056f/0056fd60.md) FUN_0056fd60

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00543d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00543/00543d28.md) · 呼出先 3件 [`00bdb590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb590.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00bdd2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2d0.md)
- 新版 呼出元 1件 [`00566bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00566/00566bc0.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fe0.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c59d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00570040",
      "incomplete_value": true,
      "site": "00570044",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054d1a8",
      "incomplete_value": true,
      "site": "0054d1ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00570048",
      "incomplete_value": true,
      "site": "0057004c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:130:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054d1b0",
      "incomplete_value": true,
      "site": "0054d1b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a60:8"
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
      "definition_site": "0057028c",
      "incomplete_value": true,
      "site": "00570290",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054d3f4",
      "incomplete_value": true,
      "site": "0054d3f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056ff40",
      "READ",
      [
        "storage",
        "002b2ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00570040",
      "READ",
      [
        "storage",
        "002b0d50",
        null,
        null
      ]
    ],
    [
      "00570048",
      "READ",
      [
        "storage",
        "002b1a60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0056ff40",
      "READ",
      [
        "storage",
        "002c43b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00570040",
      "READ",
      [
        "storage",
        "002c2350",
        null,
        null
      ]
    ],
    [
      "00570048",
      "READ",
      [
        "storage",
        "002c3130",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054cf4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cec8.md#insn-0054cf4c) · [`0054cf68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cec8.md#insn-0054cf68) · [`0054d018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054c/0054cec8.md#insn-0054d018)
- 新版 `0056fde4`（命令位置の公開資料なし） · `0056fe00`（命令位置の公開資料なし） · `0056feb0`（命令位置の公開資料なし）

~~~diff
- 0054cf4c ["INT_ADD", "register:40f0:8", ["const:54cf4c:8", "const:4:8"]]
- 0054cf4c ["CALL", null, ["callee:00c59c20:8"]]
+ 0056fde4 ["INT_ADD", "register:40f0:8", ["const:56fde4:8", "const:4:8"]]
+ 0056fde4 ["CALL", null, ["callee:00c59c20:8"]]
- 0054cf4c bytes a1401a94
+ 0056fde4 bytes 8fa71b94
- 0054cf68 ["INT_ADD", "register:40f0:8", ["const:54cf68:8", "const:4:8"]]
- 0054cf68 ["CALL", null, ["callee:00c59c20:8"]]
+ 0056fe00 ["INT_ADD", "register:40f0:8", ["const:56fe00:8", "const:4:8"]]
+ 0056fe00 ["CALL", null, ["callee:00c59c20:8"]]
- 0054cf68 bytes 9a401a94
+ 0056fe00 bytes 88a71b94
- 0054d018 ["INT_ADD", "register:40f0:8", ["const:54d018:8", "const:4:8"]]
- 0054d018 ["CALL", null, ["callee:00c59c20:8"]]
+ 0056feb0 ["INT_ADD", "register:40f0:8", ["const:56feb0:8", "const:4:8"]]
+ 0056feb0 ["CALL", null, ["callee:00c59c20:8"]]
- 0054d018 bytes 6e401a94
+ 0056feb0 bytes 5ca71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-629b1fa69750d095627d9c204d85b433"></a>

### [`0054e0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e0c8.md) → [`00570f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570f60.md) FUN_00570f60

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0054df6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054d/0054df6c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00570e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570e04.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00570f70",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054e0d8",
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
      "definition_site": "00570f6c",
      "incomplete_value": true,
      "site": "00570f70",
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
    "old": {
      "definition_site": "0054e0d4",
      "incomplete_value": true,
      "site": "0054e0d8",
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
      "00570f6c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00570f70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00570f6c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00570f70",
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

- 旧版 [`0054e0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e0c8.md#insn-0054e0d8) · [`0054e0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e0c8.md#insn-0054e0d0) · [`0054e0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e0c8.md#insn-0054e0d4)
- 新版 `00570f70`（命令位置の公開資料なし） · `00570f68`（命令位置の公開資料なし） · `00570f6c`（命令位置の公開資料なし）

~~~diff
- 0054e0d8 ["INT_ADD", "register:40f0:8", ["const:54e0d8:8", "const:4:8"]]
- 0054e0d8 ["CALL", null, ["ram:418c38:8"]]
+ 00570f70 ["INT_ADD", "register:40f0:8", ["const:570f70:8", "const:4:8"]]
+ 00570f70 ["CALL", null, ["ram:43b738:8"]]
- 0054e0d8 bytes d82afb97
+ 00570f70 bytes f229fb97
- 0054e0d0 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00570f68 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0054e0d0 bytes c0eaffb0
+ 00570f68 bytes 20eafff0
- 0054e0d4 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0054e0d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0054e0d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0054e0d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00570f6c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00570f6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00570f6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00570f6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0054e0d4 bytes 00740e91
+ 00570f6c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9422a6e884d0815ea0e57b7e3cb58b6"></a>

### [`0054e138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e138.md) → [`00570fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00570/00570fd0.md) FUN_00570fd0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00570fe8",
      "incomplete_value": false,
      "site": "00570fec",
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
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e150",
      "incomplete_value": false,
      "site": "0054e154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
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
      "site": "00571020",
      "value": [
        "leaf",
        "ram:c57aa0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054e188",
      "value": [
        "leaf",
        "ram:bdb050:8"
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
      "00570fec",
      "DATA",
      [
        "storage",
        "00bee8e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00571020",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb050"
      ]
    ]
  ],
  "added": [
    [
      "00570fec",
      "DATA",
      [
        "storage",
        "00c6b4a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00571020",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57aa0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e138.md#insn-0054e188) · [`0054e14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e138.md#insn-0054e14c) · [`0054e150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e138.md#insn-0054e150)
- 新版 `00571020`（命令位置の公開資料なし） · `00570fe4`（命令位置の公開資料なし） · `00570fe8`（命令位置の公開資料なし）

~~~diff
- 0054e188 ["INT_ADD", "register:40f0:8", ["const:54e188:8", "const:4:8"]]
- 0054e188 ["CALL", null, ["ram:bdb050:8"]]
+ 00571020 ["INT_ADD", "register:40f0:8", ["const:571020:8", "const:4:8"]]
+ 00571020 ["CALL", null, ["ram:c57aa0:8"]]
- 0054e188 bytes b2331a94
+ 00571020 bytes a09a1b94
- 0054e14c ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00570fe4 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0054e14c bytes 08350090
+ 00570fe4 bytes c83700f0
- 0054e150 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 0054e150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054e150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054e150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00570fe8 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 00570fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00570fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00570fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054e150 bytes 08812391
+ 00570fe8 bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-011122ec1510ff85b9d820bd9311cace"></a>

### [`0054e278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e278.md) → [`00571110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571110.md) FUN_00571110

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00571128",
      "incomplete_value": false,
      "site": "0057112c",
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
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e290",
      "incomplete_value": false,
      "site": "0054e294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00571160",
      "value": [
        "leaf",
        "ram:c57aa0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0054e2c8",
      "value": [
        "leaf",
        "ram:bdb050:8"
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
      "0057112c",
      "DATA",
      [
        "storage",
        "00bee930",
        null,
        "undefined *"
      ]
    ],
    [
      "00571160",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb050"
      ]
    ]
  ],
  "added": [
    [
      "0057112c",
      "DATA",
      [
        "storage",
        "00c6b4f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00571160",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57aa0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e278.md#insn-0054e2c8) · [`0054e28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e278.md#insn-0054e28c) · [`0054e290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e278.md#insn-0054e290)
- 新版 `00571160`（命令位置の公開資料なし） · `00571124`（命令位置の公開資料なし） · `00571128`（命令位置の公開資料なし）

~~~diff
- 0054e2c8 ["INT_ADD", "register:40f0:8", ["const:54e2c8:8", "const:4:8"]]
- 0054e2c8 ["CALL", null, ["ram:bdb050:8"]]
+ 00571160 ["INT_ADD", "register:40f0:8", ["const:571160:8", "const:4:8"]]
+ 00571160 ["CALL", null, ["ram:c57aa0:8"]]
- 0054e2c8 bytes 62331a94
+ 00571160 bytes 509a1b94
- 0054e28c ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00571124 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0054e28c bytes 08350090
+ 00571124 bytes c83700d0
- 0054e290 ["COPY", "tmp:0:8", ["const:930:8"]]
- 0054e290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054e290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054e290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571128 ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 00571128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054e290 bytes 08c12491
+ 00571128 bytes 08c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05190e98e0e3cd7bc9c8866f17cf7204"></a>

### [`0054e3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e3ac.md) → [`00571244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571244.md) _INIT_28

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00547bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00547/00547bf8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0056aa90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0056a/0056aa90.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 56.52% / 新版 56.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00571270",
      "incomplete_value": false,
      "site": "00571270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e3d8",
      "incomplete_value": false,
      "site": "0054e3d8",
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
            "const:e58:8"
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
      "definition_site": "00571270",
      "incomplete_value": false,
      "site": "00571270",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:918:8"
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
      "definition_site": "0054e3d8",
      "incomplete_value": false,
      "site": "0054e3d8",
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
                "const:e58:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00571274",
      "incomplete_value": false,
      "site": "00571274",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:918:8"
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
      "definition_site": "0054e3dc",
      "incomplete_value": false,
      "site": "0054e3dc",
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
                "const:e58:8"
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
      "00571264",
      "PARAM",
      [
        "storage",
        "00c25e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00571268",
      "PARAM",
      [
        "storage",
        "00547bf8",
        null,
        null
      ]
    ],
    [
      "0057126c",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00571264",
      "PARAM",
      [
        "storage",
        "00ca5918",
        null,
        "undefined8"
      ]
    ],
    [
      "00571268",
      "PARAM",
      [
        "storage",
        "0056aa90",
        null,
        null
      ]
    ],
    [
      "0057126c",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e3ac.md#insn-0054e3e0) · [`0054e3bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e3ac.md#insn-0054e3bc) · [`0054e3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e3ac.md#insn-0054e3c0)
- 新版 `00571278`（命令位置の公開資料なし） · `00571254`（命令位置の公開資料なし） · `00571258`（命令位置の公開資料なし）

~~~diff
- 0054e3e0 ["INT_ADD", "register:40f0:8", ["const:54e3e0:8", "const:4:8"]]
- 0054e3e0 ["CALL", null, ["callee:00c57a30:8"]]
+ 00571278 ["INT_ADD", "register:40f0:8", ["const:571278:8", "const:4:8"]]
+ 00571278 ["CALL", null, ["callee:00c57a30:8"]]
- 0054e3e0 bytes 00331a94
+ 00571278 bytes ee991b94
- 0054e3bc ["COPY", "register:4098:8", ["const:547bf8:8"]]
+ 00571254 ["COPY", "register:4098:8", ["const:56aa90:8"]]
- 0054e3bc bytes f3c1fc10
+ 00571254 bytes f3c1fc10
- 0054e3c0 ["COPY", "register:40a0:8", ["const:be5000:8"]]
+ 00571258 ["COPY", "register:40a0:8", ["const:c62000:8"]]
- 0054e3c0 bytes b43400f0
+ 00571258 bytes 943700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e5a1f33a5f4c82a6f5b55ec07929eb5"></a>

### [`0054e408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e408.md) → [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) FUN_005712a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00550c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00550/00550c88.md) [`00550fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00550/00550fa8.md) [`00551208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551208.md) · 呼出先 10件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00551984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551984.md) [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) [`00574730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574730.md) [`00574810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574810.md)
- 新版 呼出元 3件 [`00573b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573b20.md) [`00573e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573e40.md) [`005740a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005740a0.md) · 呼出先 10件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0057481c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/0057481c.md) [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.21% / 新版 94.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00571328",
      "incomplete_value": true,
      "site": "00571328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e490",
      "incomplete_value": true,
      "site": "0054e490",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d7:8"
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
      "definition_site": "00571390",
      "incomplete_value": true,
      "site": "00571390",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c91:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e4f8",
      "incomplete_value": true,
      "site": "0054e4f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5d0:8"
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
      "definition_site": "0057145c",
      "incomplete_value": true,
      "site": "0057145c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:daa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054e5c4",
      "incomplete_value": true,
      "site": "0054e5c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:75e:8"
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
      "00571318",
      "READ",
      [
        "storage",
        "002939d7",
        null,
        "string"
      ]
    ],
    [
      "00571378",
      "READ",
      [
        "storage",
        "002a25d0",
        null,
        "string"
      ]
    ],
    [
      "0057144c",
      "READ",
      [
        "storage",
        "002a175e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00571318",
      "READ",
      [
        "storage",
        "002a31d0",
        null,
        "string"
      ]
    ],
    [
      "00571378",
      "READ",
      [
        "storage",
        "002b2c91",
        null,
        "string"
      ]
    ],
    [
      "0057144c",
      "READ",
      [
        "storage",
        "002b1daa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054e444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e408.md#insn-0054e444) · [`0054e450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e408.md#insn-0054e450) · [`0054e464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e408.md#insn-0054e464)
- 新版 `005712dc`（命令位置の公開資料なし） · `005712e8`（命令位置の公開資料なし） · `005712fc`（命令位置の公開資料なし）

~~~diff
- 0054e444 ["INT_ADD", "register:40f0:8", ["const:54e444:8", "const:4:8"]]
- 0054e444 ["CALL", null, ["callee:005975c8:8"]]
+ 005712dc ["INT_ADD", "register:40f0:8", ["const:5712dc:8", "const:4:8"]]
+ 005712dc ["CALL", null, ["callee:005975c8:8"]]
- 0054e444 bytes bb980094
+ 005712dc bytes bb980094
- 0054e450 ["INT_ADD", "register:40f0:8", ["const:54e450:8", "const:4:8"]]
- 0054e450 ["CALL", null, ["callee:00596eec:8"]]
+ 005712e8 ["INT_ADD", "register:40f0:8", ["const:5712e8:8", "const:4:8"]]
+ 005712e8 ["CALL", null, ["callee:00596eec:8"]]
- 0054e450 bytes 01970094
+ 005712e8 bytes 01970094
- 0054e464 ["INT_ADD", "register:40f0:8", ["const:54e464:8", "const:4:8"]]
- 0054e464 ["CALL", null, ["callee:00c538e0:8"]]
+ 005712fc ["INT_ADD", "register:40f0:8", ["const:5712fc:8", "const:4:8"]]
+ 005712fc ["CALL", null, ["callee:00c538e0:8"]]
- 0054e464 bytes 8b221a94
+ 005712fc bytes 79891b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd983a71f0af0b637729e89c1f4c4a05"></a>

### [`0054ec1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ec1c.md) → [`00571ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571ab4.md) FUN_00571ab4

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dab8.md) · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00550950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550950.md) · 呼出先 15件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.03% / 新版 95.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00571c6c",
      "incomplete_value": true,
      "site": "00571c6c",
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
      "definition_site": "0054edd4",
      "incomplete_value": true,
      "site": "0054edd4",
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00571c9c",
      "incomplete_value": true,
      "site": "00571c9c",
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
      "definition_site": "0054ee04",
      "incomplete_value": true,
      "site": "0054ee04",
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
      "00571b30",
      "READ",
      [
        "storage",
        "002ac9c6",
        null,
        "string"
      ]
    ],
    [
      "00571b30",
      "READ",
      [
        "storage",
        "002ac9d6",
        null,
        "string"
      ]
    ],
    [
      "00571b34",
      "READ",
      [
        "storage",
        "002b0f40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00571b30",
      "READ",
      [
        "storage",
        "002bda3e",
        null,
        "string"
      ]
    ],
    [
      "00571b30",
      "READ",
      [
        "storage",
        "002bda4e",
        null,
        "string"
      ]
    ],
    [
      "00571b34",
      "READ",
      [
        "storage",
        "002c2530",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054ec54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ec1c.md#insn-0054ec54) · [`0054ec5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ec1c.md#insn-0054ec5c) · [`0054ec88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ec1c.md#insn-0054ec88)
- 新版 `00571aec`（命令位置の公開資料なし） · `00571af4`（命令位置の公開資料なし） · `00571b20`（命令位置の公開資料なし）

~~~diff
- 0054ec54 ["INT_ADD", "register:40f0:8", ["const:54ec54:8", "const:4:8"]]
- 0054ec54 ["CALL", null, ["callee:00588e2c:8"]]
+ 00571aec ["INT_ADD", "register:40f0:8", ["const:571aec:8", "const:4:8"]]
+ 00571aec ["CALL", null, ["callee:00588e2c:8"]]
- 0054ec54 bytes d05c0094
+ 00571aec bytes d05c0094
- 0054ec5c ["INT_ADD", "register:40f0:8", ["const:54ec5c:8", "const:4:8"]]
- 0054ec5c ["CALL", null, ["callee:0058911c:8"]]
+ 00571af4 ["INT_ADD", "register:40f0:8", ["const:571af4:8", "const:4:8"]]
+ 00571af4 ["CALL", null, ["callee:0058911c:8"]]
- 0054ec5c bytes 8a5d0094
+ 00571af4 bytes 8a5d0094
- 0054ec88 ["INT_ADD", "register:40f0:8", ["const:54ec88:8", "const:4:8"]]
- 0054ec88 ["CALL", null, ["callee:00c57a90:8"]]
+ 00571b20 ["INT_ADD", "register:40f0:8", ["const:571b20:8", "const:4:8"]]
+ 00571b20 ["CALL", null, ["callee:00c57a90:8"]]
- 0054ec88 bytes ee301a94
+ 00571b20 bytes dc971b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5af89bad9459ecddbcd11122991d4b1b"></a>

### [`0054ef40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ef40.md) → [`00571dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571dd8.md) FUN_00571dd8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dabc.md) · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00550954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550954.md) · 呼出先 15件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00571e54",
      "incomplete_value": true,
      "site": "00571e60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:320:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054efbc",
      "incomplete_value": true,
      "site": "0054efc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00571e50",
      "incomplete_value": true,
      "site": "00571e64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054efb8",
      "incomplete_value": true,
      "site": "0054efcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7ca:8"
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
      "definition_site": "00571e50",
      "incomplete_value": true,
      "site": "00571e64",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0054efb8",
      "incomplete_value": true,
      "site": "0054efcc",
      "value": [
        "LOAD",
        "16",
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
      "00571e50",
      "READ",
      [
        "storage",
        "002ab7ca",
        null,
        "string"
      ]
    ],
    [
      "00571e50",
      "READ",
      [
        "storage",
        "002ab7da",
        null,
        "string"
      ]
    ],
    [
      "00571e54",
      "READ",
      [
        "storage",
        "002b0d20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00571e50",
      "READ",
      [
        "storage",
        "002bc6ed",
        null,
        "string"
      ]
    ],
    [
      "00571e50",
      "READ",
      [
        "storage",
        "002bc6fd",
        null,
        "string"
      ]
    ],
    [
      "00571e54",
      "READ",
      [
        "storage",
        "002c2320",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054ef74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ef40.md#insn-0054ef74) · [`0054ef7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ef40.md#insn-0054ef7c) · [`0054efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ef40.md#insn-0054efa8)
- 新版 `00571e0c`（命令位置の公開資料なし） · `00571e14`（命令位置の公開資料なし） · `00571e40`（命令位置の公開資料なし）

~~~diff
- 0054ef74 ["INT_ADD", "register:40f0:8", ["const:54ef74:8", "const:4:8"]]
- 0054ef74 ["CALL", null, ["callee:00588e2c:8"]]
+ 00571e0c ["INT_ADD", "register:40f0:8", ["const:571e0c:8", "const:4:8"]]
+ 00571e0c ["CALL", null, ["callee:00588e2c:8"]]
- 0054ef74 bytes 085c0094
+ 00571e0c bytes 085c0094
- 0054ef7c ["INT_ADD", "register:40f0:8", ["const:54ef7c:8", "const:4:8"]]
- 0054ef7c ["CALL", null, ["callee:0058911c:8"]]
+ 00571e14 ["INT_ADD", "register:40f0:8", ["const:571e14:8", "const:4:8"]]
+ 00571e14 ["CALL", null, ["callee:0058911c:8"]]
- 0054ef7c bytes c25c0094
+ 00571e14 bytes c25c0094
- 0054efa8 ["INT_ADD", "register:40f0:8", ["const:54efa8:8", "const:4:8"]]
- 0054efa8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00571e40 ["INT_ADD", "register:40f0:8", ["const:571e40:8", "const:4:8"]]
+ 00571e40 ["CALL", null, ["callee:00c57a90:8"]]
- 0054efa8 bytes 26301a94
+ 00571e40 bytes 14971b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd9848ccc0ec14417590a1625096b6db"></a>

### [`0054f220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f220.md) → [`005720b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005720b8.md) FUN_005720b8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052dac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dac0.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00550958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550958.md) · 呼出先 11件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057211c",
      "incomplete_value": true,
      "site": "0057212c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054f284",
      "incomplete_value": true,
      "site": "0054f294",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:90f:8"
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
      "definition_site": "00572130",
      "incomplete_value": true,
      "site": "00572130",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0054f298",
      "incomplete_value": true,
      "site": "0054f298",
      "value": [
        "LOAD",
        "8",
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
      "005720fc",
      "READ",
      [
        "storage",
        "002ae9bf",
        null,
        "string"
      ]
    ],
    [
      "0057211c",
      "READ",
      [
        "storage",
        "0029290f",
        null,
        "string"
      ]
    ],
    [
      "00572124",
      "READ",
      [
        "storage",
        "0029291d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005720fc",
      "READ",
      [
        "storage",
        "002bfea3",
        null,
        "string"
      ]
    ],
    [
      "0057211c",
      "READ",
      [
        "storage",
        "002a201f",
        null,
        "string"
      ]
    ],
    [
      "00572124",
      "READ",
      [
        "storage",
        "002a202d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054f24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f220.md#insn-0054f24c) · [`0054f254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f220.md#insn-0054f254) · [`0054f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f220.md#insn-0054f258)
- 新版 `005720e4`（命令位置の公開資料なし） · `005720ec`（命令位置の公開資料なし） · `005720f0`（命令位置の公開資料なし）

~~~diff
- 0054f24c ["INT_ADD", "register:40f0:8", ["const:54f24c:8", "const:4:8"]]
- 0054f24c ["CALL", null, ["callee:00588e2c:8"]]
+ 005720e4 ["INT_ADD", "register:40f0:8", ["const:5720e4:8", "const:4:8"]]
+ 005720e4 ["CALL", null, ["callee:00588e2c:8"]]
- 0054f24c bytes 525b0094
+ 005720e4 bytes 525b0094
- 0054f254 ["INT_ADD", "register:40f0:8", ["const:54f254:8", "const:4:8"]]
- 0054f254 ["CALL", null, ["callee:0058911c:8"]]
+ 005720ec ["INT_ADD", "register:40f0:8", ["const:5720ec:8", "const:4:8"]]
+ 005720ec ["CALL", null, ["callee:0058911c:8"]]
- 0054f254 bytes 0c5c0094
+ 005720ec bytes 0c5c0094
- 0054f258 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 005720f0 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0054f258 bytes e9eafff0
+ 005720f0 bytes 69eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7a62695827227acf10015410cae6836"></a>

### [`0054f3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f3d4.md) → [`0057226c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/0057226c.md) FUN_0057226c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dac4.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0055095c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055095c.md) · 呼出先 11件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005722c4",
      "incomplete_value": true,
      "site": "005722c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054f42c",
      "incomplete_value": true,
      "site": "0054f42c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9bf:8"
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
      "definition_site": "005722d0",
      "incomplete_value": true,
      "site": "005722e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054f438",
      "incomplete_value": true,
      "site": "0054f448",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:90f:8"
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
      "definition_site": "005722e4",
      "incomplete_value": true,
      "site": "005722e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0054f44c",
      "incomplete_value": true,
      "site": "0054f44c",
      "value": [
        "LOAD",
        "8",
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
      "005722b0",
      "READ",
      [
        "storage",
        "002ae9bf",
        null,
        "string"
      ]
    ],
    [
      "005722d0",
      "READ",
      [
        "storage",
        "0029290f",
        null,
        "string"
      ]
    ],
    [
      "005722d8",
      "READ",
      [
        "storage",
        "0029291d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005722b0",
      "READ",
      [
        "storage",
        "002bfea3",
        null,
        "string"
      ]
    ],
    [
      "005722d0",
      "READ",
      [
        "storage",
        "002a201f",
        null,
        "string"
      ]
    ],
    [
      "005722d8",
      "READ",
      [
        "storage",
        "002a202d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054f400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f3d4.md#insn-0054f400) · [`0054f408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f3d4.md#insn-0054f408) · [`0054f40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f3d4.md#insn-0054f40c)
- 新版 `00572298`（命令位置の公開資料なし） · `005722a0`（命令位置の公開資料なし） · `005722a4`（命令位置の公開資料なし）

~~~diff
- 0054f400 ["INT_ADD", "register:40f0:8", ["const:54f400:8", "const:4:8"]]
- 0054f400 ["CALL", null, ["callee:00588e2c:8"]]
+ 00572298 ["INT_ADD", "register:40f0:8", ["const:572298:8", "const:4:8"]]
+ 00572298 ["CALL", null, ["callee:00588e2c:8"]]
- 0054f400 bytes e55a0094
+ 00572298 bytes e55a0094
- 0054f408 ["INT_ADD", "register:40f0:8", ["const:54f408:8", "const:4:8"]]
- 0054f408 ["CALL", null, ["callee:0058911c:8"]]
+ 005722a0 ["INT_ADD", "register:40f0:8", ["const:5722a0:8", "const:4:8"]]
+ 005722a0 ["CALL", null, ["callee:0058911c:8"]]
- 0054f408 bytes 9f5b0094
+ 005722a0 bytes 9f5b0094
- 0054f40c ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 005722a4 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0054f40c bytes e9eafff0
+ 005722a4 bytes 69eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-128277488e94af0fc15be92315927c18"></a>

### [`0054f588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f588.md) → [`00572420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572420.md) FUN_00572420

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dac8.md) · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00551eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551eb0.md)
- 新版 呼出元 1件 [`00550960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550960.md) · 呼出先 19件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00574d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574d48.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 92.44% / 新版 92.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057249c",
      "incomplete_value": true,
      "site": "005724ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054f604",
      "incomplete_value": true,
      "site": "0054f614",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a8:8"
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
      "definition_site": "005724b0",
      "incomplete_value": true,
      "site": "005724b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0054f618",
      "incomplete_value": true,
      "site": "0054f618",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005724a4",
      "incomplete_value": true,
      "site": "005724b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0054f60c",
      "incomplete_value": true,
      "site": "0054f61c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057249c",
      "READ",
      [
        "storage",
        "002a83a8",
        null,
        "string"
      ]
    ],
    [
      "005724a0",
      "READ",
      [
        "storage",
        "002a83b7",
        null,
        "string"
      ]
    ],
    [
      "005724a4",
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
      "0057249c",
      "READ",
      [
        "storage",
        "002b904a",
        null,
        "string"
      ]
    ],
    [
      "005724a0",
      "READ",
      [
        "storage",
        "002b9059",
        null,
        "string"
      ]
    ],
    [
      "005724a4",
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

- 旧版 [`0054f680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f588.md#insn-0054f680) · [`0054f6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f588.md#insn-0054f6fc) · [`0054f5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f588.md#insn-0054f5bc)
- 新版 `00572518`（命令位置の公開資料なし） · `00572594`（命令位置の公開資料なし） · `00572454`（命令位置の公開資料なし）

~~~diff
- 0054f680 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:2f8:8"]]
- 0054f680 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
+ 00572518 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:db8:8"]]
+ 00572518 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 0054f680 bytes 54f902b9
+ 00572518 bytes 54b90db9
- 0054f6fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 0054f6fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00572594 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
+ 00572594 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0054f6fc bytes 097101f9
+ 00572594 bytes 09d106f9
- 0054f5bc ["INT_ADD", "register:40f0:8", ["const:54f5bc:8", "const:4:8"]]
- 0054f5bc ["CALL", null, ["callee:00588e2c:8"]]
+ 00572454 ["INT_ADD", "register:40f0:8", ["const:572454:8", "const:4:8"]]
+ 00572454 ["CALL", null, ["callee:00588e2c:8"]]
- 0054f5bc bytes 765a0094
+ 00572454 bytes 765a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cec6c1e4dde5173e8d34d21ede047e0"></a>

### [`0054f9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f9dc.md) → [`00572874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572874.md) FUN_00572874

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052dacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dacc.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00550964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550964.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005728c0",
      "incomplete_value": true,
      "site": "005728c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c9c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054fa28",
      "incomplete_value": true,
      "site": "0054fa28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc3:8"
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
      "005728b0",
      "READ",
      [
        "storage",
        "00299dc3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005728b0",
      "READ",
      [
        "storage",
        "002a9c9c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054f9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f9dc.md#insn-0054f9fc) · [`0054fa04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f9dc.md#insn-0054fa04) · [`0054fa0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054f9dc.md#insn-0054fa0c)
- 新版 `00572894`（命令位置の公開資料なし） · `0057289c`（命令位置の公開資料なし） · `005728a4`（命令位置の公開資料なし）

~~~diff
- 0054f9fc ["INT_ADD", "register:40f0:8", ["const:54f9fc:8", "const:4:8"]]
- 0054f9fc ["CALL", null, ["callee:00588e2c:8"]]
+ 00572894 ["INT_ADD", "register:40f0:8", ["const:572894:8", "const:4:8"]]
+ 00572894 ["CALL", null, ["callee:00588e2c:8"]]
- 0054f9fc bytes 66590094
+ 00572894 bytes 66590094
- 0054fa04 ["INT_ADD", "register:40f0:8", ["const:54fa04:8", "const:4:8"]]
- 0054fa04 ["CALL", null, ["callee:0058911c:8"]]
+ 0057289c ["INT_ADD", "register:40f0:8", ["const:57289c:8", "const:4:8"]]
+ 0057289c ["CALL", null, ["callee:0058911c:8"]]
- 0054fa04 bytes 205a0094
+ 0057289c bytes 205a0094
- 0054fa0c ["COPY", "register:4048:8", ["const:299000:8"]]
+ 005728a4 ["COPY", "register:4048:8", ["const:2a9000:8"]]
- 0054fa0c bytes 49eaffd0
+ 005728a4 bytes a9e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f4868467a7822732ae89a097c5b91c5"></a>

### [`0054fb0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fb0c.md) → [`005729a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/005729a4.md) FUN_005729a4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052dad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad0.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00550968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550968.md) · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005729e0",
      "incomplete_value": true,
      "site": "005729f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ead:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054fb48",
      "incomplete_value": true,
      "site": "0054fb60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9c9:8"
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
      "definition_site": "005729fc",
      "incomplete_value": true,
      "site": "00572a08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c54:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054fb64",
      "incomplete_value": true,
      "site": "0054fb70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:57a:8"
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
      "definition_site": "00572a0c",
      "incomplete_value": true,
      "site": "00572a0c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0054fb74",
      "incomplete_value": true,
      "site": "0054fb74",
      "value": [
        "LOAD",
        "8",
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
      "005729e0",
      "READ",
      [
        "storage",
        "002ae9c9",
        null,
        "string"
      ]
    ],
    [
      "005729fc",
      "READ",
      [
        "storage",
        "002a357a",
        null,
        "string"
      ]
    ],
    [
      "00572a00",
      "READ",
      [
        "storage",
        "002a3587",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005729e0",
      "READ",
      [
        "storage",
        "002bfead",
        null,
        "string"
      ]
    ],
    [
      "005729fc",
      "READ",
      [
        "storage",
        "002b3c54",
        null,
        "string"
      ]
    ],
    [
      "00572a00",
      "READ",
      [
        "storage",
        "002b3c61",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054fb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fb0c.md#insn-0054fb30) · [`0054fb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fb0c.md#insn-0054fb38) · [`0054fb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fb0c.md#insn-0054fb40)
- 新版 `005729c8`（命令位置の公開資料なし） · `005729d0`（命令位置の公開資料なし） · `005729d8`（命令位置の公開資料なし）

~~~diff
- 0054fb30 ["INT_ADD", "register:40f0:8", ["const:54fb30:8", "const:4:8"]]
- 0054fb30 ["CALL", null, ["callee:00588e2c:8"]]
+ 005729c8 ["INT_ADD", "register:40f0:8", ["const:5729c8:8", "const:4:8"]]
+ 005729c8 ["CALL", null, ["callee:00588e2c:8"]]
- 0054fb30 bytes 19590094
+ 005729c8 bytes 19590094
- 0054fb38 ["INT_ADD", "register:40f0:8", ["const:54fb38:8", "const:4:8"]]
- 0054fb38 ["CALL", null, ["callee:0058911c:8"]]
+ 005729d0 ["INT_ADD", "register:40f0:8", ["const:5729d0:8", "const:4:8"]]
+ 005729d0 ["CALL", null, ["callee:0058911c:8"]]
- 0054fb38 bytes d3590094
+ 005729d0 bytes d3590094
- 0054fb40 ["COPY", "register:4048:8", ["const:2ae000:8"]]
+ 005729d8 ["COPY", "register:4048:8", ["const:2bf000:8"]]
- 0054fb40 bytes e9eafff0
+ 005729d8 bytes 69eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f72b09333a57e942f836ae9c81d2676"></a>

### [`0054fcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fcc8.md) → [`00572b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572b60.md) FUN_00572b60

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052dad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad4.md) · 呼出先 2件 [`00552018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552018.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0055096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055096c.md) · 呼出先 2件 [`00574eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574eb0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00572bc8",
      "incomplete_value": false,
      "site": "00572bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054fd30",
      "incomplete_value": false,
      "site": "0054fd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "00572bc8",
      "PARAM",
      [
        "storage",
        "00c262b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00572bc8",
      "PARAM",
      [
        "storage",
        "00ca5d70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054fd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fcc8.md#insn-0054fd3c) · [`0054fd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fcc8.md#insn-0054fd00) · [`0054fd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fcc8.md#insn-0054fd28)
- 新版 `00572bd4`（命令位置の公開資料なし） · `00572b98`（命令位置の公開資料なし） · `00572bc0`（命令位置の公開資料なし）

~~~diff
- 0054fd3c ["INT_ADD", "register:40f0:8", ["const:54fd3c:8", "const:4:8"]]
- 0054fd3c ["CALL", null, ["callee:00574eb0:8"]]
+ 00572bd4 ["INT_ADD", "register:40f0:8", ["const:572bd4:8", "const:4:8"]]
+ 00572bd4 ["CALL", null, ["callee:00574eb0:8"]]
- 0054fd3c bytes b7080094
+ 00572bd4 bytes b7080094
- 0054fd00 ["COPY", "register:0:8", ["register:4048:8"]]
- 0054fd00 ["INT_ADD", "register:40f0:8", ["const:54fd00:8", "const:4:8"]]
- 0054fd00 ["CALLIND", null, ["register:0:8"]]
+ 00572b98 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00572b98 ["INT_ADD", "register:40f0:8", ["const:572b98:8", "const:4:8"]]
+ 00572b98 ["CALLIND", null, ["register:0:8"]]
- 0054fd00 bytes 20013fd6
+ 00572b98 bytes 20013fd6
- 0054fd28 ["COPY", "register:0:8", ["register:4040:8"]]
- 0054fd28 ["INT_ADD", "register:40f0:8", ["const:54fd28:8", "const:4:8"]]
- 0054fd28 ["CALLIND", null, ["register:0:8"]]
+ 00572bc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00572bc0 ["INT_ADD", "register:40f0:8", ["const:572bc0:8", "const:4:8"]]
+ 00572bc0 ["CALLIND", null, ["register:0:8"]]
- 0054fd28 bytes 00013fd6
+ 00572bc0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9632992da8f09e3ec81454d6b78774c7"></a>

### [`0054fd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fd90.md) → [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) Java_jp_co_ponos_battlecats_MyActivity_onIapList

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0054ea94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054ea94.md) [`005515a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/005515a0.md) [`0055224c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/0055224c.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0057192c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/0057192c.md) [`00574438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574438.md) [`005750e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005750e4.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.32% / 新版 95.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00572cfc",
      "incomplete_value": false,
      "site": "00572cfc",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054fe64",
      "incomplete_value": false,
      "site": "0054fe64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:b50:8"
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
      "definition_site": "00572da8",
      "incomplete_value": true,
      "site": "00572dac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0054ff10",
      "incomplete_value": true,
      "site": "0054ff14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:380:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572e38",
      "incomplete_value": true,
      "site": "00572e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054ffa0",
      "incomplete_value": true,
      "site": "0054ffac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00572c64",
      "READ",
      [
        "storage",
        "00c262e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00572cfc",
      "DATA",
      [
        "storage",
        "00beeb50",
        null,
        "pointer"
      ]
    ],
    [
      "00572da8",
      "READ",
      [
        "storage",
        "002b1380",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00572c64",
      "READ",
      [
        "storage",
        "00ca5da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00572cfc",
      "DATA",
      [
        "storage",
        "00c6b710",
        null,
        "pointer"
      ]
    ],
    [
      "00572da8",
      "READ",
      [
        "storage",
        "002c29c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054fdc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fd90.md#insn-0054fdc4) · [`0054fdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fd90.md#insn-0054fdc8) · [`0054fdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fd90.md#insn-0054fdd4)
- 新版 `00572c5c`（命令位置の公開資料なし） · `00572c60`（命令位置の公開資料なし） · `00572c6c`（命令位置の公開資料なし）

~~~diff
- 0054fdc4 ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 00572c5c ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0054fdc4 bytes a83600f0
+ 00572c5c bytes 883900f0
- 0054fdc8 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 0054fdc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054fdc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054fdc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00572c60 ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 00572c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00572c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00572c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054fdc8 bytes 08a10b91
+ 00572c60 bytes 08a13691
- 0054fdd4 ["COPY", "register:40d0:8", ["const:c26000:8"]]
+ 00572c6c ["COPY", "register:40d0:8", ["const:ca5000:8"]]
- 0054fdd4 bytes ba3600f0
+ 00572c6c bytes 9a3900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58fe93b1238ef67a1a2388a5c514a22a"></a>

### [`00550fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00550/00550fa8.md) → [`00573e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573e40.md) Java_jp_co_ponos_battlecats_MyActivity_onIapPurchases

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0054e408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e408.md) [`0056774c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056774c.md) [`00567848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567848.md) [`00567900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567900.md) [`005679e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) [`0058a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a5e4.md) [`0058a6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a6e0.md) [`0058a798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a798.md) [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00573f7c",
      "incomplete_value": true,
      "site": "00573f7c",
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
      "definition_site": "005510e4",
      "incomplete_value": true,
      "site": "005510e4",
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005510e4"
      ],
      [
        "FALL_THROUGH",
        "00573f7c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00573f7c",
      "incomplete_value": true,
      "site": "00573f80",
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
      "definition_site": "005510e4",
      "incomplete_value": true,
      "site": "005510e8",
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
      "00573f78",
      "READ",
      [
        "storage",
        "00c262d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00573f78",
      "READ",
      [
        "storage",
        "00ca5d90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00550fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00550/00550fa8.md#insn-00550fe8) · [`00550ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00550/00550fa8.md#insn-00550ff4) · [`00551004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00550/00550fa8.md#insn-00551004)
- 新版 `00573e80`（命令位置の公開資料なし） · `00573e8c`（命令位置の公開資料なし） · `00573e9c`（命令位置の公開資料なし）

~~~diff
- 00550fe8 ["INT_ADD", "register:40f0:8", ["const:550fe8:8", "const:4:8"]]
- 00550fe8 ["CALL", null, ["callee:0058a5e4:8"]]
+ 00573e80 ["INT_ADD", "register:40f0:8", ["const:573e80:8", "const:4:8"]]
+ 00573e80 ["CALL", null, ["callee:0058a5e4:8"]]
- 00550fe8 bytes d9590094
+ 00573e80 bytes d9590094
- 00550ff4 ["INT_ADD", "register:40f0:8", ["const:550ff4:8", "const:4:8"]]
- 00550ff4 ["CALL", null, ["callee:0058a5e4:8"]]
+ 00573e8c ["INT_ADD", "register:40f0:8", ["const:573e8c:8", "const:4:8"]]
+ 00573e8c ["CALL", null, ["callee:0058a5e4:8"]]
- 00550ff4 bytes d6590094
+ 00573e8c bytes d6590094
- 00551004 ["INT_ADD", "register:40f0:8", ["const:551004:8", "const:4:8"]]
- 00551004 ["CALL", null, ["callee:0058a798:8"]]
+ 00573e9c ["INT_ADD", "register:40f0:8", ["const:573e9c:8", "const:4:8"]]
+ 00573e9c ["CALL", null, ["callee:0058a798:8"]]
- 00551004 bytes 3f5a0094
+ 00573e9c bytes 3f5a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4484260c409b9e3167c96d3f079ca73"></a>

### [`00551208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551208.md) → [`005740a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005740a0.md) Java_jp_co_ponos_battlecats_MyActivity_onIapPurchases2

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0054e408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e408.md) [`0056774c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/0056774c.md) [`00567848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567848.md) [`00567900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567900.md) [`005679e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/005679e4.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) [`0058a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a5e4.md) [`0058a6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a6e0.md) [`0058a798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a798.md) [`0058a87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058a87c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.74% / 新版 98.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00574238",
      "incomplete_value": true,
      "site": "00574238",
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
      "definition_site": "005513a0",
      "incomplete_value": true,
      "site": "005513a0",
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005513a0"
      ],
      [
        "FALL_THROUGH",
        "00574238"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00574238",
      "incomplete_value": true,
      "site": "0057423c",
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
      "definition_site": "005513a0",
      "incomplete_value": true,
      "site": "005513a4",
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
    "ordinal": 17,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00574234",
      "READ",
      [
        "storage",
        "00c262d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00574234",
      "READ",
      [
        "storage",
        "00ca5d90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551208.md#insn-00551250) · [`0055125c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551208.md#insn-0055125c) · [`00551274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551208.md#insn-00551274)
- 新版 `005740e8`（命令位置の公開資料なし） · `005740f4`（命令位置の公開資料なし） · `0057410c`（命令位置の公開資料なし）

~~~diff
- 00551250 ["INT_ADD", "register:40f0:8", ["const:551250:8", "const:4:8"]]
- 00551250 ["CALL", null, ["callee:0058a5e4:8"]]
+ 005740e8 ["INT_ADD", "register:40f0:8", ["const:5740e8:8", "const:4:8"]]
+ 005740e8 ["CALL", null, ["callee:0058a5e4:8"]]
- 00551250 bytes 3f590094
+ 005740e8 bytes 3f590094
- 0055125c ["INT_ADD", "register:40f0:8", ["const:55125c:8", "const:4:8"]]
- 0055125c ["CALL", null, ["callee:0058a5e4:8"]]
+ 005740f4 ["INT_ADD", "register:40f0:8", ["const:5740f4:8", "const:4:8"]]
+ 005740f4 ["CALL", null, ["callee:0058a5e4:8"]]
- 0055125c bytes 3c590094
+ 005740f4 bytes 3c590094
- 00551274 ["COPY", "register:0:8", ["register:4040:8"]]
- 00551274 ["INT_ADD", "register:40f0:8", ["const:551274:8", "const:4:8"]]
- 00551274 ["CALLIND", null, ["register:0:8"]]
+ 0057410c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057410c ["INT_ADD", "register:40f0:8", ["const:57410c:8", "const:4:8"]]
+ 0057410c ["CALLIND", null, ["register:0:8"]]
- 00551274 bytes 00013fd6
+ 0057410c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06c0e478c476b6c3b3091e0be4d45e2e"></a>

### [`005515a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/005515a0.md) → [`00574438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574438.md) FUN_00574438

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0054fd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054f/0054fd90.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00572c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00572/00572c28.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00574468",
      "incomplete_value": true,
      "site": "00574468",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005515d0",
      "incomplete_value": true,
      "site": "005515d0",
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
            "const:a20:8"
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
      "00574468",
      "DATA",
      [
        "storage",
        "00beea20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574468",
      "DATA",
      [
        "storage",
        "00c6b5e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005515bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/005515a0.md#insn-005515bc) · [`005515c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/005515a0.md#insn-005515c0) · [`00551608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/005515a0.md#insn-00551608)
- 新版 `00574454`（命令位置の公開資料なし） · `00574458`（命令位置の公開資料なし） · `005744a0`（命令位置の公開資料なし）

~~~diff
- 005515bc ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00574454 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 005515bc bytes e83400b0
+ 00574454 bytes a83700f0
- 005515c0 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 005515c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005515c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005515c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574458 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 00574458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005515c0 bytes 08812891
+ 00574458 bytes 08811791
- 00551608 ["INT_ADD", "register:40f0:8", ["const:551608:8", "const:4:8"]]
- 00551608 ["CALL", null, ["callee:0043bae0:8"]]
+ 005744a0 ["INT_ADD", "register:40f0:8", ["const:5744a0:8", "const:4:8"]]
+ 005744a0 ["CALL", null, ["callee:0043bae0:8"]]
- 00551608 bytes 761efb97
+ 005744a0 bytes 901dfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb9819339d30d737e5e306f912cdffae"></a>

### [`00551850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551850.md) → [`005746e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005746e8.md) FUN_005746e8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0055154c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/0055154c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005743e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005743e4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574700",
      "incomplete_value": false,
      "site": "00574704",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551868",
      "incomplete_value": false,
      "site": "0055186c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "00574704",
      "DATA",
      [
        "storage",
        "00beea20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574704",
      "DATA",
      [
        "storage",
        "00c6b5e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551850.md#insn-00551864) · [`00551868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551850.md#insn-00551868) · [`005518a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551850.md#insn-005518a4)
- 新版 `005746fc`（命令位置の公開資料なし） · `00574700`（命令位置の公開資料なし） · `0057473c`（命令位置の公開資料なし）

~~~diff
- 00551864 ["COPY", "register:4048:8", ["const:bee000:8"]]
+ 005746fc ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00551864 bytes e93400b0
+ 005746fc bytes a93700f0
- 00551868 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00551868 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00551868 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00551868 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00574700 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 00574700 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00574700 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00574700 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00551868 bytes 29812891
+ 00574700 bytes 29811791
- 005518a4 ["INT_ADD", "register:40f0:8", ["const:5518a4:8", "const:4:8"]]
- 005518a4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0057473c ["INT_ADD", "register:40f0:8", ["const:57473c:8", "const:4:8"]]
+ 0057473c ["CALL", null, ["callee:00c57ab0:8"]]
- 005518a4 bytes ef251a94
+ 0057473c bytes dd8c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53bed18b0bc24300e63d7130dfa8a695"></a>

### [`00551984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551984.md) → [`0057481c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/0057481c.md) FUN_0057481c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0054e408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e408.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 1件 [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574840",
      "incomplete_value": false,
      "site": "00574840",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005519a8",
      "incomplete_value": false,
      "site": "005519a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "00574840",
      "DATA",
      [
        "storage",
        "00beead8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574840",
      "DATA",
      [
        "storage",
        "00c6b698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055199c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551984.md#insn-0055199c) · [`005519a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551984.md#insn-005519a0) · [`005519a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551984.md#insn-005519a4)
- 新版 `00574834`（命令位置の公開資料なし） · `00574838`（命令位置の公開資料なし）

~~~diff
- 0055199c ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00574834 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055199c bytes e83400b0
+ 00574834 bytes a83700f0
- 005519a0 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 005519a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005519a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005519a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574838 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 00574838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005519a0 bytes 08612b91
+ 00574838 bytes 08611a91
- 005519a4 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 005519a4 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-422488b8241368e0272064d46685f5a4"></a>

### [`00551bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551bf4.md) → [`00574a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574a8c.md) FUN_00574a8c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00551930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551930.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005747c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/005747c8.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574aa4",
      "incomplete_value": false,
      "site": "00574aa8",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551c0c",
      "incomplete_value": false,
      "site": "00551c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "00574aa8",
      "DATA",
      [
        "storage",
        "00beead8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574aa8",
      "DATA",
      [
        "storage",
        "00c6b698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551bf4.md#insn-00551c08) · [`00551c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551bf4.md#insn-00551c0c) · [`00551c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551bf4.md#insn-00551c20)
- 新版 `00574aa0`（命令位置の公開資料なし） · `00574aa4`（命令位置の公開資料なし） · `00574ab8`（命令位置の公開資料なし）

~~~diff
- 00551c08 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00574aa0 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00551c08 bytes e83400b0
+ 00574aa0 bytes a83700f0
- 00551c0c ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 00551c0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00551c0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00551c0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574aa4 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 00574aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00551c0c bytes 08612b91
+ 00574aa4 bytes 08611a91
- 00551c20 ["INT_ADD", "register:40f0:8", ["const:551c20:8", "const:4:8"]]
- 00551c20 ["CALL", null, ["callee:00c538e0:8"]]
+ 00574ab8 ["INT_ADD", "register:40f0:8", ["const:574ab8:8", "const:4:8"]]
+ 00574ab8 ["CALL", null, ["callee:00c538e0:8"]]
- 00551c20 bytes 9c141a94
+ 00574ab8 bytes 8a7b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8970e64bb0d325beca8111d0924657d1"></a>

### [`00551ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551ccc.md) → [`00574b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574b64.md) FUN_00574b64

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00550/00550c88.md) · 呼出先 2件 [`00574784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574784.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00573b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00573/00573b20.md) · 呼出先 2件 [`0059761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574b8c",
      "incomplete_value": false,
      "site": "00574b94",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551cf4",
      "incomplete_value": false,
      "site": "00551cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "definition_site": "00574ba0",
      "incomplete_value": false,
      "site": "00574ba0",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00551d08",
      "incomplete_value": false,
      "site": "00551d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "00574b94",
      "DATA",
      [
        "storage",
        "00beea88",
        null,
        "undefined *"
      ]
    ],
    [
      "00574ba0",
      "DATA",
      [
        "storage",
        "00beead8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574b94",
      "DATA",
      [
        "storage",
        "00c6b648",
        null,
        "undefined *"
      ]
    ],
    [
      "00574ba0",
      "DATA",
      [
        "storage",
        "00c6b698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00551cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551ccc.md#insn-00551cec) · [`00551cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551ccc.md#insn-00551cf0) · [`00551cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551ccc.md#insn-00551cf4)
- 新版 `00574b84`（命令位置の公開資料なし） · `00574b88`（命令位置の公開資料なし） · `00574b8c`（命令位置の公開資料なし）

~~~diff
- 00551cec ["INT_ADD", "register:40f0:8", ["const:551cec:8", "const:4:8"]]
- 00551cec ["CALL", null, ["callee:00c57a90:8"]]
+ 00574b84 ["INT_ADD", "register:40f0:8", ["const:574b84:8", "const:4:8"]]
+ 00574b84 ["CALL", null, ["callee:00c57a90:8"]]
- 00551cec bytes d5241a94
+ 00574b84 bytes c38b1b94
- 00551cf0 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00574b88 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00551cf0 bytes e83400b0
+ 00574b88 bytes a83700f0
- 00551cf4 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00551cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00551cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00551cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574b8c ["COPY", "tmp:0:8", ["const:648:8"]]
+ 00574b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00551cf4 bytes 08212a91
+ 00574b8c bytes 08211991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff07bec910d4df3caa6ac0ef5c7a7a65"></a>

### [`0055246c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/0055246c.md) → [`00575304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575304.md) FUN_00575304

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00552310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552310.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005751a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005751a8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00575314",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0055247c",
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
      "definition_site": "00575310",
      "incomplete_value": false,
      "site": "00575314",
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
      "definition_site": "00552478",
      "incomplete_value": false,
      "site": "0055247c",
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
      "00575310",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00575314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00575310",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00575314",
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

- 旧版 [`0055247c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/0055246c.md#insn-0055247c) · [`00552474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/0055246c.md#insn-00552474) · [`00552478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/0055246c.md#insn-00552478)
- 新版 `00575314`（命令位置の公開資料なし） · `0057530c`（命令位置の公開資料なし） · `00575310`（命令位置の公開資料なし）

~~~diff
- 0055247c ["INT_ADD", "register:40f0:8", ["const:55247c:8", "const:4:8"]]
- 0055247c ["CALL", null, ["ram:418c38:8"]]
+ 00575314 ["INT_ADD", "register:40f0:8", ["const:575314:8", "const:4:8"]]
+ 00575314 ["CALL", null, ["ram:43b738:8"]]
- 0055247c bytes ef19fb97
+ 00575314 bytes 0919fb97
- 00552474 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0057530c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00552474 bytes a0eaffb0
+ 0057530c bytes 00eaffd0
- 00552478 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00552478 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00552478 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00552478 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00575310 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00575310 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00575310 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00575310 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00552478 bytes 00740e91
+ 00575310 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b9a935a9304d12d08cc35e84ad12601"></a>

### [`00552480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552480.md) → [`00575318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575318.md) _INIT_29

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0054e8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e8f0.md) [`0054e920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e920.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00571788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/00571788.md) [`005717b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005717b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 45.83% / 新版 45.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00575340",
      "incomplete_value": false,
      "site": "00575340",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:d70:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005524a8",
      "incomplete_value": false,
      "site": "005524a8",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:2b0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "0057535c",
      "incomplete_value": false,
      "site": "0057535c",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:da0:8"
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
      "definition_site": "005524c4",
      "incomplete_value": false,
      "site": "005524c4",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:2e0:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00575360",
      "incomplete_value": false,
      "site": "00575360",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:da0:8"
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
      "definition_site": "005524c8",
      "incomplete_value": false,
      "site": "005524c8",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:2e0:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00575330",
      "PARAM",
      [
        "storage",
        "00c262b0",
        null,
        null
      ]
    ],
    [
      "00575338",
      "PARAM",
      [
        "storage",
        "0054e8f0",
        null,
        null
      ]
    ],
    [
      "0057533c",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00575330",
      "PARAM",
      [
        "storage",
        "00ca5d70",
        null,
        null
      ]
    ],
    [
      "00575338",
      "PARAM",
      [
        "storage",
        "00571788",
        null,
        null
      ]
    ],
    [
      "0057533c",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005524ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552480.md#insn-005524ac) · [`0055248c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552480.md#insn-0055248c) · [`00552490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552480.md#insn-00552490)
- 新版 `00575344`（命令位置の公開資料なし） · `00575324`（命令位置の公開資料なし） · `00575328`（命令位置の公開資料なし）

~~~diff
- 005524ac ["INT_ADD", "register:40f0:8", ["const:5524ac:8", "const:4:8"]]
- 005524ac ["CALL", null, ["callee:00c57a30:8"]]
+ 00575344 ["INT_ADD", "register:40f0:8", ["const:575344:8", "const:4:8"]]
+ 00575344 ["CALL", null, ["callee:00c57a30:8"]]
- 005524ac bytes cd221a94
+ 00575344 bytes bb891b94
- 0055248c ["COPY", "register:4098:8", ["const:be5000:8"]]
+ 00575324 ["COPY", "register:4098:8", ["const:c62000:8"]]
- 0055248c bytes 933400f0
+ 00575324 bytes 733700b0
- 00552490 ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 00552490 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00552490 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00552490 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00575328 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00575328 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00575328 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00575328 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00552490 bytes 73423f91
+ 00575328 bytes 73422e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-189b0b5abc8b020b82b75d1397e6afba"></a>

### [`00552540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552540.md) → [`005753d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005753d8.md) FUN_005753d8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad8.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00550970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550970.md) · 呼出先 11件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057541c",
      "incomplete_value": true,
      "site": "00575434",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00552584",
      "incomplete_value": true,
      "site": "0055259c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:295000:8"
              ],
              [
                "leaf",
                "const:b8c:8"
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
      "definition_site": "00575438",
      "incomplete_value": true,
      "site": "00575444",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4a1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005525a0",
      "incomplete_value": true,
      "site": "005525ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:725:8"
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
      "definition_site": "00575448",
      "incomplete_value": true,
      "site": "00575448",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005525b0",
      "incomplete_value": true,
      "site": "005525b0",
      "value": [
        "LOAD",
        "8",
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
      "0057541c",
      "READ",
      [
        "storage",
        "00295b8c",
        null,
        "string"
      ]
    ],
    [
      "00575438",
      "READ",
      [
        "storage",
        "002aa725",
        null,
        "string"
      ]
    ],
    [
      "0057543c",
      "READ",
      [
        "storage",
        "002aa732",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057541c",
      "READ",
      [
        "storage",
        "002a55c5",
        null,
        "string"
      ]
    ],
    [
      "00575438",
      "READ",
      [
        "storage",
        "002bb4a1",
        null,
        "string"
      ]
    ],
    [
      "0057543c",
      "READ",
      [
        "storage",
        "002bb4ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00552564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552540.md#insn-00552564) · [`0055256c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552540.md#insn-0055256c) · [`00552574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552540.md#insn-00552574)
- 新版 `005753fc`（命令位置の公開資料なし） · `00575404`（命令位置の公開資料なし） · `0057540c`（命令位置の公開資料なし）

~~~diff
- 00552564 ["INT_ADD", "register:40f0:8", ["const:552564:8", "const:4:8"]]
- 00552564 ["CALL", null, ["callee:00588e2c:8"]]
+ 005753fc ["INT_ADD", "register:40f0:8", ["const:5753fc:8", "const:4:8"]]
+ 005753fc ["CALL", null, ["callee:00588e2c:8"]]
- 00552564 bytes 8c4e0094
+ 005753fc bytes 8c4e0094
- 0055256c ["INT_ADD", "register:40f0:8", ["const:55256c:8", "const:4:8"]]
- 0055256c ["CALL", null, ["callee:0058911c:8"]]
+ 00575404 ["INT_ADD", "register:40f0:8", ["const:575404:8", "const:4:8"]]
+ 00575404 ["CALL", null, ["callee:0058911c:8"]]
- 0055256c bytes 464f0094
+ 00575404 bytes 464f0094
- 00552574 ["COPY", "register:4048:8", ["const:295000:8"]]
+ 0057540c ["COPY", "register:4048:8", ["const:2a5000:8"]]
- 00552574 bytes 09eafff0
+ 0057540c bytes 89e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f22ac2a35f0fcd0e438ed6d2ca6b5b8a"></a>

### [`005526b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005526b0.md) → [`00575548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575548.md) FUN_00575548

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dadc.md) · 呼出先 14件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00552eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552eb4.md) [`005530c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005530c0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md)
- 新版 呼出元 1件 [`00550974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550974.md) · 呼出先 14件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00575d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575d4c.md) [`00575f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575f58.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.40% / 新版 82.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00575598",
      "incomplete_value": true,
      "site": "005755a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:27a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00552700",
      "incomplete_value": true,
      "site": "00552710",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:964:8"
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
      "definition_site": "005755b8",
      "incomplete_value": true,
      "site": "005755b8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00552720",
      "incomplete_value": true,
      "site": "00552720",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005755ac",
      "incomplete_value": true,
      "site": "005755c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00552714",
      "incomplete_value": true,
      "site": "00552728",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00575598",
      "READ",
      [
        "storage",
        "00294964",
        null,
        "string"
      ]
    ],
    [
      "0057559c",
      "READ",
      [
        "storage",
        "00294973",
        null,
        "string"
      ]
    ],
    [
      "005755ac",
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
      "00575598",
      "READ",
      [
        "storage",
        "002a427a",
        null,
        "string"
      ]
    ],
    [
      "0057559c",
      "READ",
      [
        "storage",
        "002a4289",
        null,
        "string"
      ]
    ],
    [
      "005755ac",
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

- 旧版 [`00552824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005526b0.md#insn-00552824) · [`00552848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005526b0.md#insn-00552848) · [`0055286c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005526b0.md#insn-0055286c)
- 新版 `005756bc`（命令位置の公開資料なし） · `005756e0`（命令位置の公開資料なし） · `00575704`（命令位置の公開資料なし）

~~~diff
- 00552824 ["INT_ADD", "register:40f0:8", ["const:552824:8", "const:4:8"]]
- 00552824 ["CALL", null, ["callee:00575f58:8"]]
+ 005756bc ["INT_ADD", "register:40f0:8", ["const:5756bc:8", "const:4:8"]]
+ 005756bc ["CALL", null, ["callee:00575f58:8"]]
- 00552824 bytes 27020094
+ 005756bc bytes 27020094
- 00552848 ["INT_ADD", "register:40f0:8", ["const:552848:8", "const:4:8"]]
- 00552848 ["CALL", null, ["callee:00575d4c:8"]]
+ 005756e0 ["INT_ADD", "register:40f0:8", ["const:5756e0:8", "const:4:8"]]
+ 005756e0 ["CALL", null, ["callee:00575d4c:8"]]
- 00552848 bytes 9b010094
+ 005756e0 bytes 9b010094
- 0055286c ["INT_ADD", "register:40f0:8", ["const:55286c:8", "const:4:8"]]
- 0055286c ["CALL", null, ["callee:00575d4c:8"]]
+ 00575704 ["INT_ADD", "register:40f0:8", ["const:575704:8", "const:4:8"]]
+ 00575704 ["CALL", null, ["callee:00575d4c:8"]]
- 0055286c bytes 92010094
+ 00575704 bytes 92010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29564dc2b9466f86581ce5175c4a170d"></a>

### [`005528f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005528f8.md) → [`00575790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575790.md) FUN_00575790

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dae0.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00553278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553278.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00550978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550978.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00576110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576110.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.72% / 新版 90.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005757d8",
      "incomplete_value": true,
      "site": "005757e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4b7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00552940",
      "incomplete_value": true,
      "site": "00552950",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:73b:8"
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
      "definition_site": "005757dc",
      "incomplete_value": true,
      "site": "00575800",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00552944",
      "incomplete_value": true,
      "site": "00552968",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005757ec",
      "incomplete_value": true,
      "site": "00575804",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00552954",
      "incomplete_value": true,
      "site": "0055296c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005757d8",
      "READ",
      [
        "storage",
        "002aa73b",
        null,
        "string"
      ]
    ],
    [
      "005757dc",
      "READ",
      [
        "storage",
        "002aa748",
        null,
        "string"
      ]
    ],
    [
      "005757ec",
      "READ",
      [
        "storage",
        "002b14c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005757d8",
      "READ",
      [
        "storage",
        "002bb4b7",
        null,
        "string"
      ]
    ],
    [
      "005757dc",
      "READ",
      [
        "storage",
        "002bb4c4",
        null,
        "string"
      ]
    ],
    [
      "005757ec",
      "READ",
      [
        "storage",
        "002c2b10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055291c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005528f8.md#insn-0055291c) · [`00552924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005528f8.md#insn-00552924) · [`00552930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005528f8.md#insn-00552930)
- 新版 `005757b4`（命令位置の公開資料なし） · `005757bc`（命令位置の公開資料なし） · `005757c8`（命令位置の公開資料なし）

~~~diff
- 0055291c ["INT_ADD", "register:40f0:8", ["const:55291c:8", "const:4:8"]]
- 0055291c ["CALL", null, ["callee:00588e2c:8"]]
+ 005757b4 ["INT_ADD", "register:40f0:8", ["const:5757b4:8", "const:4:8"]]
+ 005757b4 ["CALL", null, ["callee:00588e2c:8"]]
- 0055291c bytes 9e4d0094
+ 005757b4 bytes 9e4d0094
- 00552924 ["INT_ADD", "register:40f0:8", ["const:552924:8", "const:4:8"]]
- 00552924 ["CALL", null, ["callee:0058911c:8"]]
+ 005757bc ["INT_ADD", "register:40f0:8", ["const:5757bc:8", "const:4:8"]]
+ 005757bc ["CALL", null, ["callee:0058911c:8"]]
- 00552924 bytes 584e0094
+ 005757bc bytes 584e0094
- 00552930 ["INT_ADD", "register:40f0:8", ["const:552930:8", "const:4:8"]]
- 00552930 ["CALL", null, ["callee:00c57a90:8"]]
+ 005757c8 ["INT_ADD", "register:40f0:8", ["const:5757c8:8", "const:4:8"]]
+ 005757c8 ["CALL", null, ["callee:00c57a90:8"]]
- 00552930 bytes c4211a94
+ 005757c8 bytes b2881b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a6fd269f606a8f7a025599a42adf31c"></a>

### [`00552ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552ab8.md) → [`00575950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575950.md) FUN_00575950

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dae4.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0055097c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055097c.md) · 呼出先 13件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005759b4",
      "incomplete_value": true,
      "site": "005759cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:292:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00552b1c",
      "incomplete_value": true,
      "site": "00552b34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:97c:8"
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
      "005759b4",
      "READ",
      [
        "storage",
        "0029497c",
        null,
        "string"
      ]
    ],
    [
      "005759e8",
      "READ",
      [
        "storage",
        "002aea0e",
        null,
        "string"
      ]
    ],
    [
      "005759e8",
      "READ",
      [
        "storage",
        "002aea1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005759b4",
      "READ",
      [
        "storage",
        "002a4292",
        null,
        "string"
      ]
    ],
    [
      "005759e8",
      "READ",
      [
        "storage",
        "002bfef2",
        null,
        "string"
      ]
    ],
    [
      "005759e8",
      "READ",
      [
        "storage",
        "002bff02",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00552b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552ab8.md#insn-00552b04) · [`00552b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552ab8.md#insn-00552b0c) · [`00552b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552ab8.md#insn-00552b10)
- 新版 `0057599c`（命令位置の公開資料なし） · `005759a4`（命令位置の公開資料なし） · `005759a8`（命令位置の公開資料なし）

~~~diff
- 00552b04 ["INT_ADD", "register:40f0:8", ["const:552b04:8", "const:4:8"]]
- 00552b04 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057599c ["INT_ADD", "register:40f0:8", ["const:57599c:8", "const:4:8"]]
+ 0057599c ["CALL", null, ["callee:00588e2c:8"]]
- 00552b04 bytes 244d0094
+ 0057599c bytes 244d0094
- 00552b0c ["INT_ADD", "register:40f0:8", ["const:552b0c:8", "const:4:8"]]
- 00552b0c ["CALL", null, ["callee:0058911c:8"]]
+ 005759a4 ["INT_ADD", "register:40f0:8", ["const:5759a4:8", "const:4:8"]]
+ 005759a4 ["CALL", null, ["callee:0058911c:8"]]
- 00552b0c bytes de4d0094
+ 005759a4 bytes de4d0094
- 00552b10 ["COPY", "register:4048:8", ["const:294000:8"]]
+ 005759a8 ["COPY", "register:4048:8", ["const:2a4000:8"]]
- 00552b10 bytes 09eaffd0
+ 005759a8 bytes 69e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd6ef0e1f5bd24381115e3d2f3d3de48"></a>

### [`0055347c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/0055347c.md) → [`00576314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576314.md) _INIT_30

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`005524e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/005524e0.md) [`00552510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552510.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00575378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575378.md) [`005753a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/005753a8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057633c",
      "incomplete_value": false,
      "site": "0057633c",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:dc0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005534a4",
      "incomplete_value": false,
      "site": "005534a4",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:300:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "00576358",
      "incomplete_value": false,
      "site": "00576358",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:df0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005534c0",
      "incomplete_value": false,
      "site": "005534c0",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:330:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "00576334",
      "incomplete_value": false,
      "site": "00576340",
      "value": [
        "leaf",
        "const:575378:8"
      ]
    },
    "old": {
      "definition_site": "0055349c",
      "incomplete_value": false,
      "site": "005534a8",
      "value": [
        "leaf",
        "const:5524e0:8"
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
      "0057632c",
      "PARAM",
      [
        "storage",
        "00c26300",
        null,
        null
      ]
    ],
    [
      "00576334",
      "PARAM",
      [
        "storage",
        "005524e0",
        null,
        null
      ]
    ],
    [
      "00576338",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057632c",
      "PARAM",
      [
        "storage",
        "00ca5dc0",
        null,
        null
      ]
    ],
    [
      "00576334",
      "PARAM",
      [
        "storage",
        "00575378",
        null,
        null
      ]
    ],
    [
      "00576338",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005534a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/0055347c.md#insn-005534a8) · [`00553488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/0055347c.md#insn-00553488) · [`0055348c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/0055347c.md#insn-0055348c)
- 新版 `00576340`（命令位置の公開資料なし） · `00576320`（命令位置の公開資料なし） · `00576324`（命令位置の公開資料なし）

~~~diff
- 005534a8 ["INT_ADD", "register:40f0:8", ["const:5534a8:8", "const:4:8"]]
- 005534a8 ["CALL", null, ["callee:00c57a30:8"]]
+ 00576340 ["INT_ADD", "register:40f0:8", ["const:576340:8", "const:4:8"]]
+ 00576340 ["CALL", null, ["callee:00c57a30:8"]]
- 005534a8 bytes ce1e1a94
+ 00576340 bytes bc851b94
- 00553488 ["COPY", "register:4098:8", ["const:be5000:8"]]
+ 00576320 ["COPY", "register:4098:8", ["const:c62000:8"]]
- 00553488 bytes 933400d0
+ 00576320 bytes 73370090
- 0055348c ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 0055348c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0055348c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0055348c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00576324 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00576324 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00576324 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00576324 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0055348c bytes 73423f91
+ 00576324 bytes 73422e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b9fd33f4d20b010a57cfb4133aef600"></a>

### [`005534d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005534d4.md) → [`0057636c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057636c.md) FUN_0057636c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052daf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052daf0.md) · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 1件 [`00550988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550988.md) · 呼出先 4件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005763b0",
      "incomplete_value": false,
      "site": "005763c8",
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
            "const:1da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553518",
      "incomplete_value": false,
      "site": "00553530",
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
            "const:9e1:8"
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
      "definition_site": "005763b8",
      "incomplete_value": false,
      "site": "005763c8",
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
            "const:1ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553520",
      "incomplete_value": false,
      "site": "00553530",
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
            "const:9f1:8"
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
      "005763b0",
      "PARAM",
      [
        "storage",
        "002939e1",
        null,
        "string"
      ]
    ],
    [
      "005763b8",
      "PARAM",
      [
        "storage",
        "002939f1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005763b0",
      "PARAM",
      [
        "storage",
        "002a31da",
        null,
        "string"
      ]
    ],
    [
      "005763b8",
      "PARAM",
      [
        "storage",
        "002a31ea",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00553530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005534d4.md#insn-00553530) · [`005534e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005534d4.md#insn-005534e4) · [`005534ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005534d4.md#insn-005534ec)
- 新版 `005763c8`（命令位置の公開資料なし） · `0057637c`（命令位置の公開資料なし） · `00576384`（命令位置の公開資料なし）

~~~diff
- 00553530 ["COPY", "register:0:8", ["register:4040:8"]]
- 00553530 ["INT_ADD", "register:40f0:8", ["const:553530:8", "const:4:8"]]
- 00553530 ["CALLIND", null, ["register:0:8"]]
+ 005763c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005763c8 ["INT_ADD", "register:40f0:8", ["const:5763c8:8", "const:4:8"]]
+ 005763c8 ["CALLIND", null, ["register:0:8"]]
- 00553530 bytes 00013fd6
+ 005763c8 bytes 00013fd6
- 005534e4 ["INT_ADD", "register:40f0:8", ["const:5534e4:8", "const:4:8"]]
- 005534e4 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057637c ["INT_ADD", "register:40f0:8", ["const:57637c:8", "const:4:8"]]
+ 0057637c ["CALL", null, ["callee:00588e2c:8"]]
- 005534e4 bytes ac4a0094
+ 0057637c bytes ac4a0094
- 005534ec ["INT_ADD", "register:40f0:8", ["const:5534ec:8", "const:4:8"]]
- 005534ec ["CALL", null, ["callee:0058911c:8"]]
+ 00576384 ["INT_ADD", "register:40f0:8", ["const:576384:8", "const:4:8"]]
+ 00576384 ["CALL", null, ["callee:0058911c:8"]]
- 005534ec bytes 664b0094
+ 00576384 bytes 664b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6c646fda53332f8d0b9ef16211c28ae"></a>

### [`00553568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553568.md) → [`00576400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576400.md) FUN_00576400

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052daf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052daf4.md) · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 1件 [`0055098c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055098c.md) · 呼出先 4件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00576450",
      "incomplete_value": false,
      "site": "00576468",
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
            "const:d12:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005535b8",
      "incomplete_value": false,
      "site": "005535d0",
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
            "const:758:8"
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
      "definition_site": "00576458",
      "incomplete_value": false,
      "site": "00576468",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005535c0",
      "incomplete_value": false,
      "site": "005535d0",
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
            "const:5e6:8"
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
      "00576450",
      "PARAM",
      [
        "storage",
        "002a0758",
        null,
        "string"
      ]
    ],
    [
      "00576458",
      "PARAM",
      [
        "storage",
        "0029d5e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00576450",
      "PARAM",
      [
        "storage",
        "002b0d12",
        null,
        "string"
      ]
    ],
    [
      "00576458",
      "PARAM",
      [
        "storage",
        "002ad870",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005535d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553568.md#insn-005535d0) · [`00553584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553568.md#insn-00553584) · [`0055358c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553568.md#insn-0055358c)
- 新版 `00576468`（命令位置の公開資料なし） · `0057641c`（命令位置の公開資料なし） · `00576424`（命令位置の公開資料なし）

~~~diff
- 005535d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005535d0 ["INT_ADD", "register:40f0:8", ["const:5535d0:8", "const:4:8"]]
- 005535d0 ["CALLIND", null, ["register:0:8"]]
+ 00576468 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00576468 ["INT_ADD", "register:40f0:8", ["const:576468:8", "const:4:8"]]
+ 00576468 ["CALLIND", null, ["register:0:8"]]
- 005535d0 bytes 00013fd6
+ 00576468 bytes 00013fd6
- 00553584 ["INT_ADD", "register:40f0:8", ["const:553584:8", "const:4:8"]]
- 00553584 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057641c ["INT_ADD", "register:40f0:8", ["const:57641c:8", "const:4:8"]]
+ 0057641c ["CALL", null, ["callee:00588e2c:8"]]
- 00553584 bytes 844a0094
+ 0057641c bytes 844a0094
- 0055358c ["INT_ADD", "register:40f0:8", ["const:55358c:8", "const:4:8"]]
- 0055358c ["CALL", null, ["callee:0058911c:8"]]
+ 00576424 ["INT_ADD", "register:40f0:8", ["const:576424:8", "const:4:8"]]
+ 00576424 ["CALL", null, ["callee:0058911c:8"]]
- 0055358c bytes 3e4b0094
+ 00576424 bytes 3e4b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cc1668cf3801ea6426f2123466ab802"></a>

### [`00553628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553628.md) → [`005764c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005764c0.md) FUN_005764c0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052db20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db20.md) · 呼出先 4件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 1件 [`005509b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509b8.md) · 呼出先 4件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00576504",
      "incomplete_value": false,
      "site": "0057651c",
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
            "const:3eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055366c",
      "incomplete_value": false,
      "site": "00553684",
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
            "const:748:8"
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
      "definition_site": "0057650c",
      "incomplete_value": false,
      "site": "0057651c",
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
            "const:a4f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553674",
      "incomplete_value": false,
      "site": "00553684",
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
            "const:6ca:8"
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
      "00576504",
      "PARAM",
      [
        "storage",
        "002a9748",
        null,
        "string"
      ]
    ],
    [
      "0057650c",
      "PARAM",
      [
        "storage",
        "0029e6ca",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00576504",
      "PARAM",
      [
        "storage",
        "002ba3eb",
        null,
        "string"
      ]
    ],
    [
      "0057650c",
      "PARAM",
      [
        "storage",
        "002aea4f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00553684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553628.md#insn-00553684) · [`00553638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553628.md#insn-00553638) · [`00553640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553628.md#insn-00553640)
- 新版 `0057651c`（命令位置の公開資料なし） · `005764d0`（命令位置の公開資料なし） · `005764d8`（命令位置の公開資料なし）

~~~diff
- 00553684 ["COPY", "register:0:8", ["register:4040:8"]]
- 00553684 ["INT_ADD", "register:40f0:8", ["const:553684:8", "const:4:8"]]
- 00553684 ["CALLIND", null, ["register:0:8"]]
+ 0057651c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0057651c ["INT_ADD", "register:40f0:8", ["const:57651c:8", "const:4:8"]]
+ 0057651c ["CALLIND", null, ["register:0:8"]]
- 00553684 bytes 00013fd6
+ 0057651c bytes 00013fd6
- 00553638 ["INT_ADD", "register:40f0:8", ["const:553638:8", "const:4:8"]]
- 00553638 ["CALL", null, ["callee:00588e2c:8"]]
+ 005764d0 ["INT_ADD", "register:40f0:8", ["const:5764d0:8", "const:4:8"]]
+ 005764d0 ["CALL", null, ["callee:00588e2c:8"]]
- 00553638 bytes 574a0094
+ 005764d0 bytes 574a0094
- 00553640 ["INT_ADD", "register:40f0:8", ["const:553640:8", "const:4:8"]]
- 00553640 ["CALL", null, ["callee:0058911c:8"]]
+ 005764d8 ["INT_ADD", "register:40f0:8", ["const:5764d8:8", "const:4:8"]]
+ 005764d8 ["CALL", null, ["callee:0058911c:8"]]
- 00553640 bytes 114b0094
+ 005764d8 bytes 114b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9ad0e5b53e7c72bbdf60cc10591c31e"></a>

### [`005536e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005536e4.md) → [`0057657c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057657c.md) FUN_0057657c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052db24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db24.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`005509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509bc.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

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
      "definition_site": "005765b8",
      "incomplete_value": true,
      "site": "005765d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ecb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553720",
      "incomplete_value": true,
      "site": "00553738",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:65e:8"
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
      "005765b8",
      "READ",
      [
        "storage",
        "002a465e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005765b8",
      "READ",
      [
        "storage",
        "002b4ecb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00553700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005536e4.md#insn-00553700) · [`00553708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005536e4.md#insn-00553708) · [`00553710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005536e4.md#insn-00553710)
- 新版 `00576598`（命令位置の公開資料なし） · `005765a0`（命令位置の公開資料なし） · `005765a8`（命令位置の公開資料なし）

~~~diff
- 00553700 ["INT_ADD", "register:40f0:8", ["const:553700:8", "const:4:8"]]
- 00553700 ["CALL", null, ["callee:00588e2c:8"]]
+ 00576598 ["INT_ADD", "register:40f0:8", ["const:576598:8", "const:4:8"]]
+ 00576598 ["CALL", null, ["callee:00588e2c:8"]]
- 00553700 bytes 254a0094
+ 00576598 bytes 254a0094
- 00553708 ["INT_ADD", "register:40f0:8", ["const:553708:8", "const:4:8"]]
- 00553708 ["CALL", null, ["callee:0058911c:8"]]
+ 005765a0 ["INT_ADD", "register:40f0:8", ["const:5765a0:8", "const:4:8"]]
+ 005765a0 ["CALL", null, ["callee:0058911c:8"]]
- 00553708 bytes df4a0094
+ 005765a0 bytes df4a0094
- 00553710 ["COPY", "register:4048:8", ["const:2a4000:8"]]
+ 005765a8 ["COPY", "register:4048:8", ["const:2b4000:8"]]
- 00553710 bytes 89eaffb0
+ 005765a8 bytes e9e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ced4ea71fa51a95ea4234a5585dc729c"></a>

### [`00553828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553828.md) → [`005766c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005766c0.md) FUN_005766c0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00553950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553950.md) · 呼出先 7件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 1件 [`005767e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005767e8.md) · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005766e8",
      "incomplete_value": true,
      "site": "005766ec",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553850",
      "incomplete_value": true,
      "site": "00553854",
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
            "const:ba0:8"
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
      "005766ec",
      "DATA",
      [
        "storage",
        "00beeba0",
        null,
        "undefined *"
      ]
    ],
    [
      "00576710",
      "READ",
      [
        "storage",
        "002939f5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005766ec",
      "DATA",
      [
        "storage",
        "00c6b760",
        null,
        "undefined *"
      ]
    ],
    [
      "00576710",
      "READ",
      [
        "storage",
        "002a31ee",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055384c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553828.md#insn-0055384c) · [`00553850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553828.md#insn-00553850) · [`00553858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553828.md#insn-00553858)
- 新版 `005766e4`（命令位置の公開資料なし） · `005766e8`（命令位置の公開資料なし） · `005766f0`（命令位置の公開資料なし）

~~~diff
- 0055384c ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 005766e4 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055384c bytes c83400f0
+ 005766e4 bytes a83700b0
- 00553850 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00553850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00553850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00553850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005766e8 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 005766e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005766e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005766e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00553850 bytes 08812e91
+ 005766e8 bytes 08811d91
- 00553858 ["INT_ADD", "register:40f0:8", ["const:553858:8", "const:4:8"]]
- 00553858 ["CALL", null, ["callee:00588e2c:8"]]
+ 005766f0 ["INT_ADD", "register:40f0:8", ["const:5766f0:8", "const:4:8"]]
+ 005766f0 ["CALL", null, ["callee:00588e2c:8"]]
- 00553858 bytes cf490094
+ 005766f0 bytes cf490094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e604516b747c804681c2210c341173b4"></a>

### [`00553ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553ac4.md) → [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) FUN_0057695c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00554440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554440.md) [`00554a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554a08.md) [`00554da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554da8.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md)
- 新版 呼出元 3件 [`005772d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md) [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.81% / 新版 96.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005769d0",
      "incomplete_value": true,
      "site": "005769d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:4d5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00553b38",
      "incomplete_value": true,
      "site": "00553b38",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:759:8"
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
      "definition_site": "005769d4",
      "incomplete_value": true,
      "site": "005769d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00553b3c",
      "incomplete_value": true,
      "site": "00553b3c",
      "value": [
        "LOAD",
        "8",
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
      "005769c0",
      "READ",
      [
        "storage",
        "002aa759",
        null,
        "string"
      ]
    ],
    [
      "005769c8",
      "READ",
      [
        "storage",
        "002aa75f",
        null,
        "string"
      ]
    ],
    [
      "00576a38",
      "READ",
      [
        "storage",
        "002afceb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005769c0",
      "READ",
      [
        "storage",
        "002bb4d5",
        null,
        "string"
      ]
    ],
    [
      "005769c8",
      "READ",
      [
        "storage",
        "002bb4db",
        null,
        "string"
      ]
    ],
    [
      "00576a38",
      "READ",
      [
        "storage",
        "002c127b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00553b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553ac4.md#insn-00553b08) · [`00553b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553ac4.md#insn-00553b18) · [`00553b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553ac4.md#insn-00553b20)
- 新版 `005769a0`（命令位置の公開資料なし） · `005769b0`（命令位置の公開資料なし） · `005769b8`（命令位置の公開資料なし）

~~~diff
- 00553b08 ["INT_ADD", "register:40f0:8", ["const:553b08:8", "const:4:8"]]
- 00553b08 ["CALL", null, ["callee:00588e2c:8"]]
+ 005769a0 ["INT_ADD", "register:40f0:8", ["const:5769a0:8", "const:4:8"]]
+ 005769a0 ["CALL", null, ["callee:00588e2c:8"]]
- 00553b08 bytes 23490094
+ 005769a0 bytes 23490094
- 00553b18 ["INT_ADD", "register:40f0:8", ["const:553b18:8", "const:4:8"]]
- 00553b18 ["CALL", null, ["callee:0058911c:8"]]
+ 005769b0 ["INT_ADD", "register:40f0:8", ["const:5769b0:8", "const:4:8"]]
+ 005769b0 ["CALL", null, ["callee:0058911c:8"]]
- 00553b18 bytes db490094
+ 005769b0 bytes db490094
- 00553b20 ["COPY", "register:4048:8", ["const:2aa000:8"]]
+ 005769b8 ["COPY", "register:4048:8", ["const:2bb000:8"]]
- 00553b20 bytes a9eafff0
+ 005769b8 bytes 29eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b97ff0b73d20d4e194d0caf5a07c3f3"></a>

### [`00554030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554030.md) → [`00576ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576ec8.md) FUN_00576ec8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00554440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554440.md) [`00554da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554da8.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 2件 [`005772d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md) [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00576f28",
      "incomplete_value": true,
      "site": "00576f3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00554090",
      "incomplete_value": true,
      "site": "005540a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bb2:8"
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
      "definition_site": "00576f40",
      "incomplete_value": true,
      "site": "00576f40",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005540a8",
      "incomplete_value": true,
      "site": "005540a8",
      "value": [
        "LOAD",
        "8",
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
      "00576f0c",
      "READ",
      [
        "storage",
        "00294991",
        null,
        "string"
      ]
    ],
    [
      "00576f14",
      "READ",
      [
        "storage",
        "00294997",
        null,
        "string"
      ]
    ],
    [
      "00576f28",
      "READ",
      [
        "storage",
        "00296bb2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00576f0c",
      "READ",
      [
        "storage",
        "002a42a7",
        null,
        "string"
      ]
    ],
    [
      "00576f14",
      "READ",
      [
        "storage",
        "002a42ad",
        null,
        "string"
      ]
    ],
    [
      "00576f28",
      "READ",
      [
        "storage",
        "002a66e7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055405c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554030.md#insn-0055405c) · [`00554064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554030.md#insn-00554064) · [`0055406c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554030.md#insn-0055406c)
- 新版 `00576ef4`（命令位置の公開資料なし） · `00576efc`（命令位置の公開資料なし） · `00576f04`（命令位置の公開資料なし）

~~~diff
- 0055405c ["INT_ADD", "register:40f0:8", ["const:55405c:8", "const:4:8"]]
- 0055405c ["CALL", null, ["callee:00588e2c:8"]]
+ 00576ef4 ["INT_ADD", "register:40f0:8", ["const:576ef4:8", "const:4:8"]]
+ 00576ef4 ["CALL", null, ["callee:00588e2c:8"]]
- 0055405c bytes ce470094
+ 00576ef4 bytes ce470094
- 00554064 ["INT_ADD", "register:40f0:8", ["const:554064:8", "const:4:8"]]
- 00554064 ["CALL", null, ["callee:0058911c:8"]]
+ 00576efc ["INT_ADD", "register:40f0:8", ["const:576efc:8", "const:4:8"]]
+ 00576efc ["CALL", null, ["callee:0058911c:8"]]
- 00554064 bytes 88480094
+ 00576efc bytes 88480094
- 0055406c ["COPY", "register:4048:8", ["const:294000:8"]]
+ 00576f04 ["COPY", "register:4048:8", ["const:2a4000:8"]]
- 0055406c bytes 09eaff90
+ 00576f04 bytes 69e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f25d0fde06b3a79c51d9f02614798334"></a>

### [`00554274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554274.md) → [`0057710c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/0057710c.md) FUN_0057710c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00554a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554a08.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 1件 [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00577168",
      "incomplete_value": true,
      "site": "00577168",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:715:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005542d0",
      "incomplete_value": true,
      "site": "005542d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f2:8"
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
      "definition_site": "00577170",
      "incomplete_value": true,
      "site": "00577170",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005542d8",
      "incomplete_value": true,
      "site": "005542d8",
      "value": [
        "LOAD",
        "8",
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
      "00577150",
      "READ",
      [
        "storage",
        "002ab7f2",
        null,
        "string"
      ]
    ],
    [
      "00577158",
      "READ",
      [
        "storage",
        "002ab7f7",
        null,
        "string"
      ]
    ],
    [
      "0057716c",
      "READ",
      [
        "storage",
        "00296bb2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00577150",
      "READ",
      [
        "storage",
        "002bc715",
        null,
        "string"
      ]
    ],
    [
      "00577158",
      "READ",
      [
        "storage",
        "002bc71a",
        null,
        "string"
      ]
    ],
    [
      "0057716c",
      "READ",
      [
        "storage",
        "002a66e7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005542a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554274.md#insn-005542a0) · [`005542a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554274.md#insn-005542a8) · [`005542b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554274.md#insn-005542b0)
- 新版 `00577138`（命令位置の公開資料なし） · `00577140`（命令位置の公開資料なし） · `00577148`（命令位置の公開資料なし）

~~~diff
- 005542a0 ["INT_ADD", "register:40f0:8", ["const:5542a0:8", "const:4:8"]]
- 005542a0 ["CALL", null, ["callee:00588e2c:8"]]
+ 00577138 ["INT_ADD", "register:40f0:8", ["const:577138:8", "const:4:8"]]
+ 00577138 ["CALL", null, ["callee:00588e2c:8"]]
- 005542a0 bytes 3d470094
+ 00577138 bytes 3d470094
- 005542a8 ["INT_ADD", "register:40f0:8", ["const:5542a8:8", "const:4:8"]]
- 005542a8 ["CALL", null, ["callee:0058911c:8"]]
+ 00577140 ["INT_ADD", "register:40f0:8", ["const:577140:8", "const:4:8"]]
+ 00577140 ["CALL", null, ["callee:0058911c:8"]]
- 005542a8 bytes f7470094
+ 00577140 bytes f7470094
- 005542b0 ["COPY", "register:4048:8", ["const:2ab000:8"]]
+ 00577148 ["COPY", "register:4048:8", ["const:2bc000:8"]]
- 005542b0 bytes a9eafff0
+ 00577148 bytes 29eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dcb2b9c703d33e370a82e50ba42bd62"></a>

### [`00554440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554440.md) → [`005772d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005772d8.md) FUN_005772d8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db2c.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00553ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553ac4.md) [`00554030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554030.md) [`005541a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005541a8.md)
- 新版 呼出元 1件 [`005509c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509c4.md) · 呼出先 15件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) [`00576ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576ec8.md) [`00577040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md)

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
    "old": {
      "definition_site": "0055457c",
      "incomplete_value": false,
      "site": "00554584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
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
    "old": {
      "definition_site": "00554594",
      "incomplete_value": false,
      "site": "00554594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
    "old": {
      "definition_site": "00554640",
      "incomplete_value": true,
      "site": "00554640",
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
            "const:3b0:8"
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
      "00577340",
      "READ",
      [
        "storage",
        "002a9754",
        null,
        "string"
      ]
    ],
    [
      "0057741c",
      "DATA",
      [
        "storage",
        "00beeec0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057742c",
      "DATA",
      [
        "storage",
        "00beeba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577340",
      "READ",
      [
        "storage",
        "002ba3f7",
        null,
        "string"
      ]
    ],
    [
      "0057741c",
      "DATA",
      [
        "storage",
        "00c6ba80",
        null,
        "undefined *"
      ]
    ],
    [
      "0057742c",
      "DATA",
      [
        "storage",
        "00c6b760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00554640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554440.md#insn-00554640) · [`00554488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554440.md#insn-00554488) · [`00554490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554440.md#insn-00554490)
- 新版 `005774d8`（命令位置の公開資料なし） · `00577320`（命令位置の公開資料なし） · `00577328`（命令位置の公開資料なし）

~~~diff
- 00554640 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3b0:8"]]
- 00554640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005774d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 005774d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00554640 bytes 09d901f9
+ 005774d8 bytes 093907f9
- 00554488 ["INT_ADD", "register:40f0:8", ["const:554488:8", "const:4:8"]]
- 00554488 ["CALL", null, ["callee:00588e2c:8"]]
+ 00577320 ["INT_ADD", "register:40f0:8", ["const:577320:8", "const:4:8"]]
+ 00577320 ["CALL", null, ["callee:00588e2c:8"]]
- 00554488 bytes c3460094
+ 00577320 bytes c3460094
- 00554490 ["INT_ADD", "register:40f0:8", ["const:554490:8", "const:4:8"]]
- 00554490 ["CALL", null, ["callee:0058911c:8"]]
+ 00577328 ["INT_ADD", "register:40f0:8", ["const:577328:8", "const:4:8"]]
+ 00577328 ["CALL", null, ["callee:0058911c:8"]]
- 00554490 bytes 7d470094
+ 00577328 bytes 7d470094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad41bb4f9e7ca165e642fcd9b549b8c2"></a>

### [`005547a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005547a0.md) → [`00577638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577638.md) FUN_00577638

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00554914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554914.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`005777ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005777ac.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

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
    "old": {
      "definition_site": "005547c0",
      "incomplete_value": false,
      "site": "005547c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "00577658",
      "DATA",
      [
        "storage",
        "00beec28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00577658",
      "DATA",
      [
        "storage",
        "00c6b7e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005547b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005547a0.md#insn-005547b4) · [`005547b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005547a0.md#insn-005547b8) · [`005547bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005547a0.md#insn-005547bc)
- 新版 `0057764c`（命令位置の公開資料なし） · `00577650`（命令位置の公開資料なし）

~~~diff
- 005547b4 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 0057764c ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 005547b4 bytes c83400d0
+ 0057764c bytes a8370090
- 005547b8 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 005547b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005547b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005547b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00577650 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00577650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00577650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00577650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005547b8 bytes 08a13091
+ 00577650 bytes 08a11f91
- 005547bc ["COPY", "register:40a0:8", ["register:4000:8"]]
- 005547bc bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06ec1f4aed3479fae39431d7f270b03d"></a>

### [`00554a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554a08.md) → [`005778a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/005778a0.md) FUN_005778a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00553ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553ac4.md) [`005541a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005541a8.md) [`00554274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554274.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) [`00577040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md) [`0057710c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/0057710c.md)

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
    "old": {
      "definition_site": "00554b48",
      "incomplete_value": false,
      "site": "00554b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
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
    "old": {
      "definition_site": "00554c0c",
      "incomplete_value": true,
      "site": "00554c0c",
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
            "const:3b0:8"
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
    "old": {
      "definition_site": "00554c08",
      "incomplete_value": true,
      "site": "00554c08",
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
      "0057790c",
      "READ",
      [
        "storage",
        "002a9754",
        null,
        "string"
      ]
    ],
    [
      "005779e8",
      "DATA",
      [
        "storage",
        "00beeec0",
        null,
        "undefined *"
      ]
    ],
    [
      "005779f8",
      "DATA",
      [
        "storage",
        "00beeba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057790c",
      "READ",
      [
        "storage",
        "002ba3f7",
        null,
        "string"
      ]
    ],
    [
      "005779e8",
      "DATA",
      [
        "storage",
        "00c6ba80",
        null,
        "undefined *"
      ]
    ],
    [
      "005779f8",
      "DATA",
      [
        "storage",
        "00c6b760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00554c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554a08.md#insn-00554c0c) · [`00554a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554a08.md#insn-00554a54) · [`00554a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554a08.md#insn-00554a5c)
- 新版 `00577aa4`（命令位置の公開資料なし） · `005778ec`（命令位置の公開資料なし） · `005778f4`（命令位置の公開資料なし）

~~~diff
- 00554c0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3b0:8"]]
- 00554c0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00577aa4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00577aa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00554c0c bytes 09d901f9
+ 00577aa4 bytes 093907f9
- 00554a54 ["INT_ADD", "register:40f0:8", ["const:554a54:8", "const:4:8"]]
- 00554a54 ["CALL", null, ["callee:00588e2c:8"]]
+ 005778ec ["INT_ADD", "register:40f0:8", ["const:5778ec:8", "const:4:8"]]
+ 005778ec ["CALL", null, ["callee:00588e2c:8"]]
- 00554a54 bytes 50450094
+ 005778ec bytes 50450094
- 00554a5c ["INT_ADD", "register:40f0:8", ["const:554a5c:8", "const:4:8"]]
- 00554a5c ["CALL", null, ["callee:0058911c:8"]]
+ 005778f4 ["INT_ADD", "register:40f0:8", ["const:5778f4:8", "const:4:8"]]
+ 005778f4 ["CALL", null, ["callee:0058911c:8"]]
- 00554a5c bytes 0a460094
+ 005778f4 bytes 0a460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cddf74649f57f149e087b6a9707f3d5a"></a>

### [`00554da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554da8.md) → [`00577c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577c40.md) FUN_00577c40

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00553ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553ac4.md) [`00554030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554030.md) [`005541a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/005541a8.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057695c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057695c.md) [`00576ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576ec8.md) [`00577040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577040.md)

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
    "old": {
      "definition_site": "00554f00",
      "incomplete_value": false,
      "site": "00554f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
    "old": {
      "definition_site": "00554fac",
      "incomplete_value": true,
      "site": "00554fac",
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
            "const:3b0:8"
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
    "old": {
      "definition_site": "00554fa8",
      "incomplete_value": true,
      "site": "00554fa8",
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
      "00577cac",
      "READ",
      [
        "storage",
        "002a9754",
        null,
        "string"
      ]
    ],
    [
      "00577d88",
      "DATA",
      [
        "storage",
        "00beeec0",
        null,
        "undefined *"
      ]
    ],
    [
      "00577d98",
      "DATA",
      [
        "storage",
        "00beeba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577cac",
      "READ",
      [
        "storage",
        "002ba3f7",
        null,
        "string"
      ]
    ],
    [
      "00577d88",
      "DATA",
      [
        "storage",
        "00c6ba80",
        null,
        "undefined *"
      ]
    ],
    [
      "00577d98",
      "DATA",
      [
        "storage",
        "00c6b760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00554fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554da8.md#insn-00554fac) · [`00554df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554da8.md#insn-00554df4) · [`00554dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00554/00554da8.md#insn-00554dfc)
- 新版 `00577e44`（命令位置の公開資料なし） · `00577c8c`（命令位置の公開資料なし） · `00577c94`（命令位置の公開資料なし）

~~~diff
- 00554fac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3b0:8"]]
- 00554fac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00577e44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00577e44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00554fac bytes 09d901f9
+ 00577e44 bytes 093907f9
- 00554df4 ["INT_ADD", "register:40f0:8", ["const:554df4:8", "const:4:8"]]
- 00554df4 ["CALL", null, ["callee:00588e2c:8"]]
+ 00577c8c ["INT_ADD", "register:40f0:8", ["const:577c8c:8", "const:4:8"]]
+ 00577c8c ["CALL", null, ["callee:00588e2c:8"]]
- 00554df4 bytes 68440094
+ 00577c8c bytes 68440094
- 00554dfc ["INT_ADD", "register:40f0:8", ["const:554dfc:8", "const:4:8"]]
- 00554dfc ["CALL", null, ["callee:0058911c:8"]]
+ 00577c94 ["INT_ADD", "register:40f0:8", ["const:577c94:8", "const:4:8"]]
+ 00577c94 ["CALL", null, ["callee:0058911c:8"]]
- 00554dfc bytes 22450094
+ 00577c94 bytes 22450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a57b95a318b79c52676f13c4f551f6d"></a>

### [`00555148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555148.md) → [`00577fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00577/00577fe0.md) FUN_00577fe0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005552ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/005552ec.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00559348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559348.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00578184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578184.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`0057c1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1e0.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

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
    "old": {
      "definition_site": "00555174",
      "incomplete_value": false,
      "site": "00555178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c48:8"
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
      "00578010",
      "DATA",
      [
        "storage",
        "00beec48",
        null,
        "undefined *"
      ]
    ],
    [
      "00578034",
      "READ",
      [
        "storage",
        "002939f5",
        null,
        "string"
      ]
    ],
    [
      "005780d4",
      "PARAM",
      [
        "storage",
        "00c263b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00578010",
      "DATA",
      [
        "storage",
        "00c6b808",
        null,
        "undefined *"
      ]
    ],
    [
      "00578034",
      "READ",
      [
        "storage",
        "002a31ee",
        null,
        "string"
      ]
    ],
    [
      "005780d4",
      "PARAM",
      [
        "storage",
        "00ca5e70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555148.md#insn-00555170) · [`00555174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555148.md#insn-00555174) · [`0055517c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555148.md#insn-0055517c)
- 新版 `00578008`（命令位置の公開資料なし） · `0057800c`（命令位置の公開資料なし） · `00578014`（命令位置の公開資料なし）

~~~diff
- 00555170 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00578008 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00555170 bytes c83400b0
+ 00578008 bytes 883700f0
- 00555174 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 00555174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00555174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00555174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057800c ["COPY", "tmp:0:8", ["const:808:8"]]
+ 0057800c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057800c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057800c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00555174 bytes 08213191
+ 0057800c bytes 08212091
- 0055517c ["INT_ADD", "register:40f0:8", ["const:55517c:8", "const:4:8"]]
- 0055517c ["CALL", null, ["callee:00588e2c:8"]]
+ 00578014 ["INT_ADD", "register:40f0:8", ["const:578014:8", "const:4:8"]]
+ 00578014 ["CALL", null, ["callee:00588e2c:8"]]
- 0055517c bytes 86430094
+ 00578014 bytes 86430094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6a067111ec7021b5929c2180bea9581"></a>

### [`00555484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555484.md) → [`0057831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/0057831c.md) FUN_0057831c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md)

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
    "old": {
      "definition_site": "005554f0",
      "incomplete_value": true,
      "site": "005554f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5ec:8"
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
    "old": {
      "definition_site": "00555508",
      "incomplete_value": true,
      "site": "00555518",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:76a:8"
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
    "old": {
      "definition_site": "0055551c",
      "incomplete_value": true,
      "site": "0055551c",
      "value": [
        "LOAD",
        "8",
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
      "00578374",
      "READ",
      [
        "storage",
        "0029d5ec",
        null,
        "string"
      ]
    ],
    [
      "005783a0",
      "READ",
      [
        "storage",
        "002a576a",
        null,
        "string"
      ]
    ],
    [
      "005783a4",
      "READ",
      [
        "storage",
        "002a5779",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578374",
      "READ",
      [
        "storage",
        "002ad876",
        null,
        "string"
      ]
    ],
    [
      "005783a0",
      "READ",
      [
        "storage",
        "002b6198",
        null,
        "string"
      ]
    ],
    [
      "005783a4",
      "READ",
      [
        "storage",
        "002b61a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055557c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555484.md#insn-0055557c) · [`005556ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555484.md#insn-005556ac) · [`005554bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555484.md#insn-005554bc)
- 新版 `00578414`（命令位置の公開資料なし） · `00578544`（命令位置の公開資料なし） · `00578354`（命令位置の公開資料なし）

~~~diff
- 0055557c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a8:8"]]
- 0055557c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:4"]]
+ 00578414 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e68:8"]]
+ 00578414 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:4"]]
- 0055557c bytes 16a903b9
+ 00578414 bytes 16690eb9
- 005556ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
- 005556ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00578544 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e50:8"]]
+ 00578544 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005556ac bytes 09c901f9
+ 00578544 bytes 092907f9
- 005554bc ["INT_ADD", "register:40f0:8", ["const:5554bc:8", "const:4:8"]]
- 005554bc ["CALL", null, ["callee:00588e2c:8"]]
+ 00578354 ["INT_ADD", "register:40f0:8", ["const:578354:8", "const:4:8"]]
+ 00578354 ["CALL", null, ["callee:00588e2c:8"]]
- 005554bc bytes b6420094
+ 00578354 bytes b6420094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-922abf2ab11a396ccc875dbce862bb0f"></a>

### [`005558b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/005558b8.md) → [`00578750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578750.md) FUN_00578750

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

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
    "old": {
      "definition_site": "00555914",
      "incomplete_value": true,
      "site": "00555914",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5ec:8"
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
    "old": {
      "definition_site": "00555928",
      "incomplete_value": true,
      "site": "00555930",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bb2:8"
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
    "old": {
      "definition_site": "00555934",
      "incomplete_value": true,
      "site": "00555934",
      "value": [
        "LOAD",
        "8",
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
      "0057879c",
      "READ",
      [
        "storage",
        "0029d5ec",
        null,
        "string"
      ]
    ],
    [
      "005787c0",
      "READ",
      [
        "storage",
        "00296bb2",
        null,
        "string"
      ]
    ],
    [
      "005787c4",
      "READ",
      [
        "storage",
        "00296bc0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057879c",
      "READ",
      [
        "storage",
        "002ad876",
        null,
        "string"
      ]
    ],
    [
      "005787c0",
      "READ",
      [
        "storage",
        "002a66e7",
        null,
        "string"
      ]
    ],
    [
      "005787c4",
      "READ",
      [
        "storage",
        "002a66f5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005558e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/005558b8.md#insn-005558e0) · [`005558e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/005558b8.md#insn-005558e8) · [`005558fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/005558b8.md#insn-005558fc)
- 新版 `00578778`（命令位置の公開資料なし） · `00578780`（命令位置の公開資料なし） · `00578794`（命令位置の公開資料なし）

~~~diff
- 005558e0 ["INT_ADD", "register:40f0:8", ["const:5558e0:8", "const:4:8"]]
- 005558e0 ["CALL", null, ["callee:00588e2c:8"]]
+ 00578778 ["INT_ADD", "register:40f0:8", ["const:578778:8", "const:4:8"]]
+ 00578778 ["CALL", null, ["callee:00588e2c:8"]]
- 005558e0 bytes ad410094
+ 00578778 bytes ad410094
- 005558e8 ["INT_ADD", "register:40f0:8", ["const:5558e8:8", "const:4:8"]]
- 005558e8 ["CALL", null, ["callee:0058911c:8"]]
+ 00578780 ["INT_ADD", "register:40f0:8", ["const:578780:8", "const:4:8"]]
+ 00578780 ["CALL", null, ["callee:0058911c:8"]]
- 005558e8 bytes 67420094
+ 00578780 bytes 67420094
- 005558fc ["COPY", "register:4040:8", ["const:29d000:8"]]
+ 00578794 ["COPY", "register:4040:8", ["const:2ad000:8"]]
- 005558fc bytes 48eaff90
+ 00578794 bytes a8e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19e4f1473922c38f556d1d4c38c005d2"></a>

### [`00555a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555a38.md) → [`005788d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/005788d0.md) FUN_005788d0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

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
    "old": {
      "definition_site": "00555a90",
      "incomplete_value": true,
      "site": "00555a90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:526:8"
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
    "old": {
      "definition_site": "00555a98",
      "incomplete_value": true,
      "site": "00555a98",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "00555a94",
      "incomplete_value": true,
      "site": "00555aa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:782:8"
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
      "00578910",
      "READ",
      [
        "storage",
        "0029b526",
        null,
        "string"
      ]
    ],
    [
      "00578918",
      "READ",
      [
        "storage",
        "0029b52b",
        null,
        "string"
      ]
    ],
    [
      "0057892c",
      "READ",
      [
        "storage",
        "002a5782",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578910",
      "READ",
      [
        "storage",
        "002ab594",
        null,
        "string"
      ]
    ],
    [
      "00578918",
      "READ",
      [
        "storage",
        "002ab599",
        null,
        "string"
      ]
    ],
    [
      "0057892c",
      "READ",
      [
        "storage",
        "002b61b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555a38.md#insn-00555a60) · [`00555a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555a38.md#insn-00555a68) · [`00555a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555a38.md#insn-00555a70)
- 新版 `005788f8`（命令位置の公開資料なし） · `00578900`（命令位置の公開資料なし） · `00578908`（命令位置の公開資料なし）

~~~diff
- 00555a60 ["INT_ADD", "register:40f0:8", ["const:555a60:8", "const:4:8"]]
- 00555a60 ["CALL", null, ["callee:00588e2c:8"]]
+ 005788f8 ["INT_ADD", "register:40f0:8", ["const:5788f8:8", "const:4:8"]]
+ 005788f8 ["CALL", null, ["callee:00588e2c:8"]]
- 00555a60 bytes 4d410094
+ 005788f8 bytes 4d410094
- 00555a68 ["INT_ADD", "register:40f0:8", ["const:555a68:8", "const:4:8"]]
- 00555a68 ["CALL", null, ["callee:0058911c:8"]]
+ 00578900 ["INT_ADD", "register:40f0:8", ["const:578900:8", "const:4:8"]]
+ 00578900 ["CALL", null, ["callee:0058911c:8"]]
- 00555a68 bytes 07420094
+ 00578900 bytes 07420094
- 00555a70 ["COPY", "register:4048:8", ["const:29b000:8"]]
+ 00578908 ["COPY", "register:4048:8", ["const:2ab000:8"]]
- 00555a70 bytes 29eaffd0
+ 00578908 bytes 89e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea9731d5a414153ce6f16c95205774ac"></a>

### [`00555bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555bd4.md) → [`00578a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578a6c.md) FUN_00578a6c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

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
    "old": {
      "definition_site": "00555c20",
      "incomplete_value": true,
      "site": "00555c20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef7:8"
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
    "old": {
      "definition_site": "00555c24",
      "incomplete_value": true,
      "site": "00555c24",
      "value": [
        "LOAD",
        "8",
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
      "00578aa8",
      "READ",
      [
        "storage",
        "00298ef7",
        null,
        "string"
      ]
    ],
    [
      "00578ab0",
      "READ",
      [
        "storage",
        "00298efc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578aa8",
      "READ",
      [
        "storage",
        "002a8cb5",
        null,
        "string"
      ]
    ],
    [
      "00578ab0",
      "READ",
      [
        "storage",
        "002a8cba",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555bd4.md#insn-00555bf8) · [`00555c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555bd4.md#insn-00555c00) · [`00555c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555bd4.md#insn-00555c08)
- 新版 `00578a90`（命令位置の公開資料なし） · `00578a98`（命令位置の公開資料なし） · `00578aa0`（命令位置の公開資料なし）

~~~diff
- 00555bf8 ["INT_ADD", "register:40f0:8", ["const:555bf8:8", "const:4:8"]]
- 00555bf8 ["CALL", null, ["callee:00588e2c:8"]]
+ 00578a90 ["INT_ADD", "register:40f0:8", ["const:578a90:8", "const:4:8"]]
+ 00578a90 ["CALL", null, ["callee:00588e2c:8"]]
- 00555bf8 bytes e7400094
+ 00578a90 bytes e7400094
- 00555c00 ["INT_ADD", "register:40f0:8", ["const:555c00:8", "const:4:8"]]
- 00555c00 ["CALL", null, ["callee:0058911c:8"]]
+ 00578a98 ["INT_ADD", "register:40f0:8", ["const:578a98:8", "const:4:8"]]
+ 00578a98 ["CALL", null, ["callee:0058911c:8"]]
- 00555c00 bytes a1410094
+ 00578a98 bytes a1410094
- 00555c08 ["COPY", "register:4048:8", ["const:298000:8"]]
+ 00578aa0 ["COPY", "register:4048:8", ["const:2a8000:8"]]
- 00555c08 bytes 09eafff0
+ 00578aa0 bytes 89e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57c66a93b9bd6b91310559b9378f16de"></a>

### [`00555d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555d04.md) → [`00578b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578b9c.md) FUN_00578b9c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "00555d50",
      "incomplete_value": true,
      "site": "00555d50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:766:8"
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
    "old": {
      "definition_site": "00555d54",
      "incomplete_value": true,
      "site": "00555d54",
      "value": [
        "LOAD",
        "8",
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
      "00578bd8",
      "READ",
      [
        "storage",
        "002a0766",
        null,
        "string"
      ]
    ],
    [
      "00578be0",
      "READ",
      [
        "storage",
        "002a076b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578bd8",
      "READ",
      [
        "storage",
        "002b0d20",
        null,
        "string"
      ]
    ],
    [
      "00578be0",
      "READ",
      [
        "storage",
        "002b0d25",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555d04.md#insn-00555d28) · [`00555d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555d04.md#insn-00555d30) · [`00555d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555d04.md#insn-00555d38)
- 新版 `00578bc0`（命令位置の公開資料なし） · `00578bc8`（命令位置の公開資料なし） · `00578bd0`（命令位置の公開資料なし）

~~~diff
- 00555d28 ["INT_ADD", "register:40f0:8", ["const:555d28:8", "const:4:8"]]
- 00555d28 ["CALL", null, ["callee:00588e2c:8"]]
+ 00578bc0 ["INT_ADD", "register:40f0:8", ["const:578bc0:8", "const:4:8"]]
+ 00578bc0 ["CALL", null, ["callee:00588e2c:8"]]
- 00555d28 bytes 9b400094
+ 00578bc0 bytes 9b400094
- 00555d30 ["INT_ADD", "register:40f0:8", ["const:555d30:8", "const:4:8"]]
- 00555d30 ["CALL", null, ["callee:0058911c:8"]]
+ 00578bc8 ["INT_ADD", "register:40f0:8", ["const:578bc8:8", "const:4:8"]]
+ 00578bc8 ["CALL", null, ["callee:0058911c:8"]]
- 00555d30 bytes 55410094
+ 00578bc8 bytes 55410094
- 00555d38 ["COPY", "register:4048:8", ["const:2a0000:8"]]
+ 00578bd0 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00555d38 bytes 49eafff0
+ 00578bd0 bytes c9e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f62a6ab58934a7c67605029d3c698323"></a>

### [`00555e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555e74.md) → [`00578d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578d0c.md) FUN_00578d0c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "00555ec0",
      "incomplete_value": true,
      "site": "00555ec0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c4:8"
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
    "old": {
      "definition_site": "00555ec4",
      "incomplete_value": true,
      "site": "00555ec4",
      "value": [
        "LOAD",
        "8",
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
      "00578d48",
      "READ",
      [
        "storage",
        "002a35c4",
        null,
        "string"
      ]
    ],
    [
      "00578d50",
      "READ",
      [
        "storage",
        "002a35c9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578d48",
      "READ",
      [
        "storage",
        "002b3c9e",
        null,
        "string"
      ]
    ],
    [
      "00578d50",
      "READ",
      [
        "storage",
        "002b3ca3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00555e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555e74.md#insn-00555e98) · [`00555ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555e74.md#insn-00555ea0) · [`00555ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555e74.md#insn-00555ea8)
- 新版 `00578d30`（命令位置の公開資料なし） · `00578d38`（命令位置の公開資料なし） · `00578d40`（命令位置の公開資料なし）

~~~diff
- 00555e98 ["INT_ADD", "register:40f0:8", ["const:555e98:8", "const:4:8"]]
- 00555e98 ["CALL", null, ["callee:00588e2c:8"]]
+ 00578d30 ["INT_ADD", "register:40f0:8", ["const:578d30:8", "const:4:8"]]
+ 00578d30 ["CALL", null, ["callee:00588e2c:8"]]
- 00555e98 bytes 3f400094
+ 00578d30 bytes 3f400094
- 00555ea0 ["INT_ADD", "register:40f0:8", ["const:555ea0:8", "const:4:8"]]
- 00555ea0 ["CALL", null, ["callee:0058911c:8"]]
+ 00578d38 ["INT_ADD", "register:40f0:8", ["const:578d38:8", "const:4:8"]]
+ 00578d38 ["CALL", null, ["callee:0058911c:8"]]
- 00555ea0 bytes f9400094
+ 00578d38 bytes f9400094
- 00555ea8 ["COPY", "register:4048:8", ["const:2a3000:8"]]
+ 00578d40 ["COPY", "register:4048:8", ["const:2b3000:8"]]
- 00555ea8 bytes 69eaffd0
+ 00578d40 bytes c9e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d0242d9a01f0c23024ac01a56a491e8"></a>

### [`00555fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555fe4.md) → [`00578e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578e7c.md) FUN_00578e7c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0055664c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/0055664c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005794e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/005794e4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

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
    "old": {
      "definition_site": "00556144",
      "incomplete_value": true,
      "site": "00556144",
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
            "const:378:8"
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
    "old": {
      "definition_site": "005563b8",
      "incomplete_value": true,
      "site": "005563b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5f8:8"
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
    "old": {
      "definition_site": "005563bc",
      "incomplete_value": true,
      "site": "005563bc",
      "value": [
        "LOAD",
        "8",
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
      "00578f58",
      "READ",
      [
        "storage",
        "00c26380",
        null,
        "undefined8"
      ]
    ],
    [
      "00578fbc",
      "DATA",
      [
        "storage",
        "00c26380",
        null,
        "undefined8"
      ]
    ],
    [
      "00578fcc",
      "WRITE",
      [
        "storage",
        "00c26380",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00578f58",
      "READ",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "00578fbc",
      "DATA",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "00578fcc",
      "WRITE",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00556144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555fe4.md#insn-00556144) · [`00556040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555fe4.md#insn-00556040) · [`0055606c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555fe4.md#insn-0055606c)
- 新版 `00578fdc`（命令位置の公開資料なし） · `00578ed8`（命令位置の公開資料なし） · `00578f04`（命令位置の公開資料なし）

~~~diff
- 00556144 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
- 00556144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00578fdc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e38:8"]]
+ 00578fdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00556144 bytes 09bd01f9
+ 00578fdc bytes 091d07f9
- 00556040 ["COPY", "register:0:8", ["register:4048:8"]]
- 00556040 ["INT_ADD", "register:40f0:8", ["const:556040:8", "const:4:8"]]
- 00556040 ["CALLIND", null, ["register:0:8"]]
+ 00578ed8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00578ed8 ["INT_ADD", "register:40f0:8", ["const:578ed8:8", "const:4:8"]]
+ 00578ed8 ["CALLIND", null, ["register:0:8"]]
- 00556040 bytes 20013fd6
+ 00578ed8 bytes 20013fd6
- 0055606c ["COPY", "register:0:8", ["register:4040:8"]]
- 0055606c ["INT_ADD", "register:40f0:8", ["const:55606c:8", "const:4:8"]]
- 0055606c ["CALLIND", null, ["register:0:8"]]
+ 00578f04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00578f04 ["INT_ADD", "register:40f0:8", ["const:578f04:8", "const:4:8"]]
+ 00578f04 ["CALLIND", null, ["register:0:8"]]
- 0055606c bytes 00013fd6
+ 00578f04 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c8c03eb7dad4cd9ac3482054aaec896"></a>

### [`0055664c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/0055664c.md) → [`005794e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/005794e4.md) FUN_005794e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00555fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00555/00555fe4.md) · 呼出先 11件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00574784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574784.md) [`00574810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574810.md) [`00574bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bb4.md) [`00574bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bbc.md)
- 新版 呼出元 1件 [`00578e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00578/00578e7c.md) · 呼出先 11件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0059761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md) [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md) [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`00597a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a54.md)

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
    "old": {
      "definition_site": "00556788",
      "incomplete_value": false,
      "site": "00556790",
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
            "const:bdc:8"
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
    "old": {
      "definition_site": "005567ec",
      "incomplete_value": false,
      "site": "005567f4",
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
            "const:774:8"
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
    "old": {
      "definition_site": "00556850",
      "incomplete_value": false,
      "site": "00556858",
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
            "const:534:8"
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
      "00579620",
      "PARAM",
      [
        "storage",
        "00290bdc",
        null,
        "string"
      ]
    ],
    [
      "00579684",
      "PARAM",
      [
        "storage",
        "002a0774",
        null,
        "string"
      ]
    ],
    [
      "005796e8",
      "PARAM",
      [
        "storage",
        "0029b534",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00579620",
      "PARAM",
      [
        "storage",
        "002a011e",
        null,
        "string"
      ]
    ],
    [
      "00579684",
      "PARAM",
      [
        "storage",
        "002b0d2e",
        null,
        "string"
      ]
    ],
    [
      "005796e8",
      "PARAM",
      [
        "storage",
        "002ab5a2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00556790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/0055664c.md#insn-00556790) · [`005567f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/0055664c.md#insn-005567f4) · [`00556858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/0055664c.md#insn-00556858)
- 新版 `00579628`（命令位置の公開資料なし） · `0057968c`（命令位置の公開資料なし） · `005796f0`（命令位置の公開資料なし）

~~~diff
- 00556790 ["INT_ADD", "register:40f0:8", ["const:556790:8", "const:4:8"]]
- 00556790 ["CALL", null, ["callee:00c57b70:8"]]
+ 00579628 ["INT_ADD", "register:40f0:8", ["const:579628:8", "const:4:8"]]
+ 00579628 ["CALL", null, ["callee:00c57b70:8"]]
- 00556790 bytes 64121a94
+ 00579628 bytes 52791b94
- 005567f4 ["INT_ADD", "register:40f0:8", ["const:5567f4:8", "const:4:8"]]
- 005567f4 ["CALL", null, ["callee:00c57b70:8"]]
+ 0057968c ["INT_ADD", "register:40f0:8", ["const:57968c:8", "const:4:8"]]
+ 0057968c ["CALL", null, ["callee:00c57b70:8"]]
- 005567f4 bytes 4b121a94
+ 0057968c bytes 39791b94
- 00556858 ["INT_ADD", "register:40f0:8", ["const:556858:8", "const:4:8"]]
- 00556858 ["CALL", null, ["callee:00c57b70:8"]]
+ 005796f0 ["INT_ADD", "register:40f0:8", ["const:5796f0:8", "const:4:8"]]
+ 005796f0 ["CALL", null, ["callee:00c57b70:8"]]
- 00556858 bytes 32121a94
+ 005796f0 bytes 20791b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bfead71d07e352ef202fa680e85a668"></a>

### [`00556bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/00556bf4.md) → [`00579a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/00579a8c.md) FUN_00579a8c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

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
    "old": {
      "definition_site": "00556d50",
      "incomplete_value": true,
      "site": "00556d50",
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
            "const:378:8"
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
    "old": {
      "definition_site": "00556ef0",
      "incomplete_value": true,
      "site": "00556ef0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5f8:8"
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
    "old": {
      "definition_site": "00556ef8",
      "incomplete_value": true,
      "site": "00556ef8",
      "value": [
        "LOAD",
        "8",
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
      "00579b64",
      "READ",
      [
        "storage",
        "00c26380",
        null,
        "undefined8"
      ]
    ],
    [
      "00579bc8",
      "DATA",
      [
        "storage",
        "00c26380",
        null,
        "undefined8"
      ]
    ],
    [
      "00579bd8",
      "WRITE",
      [
        "storage",
        "00c26380",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00579b64",
      "READ",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "00579bc8",
      "DATA",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "00579bd8",
      "WRITE",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00556d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/00556bf4.md#insn-00556d50) · [`00556c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/00556bf4.md#insn-00556c4c) · [`00556c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/00556bf4.md#insn-00556c78)
- 新版 `00579be8`（命令位置の公開資料なし） · `00579ae4`（命令位置の公開資料なし） · `00579b10`（命令位置の公開資料なし）

~~~diff
- 00556d50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
- 00556d50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00579be8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e38:8"]]
+ 00579be8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00556d50 bytes 09bd01f9
+ 00579be8 bytes 091d07f9
- 00556c4c ["COPY", "register:0:8", ["register:4048:8"]]
- 00556c4c ["INT_ADD", "register:40f0:8", ["const:556c4c:8", "const:4:8"]]
- 00556c4c ["CALLIND", null, ["register:0:8"]]
+ 00579ae4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00579ae4 ["INT_ADD", "register:40f0:8", ["const:579ae4:8", "const:4:8"]]
+ 00579ae4 ["CALLIND", null, ["register:0:8"]]
- 00556c4c bytes 20013fd6
+ 00579ae4 bytes 20013fd6
- 00556c78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00556c78 ["INT_ADD", "register:40f0:8", ["const:556c78:8", "const:4:8"]]
- 00556c78 ["CALLIND", null, ["register:0:8"]]
+ 00579b10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00579b10 ["INT_ADD", "register:40f0:8", ["const:579b10:8", "const:4:8"]]
+ 00579b10 ["CALLIND", null, ["register:0:8"]]
- 00556c78 bytes 00013fd6
+ 00579b10 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8806a033b7df5b423acbc2e713259192"></a>

### [`00557264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557264.md) → [`0057a0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a0fc.md) FUN_0057a0fc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

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
    "old": {
      "definition_site": "005572c8",
      "incomplete_value": true,
      "site": "005572c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5d2:8"
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
    "old": {
      "definition_site": "005572cc",
      "incomplete_value": true,
      "site": "005572cc",
      "value": [
        "LOAD",
        "8",
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
      "0057a150",
      "READ",
      [
        "storage",
        "002a35d2",
        null,
        "string"
      ]
    ],
    [
      "0057a158",
      "READ",
      [
        "storage",
        "002a35d7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a150",
      "READ",
      [
        "storage",
        "002b3cac",
        null,
        "string"
      ]
    ],
    [
      "0057a158",
      "READ",
      [
        "storage",
        "002b3cb1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005572a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557264.md#insn-005572a0) · [`005572a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557264.md#insn-005572a8) · [`005572b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557264.md#insn-005572b0)
- 新版 `0057a138`（命令位置の公開資料なし） · `0057a140`（命令位置の公開資料なし） · `0057a148`（命令位置の公開資料なし）

~~~diff
- 005572a0 ["INT_ADD", "register:40f0:8", ["const:5572a0:8", "const:4:8"]]
- 005572a0 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057a138 ["INT_ADD", "register:40f0:8", ["const:57a138:8", "const:4:8"]]
+ 0057a138 ["CALL", null, ["callee:00588e2c:8"]]
- 005572a0 bytes 3d3b0094
+ 0057a138 bytes 3d3b0094
- 005572a8 ["INT_ADD", "register:40f0:8", ["const:5572a8:8", "const:4:8"]]
- 005572a8 ["CALL", null, ["callee:0058911c:8"]]
+ 0057a140 ["INT_ADD", "register:40f0:8", ["const:57a140:8", "const:4:8"]]
+ 0057a140 ["CALL", null, ["callee:0058911c:8"]]
- 005572a8 bytes f73b0094
+ 0057a140 bytes f73b0094
- 005572b0 ["COPY", "register:4048:8", ["const:2a3000:8"]]
+ 0057a148 ["COPY", "register:4048:8", ["const:2b3000:8"]]
- 005572b0 bytes 69eaff90
+ 0057a148 bytes c9e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43018bbbbda274b1186f046592a44ce8"></a>

### [`005574b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/005574b4.md) → [`0057a34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a34c.md) FUN_0057a34c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "00557508",
      "incomplete_value": true,
      "site": "00557508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:75e:8"
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
    "old": {
      "definition_site": "0055750c",
      "incomplete_value": true,
      "site": "0055750c",
      "value": [
        "LOAD",
        "8",
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
      "0057a390",
      "READ",
      [
        "storage",
        "002a975e",
        null,
        "string"
      ]
    ],
    [
      "0057a398",
      "READ",
      [
        "storage",
        "002a9764",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a390",
      "READ",
      [
        "storage",
        "002ba401",
        null,
        "string"
      ]
    ],
    [
      "0057a398",
      "READ",
      [
        "storage",
        "002ba407",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005574e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/005574b4.md#insn-005574e0) · [`005574e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/005574b4.md#insn-005574e8) · [`005574f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/005574b4.md#insn-005574f0)
- 新版 `0057a378`（命令位置の公開資料なし） · `0057a380`（命令位置の公開資料なし） · `0057a388`（命令位置の公開資料なし）

~~~diff
- 005574e0 ["INT_ADD", "register:40f0:8", ["const:5574e0:8", "const:4:8"]]
- 005574e0 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057a378 ["INT_ADD", "register:40f0:8", ["const:57a378:8", "const:4:8"]]
+ 0057a378 ["CALL", null, ["callee:00588e2c:8"]]
- 005574e0 bytes ad3a0094
+ 0057a378 bytes ad3a0094
- 005574e8 ["INT_ADD", "register:40f0:8", ["const:5574e8:8", "const:4:8"]]
- 005574e8 ["CALL", null, ["callee:0058911c:8"]]
+ 0057a380 ["INT_ADD", "register:40f0:8", ["const:57a380:8", "const:4:8"]]
+ 0057a380 ["CALL", null, ["callee:0058911c:8"]]
- 005574e8 bytes 673b0094
+ 0057a380 bytes 673b0094
- 005574f0 ["COPY", "register:4048:8", ["const:2a9000:8"]]
+ 0057a388 ["COPY", "register:4048:8", ["const:2ba000:8"]]
- 005574f0 bytes 89eaffd0
+ 0057a388 bytes 09eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28bc29d199170123db5e9767546eee40"></a>

### [`005575ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/005575ec.md) → [`0057a484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a484.md) FUN_0057a484

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "00557640",
      "incomplete_value": true,
      "site": "00557640",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:92a:8"
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
    "old": {
      "definition_site": "00557644",
      "incomplete_value": true,
      "site": "00557644",
      "value": [
        "LOAD",
        "8",
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
      "0057a4c8",
      "READ",
      [
        "storage",
        "002a692a",
        null,
        "string"
      ]
    ],
    [
      "0057a4d0",
      "READ",
      [
        "storage",
        "002a6930",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a4c8",
      "READ",
      [
        "storage",
        "002b741b",
        null,
        "string"
      ]
    ],
    [
      "0057a4d0",
      "READ",
      [
        "storage",
        "002b7421",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00557618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/005575ec.md#insn-00557618) · [`00557620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/005575ec.md#insn-00557620) · [`00557628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/005575ec.md#insn-00557628)
- 新版 `0057a4b0`（命令位置の公開資料なし） · `0057a4b8`（命令位置の公開資料なし） · `0057a4c0`（命令位置の公開資料なし）

~~~diff
- 00557618 ["INT_ADD", "register:40f0:8", ["const:557618:8", "const:4:8"]]
- 00557618 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057a4b0 ["INT_ADD", "register:40f0:8", ["const:57a4b0:8", "const:4:8"]]
+ 0057a4b0 ["CALL", null, ["callee:00588e2c:8"]]
- 00557618 bytes 5f3a0094
+ 0057a4b0 bytes 5f3a0094
- 00557620 ["INT_ADD", "register:40f0:8", ["const:557620:8", "const:4:8"]]
- 00557620 ["CALL", null, ["callee:0058911c:8"]]
+ 0057a4b8 ["INT_ADD", "register:40f0:8", ["const:57a4b8:8", "const:4:8"]]
+ 0057a4b8 ["CALL", null, ["callee:0058911c:8"]]
- 00557620 bytes 193b0094
+ 0057a4b8 bytes 193b0094
- 00557628 ["COPY", "register:4048:8", ["const:2a6000:8"]]
+ 0057a4c0 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 00557628 bytes 69eafff0
+ 0057a4c0 bytes e9e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2753622598e4b9f64b52a22267f09678"></a>

### [`00557724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557724.md) → [`0057a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a5bc.md) FUN_0057a5bc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00559458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559458.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0057c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "0055775c",
      "incomplete_value": false,
      "site": "00557770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00557764",
      "incomplete_value": false,
      "site": "00557770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:de0:8"
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
      "0057a5f4",
      "PARAM",
      [
        "storage",
        "00beedc8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057a5fc",
      "PARAM",
      [
        "storage",
        "00beede0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0057a5f4",
      "PARAM",
      [
        "storage",
        "00c6b988",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057a5fc",
      "PARAM",
      [
        "storage",
        "00c6b9a0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00557770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557724.md#insn-00557770) · [`00557758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557724.md#insn-00557758) · [`0055775c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557724.md#insn-0055775c)
- 新版 `0057a608`（命令位置の公開資料なし） · `0057a5f0`（命令位置の公開資料なし） · `0057a5f4`（命令位置の公開資料なし）

~~~diff
- 00557770 ["INT_ADD", "register:40f0:8", ["const:557770:8", "const:4:8"]]
- 00557770 ["CALL", null, ["callee:00c58210:8"]]
+ 0057a608 ["INT_ADD", "register:40f0:8", ["const:57a608:8", "const:4:8"]]
+ 0057a608 ["CALL", null, ["callee:00c58210:8"]]
- 00557770 bytes 14101a94
+ 0057a608 bytes 02771b94
- 00557758 ["COPY", "register:4008:8", ["const:bee000:8"]]
+ 0057a5f0 ["COPY", "register:4008:8", ["const:c6b000:8"]]
- 00557758 bytes a13400f0
+ 0057a5f0 bytes 813700b0
- 0055775c ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 0055775c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0055775c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0055775c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0057a5f4 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 0057a5f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0057a5f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0057a5f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0055775c bytes 21203791
+ 0057a5f4 bytes 21202691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e70b662401bb190f349120413de3e979"></a>

### [`00557864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557864.md) → [`0057a6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a6fc.md) FUN_0057a6fc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db34.md) · 呼出先 8件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 1件 [`005509cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509cc.md) · 呼出先 8件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "005578e0",
      "incomplete_value": true,
      "site": "005578e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:768:8"
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
    "old": {
      "definition_site": "00557904",
      "incomplete_value": true,
      "site": "00557904",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:76c:8"
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
    "old": {
      "definition_site": "005579c4",
      "incomplete_value": false,
      "site": "005579cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
      "0057a76c",
      "READ",
      [
        "storage",
        "002aa768",
        null,
        "string"
      ]
    ],
    [
      "0057a798",
      "READ",
      [
        "storage",
        "002a176c",
        null,
        "string"
      ]
    ],
    [
      "0057a864",
      "DATA",
      [
        "storage",
        "00beef60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a76c",
      "READ",
      [
        "storage",
        "002bb4e4",
        null,
        "string"
      ]
    ],
    [
      "0057a798",
      "READ",
      [
        "storage",
        "002b1db8",
        null,
        "string"
      ]
    ],
    [
      "0057a864",
      "DATA",
      [
        "storage",
        "00c6bb20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005578b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557864.md#insn-005578b0) · [`005578b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557864.md#insn-005578b8) · [`005578cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557864.md#insn-005578cc)
- 新版 `0057a748`（命令位置の公開資料なし） · `0057a750`（命令位置の公開資料なし） · `0057a764`（命令位置の公開資料なし）

~~~diff
- 005578b0 ["INT_ADD", "register:40f0:8", ["const:5578b0:8", "const:4:8"]]
- 005578b0 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057a748 ["INT_ADD", "register:40f0:8", ["const:57a748:8", "const:4:8"]]
+ 0057a748 ["CALL", null, ["callee:00588e2c:8"]]
- 005578b0 bytes b9390094
+ 0057a748 bytes b9390094
- 005578b8 ["INT_ADD", "register:40f0:8", ["const:5578b8:8", "const:4:8"]]
- 005578b8 ["CALL", null, ["callee:0058911c:8"]]
+ 0057a750 ["INT_ADD", "register:40f0:8", ["const:57a750:8", "const:4:8"]]
+ 0057a750 ["CALL", null, ["callee:0058911c:8"]]
- 005578b8 bytes 733a0094
+ 0057a750 bytes 733a0094
- 005578cc ["COPY", "register:4040:8", ["const:2aa000:8"]]
+ 0057a764 ["COPY", "register:4040:8", ["const:2bb000:8"]]
- 005578cc bytes 88eafff0
+ 0057a764 bytes 08eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c37ddfb23886f0316566bea171f0ea54"></a>

### [`00557a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557a90.md) → [`0057a928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a928.md) FUN_0057a928

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
    "old": {
      "definition_site": "00557aac",
      "incomplete_value": false,
      "site": "00557ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
    "old": {
      "definition_site": "00557ac8",
      "incomplete_value": false,
      "site": "00557ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:d18:8"
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
      "0057a94c",
      "DATA",
      [
        "storage",
        "00beefb0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057a960",
      "DATA",
      [
        "storage",
        "00beed18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a94c",
      "DATA",
      [
        "storage",
        "00c6bb70",
        null,
        "undefined *"
      ]
    ],
    [
      "0057a960",
      "DATA",
      [
        "storage",
        "00c6b8d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00557aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557a90.md#insn-00557aa4) · [`00557aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557a90.md#insn-00557aa8) · [`00557aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557a90.md#insn-00557aac)
- 新版 `0057a93c`（命令位置の公開資料なし） · `0057a940`（命令位置の公開資料なし） · `0057a944`（命令位置の公開資料なし）

~~~diff
- 00557aa4 ["INT_ADD", "register:40f0:8", ["const:557aa4:8", "const:4:8"]]
- 00557aa4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0057a93c ["INT_ADD", "register:40f0:8", ["const:57a93c:8", "const:4:8"]]
+ 0057a93c ["CALL", null, ["callee:00c57a90:8"]]
- 00557aa4 bytes 670d1a94
+ 0057a93c bytes 55741b94
- 00557aa8 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 0057a940 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00557aa8 bytes a83400f0
+ 0057a940 bytes 883700b0
- 00557aac ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 00557aac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00557aac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00557aac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a944 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 0057a944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00557aac bytes 08c13e91
+ 0057a944 bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f1c5e0ed58984fd7087caaa7bdc4ad7"></a>

### [`00557adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557adc.md) → [`0057a974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a974.md) FUN_0057a974

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00558fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558fd0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

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
    "old": {
      "definition_site": "00557b50",
      "incomplete_value": true,
      "site": "00557b50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a3c:8"
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
    "old": {
      "definition_site": "00557b58",
      "incomplete_value": true,
      "site": "00557b58",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "00557b54",
      "incomplete_value": true,
      "site": "00557b68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bb2:8"
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
      "0057a9d0",
      "READ",
      [
        "storage",
        "002aea3c",
        null,
        "string"
      ]
    ],
    [
      "0057a9d8",
      "READ",
      [
        "storage",
        "002aea42",
        null,
        "string"
      ]
    ],
    [
      "0057a9ec",
      "READ",
      [
        "storage",
        "00296bb2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a9d0",
      "READ",
      [
        "storage",
        "002bff20",
        null,
        "string"
      ]
    ],
    [
      "0057a9d8",
      "READ",
      [
        "storage",
        "002bff26",
        null,
        "string"
      ]
    ],
    [
      "0057a9ec",
      "READ",
      [
        "storage",
        "002a66e7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00557c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557adc.md#insn-00557c60) · [`00557b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557adc.md#insn-00557b10) · [`00557b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557adc.md#insn-00557b24)
- 新版 `0057aaf8`（命令位置の公開資料なし） · `0057a9a8`（命令位置の公開資料なし） · `0057a9bc`（命令位置の公開資料なし）

~~~diff
- 00557c60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3e0:8"]]
- 00557c60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0057aaf8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 0057aaf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00557c60 bytes 09f101f9
+ 0057aaf8 bytes 095107f9
- 00557b10 ["INT_ADD", "register:40f0:8", ["const:557b10:8", "const:4:8"]]
- 00557b10 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057a9a8 ["INT_ADD", "register:40f0:8", ["const:57a9a8:8", "const:4:8"]]
+ 0057a9a8 ["CALL", null, ["callee:00588e2c:8"]]
- 00557b10 bytes 21390094
+ 0057a9a8 bytes 21390094
- 00557b24 ["INT_ADD", "register:40f0:8", ["const:557b24:8", "const:4:8"]]
- 00557b24 ["CALL", null, ["callee:00589890:8"]]
+ 0057a9bc ["INT_ADD", "register:40f0:8", ["const:57a9bc:8", "const:4:8"]]
+ 0057a9bc ["CALL", null, ["callee:00589890:8"]]
- 00557b24 bytes b53b0094
+ 0057a9bc bytes b53b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bded01c339c9865233d174d838f218e8"></a>

### [`00557d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557d8c.md) → [`0057ac24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057ac24.md) FUN_0057ac24

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "00557dec",
      "incomplete_value": true,
      "site": "00557dec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c41:8"
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
    "old": {
      "definition_site": "00557e68",
      "incomplete_value": true,
      "site": "00557e68",
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
      "0057ac74",
      "READ",
      [
        "storage",
        "00297c41",
        null,
        "string"
      ]
    ],
    [
      "0057acfc",
      "READ",
      [
        "storage",
        "00c263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0057ad58",
      "READ",
      [
        "storage",
        "00c26420",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057ac74",
      "READ",
      [
        "storage",
        "002a789a",
        null,
        "string"
      ]
    ],
    [
      "0057acfc",
      "READ",
      [
        "storage",
        "00ca5e90",
        null,
        "undefined8"
      ]
    ],
    [
      "0057ad58",
      "READ",
      [
        "storage",
        "00ca5ee0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00557dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557d8c.md#insn-00557dbc) · [`00557dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557d8c.md#insn-00557dc4) · [`00557dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557d8c.md#insn-00557dcc)
- 新版 `0057ac54`（命令位置の公開資料なし） · `0057ac5c`（命令位置の公開資料なし） · `0057ac64`（命令位置の公開資料なし）

~~~diff
- 00557dbc ["INT_ADD", "register:40f0:8", ["const:557dbc:8", "const:4:8"]]
- 00557dbc ["CALL", null, ["callee:00588e2c:8"]]
+ 0057ac54 ["INT_ADD", "register:40f0:8", ["const:57ac54:8", "const:4:8"]]
+ 0057ac54 ["CALL", null, ["callee:00588e2c:8"]]
- 00557dbc bytes 76380094
+ 0057ac54 bytes 76380094
- 00557dc4 ["INT_ADD", "register:40f0:8", ["const:557dc4:8", "const:4:8"]]
- 00557dc4 ["CALL", null, ["callee:0058911c:8"]]
+ 0057ac5c ["INT_ADD", "register:40f0:8", ["const:57ac5c:8", "const:4:8"]]
+ 0057ac5c ["CALL", null, ["callee:0058911c:8"]]
- 00557dc4 bytes 30390094
+ 0057ac5c bytes 30390094
- 00557dcc ["COPY", "register:4048:8", ["const:297000:8"]]
+ 0057ac64 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00557dcc bytes 09eaff90
+ 0057ac64 bytes 69e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4065412850da5d4eac89c1bb61c5f343"></a>

### [`00557f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557f84.md) → [`0057ae1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057ae1c.md) FUN_0057ae1c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "00557fe0",
      "incomplete_value": true,
      "site": "00557fe0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:939:8"
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
      "0057ae60",
      "READ",
      [
        "storage",
        "002a6939",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057ae60",
      "READ",
      [
        "storage",
        "002b742a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00557fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557f84.md#insn-00557fa8) · [`00557fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557f84.md#insn-00557fb0) · [`00557fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557f84.md#insn-00557fb8)
- 新版 `0057ae40`（命令位置の公開資料なし） · `0057ae48`（命令位置の公開資料なし） · `0057ae50`（命令位置の公開資料なし）

~~~diff
- 00557fa8 ["INT_ADD", "register:40f0:8", ["const:557fa8:8", "const:4:8"]]
- 00557fa8 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057ae40 ["INT_ADD", "register:40f0:8", ["const:57ae40:8", "const:4:8"]]
+ 0057ae40 ["CALL", null, ["callee:00588e2c:8"]]
- 00557fa8 bytes fb370094
+ 0057ae40 bytes fb370094
- 00557fb0 ["INT_ADD", "register:40f0:8", ["const:557fb0:8", "const:4:8"]]
- 00557fb0 ["CALL", null, ["callee:0058911c:8"]]
+ 0057ae48 ["INT_ADD", "register:40f0:8", ["const:57ae48:8", "const:4:8"]]
+ 0057ae48 ["CALL", null, ["callee:0058911c:8"]]
- 00557fb0 bytes b5380094
+ 0057ae48 bytes b5380094
- 00557fb8 ["COPY", "register:4048:8", ["const:2a6000:8"]]
+ 0057ae50 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 00557fb8 bytes 69eafff0
+ 0057ae50 bytes e9e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d3dbe4bf219eb0ffadb42ddddf55cf7"></a>

### [`005580a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005580a4.md) → [`0057af3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057af3c.md) FUN_0057af3c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db3c.md) · 呼出先 11件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 1件 [`005509d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d4.md) · 呼出先 11件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "00558110",
      "incomplete_value": true,
      "site": "00558118",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:944:8"
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
    "old": {
      "definition_site": "0055811c",
      "incomplete_value": true,
      "site": "0055811c",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "005581dc",
      "incomplete_value": false,
      "site": "005581e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "0057afa8",
      "READ",
      [
        "storage",
        "00292944",
        null,
        "string"
      ]
    ],
    [
      "0057afac",
      "READ",
      [
        "storage",
        "00292951",
        null,
        "string"
      ]
    ],
    [
      "0057b07c",
      "DATA",
      [
        "storage",
        "00bef000",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057afa8",
      "READ",
      [
        "storage",
        "002a2054",
        null,
        "string"
      ]
    ],
    [
      "0057afac",
      "READ",
      [
        "storage",
        "002a2061",
        null,
        "string"
      ]
    ],
    [
      "0057b07c",
      "DATA",
      [
        "storage",
        "00c6bbc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005580d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005580a4.md#insn-005580d0) · [`005580d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005580a4.md#insn-005580d8) · [`00558108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005580a4.md#insn-00558108)
- 新版 `0057af68`（命令位置の公開資料なし） · `0057af70`（命令位置の公開資料なし） · `0057afa0`（命令位置の公開資料なし）

~~~diff
- 005580d0 ["INT_ADD", "register:40f0:8", ["const:5580d0:8", "const:4:8"]]
- 005580d0 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057af68 ["INT_ADD", "register:40f0:8", ["const:57af68:8", "const:4:8"]]
+ 0057af68 ["CALL", null, ["callee:00588e2c:8"]]
- 005580d0 bytes b1370094
+ 0057af68 bytes b1370094
- 005580d8 ["INT_ADD", "register:40f0:8", ["const:5580d8:8", "const:4:8"]]
- 005580d8 ["CALL", null, ["callee:0058911c:8"]]
+ 0057af70 ["INT_ADD", "register:40f0:8", ["const:57af70:8", "const:4:8"]]
+ 0057af70 ["CALL", null, ["callee:0058911c:8"]]
- 005580d8 bytes 6b380094
+ 0057af70 bytes 6b380094
- 00558108 ["COPY", "register:4048:8", ["const:292000:8"]]
+ 0057afa0 ["COPY", "register:4048:8", ["const:2a2000:8"]]
- 00558108 bytes c9e9ffd0
+ 0057afa0 bytes 49e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23c747e9b2ebb48dabad1208ce2da0be"></a>

### [`0055828c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/0055828c.md) → [`0057b124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b124.md) FUN_0057b124

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db38.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`0055977c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/0055977c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 1件 [`005509d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d0.md) · 呼出先 15件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0057c614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c614.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

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
    "old": {
      "definition_site": "005584b4",
      "incomplete_value": true,
      "site": "005584b4",
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
            "const:3c8:8"
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
    "old": {
      "definition_site": "00558570",
      "incomplete_value": false,
      "site": "00558578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
    "old": {
      "definition_site": "00558588",
      "incomplete_value": false,
      "site": "00558588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "0057b1a4",
      "READ",
      [
        "storage",
        "00299deb",
        null,
        "string"
      ]
    ],
    [
      "0057b1a4",
      "READ",
      [
        "storage",
        "00299dfb",
        null,
        "string"
      ]
    ],
    [
      "0057b1a8",
      "READ",
      [
        "storage",
        "002b17f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057b1a4",
      "READ",
      [
        "storage",
        "002a9cc4",
        null,
        "string"
      ]
    ],
    [
      "0057b1a4",
      "READ",
      [
        "storage",
        "002a9cd4",
        null,
        "string"
      ]
    ],
    [
      "0057b1a8",
      "READ",
      [
        "storage",
        "002c2e80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005584b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/0055828c.md#insn-005584b4) · [`005582c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/0055828c.md#insn-005582c8) · [`005582d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/0055828c.md#insn-005582d0)
- 新版 `0057b34c`（命令位置の公開資料なし） · `0057b160`（命令位置の公開資料なし） · `0057b168`（命令位置の公開資料なし）

~~~diff
- 005584b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3c8:8"]]
- 005584b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0057b34c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
+ 0057b34c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005584b4 bytes 09e501f9
+ 0057b34c bytes 094507f9
- 005582c8 ["INT_ADD", "register:40f0:8", ["const:5582c8:8", "const:4:8"]]
- 005582c8 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057b160 ["INT_ADD", "register:40f0:8", ["const:57b160:8", "const:4:8"]]
+ 0057b160 ["CALL", null, ["callee:00588e2c:8"]]
- 005582c8 bytes 33370094
+ 0057b160 bytes 33370094
- 005582d0 ["INT_ADD", "register:40f0:8", ["const:5582d0:8", "const:4:8"]]
- 005582d0 ["CALL", null, ["callee:0058911c:8"]]
+ 0057b168 ["INT_ADD", "register:40f0:8", ["const:57b168:8", "const:4:8"]]
+ 0057b168 ["CALL", null, ["callee:0058911c:8"]]
- 005582d0 bytes ed370094
+ 0057b168 bytes ed370094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28d6cd6cc86cc9e2dbaba97c91948cba"></a>

### [`00558640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558640.md) → [`0057b4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b4d8.md) Java_jp_co_ponos_battlecats_MyActivity_onAlertClick

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "005587b0",
      "incomplete_value": true,
      "site": "005587b0",
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
            "const:3e0:8"
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
    "old": {
      "definition_site": "0055866c",
      "incomplete_value": true,
      "site": "0055866c",
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
    "old": {
      "definition_site": "005587ac",
      "incomplete_value": true,
      "site": "005587ac",
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
      "0057b500",
      "READ",
      [
        "storage",
        "00c263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b548",
      "READ",
      [
        "storage",
        "00c26420",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b57c",
      "READ",
      [
        "storage",
        "00c263e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b500",
      "READ",
      [
        "storage",
        "00ca5e90",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b548",
      "READ",
      [
        "storage",
        "00ca5ee0",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b57c",
      "READ",
      [
        "storage",
        "00ca5ea8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005587b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558640.md#insn-005587b0) · [`00558660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558640.md#insn-00558660) · [`00558664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558640.md#insn-00558664)
- 新版 `0057b648`（命令位置の公開資料なし） · `0057b4f8`（命令位置の公開資料なし） · `0057b4fc`（命令位置の公開資料なし）

~~~diff
- 005587b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3e0:8"]]
- 005587b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0057b648 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ea0:8"]]
+ 0057b648 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005587b0 bytes 28f101f9
+ 0057b648 bytes 285107f9
- 00558660 ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 0057b4f8 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 00558660 bytes 683600d0
+ 0057b4f8 bytes 483900d0
- 00558664 ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 00558664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00558664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00558664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b4fc ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 0057b4fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b4fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b4fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00558664 bytes 08410f91
+ 0057b4fc bytes 08413a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21352a57d367b6da04e5f25c0cec2d23"></a>

### [`00558824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558824.md) → [`0057b6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b6bc.md) Java_jp_co_ponos_battlecats_MyActivity_onButtonClick

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00558830",
      "incomplete_value": true,
      "site": "00558830",
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
      "0057b6c4",
      "READ",
      [
        "storage",
        "00c263b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b71c",
      "READ",
      [
        "storage",
        "00c263e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b6c4",
      "READ",
      [
        "storage",
        "00ca5e78",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b71c",
      "READ",
      [
        "storage",
        "00ca5ea0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00558824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558824.md#insn-00558824) · [`00558828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558824.md#insn-00558828) · [`00558834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558824.md#insn-00558834)
- 新版 `0057b6bc`（命令位置の公開資料なし） · `0057b6c0`（命令位置の公開資料なし） · `0057b6cc`（命令位置の公開資料なし）

~~~diff
- 00558824 ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 0057b6bc ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 00558824 bytes 683600d0
+ 0057b6bc bytes 483900d0
- 00558828 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 00558828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00558828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00558828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b6c0 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 0057b6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00558828 bytes 08e10e91
+ 0057b6c0 bytes 08e13991
- 00558834 ["COPY", "register:4048:8", ["const:c26000:8"]]
+ 0057b6cc ["COPY", "register:4048:8", ["const:ca5000:8"]]
- 00558834 bytes 693600d0
+ 0057b6cc bytes 493900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d57272452670c267f6aed0ebddc21951"></a>

### [`005588a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005588a0.md) → [`0057b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b738.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewFilter

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "005588c8",
      "incomplete_value": true,
      "site": "005588c8",
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
      "0057b75c",
      "READ",
      [
        "storage",
        "00c26380",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b7b4",
      "READ",
      [
        "storage",
        "00c26400",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b75c",
      "READ",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b7b4",
      "READ",
      [
        "storage",
        "00ca5ec0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005588bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005588a0.md#insn-005588bc) · [`005588c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005588a0.md#insn-005588c0) · [`005588cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005588a0.md#insn-005588cc)
- 新版 `0057b754`（命令位置の公開資料なし） · `0057b758`（命令位置の公開資料なし） · `0057b764`（命令位置の公開資料なし）

~~~diff
- 005588bc ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 0057b754 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 005588bc bytes 683600d0
+ 0057b754 bytes 483900d0
- 005588c0 ["COPY", "tmp:0:8", ["const:380:8"]]
- 005588c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005588c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005588c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b758 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 0057b758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005588c0 bytes 08010e91
+ 0057b758 bytes 08013991
- 005588cc ["COPY", "register:4098:8", ["const:c26000:8"]]
+ 0057b764 ["COPY", "register:4098:8", ["const:ca5000:8"]]
- 005588cc bytes 733600d0
+ 0057b764 bytes 533900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e2d74e769ce9537e94c22c7ea182823"></a>

### [`005589d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005589d8.md) → [`0057b870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b870.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewResult

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "00558a08",
      "incomplete_value": true,
      "site": "00558a08",
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
      "0057b89c",
      "READ",
      [
        "storage",
        "00c26380",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b8f4",
      "READ",
      [
        "storage",
        "00c263d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b89c",
      "READ",
      [
        "storage",
        "00ca5e40",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b8f4",
      "READ",
      [
        "storage",
        "00ca5e90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005589fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005589d8.md#insn-005589fc) · [`00558a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005589d8.md#insn-00558a00) · [`00558a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/005589d8.md#insn-00558a0c)
- 新版 `0057b894`（命令位置の公開資料なし） · `0057b898`（命令位置の公開資料なし） · `0057b8a4`（命令位置の公開資料なし）

~~~diff
- 005589fc ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 0057b894 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 005589fc bytes 683600d0
+ 0057b894 bytes 483900d0
- 00558a00 ["COPY", "tmp:0:8", ["const:380:8"]]
- 00558a00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00558a00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00558a00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b898 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 0057b898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00558a00 bytes 08010e91
+ 0057b898 bytes 08013991
- 00558a0c ["COPY", "register:40a8:8", ["const:c26000:8"]]
+ 0057b8a4 ["COPY", "register:40a8:8", ["const:ca5000:8"]]
- 00558a0c bytes 753600d0
+ 0057b8a4 bytes 553900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9f7838fbce8e039018c04903dcb7f55"></a>

### [`00558b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558b10.md) → [`0057b9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057b9a8.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewEvalResult

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "00558b40",
      "incomplete_value": true,
      "site": "00558b40",
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
      "0057b9d4",
      "READ",
      [
        "storage",
        "00c26398",
        null,
        "undefined8"
      ]
    ],
    [
      "0057ba70",
      "READ",
      [
        "storage",
        "00c263e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b9d4",
      "READ",
      [
        "storage",
        "00ca5e58",
        null,
        "undefined8"
      ]
    ],
    [
      "0057ba70",
      "READ",
      [
        "storage",
        "00ca5ea8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00558b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558b10.md#insn-00558b34) · [`00558b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558b10.md#insn-00558b38) · [`00558b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558b10.md#insn-00558b44)
- 新版 `0057b9cc`（命令位置の公開資料なし） · `0057b9d0`（命令位置の公開資料なし） · `0057b9dc`（命令位置の公開資料なし）

~~~diff
- 00558b34 ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 0057b9cc ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 00558b34 bytes 683600d0
+ 0057b9cc bytes 483900d0
- 00558b38 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00558b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00558b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00558b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b9d0 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 0057b9d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b9d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b9d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00558b38 bytes 08610e91
+ 0057b9d0 bytes 08613991
- 00558b44 ["COPY", "register:40a8:8", ["const:c26000:8"]]
+ 0057b9dc ["COPY", "register:40a8:8", ["const:ca5000:8"]]
- 00558b44 bytes 753600d0
+ 0057b9dc bytes 553900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d97394ce87a3d35bdc777fe709c73031"></a>

### [`00558ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558ca4.md) → [`0057bb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bb3c.md) FUN_0057bb3c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
    "old": {
      "definition_site": "00558cbc",
      "incomplete_value": false,
      "site": "00558cc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "0057bb58",
      "DATA",
      [
        "storage",
        "00beec28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057bb58",
      "DATA",
      [
        "storage",
        "00c6b7e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00558cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558ca4.md#insn-00558cb8) · [`00558cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558ca4.md#insn-00558cbc) · [`00558cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558ca4.md#insn-00558cf0)
- 新版 `0057bb50`（命令位置の公開資料なし） · `0057bb54`（命令位置の公開資料なし） · `0057bb88`（命令位置の公開資料なし）

~~~diff
- 00558cb8 ["COPY", "register:4048:8", ["const:bee000:8"]]
+ 0057bb50 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00558cb8 bytes a93400d0
+ 0057bb50 bytes 89370090
- 00558cbc ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00558cbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00558cbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00558cbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057bb54 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 0057bb54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057bb54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057bb54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00558cbc bytes 29a13091
+ 0057bb54 bytes 29a11f91
- 00558cf0 ["INT_ADD", "register:40f0:8", ["const:558cf0:8", "const:4:8"]]
- 00558cf0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0057bb88 ["INT_ADD", "register:40f0:8", ["const:57bb88:8", "const:4:8"]]
+ 0057bb88 ["CALL", null, ["callee:00c57ab0:8"]]
- 00558cf0 bytes dc081a94
+ 0057bb88 bytes ca6f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d36458674c57aa01c0f3b39e8e36c754"></a>

### [`00559334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559334.md) → [`0057c1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c1cc.md) FUN_0057c1cc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005591d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005591d8.md) [`00559458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559458.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0057c070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c070.md) [`0057c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2f0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0057c1dc",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00559344",
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
    "old": {
      "definition_site": "00559340",
      "incomplete_value": false,
      "site": "00559344",
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
      "0057c1d8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0057c1dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0057c1d8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0057c1dc",
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

- 旧版 [`00559344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559334.md#insn-00559344) · [`0055933c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559334.md#insn-0055933c) · [`00559340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559334.md#insn-00559340)
- 新版 `0057c1dc`（命令位置の公開資料なし） · `0057c1d4`（命令位置の公開資料なし） · `0057c1d8`（命令位置の公開資料なし）

~~~diff
- 00559344 ["INT_ADD", "register:40f0:8", ["const:559344:8", "const:4:8"]]
- 00559344 ["CALL", null, ["ram:418c38:8"]]
+ 0057c1dc ["INT_ADD", "register:40f0:8", ["const:57c1dc:8", "const:4:8"]]
+ 0057c1dc ["CALL", null, ["ram:43b738:8"]]
- 00559344 bytes 3dfefa97
+ 0057c1dc bytes 57fdfa97
- 0055933c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0057c1d4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0055933c bytes 60eaffd0
+ 0057c1d4 bytes c0e9fff0
- 00559340 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00559340 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00559340 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00559340 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057c1d8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0057c1d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c1d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c1d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00559340 bytes 00740e91
+ 0057c1d8 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-473a55a43f66f4798c811730fcc623cb"></a>

### [`00559444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559444.md) → [`0057c2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c2dc.md) FUN_0057c2dc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005573cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/005573cc.md) [`00557424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/00557424.md) [`0055746c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00557/0055746c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`0057a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a264.md) [`0057a2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a2bc.md) [`0057a304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057a/0057a304.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "0057c2ec",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00559454",
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
    "old": {
      "definition_site": "00559450",
      "incomplete_value": false,
      "site": "00559454",
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
      "0057c2e8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0057c2ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "0057c2e8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0057c2ec",
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

- 旧版 [`00559454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559444.md#insn-00559454) · [`0055944c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559444.md#insn-0055944c) · [`00559450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559444.md#insn-00559450)
- 新版 `0057c2ec`（命令位置の公開資料なし） · `0057c2e4`（命令位置の公開資料なし） · `0057c2e8`（命令位置の公開資料なし）

~~~diff
- 00559454 ["INT_ADD", "register:40f0:8", ["const:559454:8", "const:4:8"]]
- 00559454 ["CALL", null, ["ram:41fdf0:8"]]
+ 0057c2ec ["INT_ADD", "register:40f0:8", ["const:57c2ec:8", "const:4:8"]]
+ 0057c2ec ["CALL", null, ["ram:4428f0:8"]]
- 00559454 bytes 671afb97
+ 0057c2ec bytes 8119fb97
- 0055944c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0057c2e4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0055944c bytes 60eaffd0
+ 0057c2e4 bytes c0e9fff0
- 00559450 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00559450 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00559450 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00559450 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057c2e8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0057c2e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c2e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c2e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00559450 bytes 00740e91
+ 0057c2e8 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb29cffaecf149e34c2bb4bef8f9d964"></a>

### [`005598e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005598e4.md) → [`0057c77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c77c.md) _INIT_31

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`005536d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005536d4.md) [`005536dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005536dc.md) [`00553820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553820.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`0057656c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/0057656c.md) [`00576574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576574.md) [`005766b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/005766b8.md)

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
    "old": {
      "definition_site": "00559920",
      "incomplete_value": true,
      "site": "0055993c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00559944",
      "incomplete_value": true,
      "site": "00559960",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00559964",
      "incomplete_value": true,
      "site": "00559980",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057c7b8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0057c7dc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0057c7fc",
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
      "0057c7b8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0057c7dc",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0057c7fc",
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

- 旧版 [`00559b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005598e4.md#insn-00559b1c) · [`00559b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005598e4.md#insn-00559b44) · [`00559b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/005598e4.md#insn-00559b94)
- 新版 `0057c9b4`（命令位置の公開資料なし） · `0057c9dc`（命令位置の公開資料なし）

~~~diff
- 00559b1c ["INT_ADD", "register:40f0:8", ["const:559b1c:8", "const:4:8"]]
- 00559b1c ["CALL", null, ["callee:00c57a30:8"]]
+ 0057c9b4 ["INT_ADD", "register:40f0:8", ["const:57c9b4:8", "const:4:8"]]
+ 0057c9b4 ["CALL", null, ["callee:00c57a30:8"]]
- 00559b1c bytes 31051a94
+ 0057c9b4 bytes 1f6c1b94
- 00559b44 ["INT_ADD", "register:40f0:8", ["const:559b44:8", "const:4:8"]]
- 00559b44 ["CALL", null, ["callee:00c57a30:8"]]
+ 0057c9dc ["INT_ADD", "register:40f0:8", ["const:57c9dc:8", "const:4:8"]]
+ 0057c9dc ["CALL", null, ["callee:00c57a30:8"]]
- 00559b44 bytes 27051a94
+ 0057c9dc bytes 156c1b94
- 00559b94 ["INT_ADD", "register:40f0:8", ["const:559b94:8", "const:4:8"]]
- 00559b94 ["CALL", null, ["callee:00c57a30:8"]]
- 00559b94 bytes 13051a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c09c98ac3f9eacbcfe1976c66a984d91"></a>

### [`00559d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559d40.md) → [`0057cbd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cbd8.md) FUN_0057cbd8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c59d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d40.md)

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
    "old": {
      "definition_site": "00559d60",
      "incomplete_value": false,
      "site": "00559d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:50:8"
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
    "old": {
      "definition_site": "00559d60",
      "incomplete_value": false,
      "site": "00559d60",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:50:8"
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
      "0057cbf8",
      "DATA",
      [
        "storage",
        "00bef050",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cbf8",
      "DATA",
      [
        "storage",
        "00bef118",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057cbf8",
      "DATA",
      [
        "storage",
        "00c6bc10",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cbf8",
      "DATA",
      [
        "storage",
        "00c6bcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00559d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559d40.md#insn-00559d50) · [`00559d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559d40.md#insn-00559d54) · [`00559d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559d40.md#insn-00559d68)
- 新版 `0057cbe8`（命令位置の公開資料なし） · `0057cbec`（命令位置の公開資料なし） · `0057cc00`（命令位置の公開資料なし）

~~~diff
- 00559d50 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0057cbe8 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00559d50 bytes a83400d0
+ 0057cbe8 bytes 683700f0
- 00559d54 ["COPY", "tmp:0:8", ["const:50:8"]]
- 00559d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00559d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00559d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cbec ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0057cbec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cbec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cbec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00559d54 bytes 08410191
+ 0057cbec bytes 08413091
- 00559d68 ["INT_ADD", "register:40f0:8", ["const:559d68:8", "const:4:8"]]
- 00559d68 ["CALL", null, ["callee:00c59d40:8"]]
+ 0057cc00 ["INT_ADD", "register:40f0:8", ["const:57cc00:8", "const:4:8"]]
+ 0057cc00 ["CALL", null, ["callee:00c59d40:8"]]
- 00559d68 bytes 620d1a94
+ 0057cc00 bytes 50741b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03c8872a3936fca306d6b36ddd9143ec"></a>

### [`00559da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559da0.md) → [`0057cc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057cc38.md) FUN_0057cc38

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd2f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c59d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d40.md)

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
    "old": {
      "definition_site": "00559dc0",
      "incomplete_value": false,
      "site": "00559dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:50:8"
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
    "old": {
      "definition_site": "00559dc0",
      "incomplete_value": false,
      "site": "00559dc0",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:50:8"
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
      "0057cc58",
      "DATA",
      [
        "storage",
        "00bef050",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cc58",
      "DATA",
      [
        "storage",
        "00bef118",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057cc58",
      "DATA",
      [
        "storage",
        "00c6bc10",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cc58",
      "DATA",
      [
        "storage",
        "00c6bcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00559db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559da0.md#insn-00559db0) · [`00559db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559da0.md#insn-00559db4) · [`00559dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559da0.md#insn-00559dc8)
- 新版 `0057cc48`（命令位置の公開資料なし） · `0057cc4c`（命令位置の公開資料なし） · `0057cc60`（命令位置の公開資料なし）

~~~diff
- 00559db0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0057cc48 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00559db0 bytes a83400d0
+ 0057cc48 bytes 683700f0
- 00559db4 ["COPY", "tmp:0:8", ["const:50:8"]]
- 00559db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00559db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00559db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cc4c ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0057cc4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cc4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cc4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00559db4 bytes 08410191
+ 0057cc4c bytes 08413091
- 00559dc8 ["INT_ADD", "register:40f0:8", ["const:559dc8:8", "const:4:8"]]
- 00559dc8 ["CALL", null, ["callee:00c59d40:8"]]
+ 0057cc60 ["INT_ADD", "register:40f0:8", ["const:57cc60:8", "const:4:8"]]
+ 0057cc60 ["CALL", null, ["callee:00c59d40:8"]]
- 00559dc8 bytes 4a0d1a94
+ 0057cc60 bytes 38741b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc2f0ca299f86adc9408ad8487b0a307"></a>

### [`00559fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559fe0.md) → [`0057ce78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057ce78.md) FUN_0057ce78

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00567d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "0055a150",
      "incomplete_value": false,
      "site": "0055a15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "0057cff4",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057cff4",
      "DATA",
      [
        "storage",
        "00c6be60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559fe0.md#insn-0055a02c) · [`0055a048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559fe0.md#insn-0055a048) · [`0055a080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00559/00559fe0.md#insn-0055a080)
- 新版 `0057cec4`（命令位置の公開資料なし） · `0057cee0`（命令位置の公開資料なし） · `0057cf18`（命令位置の公開資料なし）

~~~diff
- 0055a02c ["INT_ADD", "register:40f0:8", ["const:55a02c:8", "const:4:8"]]
- 0055a02c ["CALL", null, ["callee:00c57a90:8"]]
+ 0057cec4 ["INT_ADD", "register:40f0:8", ["const:57cec4:8", "const:4:8"]]
+ 0057cec4 ["CALL", null, ["callee:00c57a90:8"]]
- 0055a02c bytes 05041a94
+ 0057cec4 bytes f36a1b94
- 0055a048 ["INT_ADD", "register:40f0:8", ["const:55a048:8", "const:4:8"]]
- 0055a048 ["CALL", null, ["callee:00c57c90:8"]]
+ 0057cee0 ["INT_ADD", "register:40f0:8", ["const:57cee0:8", "const:4:8"]]
+ 0057cee0 ["CALL", null, ["callee:00c57c90:8"]]
- 0055a048 bytes 7e041a94
+ 0057cee0 bytes 6c6b1b94
- 0055a080 ["INT_ADD", "register:40f0:8", ["const:55a080:8", "const:4:8"]]
- 0055a080 ["CALL", null, ["callee:00c59d80:8"]]
+ 0057cf18 ["INT_ADD", "register:40f0:8", ["const:57cf18:8", "const:4:8"]]
+ 0057cf18 ["CALL", null, ["callee:00c59d80:8"]]
- 0055a080 bytes ac0c1a94
+ 0057cf18 bytes 9a731b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a673fe07221625a4e083b82a57818eaa"></a>

### [`0055a5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a5bc.md) → [`0057d454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d454.md) FUN_0057d454

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00567d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567d4c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0058abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058abe4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "0055a734",
      "incomplete_value": false,
      "site": "0055a740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "0057d5d8",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d5d8",
      "DATA",
      [
        "storage",
        "00c6be60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a5bc.md#insn-0055a608) · [`0055a624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a5bc.md#insn-0055a624) · [`0055a660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055a5bc.md#insn-0055a660)
- 新版 `0057d4a0`（命令位置の公開資料なし） · `0057d4bc`（命令位置の公開資料なし） · `0057d4f8`（命令位置の公開資料なし）

~~~diff
- 0055a608 ["INT_ADD", "register:40f0:8", ["const:55a608:8", "const:4:8"]]
- 0055a608 ["CALL", null, ["callee:00c57a90:8"]]
+ 0057d4a0 ["INT_ADD", "register:40f0:8", ["const:57d4a0:8", "const:4:8"]]
+ 0057d4a0 ["CALL", null, ["callee:00c57a90:8"]]
- 0055a608 bytes 8e021a94
+ 0057d4a0 bytes 7c691b94
- 0055a624 ["INT_ADD", "register:40f0:8", ["const:55a624:8", "const:4:8"]]
- 0055a624 ["CALL", null, ["callee:00c57c90:8"]]
+ 0057d4bc ["INT_ADD", "register:40f0:8", ["const:57d4bc:8", "const:4:8"]]
+ 0057d4bc ["CALL", null, ["callee:00c57c90:8"]]
- 0055a624 bytes 07031a94
+ 0057d4bc bytes f5691b94
- 0055a660 ["INT_ADD", "register:40f0:8", ["const:55a660:8", "const:4:8"]]
- 0055a660 ["CALL", null, ["callee:00c59c80:8"]]
+ 0057d4f8 ["INT_ADD", "register:40f0:8", ["const:57d4f8:8", "const:4:8"]]
+ 0057d4f8 ["CALL", null, ["callee:00c59c80:8"]]
- 0055a660 bytes f40a1a94
+ 0057d4f8 bytes e2711b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a60b38bc9fad774de46a4174905ccf4"></a>

### [`0055aad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055aad0.md) → [`0057d968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057d968.md) FUN_0057d968

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md) [`00bdd310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd310.md)
- 新版 呼出元 1件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c59c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c90.md) [`00c59d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59d60.md)

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
    "old": {
      "definition_site": "0055ab28",
      "incomplete_value": false,
      "site": "0055ab34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
    "old": {
      "definition_site": "0055ab48",
      "incomplete_value": false,
      "site": "0055ab48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:50:8"
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
    "old": {
      "definition_site": "0055ab4c",
      "incomplete_value": false,
      "site": "0055ab50",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:50:8"
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
      "0057d988",
      "READ",
      [
        "storage",
        "00c1b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "0057d99c",
      "READ",
      [
        "storage",
        "00c263f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0057d9cc",
      "DATA",
      [
        "storage",
        "00bef2f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057d988",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "0057d99c",
      "READ",
      [
        "storage",
        "00ca5eb8",
        null,
        "undefined8"
      ]
    ],
    [
      "0057d9cc",
      "DATA",
      [
        "storage",
        "00c6beb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055aae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055aad0.md#insn-0055aae8) · [`0055aaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055aad0.md#insn-0055aaf0) · [`0055ab10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055aad0.md#insn-0055ab10)
- 新版 `0057d980`（命令位置の公開資料なし） · `0057d988`（命令位置の公開資料なし） · `0057d9a8`（命令位置の公開資料なし）

~~~diff
- 0055aae8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 0057d980 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0055aae8 bytes 083600b0
+ 0057d980 bytes e83800b0
- 0055aaf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
- 0055aaf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0057d988 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed0:8"]]
+ 0057d988 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0055aaf0 bytes 087142f9
+ 0057d988 bytes 086947f9
- 0055ab10 ["INT_ADD", "register:40f0:8", ["const:55ab10:8", "const:4:8"]]
- 0055ab10 ["CALL", null, ["callee:00c59d60:8"]]
+ 0057d9a8 ["INT_ADD", "register:40f0:8", ["const:57d9a8:8", "const:4:8"]]
+ 0057d9a8 ["CALL", null, ["callee:00c59d60:8"]]
- 0055ab10 bytes 000a1a94
+ 0057d9a8 bytes ee701b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-557728f61045fedf9eb4cc502b99b035"></a>

### [`0055ac68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ac68.md) → [`0057db00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db00.md) FUN_0057db00

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
    "old": {
      "definition_site": "0055ac78",
      "incomplete_value": false,
      "site": "0055ac78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:130:8"
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
    "old": {
      "definition_site": "0055ac78",
      "incomplete_value": false,
      "site": "0055ac78",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:130:8"
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
      "0057db10",
      "DATA",
      [
        "storage",
        "00bef130",
        null,
        "undefined *"
      ]
    ],
    [
      "0057db10",
      "DATA",
      [
        "storage",
        "00bef1f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057db10",
      "DATA",
      [
        "storage",
        "00c6bcf0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057db10",
      "DATA",
      [
        "storage",
        "00c6bdb8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ac68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ac68.md#insn-0055ac68) · [`0055ac6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ac68.md#insn-0055ac6c)
- 新版 `0057db00`（命令位置の公開資料なし） · `0057db04`（命令位置の公開資料なし）

~~~diff
- 0055ac68 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0057db00 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055ac68 bytes a83400b0
+ 0057db00 bytes 683700d0
- 0055ac6c ["COPY", "tmp:0:8", ["const:130:8"]]
- 0055ac6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057db04 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 0057db04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057db04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057db04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ac6c bytes 08c10491
+ 0057db04 bytes 08c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9995175fcfdf5a4bd8b79d1732289a2"></a>

### [`0055ac8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ac8c.md) → [`0057db24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057db24.md) FUN_0057db24

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
    "old": {
      "definition_site": "0055ac9c",
      "incomplete_value": true,
      "site": "0055ac9c",
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
            "const:130:8"
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
    "old": {
      "definition_site": "0055ac9c",
      "incomplete_value": true,
      "site": "0055ac9c",
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
                "const:130:8"
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
      "0057db34",
      "DATA",
      [
        "storage",
        "00bef130",
        null,
        "undefined *"
      ]
    ],
    [
      "0057db34",
      "DATA",
      [
        "storage",
        "00bef1f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057db34",
      "DATA",
      [
        "storage",
        "00c6bcf0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057db34",
      "DATA",
      [
        "storage",
        "00c6bdb8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ac8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ac8c.md#insn-0055ac8c) · [`0055ac90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ac8c.md#insn-0055ac90) · [`0055acbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055ac8c.md#insn-0055acbc)
- 新版 `0057db24`（命令位置の公開資料なし） · `0057db28`（命令位置の公開資料なし） · `0057db54`（命令位置の公開資料なし）

~~~diff
- 0055ac8c ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0057db24 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055ac8c bytes a83400b0
+ 0057db24 bytes 683700d0
- 0055ac90 ["COPY", "tmp:0:8", ["const:130:8"]]
- 0055ac90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057db28 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 0057db28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057db28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057db28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ac90 bytes 08c10491
+ 0057db28 bytes 08c13391
- 0055acbc ["INT_ADD", "register:40f0:8", ["const:55acbc:8", "const:4:8"]]
- 0055acbc ["CALL", null, ["callee:00c57ab0:8"]]
+ 0057db54 ["INT_ADD", "register:40f0:8", ["const:57db54:8", "const:4:8"]]
+ 0057db54 ["CALL", null, ["callee:00c57ab0:8"]]
- 0055acbc bytes e9001a94
+ 0057db54 bytes d7671b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bffea17261de98947fe70eea81de44fc"></a>

### [`0055b1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b1b8.md) → [`0057e050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e050.md) FUN_0057e050

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0052dd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd30.md) [`005627f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/005627f4.md) [`0056340c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00563/0056340c.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`00550bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bc8.md) [`0058568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/0058568c.md) [`005862a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00586/005862a4.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
    "old": {
      "definition_site": "0055b1ec",
      "incomplete_value": false,
      "site": "0055b1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "0057e08c",
      "DATA",
      [
        "storage",
        "00bef408",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e0a4",
      "DATA",
      [
        "storage",
        "00bef390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e08c",
      "DATA",
      [
        "storage",
        "00c6bfc8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e0a4",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b1b8.md#insn-0055b1e4) · [`0055b1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b1b8.md#insn-0055b1e8) · [`0055b1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b1b8.md#insn-0055b1ec)
- 新版 `0057e07c`（命令位置の公開資料なし） · `0057e080`（命令位置の公開資料なし） · `0057e084`（命令位置の公開資料なし）

~~~diff
- 0055b1e4 ["INT_ADD", "register:40f0:8", ["const:55b1e4:8", "const:4:8"]]
- 0055b1e4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0057e07c ["INT_ADD", "register:40f0:8", ["const:57e07c:8", "const:4:8"]]
+ 0057e07c ["CALL", null, ["callee:00c57a90:8"]]
- 0055b1e4 bytes 97ff1994
+ 0057e07c bytes 85661b94
- 0055b1e8 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0057e080 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055b1e8 bytes a8340090
+ 0057e080 bytes 683700b0
- 0055b1ec ["COPY", "tmp:0:8", ["const:408:8"]]
- 0055b1ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b1ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b1ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e084 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 0057e084 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e084 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e084 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b1ec bytes 08211091
+ 0057e084 bytes 08213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53e015a761b65a638a72a0b9366a6ba7"></a>

### [`0055b28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b28c.md) → [`0057e124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e124.md) FUN_0057e124

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
    "old": {
      "definition_site": "0055b2a4",
      "incomplete_value": true,
      "site": "0055b2a8",
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
            "const:390:8"
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
      "0057e140",
      "DATA",
      [
        "storage",
        "00bef390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e140",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b28c.md#insn-0055b2a0) · [`0055b2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b28c.md#insn-0055b2a4) · [`0055b2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b28c.md#insn-0055b2b8)
- 新版 `0057e138`（命令位置の公開資料なし） · `0057e13c`（命令位置の公開資料なし） · `0057e150`（命令位置の公開資料なし）

~~~diff
- 0055b2a0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0057e138 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055b2a0 bytes a8340090
+ 0057e138 bytes 683700b0
- 0055b2a4 ["COPY", "tmp:0:8", ["const:390:8"]]
- 0055b2a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b2a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b2a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e13c ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 0057e13c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e13c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e13c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b2a4 bytes 08410e91
+ 0057e13c bytes 08413d91
- 0055b2b8 ["INT_ADD", "register:40f0:8", ["const:55b2b8:8", "const:4:8"]]
- 0055b2b8 ["CALL", null, ["callee:00c538e0:8"]]
+ 0057e150 ["INT_ADD", "register:40f0:8", ["const:57e150:8", "const:4:8"]]
+ 0057e150 ["CALL", null, ["callee:00c538e0:8"]]
- 0055b2b8 bytes f6ee1994
+ 0057e150 bytes e4551b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f3b4cd114a94e6b809778d8f456c653"></a>

### [`0055b304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b304.md) → [`0057e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e19c.md) FUN_0057e19c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
    "old": {
      "definition_site": "0055b31c",
      "incomplete_value": false,
      "site": "0055b320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "0057e1b8",
      "DATA",
      [
        "storage",
        "00bef390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e1b8",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b304.md#insn-0055b318) · [`0055b31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b304.md#insn-0055b31c) · [`0055b330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b304.md#insn-0055b330)
- 新版 `0057e1b0`（命令位置の公開資料なし） · `0057e1b4`（命令位置の公開資料なし） · `0057e1c8`（命令位置の公開資料なし）

~~~diff
- 0055b318 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0057e1b0 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055b318 bytes a8340090
+ 0057e1b0 bytes 683700b0
- 0055b31c ["COPY", "tmp:0:8", ["const:390:8"]]
- 0055b31c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b31c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b31c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e1b4 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 0057e1b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e1b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e1b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b31c bytes 08410e91
+ 0057e1b4 bytes 08413d91
- 0055b330 ["INT_ADD", "register:40f0:8", ["const:55b330:8", "const:4:8"]]
- 0055b330 ["CALL", null, ["callee:00c538e0:8"]]
+ 0057e1c8 ["INT_ADD", "register:40f0:8", ["const:57e1c8:8", "const:4:8"]]
+ 0057e1c8 ["CALL", null, ["callee:00c538e0:8"]]
- 0055b330 bytes d8ee1994
+ 0057e1c8 bytes c6551b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95c8151946c7a96e4f2d38c4898e4e8c"></a>

### [`0055b37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b37c.md) → [`0057e214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e214.md) FUN_0057e214

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055af38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055a/0055af38.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0057ddd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057d/0057ddd0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
    "old": {
      "definition_site": "0055b3a8",
      "incomplete_value": false,
      "site": "0055b3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
    "old": {
      "definition_site": "0055b3b4",
      "incomplete_value": false,
      "site": "0055b3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "0057e244",
      "DATA",
      [
        "storage",
        "00bef408",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e25c",
      "DATA",
      [
        "storage",
        "00bef390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e244",
      "DATA",
      [
        "storage",
        "00c6bfc8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e25c",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b37c.md#insn-0055b3a4) · [`0055b3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b37c.md#insn-0055b3a8) · [`0055b3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b37c.md#insn-0055b3b0)
- 新版 `0057e23c`（命令位置の公開資料なし） · `0057e240`（命令位置の公開資料なし）

~~~diff
- 0055b3a4 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0057e23c ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0055b3a4 bytes a8340090
+ 0057e23c bytes 683700b0
- 0055b3a8 ["COPY", "tmp:0:8", ["const:408:8"]]
- 0055b3a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b3a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b3a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e240 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 0057e240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b3a8 bytes 08211091
+ 0057e240 bytes 08213f91
- 0055b3b0 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 0055b3b0 bytes a8340090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87db17f126af56725d4f13d15434c0d2"></a>

### [`0055b604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b604.md) → [`0057e49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e49c.md) FUN_0057e49c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0052dd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd54.md) [`0055bd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bd18.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056627c.md)
- 新版 呼出元 2件 [`00550bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bec.md) [`0057ebb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ebb0.md) · 呼出先 15件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`00589114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589114.md)

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
    "old": {
      "definition_site": "0055b664",
      "incomplete_value": true,
      "site": "0055b664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc9:8"
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
    "old": {
      "definition_site": "0055b670",
      "incomplete_value": true,
      "site": "0055b67c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a0d:8"
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
    "old": {
      "definition_site": "0055b71c",
      "incomplete_value": true,
      "site": "0055b71c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:798:8"
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
      "0057e4ec",
      "READ",
      [
        "storage",
        "00296bc9",
        null,
        "string"
      ]
    ],
    [
      "0057e508",
      "READ",
      [
        "storage",
        "002aca0d",
        null,
        "string"
      ]
    ],
    [
      "0057e59c",
      "READ",
      [
        "storage",
        "002a5798",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057e4ec",
      "READ",
      [
        "storage",
        "002a66fe",
        null,
        "string"
      ]
    ],
    [
      "0057e508",
      "READ",
      [
        "storage",
        "002bda85",
        null,
        "string"
      ]
    ],
    [
      "0057e59c",
      "READ",
      [
        "storage",
        "002b61c6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b604.md#insn-0055b630) · [`0055b638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b604.md#insn-0055b638) · [`0055b64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b604.md#insn-0055b64c)
- 新版 `0057e4c8`（命令位置の公開資料なし） · `0057e4d0`（命令位置の公開資料なし） · `0057e4e4`（命令位置の公開資料なし）

~~~diff
- 0055b630 ["INT_ADD", "register:40f0:8", ["const:55b630:8", "const:4:8"]]
- 0055b630 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057e4c8 ["INT_ADD", "register:40f0:8", ["const:57e4c8:8", "const:4:8"]]
+ 0057e4c8 ["CALL", null, ["callee:00588e2c:8"]]
- 0055b630 bytes 592a0094
+ 0057e4c8 bytes 592a0094
- 0055b638 ["INT_ADD", "register:40f0:8", ["const:55b638:8", "const:4:8"]]
- 0055b638 ["CALL", null, ["callee:0058911c:8"]]
+ 0057e4d0 ["INT_ADD", "register:40f0:8", ["const:57e4d0:8", "const:4:8"]]
+ 0057e4d0 ["CALL", null, ["callee:0058911c:8"]]
- 0055b638 bytes 132b0094
+ 0057e4d0 bytes 132b0094
- 0055b64c ["COPY", "register:4040:8", ["const:296000:8"]]
+ 0057e4e4 ["COPY", "register:4040:8", ["const:2a6000:8"]]
- 0055b64c bytes c8e9fff0
+ 0057e4e4 bytes 48e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed4a51cafbd64b4daa918a23949d9780"></a>

### [`0055b95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b95c.md) → [`0057e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057e7f4.md) FUN_0057e7f4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd50.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056627c.md)
- 新版 呼出元 1件 [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md) · 呼出先 15件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`00589114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589114.md)

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
    "old": {
      "definition_site": "0055b9c8",
      "incomplete_value": true,
      "site": "0055b9d4",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:a0d:8"
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
    "old": {
      "definition_site": "0055ba74",
      "incomplete_value": true,
      "site": "0055ba74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:798:8"
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
    "old": {
      "definition_site": "0055ba7c",
      "incomplete_value": true,
      "site": "0055ba7c",
      "value": [
        "LOAD",
        "8",
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
      "0057e844",
      "READ",
      [
        "storage",
        "00290be5",
        null,
        "string"
      ]
    ],
    [
      "0057e860",
      "READ",
      [
        "storage",
        "002aca0d",
        null,
        "string"
      ]
    ],
    [
      "0057e8f4",
      "READ",
      [
        "storage",
        "002a5798",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057e844",
      "READ",
      [
        "storage",
        "002a0127",
        null,
        "string"
      ]
    ],
    [
      "0057e860",
      "READ",
      [
        "storage",
        "002bda85",
        null,
        "string"
      ]
    ],
    [
      "0057e8f4",
      "READ",
      [
        "storage",
        "002b61c6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b95c.md#insn-0055b988) · [`0055b990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b95c.md#insn-0055b990) · [`0055b9a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055b95c.md#insn-0055b9a4)
- 新版 `0057e820`（命令位置の公開資料なし） · `0057e828`（命令位置の公開資料なし） · `0057e83c`（命令位置の公開資料なし）

~~~diff
- 0055b988 ["INT_ADD", "register:40f0:8", ["const:55b988:8", "const:4:8"]]
- 0055b988 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057e820 ["INT_ADD", "register:40f0:8", ["const:57e820:8", "const:4:8"]]
+ 0057e820 ["CALL", null, ["callee:00588e2c:8"]]
- 0055b988 bytes 83290094
+ 0057e820 bytes 83290094
- 0055b990 ["INT_ADD", "register:40f0:8", ["const:55b990:8", "const:4:8"]]
- 0055b990 ["CALL", null, ["callee:0058911c:8"]]
+ 0057e828 ["INT_ADD", "register:40f0:8", ["const:57e828:8", "const:4:8"]]
+ 0057e828 ["CALL", null, ["callee:0058911c:8"]]
- 0055b990 bytes 3d2a0094
+ 0057e828 bytes 3d2a0094
- 0055b9a4 ["COPY", "register:4040:8", ["const:290000:8"]]
+ 0057e83c ["COPY", "register:4040:8", ["const:2a0000:8"]]
- 0055b9a4 bytes a8e9ffb0
+ 0057e83c bytes 08e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-050aefdb8b17cdf7a0664066543e8784"></a>

### [`0055bf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bf90.md) → [`0057ee28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ee28.md) FUN_0057ee28

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "0055bfd0",
      "incomplete_value": true,
      "site": "0055bfe0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:290000:8"
              ],
              [
                "leaf",
                "const:bf1:8"
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
    "old": {
      "definition_site": "0055bfe4",
      "incomplete_value": true,
      "site": "0055bfe4",
      "value": [
        "LOAD",
        "8",
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
      "0057ee68",
      "READ",
      [
        "storage",
        "00290bf1",
        null,
        "string"
      ]
    ],
    [
      "0057ee70",
      "READ",
      [
        "storage",
        "00290bfe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057ee68",
      "READ",
      [
        "storage",
        "002a0133",
        null,
        "string"
      ]
    ],
    [
      "0057ee70",
      "READ",
      [
        "storage",
        "002a0140",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055bfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bf90.md#insn-0055bfb8) · [`0055bfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bf90.md#insn-0055bfc0) · [`0055bfc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055b/0055bf90.md#insn-0055bfc8)
- 新版 `0057ee50`（命令位置の公開資料なし） · `0057ee58`（命令位置の公開資料なし） · `0057ee60`（命令位置の公開資料なし）

~~~diff
- 0055bfb8 ["INT_ADD", "register:40f0:8", ["const:55bfb8:8", "const:4:8"]]
- 0055bfb8 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057ee50 ["INT_ADD", "register:40f0:8", ["const:57ee50:8", "const:4:8"]]
+ 0057ee50 ["CALL", null, ["callee:00588e2c:8"]]
- 0055bfb8 bytes f7270094
+ 0057ee50 bytes f7270094
- 0055bfc0 ["INT_ADD", "register:40f0:8", ["const:55bfc0:8", "const:4:8"]]
- 0055bfc0 ["CALL", null, ["callee:0058911c:8"]]
+ 0057ee58 ["INT_ADD", "register:40f0:8", ["const:57ee58:8", "const:4:8"]]
+ 0057ee58 ["CALL", null, ["callee:0058911c:8"]]
- 0055bfc0 bytes b1280094
+ 0057ee58 bytes b1280094
- 0055bfc8 ["COPY", "register:4048:8", ["const:290000:8"]]
+ 0057ee60 ["COPY", "register:4048:8", ["const:2a0000:8"]]
- 0055bfc8 bytes a9e9ffb0
+ 0057ee60 bytes 09e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c7f84ca951b0c733e07bb5fed56e5f7"></a>

### [`0055c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c104.md) → [`0057ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057e/0057ef9c.md) FUN_0057ef9c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "0055c150",
      "incomplete_value": true,
      "site": "0055c16c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:295000:8"
              ],
              [
                "leaf",
                "const:b9f:8"
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
      "0057efe8",
      "READ",
      [
        "storage",
        "00295b9f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057efe8",
      "READ",
      [
        "storage",
        "002a55d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c104.md#insn-0055c12c) · [`0055c134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c104.md#insn-0055c134) · [`0055c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c104.md#insn-0055c13c)
- 新版 `0057efc4`（命令位置の公開資料なし） · `0057efcc`（命令位置の公開資料なし） · `0057efd4`（命令位置の公開資料なし）

~~~diff
- 0055c12c ["INT_ADD", "register:40f0:8", ["const:55c12c:8", "const:4:8"]]
- 0055c12c ["CALL", null, ["callee:00588e2c:8"]]
+ 0057efc4 ["INT_ADD", "register:40f0:8", ["const:57efc4:8", "const:4:8"]]
+ 0057efc4 ["CALL", null, ["callee:00588e2c:8"]]
- 0055c12c bytes 9a270094
+ 0057efc4 bytes 9a270094
- 0055c134 ["INT_ADD", "register:40f0:8", ["const:55c134:8", "const:4:8"]]
- 0055c134 ["CALL", null, ["callee:0058911c:8"]]
+ 0057efcc ["INT_ADD", "register:40f0:8", ["const:57efcc:8", "const:4:8"]]
+ 0057efcc ["CALL", null, ["callee:0058911c:8"]]
- 0055c134 bytes 54280094
+ 0057efcc bytes 54280094
- 0055c13c ["COPY", "register:4048:8", ["const:295000:8"]]
+ 0057efd4 ["COPY", "register:4048:8", ["const:2a5000:8"]]
- 0055c13c bytes c9e9ffb0
+ 0057efd4 bytes 29e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aab044ff02b206349ffe111ea7d8e5a7"></a>

### [`0055c284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c284.md) → [`0057f11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f11c.md) FUN_0057f11c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "0055c2d0",
      "incomplete_value": true,
      "site": "0055c2ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cb9:8"
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
      "0057f168",
      "READ",
      [
        "storage",
        "0028fcb9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f168",
      "READ",
      [
        "storage",
        "0029f0f9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c284.md#insn-0055c2ac) · [`0055c2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c284.md#insn-0055c2b4) · [`0055c2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c284.md#insn-0055c2bc)
- 新版 `0057f144`（命令位置の公開資料なし） · `0057f14c`（命令位置の公開資料なし） · `0057f154`（命令位置の公開資料なし）

~~~diff
- 0055c2ac ["INT_ADD", "register:40f0:8", ["const:55c2ac:8", "const:4:8"]]
- 0055c2ac ["CALL", null, ["callee:00588e2c:8"]]
+ 0057f144 ["INT_ADD", "register:40f0:8", ["const:57f144:8", "const:4:8"]]
+ 0057f144 ["CALL", null, ["callee:00588e2c:8"]]
- 0055c2ac bytes 3a270094
+ 0057f144 bytes 3a270094
- 0055c2b4 ["INT_ADD", "register:40f0:8", ["const:55c2b4:8", "const:4:8"]]
- 0055c2b4 ["CALL", null, ["callee:0058911c:8"]]
+ 0057f14c ["INT_ADD", "register:40f0:8", ["const:57f14c:8", "const:4:8"]]
+ 0057f14c ["CALL", null, ["callee:0058911c:8"]]
- 0055c2b4 bytes f4270094
+ 0057f14c bytes f4270094
- 0055c2bc ["COPY", "register:4048:8", ["const:28f000:8"]]
+ 0057f154 ["COPY", "register:4048:8", ["const:29f000:8"]]
- 0055c2bc bytes 89e9fff0
+ 0057f154 bytes 09e9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c94a9fca0c771d936d9e69e5c65f5a24"></a>

### [`0055c3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c3fc.md) → [`0057f294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f294.md) FUN_0057f294

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "0055c448",
      "incomplete_value": true,
      "site": "0055c458",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:745:8"
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
    "old": {
      "definition_site": "0055c460",
      "incomplete_value": true,
      "site": "0055c460",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "0055c45c",
      "incomplete_value": true,
      "site": "0055c474",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057f2e0",
      "READ",
      [
        "storage",
        "0029c745",
        null,
        "string"
      ]
    ],
    [
      "0057f2e4",
      "READ",
      [
        "storage",
        "0029c754",
        null,
        "string"
      ]
    ],
    [
      "0057f2f4",
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
      "0057f2e0",
      "READ",
      [
        "storage",
        "002ac8de",
        null,
        "string"
      ]
    ],
    [
      "0057f2e4",
      "READ",
      [
        "storage",
        "002ac8ed",
        null,
        "string"
      ]
    ],
    [
      "0057f2f4",
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

- 旧版 [`0055c424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c3fc.md#insn-0055c424) · [`0055c42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c3fc.md#insn-0055c42c) · [`0055c438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c3fc.md#insn-0055c438)
- 新版 `0057f2bc`（命令位置の公開資料なし） · `0057f2c4`（命令位置の公開資料なし） · `0057f2d0`（命令位置の公開資料なし）

~~~diff
- 0055c424 ["INT_ADD", "register:40f0:8", ["const:55c424:8", "const:4:8"]]
- 0055c424 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057f2bc ["INT_ADD", "register:40f0:8", ["const:57f2bc:8", "const:4:8"]]
+ 0057f2bc ["CALL", null, ["callee:00588e2c:8"]]
- 0055c424 bytes dc260094
+ 0057f2bc bytes dc260094
- 0055c42c ["INT_ADD", "register:40f0:8", ["const:55c42c:8", "const:4:8"]]
- 0055c42c ["CALL", null, ["callee:0058911c:8"]]
+ 0057f2c4 ["INT_ADD", "register:40f0:8", ["const:57f2c4:8", "const:4:8"]]
+ 0057f2c4 ["CALL", null, ["callee:0058911c:8"]]
- 0055c42c bytes 96270094
+ 0057f2c4 bytes 96270094
- 0055c438 ["INT_ADD", "register:40f0:8", ["const:55c438:8", "const:4:8"]]
- 0055c438 ["CALL", null, ["callee:00c57a90:8"]]
+ 0057f2d0 ["INT_ADD", "register:40f0:8", ["const:57f2d0:8", "const:4:8"]]
+ 0057f2d0 ["CALL", null, ["callee:00c57a90:8"]]
- 0055c438 bytes 02fb1994
+ 0057f2d0 bytes f0611b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b7c812d3d2fb84e5b173aec81855cfd"></a>

### [`0055c58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c58c.md) → [`0057f424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f424.md) FUN_0057f424

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00558f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0057bdcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057bdcc.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)

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
    "old": {
      "definition_site": "0055c5dc",
      "incomplete_value": true,
      "site": "0055c5f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b21:8"
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
    "old": {
      "definition_site": "0055c5f8",
      "incomplete_value": true,
      "site": "0055c604",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:670:8"
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
    "old": {
      "definition_site": "0055c608",
      "incomplete_value": true,
      "site": "0055c608",
      "value": [
        "LOAD",
        "8",
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
      "0057f474",
      "READ",
      [
        "storage",
        "002adb21",
        null,
        "string"
      ]
    ],
    [
      "0057f490",
      "READ",
      [
        "storage",
        "002a4670",
        null,
        "string"
      ]
    ],
    [
      "0057f494",
      "READ",
      [
        "storage",
        "002a467e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f474",
      "READ",
      [
        "storage",
        "002bee47",
        null,
        "string"
      ]
    ],
    [
      "0057f490",
      "READ",
      [
        "storage",
        "002b4edd",
        null,
        "string"
      ]
    ],
    [
      "0057f494",
      "READ",
      [
        "storage",
        "002b4eeb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c58c.md#insn-0055c5bc) · [`0055c5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c58c.md#insn-0055c5c4) · [`0055c5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c58c.md#insn-0055c5cc)
- 新版 `0057f454`（命令位置の公開資料なし） · `0057f45c`（命令位置の公開資料なし） · `0057f464`（命令位置の公開資料なし）

~~~diff
- 0055c5bc ["INT_ADD", "register:40f0:8", ["const:55c5bc:8", "const:4:8"]]
- 0055c5bc ["CALL", null, ["callee:00588e2c:8"]]
+ 0057f454 ["INT_ADD", "register:40f0:8", ["const:57f454:8", "const:4:8"]]
+ 0057f454 ["CALL", null, ["callee:00588e2c:8"]]
- 0055c5bc bytes 76260094
+ 0057f454 bytes 76260094
- 0055c5c4 ["INT_ADD", "register:40f0:8", ["const:55c5c4:8", "const:4:8"]]
- 0055c5c4 ["CALL", null, ["callee:0058911c:8"]]
+ 0057f45c ["INT_ADD", "register:40f0:8", ["const:57f45c:8", "const:4:8"]]
+ 0057f45c ["CALL", null, ["callee:0058911c:8"]]
- 0055c5c4 bytes 30270094
+ 0057f45c bytes 30270094
- 0055c5cc ["COPY", "register:4048:8", ["const:2ad000:8"]]
+ 0057f464 ["COPY", "register:4048:8", ["const:2be000:8"]]
- 0055c5cc bytes 89eaffb0
+ 0057f464 bytes e9e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49520dca9ea5291f31e09e882cd0ecbc"></a>

### [`0055c754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c754.md) → [`0057f5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f5ec.md) FUN_0057f5ec

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056627c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md)
- 新版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`00589114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589114.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)

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
    "old": {
      "definition_site": "0055c79c",
      "incomplete_value": true,
      "site": "0055c7ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7a8:8"
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
    "old": {
      "definition_site": "0055c7c8",
      "incomplete_value": true,
      "site": "0055c7d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a4b:8"
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
    "old": {
      "definition_site": "0055c7cc",
      "incomplete_value": true,
      "site": "0055c7dc",
      "value": [
        "LOAD",
        "8",
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
      "0057f634",
      "READ",
      [
        "storage",
        "002a57a8",
        null,
        "string"
      ]
    ],
    [
      "0057f660",
      "READ",
      [
        "storage",
        "002aea4b",
        null,
        "string"
      ]
    ],
    [
      "0057f664",
      "READ",
      [
        "storage",
        "002aea5b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f634",
      "READ",
      [
        "storage",
        "002b61d6",
        null,
        "string"
      ]
    ],
    [
      "0057f660",
      "READ",
      [
        "storage",
        "002bff2f",
        null,
        "string"
      ]
    ],
    [
      "0057f664",
      "READ",
      [
        "storage",
        "002bff3f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c754.md#insn-0055c784) · [`0055c78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c754.md#insn-0055c78c) · [`0055c790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c754.md#insn-0055c790)
- 新版 `0057f61c`（命令位置の公開資料なし） · `0057f624`（命令位置の公開資料なし） · `0057f628`（命令位置の公開資料なし）

~~~diff
- 0055c784 ["INT_ADD", "register:40f0:8", ["const:55c784:8", "const:4:8"]]
- 0055c784 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057f61c ["INT_ADD", "register:40f0:8", ["const:57f61c:8", "const:4:8"]]
+ 0057f61c ["CALL", null, ["callee:00588e2c:8"]]
- 0055c784 bytes 04260094
+ 0057f61c bytes 04260094
- 0055c78c ["INT_ADD", "register:40f0:8", ["const:55c78c:8", "const:4:8"]]
- 0055c78c ["CALL", null, ["callee:0058911c:8"]]
+ 0057f624 ["INT_ADD", "register:40f0:8", ["const:57f624:8", "const:4:8"]]
+ 0057f624 ["CALL", null, ["callee:0058911c:8"]]
- 0055c78c bytes be260094
+ 0057f624 bytes be260094
- 0055c790 ["COPY", "register:4048:8", ["const:2a5000:8"]]
+ 0057f628 ["COPY", "register:4048:8", ["const:2b6000:8"]]
- 0055c790 bytes 49eaffb0
+ 0057f628 bytes a9e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a13d388d2ccbf9c71466d1d24f2aa8e"></a>

### [`0055c994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c994.md) → [`0057f82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057f/0057f82c.md) FUN_0057f82c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005398ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005398ec.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 0件  · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`0055c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

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
    "old": {
      "definition_site": "0055ca04",
      "incomplete_value": true,
      "site": "0055ca04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e14:8"
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
    "old": {
      "definition_site": "0055ca20",
      "incomplete_value": true,
      "site": "0055ca30",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:1e0:8"
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
      "0057f888",
      "READ",
      [
        "storage",
        "00299e14",
        null,
        "string"
      ]
    ],
    [
      "0057f890",
      "READ",
      [
        "storage",
        "00299e19",
        null,
        "string"
      ]
    ],
    [
      "0057f8b8",
      "READ",
      [
        "storage",
        "002b11e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057f888",
      "READ",
      [
        "storage",
        "002a9ced",
        null,
        "string"
      ]
    ],
    [
      "0057f890",
      "READ",
      [
        "storage",
        "002a9cf2",
        null,
        "string"
      ]
    ],
    [
      "0057f8b8",
      "READ",
      [
        "storage",
        "002c2820",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c994.md#insn-0055c9d8) · [`0055c9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c994.md#insn-0055c9e0) · [`0055c9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055c/0055c994.md#insn-0055c9e8)
- 新版 `0057f870`（命令位置の公開資料なし） · `0057f878`（命令位置の公開資料なし） · `0057f880`（命令位置の公開資料なし）

~~~diff
- 0055c9d8 ["INT_ADD", "register:40f0:8", ["const:55c9d8:8", "const:4:8"]]
- 0055c9d8 ["CALL", null, ["callee:00588e2c:8"]]
+ 0057f870 ["INT_ADD", "register:40f0:8", ["const:57f870:8", "const:4:8"]]
+ 0057f870 ["CALL", null, ["callee:00588e2c:8"]]
- 0055c9d8 bytes 6f250094
+ 0057f870 bytes 6f250094
- 0055c9e0 ["INT_ADD", "register:40f0:8", ["const:55c9e0:8", "const:4:8"]]
- 0055c9e0 ["CALL", null, ["callee:0058911c:8"]]
+ 0057f878 ["INT_ADD", "register:40f0:8", ["const:57f878:8", "const:4:8"]]
+ 0057f878 ["CALL", null, ["callee:0058911c:8"]]
- 0055c9e0 bytes 29260094
+ 0057f878 bytes 29260094
- 0055c9e8 ["COPY", "register:4048:8", ["const:299000:8"]]
+ 0057f880 ["COPY", "register:4048:8", ["const:2a9000:8"]]
- 0055c9e8 bytes e9e9ffb0
+ 0057f880 bytes 49e9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

