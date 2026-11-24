# v15.7.4 → v16.0.0 · 最優先の変更候補 (73)

[一覧の目次](README.md)

<a id="compare-edc485074a81436db14213b7cd3fb3fb"></a>

### [`00b83d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83d9c.md) → [`00c007e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c007e4.md) FUN_00c007e4

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83d94.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c007dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c007dc.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00838",
      "incomplete_value": true,
      "site": "00c0083c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b83df0",
      "incomplete_value": true,
      "site": "00b83df4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c0086c",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b83e24",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c00838",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c00838",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0086c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c00838",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00838",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0086c",
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

- 旧版 [`00b83df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83d9c.md#insn-00b83df4) · [`00b83e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83d9c.md#insn-00b83e24) · [`00b83dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83d9c.md#insn-00b83dc8)
- 新版 [`00c0083c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c007e4.md#insn-00c0083c) · [`00c0086c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c007e4.md#insn-00c0086c) · [`00c00810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c007e4.md#insn-00c00810)

~~~diff
- 00b83df4 ["INT_ADD", "register:40f0:8", ["const:b83df4:8", "const:4:8"]]
- 00b83df4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c0083c ["INT_ADD", "register:40f0:8", ["const:c0083c:8", "const:4:8"]]
+ 00c0083c ["CALL", null, ["callee:00c57e80:8"]]
- 00b83df4 bytes 8f5d0194
+ 00c0083c bytes 915d0194
- 00b83e24 ["INT_ADD", "register:40f0:8", ["const:b83e24:8", "const:4:8"]]
- 00b83e24 ["CALL", null, ["ram:bdb440:8"]]
+ 00c0086c ["INT_ADD", "register:40f0:8", ["const:c0086c:8", "const:4:8"]]
+ 00c0086c ["CALL", null, ["ram:c57e90:8"]]
- 00b83e24 bytes 875d0194
+ 00c0086c bytes 895d0194
- 00b83dc8 ["INT_ADD", "register:40f0:8", ["const:b83dc8:8", "const:4:8"]]
- 00b83dc8 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c00810 ["INT_ADD", "register:40f0:8", ["const:c00810:8", "const:4:8"]]
+ 00c00810 ["CALL", null, ["callee:00c5e020:8"]]
- 00b83dc8 bytes 96750194
+ 00c00810 bytes 04760194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5761cf8a76cdf3637c6ed5d5320bffec"></a>

### [`00b83f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83f18.md) → [`00c00960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00960.md) FUN_00c00960

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83f10.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c00958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00958.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c009b4",
      "incomplete_value": true,
      "site": "00c009b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b83f6c",
      "incomplete_value": true,
      "site": "00b83f70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c009e8",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b83fa0",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c009b4",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c009b4",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c009e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c009b4",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c009b4",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c009e8",
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

- 旧版 [`00b83f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83f18.md#insn-00b83f70) · [`00b83fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83f18.md#insn-00b83fa0) · [`00b83f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83f18.md#insn-00b83f44)
- 新版 [`00c009b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00960.md#insn-00c009b8) · [`00c009e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00960.md#insn-00c009e8) · [`00c0098c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00960.md#insn-00c0098c)

~~~diff
- 00b83f70 ["INT_ADD", "register:40f0:8", ["const:b83f70:8", "const:4:8"]]
- 00b83f70 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c009b8 ["INT_ADD", "register:40f0:8", ["const:c009b8:8", "const:4:8"]]
+ 00c009b8 ["CALL", null, ["callee:00c57e80:8"]]
- 00b83f70 bytes 305d0194
+ 00c009b8 bytes 325d0194
- 00b83fa0 ["INT_ADD", "register:40f0:8", ["const:b83fa0:8", "const:4:8"]]
- 00b83fa0 ["CALL", null, ["ram:bdb440:8"]]
+ 00c009e8 ["INT_ADD", "register:40f0:8", ["const:c009e8:8", "const:4:8"]]
+ 00c009e8 ["CALL", null, ["ram:c57e90:8"]]
- 00b83fa0 bytes 285d0194
+ 00c009e8 bytes 2a5d0194
- 00b83f44 ["INT_ADD", "register:40f0:8", ["const:b83f44:8", "const:4:8"]]
- 00b83f44 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c0098c ["INT_ADD", "register:40f0:8", ["const:c0098c:8", "const:4:8"]]
+ 00c0098c ["CALL", null, ["callee:00c5e020:8"]]
- 00b83f44 bytes 37750194
+ 00c0098c bytes a5750194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7929dfd47c5bba804637eec0e104fbb"></a>

### [`00b84050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84050.md) → [`00c00a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00a98.md) FUN_00c00a98

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b84048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84048.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c00a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00a90.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00aec",
      "incomplete_value": true,
      "site": "00c00af0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b840a4",
      "incomplete_value": true,
      "site": "00b840a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c00b20",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b840d8",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c00aec",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c00aec",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00b20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c00aec",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00aec",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00b20",
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

- 旧版 [`00b840a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84050.md#insn-00b840a8) · [`00b840d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84050.md#insn-00b840d8) · [`00b8407c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84050.md#insn-00b8407c)
- 新版 [`00c00af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00a98.md#insn-00c00af0) · [`00c00b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00a98.md#insn-00c00b20) · [`00c00ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00a98.md#insn-00c00ac4)

~~~diff
- 00b840a8 ["INT_ADD", "register:40f0:8", ["const:b840a8:8", "const:4:8"]]
- 00b840a8 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c00af0 ["INT_ADD", "register:40f0:8", ["const:c00af0:8", "const:4:8"]]
+ 00c00af0 ["CALL", null, ["callee:00c57e80:8"]]
- 00b840a8 bytes e25c0194
+ 00c00af0 bytes e45c0194
- 00b840d8 ["INT_ADD", "register:40f0:8", ["const:b840d8:8", "const:4:8"]]
- 00b840d8 ["CALL", null, ["ram:bdb440:8"]]
+ 00c00b20 ["INT_ADD", "register:40f0:8", ["const:c00b20:8", "const:4:8"]]
+ 00c00b20 ["CALL", null, ["ram:c57e90:8"]]
- 00b840d8 bytes da5c0194
+ 00c00b20 bytes dc5c0194
- 00b8407c ["INT_ADD", "register:40f0:8", ["const:b8407c:8", "const:4:8"]]
- 00b8407c ["CALL", null, ["callee:00c5e020:8"]]
+ 00c00ac4 ["INT_ADD", "register:40f0:8", ["const:c00ac4:8", "const:4:8"]]
+ 00c00ac4 ["CALL", null, ["callee:00c5e020:8"]]
- 00b8407c bytes e9740194
+ 00c00ac4 bytes 57750194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25195ac0ceb2a16de0784393fdee9759"></a>

### [`00b84188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84188.md) → [`00c00bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00bd0.md) FUN_00c00bd0

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b84180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84180.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c00bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00bc8.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00c24",
      "incomplete_value": true,
      "site": "00c00c28",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b841dc",
      "incomplete_value": true,
      "site": "00b841e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c00c58",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b84210",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c00c24",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c00c24",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00c58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c00c24",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00c24",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00c58",
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

- 旧版 [`00b841e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84188.md#insn-00b841e0) · [`00b84210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84188.md#insn-00b84210) · [`00b841b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84188.md#insn-00b841b4)
- 新版 [`00c00c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00bd0.md#insn-00c00c28) · [`00c00c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00bd0.md#insn-00c00c58) · [`00c00bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00bd0.md#insn-00c00bfc)

~~~diff
- 00b841e0 ["INT_ADD", "register:40f0:8", ["const:b841e0:8", "const:4:8"]]
- 00b841e0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c00c28 ["INT_ADD", "register:40f0:8", ["const:c00c28:8", "const:4:8"]]
+ 00c00c28 ["CALL", null, ["callee:00c57e80:8"]]
- 00b841e0 bytes 945c0194
+ 00c00c28 bytes 965c0194
- 00b84210 ["INT_ADD", "register:40f0:8", ["const:b84210:8", "const:4:8"]]
- 00b84210 ["CALL", null, ["ram:bdb440:8"]]
+ 00c00c58 ["INT_ADD", "register:40f0:8", ["const:c00c58:8", "const:4:8"]]
+ 00c00c58 ["CALL", null, ["ram:c57e90:8"]]
- 00b84210 bytes 8c5c0194
+ 00c00c58 bytes 8e5c0194
- 00b841b4 ["INT_ADD", "register:40f0:8", ["const:b841b4:8", "const:4:8"]]
- 00b841b4 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c00bfc ["INT_ADD", "register:40f0:8", ["const:c00bfc:8", "const:4:8"]]
+ 00c00bfc ["CALL", null, ["callee:00c5e020:8"]]
- 00b841b4 bytes 9b740194
+ 00c00bfc bytes 09750194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec9c810ca7f7f4c968f691f3bfee8a0d"></a>

### [`00b842c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b842c0.md) → [`00c00d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00d08.md) FUN_00c00d08

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b842b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b842b8.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c00d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00d00.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00d5c",
      "incomplete_value": true,
      "site": "00c00d60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84314",
      "incomplete_value": true,
      "site": "00b84318",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c00d90",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b84348",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c00d5c",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c00d5c",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00d90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c00d5c",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00d5c",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00d90",
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

- 旧版 [`00b84318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b842c0.md#insn-00b84318) · [`00b84348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b842c0.md#insn-00b84348) · [`00b842ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b842c0.md#insn-00b842ec)
- 新版 [`00c00d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00d08.md#insn-00c00d60) · [`00c00d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00d08.md#insn-00c00d90) · [`00c00d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00d08.md#insn-00c00d34)

~~~diff
- 00b84318 ["INT_ADD", "register:40f0:8", ["const:b84318:8", "const:4:8"]]
- 00b84318 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c00d60 ["INT_ADD", "register:40f0:8", ["const:c00d60:8", "const:4:8"]]
+ 00c00d60 ["CALL", null, ["callee:00c57e80:8"]]
- 00b84318 bytes 465c0194
+ 00c00d60 bytes 485c0194
- 00b84348 ["INT_ADD", "register:40f0:8", ["const:b84348:8", "const:4:8"]]
- 00b84348 ["CALL", null, ["ram:bdb440:8"]]
+ 00c00d90 ["INT_ADD", "register:40f0:8", ["const:c00d90:8", "const:4:8"]]
+ 00c00d90 ["CALL", null, ["ram:c57e90:8"]]
- 00b84348 bytes 3e5c0194
+ 00c00d90 bytes 405c0194
- 00b842ec ["INT_ADD", "register:40f0:8", ["const:b842ec:8", "const:4:8"]]
- 00b842ec ["CALL", null, ["callee:00c5e020:8"]]
+ 00c00d34 ["INT_ADD", "register:40f0:8", ["const:c00d34:8", "const:4:8"]]
+ 00c00d34 ["CALL", null, ["callee:00c5e020:8"]]
- 00b842ec bytes 4d740194
+ 00c00d34 bytes bb740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e6fbd47990c53b0a696adac7fa4b9b9"></a>

### [`00b843f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b843f8.md) → [`00c00e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00e40.md) FUN_00c00e40

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b843f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b843f0.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c00e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00e38.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00e94",
      "incomplete_value": true,
      "site": "00c00e98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8444c",
      "incomplete_value": true,
      "site": "00b84450",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c00ec8",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b84480",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c00e94",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c00e94",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00ec8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c00e94",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00e94",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00ec8",
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

- 旧版 [`00b84450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b843f8.md#insn-00b84450) · [`00b84480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b843f8.md#insn-00b84480) · [`00b84424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b843f8.md#insn-00b84424)
- 新版 [`00c00e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00e40.md#insn-00c00e98) · [`00c00ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00e40.md#insn-00c00ec8) · [`00c00e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00e40.md#insn-00c00e6c)

~~~diff
- 00b84450 ["INT_ADD", "register:40f0:8", ["const:b84450:8", "const:4:8"]]
- 00b84450 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c00e98 ["INT_ADD", "register:40f0:8", ["const:c00e98:8", "const:4:8"]]
+ 00c00e98 ["CALL", null, ["callee:00c57e80:8"]]
- 00b84450 bytes f85b0194
+ 00c00e98 bytes fa5b0194
- 00b84480 ["INT_ADD", "register:40f0:8", ["const:b84480:8", "const:4:8"]]
- 00b84480 ["CALL", null, ["ram:bdb440:8"]]
+ 00c00ec8 ["INT_ADD", "register:40f0:8", ["const:c00ec8:8", "const:4:8"]]
+ 00c00ec8 ["CALL", null, ["ram:c57e90:8"]]
- 00b84480 bytes f05b0194
+ 00c00ec8 bytes f25b0194
- 00b84424 ["INT_ADD", "register:40f0:8", ["const:b84424:8", "const:4:8"]]
- 00b84424 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c00e6c ["INT_ADD", "register:40f0:8", ["const:c00e6c:8", "const:4:8"]]
+ 00c00e6c ["CALL", null, ["callee:00c5e020:8"]]
- 00b84424 bytes ff730194
+ 00c00e6c bytes 6d740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c47ab0c15745287b9314bf47a886b846"></a>

### [`00b84530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84530.md) → [`00c00f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00f78.md) FUN_00c00f78

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b84528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84528.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c00f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00f70.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00fcc",
      "incomplete_value": true,
      "site": "00c00fd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84584",
      "incomplete_value": true,
      "site": "00b84588",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c01000",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b845b8",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c00fcc",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c00fcc",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c01000",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c00fcc",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00fcc",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c01000",
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

- 旧版 [`00b84588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84530.md#insn-00b84588) · [`00b845b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84530.md#insn-00b845b8) · [`00b8455c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84530.md#insn-00b8455c)
- 新版 [`00c00fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00f78.md#insn-00c00fd0) · [`00c01000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00f78.md#insn-00c01000) · [`00c00fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00f78.md#insn-00c00fa4)

~~~diff
- 00b84588 ["INT_ADD", "register:40f0:8", ["const:b84588:8", "const:4:8"]]
- 00b84588 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c00fd0 ["INT_ADD", "register:40f0:8", ["const:c00fd0:8", "const:4:8"]]
+ 00c00fd0 ["CALL", null, ["callee:00c57e80:8"]]
- 00b84588 bytes aa5b0194
+ 00c00fd0 bytes ac5b0194
- 00b845b8 ["INT_ADD", "register:40f0:8", ["const:b845b8:8", "const:4:8"]]
- 00b845b8 ["CALL", null, ["ram:bdb440:8"]]
+ 00c01000 ["INT_ADD", "register:40f0:8", ["const:c01000:8", "const:4:8"]]
+ 00c01000 ["CALL", null, ["ram:c57e90:8"]]
- 00b845b8 bytes a25b0194
+ 00c01000 bytes a45b0194
- 00b8455c ["INT_ADD", "register:40f0:8", ["const:b8455c:8", "const:4:8"]]
- 00b8455c ["CALL", null, ["callee:00c5e020:8"]]
+ 00c00fa4 ["INT_ADD", "register:40f0:8", ["const:c00fa4:8", "const:4:8"]]
+ 00c00fa4 ["CALL", null, ["callee:00c5e020:8"]]
- 00b8455c bytes b1730194
+ 00c00fa4 bytes 1f740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71bea46cd49a60dee6031b326b9fef70"></a>

### [`00b84668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84668.md) → [`00c010b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c010b0.md) FUN_00c010b0

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b84660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84660.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c010a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c010a8.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c01104",
      "incomplete_value": true,
      "site": "00c01108",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b846bc",
      "incomplete_value": true,
      "site": "00b846c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b846f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c01138"
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
      "unmatched:00b846bc",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b846bc",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b846f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c01104",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c01104",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c01138",
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

- 旧版 [`00b846c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84668.md#insn-00b846c0) · [`00b846f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84668.md#insn-00b846f0)
- 新版 [`00c01108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c010b0.md#insn-00c01108) · [`00c01138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c010b0.md#insn-00c01138)

~~~diff
- 00b846c0 ["INT_ADD", "register:40f0:8", ["const:b846c0:8", "const:4:8"]]
- 00b846c0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c01108 ["INT_ADD", "register:40f0:8", ["const:c01108:8", "const:4:8"]]
+ 00c01108 ["CALL", null, ["callee:00c57e80:8"]]
- 00b846c0 bytes 5c5b0194
+ 00c01108 bytes 5e5b0194
- 00b846f0 ["INT_ADD", "register:40f0:8", ["const:b846f0:8", "const:4:8"]]
- 00b846f0 ["CALL", null, ["ram:bdb440:8"]]
- 00b846f0 bytes 545b0194
+ 00c01138 ["INT_ADD", "register:40f0:8", ["const:c01138:8", "const:4:8"]]
+ 00c01138 ["CALL", null, ["ram:c57e90:8"]]
+ 00c01138 bytes 565b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9266da8e2d0d3e2f73919044ba653620"></a>

### [`00b847a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b847a0.md) → [`00c011e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c011e8.md) FUN_00c011e8

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b84798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84798.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c011e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c011e0.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0123c",
      "incomplete_value": true,
      "site": "00c01240",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b847f4",
      "incomplete_value": true,
      "site": "00b847f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c01270",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b84828",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c0123c",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c0123c",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c01270",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c0123c",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c0123c",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c01270",
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

- 旧版 [`00b847f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b847a0.md#insn-00b847f8) · [`00b84828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b847a0.md#insn-00b84828) · [`00b847cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b847a0.md#insn-00b847cc)
- 新版 [`00c01240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c011e8.md#insn-00c01240) · [`00c01270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c011e8.md#insn-00c01270) · [`00c01214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c011e8.md#insn-00c01214)

~~~diff
- 00b847f8 ["INT_ADD", "register:40f0:8", ["const:b847f8:8", "const:4:8"]]
- 00b847f8 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c01240 ["INT_ADD", "register:40f0:8", ["const:c01240:8", "const:4:8"]]
+ 00c01240 ["CALL", null, ["callee:00c57e80:8"]]
- 00b847f8 bytes 0e5b0194
+ 00c01240 bytes 105b0194
- 00b84828 ["INT_ADD", "register:40f0:8", ["const:b84828:8", "const:4:8"]]
- 00b84828 ["CALL", null, ["ram:bdb440:8"]]
+ 00c01270 ["INT_ADD", "register:40f0:8", ["const:c01270:8", "const:4:8"]]
+ 00c01270 ["CALL", null, ["ram:c57e90:8"]]
- 00b84828 bytes 065b0194
+ 00c01270 bytes 085b0194
- 00b847cc ["INT_ADD", "register:40f0:8", ["const:b847cc:8", "const:4:8"]]
- 00b847cc ["CALL", null, ["callee:00c5e020:8"]]
+ 00c01214 ["INT_ADD", "register:40f0:8", ["const:c01214:8", "const:4:8"]]
+ 00c01214 ["CALL", null, ["callee:00c5e020:8"]]
- 00b847cc bytes 15730194
+ 00c01214 bytes 83730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcea05e929e49f03e5ee75c7907a7803"></a>

### [`00b848d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b848d8.md) → [`00c01320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01320.md) FUN_00c01320

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b848d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b848d0.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c01318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01318.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c01374",
      "incomplete_value": true,
      "site": "00c01378",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8492c",
      "incomplete_value": true,
      "site": "00b84930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84960"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c013a8"
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
      "unmatched:00b8492c",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b8492c",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b84960",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c01374",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c01374",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c013a8",
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

- 旧版 [`00b84930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b848d8.md#insn-00b84930) · [`00b84960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b848d8.md#insn-00b84960)
- 新版 [`00c01378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01320.md#insn-00c01378) · [`00c013a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01320.md#insn-00c013a8)

~~~diff
- 00b84930 ["INT_ADD", "register:40f0:8", ["const:b84930:8", "const:4:8"]]
- 00b84930 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c01378 ["INT_ADD", "register:40f0:8", ["const:c01378:8", "const:4:8"]]
+ 00c01378 ["CALL", null, ["callee:00c57e80:8"]]
- 00b84930 bytes c05a0194
+ 00c01378 bytes c25a0194
- 00b84960 ["INT_ADD", "register:40f0:8", ["const:b84960:8", "const:4:8"]]
- 00b84960 ["CALL", null, ["ram:bdb440:8"]]
- 00b84960 bytes b85a0194
+ 00c013a8 ["INT_ADD", "register:40f0:8", ["const:c013a8:8", "const:4:8"]]
+ 00c013a8 ["CALL", null, ["ram:c57e90:8"]]
+ 00c013a8 bytes ba5a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f26d08ebc58558501c44f738b0ef0b6"></a>

### [`00b84b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b5c.md) → [`00c015a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c015a4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEPwl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1440.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5e040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e040.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c015e4",
      "incomplete_value": true,
      "site": "00c015e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84b9c",
      "incomplete_value": true,
      "site": "00b84ba0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "site": "00c01604",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b84bbc",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c015e4",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00c015e4",
      "PARAM",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c01604",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c015e4",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c015e4",
      "PARAM",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c01604",
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

- 旧版 [`00b84ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b5c.md#insn-00b84ba0) · [`00b84bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b5c.md#insn-00b84bbc) · [`00b84b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84b5c.md#insn-00b84b90)
- 新版 [`00c015e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c015a4.md#insn-00c015e8) · [`00c01604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c015a4.md#insn-00c01604) · [`00c015d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c015a4.md#insn-00c015d8)

~~~diff
- 00b84ba0 ["INT_ADD", "register:40f0:8", ["const:b84ba0:8", "const:4:8"]]
- 00b84ba0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c015e8 ["INT_ADD", "register:40f0:8", ["const:c015e8:8", "const:4:8"]]
+ 00c015e8 ["CALL", null, ["callee:00c57e80:8"]]
- 00b84ba0 bytes 245a0194
+ 00c015e8 bytes 265a0194
- 00b84bbc ["INT_ADD", "register:40f0:8", ["const:b84bbc:8", "const:4:8"]]
- 00b84bbc ["CALL", null, ["ram:bdb440:8"]]
+ 00c01604 ["INT_ADD", "register:40f0:8", ["const:c01604:8", "const:4:8"]]
+ 00c01604 ["CALL", null, ["ram:c57e90:8"]]
- 00b84bbc bytes 215a0194
+ 00c01604 bytes 235a0194
- 00b84b90 ["INT_ADD", "register:40f0:8", ["const:b84b90:8", "const:4:8"]]
- 00b84b90 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c015d8 ["INT_ADD", "register:40f0:8", ["const:c015d8:8", "const:4:8"]]
+ 00c015d8 ["CALL", null, ["callee:00c57e70:8"]]
- 00b84b90 bytes 245a0194
+ 00c015d8 bytes 265a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7aa0484fe872140e2e530da1352a44f"></a>

### [`00b84c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84c00.md) → [`00c01648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01648.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getEPwlw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1440.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c5e040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e040.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.94% / 新版 98.94%

CFGの説明率　旧版 91.18% / 新版 93.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c01674",
      "incomplete_value": true,
      "site": "00c01684",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:10:8"
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
      "definition_site": "00b84c2c",
      "incomplete_value": true,
      "site": "00b84c3c",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b84c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84c00.md#insn-00b84c3c) · [`00b84c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84c00.md#insn-00b84c2c) · [`00b84c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84c00.md#insn-00b84c44)
- 新版 [`00c01684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01648.md#insn-00c01684) · [`00c0168c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01648.md#insn-00c0168c)

~~~diff
- 00b84c3c ["INT_ADD", "register:40f0:8", ["const:b84c3c:8", "const:4:8"]]
- 00b84c3c ["CALL", null, ["callee:00c5e020:8"]]
+ 00c01684 ["INT_ADD", "register:40f0:8", ["const:c01684:8", "const:4:8"]]
+ 00c01684 ["CALL", null, ["callee:00c5e020:8"]]
- 00b84c3c bytes f9710194
+ 00c01684 bytes 67720194
- 00b84c2c ["INT_SUB", "register:4000:8", ["register:40e8:8", "const:4:8"]]
- 00b84c2c bytes a01300d1
- 00b84c44 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b84c44 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 00c0168c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00c0168c ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00b84c44 bytes 48080034
+ 00c0168c bytes 48080034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c366a36d75c0dd42ae877a3ac76ecb60"></a>

### [`00b84dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84dd0.md) → [`00c01818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01818.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE3getERNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1450.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5e050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e050.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c01850",
      "incomplete_value": true,
      "site": "00c01854",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84e08",
      "incomplete_value": true,
      "site": "00b84e0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "site": "00c01870",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b84e28",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c01850",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00c01850",
      "PARAM",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c01870",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c01850",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c01850",
      "PARAM",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c01870",
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

- 旧版 [`00b84e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84dd0.md#insn-00b84e0c) · [`00b84e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84dd0.md#insn-00b84e28) · [`00b84dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84dd0.md#insn-00b84dfc)
- 新版 [`00c01854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01818.md#insn-00c01854) · [`00c01870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01818.md#insn-00c01870) · [`00c01844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01818.md#insn-00c01844)

~~~diff
- 00b84e0c ["INT_ADD", "register:40f0:8", ["const:b84e0c:8", "const:4:8"]]
- 00b84e0c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c01854 ["INT_ADD", "register:40f0:8", ["const:c01854:8", "const:4:8"]]
+ 00c01854 ["CALL", null, ["callee:00c57e80:8"]]
- 00b84e0c bytes 89590194
+ 00c01854 bytes 8b590194
- 00b84e28 ["INT_ADD", "register:40f0:8", ["const:b84e28:8", "const:4:8"]]
- 00b84e28 ["CALL", null, ["ram:bdb440:8"]]
+ 00c01870 ["INT_ADD", "register:40f0:8", ["const:c01870:8", "const:4:8"]]
+ 00c01870 ["CALL", null, ["ram:c57e90:8"]]
- 00b84e28 bytes 86590194
+ 00c01870 bytes 88590194
- 00b84dfc ["INT_ADD", "register:40f0:8", ["const:b84dfc:8", "const:4:8"]]
- 00b84dfc ["CALL", null, ["callee:00c57e70:8"]]
+ 00c01844 ["INT_ADD", "register:40f0:8", ["const:c01844:8", "const:4:8"]]
+ 00c01844 ["CALL", null, ["callee:00c57e70:8"]]
- 00b84dfc bytes 89590194
+ 00c01844 bytes 8b590194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dff3dfa25ec3f54d8196968f491c456c"></a>

### [`00b84fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84fc8.md) → [`00c01a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01a10.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7getlineEPwl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1460.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5e060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e060.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c01a50",
      "incomplete_value": true,
      "site": "00c01a54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b85008",
      "incomplete_value": true,
      "site": "00b8500c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "site": "00c01a70",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b85028",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c01a50",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00c01a50",
      "PARAM",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c01a70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c01a50",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c01a50",
      "PARAM",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c01a70",
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

- 旧版 [`00b8500c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84fc8.md#insn-00b8500c) · [`00b85028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84fc8.md#insn-00b85028) · [`00b84ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b84/00b84fc8.md#insn-00b84ffc)
- 新版 [`00c01a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01a10.md#insn-00c01a54) · [`00c01a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01a10.md#insn-00c01a70) · [`00c01a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01a10.md#insn-00c01a44)

~~~diff
- 00b8500c ["INT_ADD", "register:40f0:8", ["const:b8500c:8", "const:4:8"]]
- 00b8500c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c01a54 ["INT_ADD", "register:40f0:8", ["const:c01a54:8", "const:4:8"]]
+ 00c01a54 ["CALL", null, ["callee:00c57e80:8"]]
- 00b8500c bytes 09590194
+ 00c01a54 bytes 0b590194
- 00b85028 ["INT_ADD", "register:40f0:8", ["const:b85028:8", "const:4:8"]]
- 00b85028 ["CALL", null, ["ram:bdb440:8"]]
+ 00c01a70 ["INT_ADD", "register:40f0:8", ["const:c01a70:8", "const:4:8"]]
+ 00c01a70 ["CALL", null, ["ram:c57e90:8"]]
- 00b85028 bytes 06590194
+ 00c01a70 bytes 08590194
- 00b84ffc ["INT_ADD", "register:40f0:8", ["const:b84ffc:8", "const:4:8"]]
- 00b84ffc ["CALL", null, ["callee:00c57e70:8"]]
+ 00c01a44 ["INT_ADD", "register:40f0:8", ["const:c01a44:8", "const:4:8"]]
+ 00c01a44 ["CALL", null, ["callee:00c57e70:8"]]
- 00b84ffc bytes 09590194
+ 00c01a44 bytes 0b590194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4eb7cae8b810bb2a6f0e89166ece12a"></a>

### [`00b85b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85b0c.md) → [`00c02554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02554.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5tellgEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85b0c.md#insn-00b85b30) · [`00b85b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85b0c.md#insn-00b85b38) · [`00b85b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85b0c.md#insn-00b85b60)
- 新版 [`00c02578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02554.md#insn-00c02578) · [`00c02580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02554.md#insn-00c02580) · [`00c025a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02554.md#insn-00c025a8)

~~~diff
- 00b85b30 ["INT_ADD", "register:40f0:8", ["const:b85b30:8", "const:4:8"]]
- 00b85b30 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c02578 ["INT_ADD", "register:40f0:8", ["const:c02578:8", "const:4:8"]]
+ 00c02578 ["CALL", null, ["callee:00c5e020:8"]]
- 00b85b30 bytes 3c6e0194
+ 00c02578 bytes aa6e0194
- 00b85b38 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b85b38 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00c02580 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00c02580 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b85b38 bytes a8020034
+ 00c02580 bytes a8020034
- 00b85b60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85b60 ["INT_ADD", "register:40f0:8", ["const:b85b60:8", "const:4:8"]]
- 00b85b60 ["CALLIND", null, ["register:0:8"]]
+ 00c025a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c025a8 ["INT_ADD", "register:40f0:8", ["const:c025a8:8", "const:4:8"]]
+ 00c025a8 ["CALLIND", null, ["register:0:8"]]
- 00b85b60 bytes 00013fd6
+ 00c025a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a3bfc97386c532a0b921cc151b3daf1"></a>

### [`00b85d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85d18.md) → [`00c02760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02760.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgExNS_8ios_base7seekdirE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b85d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85d18.md#insn-00b85d54) · [`00b85d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85d18.md#insn-00b85d64) · [`00b85d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85d18.md#insn-00b85d6c)
- 新版 [`00c0279c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02760.md#insn-00c0279c) · [`00c027ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02760.md#insn-00c027ac) · [`00c027b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02760.md#insn-00c027b4)

~~~diff
- 00b85d54 ["INT_ADD", "register:40f0:8", ["const:b85d54:8", "const:4:8"]]
- 00b85d54 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00c0279c ["INT_ADD", "register:40f0:8", ["const:c0279c:8", "const:4:8"]]
+ 00c0279c ["CALL", null, ["callee:00c57ea0:8"]]
- 00b85d54 bytes bf550194
+ 00c0279c bytes c1550194
- 00b85d64 ["INT_ADD", "register:40f0:8", ["const:b85d64:8", "const:4:8"]]
- 00b85d64 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c027ac ["INT_ADD", "register:40f0:8", ["const:c027ac:8", "const:4:8"]]
+ 00c027ac ["CALL", null, ["callee:00c5e020:8"]]
- 00b85d64 bytes af6d0194
+ 00c027ac bytes 1d6e0194
- 00b85d6c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b85d6c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00c027b4 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00c027b4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b85d6c bytes 88020034
+ 00c027b4 bytes 88020034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c70820f1b4853bdfda75aec77df9a7a"></a>

### [`00b85e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85e80.md) → [`00c028c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c028c8.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEEC1EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c028f4",
      "incomplete_value": true,
      "site": "00c028f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b85eac",
      "incomplete_value": true,
      "site": "00b85eac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c028f0",
      "incomplete_value": true,
      "site": "00c028f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b85ea8",
      "incomplete_value": true,
      "site": "00b85eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "00c028e4",
      "READ",
      [
        "storage",
        "00c1bd20",
        null,
        "pointer"
      ]
    ],
    [
      "00c028f4",
      "DATA",
      [
        "storage",
        "00c132e0",
        null,
        "pointer"
      ]
    ],
    [
      "00c028f8",
      "DATA",
      [
        "storage",
        "00c132b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c028e4",
      "READ",
      [
        "storage",
        "00c9b750",
        null,
        "pointer"
      ]
    ],
    [
      "00c028f4",
      "DATA",
      [
        "storage",
        "00c92c88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00c028f8",
      "DATA",
      [
        "storage",
        "00c92c60",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b85e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85e80.md#insn-00b85e90) · [`00b85e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85e80.md#insn-00b85e9c) · [`00b85eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85e80.md#insn-00b85eb8)
- 新版 [`00c028d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c028c8.md#insn-00c028d8) · [`00c028e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c028c8.md#insn-00c028e4) · [`00c02900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c028c8.md#insn-00c02900)

~~~diff
- 00b85e90 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00c028d8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b85e90 bytes a80400d0
+ 00c028d8 bytes c80400b0
- 00b85e9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
- 00b85e9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c028e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:750:8"]]
+ 00c028e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b85e9c bytes 089146f9
+ 00c028e4 bytes 08a943f9
- 00b85eb8 ["INT_ADD", "register:40f0:8", ["const:b85eb8:8", "const:4:8"]]
- 00b85eb8 ["CALL", null, ["callee:00c57de0:8"]]
+ 00c02900 ["INT_ADD", "register:40f0:8", ["const:c02900:8", "const:4:8"]]
+ 00c02900 ["CALL", null, ["callee:00c57de0:8"]]
- 00b85eb8 bytes 36550194
+ 00c02900 bytes 38550194
~~~


<a id="compare-ab06a6715aa54f50d98bb58cebbef6ca"></a>

### [`00b8616c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8616c.md) → [`00c02bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02bb4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEb

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c02c08",
      "incomplete_value": true,
      "site": "00c02c0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b861c0",
      "incomplete_value": true,
      "site": "00b861c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c02c18",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b861d0",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c02c50",
      "incomplete_value": true,
      "site": "00c02c54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86208",
      "incomplete_value": true,
      "site": "00b8620c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "00c02c08",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00c02c08",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c02c18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c02c08",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c02c08",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c02c18",
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

- 旧版 [`00b861c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8616c.md#insn-00b861c4) · [`00b861d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8616c.md#insn-00b861d0) · [`00b8620c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8616c.md#insn-00b8620c)
- 新版 [`00c02c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02bb4.md#insn-00c02c0c) · [`00c02c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02bb4.md#insn-00c02c18) · [`00c02c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02bb4.md#insn-00c02c54)

~~~diff
- 00b861c4 ["INT_ADD", "register:40f0:8", ["const:b861c4:8", "const:4:8"]]
- 00b861c4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c02c0c ["INT_ADD", "register:40f0:8", ["const:c02c0c:8", "const:4:8"]]
+ 00c02c0c ["CALL", null, ["callee:00c57e80:8"]]
- 00b861c4 bytes 9b540194
+ 00c02c0c bytes 9d540194
- 00b861d0 ["INT_ADD", "register:40f0:8", ["const:b861d0:8", "const:4:8"]]
- 00b861d0 ["CALL", null, ["ram:bdb440:8"]]
+ 00c02c18 ["INT_ADD", "register:40f0:8", ["const:c02c18:8", "const:4:8"]]
+ 00c02c18 ["CALL", null, ["ram:c57e90:8"]]
- 00b861d0 bytes 9c540194
+ 00c02c18 bytes 9e540194
- 00b8620c ["INT_ADD", "register:40f0:8", ["const:b8620c:8", "const:4:8"]]
- 00b8620c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c02c54 ["INT_ADD", "register:40f0:8", ["const:c02c54:8", "const:4:8"]]
+ 00c02c54 ["CALL", null, ["callee:00c57e80:8"]]
- 00b8620c bytes 89540194
+ 00c02c54 bytes 8b540194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1a9aab28e0921d249df99fb9b948e49"></a>

### [`00b862fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b862fc.md) → [`00c02d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02d44.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEs

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c02da0",
      "incomplete_value": true,
      "site": "00c02da4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86358",
      "incomplete_value": true,
      "site": "00b8635c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c02db0",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b86368",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c02de8",
      "incomplete_value": true,
      "site": "00c02dec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b863a0",
      "incomplete_value": true,
      "site": "00b863a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "00c02da0",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00c02da0",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c02db0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c02da0",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c02da0",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c02db0",
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

- 旧版 [`00b8635c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b862fc.md#insn-00b8635c) · [`00b86368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b862fc.md#insn-00b86368) · [`00b863a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b862fc.md#insn-00b863a4)
- 新版 [`00c02da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02d44.md#insn-00c02da4) · [`00c02db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02d44.md#insn-00c02db0) · [`00c02dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02d44.md#insn-00c02dec)

~~~diff
- 00b8635c ["INT_ADD", "register:40f0:8", ["const:b8635c:8", "const:4:8"]]
- 00b8635c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c02da4 ["INT_ADD", "register:40f0:8", ["const:c02da4:8", "const:4:8"]]
+ 00c02da4 ["CALL", null, ["callee:00c57e80:8"]]
- 00b8635c bytes 35540194
+ 00c02da4 bytes 37540194
- 00b86368 ["INT_ADD", "register:40f0:8", ["const:b86368:8", "const:4:8"]]
- 00b86368 ["CALL", null, ["ram:bdb440:8"]]
+ 00c02db0 ["INT_ADD", "register:40f0:8", ["const:c02db0:8", "const:4:8"]]
+ 00c02db0 ["CALL", null, ["ram:c57e90:8"]]
- 00b86368 bytes 36540194
+ 00c02db0 bytes 38540194
- 00b863a4 ["INT_ADD", "register:40f0:8", ["const:b863a4:8", "const:4:8"]]
- 00b863a4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c02dec ["INT_ADD", "register:40f0:8", ["const:c02dec:8", "const:4:8"]]
+ 00c02dec ["CALL", null, ["callee:00c57e80:8"]]
- 00b863a4 bytes 23540194
+ 00c02dec bytes 25540194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6604e796fb727d10d652532fbc17643f"></a>

### [`00b864b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b864b4.md) → [`00c02efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02efc.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEt

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 33.33% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c02f50",
      "incomplete_value": true,
      "site": "00c02f54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86508",
      "incomplete_value": true,
      "site": "00b8650c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c02f60",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b86518",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c02f98",
      "incomplete_value": true,
      "site": "00c02f9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86550",
      "incomplete_value": true,
      "site": "00b86554",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "00c02f50",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00c02f50",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c02f60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c02f50",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c02f50",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c02f60",
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

- 旧版 [`00b8650c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b864b4.md#insn-00b8650c) · [`00b86518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b864b4.md#insn-00b86518) · [`00b86554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b864b4.md#insn-00b86554)
- 新版 [`00c02f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02efc.md#insn-00c02f54) · [`00c02f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02efc.md#insn-00c02f60) · [`00c02f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02efc.md#insn-00c02f9c)

~~~diff
- 00b8650c ["INT_ADD", "register:40f0:8", ["const:b8650c:8", "const:4:8"]]
- 00b8650c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c02f54 ["INT_ADD", "register:40f0:8", ["const:c02f54:8", "const:4:8"]]
+ 00c02f54 ["CALL", null, ["callee:00c57e80:8"]]
- 00b8650c bytes c9530194
+ 00c02f54 bytes cb530194
- 00b86518 ["INT_ADD", "register:40f0:8", ["const:b86518:8", "const:4:8"]]
- 00b86518 ["CALL", null, ["ram:bdb440:8"]]
+ 00c02f60 ["INT_ADD", "register:40f0:8", ["const:c02f60:8", "const:4:8"]]
+ 00c02f60 ["CALL", null, ["ram:c57e90:8"]]
- 00b86518 bytes ca530194
+ 00c02f60 bytes cc530194
- 00b86554 ["INT_ADD", "register:40f0:8", ["const:b86554:8", "const:4:8"]]
- 00b86554 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c02f9c ["INT_ADD", "register:40f0:8", ["const:c02f9c:8", "const:4:8"]]
+ 00c02f9c ["CALL", null, ["callee:00c57e80:8"]]
- 00b86554 bytes b7530194
+ 00c02f9c bytes b9530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a0813cf06273e2d1b4596aaa7b476ef"></a>

### [`00b86644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86644.md) → [`00c0308c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c0308c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEi

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment

命令の説明率　旧版 84.71% / 新版 84.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b866a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b866b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03130",
      "incomplete_value": true,
      "site": "00c03134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b866e8",
      "incomplete_value": true,
      "site": "00b866ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "unmatched:00b866a0",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b866a0",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b866a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ],
  "added": [
    [
      "00c030e8",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c030e8",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c030ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b866a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86644.md#insn-00b866a4) · [`00b866b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86644.md#insn-00b866b0) · [`00b866ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86644.md#insn-00b866ec)
- 新版 [`00c03134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c0308c.md#insn-00c03134)

~~~diff
- 00b866a4 ["INT_ADD", "register:40f0:8", ["const:b866a4:8", "const:4:8"]]
- 00b866a4 ["CALL", null, ["callee:00c57e80:8"]]
- 00b866a4 bytes 63530194
- 00b866b0 ["INT_ADD", "register:40f0:8", ["const:b866b0:8", "const:4:8"]]
- 00b866b0 ["CALL", null, ["ram:bdb440:8"]]
- 00b866b0 bytes 64530194
- 00b866ec ["INT_ADD", "register:40f0:8", ["const:b866ec:8", "const:4:8"]]
- 00b866ec ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03134 ["INT_ADD", "register:40f0:8", ["const:c03134:8", "const:4:8"]]
+ 00c03134 ["CALL", null, ["callee:00c57e80:8"]]
- 00b866ec bytes 51530194
+ 00c03134 bytes 53530194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d264d81cca967fc9b834b6dcffaf0fa"></a>

### [`00b867fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b867fc.md) → [`00c03244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03244.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEj

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 33.33% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86854"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86860"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c032e0",
      "incomplete_value": true,
      "site": "00c032e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86898",
      "incomplete_value": true,
      "site": "00b8689c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "unmatched:00b86850",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b86850",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b86854",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ],
  "added": [
    [
      "00c03298",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03298",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0329c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b867fc.md#insn-00b86854) · [`00b86860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b867fc.md#insn-00b86860) · [`00b8689c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b867fc.md#insn-00b8689c)
- 新版 [`00c032e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03244.md#insn-00c032e4)

~~~diff
- 00b86854 ["INT_ADD", "register:40f0:8", ["const:b86854:8", "const:4:8"]]
- 00b86854 ["CALL", null, ["callee:00c57e80:8"]]
- 00b86854 bytes f7520194
- 00b86860 ["INT_ADD", "register:40f0:8", ["const:b86860:8", "const:4:8"]]
- 00b86860 ["CALL", null, ["ram:bdb440:8"]]
- 00b86860 bytes f8520194
- 00b8689c ["INT_ADD", "register:40f0:8", ["const:b8689c:8", "const:4:8"]]
- 00b8689c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c032e4 ["INT_ADD", "register:40f0:8", ["const:c032e4:8", "const:4:8"]]
+ 00c032e4 ["CALL", null, ["callee:00c57e80:8"]]
- 00b8689c bytes e5520194
+ 00c032e4 bytes e7520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b846dfbda6b906ba42ef5e2959d83c4"></a>

### [`00b8698c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8698c.md) → [`00c033d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c033d4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 30.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b869e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b869f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03470",
      "incomplete_value": true,
      "site": "00c03474",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86a28",
      "incomplete_value": true,
      "site": "00b86a2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "unmatched:00b869e0",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b869e0",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b869e4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ],
  "added": [
    [
      "00c03428",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03428",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0342c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b869e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8698c.md#insn-00b869e4) · [`00b869f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8698c.md#insn-00b869f0) · [`00b86a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b8698c.md#insn-00b86a2c)
- 新版 [`00c03474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c033d4.md#insn-00c03474)

~~~diff
- 00b869e4 ["INT_ADD", "register:40f0:8", ["const:b869e4:8", "const:4:8"]]
- 00b869e4 ["CALL", null, ["callee:00c57e80:8"]]
- 00b869e4 bytes 93520194
- 00b869f0 ["INT_ADD", "register:40f0:8", ["const:b869f0:8", "const:4:8"]]
- 00b869f0 ["CALL", null, ["ram:bdb440:8"]]
- 00b869f0 bytes 94520194
- 00b86a2c ["INT_ADD", "register:40f0:8", ["const:b86a2c:8", "const:4:8"]]
- 00b86a2c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03474 ["INT_ADD", "register:40f0:8", ["const:c03474:8", "const:4:8"]]
+ 00c03474 ["CALL", null, ["callee:00c57e80:8"]]
- 00b86a2c bytes 81520194
+ 00c03474 bytes 83520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42c6887a74af398d6b7d3ee46d6b1d46"></a>

### [`00b86b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86b1c.md) → [`00c03564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03564.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 10.00% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86b74"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b86b80"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03600",
      "incomplete_value": true,
      "site": "00c03604",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86bb8",
      "incomplete_value": true,
      "site": "00b86bbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "unmatched:00b86b70",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b86b70",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b86b74",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ],
  "added": [
    [
      "00c035b8",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c035b8",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c035bc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b86b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86b1c.md#insn-00b86b74) · [`00b86b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86b1c.md#insn-00b86b80) · [`00b86bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86b1c.md#insn-00b86bbc)
- 新版 [`00c03604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03564.md#insn-00c03604)

~~~diff
- 00b86b74 ["INT_ADD", "register:40f0:8", ["const:b86b74:8", "const:4:8"]]
- 00b86b74 ["CALL", null, ["callee:00c57e80:8"]]
- 00b86b74 bytes 2f520194
- 00b86b80 ["INT_ADD", "register:40f0:8", ["const:b86b80:8", "const:4:8"]]
- 00b86b80 ["CALL", null, ["ram:bdb440:8"]]
- 00b86b80 bytes 30520194
- 00b86bbc ["INT_ADD", "register:40f0:8", ["const:b86bbc:8", "const:4:8"]]
- 00b86bbc ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03604 ["INT_ADD", "register:40f0:8", ["const:c03604:8", "const:4:8"]]
+ 00c03604 ["CALL", null, ["callee:00c57e80:8"]]
- 00b86bbc bytes 1d520194
+ 00c03604 bytes 1f520194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6d3e20c888488b497f9c98bb297e458"></a>

### [`00b86cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86cac.md) → [`00c036f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c036f4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEx

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03748",
      "incomplete_value": true,
      "site": "00c0374c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86d00",
      "incomplete_value": true,
      "site": "00b86d04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c03758",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b86d10",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03790",
      "incomplete_value": true,
      "site": "00c03794",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86d48",
      "incomplete_value": true,
      "site": "00b86d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "00c03748",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00c03748",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03758",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c03748",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03748",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03758",
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

- 旧版 [`00b86d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86cac.md#insn-00b86d04) · [`00b86d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86cac.md#insn-00b86d10) · [`00b86d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86cac.md#insn-00b86d4c)
- 新版 [`00c0374c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c036f4.md#insn-00c0374c) · [`00c03758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c036f4.md#insn-00c03758) · [`00c03794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c036f4.md#insn-00c03794)

~~~diff
- 00b86d04 ["INT_ADD", "register:40f0:8", ["const:b86d04:8", "const:4:8"]]
- 00b86d04 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c0374c ["INT_ADD", "register:40f0:8", ["const:c0374c:8", "const:4:8"]]
+ 00c0374c ["CALL", null, ["callee:00c57e80:8"]]
- 00b86d04 bytes cb510194
+ 00c0374c bytes cd510194
- 00b86d10 ["INT_ADD", "register:40f0:8", ["const:b86d10:8", "const:4:8"]]
- 00b86d10 ["CALL", null, ["ram:bdb440:8"]]
+ 00c03758 ["INT_ADD", "register:40f0:8", ["const:c03758:8", "const:4:8"]]
+ 00c03758 ["CALL", null, ["ram:c57e90:8"]]
- 00b86d10 bytes cc510194
+ 00c03758 bytes ce510194
- 00b86d4c ["INT_ADD", "register:40f0:8", ["const:b86d4c:8", "const:4:8"]]
- 00b86d4c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03794 ["INT_ADD", "register:40f0:8", ["const:c03794:8", "const:4:8"]]
+ 00c03794 ["CALL", null, ["callee:00c57e80:8"]]
- 00b86d4c bytes b9510194
+ 00c03794 bytes bb510194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad6ba2a93e62715e3d286ed8401b8ad0"></a>

### [`00b86e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86e3c.md) → [`00c03884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03884.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEy

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c038d8",
      "incomplete_value": true,
      "site": "00c038dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86e90",
      "incomplete_value": true,
      "site": "00b86e94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c038e8",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b86ea0",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03920",
      "incomplete_value": true,
      "site": "00c03924",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86ed8",
      "incomplete_value": true,
      "site": "00b86edc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "00c038d8",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00c038d8",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c038e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c038d8",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c038d8",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c038e8",
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

- 旧版 [`00b86e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86e3c.md#insn-00b86e94) · [`00b86ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86e3c.md#insn-00b86ea0) · [`00b86edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86e3c.md#insn-00b86edc)
- 新版 [`00c038dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03884.md#insn-00c038dc) · [`00c038e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03884.md#insn-00c038e8) · [`00c03924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03884.md#insn-00c03924)

~~~diff
- 00b86e94 ["INT_ADD", "register:40f0:8", ["const:b86e94:8", "const:4:8"]]
- 00b86e94 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c038dc ["INT_ADD", "register:40f0:8", ["const:c038dc:8", "const:4:8"]]
+ 00c038dc ["CALL", null, ["callee:00c57e80:8"]]
- 00b86e94 bytes 67510194
+ 00c038dc bytes 69510194
- 00b86ea0 ["INT_ADD", "register:40f0:8", ["const:b86ea0:8", "const:4:8"]]
- 00b86ea0 ["CALL", null, ["ram:bdb440:8"]]
+ 00c038e8 ["INT_ADD", "register:40f0:8", ["const:c038e8:8", "const:4:8"]]
+ 00c038e8 ["CALL", null, ["ram:c57e90:8"]]
- 00b86ea0 bytes 68510194
+ 00c038e8 bytes 6a510194
- 00b86edc ["INT_ADD", "register:40f0:8", ["const:b86edc:8", "const:4:8"]]
- 00b86edc ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03924 ["INT_ADD", "register:40f0:8", ["const:c03924:8", "const:4:8"]]
+ 00c03924 ["CALL", null, ["callee:00c57e80:8"]]
- 00b86edc bytes 55510194
+ 00c03924 bytes 57510194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84db067180b92e3bac6630ea18a92614"></a>

### [`00b86fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86fcc.md) → [`00c03a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03a14.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEf

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03a6c",
      "incomplete_value": true,
      "site": "00c03a70",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b87024",
      "incomplete_value": true,
      "site": "00b87028",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c03a7c",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b87034",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03ab4",
      "incomplete_value": true,
      "site": "00c03ab8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8706c",
      "incomplete_value": true,
      "site": "00b87070",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "00c03a6c",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00c03a6c",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03a7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c03a6c",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03a6c",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03a7c",
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

- 旧版 [`00b87028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86fcc.md#insn-00b87028) · [`00b87034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86fcc.md#insn-00b87034) · [`00b87070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b86/00b86fcc.md#insn-00b87070)
- 新版 [`00c03a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03a14.md#insn-00c03a70) · [`00c03a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03a14.md#insn-00c03a7c) · [`00c03ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03a14.md#insn-00c03ab8)

~~~diff
- 00b87028 ["INT_ADD", "register:40f0:8", ["const:b87028:8", "const:4:8"]]
- 00b87028 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03a70 ["INT_ADD", "register:40f0:8", ["const:c03a70:8", "const:4:8"]]
+ 00c03a70 ["CALL", null, ["callee:00c57e80:8"]]
- 00b87028 bytes 02510194
+ 00c03a70 bytes 04510194
- 00b87034 ["INT_ADD", "register:40f0:8", ["const:b87034:8", "const:4:8"]]
- 00b87034 ["CALL", null, ["ram:bdb440:8"]]
+ 00c03a7c ["INT_ADD", "register:40f0:8", ["const:c03a7c:8", "const:4:8"]]
+ 00c03a7c ["CALL", null, ["ram:c57e90:8"]]
- 00b87034 bytes 03510194
+ 00c03a7c bytes 05510194
- 00b87070 ["INT_ADD", "register:40f0:8", ["const:b87070:8", "const:4:8"]]
- 00b87070 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03ab8 ["INT_ADD", "register:40f0:8", ["const:c03ab8:8", "const:4:8"]]
+ 00c03ab8 ["CALL", null, ["callee:00c57e80:8"]]
- 00b87070 bytes f0500194
+ 00c03ab8 bytes f2500194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f52a2cf0aa46231587554225bbc6942"></a>

### [`00b87164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87164.md) → [`00c03bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03bac.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEd

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03c04",
      "incomplete_value": true,
      "site": "00c03c08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b871bc",
      "incomplete_value": true,
      "site": "00b871c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c03c14",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b871cc",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03c4c",
      "incomplete_value": true,
      "site": "00c03c50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b87204",
      "incomplete_value": true,
      "site": "00b87208",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "00c03c04",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00c03c04",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03c14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c03c04",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03c04",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03c14",
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

- 旧版 [`00b871c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87164.md#insn-00b871c0) · [`00b871cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87164.md#insn-00b871cc) · [`00b87208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87164.md#insn-00b87208)
- 新版 [`00c03c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03bac.md#insn-00c03c08) · [`00c03c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03bac.md#insn-00c03c14) · [`00c03c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03bac.md#insn-00c03c50)

~~~diff
- 00b871c0 ["INT_ADD", "register:40f0:8", ["const:b871c0:8", "const:4:8"]]
- 00b871c0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03c08 ["INT_ADD", "register:40f0:8", ["const:c03c08:8", "const:4:8"]]
+ 00c03c08 ["CALL", null, ["callee:00c57e80:8"]]
- 00b871c0 bytes 9c500194
+ 00c03c08 bytes 9e500194
- 00b871cc ["INT_ADD", "register:40f0:8", ["const:b871cc:8", "const:4:8"]]
- 00b871cc ["CALL", null, ["ram:bdb440:8"]]
+ 00c03c14 ["INT_ADD", "register:40f0:8", ["const:c03c14:8", "const:4:8"]]
+ 00c03c14 ["CALL", null, ["ram:c57e90:8"]]
- 00b871cc bytes 9d500194
+ 00c03c14 bytes 9f500194
- 00b87208 ["INT_ADD", "register:40f0:8", ["const:b87208:8", "const:4:8"]]
- 00b87208 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03c50 ["INT_ADD", "register:40f0:8", ["const:c03c50:8", "const:4:8"]]
+ 00c03c50 ["CALL", null, ["callee:00c57e80:8"]]
- 00b87208 bytes 8a500194
+ 00c03c50 bytes 8c500194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6ffcca5aa5c92e23afc36fdfda12894"></a>

### [`00b872fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b872fc.md) → [`00c03d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03d44.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEe

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03d98",
      "incomplete_value": true,
      "site": "00c03d9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b87350",
      "incomplete_value": true,
      "site": "00b87354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c03da8",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b87360",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03de0",
      "incomplete_value": true,
      "site": "00c03de4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b87398",
      "incomplete_value": true,
      "site": "00b8739c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "00c03d98",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00c03d98",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03da8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c03d98",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03d98",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03da8",
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

- 旧版 [`00b87354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b872fc.md#insn-00b87354) · [`00b87360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b872fc.md#insn-00b87360) · [`00b8739c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b872fc.md#insn-00b8739c)
- 新版 [`00c03d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03d44.md#insn-00c03d9c) · [`00c03da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03d44.md#insn-00c03da8) · [`00c03de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03d44.md#insn-00c03de4)

~~~diff
- 00b87354 ["INT_ADD", "register:40f0:8", ["const:b87354:8", "const:4:8"]]
- 00b87354 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03d9c ["INT_ADD", "register:40f0:8", ["const:c03d9c:8", "const:4:8"]]
+ 00c03d9c ["CALL", null, ["callee:00c57e80:8"]]
- 00b87354 bytes 37500194
+ 00c03d9c bytes 39500194
- 00b87360 ["INT_ADD", "register:40f0:8", ["const:b87360:8", "const:4:8"]]
- 00b87360 ["CALL", null, ["ram:bdb440:8"]]
+ 00c03da8 ["INT_ADD", "register:40f0:8", ["const:c03da8:8", "const:4:8"]]
+ 00c03da8 ["CALL", null, ["ram:c57e90:8"]]
- 00b87360 bytes 38500194
+ 00c03da8 bytes 3a500194
- 00b8739c ["INT_ADD", "register:40f0:8", ["const:b8739c:8", "const:4:8"]]
- 00b8739c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03de4 ["INT_ADD", "register:40f0:8", ["const:c03de4:8", "const:4:8"]]
+ 00c03de4 ["CALL", null, ["callee:00c57e80:8"]]
- 00b8739c bytes 25500194
+ 00c03de4 bytes 27500194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f166dee18f805edb8f589b5137177c0"></a>

### [`00b8748c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8748c.md) → [`00c03ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03ed4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPKv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03f28",
      "incomplete_value": true,
      "site": "00c03f2c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b874e0",
      "incomplete_value": true,
      "site": "00b874e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c03f38",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b874f0",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c03f70",
      "incomplete_value": true,
      "site": "00c03f74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b87528",
      "incomplete_value": true,
      "site": "00b8752c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "00c03f28",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00c03f28",
      "PARAM",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03f38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c03f28",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c03f28",
      "PARAM",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c03f38",
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

- 旧版 [`00b874e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8748c.md#insn-00b874e4) · [`00b874f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8748c.md#insn-00b874f0) · [`00b8752c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8748c.md#insn-00b8752c)
- 新版 [`00c03f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03ed4.md#insn-00c03f2c) · [`00c03f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03ed4.md#insn-00c03f38) · [`00c03f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c03/00c03ed4.md#insn-00c03f74)

~~~diff
- 00b874e4 ["INT_ADD", "register:40f0:8", ["const:b874e4:8", "const:4:8"]]
- 00b874e4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03f2c ["INT_ADD", "register:40f0:8", ["const:c03f2c:8", "const:4:8"]]
+ 00c03f2c ["CALL", null, ["callee:00c57e80:8"]]
- 00b874e4 bytes d34f0194
+ 00c03f2c bytes d54f0194
- 00b874f0 ["INT_ADD", "register:40f0:8", ["const:b874f0:8", "const:4:8"]]
- 00b874f0 ["CALL", null, ["ram:bdb440:8"]]
+ 00c03f38 ["INT_ADD", "register:40f0:8", ["const:c03f38:8", "const:4:8"]]
+ 00c03f38 ["CALL", null, ["ram:c57e90:8"]]
- 00b874f0 bytes d44f0194
+ 00c03f38 bytes d64f0194
- 00b8752c ["INT_ADD", "register:40f0:8", ["const:b8752c:8", "const:4:8"]]
- 00b8752c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c03f74 ["INT_ADD", "register:40f0:8", ["const:c03f74:8", "const:4:8"]]
+ 00c03f74 ["CALL", null, ["callee:00c57e80:8"]]
- 00b8752c bytes c14f0194
+ 00c03f74 bytes c34f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50458f6e5351f12af8768427935e02d0"></a>

### [`00b8761c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8761c.md) → [`00c04064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04064.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEElsEPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md) [`00c5e010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e010.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.84% / 新版 98.84%

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
      "site": "00c0419c",
      "value": [
        "leaf",
        "ram:c5e010:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b87754",
      "value": [
        "leaf",
        "ram:be1410:8"
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
      "00c0419c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1410"
      ]
    ]
  ],
  "added": [
    [
      "00c0419c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e010"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b87754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8761c.md#insn-00b87754) · [`00b87644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8761c.md#insn-00b87644) · [`00b87698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b8761c.md#insn-00b87698)
- 新版 [`00c0419c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04064.md#insn-00c0419c) · [`00c0408c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04064.md#insn-00c0408c) · [`00c040e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04064.md#insn-00c040e0)

~~~diff
- 00b87754 ["INT_ADD", "register:40f0:8", ["const:b87754:8", "const:4:8"]]
- 00b87754 ["CALL", null, ["ram:be1410:8"]]
+ 00c0419c ["INT_ADD", "register:40f0:8", ["const:c0419c:8", "const:4:8"]]
+ 00c0419c ["CALL", null, ["ram:c5e010:8"]]
- 00b87754 bytes 2f670194
+ 00c0419c bytes 9d670194
- 00b87644 ["INT_ADD", "register:40f0:8", ["const:b87644:8", "const:4:8"]]
- 00b87644 ["CALL", null, ["callee:00c5e000:8"]]
+ 00c0408c ["INT_ADD", "register:40f0:8", ["const:c0408c:8", "const:4:8"]]
+ 00c0408c ["CALL", null, ["callee:00c5e000:8"]]
- 00b87644 bytes 6f670194
+ 00c0408c bytes dd670194
- 00b87698 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87698 ["INT_ADD", "register:40f0:8", ["const:b87698:8", "const:4:8"]]
- 00b87698 ["CALLIND", null, ["register:0:8"]]
+ 00c040e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c040e0 ["INT_ADD", "register:40f0:8", ["const:c040e0:8", "const:4:8"]]
+ 00c040e0 ["CALLIND", null, ["register:0:8"]]
- 00b87698 bytes 00013fd6
+ 00c040e0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-189a8f14ac0be54720a5fc83a66f3f7d"></a>

### [`00b877e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b877e8.md) → [`00c04230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04230.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE3putEw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md) [`00c5e010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e010.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

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
      "site": "00c042cc",
      "value": [
        "leaf",
        "ram:c5e010:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b87884",
      "value": [
        "leaf",
        "ram:be1410:8"
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
      "00c042cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1410"
      ]
    ]
  ],
  "added": [
    [
      "00c042cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e010"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b87884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b877e8.md#insn-00b87884) · [`00b8780c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b877e8.md#insn-00b8780c) · [`00b87858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b877e8.md#insn-00b87858)
- 新版 [`00c042cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04230.md#insn-00c042cc) · [`00c04254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04230.md#insn-00c04254) · [`00c042a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04230.md#insn-00c042a0)

~~~diff
- 00b87884 ["INT_ADD", "register:40f0:8", ["const:b87884:8", "const:4:8"]]
- 00b87884 ["CALL", null, ["ram:be1410:8"]]
+ 00c042cc ["INT_ADD", "register:40f0:8", ["const:c042cc:8", "const:4:8"]]
+ 00c042cc ["CALL", null, ["ram:c5e010:8"]]
- 00b87884 bytes e3660194
+ 00c042cc bytes 51670194
- 00b8780c ["INT_ADD", "register:40f0:8", ["const:b8780c:8", "const:4:8"]]
- 00b8780c ["CALL", null, ["callee:00c5e000:8"]]
+ 00c04254 ["INT_ADD", "register:40f0:8", ["const:c04254:8", "const:4:8"]]
+ 00c04254 ["CALL", null, ["callee:00c5e000:8"]]
- 00b8780c bytes fd660194
+ 00c04254 bytes 6b670194
- 00b87858 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87858 ["INT_ADD", "register:40f0:8", ["const:b87858:8", "const:4:8"]]
- 00b87858 ["CALLIND", null, ["register:0:8"]]
+ 00c042a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c042a0 ["INT_ADD", "register:40f0:8", ["const:c042a0:8", "const:4:8"]]
+ 00c042a0 ["CALLIND", null, ["register:0:8"]]
- 00b87858 bytes 00013fd6
+ 00c042a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ba71a6c2ce137845ac9a2bc609be8af"></a>

### [`00b878e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b878e8.md) → [`00c04330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04330.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5writeEPKwl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md) [`00c5e010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e010.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

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
      "site": "00c043b4",
      "value": [
        "leaf",
        "ram:c5e010:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b8796c",
      "value": [
        "leaf",
        "ram:be1410:8"
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
      "00c043b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1410"
      ]
    ]
  ],
  "added": [
    [
      "00c043b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e010"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8796c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b878e8.md#insn-00b8796c) · [`00b87914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b878e8.md#insn-00b87914) · [`00b87944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b878e8.md#insn-00b87944)
- 新版 [`00c043b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04330.md#insn-00c043b4) · [`00c0435c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04330.md#insn-00c0435c) · [`00c0438c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04330.md#insn-00c0438c)

~~~diff
- 00b8796c ["INT_ADD", "register:40f0:8", ["const:b8796c:8", "const:4:8"]]
- 00b8796c ["CALL", null, ["ram:be1410:8"]]
+ 00c043b4 ["INT_ADD", "register:40f0:8", ["const:c043b4:8", "const:4:8"]]
+ 00c043b4 ["CALL", null, ["ram:c5e010:8"]]
- 00b8796c bytes a9660194
+ 00c043b4 bytes 17670194
- 00b87914 ["INT_ADD", "register:40f0:8", ["const:b87914:8", "const:4:8"]]
- 00b87914 ["CALL", null, ["callee:00c5e000:8"]]
+ 00c0435c ["INT_ADD", "register:40f0:8", ["const:c0435c:8", "const:4:8"]]
+ 00c0435c ["CALL", null, ["callee:00c5e000:8"]]
- 00b87914 bytes bb660194
+ 00c0435c bytes 29670194
- 00b87944 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87944 ["INT_ADD", "register:40f0:8", ["const:b87944:8", "const:4:8"]]
- 00b87944 ["CALLIND", null, ["register:0:8"]]
+ 00c0438c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0438c ["INT_ADD", "register:40f0:8", ["const:c0438c:8", "const:4:8"]]
+ 00c0438c ["CALLIND", null, ["register:0:8"]]
- 00b87944 bytes 00013fd6
+ 00c0438c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c90dc5d5ea29830a1fa70cba308b536"></a>

### [`00b87a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87a34.md) → [`00c0447c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c0447c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5seekpENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md) [`00c5e010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e010.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.67% / 新版 97.67%

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
      "site": "00c04508",
      "value": [
        "leaf",
        "ram:c5e010:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b87ac0",
      "value": [
        "leaf",
        "ram:be1410:8"
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
      "00c04508",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1410"
      ]
    ]
  ],
  "added": [
    [
      "00c04508",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e010"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b87ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87a34.md#insn-00b87ac0) · [`00b87a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87a34.md#insn-00b87a60) · [`00b87a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87a34.md#insn-00b87a98)
- 新版 [`00c04508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c0447c.md#insn-00c04508) · [`00c044a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c0447c.md#insn-00c044a8) · [`00c044e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c0447c.md#insn-00c044e0)

~~~diff
- 00b87ac0 ["INT_ADD", "register:40f0:8", ["const:b87ac0:8", "const:4:8"]]
- 00b87ac0 ["CALL", null, ["ram:be1410:8"]]
+ 00c04508 ["INT_ADD", "register:40f0:8", ["const:c04508:8", "const:4:8"]]
+ 00c04508 ["CALL", null, ["ram:c5e010:8"]]
- 00b87ac0 bytes 54660194
+ 00c04508 bytes c2660194
- 00b87a60 ["INT_ADD", "register:40f0:8", ["const:b87a60:8", "const:4:8"]]
- 00b87a60 ["CALL", null, ["callee:00c5e000:8"]]
+ 00c044a8 ["INT_ADD", "register:40f0:8", ["const:c044a8:8", "const:4:8"]]
+ 00c044a8 ["CALL", null, ["callee:00c5e000:8"]]
- 00b87a60 bytes 68660194
+ 00c044a8 bytes d6660194
- 00b87a98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87a98 ["INT_ADD", "register:40f0:8", ["const:b87a98:8", "const:4:8"]]
- 00b87a98 ["CALLIND", null, ["register:0:8"]]
+ 00c044e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c044e0 ["INT_ADD", "register:40f0:8", ["const:c044e0:8", "const:4:8"]]
+ 00c044e0 ["CALLIND", null, ["register:0:8"]]
- 00b87a98 bytes 00013fd6
+ 00c044e0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc5a0b99194d424ed56b7fc2421a7d3c"></a>

### [`00b87af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87af8.md) → [`00c04540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04540.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5seekpExNS_8ios_base7seekdirE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md) [`00c5e010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e010.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.67% / 新版 97.67%

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
      "site": "00c045cc",
      "value": [
        "leaf",
        "ram:c5e010:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b87b84",
      "value": [
        "leaf",
        "ram:be1410:8"
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
      "00c045cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1410"
      ]
    ]
  ],
  "added": [
    [
      "00c045cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e010"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b87b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87af8.md#insn-00b87b84) · [`00b87b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87af8.md#insn-00b87b24) · [`00b87b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87af8.md#insn-00b87b5c)
- 新版 [`00c045cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04540.md#insn-00c045cc) · [`00c0456c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04540.md#insn-00c0456c) · [`00c045a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04540.md#insn-00c045a4)

~~~diff
- 00b87b84 ["INT_ADD", "register:40f0:8", ["const:b87b84:8", "const:4:8"]]
- 00b87b84 ["CALL", null, ["ram:be1410:8"]]
+ 00c045cc ["INT_ADD", "register:40f0:8", ["const:c045cc:8", "const:4:8"]]
+ 00c045cc ["CALL", null, ["ram:c5e010:8"]]
- 00b87b84 bytes 23660194
+ 00c045cc bytes 91660194
- 00b87b24 ["INT_ADD", "register:40f0:8", ["const:b87b24:8", "const:4:8"]]
- 00b87b24 ["CALL", null, ["callee:00c5e000:8"]]
+ 00c0456c ["INT_ADD", "register:40f0:8", ["const:c0456c:8", "const:4:8"]]
+ 00c0456c ["CALL", null, ["callee:00c5e000:8"]]
- 00b87b24 bytes 37660194
+ 00c0456c bytes a5660194
- 00b87b5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b87b5c ["INT_ADD", "register:40f0:8", ["const:b87b5c:8", "const:4:8"]]
- 00b87b5c ["CALLIND", null, ["register:0:8"]]
+ 00c045a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c045a4 ["INT_ADD", "register:40f0:8", ["const:c045a4:8", "const:4:8"]]
+ 00c045a4 ["CALLIND", null, ["register:0:8"]]
- 00b87b5c bytes 00013fd6
+ 00c045a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80a9ba7dc451e8254d5fadf7280e8f92"></a>

### [`00b87bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87bbc.md) → [`00c04604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04604.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC1EOS5_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b87c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87c68.md) [`00bdd950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd950.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c046b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c046b0.md) [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 78.12% / 新版 78.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0462c",
      "incomplete_value": true,
      "site": "00c0462c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b87be4",
      "incomplete_value": true,
      "site": "00b87be4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00c04658",
      "incomplete_value": true,
      "site": "00c0465c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b87c10",
      "incomplete_value": true,
      "site": "00b87c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c04630",
      "value": [
        "leaf",
        "ram:c5a3a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b87be8",
      "value": [
        "leaf",
        "ram:bdd950:8"
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
      "00c04624",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00c0462c",
      "DATA",
      [
        "storage",
        "00c11220",
        null,
        "pointer"
      ]
    ],
    [
      "00c04630",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdd950"
      ]
    ]
  ],
  "added": [
    [
      "00c04624",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00c0462c",
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c04630",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a3a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b87be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87bbc.md#insn-00b87be8) · [`00b87bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87bbc.md#insn-00b87bd0) · [`00b87bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87bbc.md#insn-00b87bdc)
- 新版 [`00c04630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04604.md#insn-00c04630) · [`00c04618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04604.md#insn-00c04618) · [`00c04624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04604.md#insn-00c04624)

~~~diff
- 00b87be8 ["INT_ADD", "register:40f0:8", ["const:b87be8:8", "const:4:8"]]
- 00b87be8 ["CALL", null, ["ram:bdd950:8"]]
+ 00c04630 ["INT_ADD", "register:40f0:8", ["const:c04630:8", "const:4:8"]]
+ 00c04630 ["CALL", null, ["ram:c5a3a0:8"]]
- 00b87be8 bytes 5a570194
+ 00c04630 bytes 5c570194
- 00b87bd0 ["COPY", "register:40a8:8", ["const:c1b000:8"]]
+ 00c04618 ["COPY", "register:40a8:8", ["const:c9b000:8"]]
- 00b87bd0 bytes b5040090
+ 00c04618 bytes b50400f0
- 00b87bdc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a50:8"]]
- 00b87bdc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c04624 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:448:8"]]
+ 00c04624 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00b87bdc bytes b52a45f9
+ 00c04624 bytes b52642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdac6f50e6ec5ca7f0cdca5e4cac4ab5"></a>

### [`00b87e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87e3c.md) → [`00c04884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04884.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1470.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 1件 [`00c5e070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e070.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.26% / 新版 94.26%

CFGの説明率　旧版 46.67% / 新版 38.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b87f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c04954"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b87f24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b87ff0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ],
    [
      "unmatched:00b87ff8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c04a38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ],
    [
      "00c04a40",
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

- 旧版 [`00b87f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87e3c.md#insn-00b87f0c) · [`00b87f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87e3c.md#insn-00b87f24) · [`00b87fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87e3c.md#insn-00b87fe8)
- 新版 [`00c04a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04884.md#insn-00c04a30)

~~~diff
- 00b87f0c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b87f0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b87f0c bytes 6002803d
- 00b87f24 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b87f24 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b87f24 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b87f24 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b87f24 bytes 4801899a
- 00b87fe8 ["INT_ADD", "register:40f0:8", ["const:b87fe8:8", "const:4:8"]]
- 00b87fe8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c04a30 ["INT_ADD", "register:40f0:8", ["const:c04a30:8", "const:4:8"]]
+ 00c04a30 ["CALL", null, ["callee:00c5dee0:8"]]
- 00b87fe8 bytes be640194
+ 00c04a30 bytes 2c650194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f41f9e0fa0bc8665c63ac25577dddf0"></a>

### [`00b88038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88038.md) → [`00c04a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04a80.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4swapERS5_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.82% / 新版 92.82%

CFGの説明率　旧版 29.17% / 新版 22.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b881e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b881ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c04c30"
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
      "unmatched:00b880b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c04ad4"
      ]
    ],
    [
      "unmatched:00b882ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ],
    [
      "unmatched:00b882b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c04af8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c04ad4"
      ]
    ],
    [
      "00c04cf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ],
    [
      "00c04cfc",
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

- 旧版 [`00b880b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88038.md#insn-00b880b0) · [`00b8817c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88038.md#insn-00b8817c) · [`00b881e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88038.md#insn-00b881e4)

~~~diff
- 00b880b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4060:8", "const:0:8"]]
- 00b880b0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b880b0 bytes ecfeffb5
- 00b8817c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8817c ["COPY", "tmp:1:8", ["register:4028:8"]]
- 00b8817c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b8817c ["INT_NEGATE", "tmp:1:8", ["const:0:8"]]
- 00b8817c bytes a4109fda
- 00b881e4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b881e4 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b881e4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b881e4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b881e4 bytes e903899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38316ae55e514388a8fa5a74921d3b92"></a>

### [`00b88310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88310.md) → [`00c04d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04d58.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00525380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525380.md) [`00b75338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75338.md) [`00b753ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b753ec.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00548218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548218.md) [`00bf1d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1d80.md) [`00bf1e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1e34.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 70.00% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8836c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88310.md#insn-00b8836c) · [`00b88384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88310.md#insn-00b88384)
- 新版 [`00c04db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04d58.md#insn-00c04db4) · [`00c04dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04d58.md#insn-00c04dcc)

~~~diff
- 00b8836c ["INT_ADD", "register:40f0:8", ["const:b8836c:8", "const:4:8"]]
- 00b8836c ["CALL", null, ["callee:00bf1e34:8"]]
+ 00c04db4 ["INT_ADD", "register:40f0:8", ["const:c04db4:8", "const:4:8"]]
+ 00c04db4 ["CALL", null, ["callee:00bf1e34:8"]]
- 00b8836c bytes 20b4ff97
+ 00c04db4 bytes 20b4ff97
- 00b88384 ["INT_ADD", "register:40f0:8", ["const:b88384:8", "const:4:8"]]
- 00b88384 ["CALL", null, ["callee:00bf1d80:8"]]
+ 00c04dcc ["INT_ADD", "register:40f0:8", ["const:c04dcc:8", "const:4:8"]]
+ 00c04dcc ["CALL", null, ["callee:00bf1d80:8"]]
- 00b88384 bytes edb3ff97
+ 00c04dcc bytes edb3ff97
~~~


<a id="compare-bb567ab84524b4a1a9da3640d324a73d"></a>

### [`00b8839c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8839c.md) → [`00c04de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04de4.md) _ZNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md) [`00be1470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1470.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md) [`00c5e070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e070.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b883ec",
      "incomplete_value": true,
      "site": "00b8840c",
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
            "const:18:8"
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
    "new": null,
    "old": {
      "definition_site": "00b883f4",
      "incomplete_value": true,
      "site": "00b8840c",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b88424"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b8840c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8839c.md#insn-00b8840c) · [`00b88424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8839c.md#insn-00b88424)
- 新版 [`00c04e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04de4.md#insn-00c04e54) · [`00c04e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04de4.md#insn-00c04e6c)

~~~diff
- 00b8840c ["INT_ADD", "register:40f0:8", ["const:b8840c:8", "const:4:8"]]
- 00b8840c ["CALL", null, ["callee:00c5e070:8"]]
+ 00c04e54 ["INT_ADD", "register:40f0:8", ["const:c04e54:8", "const:4:8"]]
+ 00c04e54 ["CALL", null, ["callee:00c5e070:8"]]
- 00b8840c bytes 19640194
+ 00c04e54 bytes 87640194
- 00b88424 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b88424 ["RETURN", null, ["register:0:8"]]
- 00b88424 bytes c0035fd6
+ 00c04e6c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c04e6c ["RETURN", null, ["register:0:8"]]
+ 00c04e6c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c7d94dfd712c65eb4382234b35a20d2"></a>

### [`00b88428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88428.md) → [`00c04e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04e70.md) _ZNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md) [`00be1470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1470.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md) [`00c5e070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e070.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.56% / 新版 80.56%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8842c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8842c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b88430"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8842c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b88430",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b88434",
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
      "00c04e74",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c04e78",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c04e7c",
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

- 旧版 [`00b8842c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88428.md#insn-00b8842c) · [`00b88430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88428.md#insn-00b88430) · [`00b88434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88428.md#insn-00b88434)

~~~diff
- 00b8842c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b8842c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b8842c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b8842c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b8842c bytes fd7bbca9
- 00b88430 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b88430 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b88430 bytes f70b00f9
- 00b88434 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b88434 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b88434 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b88434 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b88434 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-908ecdec75df93053f189683ad2d3565"></a>

### [`00b886b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b886b0.md) → [`00c050f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c050f8.md) _ZNSt6__ndk114basic_ofstreamIcNS_11char_traitsIcEEE4openEPKcj

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b88f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c059a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md) [`00c59c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0515c",
      "incomplete_value": true,
      "site": "00c05160",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c05158",
      "incomplete_value": true,
      "site": "00c05160",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b88718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b886b0.md#insn-00b88718) · [`00b88708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b886b0.md#insn-00b88708) · [`00b88728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b886b0.md#insn-00b88728)
- 新版 [`00c05160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c050f8.md#insn-00c05160) · [`00c05150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c050f8.md#insn-00c05150) · [`00c05170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c050f8.md#insn-00c05170)

~~~diff
- 00b88718 ["INT_ADD", "register:40f0:8", ["const:b88718:8", "const:4:8"]]
- 00b88718 ["CALL", null, ["callee:00c59c90:8"]]
+ 00c05160 ["INT_ADD", "register:40f0:8", ["const:c05160:8", "const:4:8"]]
+ 00c05160 ["CALL", null, ["callee:00c59c90:8"]]
- 00b88718 bytes ca520194
+ 00c05160 bytes cc520194
- 00b88708 ["INT_ADD", "register:40f0:8", ["const:b88708:8", "const:4:8"]]
- 00b88708 ["CALL", null, ["callee:00c059a4:8"]]
+ 00c05150 ["INT_ADD", "register:40f0:8", ["const:c05150:8", "const:4:8"]]
+ 00c05150 ["CALL", null, ["callee:00c059a4:8"]]
- 00b88708 bytes 15020094
+ 00c05150 bytes 15020094
- 00b88728 ["INT_RIGHT", "tmp:0:4", ["register:40a0:4", "const:1:4"]]
- 00b88728 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b88728 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b88728 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00c05170 ["INT_RIGHT", "tmp:0:4", ["register:40a0:4", "const:1:4"]]
+ 00c05170 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c05170 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c05170 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b88728 bytes 34010836
+ 00c05170 bytes 34010836
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b59b9aaf63d9d706bd17010e3511281a"></a>

### [`00b8881c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8881c.md) → [`00c05264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05264.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0b0.md) · 呼出先 6件 [`00b47d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47d4c.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd950.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)
- 新版 呼出元 1件 [`00c58b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b00.md) · 呼出先 6件 [`00bb5598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.97% / 新版 81.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c05288",
      "incomplete_value": true,
      "site": "00c05288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b88840",
      "incomplete_value": true,
      "site": "00b88840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "store_value",
    "new": {
      "definition_site": "00c052ac",
      "incomplete_value": true,
      "site": "00c052b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b88864",
      "incomplete_value": true,
      "site": "00b88868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c0528c",
      "value": [
        "leaf",
        "ram:c5a3a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b88844",
      "value": [
        "leaf",
        "ram:bdd950:8"
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
      "00c05280",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00c05288",
      "DATA",
      [
        "storage",
        "00c11220",
        null,
        "pointer"
      ]
    ],
    [
      "00c0528c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdd950"
      ]
    ]
  ],
  "added": [
    [
      "00c05280",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00c05288",
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c0528c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a3a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b88844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8881c.md#insn-00b88844) · [`00b88890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8881c.md#insn-00b88890) · [`00b8889c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b8881c.md#insn-00b8889c)
- 新版 [`00c0528c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05264.md#insn-00c0528c) · [`00c052d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05264.md#insn-00c052d8) · [`00c052e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05264.md#insn-00c052e4)

~~~diff
- 00b88844 ["INT_ADD", "register:40f0:8", ["const:b88844:8", "const:4:8"]]
- 00b88844 ["CALL", null, ["ram:bdd950:8"]]
+ 00c0528c ["INT_ADD", "register:40f0:8", ["const:c0528c:8", "const:4:8"]]
+ 00c0528c ["CALL", null, ["ram:c5a3a0:8"]]
- 00b88844 bytes 43540194
+ 00c0528c bytes 45540194
- 00b88890 ["INT_ADD", "register:40f0:8", ["const:b88890:8", "const:4:8"]]
- 00b88890 ["CALL", null, ["callee:00c5cd80:8"]]
+ 00c052d8 ["INT_ADD", "register:40f0:8", ["const:c052d8:8", "const:4:8"]]
+ 00c052d8 ["CALL", null, ["callee:00c5cd80:8"]]
- 00b88890 bytes 785e0194
+ 00c052d8 bytes aa5e0194
- 00b8889c ["INT_ADD", "register:40f0:8", ["const:b8889c:8", "const:4:8"]]
- 00b8889c ["CALL", null, ["ram:bdb440:8"]]
+ 00c052e4 ["INT_ADD", "register:40f0:8", ["const:c052e4:8", "const:4:8"]]
+ 00c052e4 ["CALL", null, ["ram:c57e90:8"]]
- 00b8889c bytes e94a0194
+ 00c052e4 bytes eb4a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffbd89a7f8177ac15b303936763fc2dd"></a>

### [`00b88940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88940.md) → [`00c05388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05388.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1EOS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.06% / 新版 94.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c053b0",
      "incomplete_value": true,
      "site": "00c053b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b88968",
      "incomplete_value": true,
      "site": "00b88968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00c053e4",
      "incomplete_value": true,
      "site": "00c053ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b8899c",
      "incomplete_value": true,
      "site": "00b889a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00c053a4",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00c053b0",
      "DATA",
      [
        "storage",
        "00c11220",
        null,
        "pointer"
      ]
    ],
    [
      "00c053dc",
      "READ",
      [
        "storage",
        "00c1bad0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c053a4",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00c053b0",
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c053dc",
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b88950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88940.md#insn-00b88950) · [`00b8895c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88940.md#insn-00b8895c) · [`00b8896c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88940.md#insn-00b8896c)
- 新版 [`00c05398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05388.md#insn-00c05398) · [`00c053a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05388.md#insn-00c053a4) · [`00c053b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05388.md#insn-00c053b4)

~~~diff
- 00b88950 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00c05398 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b88950 bytes 880400f0
+ 00c05398 bytes a80400d0
- 00b8895c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
- 00b8895c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c053a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
+ 00c053a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8895c bytes 082945f9
+ 00c053a4 bytes 082542f9
- 00b8896c ["INT_ADD", "register:40f0:8", ["const:b8896c:8", "const:4:8"]]
- 00b8896c ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00c053b4 ["INT_ADD", "register:40f0:8", ["const:c053b4:8", "const:4:8"]]
+ 00c053b4 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00b8896c bytes 05540194
+ 00c053b4 bytes 07540194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e679ae2a363cb52b7be1d3e115431b4"></a>

### [`00b88ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ad4.md) → [`00c0551c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0551c.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0d0.md) · 呼出先 5件 [`00b47d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47d4c.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md) [`00be0280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0280.md)
- 新版 呼出元 1件 [`00c58b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b20.md) · 呼出先 5件 [`00bb5598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md) [`00c5ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md) [`00c5cd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd90.md)

変更の種類 constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 90.70% / 新版 90.70%

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
      "definition_site": "00c05540",
      "incomplete_value": true,
      "site": "00c05544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b88af8",
      "incomplete_value": true,
      "site": "00b88afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "store_value",
    "new": {
      "definition_site": "00c055ac",
      "incomplete_value": true,
      "site": "00c055ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b88b64",
      "incomplete_value": true,
      "site": "00b88b64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00c05538",
      "READ",
      [
        "storage",
        "00c1bad0",
        null,
        "pointer"
      ]
    ],
    [
      "00c05544",
      "DATA",
      [
        "storage",
        "00c11358",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c05564",
      "READ",
      [
        "storage",
        "00c11370",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00c05538",
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c05544",
      "DATA",
      [
        "storage",
        "00c90b70",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00c05564",
      "READ",
      [
        "storage",
        "00c90b88",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b88ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ad4.md#insn-00b88ae8) · [`00b88af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ad4.md#insn-00b88af0) · [`00b88b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ad4.md#insn-00b88b08)
- 新版 [`00c05530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0551c.md#insn-00c05530) · [`00c05538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0551c.md#insn-00c05538) · [`00c05550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0551c.md#insn-00c05550)

~~~diff
- 00b88ae8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00c05530 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b88ae8 bytes 880400f0
+ 00c05530 bytes a80400d0
- 00b88af0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ad0:8"]]
- 00b88af0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c05538 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4f0:8"]]
+ 00c05538 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b88af0 bytes 086945f9
+ 00c05538 bytes 087942f9
- 00b88b08 ["INT_ADD", "register:40f0:8", ["const:b88b08:8", "const:4:8"]]
- 00b88b08 ["CALL", null, ["callee:00c5cd90:8"]]
+ 00c05550 ["INT_ADD", "register:40f0:8", ["const:c05550:8", "const:4:8"]]
+ 00c05550 ["CALL", null, ["callee:00c5cd90:8"]]
- 00b88b08 bytes de5d0194
+ 00c05550 bytes 105e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d420c12b71af3d0b11f2daa5bbf77be7"></a>

### [`00b88c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c60.md) → [`00c056a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c056a8.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 72.41% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_condition` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b88ea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b88ea4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b88f24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c056ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ],
    [
      "unmatched:00b88ea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c05920"
      ]
    ]
  ],
  "added": [
    [
      "00c056ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ],
    [
      "00c058f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c05920"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b88ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c60.md#insn-00b88ca4) · [`00b88ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c60.md#insn-00b88ea0) · [`00b88ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c60.md#insn-00b88ea4)
- 新版 [`00c056ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c056a8.md#insn-00c056ec)

~~~diff
- 00b88ca4 ["INT_ADD", "register:40f0:8", ["const:b88ca4:8", "const:4:8"]]
- 00b88ca4 ["CALL", null, ["ram:bdb440:8"]]
+ 00c056ec ["INT_ADD", "register:40f0:8", ["const:c056ec:8", "const:4:8"]]
+ 00c056ec ["CALL", null, ["ram:c57e90:8"]]
- 00b88ca4 bytes e7490194
+ 00c056ec bytes e9490194
- 00b88ea0 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b88ea0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:a2:8"]]
- 00b88ea0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b88ea0 bytes 8a8a0239
- 00b88ea4 ["COPY", "tmp:0:4", ["register:4058:4"]]
- 00b88ea4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:a2:8"]]
- 00b88ea4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b88ea4 bytes 6b8a0239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c74c2273c4b883e1b69150d600b3e87"></a>

### [`00b88f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md) → [`00c059a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md) FUN_00c059a4

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00b88544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88544.md) [`00b885f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b885f4.md) [`00b886b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b886b0.md) [`00b88760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88760.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00c04f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04f8c.md) [`00c0503c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0503c.md) [`00c050f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c050f8.md) [`00c051a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c051a8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 74.03% / 新版 74.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c059e0",
      "incomplete_value": false,
      "site": "00c059e4",
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
            "const:dbd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b88f98",
      "incomplete_value": false,
      "site": "00b88f9c",
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
            "const:5d6:8"
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
      "definition_site": "00c059f0",
      "incomplete_value": false,
      "site": "00c059f4",
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
            "const:86e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b88fa8",
      "incomplete_value": false,
      "site": "00b88fac",
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
            "const:995:8"
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
      "definition_site": "00c05a00",
      "incomplete_value": false,
      "site": "00c05a04",
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
            "const:521:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b88fb8",
      "incomplete_value": false,
      "site": "00b88fbc",
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
            "const:19c:8"
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
      "00c059c4",
      "DATA",
      [
        "storage",
        "0029782f",
        null,
        null
      ]
    ],
    [
      "00c059cc",
      "DATA",
      [
        "storage",
        "002facd8",
        "switchD_00b88f8c::switchdataD_002facd8",
        "byte"
      ]
    ],
    [
      "00c059e0",
      "DATA",
      [
        "storage",
        "002935d6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c059c4",
      "DATA",
      [
        "storage",
        "002a746a",
        null,
        null
      ]
    ],
    [
      "00c059cc",
      "DATA",
      [
        "storage",
        "00310b10",
        "switchD_00c059d4::switchdataD_00310b10",
        "byte"
      ]
    ],
    [
      "00c059e0",
      "DATA",
      [
        "storage",
        "002a2dbd",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b88f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md#insn-00b88f70) · [`00b88f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md#insn-00b88f74) · [`00b88f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md#insn-00b88f78)
- 新版 [`00c059b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md#insn-00c059b8) · [`00c059bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md#insn-00c059bc) · [`00c059c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md#insn-00c059c0)

~~~diff
- 00b88f70 ["COPY", "register:4048:8", ["const:2fa000:8"]]
+ 00c059b8 ["COPY", "register:4048:8", ["const:310000:8"]]
- 00b88f70 bytes 89bbffd0
+ 00c059b8 bytes 49b8fff0
- 00b88f74 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 00b88f74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b88f74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b88f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c059bc ["COPY", "tmp:0:8", ["const:b10:8"]]
+ 00c059bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c059bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c059bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b88f74 bytes 29613391
+ 00c059bc bytes 29412c91
- 00b88f78 ["COPY", "register:4000:8", ["const:297000:8"]]
+ 00c059c0 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00b88f78 bytes 60b8fff0
+ 00c059c0 bytes 00b5ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd04d88bf4d52fc38b588f9ad8e593d8"></a>

### [`00b89908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89908.md) → [`00c06350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06350.md) _ZNSt6__ndk18ios_base4InitC2Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be14f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14f0.md) · 呼出先 5件 [`00b89320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89320.md) [`00b898bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b898bc.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00c5e0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0f0.md) · 呼出先 5件 [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) [`00c06304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06304.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06384",
      "incomplete_value": false,
      "site": "00c06388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8993c",
      "incomplete_value": false,
      "site": "00b89940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "site": "00c06390",
      "value": [
        "leaf",
        "ram:c05d68:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b89948",
      "value": [
        "leaf",
        "ram:b89320:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06398",
      "incomplete_value": false,
      "site": "00c063ac",
      "value": [
        "leaf",
        "const:c06304:8"
      ]
    },
    "old": {
      "definition_site": "00b89950",
      "incomplete_value": false,
      "site": "00b89964",
      "value": [
        "leaf",
        "const:b898bc:8"
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
      "00c06368",
      "READ",
      [
        "storage",
        "010a2848",
        null,
        "undefined1"
      ]
    ],
    [
      "00c06384",
      "PARAM",
      [
        "storage",
        "010a2848",
        null,
        "undefined1"
      ]
    ],
    [
      "00c06390",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b89320"
      ]
    ]
  ],
  "added": [
    [
      "00c06368",
      "READ",
      [
        "storage",
        "01127750",
        null,
        "undefined1"
      ]
    ],
    [
      "00c06384",
      "PARAM",
      [
        "storage",
        "01127750",
        null,
        "undefined1"
      ]
    ],
    [
      "00c06390",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c05d68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89908.md#insn-00b89940) · [`00b89948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89908.md#insn-00b89948) · [`00b89964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89908.md#insn-00b89964)
- 新版 [`00c06388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06350.md#insn-00c06388) · [`00c06390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06350.md#insn-00c06390) · [`00c063ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06350.md#insn-00c063ac)

~~~diff
- 00b89940 ["INT_ADD", "register:40f0:8", ["const:b89940:8", "const:4:8"]]
- 00b89940 ["CALL", null, ["callee:00c57a50:8"]]
+ 00c06388 ["INT_ADD", "register:40f0:8", ["const:c06388:8", "const:4:8"]]
+ 00c06388 ["CALL", null, ["callee:00c57a50:8"]]
- 00b89940 bytes b0450194
+ 00c06388 bytes b2450194
- 00b89948 ["INT_ADD", "register:40f0:8", ["const:b89948:8", "const:4:8"]]
- 00b89948 ["CALL", null, ["ram:b89320:8"]]
+ 00c06390 ["INT_ADD", "register:40f0:8", ["const:c06390:8", "const:4:8"]]
+ 00c06390 ["CALL", null, ["ram:c05d68:8"]]
- 00b89948 bytes 76feff97
+ 00c06390 bytes 76feff97
- 00b89964 ["INT_ADD", "register:40f0:8", ["const:b89964:8", "const:4:8"]]
- 00b89964 ["CALL", null, ["callee:00c57a30:8"]]
+ 00c063ac ["INT_ADD", "register:40f0:8", ["const:c063ac:8", "const:4:8"]]
+ 00c063ac ["CALL", null, ["callee:00c57a30:8"]]
- 00b89964 bytes 9f450194
+ 00c063ac bytes a1450194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75f09b8d569f169840987ba521d5f412"></a>

### [`00b899cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b899cc.md) → [`00c06414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06414.md) FUN_00c06414

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b89320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89320.md) · 呼出先 2件 [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md)
- 新版 呼出元 1件 [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06434",
      "incomplete_value": true,
      "site": "00c06438",
      "value": [
        "live",
        "register:4008:8"
      ]
    },
    "old": {
      "definition_site": "00b899ec",
      "incomplete_value": true,
      "site": "00b899f0",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06430",
      "incomplete_value": true,
      "site": "00c06438",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:4b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b89a48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b899e8",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b899e8",
      "PARAM",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b89a44",
      "PARAM",
      [
        "storage",
        "002a52c9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c06430",
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c06430",
      "PARAM",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0648c",
      "PARAM",
      [
        "storage",
        "002b5cf7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b899f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b899cc.md#insn-00b899f0) · [`00b89a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b899cc.md#insn-00b89a48)
- 新版 [`00c06438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06414.md#insn-00c06438) · [`00c06490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06414.md#insn-00c06490)

~~~diff
- 00b899f0 ["INT_ADD", "register:40f0:8", ["const:b899f0:8", "const:4:8"]]
- 00b899f0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c06438 ["INT_ADD", "register:40f0:8", ["const:c06438:8", "const:4:8"]]
+ 00c06438 ["CALL", null, ["callee:00c57e80:8"]]
- 00b899f0 bytes 90460194
+ 00c06438 bytes 92460194
- 00b89a48 ["INT_ADD", "register:40f0:8", ["const:b89a48:8", "const:4:8"]]
- 00b89a48 ["CALL", null, ["callee:00c5dbb0:8"]]
- 00b89a48 bytes 5a5d0194
+ 00c06490 ["INT_ADD", "register:40f0:8", ["const:c06490:8", "const:4:8"]]
+ 00c06490 ["CALL", null, ["callee:00c5dbb0:8"]]
+ 00c06490 bytes c85d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4ba4dabd3cb883a4578d6623f59e008"></a>

### [`00b89a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89a64.md) → [`00c064ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c064ac.md) FUN_00c064ac

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be14a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 98.65% / 新版 98.65%

CFGの説明率　旧版 85.71% / 新版 88.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b89b18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c06560"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00b89b18"
      ],
      [
        "FALL_THROUGH",
        "00c06560"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00c06560",
      "incomplete_value": true,
      "site": "00c06570",
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
                "const:0:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89b18",
      "incomplete_value": true,
      "site": "00b89b28",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
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
      "unmatched:00b89b18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c06578"
      ]
    ]
  ],
  "added": [
    [
      "00c06560",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c06578"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89a64.md#insn-00b89b18) · [`00b89aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89a64.md#insn-00b89aa4)
- 新版 [`00c06560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c064ac.md#insn-00c06560) · [`00c064ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c064ac.md#insn-00c064ec)

~~~diff
- 00b89b18 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b89b18 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b89b18 bytes c1000054
+ 00c06560 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c06560 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00c06560 bytes c1000054
- 00b89aa4 ["INT_ADD", "register:40f0:8", ["const:b89aa4:8", "const:4:8"]]
- 00b89aa4 ["CALL", null, ["callee:00c5e0a0:8"]]
+ 00c064ec ["INT_ADD", "register:40f0:8", ["const:c064ec:8", "const:4:8"]]
+ 00c064ec ["CALL", null, ["callee:00c5e0a0:8"]]
- 00b89aa4 bytes 7f5e0194
+ 00c064ec bytes ed5e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe7a98c5dbf8b2bf09d0f88c6f69562f"></a>

### [`00b89b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89b8c.md) → [`00c065d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c065d4.md) FUN_00c065d4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 2件 [`00b89a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89a4c.md) [`00b89a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89a58.md) · 呼出先 2件 [`00be14a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14a0.md) [`00be14b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14b0.md)
- 新版 呼出元 2件 [`00c06494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06494.md) [`00c064a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c064a0.md) · 呼出先 2件 [`00c5e0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0a0.md) [`00c5e0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 90.70% / 新版 92.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06620",
      "incomplete_value": true,
      "site": "00c06624",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:40:8"
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

- 旧版 [`00b89bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89b8c.md#insn-00b89bdc) · [`00b89bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89b8c.md#insn-00b89bb8) · [`00b89bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89b8c.md#insn-00b89bc8)
- 新版 [`00c06624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c065d4.md#insn-00c06624) · [`00c06600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c065d4.md#insn-00c06600) · [`00c06610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c065d4.md#insn-00c06610)

~~~diff
- 00b89bdc ["INT_ADD", "register:40f0:8", ["const:b89bdc:8", "const:4:8"]]
- 00b89bdc ["CALL", null, ["callee:00c5e0b0:8"]]
+ 00c06624 ["INT_ADD", "register:40f0:8", ["const:c06624:8", "const:4:8"]]
+ 00c06624 ["CALL", null, ["callee:00c5e0b0:8"]]
- 00b89bdc bytes 355e0194
+ 00c06624 bytes a35e0194
- 00b89bb8 ["INT_RIGHT", "tmp:0:4", ["register:4008:4", "const:0:4"]]
- 00b89bb8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b89bb8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b89bb8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00c06600 ["INT_RIGHT", "tmp:0:4", ["register:4008:4", "const:0:4"]]
+ 00c06600 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c06600 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c06600 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b89bb8 bytes 010b0036
+ 00c06600 bytes 010b0036
- 00b89bc8 ["BRANCH", null, ["local:b28:8"]]
+ 00c06610 ["BRANCH", null, ["local:b27:8"]]
- 00b89bc8 bytes 54000014
+ 00c06610 bytes 54000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f3352b3b109efc4e6cc588090ca7e4e"></a>

### [`00b89d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89d60.md) → [`00c067a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c067a8.md) FUN_00c067a8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c067d4",
      "incomplete_value": true,
      "site": "00c067d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:4b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89d8c",
      "incomplete_value": true,
      "site": "00b89d90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab0:8"
              ]
            ]
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
      "00c067d4",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ],
    [
      "00c067d4",
      "PARAM",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c067d4",
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c067d4",
      "PARAM",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b89d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89d60.md#insn-00b89d90) · [`00b89d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89d60.md#insn-00b89d80) · [`00b89d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89d60.md#insn-00b89d84)
- 新版 [`00c067d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c067a8.md#insn-00c067d8) · [`00c067c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c067a8.md#insn-00c067c8) · [`00c067cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c067a8.md#insn-00c067cc)

~~~diff
- 00b89d90 ["INT_ADD", "register:40f0:8", ["const:b89d90:8", "const:4:8"]]
- 00b89d90 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c067d8 ["INT_ADD", "register:40f0:8", ["const:c067d8:8", "const:4:8"]]
+ 00c067d8 ["CALL", null, ["callee:00c57e80:8"]]
- 00b89d90 bytes a8450194
+ 00c067d8 bytes aa450194
- 00b89d80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b89d80 ["INT_ADD", "register:40f0:8", ["const:b89d80:8", "const:4:8"]]
- 00b89d80 ["CALLIND", null, ["register:0:8"]]
+ 00c067c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c067c8 ["INT_ADD", "register:40f0:8", ["const:c067c8:8", "const:4:8"]]
+ 00c067c8 ["CALLIND", null, ["register:0:8"]]
- 00b89d80 bytes 00013fd6
+ 00c067c8 bytes 00013fd6
- 00b89d84 ["COPY", "register:4008:8", ["const:c1b000:8"]]
+ 00c067cc ["COPY", "register:4008:8", ["const:c9b000:8"]]
- 00b89d84 bytes 810400d0
+ 00c067cc bytes a10400b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a486d4bb9418263a3e28a84fcfc17581"></a>

### [`00b8a060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a060.md) → [`00c06aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06aa8.md) FUN_00c06aa8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b89320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b89320.md) · 呼出先 2件 [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md)
- 新版 呼出元 1件 [`00c05d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 78.12% / 新版 78.12%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06ac4",
      "incomplete_value": true,
      "site": "00c06acc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
    "old": {
      "definition_site": "00b8a07c",
      "incomplete_value": true,
      "site": "00b8a084",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a0ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a0dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8a07c",
      "READ",
      [
        "storage",
        "00c1bd78",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b8a07c",
      "PARAM",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b8a0d8",
      "PARAM",
      [
        "storage",
        "002a52c9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c06ac4",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c06ac4",
      "PARAM",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c06b20",
      "PARAM",
      [
        "storage",
        "002b5cf7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a060.md#insn-00b8a084) · [`00b8a0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a060.md#insn-00b8a0ac) · [`00b8a0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a060.md#insn-00b8a0dc)
- 新版 [`00c06acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06aa8.md#insn-00c06acc)

~~~diff
- 00b8a084 ["INT_ADD", "register:40f0:8", ["const:b8a084:8", "const:4:8"]]
- 00b8a084 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c06acc ["INT_ADD", "register:40f0:8", ["const:c06acc:8", "const:4:8"]]
+ 00c06acc ["CALL", null, ["callee:00c57e80:8"]]
- 00b8a084 bytes eb440194
+ 00c06acc bytes ed440194
- 00b8a0ac ["COPY", "register:0:8", ["register:4048:8"]]
- 00b8a0ac ["INT_ADD", "register:40f0:8", ["const:b8a0ac:8", "const:4:8"]]
- 00b8a0ac ["CALLIND", null, ["register:0:8"]]
- 00b8a0ac bytes 20013fd6
- 00b8a0dc ["INT_ADD", "register:40f0:8", ["const:b8a0dc:8", "const:4:8"]]
- 00b8a0dc ["CALL", null, ["callee:00c5dbb0:8"]]
- 00b8a0dc bytes b55b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9187161da274aeda885e83fcdb4ec83"></a>

### [`00b8a3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a3ec.md) → [`00c06e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06e34.md) FUN_00c06e34

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06e60",
      "incomplete_value": true,
      "site": "00c06e64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
    "old": {
      "definition_site": "00b8a418",
      "incomplete_value": true,
      "site": "00b8a41c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
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
      "00c06e60",
      "READ",
      [
        "storage",
        "00c1bd78",
        null,
        "pointer"
      ]
    ],
    [
      "00c06e60",
      "PARAM",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c06e60",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c06e60",
      "PARAM",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a3ec.md#insn-00b8a41c) · [`00b8a40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a3ec.md#insn-00b8a40c) · [`00b8a410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a3ec.md#insn-00b8a410)
- 新版 [`00c06e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06e34.md#insn-00c06e64) · [`00c06e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06e34.md#insn-00c06e54) · [`00c06e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06e34.md#insn-00c06e58)

~~~diff
- 00b8a41c ["INT_ADD", "register:40f0:8", ["const:b8a41c:8", "const:4:8"]]
- 00b8a41c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c06e64 ["INT_ADD", "register:40f0:8", ["const:c06e64:8", "const:4:8"]]
+ 00c06e64 ["CALL", null, ["callee:00c57e80:8"]]
- 00b8a41c bytes 05440194
+ 00c06e64 bytes 07440194
- 00b8a40c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a40c ["INT_ADD", "register:40f0:8", ["const:b8a40c:8", "const:4:8"]]
- 00b8a40c ["CALLIND", null, ["register:0:8"]]
+ 00c06e54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c06e54 ["INT_ADD", "register:40f0:8", ["const:c06e54:8", "const:4:8"]]
+ 00c06e54 ["CALLIND", null, ["register:0:8"]]
- 00b8a40c bytes 00013fd6
+ 00c06e54 bytes 00013fd6
- 00b8a410 ["COPY", "register:4008:8", ["const:c1b000:8"]]
+ 00c06e58 ["COPY", "register:4008:8", ["const:c9b000:8"]]
- 00b8a410 bytes 810400b0
+ 00c06e58 bytes a10400b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68a2bfb77db809faa954197bf4d3400e"></a>

### [`00b8a88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a88c.md) → [`00c072d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c072d4.md) _ZNSt6__ndk17collateIwED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1510.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e110.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00c072e8",
      "value": [
        "leaf",
        "ram:c5e110:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b8a8a0",
      "value": [
        "leaf",
        "ram:be1510:8"
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
      "00c072e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1510"
      ]
    ]
  ],
  "added": [
    [
      "00c072e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e110"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a88c.md#insn-00b8a8a0)
- 新版 [`00c072e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c072d4.md#insn-00c072e8)

~~~diff
- 00b8a8a0 ["INT_ADD", "register:40f0:8", ["const:b8a8a0:8", "const:4:8"]]
- 00b8a8a0 ["CALL", null, ["ram:be1510:8"]]
+ 00c072e8 ["INT_ADD", "register:40f0:8", ["const:c072e8:8", "const:4:8"]]
+ 00c072e8 ["CALL", null, ["ram:c5e110:8"]]
- 00b8a8a0 bytes 1c5b0194
+ 00c072e8 bytes 8a5b0194
~~~


<a id="compare-aa5f8ca26eb719576720df36bc05a7d0"></a>

### [`00b8a910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a910.md) → [`00c07358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07358.md) _ZNKSt6__ndk17collateIwE12do_transformEPKwS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 70.00% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b8a93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a910.md#insn-00b8a93c) · [`00b8a948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a910.md#insn-00b8a948) · [`00b8a95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a910.md#insn-00b8a95c)
- 新版 [`00c07384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07358.md#insn-00c07384) · [`00c07390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07358.md#insn-00c07390) · [`00c073a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07358.md#insn-00c073a4)

~~~diff
- 00b8a93c ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
+ 00c07384 ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
- 00b8a93c bytes 02050054
+ 00c07384 bytes 02050054
- 00b8a948 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8a948 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b8a948 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00c07390 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c07390 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c07390 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00b8a948 bytes e8000054
+ 00c07390 bytes e8000054
- 00b8a95c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8a95c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00c073a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c073a4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b8a95c bytes 41020054
+ 00c073a4 bytes 41020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd7954d1c62ed0fa6d22dd5c14e8f25e"></a>

### [`00b8aa1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aa1c.md) → [`00c07464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07464.md) _ZNKSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjRb

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.12% / 新版 63.12%

CFGの説明率　旧版 12.24% / 新版 18.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8aa24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8aa24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8aa28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8aa24",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8aa28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8aa2c",
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
      "00c0746c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c07470",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c07474",
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

- 旧版 [`00b8aa24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aa1c.md#insn-00b8aa24) · [`00b8aa28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aa1c.md#insn-00b8aa28) · [`00b8aa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aa1c.md#insn-00b8aa2c)

~~~diff
- 00b8aa24 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b8aa24 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b8aa24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b8aa24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8aa24 bytes fd7b05a9
- 00b8aa28 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b8aa28 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b8aa28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b8aa28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8aa28 bytes f85f06a9
- 00b8aa2c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b8aa2c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b8aa2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b8aa2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8aa2c bytes f65707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6ce9913672c5a36aac61f0dc9dc19a8"></a>

### [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md) → [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) FUN_00c076f0

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00b8aa1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aa1c.md) [`00b96608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96608.md) [`00b96760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96760.md) [`00b9681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9681c.md) [`00b9696c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9696c.md) · 呼出先 3件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00be0f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f80.md)
- 新版 呼出元 7件 [`00c07464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07464.md) [`00c13050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13050.md) [`00c131a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c131a8.md) [`00c13264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13264.md) [`00c133b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c133b4.md) · 呼出先 3件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c5db80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.28% / 新版 92.28%

CFGの説明率　旧版 76.86% / 新版 70.99%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8acf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8acf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ad6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8acf4",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8acf8",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8ad00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c07760"
      ]
    ]
  ],
  "added": [
    [
      "00c0773c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00c07740",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ],
    [
      "00c07748",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c07760"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8acf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md#insn-00b8acf4) · [`00b8acf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md#insn-00b8acf8) · [`00b8ad00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md#insn-00b8ad00)

~~~diff
- 00b8acf4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b8acf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4030:4"]]
- 00b8acf4 bytes e63b00b9
- 00b8acf8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b8acf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:8"]]
- 00b8acf8 bytes e50700f9
- 00b8ad00 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b8ad00 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b8ad00 bytes c3000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4905c42a66f64464dcd323ea2fb0917c"></a>

### [`00b8b994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b994.md) → [`00c083dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c08/00c083dc.md) FUN_00c083dc

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8b98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b98c.md) · 呼出先 6件 [`00bb954c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb954c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)
- 新版 呼出元 1件 [`00c083d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c08/00c083d4.md) · 呼出先 6件 [`00c35f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35f94.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e120.md) [`00c5e130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e130.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.86% / 新版 84.86%

CFGの説明率　旧版 43.62% / 新版 38.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8bca0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c086e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ba84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c084c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8ba94"
      ]
    ],
    [
      "unmatched:00b8ba84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c084f8"
      ]
    ],
    [
      "unmatched:00b8ba8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c084e4"
      ]
    ]
  ],
  "added": [
    [
      "00c084c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c084dc"
      ]
    ],
    [
      "00c084cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c084f8"
      ]
    ],
    [
      "00c084d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c084e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8ba84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b994.md#insn-00b8ba84) · [`00b8ba8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b994.md#insn-00b8ba8c) · [`00b8ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b994.md#insn-00b8ba98)

~~~diff
- 00b8ba84 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 00b8ba84 bytes 60010054
- 00b8ba8c ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b8ba8c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b8ba8c bytes 950000b5
- 00b8ba98 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b8ba98 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b8ba98 bytes d50100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c89e1c19537a5b2e21d0d36749191966"></a>

### [`00b8c20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c20c.md) → [`00c08c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c08/00c08c54.md) FUN_00c08c54

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8c204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c204.md) · 呼出先 6件 [`00bb97f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb97f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)
- 新版 呼出元 1件 [`00c08c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c08/00c08c4c.md) · 呼出先 6件 [`00c36240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36240.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e120.md) [`00c5e130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e130.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.45% / 新版 88.45%

CFGの説明率　旧版 38.46% / 新版 42.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8c2d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8c2fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8c304"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c08d38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8c30c"
      ]
    ],
    [
      "unmatched:00b8c2fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c08d70"
      ]
    ],
    [
      "unmatched:00b8c304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c08d5c"
      ]
    ]
  ],
  "added": [
    [
      "00c08d38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c08d54"
      ]
    ],
    [
      "00c08d44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c08d70"
      ]
    ],
    [
      "00c08d4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c08d5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8c2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c20c.md#insn-00b8c2d4) · [`00b8c2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c20c.md#insn-00b8c2fc) · [`00b8c304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c20c.md#insn-00b8c304)

~~~diff
- 00b8c2d4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8c2d4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b8c2d4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b8c2d4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:1:8"]]
- 00b8c2d4 bytes 3815949a
- 00b8c2fc ["CBRANCH", null, ["local:b19:8", "register:101:1"]]
- 00b8c2fc bytes 60010054
- 00b8c304 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b8c304 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00b8c304 bytes 950000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0f4e0acd5be6720f2644137c2de2b83"></a>

### [`00b8d6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d6c4.md) → [`00c0a10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a10c.md) _ZNKSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjRPv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8ddb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a800.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.88% / 新版 77.88%

CFGの説明率　旧版 52.42% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_condition` 1件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0a158",
      "incomplete_value": true,
      "site": "00c0a158",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b8d710",
      "incomplete_value": true,
      "site": "00b8d710",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d908"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d918"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c0a150",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00c0a158",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0a15c",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0a150",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c0a158",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0a15c",
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8d7ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d6c4.md#insn-00b8d7ec) · [`00b8d7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d6c4.md#insn-00b8d7f4) · [`00b8d800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8d6c4.md#insn-00b8d800)

~~~diff
- 00b8d7ec ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00b8d7ec bytes 60010054
- 00b8d7f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b8d7f4 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b8d7f4 bytes 950000b5
- 00b8d800 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b8d800 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00b8d800 bytes d50100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af5d503faff340c42c0e5a1dc886a671"></a>

### [`00b8de6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8de6c.md) → [`00c0a8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a8b4.md) _ZNSt6__ndk16__clocEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0a910",
      "incomplete_value": true,
      "site": "00c0a910",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8dec8",
      "incomplete_value": true,
      "site": "00b8dec8",
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
            "const:990:8"
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
      "definition_site": "00c0a8f0",
      "incomplete_value": false,
      "site": "00c0a8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8dea8",
      "incomplete_value": false,
      "site": "00b8deac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "definition_site": "00c0a900",
      "incomplete_value": false,
      "site": "00c0a90c",
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
            "const:13c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8deb8",
      "incomplete_value": false,
      "site": "00b8dec4",
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
            "const:70e:8"
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
      "00c0a8d0",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0a8d8",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0a8f0",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c0a8d0",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0a8d8",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0a8f0",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8deac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8de6c.md#insn-00b8deac) · [`00b8dec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8de6c.md#insn-00b8dec4) · [`00b8dec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8de6c.md#insn-00b8dec8)
- 新版 [`00c0a8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a8b4.md#insn-00c0a8f4) · [`00c0a90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a8b4.md#insn-00c0a90c) · [`00c0a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a8b4.md#insn-00c0a910)

~~~diff
- 00b8deac ["INT_ADD", "register:40f0:8", ["const:b8deac:8", "const:4:8"]]
- 00b8deac ["CALL", null, ["callee:00c57a50:8"]]
+ 00c0a8f4 ["INT_ADD", "register:40f0:8", ["const:c0a8f4:8", "const:4:8"]]
+ 00c0a8f4 ["CALL", null, ["callee:00c57a50:8"]]
- 00b8deac bytes 55340194
+ 00c0a8f4 bytes 57340194
- 00b8dec4 ["INT_ADD", "register:40f0:8", ["const:b8dec4:8", "const:4:8"]]
- 00b8dec4 ["CALL", null, ["callee:00c5ce20:8"]]
+ 00c0a90c ["INT_ADD", "register:40f0:8", ["const:c0a90c:8", "const:4:8"]]
+ 00c0a90c ["CALL", null, ["callee:00c5ce20:8"]]
- 00b8dec4 bytes ab4d0194
+ 00c0a90c bytes 45490194
- 00b8dec8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
- 00b8dec8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c0a910 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00c0a910 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b8dec8 bytes 60ca04f9
+ 00c0a910 bytes 604e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ba5773ef946959a11237524870f8177"></a>

### [`00b8def4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8def4.md) → [`00c0a93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md) _ZNKSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjRb

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.40% / 新版 84.40%

CFGの説明率　旧版 56.67% / 新版 56.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0a9c0",
      "incomplete_value": true,
      "site": "00c0a9c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8df78",
      "incomplete_value": true,
      "site": "00b8df78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8dff0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8e008"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c0a9b8",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00c0a9c0",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0a9c4",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0a9b8",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c0a9c0",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0a9c4",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8dfac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8def4.md#insn-00b8dfac) · [`00b8dfd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8def4.md#insn-00b8dfd4) · [`00b8dff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8def4.md#insn-00b8dff0)
- 新版 [`00c0a9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md#insn-00c0a9f4)

~~~diff
- 00b8dfac ["INT_ADD", "register:40f0:8", ["const:b8dfac:8", "const:4:8"]]
- 00b8dfac ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c0a9f4 ["INT_ADD", "register:40f0:8", ["const:c0a9f4:8", "const:4:8"]]
+ 00c0a9f4 ["CALL", null, ["callee:00c5dae0:8"]]
- 00b8dfac bytes cd4b0194
+ 00c0a9f4 bytes 3b4c0194
- 00b8dfd4 ["INT_ADD", "register:40f0:8", ["const:b8dfd4:8", "const:4:8"]]
- 00b8dfd4 ["CALL", null, ["ram:bdb440:8"]]
- 00b8dfd4 bytes 1b350194
- 00b8dff0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b8dff0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00b8dff0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b8dff0 bytes b8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d76fd897e1ecd1f8fda6ce0805a916ef"></a>

### [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md) → [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) FUN_00c0abc8

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00b8def4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8def4.md) [`00b98350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98350.md) [`00b984a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b984a8.md) [`00b98564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98564.md) [`00b986b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b986b4.md) · 呼出先 3件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00be0f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f80.md)
- 新版 呼出元 7件 [`00c0a93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md) [`00c14d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14d98.md) [`00c14ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14ef0.md) [`00c14fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14fac.md) [`00c150fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c150fc.md) · 呼出先 3件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c5db80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.05% / 新版 89.05%

CFGの説明率　旧版 68.00% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8e1cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8e1d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c0ac14"
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
      "unmatched:00b8e1cc",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8e1d0",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8e1d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0ac38"
      ]
    ]
  ],
  "added": [
    [
      "00c0ac14",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00c0ac18",
      "WRITE",
      [
        "storage",
        "Stack[-0xf8]",
        null,
        null
      ]
    ],
    [
      "00c0ac20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0ac38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8e1cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md#insn-00b8e1cc) · [`00b8e1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md#insn-00b8e1d0) · [`00b8e1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md#insn-00b8e1d8)

~~~diff
- 00b8e1cc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b8e1cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4030:4"]]
- 00b8e1cc bytes e63b00b9
- 00b8e1d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b8e1d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:8"]]
- 00b8e1d0 bytes e50700f9
- 00b8e1d8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b8e1d8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b8e1d8 bytes c3000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8111725d2a7e03e0a2080c2bede229d7"></a>

### [`00b8e5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e5fc.md) → [`00c0b044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0b044.md) FUN_00c0b044

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8e5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e5f4.md) · 呼出先 6件 [`00bb92fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)
- 新版 呼出元 1件 [`00c0b03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0b03c.md) · 呼出先 6件 [`00c35d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35d44.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e190.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 83.06% / 新版 83.06%

CFGの説明率　旧版 46.88% / 新版 47.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 2件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8e6e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8e71c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8e720"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8e6e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0b14c"
      ]
    ],
    [
      "00c0b138",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8e714"
      ]
    ],
    [
      "00c0b140",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8e724"
      ]
    ]
  ],
  "added": [
    [
      "00c0b130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0b14c"
      ]
    ],
    [
      "00c0b138",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0b15c"
      ]
    ],
    [
      "00c0b140",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0b16c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8e6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e5fc.md#insn-00b8e6e8) · [`00b8e710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e5fc.md#insn-00b8e710) · [`00b8e71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e5fc.md#insn-00b8e71c)

~~~diff
- 00b8e6e8 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00b8e6e8 bytes e0000054
- 00b8e710 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8e710 ["INT_ADD", "register:40f0:8", ["const:b8e710:8", "const:4:8"]]
- 00b8e710 ["CALLIND", null, ["register:0:8"]]
- 00b8e710 bytes 00013fd6
- 00b8e71c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b8e71c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b8e71c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b8e71c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b8e71c bytes f503959a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba956f58d38881a5e00d7996cbad0965"></a>

### [`00b8ea2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ea2c.md) → [`00c0b474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0b474.md) FUN_00c0b474

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8ea24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ea24.md) · 呼出先 6件 [`00bb9424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9424.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)
- 新版 呼出元 1件 [`00c0b46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0b46c.md) · 呼出先 6件 [`00c35e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35e6c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e190.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.19% / 新版 74.19%

CFGの説明率　旧版 27.37% / 新版 25.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ea34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ea34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ea38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8ea34",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8ea38",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8ea3c",
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
      "00c0b47c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00c0b480",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00c0b484",
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

- 旧版 [`00b8ea34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ea2c.md#insn-00b8ea34) · [`00b8ea38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ea2c.md#insn-00b8ea38) · [`00b8ea3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ea2c.md#insn-00b8ea3c)

~~~diff
- 00b8ea34 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b8ea34 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b8ea34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 00b8ea34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8ea34 bytes fd7b18a9
- 00b8ea38 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b8ea38 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b8ea38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 00b8ea38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8ea38 bytes fc6f19a9
- 00b8ea3c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b8ea3c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b8ea3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 00b8ea3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8ea3c bytes fa671aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14b75337e35c66bf9613619cbf5e683b"></a>

### [`00b8ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ee5c.md) → [`00c0b8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0b8a4.md) FUN_00c0b8a4

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8ee54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ee54.md) · 呼出先 6件 [`00bb954c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb954c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)
- 新版 呼出元 1件 [`00c0b89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0b89c.md) · 呼出先 6件 [`00c35f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35f94.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e190.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.05% / 新版 81.05%

CFGの説明率　旧版 38.00% / 新版 40.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ee9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c0b8e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8eea0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8ee9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1d0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8eea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0b90c"
      ]
    ],
    [
      "unmatched:00b8eea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0b904"
      ]
    ]
  ],
  "added": [
    [
      "00c0b8e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1d0]",
        null,
        null
      ]
    ],
    [
      "00c0b8e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0b90c"
      ]
    ],
    [
      "00c0b8f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0b904"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8ee9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ee5c.md#insn-00b8ee9c) · [`00b8eea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ee5c.md#insn-00b8eea0) · [`00b8eea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8ee5c.md#insn-00b8eea8)

~~~diff
- 00b8ee9c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b8ee9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:8"]]
- 00b8ee9c bytes e50b00f9
- 00b8eea0 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00b8eea0 bytes 20010054
- 00b8eea8 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00b8eea8 bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6eca9c4a2d9def02addbcf1e41cb5e21"></a>

### [`00b8f28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f28c.md) → [`00c0bcd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0bcd4.md) FUN_00c0bcd4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8f284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f284.md) · 呼出先 6件 [`00bb96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb96a4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)
- 新版 呼出元 1件 [`00c0bccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0bccc.md) · 呼出先 6件 [`00c360ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c360ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e190.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 86.69% / 新版 86.69%

CFGの説明率　旧版 58.89% / 新版 55.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8f354"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8f378"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8f3ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8f378",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0bddc"
      ]
    ],
    [
      "00c0bdc8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8f3a4"
      ]
    ],
    [
      "00c0bdd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8f3b4"
      ]
    ]
  ],
  "added": [
    [
      "00c0bdc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0bddc"
      ]
    ],
    [
      "00c0bdc8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0bdec"
      ]
    ],
    [
      "00c0bdd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0bdfc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8f314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f28c.md#insn-00b8f314) · [`00b8f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f28c.md#insn-00b8f354) · [`00b8f378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f28c.md#insn-00b8f378)
- 新版 [`00c0bd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0b/00c0bcd4.md#insn-00c0bd5c)

~~~diff
- 00b8f314 ["INT_ADD", "register:40f0:8", ["const:b8f314:8", "const:4:8"]]
- 00b8f314 ["CALL", null, ["callee:00c5e190:8"]]
+ 00c0bd5c ["INT_ADD", "register:40f0:8", ["const:c0bd5c:8", "const:4:8"]]
+ 00c0bd5c ["CALL", null, ["callee:00c5e190:8"]]
- 00b8f314 bytes a3480194
+ 00c0bd5c bytes 0d490194
- 00b8f354 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8f354 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b8f354 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b8f354 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:1:8"]]
- 00b8f354 bytes 3815939a
- 00b8f378 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00b8f378 bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71d35cb251ae34ba154273db8a821efe"></a>

### [`00b8f6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f6bc.md) → [`00c0c104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0c104.md) FUN_00c0c104

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8f6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f6b4.md) · 呼出先 6件 [`00bb97f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb97f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)
- 新版 呼出元 1件 [`00c0c0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0c0fc.md) · 呼出先 6件 [`00c36240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36240.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e190.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.08% / 新版 85.08%

CFGの説明率　旧版 41.67% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8f798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c0c1e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8f7a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8f7a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0c20c"
      ]
    ],
    [
      "00c0c1f8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8f7d4"
      ]
    ],
    [
      "00c0c200",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8f7e4"
      ]
    ]
  ],
  "added": [
    [
      "00c0c1f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0c20c"
      ]
    ],
    [
      "00c0c1f8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0c21c"
      ]
    ],
    [
      "00c0c200",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0c22c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8f744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f6bc.md#insn-00b8f744) · [`00b8f798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f6bc.md#insn-00b8f798) · [`00b8f7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8f6bc.md#insn-00b8f7a8)
- 新版 [`00c0c18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0c104.md#insn-00c0c18c)

~~~diff
- 00b8f744 ["INT_ADD", "register:40f0:8", ["const:b8f744:8", "const:4:8"]]
- 00b8f744 ["CALL", null, ["callee:00c5e190:8"]]
+ 00c0c18c ["INT_ADD", "register:40f0:8", ["const:c0c18c:8", "const:4:8"]]
+ 00c0c18c ["CALL", null, ["callee:00c5e190:8"]]
- 00b8f744 bytes 97470194
+ 00c0c18c bytes 01480194
- 00b8f798 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:18:8"]]
- 00b8f798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b8f798 bytes a80e00f9
- 00b8f7a8 ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
- 00b8f7a8 bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-185efac55c31f5382849005da060816e"></a>

### [`00b8faec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8faec.md) → [`00c0c534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0c534.md) FUN_00c0c534

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8fae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8fae4.md) · 呼出先 6件 [`00bb9940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9940.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md)
- 新版 呼出元 1件 [`00c0c52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0c52c.md) · 呼出先 6件 [`00c36388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36388.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e190.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 81.85% / 新版 81.85%

CFGの説明率　旧版 31.07% / 新版 35.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8fbd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8fc0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8fc10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8fbd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0c63c"
      ]
    ],
    [
      "00c0c628",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8fc04"
      ]
    ],
    [
      "00c0c630",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8fc14"
      ]
    ]
  ],
  "added": [
    [
      "00c0c620",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0c63c"
      ]
    ],
    [
      "00c0c628",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0c64c"
      ]
    ],
    [
      "00c0c630",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0c65c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8fbd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8faec.md#insn-00b8fbd8) · [`00b8fc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8faec.md#insn-00b8fc00) · [`00b8fc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8faec.md#insn-00b8fc0c)

~~~diff
- 00b8fbd8 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00b8fbd8 bytes e0000054
- 00b8fc00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8fc00 ["INT_ADD", "register:40f0:8", ["const:b8fc00:8", "const:4:8"]]
- 00b8fc00 ["CALLIND", null, ["register:0:8"]]
- 00b8fc00 bytes 00013fd6
- 00b8fc0c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b8fc0c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b8fc0c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b8fc0c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b8fc0c bytes f503959a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-042f75bcda40d124b5b864471feec227"></a>

### [`00b8ff1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8ff1c.md) → [`00c0c964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0c964.md) FUN_00c0c964

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8ff14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8ff14.md) · 呼出先 6件 [`00bb9a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9a88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15c0.md)
- 新版 呼出元 1件 [`00c0c95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0c/00c0c95c.md) · 呼出先 6件 [`00c364d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c364d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.31% / 新版 75.31%

CFGの説明率　旧版 47.56% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ff5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ff5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ffb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8ff5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1f0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8ffb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1d0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8ffdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0ca40"
      ]
    ]
  ],
  "added": [
    [
      "00c0c9a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1f0]",
        null,
        null
      ]
    ],
    [
      "00c0c9fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x1d0]",
        null,
        null
      ]
    ],
    [
      "00c0ca24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0ca40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8ff5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8ff1c.md#insn-00b8ff5c) · [`00b8ffac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8ff1c.md#insn-00b8ffac) · [`00b8ffb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8f/00b8ff1c.md#insn-00b8ffb4)

~~~diff
- 00b8ff5c ["COPY", "tmp:0:8", ["register:4028:8"]]
- 00b8ff5c ["COPY", "tmp:1:8", ["register:4020:8"]]
- 00b8ff5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b8ff5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8ff5c bytes e51302a9
- 00b8ffac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8ffac ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b8ffac ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b8ffac ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:1:8"]]
- 00b8ffac bytes 3715939a
- 00b8ffb4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b8ffb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b8ffb4 bytes fb2300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98b5c36bf4ebb185ef82643fad7d05d8"></a>

### [`00b90734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90734.md) → [`00c0d17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d17c.md) FUN_00c0d17c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b9072c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b9072c.md) · 呼出先 6件 [`00bb9cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9cb8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be15c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15c0.md)
- 新版 呼出元 1件 [`00c0d174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d174.md) · 呼出先 6件 [`00c36700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36700.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 84.10% / 新版 84.10%

CFGの説明率　旧版 46.51% / 新版 48.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b907f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90828"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9082c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b907f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0d258"
      ]
    ],
    [
      "00c0d244",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b90820"
      ]
    ],
    [
      "00c0d24c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b90830"
      ]
    ]
  ],
  "added": [
    [
      "00c0d23c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0d258"
      ]
    ],
    [
      "00c0d244",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0d268"
      ]
    ],
    [
      "00c0d24c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0d278"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b907f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90734.md#insn-00b907f4) · [`00b9081c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90734.md#insn-00b9081c) · [`00b90828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90734.md#insn-00b90828)

~~~diff
- 00b907f4 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00b907f4 bytes e0000054
- 00b9081c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9081c ["INT_ADD", "register:40f0:8", ["const:b9081c:8", "const:4:8"]]
- 00b9081c ["CALLIND", null, ["register:0:8"]]
- 00b9081c bytes 00013fd6
- 00b90828 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b90828 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b90828 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b90828 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b90828 bytes f503959a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-296045a3ae1d950dc44df8ba78eca50b"></a>

### [`00b90b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90b38.md) → [`00c0d580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md) _ZNKSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjRPv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8ddb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8ddb8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a800.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.52% / 新版 71.52%

CFGの説明率　旧版 44.07% / 新版 45.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 2件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0d5cc",
      "incomplete_value": true,
      "site": "00c0d5cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b90b84",
      "incomplete_value": true,
      "site": "00b90b84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90c00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b90c00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c0d5c4",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00c0d5cc",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0d5d0",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0d5c4",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c0d5cc",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0d5d0",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b90b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90b38.md#insn-00b90b90) · [`00b90c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90b38.md#insn-00b90c00) · [`00b90c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b90/00b90b38.md#insn-00b90c40)

~~~diff
- 00b90b90 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b90b90 bytes 60010054
- 00b90c00 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b90c00 ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 00b90c00 ["COPY", "tmp:2:8", ["register:8:8"]]
- 00b90c00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b90c00 bytes f96300a9
- 00b90c40 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b90c40 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b90c40 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b90c40 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:1:8"]]
- 00b90c40 bytes 3615939a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73e88d888aa852d20f40cc78addd4e68"></a>

### [`00b9121c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b9121c.md) → [`00c0dc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0dc64.md) _ZNSt6__ndk19__num_getIcE19__stage2_float_prepERNS_8ios_baseEPcRcS5_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1550.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5e150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e150.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.46% / 新版 61.46%

CFGの説明率　旧版 5.88% / 新版 4.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9125c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91274"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91278"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c0dc9c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b9125c",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b9125c",
      "WRITE",
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
      "00c0dc9c",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c0dca4",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0dca4",
      "WRITE",
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

- 旧版 [`00b9125c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b9121c.md#insn-00b9125c) · [`00b91268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b9121c.md#insn-00b91268) · [`00b91274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b9121c.md#insn-00b91274)

~~~diff
- 00b9125c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b9125c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:8"]]
- 00b9125c bytes f80700f9
- 00b91268 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b91268 bytes 60010054
- 00b91274 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b91274 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b91274 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b91274 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-349cedd0be3cc11c1109787ed5bb7a16"></a>

### [`00b913b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b913b4.md) → [`00c0ddfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0ddfc.md) _ZNSt6__ndk19__num_getIcE19__stage2_float_loopEcRbRcPcRS4_ccRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSE_RjS4_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1560.md) · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)
- 新版 呼出元 1件 [`00c5e160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e160.md) · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.25% / 新版 79.25%

CFGの説明率　旧版 22.73% / 新版 16.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 8件, `unresolved_branch_alignment` 9件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91614"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b913e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0de8c"
      ]
    ],
    [
      "unmatched:00b9142c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0df24"
      ]
    ],
    [
      "unmatched:00b91448",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0dedc"
      ]
    ]
  ],
  "added": [
    [
      "00c0de2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0de8c"
      ]
    ],
    [
      "00c0de74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0df24"
      ]
    ],
    [
      "00c0de90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0dedc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b913e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b913b4.md#insn-00b913e4) · [`00b91400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b913b4.md#insn-00b91400) · [`00b91404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b913b4.md#insn-00b91404)

~~~diff
- 00b913e4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b913e4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b913e4 bytes 01030054
- 00b91400 ["COPY", "tmp:0:8", ["register:4020:8"]]
- 00b91400 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b91400 bytes 890000f9
- 00b91404 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b91404 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b91404 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b91404 bytes 0a010039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26afac3a80ff8a25d722c79adbc90208"></a>

### [`00b91630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91630.md) → [`00c0e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e078.md) _ZNSt6__ndk19__num_getIcE17__stage2_int_prepERNS_8ios_baseEPcRc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5e120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e120.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.11% / 新版 61.11%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9166c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91684"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91688"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b91664",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b91668",
      "READ",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9166c",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0e0ac",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e0b0",
      "READ",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00c0e0b4",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9166c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91630.md#insn-00b9166c) · [`00b91678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91630.md#insn-00b91678) · [`00b91684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91630.md#insn-00b91684)

~~~diff
- 00b9166c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b9166c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b9166c bytes f70b00f9
- 00b91678 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b91678 bytes 60010054
- 00b91684 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:18:8"]]
- 00b91684 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b91684 bytes a80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23e2fac9603a3bbda352f831b092a273"></a>

### [`00b917b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b917b0.md) → [`00c0e1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e1f8.md) _ZNSt6__ndk19__num_getIwE19__stage2_float_prepERNS_8ios_baseEPwRwS5_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be15c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15c0.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5e1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1b0.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 35.71% / 新版 31.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0e230",
      "incomplete_value": true,
      "site": "00c0e238",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b917e8",
      "incomplete_value": true,
      "site": "00b917f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91888"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c0e230",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e238",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0e23c",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0e230",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e238",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0e23c",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b91824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b917b0.md#insn-00b91824) · [`00b91860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b917b0.md#insn-00b91860) · [`00b91870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b917b0.md#insn-00b91870)
- 新版 [`00c0e26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e1f8.md#insn-00c0e26c) · [`00c0e2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e1f8.md#insn-00c0e2a8)

~~~diff
- 00b91824 ["INT_ADD", "register:40f0:8", ["const:b91824:8", "const:4:8"]]
- 00b91824 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c0e26c ["INT_ADD", "register:40f0:8", ["const:c0e26c:8", "const:4:8"]]
+ 00c0e26c ["CALL", null, ["callee:00c5dae0:8"]]
- 00b91824 bytes af3d0194
+ 00c0e26c bytes 1d3e0194
- 00b91860 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b91860 ["INT_ADD", "register:40f0:8", ["const:b91860:8", "const:4:8"]]
- 00b91860 ["CALLIND", null, ["register:0:8"]]
+ 00c0e2a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0e2a8 ["INT_ADD", "register:40f0:8", ["const:c0e2a8:8", "const:4:8"]]
+ 00c0e2a8 ["CALLIND", null, ["register:0:8"]]
- 00b91860 bytes 00013fd6
+ 00c0e2a8 bytes 00013fd6
- 00b91870 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b91870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b91870 bytes f70700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-629325ac90010b12da149c33722198b3"></a>

### [`00b91948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91948.md) → [`00c0e390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e390.md) _ZNSt6__ndk19__num_getIwE19__stage2_float_loopEwRbRcPcRS4_wwRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSE_RjPw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be15d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15d0.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 1件 [`00c5e1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1c0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 81.82% / 新版 76.60%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91b60"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91b64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91b74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c0e4e4",
      "READ",
      [
        "storage",
        "00c1bd90",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e4ec",
      "DATA",
      [
        "storage",
        "002fb026",
        "_ZNSt6__ndk114__num_get_base5__srcE",
        "string"
      ]
    ],
    [
      "unmatched:00b91b64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0e5cc"
      ]
    ]
  ],
  "added": [
    [
      "00c0e4e4",
      "READ",
      [
        "storage",
        "00c9b7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e4ec",
      "DATA",
      [
        "storage",
        "00310e5e",
        "_ZNSt6__ndk114__num_get_base5__srcE",
        "string"
      ]
    ],
    [
      "00c0e5ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0e5cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b91b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91948.md#insn-00b91b60) · [`00b91b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91948.md#insn-00b91b64) · [`00b91b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91948.md#insn-00b91b74)

~~~diff
- 00b91b60 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00b91b60 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b91b60 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b91b60 ["COPY", "register:4058:8", ["tmp:0:8"]]
- 00b91b60 bytes ab018c9a
- 00b91b64 ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00b91b64 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00b91b64 bytes 0b0100b4
- 00b91b74 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b91b74 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00b91b74 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00b91b74 ["CBRANCH", null, ["local:b25:8", "tmp:2:1"]]
- 00b91b74 bytes 8c000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-567b974b3387e2e979793eea93963708"></a>

### [`00b91bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91bb0.md) → [`00c0e5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e5f8.md) _ZNSt6__ndk19__num_getIwE17__stage2_int_prepERNS_8ios_baseEPwRw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be15a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15a0.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5e190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e190.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 54.44% / 新版 54.44%

CFGの説明率　旧版 14.29% / 新版 9.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91bb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91bb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91bbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b91bb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b91bbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b91bc0",
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
      "00c0e600",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c0e604",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c0e608",
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

- 旧版 [`00b91bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91bb0.md#insn-00b91bb8) · [`00b91bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91bb0.md#insn-00b91bbc) · [`00b91bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91bb0.md#insn-00b91bc0)

~~~diff
- 00b91bb8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b91bb8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b91bb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b91bb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b91bb8 bytes fd7b02a9
- 00b91bbc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b91bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b91bbc bytes f71b00f9
- 00b91bc0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b91bc0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b91bc0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b91bc0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b91bc0 bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d293a7f341ff5e62932a85a25d3c310"></a>

### [`00b91d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91d30.md) → [`00c0e778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e778.md) _ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcb

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 30.43% / 新版 22.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0e7e0",
      "incomplete_value": true,
      "site": "00c0e7e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b91d98",
      "incomplete_value": true,
      "site": "00b91d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c0e7fc"
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
      "00c0e7d8",
      "READ",
      [
        "storage",
        "00c1bd88",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e7e0",
      "DATA",
      [
        "storage",
        "010a2b80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0e7e4",
      "READ",
      [
        "storage",
        "010a2b80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0e7d8",
      "READ",
      [
        "storage",
        "00c9b7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c0e7e0",
      "DATA",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0e7e4",
      "READ",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b91da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91d30.md#insn-00b91da4) · [`00b91db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91d30.md#insn-00b91db4) · [`00b91dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91d30.md#insn-00b91dcc)
- 新版 [`00c0e7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e778.md#insn-00c0e7ec) · [`00c0e814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e778.md#insn-00c0e814)

~~~diff
- 00b91da4 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00c0e7ec ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00b91da4 bytes 60010054
+ 00c0e7ec bytes 60010054
- 00b91db4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b91db4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b91db4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b91db4 bytes a9831ff8
- 00b91dcc ["INT_ADD", "register:40f0:8", ["const:b91dcc:8", "const:4:8"]]
- 00b91dcc ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c0e814 ["INT_ADD", "register:40f0:8", ["const:c0e814:8", "const:4:8"]]
+ 00c0e814 ["CALL", null, ["callee:00c5dae0:8"]]
- 00b91dcc bytes 453c0194
+ 00c0e814 bytes b33c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8de7f04b1d219f1fdc388092b34078e"></a>

### [`00b91f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91f10.md) → [`00c0e958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e958.md) FUN_00c0e958

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b91f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91f00.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 1件 [`00c0e948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e948.md) · 呼出先 8件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0eb54",
      "incomplete_value": true,
      "site": "00c0eb54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9210c",
      "incomplete_value": true,
      "site": "00b9210c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "definition_site": "00c0ea38",
      "incomplete_value": true,
      "site": "00c0ea50",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:898:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b91ff0",
      "incomplete_value": true,
      "site": "00b92008",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c0eaf8",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b920b0",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c0ea2c",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0ea38",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0eaf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c0ea2c",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0ea38",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0eaf8",
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

- 旧版 [`00b92008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91f10.md#insn-00b92008) · [`00b920b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91f10.md#insn-00b920b0) · [`00b920f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91f10.md#insn-00b920f0)
- 新版 [`00c0ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e958.md#insn-00c0ea50) · [`00c0eaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e958.md#insn-00c0eaf8) · [`00c0eb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e958.md#insn-00c0eb38)

~~~diff
- 00b92008 ["INT_ADD", "register:40f0:8", ["const:b92008:8", "const:4:8"]]
- 00b92008 ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c0ea50 ["INT_ADD", "register:40f0:8", ["const:c0ea50:8", "const:4:8"]]
+ 00c0ea50 ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b92008 bytes cb040094
+ 00c0ea50 bytes cb040094
- 00b920b0 ["INT_ADD", "register:40f0:8", ["const:b920b0:8", "const:4:8"]]
- 00b920b0 ["CALL", null, ["ram:bdb440:8"]]
+ 00c0eaf8 ["INT_ADD", "register:40f0:8", ["const:c0eaf8:8", "const:4:8"]]
+ 00c0eaf8 ["CALL", null, ["ram:c57e90:8"]]
- 00b920b0 bytes e4240194
+ 00c0eaf8 bytes e6240194
- 00b920f0 ["INT_ADD", "register:40f0:8", ["const:b920f0:8", "const:4:8"]]
- 00b920f0 ["CALL", null, ["callee:00c57a50:8"]]
+ 00c0eb38 ["INT_ADD", "register:40f0:8", ["const:c0eb38:8", "const:4:8"]]
+ 00c0eb38 ["CALL", null, ["callee:00c57a50:8"]]
- 00b920f0 bytes c4230194
+ 00c0eb38 bytes c6230194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80ebbfe18433ceb1f247247ed269b56e"></a>

### [`00b9215c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b9215c.md) → [`00c0eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eba4.md) FUN_00c0eba4

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b9214c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b9214c.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 1件 [`00c0eb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eb94.md) · 呼出先 8件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.12% / 新版 87.12%

CFGの説明率　旧版 90.91% / 新版 86.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c0eda0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92210"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c0ec78",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0ec84",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0ed44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c0ec78",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0ec84",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0ed44",
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

- 旧版 [`00b92210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b9215c.md#insn-00b92210) · [`00b92254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b9215c.md#insn-00b92254) · [`00b922fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b9215c.md#insn-00b922fc)
- 新版 [`00c0ec9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eba4.md#insn-00c0ec9c) · [`00c0ed44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eba4.md#insn-00c0ed44)

~~~diff
- 00b92210 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b92210 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b92210 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b92210 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
- 00b92210 bytes 4901891a
- 00b92254 ["INT_ADD", "register:40f0:8", ["const:b92254:8", "const:4:8"]]
- 00b92254 ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c0ec9c ["INT_ADD", "register:40f0:8", ["const:c0ec9c:8", "const:4:8"]]
+ 00c0ec9c ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b92254 bytes 38040094
+ 00c0ec9c bytes 38040094
- 00b922fc ["INT_ADD", "register:40f0:8", ["const:b922fc:8", "const:4:8"]]
- 00b922fc ["CALL", null, ["ram:bdb440:8"]]
+ 00c0ed44 ["INT_ADD", "register:40f0:8", ["const:c0ed44:8", "const:4:8"]]
+ 00c0ed44 ["CALL", null, ["ram:c57e90:8"]]
- 00b922fc bytes 51240194
+ 00c0ed44 bytes 53240194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3350b7fd40fc78f124da9f40578bd199"></a>

### [`00b923a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b923a8.md) → [`00c0edf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0edf0.md) FUN_00c0edf0

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b92398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92398.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 1件 [`00c0ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0ede0.md) · 呼出先 8件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 92.80% / 新版 92.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0efd0",
      "incomplete_value": true,
      "site": "00c0efd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b92588",
      "incomplete_value": true,
      "site": "00b92588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0eeb4",
      "incomplete_value": true,
      "site": "00c0eecc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:898:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9246c",
      "incomplete_value": true,
      "site": "00b92484",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c0ef74",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b9252c",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c0eea8",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0eeb4",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0ef74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c0eea8",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0eeb4",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0ef74",
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

- 旧版 [`00b92484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b923a8.md#insn-00b92484) · [`00b9252c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b923a8.md#insn-00b9252c) · [`00b9256c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b923a8.md#insn-00b9256c)
- 新版 [`00c0eecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0edf0.md#insn-00c0eecc) · [`00c0ef74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0edf0.md#insn-00c0ef74) · [`00c0efb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0edf0.md#insn-00c0efb4)

~~~diff
- 00b92484 ["INT_ADD", "register:40f0:8", ["const:b92484:8", "const:4:8"]]
- 00b92484 ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c0eecc ["INT_ADD", "register:40f0:8", ["const:c0eecc:8", "const:4:8"]]
+ 00c0eecc ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b92484 bytes ac030094
+ 00c0eecc bytes ac030094
- 00b9252c ["INT_ADD", "register:40f0:8", ["const:b9252c:8", "const:4:8"]]
- 00b9252c ["CALL", null, ["ram:bdb440:8"]]
+ 00c0ef74 ["INT_ADD", "register:40f0:8", ["const:c0ef74:8", "const:4:8"]]
+ 00c0ef74 ["CALL", null, ["ram:c57e90:8"]]
- 00b9252c bytes c5230194
+ 00c0ef74 bytes c7230194
- 00b9256c ["INT_ADD", "register:40f0:8", ["const:b9256c:8", "const:4:8"]]
- 00b9256c ["CALL", null, ["callee:00c57a50:8"]]
+ 00c0efb4 ["INT_ADD", "register:40f0:8", ["const:c0efb4:8", "const:4:8"]]
+ 00c0efb4 ["CALL", null, ["callee:00c57a50:8"]]
- 00b9256c bytes a5220194
+ 00c0efb4 bytes a7220194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4888c1523c348793983cca285556fa34"></a>

### [`00b925d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925d8.md) → [`00c0f020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f020.md) FUN_00c0f020

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b925c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925c8.md) · 呼出先 8件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 1件 [`00c0f010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f010.md) · 呼出先 8件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 91.20% / 新版 91.20%

CFGの説明率　旧版 80.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0f200",
      "incomplete_value": true,
      "site": "00c0f200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b927b8",
      "incomplete_value": true,
      "site": "00b927b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b926d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c0f120"
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
      "00c0f0d8",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f0e4",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b926d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0f170"
      ]
    ]
  ],
  "added": [
    [
      "00c0f0d8",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f0e4",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c0f120",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0f170"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b926b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925d8.md#insn-00b926b4) · [`00b926d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925d8.md#insn-00b926d8) · [`00b92754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925d8.md#insn-00b92754)
- 新版 [`00c0f0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f020.md#insn-00c0f0fc) · [`00c0f19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f020.md#insn-00c0f19c)

~~~diff
- 00b926b4 ["INT_ADD", "register:40f0:8", ["const:b926b4:8", "const:4:8"]]
- 00b926b4 ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c0f0fc ["INT_ADD", "register:40f0:8", ["const:c0f0fc:8", "const:4:8"]]
+ 00c0f0fc ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b926b4 bytes 20030094
+ 00c0f0fc bytes 20030094
- 00b926d8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b926d8 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00b926d8 bytes 81020054
- 00b92754 ["INT_ADD", "register:40f0:8", ["const:b92754:8", "const:4:8"]]
- 00b92754 ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00c0f19c ["INT_ADD", "register:40f0:8", ["const:c0f19c:8", "const:4:8"]]
+ 00c0f19c ["CALL", null, ["callee:00c5e1d0:8"]]
- 00b92754 bytes a33b0194
+ 00c0f19c bytes 0d3c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-239b2496fba1ac7fdb428d07cefc658d"></a>

### [`00b92808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92808.md) → [`00c0f250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f250.md) FUN_00c0f250

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b927f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b927f8.md) · 呼出先 12件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00c0f240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f240.md) · 呼出先 12件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.71% / 新版 71.71%

CFGの説明率　旧版 59.34% / 新版 50.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `return_value_candidate` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92848"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92b4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92b8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b92848",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00c0f350",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f354",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b92bd8"
      ]
    ]
  ],
  "added": [
    [
      "00c0f290",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00c0f350",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0f354",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0f620"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b92848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92808.md#insn-00b92848) · [`00b92924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92808.md#insn-00b92924) · [`00b9297c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92808.md#insn-00b9297c)
- 新版 [`00c0f36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f250.md#insn-00c0f36c) · [`00c0f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f250.md#insn-00c0f3c4)

~~~diff
- 00b92848 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b92848 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00b92848 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b92848 bytes a8031ff8
- 00b92924 ["INT_ADD", "register:40f0:8", ["const:b92924:8", "const:4:8"]]
- 00b92924 ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c0f36c ["INT_ADD", "register:40f0:8", ["const:c0f36c:8", "const:4:8"]]
+ 00c0f36c ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b92924 bytes 84020094
+ 00c0f36c bytes 84020094
- 00b9297c ["INT_ADD", "register:40f0:8", ["const:b9297c:8", "const:4:8"]]
- 00b9297c ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c0f3c4 ["INT_ADD", "register:40f0:8", ["const:c0f3c4:8", "const:4:8"]]
+ 00c0f3c4 ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b9297c bytes 6e020094
+ 00c0f3c4 bytes 6e020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86e1572cd5906c811f12d7d36e15b96c"></a>

### [`00b92c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92c98.md) → [`00c0f6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f6e0.md) FUN_00c0f6e0

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b92c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92c88.md) · 呼出先 12件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00c0f6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f6d0.md) · 呼出先 12件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.03% / 新版 82.03%

CFGの説明率　旧版 82.22% / 新版 81.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `call_target` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92cb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92cb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92d90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b92cb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b92d90",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b92d94",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c0f6f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c0f7d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00c0f7dc",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b92cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92c98.md#insn-00b92cb0) · [`00b92d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92c98.md#insn-00b92d90) · [`00b92d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92c98.md#insn-00b92d98)

~~~diff
- 00b92cb0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b92cb0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b92cb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00b92cb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b92cb0 bytes f6570da9
- 00b92d90 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b92d90 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b92d90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b92d90 bytes aa831df8
- 00b92d98 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b92d98 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b92d98 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b92d98 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b92d98 bytes 48160036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8cb044d1cabc1fecc1e416e27bef3e2"></a>

### [`00b93110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93110.md) → [`00c0fb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fb58.md) _ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcPKv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.75% / 新版 81.75%

CFGの説明率　旧版 65.52% / 新版 59.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0fc4c",
      "incomplete_value": true,
      "site": "00c0fc4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b93204",
      "incomplete_value": true,
      "site": "00b93204",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b932f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c0fd3c"
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
      "unmatched:00b9313c",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0fb98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b932d0"
      ]
    ],
    [
      "unmatched:00b93154",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0fb84",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c0fb98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0fd18"
      ]
    ],
    [
      "00c0fb9c",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b93170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93110.md#insn-00b93170) · [`00b93210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93110.md#insn-00b93210) · [`00b93234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93110.md#insn-00b93234)
- 新版 [`00c0fbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fb58.md#insn-00c0fbb8) · [`00c0fc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fb58.md#insn-00c0fc58) · [`00c0fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fb58.md#insn-00c0fc7c)

~~~diff
- 00b93170 ["INT_ADD", "register:40f0:8", ["const:b93170:8", "const:4:8"]]
- 00b93170 ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c0fbb8 ["INT_ADD", "register:40f0:8", ["const:c0fbb8:8", "const:4:8"]]
+ 00c0fbb8 ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b93170 bytes 71000094
+ 00c0fbb8 bytes 71000094
- 00b93210 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 00c0fc58 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00b93210 bytes 40010054
+ 00c0fc58 bytes 40010054
- 00b93234 ["INT_ADD", "register:40f0:8", ["const:b93234:8", "const:4:8"]]
- 00b93234 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c0fc7c ["INT_ADD", "register:40f0:8", ["const:c0fc7c:8", "const:4:8"]]
+ 00c0fc7c ["CALL", null, ["callee:00c5dae0:8"]]
- 00b93234 bytes 2b370194
+ 00c0fc7c bytes 99370194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-654041a77067543893d4136c6fc777bf"></a>

### [`00b93464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93464.md) → [`00c0feac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0feac.md) _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwb

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0ff14",
      "incomplete_value": true,
      "site": "00c0ff14",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b934cc",
      "incomplete_value": true,
      "site": "00b934cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0ff1c",
      "incomplete_value": true,
      "site": "00c0ff20",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b934d4",
      "incomplete_value": true,
      "site": "00b934d8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0ff40",
      "incomplete_value": true,
      "site": "00c0ff48",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:7c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b934f8",
      "incomplete_value": true,
      "site": "00b93500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
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
      "00c0ff0c",
      "READ",
      [
        "storage",
        "00c1bd98",
        null,
        "pointer"
      ]
    ],
    [
      "00c0ff14",
      "DATA",
      [
        "storage",
        "010a2b90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0ff18",
      "READ",
      [
        "storage",
        "010a2b90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c0ff0c",
      "READ",
      [
        "storage",
        "00c9b7c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c0ff14",
      "DATA",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c0ff18",
      "READ",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b93500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93464.md#insn-00b93500) · [`00b93528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93464.md#insn-00b93528) · [`00b93600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93464.md#insn-00b93600)
- 新版 [`00c0ff48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0feac.md#insn-00c0ff48) · [`00c0ff70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0feac.md#insn-00c0ff70) · [`00c10048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0feac.md#insn-00c10048)

~~~diff
- 00b93500 ["INT_ADD", "register:40f0:8", ["const:b93500:8", "const:4:8"]]
- 00b93500 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c0ff48 ["INT_ADD", "register:40f0:8", ["const:c0ff48:8", "const:4:8"]]
+ 00c0ff48 ["CALL", null, ["callee:00c5dae0:8"]]
- 00b93500 bytes 78360194
+ 00c0ff48 bytes e6360194
- 00b93528 ["INT_ADD", "register:40f0:8", ["const:b93528:8", "const:4:8"]]
- 00b93528 ["CALL", null, ["ram:bdb440:8"]]
+ 00c0ff70 ["INT_ADD", "register:40f0:8", ["const:c0ff70:8", "const:4:8"]]
+ 00c0ff70 ["CALL", null, ["ram:c57e90:8"]]
- 00b93528 bytes c61f0194
+ 00c0ff70 bytes c81f0194
- 00b93600 ["INT_ADD", "register:40f0:8", ["const:b93600:8", "const:4:8"]]
- 00b93600 ["CALL", null, ["ram:b890e8:8"]]
+ 00c10048 ["INT_ADD", "register:40f0:8", ["const:c10048:8", "const:4:8"]]
+ 00c10048 ["CALL", null, ["ram:c05b30:8"]]
- 00b93600 bytes bad6ff97
+ 00c10048 bytes bad6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b66a6385c8e6a24ea8da1c604f5bced5"></a>

### [`00b93644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93644.md) → [`00c1008c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c1008c.md) FUN_00c1008c

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b93634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93634.md) · 呼出先 8件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 1件 [`00c1007c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c1007c.md) · 呼出先 8件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 81.82% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9367c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c10288",
      "incomplete_value": true,
      "site": "00c10288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93840",
      "incomplete_value": true,
      "site": "00b93840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c100c4"
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
      "unmatched:00b9367c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00c10160",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1016c",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c100c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00c10160",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1016c",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9367c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93644.md#insn-00b9367c) · [`00b936f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93644.md#insn-00b936f8) · [`00b9373c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93644.md#insn-00b9373c)
- 新版 [`00c10184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c1008c.md#insn-00c10184)

~~~diff
- 00b9367c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b9367c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b9367c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b9367c bytes a8831ff8
- 00b936f8 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b936f8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b936f8 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b936f8 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
- 00b936f8 bytes 4901891a
- 00b9373c ["INT_ADD", "register:40f0:8", ["const:b9373c:8", "const:4:8"]]
- 00b9373c ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c10184 ["INT_ADD", "register:40f0:8", ["const:c10184:8", "const:4:8"]]
+ 00c10184 ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b9373c bytes fefeff97
+ 00c10184 bytes fefeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-211cc4dac029a98d1bb74dcace900cf8"></a>

### [`00b93890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93890.md) → [`00c102d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102d8.md) FUN_00c102d8

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b93880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93880.md) · 呼出先 8件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 1件 [`00c102c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102c8.md) · 呼出先 8件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c104d4",
      "incomplete_value": true,
      "site": "00c104d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93a8c",
      "incomplete_value": true,
      "site": "00b93a8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c103b8",
      "incomplete_value": true,
      "site": "00c103d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:898:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93970",
      "incomplete_value": true,
      "site": "00b93988",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c10478",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b93a30",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c103ac",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c103b8",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10478",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c103ac",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c103b8",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c10478",
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

- 旧版 [`00b93988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93890.md#insn-00b93988) · [`00b93a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93890.md#insn-00b93a30) · [`00b93a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93890.md#insn-00b93a70)
- 新版 [`00c103d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102d8.md#insn-00c103d0) · [`00c10478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102d8.md#insn-00c10478) · [`00c104b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102d8.md#insn-00c104b8)

~~~diff
- 00b93988 ["INT_ADD", "register:40f0:8", ["const:b93988:8", "const:4:8"]]
- 00b93988 ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c103d0 ["INT_ADD", "register:40f0:8", ["const:c103d0:8", "const:4:8"]]
+ 00c103d0 ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b93988 bytes 6bfeff97
+ 00c103d0 bytes 6bfeff97
- 00b93a30 ["INT_ADD", "register:40f0:8", ["const:b93a30:8", "const:4:8"]]
- 00b93a30 ["CALL", null, ["ram:bdb440:8"]]
+ 00c10478 ["INT_ADD", "register:40f0:8", ["const:c10478:8", "const:4:8"]]
+ 00c10478 ["CALL", null, ["ram:c57e90:8"]]
- 00b93a30 bytes 841e0194
+ 00c10478 bytes 861e0194
- 00b93a70 ["INT_ADD", "register:40f0:8", ["const:b93a70:8", "const:4:8"]]
- 00b93a70 ["CALL", null, ["callee:00c57a50:8"]]
+ 00c104b8 ["INT_ADD", "register:40f0:8", ["const:c104b8:8", "const:4:8"]]
+ 00c104b8 ["CALL", null, ["callee:00c57a50:8"]]
- 00b93a70 bytes 641d0194
+ 00c104b8 bytes 661d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f792116e4c28ec64968a30706e184ba5"></a>

### [`00b93adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93adc.md) → [`00c10524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10524.md) FUN_00c10524

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b93acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93acc.md) · 呼出先 8件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 1件 [`00c10514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10514.md) · 呼出先 8件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 92.80% / 新版 92.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c10704",
      "incomplete_value": true,
      "site": "00c10704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93cbc",
      "incomplete_value": true,
      "site": "00b93cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:990:8"
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
    "new": null,
    "old": {
      "definition_site": "00b93ba4",
      "incomplete_value": true,
      "site": "00b93bb8",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:20:8"
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
    "new": null,
    "old": {
      "definition_site": "00b93ba0",
      "incomplete_value": true,
      "site": "00b93bb8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
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
      "00c105dc",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c105e8",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00c106a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c105dc",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c105e8",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c106a8",
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

- 旧版 [`00b93bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93adc.md#insn-00b93bb8) · [`00b93c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93adc.md#insn-00b93c60) · [`00b93ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93adc.md#insn-00b93ca0)
- 新版 [`00c10600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10524.md#insn-00c10600) · [`00c106a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10524.md#insn-00c106a8) · [`00c106e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10524.md#insn-00c106e8)

~~~diff
- 00b93bb8 ["INT_ADD", "register:40f0:8", ["const:b93bb8:8", "const:4:8"]]
- 00b93bb8 ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c10600 ["INT_ADD", "register:40f0:8", ["const:c10600:8", "const:4:8"]]
+ 00c10600 ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b93bb8 bytes dffdff97
+ 00c10600 bytes dffdff97
- 00b93c60 ["INT_ADD", "register:40f0:8", ["const:b93c60:8", "const:4:8"]]
- 00b93c60 ["CALL", null, ["ram:bdb440:8"]]
+ 00c106a8 ["INT_ADD", "register:40f0:8", ["const:c106a8:8", "const:4:8"]]
+ 00c106a8 ["CALL", null, ["ram:c57e90:8"]]
- 00b93c60 bytes f81d0194
+ 00c106a8 bytes fa1d0194
- 00b93ca0 ["INT_ADD", "register:40f0:8", ["const:b93ca0:8", "const:4:8"]]
- 00b93ca0 ["CALL", null, ["callee:00c57a50:8"]]
+ 00c106e8 ["INT_ADD", "register:40f0:8", ["const:c106e8:8", "const:4:8"]]
+ 00c106e8 ["CALL", null, ["callee:00c57a50:8"]]
- 00b93ca0 bytes d81c0194
+ 00c106e8 bytes da1c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d23a1f7ef21d4fbaf0b05d0fe8a309a"></a>

### [`00b93d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93d0c.md) → [`00c10754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10754.md) FUN_00c10754

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b93cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93cfc.md) · 呼出先 8件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 1件 [`00c10744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10744.md) · 呼出先 8件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.60% / 新版 77.60%

CFGの説明率　旧版 41.46% / 新版 30.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b93eec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c10934"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b93dcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b93dc4",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b93dcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c10910"
      ]
    ],
    [
      "unmatched:00b93dd0",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1080c",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10814",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c10910"
      ]
    ],
    [
      "00c10818",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b93dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93d0c.md#insn-00b93dcc) · [`00b93de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93d0c.md#insn-00b93de8) · [`00b93e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93d0c.md#insn-00b93e34)
- 新版 [`00c10830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10754.md#insn-00c10830)

~~~diff
- 00b93dcc ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b93dcc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b93dcc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b93dcc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b93dcc bytes e8070036
- 00b93de8 ["INT_ADD", "register:40f0:8", ["const:b93de8:8", "const:4:8"]]
- 00b93de8 ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c10830 ["INT_ADD", "register:40f0:8", ["const:c10830:8", "const:4:8"]]
+ 00c10830 ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b93de8 bytes 53fdff97
+ 00c10830 bytes 53fdff97
- 00b93e34 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b93e34 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00b93e34 bytes 4b010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e65075c17f08893b75da27cf3575a0da"></a>

### [`00b93f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93f3c.md) → [`00c10984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10984.md) FUN_00c10984

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b93f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93f2c.md) · 呼出先 12件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00c10974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10974.md) · 呼出先 12件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.84% / 新版 79.84%

CFGの説明率　旧版 80.68% / 新版 75.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 1件, `store_destination` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b94038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b94280"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b942c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b94038",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9403c",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b94040",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b9430c"
      ]
    ]
  ],
  "added": [
    [
      "00c10a80",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "00c10a84",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c10a88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c10d54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b94038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93f3c.md#insn-00b94038) · [`00b94040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93f3c.md#insn-00b94040) · [`00b94058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93f3c.md#insn-00b94058)
- 新版 [`00c10aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10984.md#insn-00c10aa0)

~~~diff
- 00b94038 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b94038 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00b94038 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b94038 bytes aa831cf8
- 00b94040 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b94040 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b94040 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b94040 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b94040 bytes 68160036
- 00b94058 ["INT_ADD", "register:40f0:8", ["const:b94058:8", "const:4:8"]]
- 00b94058 ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c10aa0 ["INT_ADD", "register:40f0:8", ["const:c10aa0:8", "const:4:8"]]
+ 00c10aa0 ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b94058 bytes b7fcff97
+ 00c10aa0 bytes b7fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15fce54d72a73b251ce5843d28ac6cae"></a>

### [`00b943cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b943cc.md) → [`00c10e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10e14.md) FUN_00c10e14

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b943bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b943bc.md) · 呼出先 12件 [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00c10e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10e04.md) · 呼出先 12件 [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.39% / 新版 75.39%

CFGの説明率　旧版 55.68% / 新版 47.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `call_target` 1件, `store_destination` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b943e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b943e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b943e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b943e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b943e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b943e8",
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
      "00c10e28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c10e2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c10e30",
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

- 旧版 [`00b943e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b943cc.md#insn-00b943e0) · [`00b943e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b943cc.md#insn-00b943e4) · [`00b943e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b943cc.md#insn-00b943e8)

~~~diff
- 00b943e0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b943e0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b943e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 00b943e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b943e0 bytes f85f17a9
- 00b943e4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b943e4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b943e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 00b943e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b943e4 bytes f65718a9
- 00b943e8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b943e8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b943e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 00b943e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b943e8 bytes f44f19a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f2fece66cb89a38a8449865a4c2f62a"></a>

### [`00b94844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94844.md) → [`00c1128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c1128c.md) _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwPKv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.24% / 新版 61.24%

CFGの説明率　旧版 31.03% / 新版 19.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9493c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b94954"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b94958"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b94874",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c112d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b94a10"
      ]
    ],
    [
      "unmatched:00b9488c",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c112bc",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c112d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c11458"
      ]
    ],
    [
      "00c112d4",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b948a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94844.md#insn-00b948a8) · [`00b948c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94844.md#insn-00b948c8) · [`00b948e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94844.md#insn-00b948e4)
- 新版 [`00c112f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c1128c.md#insn-00c112f0)

~~~diff
- 00b948a8 ["INT_ADD", "register:40f0:8", ["const:b948a8:8", "const:4:8"]]
- 00b948a8 ["CALL", null, ["callee:00c0fd7c:8"]]
+ 00c112f0 ["INT_ADD", "register:40f0:8", ["const:c112f0:8", "const:4:8"]]
+ 00c112f0 ["CALL", null, ["callee:00c0fd7c:8"]]
- 00b948a8 bytes a3faff97
+ 00c112f0 bytes a3faff97
- 00b948c8 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00b948c8 bytes e0020054
- 00b948e4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b948e4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b948e4 bytes 81000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5185fd574cceefeed12cae84d01b3e9a"></a>

### [`00b94c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94c74.md) → [`00c116bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c116bc.md) _ZNSt6__ndk19__num_putIcE21__widen_and_group_intEPcS2_S2_S2_RS2_S3_RKNS_6localeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be15e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15e0.md) · 呼出先 4件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5e1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1d0.md) · 呼出先 4件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.36% / 新版 91.36%

CFGの説明率　旧版 77.59% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b94cbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b94cdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b94ce8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b94ca4",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b94cbc",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b94cbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c116ec",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c11704",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c11704",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b94cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94c74.md#insn-00b94cbc) · [`00b94ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94c74.md#insn-00b94ccc) · [`00b94cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94c74.md#insn-00b94cdc)

~~~diff
- 00b94cbc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b94cbc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00b94cbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b94cbc bytes b5031ff8
- 00b94ccc ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b94ccc bytes 60010054
- 00b94cdc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b94cdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b94cdc bytes e81700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa3180a5dd2db351ffdd2aae71df41b3"></a>

### [`00b95068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95068.md) → [`00c11ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c11ab0.md) _ZNSt6__ndk19__num_putIcE23__widen_and_group_floatEPcS2_S2_S2_RS2_S3_RKNS_6localeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be15f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15f0.md) · 呼出先 7件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c5e1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1e0.md) · 呼出先 7件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.12% / 新版 87.12%

CFGの説明率　旧版 52.00% / 新版 44.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b950b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b950d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b950dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b95098",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b950b0",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b950b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c11ae0",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c11af8",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c11af8",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b950b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95068.md#insn-00b950b0) · [`00b950c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95068.md#insn-00b950c0) · [`00b950d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95068.md#insn-00b950d0)

~~~diff
- 00b950b0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b950b0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00b950b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b950b0 bytes b6031ff8
- 00b950c0 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b950c0 bytes 60010054
- 00b950d0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b950d0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b950d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b950d0 bytes a8831df8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f64d3a210a2ab3adf32824c0cc2805e"></a>

### [`00b95660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95660.md) → [`00c120a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c120a8.md) _ZNSt6__ndk19__num_putIwE21__widen_and_group_intEPcS2_S2_PwRS3_S4_RKNS_6localeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1600.md) · 呼出先 4件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5e1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1f0.md) · 呼出先 4件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.96% / 新版 77.96%

CFGの説明率　旧版 36.67% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b956a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b956c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b956d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b95690",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b956a8",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b956a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c120d8",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c120f0",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c120f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b956a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95660.md#insn-00b956a8) · [`00b956b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95660.md#insn-00b956b8) · [`00b956c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95660.md#insn-00b956c8)

~~~diff
- 00b956a8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b956a8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00b956a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b956a8 bytes b6031ff8
- 00b956b8 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b956b8 bytes 60010054
- 00b956c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b956c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b956c8 bytes e81700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38c87f948192647674445f9752a10dd5"></a>

### [`00b95a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95a5c.md) → [`00c124a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c124a4.md) _ZNSt6__ndk19__num_putIwE23__widen_and_group_floatEPcS2_S2_PwRS3_S4_RKNS_6localeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1610.md) · 呼出先 7件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c5e200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e200.md) · 呼出先 7件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.63% / 新版 78.63%

CFGの説明率　旧版 52.48% / 新版 39.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 3件, `store_destination` 1件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95aa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95ac4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95ad0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b95a8c",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b95aa4",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b95aa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c124d4",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c124ec",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c124ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b95aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95a5c.md#insn-00b95aa4) · [`00b95ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95a5c.md#insn-00b95ab4) · [`00b95ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b95/00b95a5c.md#insn-00b95ac4)

~~~diff
- 00b95aa4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b95aa4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00b95aa4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b95aa4 bytes b6031ff8
- 00b95ab4 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b95ab4 bytes 60010054
- 00b95ac4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b95ac4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b95ac4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b95ac4 bytes a8831df8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d542a505e3d69a3da8469d73f642d11"></a>

### [`00b96054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96054.md) → [`00c12a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c12a9c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE3getES4_S4_RNS_8ios_baseERjP2tmPKcSC_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd920.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5a370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a370.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.41% / 新版 75.41%

CFGの説明率　旧版 27.74% / 新版 21.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96064"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96064"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96068"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b96064",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b96068",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9606c",
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
      "00c12aac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c12ab0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c12ab4",
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

- 旧版 [`00b96064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96054.md#insn-00b96064) · [`00b96068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96054.md#insn-00b96068) · [`00b9606c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96054.md#insn-00b9606c)

~~~diff
- 00b96064 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b96064 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b96064 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b96064 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b96064 bytes fa6704a9
- 00b96068 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b96068 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b96068 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b96068 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b96068 bytes f85f05a9
- 00b9606c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b9606c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b9606c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b9606c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9606c bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

