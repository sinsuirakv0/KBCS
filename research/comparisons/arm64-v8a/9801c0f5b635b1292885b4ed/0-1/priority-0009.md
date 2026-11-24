# v15.7.4 → v16.0.0 · 最優先の変更候補 (9)

[一覧の目次](README.md)

<a id="compare-69ffe9741282a12e6ce14b5e85cb2bac"></a>

### [`004a9ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9ad4.md) → [`004cc96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc96c.md) _ZN5Botan4HMAC8add_dataEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58240.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cc9fc",
      "value": [
        "leaf",
        "ram:c58240:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a9b64",
      "value": [
        "leaf",
        "ram:bdb7f0:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cca20",
      "incomplete_value": true,
      "site": "004cca2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9b88",
      "incomplete_value": true,
      "site": "004a9b94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
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
      "definition_site": "004cca1c",
      "incomplete_value": false,
      "site": "004cca2c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a9b84",
      "incomplete_value": false,
      "site": "004a9b94",
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
      "004cc9fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb7f0"
      ]
    ],
    [
      "004cca1c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004cca20",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004cc9fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58240"
      ]
    ],
    [
      "004cca1c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004cca20",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a9b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9ad4.md#insn-004a9b64) · [`004a9b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9ad4.md#insn-004a9b94) · [`004a9b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9ad4.md#insn-004a9b3c)
- 新版 [`004cc9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc96c.md#insn-004cc9fc) · [`004cca2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc96c.md#insn-004cca2c) · [`004cc9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc96c.md#insn-004cc9d4)

~~~diff
- 004a9b64 ["INT_ADD", "register:40f0:8", ["const:4a9b64:8", "const:4:8"]]
- 004a9b64 ["CALL", null, ["ram:bdb7f0:8"]]
+ 004cc9fc ["INT_ADD", "register:40f0:8", ["const:4cc9fc:8", "const:4:8"]]
+ 004cc9fc ["CALL", null, ["ram:c58240:8"]]
- 004a9b64 bytes 23c71c94
+ 004cc9fc bytes 112e1e94
- 004a9b94 ["INT_ADD", "register:40f0:8", ["const:4a9b94:8", "const:4:8"]]
- 004a9b94 ["CALL", null, ["callee:00c57b10:8"]]
+ 004cca2c ["INT_ADD", "register:40f0:8", ["const:4cca2c:8", "const:4:8"]]
+ 004cca2c ["CALL", null, ["callee:00c57b10:8"]]
- 004a9b94 bytes 4bc51c94
+ 004cca2c bytes 392c1e94
- 004a9b3c ["INT_ADD", "register:40f0:8", ["const:4a9b3c:8", "const:4:8"]]
- 004a9b3c ["CALL", null, ["callee:00c57af0:8"]]
+ 004cc9d4 ["INT_ADD", "register:40f0:8", ["const:4cc9d4:8", "const:4:8"]]
+ 004cc9d4 ["CALL", null, ["callee:00c57af0:8"]]
- 004a9b3c bytes 59c51c94
+ 004cc9d4 bytes 472c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e1ab072556c4af9329a5fa99c873673"></a>

### [`004a9be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9be8.md) → [`004cca80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cca80.md) _ZN5Botan4HMAC12final_resultEPh

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58240.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ccb80",
      "value": [
        "leaf",
        "ram:c58240:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a9ce8",
      "value": [
        "leaf",
        "ram:bdb7f0:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ccba0",
      "incomplete_value": true,
      "site": "004ccbac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9d08",
      "incomplete_value": true,
      "site": "004a9d14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
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
      "definition_site": "004ccb9c",
      "incomplete_value": false,
      "site": "004ccbac",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a9d04",
      "incomplete_value": false,
      "site": "004a9d14",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ccb80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb7f0"
      ]
    ],
    [
      "004ccb9c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004ccba0",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ccb80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58240"
      ]
    ],
    [
      "004ccb9c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ccba0",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a9ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9be8.md#insn-004a9ce8) · [`004a9d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9be8.md#insn-004a9d14) · [`004a9c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9be8.md#insn-004a9c28)
- 新版 [`004ccb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cca80.md#insn-004ccb80) · [`004ccbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cca80.md#insn-004ccbac) · [`004ccac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cca80.md#insn-004ccac0)

~~~diff
- 004a9ce8 ["INT_ADD", "register:40f0:8", ["const:4a9ce8:8", "const:4:8"]]
- 004a9ce8 ["CALL", null, ["ram:bdb7f0:8"]]
+ 004ccb80 ["INT_ADD", "register:40f0:8", ["const:4ccb80:8", "const:4:8"]]
+ 004ccb80 ["CALL", null, ["ram:c58240:8"]]
- 004a9ce8 bytes c2c61c94
+ 004ccb80 bytes b02d1e94
- 004a9d14 ["INT_ADD", "register:40f0:8", ["const:4a9d14:8", "const:4:8"]]
- 004a9d14 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ccbac ["INT_ADD", "register:40f0:8", ["const:4ccbac:8", "const:4:8"]]
+ 004ccbac ["CALL", null, ["callee:00c57b10:8"]]
- 004a9d14 bytes ebc41c94
+ 004ccbac bytes d92b1e94
- 004a9c28 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a9c28 ["INT_ADD", "register:40f0:8", ["const:4a9c28:8", "const:4:8"]]
- 004a9c28 ["CALLIND", null, ["register:0:8"]]
+ 004ccac0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ccac0 ["INT_ADD", "register:40f0:8", ["const:4ccac0:8", "const:4:8"]]
+ 004ccac0 ["CALLIND", null, ["register:0:8"]]
- 004a9c28 bytes 00013fd6
+ 004ccac0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4416dd444ad9f692724ccb8d91a92b4"></a>

### [`004aa2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa2ec.md) → [`004cd184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd184.md) _ZNK5Botan4HMAC4nameEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc340.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00c58d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d90.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cd1bc",
      "incomplete_value": false,
      "site": "004cd1c8",
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
            "const:8ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa324",
      "incomplete_value": false,
      "site": "004aa330",
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
            "const:833:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cd1e8",
      "incomplete_value": false,
      "site": "004cd1f0",
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
            "const:265:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa350",
      "incomplete_value": false,
      "site": "004aa358",
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
            "const:284:8"
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
      "004cd1bc",
      "PARAM",
      [
        "storage",
        "002ac833",
        null,
        "string"
      ]
    ],
    [
      "004cd1e8",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004cd1bc",
      "PARAM",
      [
        "storage",
        "002bd8ab",
        null,
        "string"
      ]
    ],
    [
      "004cd1e8",
      "PARAM",
      [
        "storage",
        "002ab265",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aa330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa2ec.md#insn-004aa330) · [`004aa358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa2ec.md#insn-004aa358) · [`004aa31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa2ec.md#insn-004aa31c)
- 新版 [`004cd1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd184.md#insn-004cd1c8) · [`004cd1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd184.md#insn-004cd1f0) · [`004cd1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd184.md#insn-004cd1b4)

~~~diff
- 004aa330 ["INT_ADD", "register:40f0:8", ["const:4aa330:8", "const:4:8"]]
- 004aa330 ["CALL", null, ["callee:00c57b60:8"]]
+ 004cd1c8 ["INT_ADD", "register:40f0:8", ["const:4cd1c8:8", "const:4:8"]]
+ 004cd1c8 ["CALL", null, ["callee:00c57b60:8"]]
- 004aa330 bytes 78c31c94
+ 004cd1c8 bytes 662a1e94
- 004aa358 ["INT_ADD", "register:40f0:8", ["const:4aa358:8", "const:4:8"]]
- 004aa358 ["CALL", null, ["callee:00c57b70:8"]]
+ 004cd1f0 ["INT_ADD", "register:40f0:8", ["const:4cd1f0:8", "const:4:8"]]
+ 004cd1f0 ["CALL", null, ["callee:00c57b70:8"]]
- 004aa358 bytes 72c31c94
+ 004cd1f0 bytes 602a1e94
- 004aa31c ["COPY", "register:0:8", ["register:4048:8"]]
- 004aa31c ["INT_ADD", "register:40f0:8", ["const:4aa31c:8", "const:4:8"]]
- 004aa31c ["CALLIND", null, ["register:0:8"]]
+ 004cd1b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cd1b4 ["INT_ADD", "register:40f0:8", ["const:4cd1b4:8", "const:4:8"]]
+ 004cd1b4 ["CALLIND", null, ["register:0:8"]]
- 004aa31c bytes 20013fd6
+ 004cd1b4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33acd7d1e6cd67ffb2abc853c52e2348"></a>

### [`004aa404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa404.md) → [`004cd29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd29c.md) _ZNK5Botan4HMAC5cloneEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdc350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc350.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58da0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

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
      "site": "004cd2d4",
      "value": [
        "leaf",
        "ram:c58da0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004aa43c",
      "value": [
        "leaf",
        "ram:bdc350:8"
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
      "004cd2d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc350"
      ]
    ]
  ],
  "added": [
    [
      "004cd2d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58da0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aa43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa404.md#insn-004aa43c) · [`004aa418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa404.md#insn-004aa418) · [`004aa430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa404.md#insn-004aa430)
- 新版 [`004cd2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd29c.md#insn-004cd2d4) · [`004cd2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd29c.md#insn-004cd2b0) · [`004cd2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd29c.md#insn-004cd2c8)

~~~diff
- 004aa43c ["INT_ADD", "register:40f0:8", ["const:4aa43c:8", "const:4:8"]]
- 004aa43c ["CALL", null, ["ram:bdc350:8"]]
+ 004cd2d4 ["INT_ADD", "register:40f0:8", ["const:4cd2d4:8", "const:4:8"]]
+ 004cd2d4 ["CALL", null, ["ram:c58da0:8"]]
- 004aa43c bytes c5c71c94
+ 004cd2d4 bytes b32e1e94
- 004aa418 ["INT_ADD", "register:40f0:8", ["const:4aa418:8", "const:4:8"]]
- 004aa418 ["CALL", null, ["callee:00c57a90:8"]]
+ 004cd2b0 ["INT_ADD", "register:40f0:8", ["const:4cd2b0:8", "const:4:8"]]
+ 004cd2b0 ["CALL", null, ["callee:00c57a90:8"]]
- 004aa418 bytes 0ac31c94
+ 004cd2b0 bytes f8291e94
- 004aa430 ["COPY", "register:0:8", ["register:4048:8"]]
- 004aa430 ["INT_ADD", "register:40f0:8", ["const:4aa430:8", "const:4:8"]]
- 004aa430 ["CALLIND", null, ["register:0:8"]]
+ 004cd2c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cd2c8 ["INT_ADD", "register:40f0:8", ["const:4cd2c8:8", "const:4:8"]]
+ 004cd2c8 ["CALLIND", null, ["register:0:8"]]
- 004aa430 bytes 20013fd6
+ 004cd2c8 bytes 20013fd6
~~~


<a id="compare-659793f1a29b2ff676734d104c44fb6f"></a>

### [`004aa464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa464.md) → [`004cd2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd2fc.md) _ZN5Botan4HMACC2EPNS_12HashFunctionE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc350.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`00c58da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58da0.md) · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cd33c",
      "incomplete_value": true,
      "site": "004cd33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004aa4a4",
      "incomplete_value": true,
      "site": "004aa4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004cd33c",
      "incomplete_value": true,
      "site": "004cd33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa4a4",
      "incomplete_value": true,
      "site": "004aa4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:98:8"
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
      "definition_site": "004cd3b4",
      "incomplete_value": false,
      "site": "004cd3c0",
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
            "const:214:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa51c",
      "incomplete_value": false,
      "site": "004aa528",
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
            "const:571:8"
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
      "004cd320",
      "READ",
      [
        "storage",
        "00c1b170",
        null,
        "pointer"
      ]
    ],
    [
      "004cd33c",
      "DATA",
      [
        "storage",
        "00be9c50",
        null,
        "undefined1[200]"
      ]
    ],
    [
      "004cd33c",
      "DATA",
      [
        "storage",
        "00be9cd8",
        null,
        "undefined1[200]"
      ]
    ]
  ],
  "added": [
    [
      "004cd320",
      "READ",
      [
        "storage",
        "00c9ab60",
        null,
        "pointer"
      ]
    ],
    [
      "004cd33c",
      "DATA",
      [
        "storage",
        "00c66810",
        null,
        "undefined1[200]"
      ]
    ],
    [
      "004cd33c",
      "DATA",
      [
        "storage",
        "00c66898",
        null,
        "undefined1[200]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aa528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa464.md#insn-004aa528) · [`004aa57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa464.md#insn-004aa57c) · [`004aa480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa464.md#insn-004aa480)
- 新版 [`004cd3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd2fc.md#insn-004cd3c0) · [`004cd414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd2fc.md#insn-004cd414) · [`004cd318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd2fc.md#insn-004cd318)

~~~diff
- 004aa528 ["INT_ADD", "register:40f0:8", ["const:4aa528:8", "const:4:8"]]
- 004aa528 ["CALL", null, ["callee:00c57b60:8"]]
+ 004cd3c0 ["INT_ADD", "register:40f0:8", ["const:4cd3c0:8", "const:4:8"]]
+ 004cd3c0 ["CALL", null, ["callee:00c57b60:8"]]
- 004aa528 bytes fac21c94
+ 004cd3c0 bytes e8291e94
- 004aa57c ["INT_ADD", "register:40f0:8", ["const:4aa57c:8", "const:4:8"]]
- 004aa57c ["CALL", null, ["callee:00c57b10:8"]]
+ 004cd414 ["INT_ADD", "register:40f0:8", ["const:4cd414:8", "const:4:8"]]
+ 004cd414 ["CALL", null, ["callee:00c57b10:8"]]
- 004aa57c bytes d1c21c94
+ 004cd414 bytes bf291e94
- 004aa480 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004cd318 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004aa480 bytes 883b00b0
+ 004cd318 bytes 683e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53ee94b79571c6f8dc1d51005c596fbf"></a>

### [`004aa79c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa79c.md) → [`004cd634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd634.md) _ZN5Botan3KDF15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

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
      "definition_site": "004cd6ac",
      "incomplete_value": false,
      "site": "004cd6b4",
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
            "const:ed4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa814",
      "incomplete_value": false,
      "site": "004aa81c",
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
            "const:7c4:8"
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
      "definition_site": "004cd6ec",
      "incomplete_value": true,
      "site": "004cd6f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004aa854",
      "incomplete_value": true,
      "site": "004aa860",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cd6e8",
      "incomplete_value": false,
      "site": "004cd6f8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004aa850",
      "incomplete_value": false,
      "site": "004aa860",
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
      "004cd6ac",
      "PARAM",
      [
        "storage",
        "002927c4",
        null,
        null
      ]
    ],
    [
      "004cd6e8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004cd6ec",
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
      "004cd6ac",
      "PARAM",
      [
        "storage",
        "002a1ed4",
        null,
        null
      ]
    ],
    [
      "004cd6e8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004cd6ec",
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

- 旧版 [`004aa81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa79c.md#insn-004aa81c) · [`004aa860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa79c.md#insn-004aa860) · [`004aa7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa79c.md#insn-004aa7d0)
- 新版 [`004cd6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd634.md#insn-004cd6b4) · [`004cd6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd634.md#insn-004cd6f8) · [`004cd668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd634.md#insn-004cd668)

~~~diff
- 004aa81c ["INT_ADD", "register:40f0:8", ["const:4aa81c:8", "const:4:8"]]
- 004aa81c ["CALL", null, ["callee:0043dd98:8"]]
+ 004cd6b4 ["INT_ADD", "register:40f0:8", ["const:4cd6b4:8", "const:4:8"]]
+ 004cd6b4 ["CALL", null, ["callee:0043dd98:8"]]
- 004aa81c bytes 9fc2fd97
+ 004cd6b4 bytes b9c1fd97
- 004aa860 ["INT_ADD", "register:40f0:8", ["const:4aa860:8", "const:4:8"]]
- 004aa860 ["CALL", null, ["callee:00c57b10:8"]]
+ 004cd6f8 ["INT_ADD", "register:40f0:8", ["const:4cd6f8:8", "const:4:8"]]
+ 004cd6f8 ["CALL", null, ["callee:00c57b10:8"]]
- 004aa860 bytes 18c21c94
+ 004cd6f8 bytes 06291e94
- 004aa7d0 ["INT_ADD", "register:40f0:8", ["const:4aa7d0:8", "const:4:8"]]
- 004aa7d0 ["CALL", null, ["callee:00c58db0:8"]]
+ 004cd668 ["INT_ADD", "register:40f0:8", ["const:4cd668:8", "const:4:8"]]
+ 004cd668 ["CALL", null, ["callee:00c58db0:8"]]
- 004aa7d0 bytes e4c61c94
+ 004cd668 bytes d22d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6123c248a153f98e4cc88a2039b5e90d"></a>

### [`004aab0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aab0c.md) → [`004cd9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd9a4.md) _ZN5Botan7get_kdfERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc370.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58dc0.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.21% / 新版 99.21%

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
      "definition_site": "004cdb8c",
      "incomplete_value": true,
      "site": "004cdb94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aacf4",
      "incomplete_value": true,
      "site": "004aacfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
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
      "definition_site": "004cdb88",
      "incomplete_value": false,
      "site": "004cdb94",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004aacf0",
      "incomplete_value": false,
      "site": "004aacfc",
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
      "004cdb88",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004cdb8c",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004cdb8c",
      "PARAM",
      [
        "storage",
        "00be9a58",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004cdb88",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004cdb8c",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      "004cdb8c",
      "PARAM",
      [
        "storage",
        "00c66618",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aacfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aab0c.md#insn-004aacfc) · [`004aab54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aab0c.md#insn-004aab54) · [`004aab60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aab0c.md#insn-004aab60)
- 新版 [`004cdb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd9a4.md#insn-004cdb94) · [`004cd9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd9a4.md#insn-004cd9ec) · [`004cd9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd9a4.md#insn-004cd9f8)

~~~diff
- 004aacfc ["INT_ADD", "register:40f0:8", ["const:4aacfc:8", "const:4:8"]]
- 004aacfc ["CALL", null, ["callee:00c57b10:8"]]
+ 004cdb94 ["INT_ADD", "register:40f0:8", ["const:4cdb94:8", "const:4:8"]]
+ 004cdb94 ["CALL", null, ["callee:00c57b10:8"]]
- 004aacfc bytes f1c01c94
+ 004cdb94 bytes df271e94
- 004aab54 ["INT_ADD", "register:40f0:8", ["const:4aab54:8", "const:4:8"]]
- 004aab54 ["CALL", null, ["callee:0043bae0:8"]]
+ 004cd9ec ["INT_ADD", "register:40f0:8", ["const:4cd9ec:8", "const:4:8"]]
+ 004cd9ec ["CALL", null, ["callee:0043bae0:8"]]
- 004aab54 bytes 23b9fd97
+ 004cd9ec bytes 3db8fd97
- 004aab60 ["INT_ADD", "register:40f0:8", ["const:4aab60:8", "const:4:8"]]
- 004aab60 ["CALL", null, ["callee:00c58940:8"]]
+ 004cd9f8 ["INT_ADD", "register:40f0:8", ["const:4cd9f8:8", "const:4:8"]]
+ 004cd9f8 ["CALL", null, ["callee:00c58940:8"]]
- 004aab60 bytes e4c41c94
+ 004cd9f8 bytes d22b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4e0acb021125d51e01a38315dbf49d7"></a>

### [`004aad54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aad54.md) → [`004cdbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cdbec.md) _ZN5Botan7KeyPair28encryption_consistency_checkERNS_21RandomNumberGeneratorERKNS_11Private_KeyERKNS_10Public_KeyERKNSt6__ndk112basic_stringI

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cdc38",
      "value": [
        "leaf",
        "ram:c58dd0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004aada0",
      "value": [
        "leaf",
        "ram:bdc380:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cdd58",
      "incomplete_value": true,
      "site": "004cdd58",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004aaec0",
      "incomplete_value": true,
      "site": "004aaec0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cde40",
      "incomplete_value": true,
      "site": "004cde40",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004aafa8",
      "incomplete_value": true,
      "site": "004aafa8",
      "value": [
        "LOAD",
        "8",
        [
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
      "004cdc38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc380"
      ]
    ],
    [
      "004cdd48",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004cde30",
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
      "004cdc38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58dd0"
      ]
    ],
    [
      "004cdd48",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004cde30",
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

- 旧版 [`004aada0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aad54.md#insn-004aada0) · [`004aaec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aad54.md#insn-004aaec0) · [`004aafa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aad54.md#insn-004aafa8)
- 新版 [`004cdc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cdbec.md#insn-004cdc38) · [`004cdd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cdbec.md#insn-004cdd58) · [`004cde40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cdbec.md#insn-004cde40)

~~~diff
- 004aada0 ["INT_ADD", "register:40f0:8", ["const:4aada0:8", "const:4:8"]]
- 004aada0 ["CALL", null, ["ram:bdc380:8"]]
+ 004cdc38 ["INT_ADD", "register:40f0:8", ["const:4cdc38:8", "const:4:8"]]
+ 004cdc38 ["CALL", null, ["ram:c58dd0:8"]]
- 004aada0 bytes 78c51c94
+ 004cdc38 bytes 662c1e94
- 004aaec0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004aaec0 ["INT_ADD", "register:40f0:8", ["const:4aaec0:8", "const:4:8"]]
- 004aaec0 ["CALLIND", null, ["register:0:8"]]
+ 004cdd58 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cdd58 ["INT_ADD", "register:40f0:8", ["const:4cdd58:8", "const:4:8"]]
+ 004cdd58 ["CALLIND", null, ["register:0:8"]]
- 004aaec0 bytes 20013fd6
+ 004cdd58 bytes 20013fd6
- 004aafa8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004aafa8 ["INT_ADD", "register:40f0:8", ["const:4aafa8:8", "const:4:8"]]
- 004aafa8 ["CALLIND", null, ["register:0:8"]]
+ 004cde40 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cde40 ["INT_ADD", "register:40f0:8", ["const:4cde40:8", "const:4:8"]]
+ 004cde40 ["CALLIND", null, ["register:0:8"]]
- 004aafa8 bytes 20013fd6
+ 004cde40 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d771a0ba161ad86204718365a520b838"></a>

### [`004ab19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab19c.md) → [`004ce034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce034.md) _ZN5Botan7KeyPair27signature_consistency_checkERNS_21RandomNumberGeneratorERKNS_11Private_KeyERKNS_10Public_KeyERKNSt6__ndk112basic_stringIc

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3d0.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3e0.md) [`00bdc3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc3f0.md)
- 新版 呼出元 1件 [`00c58e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e20.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e30.md) [`00c58e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e40.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.06% / 新版 99.06%

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
      "site": "004ce1a0",
      "value": [
        "leaf",
        "ram:c58e70:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ab308",
      "value": [
        "leaf",
        "ram:bdc420:8"
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
      "004ce1a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc420"
      ]
    ]
  ],
  "added": [
    [
      "004ce1a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58e70"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ab308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab19c.md#insn-004ab308) · [`004ab1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab19c.md#insn-004ab1e0) · [`004ab1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab19c.md#insn-004ab1f0)
- 新版 [`004ce1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce034.md#insn-004ce1a0) · [`004ce078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce034.md#insn-004ce078) · [`004ce088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce034.md#insn-004ce088)

~~~diff
- 004ab308 ["INT_ADD", "register:40f0:8", ["const:4ab308:8", "const:4:8"]]
- 004ab308 ["CALL", null, ["ram:bdc420:8"]]
+ 004ce1a0 ["INT_ADD", "register:40f0:8", ["const:4ce1a0:8", "const:4:8"]]
+ 004ce1a0 ["CALL", null, ["ram:c58e70:8"]]
- 004ab308 bytes 46c41c94
+ 004ce1a0 bytes 342b1e94
- 004ab1e0 ["INT_ADD", "register:40f0:8", ["const:4ab1e0:8", "const:4:8"]]
- 004ab1e0 ["CALL", null, ["callee:00c58e30:8"]]
+ 004ce078 ["INT_ADD", "register:40f0:8", ["const:4ce078:8", "const:4:8"]]
+ 004ce078 ["CALL", null, ["callee:00c58e30:8"]]
- 004ab1e0 bytes 80c41c94
+ 004ce078 bytes 6e2b1e94
- 004ab1f0 ["INT_ADD", "register:40f0:8", ["const:4ab1f0:8", "const:4:8"]]
- 004ab1f0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004ce088 ["INT_ADD", "register:40f0:8", ["const:4ce088:8", "const:4:8"]]
+ 004ce088 ["CALL", null, ["callee:00c57ab0:8"]]
- 004ab1f0 bytes 9cbf1c94
+ 004ce088 bytes 8a261e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d25c4eebe3f8237b54843f667166773e"></a>

### [`004ab3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab3f4.md) → [`004ce28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce28c.md) _ZN5Botan25MessageAuthenticationCode6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc040.md) · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd40.md)
- 新版 呼出元 1件 [`00c58a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a90.md) · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58790.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.30% / 新版 99.30%

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
      "site": "004ce3d8",
      "value": [
        "leaf",
        "ram:c58da0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ab540",
      "value": [
        "leaf",
        "ram:bdc350:8"
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
      "004ce3d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc350"
      ]
    ]
  ],
  "added": [
    [
      "004ce3d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58da0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ab540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab3f4.md#insn-004ab540) · [`004ab440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab3f4.md#insn-004ab440) · [`004ab44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab3f4.md#insn-004ab44c)
- 新版 [`004ce3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce28c.md#insn-004ce3d8) · [`004ce2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce28c.md#insn-004ce2d8) · [`004ce2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce28c.md#insn-004ce2e4)

~~~diff
- 004ab540 ["INT_ADD", "register:40f0:8", ["const:4ab540:8", "const:4:8"]]
- 004ab540 ["CALL", null, ["ram:bdc350:8"]]
+ 004ce3d8 ["INT_ADD", "register:40f0:8", ["const:4ce3d8:8", "const:4:8"]]
+ 004ce3d8 ["CALL", null, ["ram:c58da0:8"]]
- 004ab540 bytes 84c31c94
+ 004ce3d8 bytes 722a1e94
- 004ab440 ["INT_ADD", "register:40f0:8", ["const:4ab440:8", "const:4:8"]]
- 004ab440 ["CALL", null, ["callee:0043bae0:8"]]
+ 004ce2d8 ["INT_ADD", "register:40f0:8", ["const:4ce2d8:8", "const:4:8"]]
+ 004ce2d8 ["CALL", null, ["callee:0043bae0:8"]]
- 004ab440 bytes e8b6fd97
+ 004ce2d8 bytes 02b6fd97
- 004ab44c ["INT_ADD", "register:40f0:8", ["const:4ab44c:8", "const:4:8"]]
- 004ab44c ["CALL", null, ["callee:00c58940:8"]]
+ 004ce2e4 ["INT_ADD", "register:40f0:8", ["const:4ce2e4:8", "const:4:8"]]
+ 004ce2e4 ["CALL", null, ["callee:00c58940:8"]]
- 004ab44c bytes a9c21c94
+ 004ce2e4 bytes 97291e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-869f099bda397950f0d9ff791b853f09"></a>

### [`004ababc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ababc.md) → [`004ce954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce954.md) _ZNK5Botan3MD510copy_stateEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005132d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/005132d4.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "004ce988",
      "incomplete_value": true,
      "site": "004ce98c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004abaf0",
      "incomplete_value": true,
      "site": "004abaf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004ce9b4",
      "incomplete_value": true,
      "site": "004ce9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004abb1c",
      "incomplete_value": true,
      "site": "004abb24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "004ce97c",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004ce98c",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004ce9a4",
      "READ",
      [
        "storage",
        "00c1b168",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ce97c",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004ce98c",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004ce9a4",
      "READ",
      [
        "storage",
        "00c9ab58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004abad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ababc.md#insn-004abad8) · [`004abadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ababc.md#insn-004abadc) · [`004abae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ababc.md#insn-004abae4)
- 新版 [`004ce970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce954.md#insn-004ce970) · [`004ce974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce954.md#insn-004ce974) · [`004ce97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce954.md#insn-004ce97c)

~~~diff
- 004abad8 ["INT_ADD", "register:40f0:8", ["const:4abad8:8", "const:4:8"]]
- 004abad8 ["CALL", null, ["callee:00c57a90:8"]]
+ 004ce970 ["INT_ADD", "register:40f0:8", ["const:4ce970:8", "const:4:8"]]
+ 004ce970 ["CALL", null, ["callee:00c57a90:8"]]
- 004abad8 bytes 5abd1c94
+ 004ce970 bytes 48241e94
- 004abadc ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004ce974 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004abadc bytes 883b0090
+ 004ce974 bytes 683e0090
- 004abae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
- 004abae4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ce97c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
+ 004ce97c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004abae4 bytes 08a540f9
+ 004ce97c bytes 089d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d662a8977a25ec7559b170781a6d9e96"></a>

### [`004ac61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac61c.md) → [`004cf4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf4b4.md) _ZN5Botan3MD55clearEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

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
      "definition_site": "004cf4fc",
      "incomplete_value": true,
      "site": "004cf500",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ac664",
      "incomplete_value": true,
      "site": "004ac668",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d30:8"
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
      "004cf4fc",
      "READ",
      [
        "storage",
        "002b0d30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004cf4fc",
      "READ",
      [
        "storage",
        "002c2330",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ac640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac61c.md#insn-004ac640) · [`004ac658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac61c.md#insn-004ac658) · [`004ac65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac61c.md#insn-004ac65c)
- 新版 [`004cf4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf4b4.md#insn-004cf4d8) · [`004cf4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf4b4.md#insn-004cf4f0) · [`004cf4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf4b4.md#insn-004cf4f4)

~~~diff
- 004ac640 ["INT_ADD", "register:40f0:8", ["const:4ac640:8", "const:4:8"]]
- 004ac640 ["CALL", null, ["callee:00c57c90:8"]]
+ 004cf4d8 ["INT_ADD", "register:40f0:8", ["const:4cf4d8:8", "const:4:8"]]
+ 004cf4d8 ["CALL", null, ["callee:00c57c90:8"]]
- 004ac640 bytes 00bb1c94
+ 004cf4d8 bytes ee211e94
- 004ac658 ["INT_ADD", "register:40f0:8", ["const:4ac658:8", "const:4:8"]]
- 004ac658 ["CALL", null, ["callee:00c57c90:8"]]
+ 004cf4f0 ["INT_ADD", "register:40f0:8", ["const:4cf4f0:8", "const:4:8"]]
+ 004cf4f0 ["CALL", null, ["callee:00c57c90:8"]]
- 004ac658 bytes faba1c94
+ 004cf4f0 bytes e8211e94
- 004ac65c ["COPY", "register:4040:8", ["const:2b0000:8"]]
+ 004cf4f4 ["COPY", "register:4040:8", ["const:2c2000:8"]]
- 004ac65c bytes 28f0ff90
+ 004cf4f4 bytes 88effff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08ee6b400767cbea9eb9bca7be3526b0"></a>

### [`004ac6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac6b0.md) → [`004cf548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf548.md) _ZN5Botan16MDx_HashFunctionC2Embbm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cf574",
      "incomplete_value": true,
      "site": "004cf574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004ac6dc",
      "incomplete_value": true,
      "site": "004ac6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004cf564",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004cf574",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "004cf564",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004cf574",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ac6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac6b0.md#insn-004ac6c0) · [`004ac6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac6b0.md#insn-004ac6cc) · [`004ac6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac6b0.md#insn-004ac6e0)
- 新版 [`004cf558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf548.md#insn-004cf558) · [`004cf564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf548.md#insn-004cf564) · [`004cf578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf548.md#insn-004cf578)

~~~diff
- 004ac6c0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004cf558 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004ac6c0 bytes 683b00f0
+ 004cf558 bytes 483e00f0
- 004ac6cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
- 004ac6cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cf564 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
+ 004cf564 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ac6cc bytes 08a540f9
+ 004cf564 bytes 089d45f9
- 004ac6e0 ["INT_ADD", "register:40f0:8", ["const:4ac6e0:8", "const:4:8"]]
- 004ac6e0 ["CALL", null, ["callee:004b34c8:8"]]
+ 004cf578 ["INT_ADD", "register:40f0:8", ["const:4cf578:8", "const:4:8"]]
+ 004cf578 ["CALL", null, ["callee:004b34c8:8"]]
- 004ac6e0 bytes d48fff97
+ 004cf578 bytes d48fff97
~~~


<a id="compare-ca4d144b13c6f8c25aaf77bc48ad5d66"></a>

### [`004ac930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac930.md) → [`004cf7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf7c8.md) _ZN5Botan16MDx_HashFunction11write_countEPh

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.29% / 新版 95.29%

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
      "definition_site": "004cf878",
      "incomplete_value": false,
      "site": "004cf880",
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
            "const:fdd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ac9e0",
      "incomplete_value": false,
      "site": "004ac9e8",
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
            "const:9c4:8"
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
      "definition_site": "004cf8b0",
      "incomplete_value": true,
      "site": "004cf8bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004aca18",
      "incomplete_value": true,
      "site": "004aca24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cf8ac",
      "incomplete_value": false,
      "site": "004cf8bc",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004aca14",
      "incomplete_value": false,
      "site": "004aca24",
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
      "004cf878",
      "PARAM",
      [
        "storage",
        "002919c4",
        null,
        "string"
      ]
    ],
    [
      "004cf8ac",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004cf8b0",
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
      "004cf878",
      "PARAM",
      [
        "storage",
        "002a0fdd",
        null,
        "string"
      ]
    ],
    [
      "004cf8ac",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004cf8b0",
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

- 旧版 [`004ac9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac930.md#insn-004ac9e8) · [`004aca24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac930.md#insn-004aca24) · [`004aca44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac930.md#insn-004aca44)
- 新版 [`004cf880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf7c8.md#insn-004cf880) · [`004cf8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf7c8.md#insn-004cf8bc) · [`004cf8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf7c8.md#insn-004cf8dc)

~~~diff
- 004ac9e8 ["INT_ADD", "register:40f0:8", ["const:4ac9e8:8", "const:4:8"]]
- 004ac9e8 ["CALL", null, ["callee:0043dd98:8"]]
+ 004cf880 ["INT_ADD", "register:40f0:8", ["const:4cf880:8", "const:4:8"]]
+ 004cf880 ["CALL", null, ["callee:0043dd98:8"]]
- 004ac9e8 bytes 2cbafd97
+ 004cf880 bytes 46b9fd97
- 004aca24 ["INT_ADD", "register:40f0:8", ["const:4aca24:8", "const:4:8"]]
- 004aca24 ["CALL", null, ["callee:00c57b10:8"]]
+ 004cf8bc ["INT_ADD", "register:40f0:8", ["const:4cf8bc:8", "const:4:8"]]
+ 004cf8bc ["CALL", null, ["callee:00c57b10:8"]]
- 004aca24 bytes a7b91c94
+ 004cf8bc bytes 95201e94
- 004aca44 ["INT_ADD", "register:40f0:8", ["const:4aca44:8", "const:4:8"]]
- 004aca44 ["CALL", null, ["callee:0043dd98:8"]]
+ 004cf8dc ["INT_ADD", "register:40f0:8", ["const:4cf8dc:8", "const:4:8"]]
+ 004cf8dc ["CALL", null, ["callee:0043dd98:8"]]
- 004aca44 bytes 15bafd97
+ 004cf8dc bytes 2fb9fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7c4df1e12bfbbc052faae61aad763af"></a>

### [`004acad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acad0.md) → [`004cf968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf968.md) _ZN5Botan9mgf1_maskERNS_12HashFunctionEPKhmPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfb0.md) · 呼出先 4件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00c58a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a00.md) · 呼出先 4件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cfb3c",
      "incomplete_value": true,
      "site": "004cfb3c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004acca4",
      "incomplete_value": true,
      "site": "004acca4",
      "value": [
        "LOAD",
        "8",
        [
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
      "004cfb2c",
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
      "004cfb2c",
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

- 旧版 [`004acca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acad0.md#insn-004acca4) · [`004acb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acad0.md#insn-004acb18) · [`004acb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acad0.md#insn-004acb24)
- 新版 [`004cfb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf968.md#insn-004cfb3c) · [`004cf9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf968.md#insn-004cf9b0) · [`004cf9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf968.md#insn-004cf9bc)

~~~diff
- 004acca4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004acca4 ["INT_ADD", "register:40f0:8", ["const:4acca4:8", "const:4:8"]]
- 004acca4 ["CALLIND", null, ["register:0:8"]]
+ 004cfb3c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cfb3c ["INT_ADD", "register:40f0:8", ["const:4cfb3c:8", "const:4:8"]]
+ 004cfb3c ["CALLIND", null, ["register:0:8"]]
- 004acca4 bytes 20013fd6
+ 004cfb3c bytes 20013fd6
- 004acb18 ["COPY", "register:40d8:8", ["const:bea000:8"]]
+ 004cf9b0 ["COPY", "register:40d8:8", ["const:c67000:8"]]
- 004acb18 bytes fb3900d0
+ 004cf9b0 bytes db3c0090
- 004acb24 ["INT_ADD", "register:40f0:8", ["const:4acb24:8", "const:4:8"]]
- 004acb24 ["CALL", null, ["callee:00c58260:8"]]
+ 004cf9bc ["INT_ADD", "register:40f0:8", ["const:4cf9bc:8", "const:4:8"]]
+ 004cf9bc ["CALL", null, ["callee:00c58260:8"]]
- 004acb24 bytes 3bbb1c94
+ 004cf9bc bytes 29221e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98dd1e61cec7cd9fdf87eaf4a657ef4c"></a>

### [`004ae010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004ae010.md) → [`004d0ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0ea8.md) _ZN5Botan8split_onERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEc

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc440.md) · 呼出先 4件 [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c98.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc160.md)
- 新版 呼出元 1件 [`00c58e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e90.md) · 呼出先 4件 [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bb0.md)

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
      "definition_site": "004d0ecc",
      "incomplete_value": false,
      "site": "004d0ed0",
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
      "definition_site": "004ae034",
      "incomplete_value": false,
      "site": "004ae038",
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
      "004d0ed0",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004d0f08",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      "004d0f08",
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
      "004d0ed0",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004d0f08",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004d0f08",
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

- 旧版 [`004ae030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004ae010.md#insn-004ae030) · [`004ae034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004ae010.md#insn-004ae034) · [`004ae048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004ae010.md#insn-004ae048)
- 新版 [`004d0ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0ea8.md#insn-004d0ec8) · [`004d0ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0ea8.md#insn-004d0ecc) · [`004d0ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0ea8.md#insn-004d0ee0)

~~~diff
- 004ae030 ["COPY", "register:4048:8", ["const:bed000:8"]]
+ 004d0ec8 ["COPY", "register:4048:8", ["const:c6a000:8"]]
- 004ae030 bytes e93900f0
+ 004d0ec8 bytes c93c00d0
- 004ae034 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 004ae034 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ae034 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ae034 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004d0ecc ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 004d0ecc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004d0ecc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004d0ecc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ae034 bytes 29c11b91
+ 004d0ecc bytes 29c10a91
- 004ae048 ["INT_ADD", "register:40f0:8", ["const:4ae048:8", "const:4:8"]]
- 004ae048 ["CALL", null, ["callee:00c58bb0:8"]]
+ 004d0ee0 ["INT_ADD", "register:40f0:8", ["const:4d0ee0:8", "const:4:8"]]
+ 004d0ee0 ["CALL", null, ["callee:00c58bb0:8"]]
- 004ae048 bytes 46b81c94
+ 004d0ee0 bytes 341f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ece1a022caaf35997446acab610c4fa"></a>

### [`004ae0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004ae0e8.md) → [`004d0f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0f80.md) _ZN5Botan20parse_algorithm_nameERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc170.md) · 呼出先 17件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md)
- 新版 呼出元 1件 [`00c58bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bc0.md) · 呼出先 17件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.70% / 新版 99.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d187c",
      "incomplete_value": true,
      "site": "004d1884",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ae9e4",
      "incomplete_value": true,
      "site": "004ae9ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d1878",
      "incomplete_value": false,
      "site": "004d1884",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004ae9e0",
      "incomplete_value": false,
      "site": "004ae9ec",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 36,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d195c",
      "incomplete_value": true,
      "site": "004d1964",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aeac4",
      "incomplete_value": true,
      "site": "004aeacc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a0:8"
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
      "004d1878",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004d187c",
      "READ",
      [
        "storage",
        "00c1b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "004d187c",
      "PARAM",
      [
        "storage",
        "00bea780",
        "_ZTIN5Botan22Invalid_Algorithm_NameE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004d1878",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004d187c",
      "READ",
      [
        "storage",
        "00c9ab90",
        null,
        "pointer"
      ]
    ],
    [
      "004d187c",
      "PARAM",
      [
        "storage",
        "00c67340",
        "_ZTIN5Botan22Invalid_Algorithm_NameE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ae9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004ae0e8.md#insn-004ae9ec) · [`004aeacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004ae0e8.md#insn-004aeacc) · [`004ae124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004ae0e8.md#insn-004ae124)
- 新版 [`004d1884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0f80.md#insn-004d1884) · [`004d1964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0f80.md#insn-004d1964) · [`004d0fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0f80.md#insn-004d0fbc)

~~~diff
- 004ae9ec ["INT_ADD", "register:40f0:8", ["const:4ae9ec:8", "const:4:8"]]
- 004ae9ec ["CALL", null, ["callee:00c57b10:8"]]
+ 004d1884 ["INT_ADD", "register:40f0:8", ["const:4d1884:8", "const:4:8"]]
+ 004d1884 ["CALL", null, ["callee:00c57b10:8"]]
- 004ae9ec bytes b5b11c94
+ 004d1884 bytes a3181e94
- 004aeacc ["INT_ADD", "register:40f0:8", ["const:4aeacc:8", "const:4:8"]]
- 004aeacc ["CALL", null, ["callee:00c57b10:8"]]
+ 004d1964 ["INT_ADD", "register:40f0:8", ["const:4d1964:8", "const:4:8"]]
+ 004d1964 ["CALL", null, ["callee:00c57b10:8"]]
- 004aeacc bytes 7db11c94
+ 004d1964 bytes 6b181e94
- 004ae124 ["INT_ADD", "register:40f0:8", ["const:4ae124:8", "const:4:8"]]
- 004ae124 ["CALL", null, ["callee:00c581d0:8"]]
+ 004d0fbc ["INT_ADD", "register:40f0:8", ["const:4d0fbc:8", "const:4:8"]]
+ 004d0fbc ["CALL", null, ["callee:00c581d0:8"]]
- 004ae124 bytes 97b51c94
+ 004d0fbc bytes 851c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fd40def84c57049b6e936ff4edc091f"></a>

### [`004b3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3cec.md) → [`004d6b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md) FUN_004d6b84

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`004950f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) [`00495e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495e3c.md) [`004b44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) [`004b4a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md) [`004b87c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b87c8.md) · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 5件 [`004b7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) [`004b8cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md) [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) [`004db660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md) · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d6cb0",
      "incomplete_value": false,
      "site": "004d6cd0",
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
      "definition_site": "004b3e18",
      "incomplete_value": false,
      "site": "004b3e38",
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
      "definition_site": "004d6cb8",
      "incomplete_value": false,
      "site": "004d6cd0",
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
      "definition_site": "004b3e20",
      "incomplete_value": false,
      "site": "004b3e38",
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
      "definition_site": "004d6cc0",
      "incomplete_value": false,
      "site": "004d6cd0",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3e28",
      "incomplete_value": false,
      "site": "004b3e38",
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
            "const:da2:8"
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
      "004d6cb0",
      "PARAM",
      [
        "storage",
        "002969cf",
        null,
        "string"
      ]
    ],
    [
      "004d6cb8",
      "PARAM",
      [
        "storage",
        "002a563f",
        null,
        "string"
      ]
    ],
    [
      "004d6cc0",
      "PARAM",
      [
        "storage",
        "00298da2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d6cb0",
      "PARAM",
      [
        "storage",
        "002a6504",
        null,
        "string"
      ]
    ],
    [
      "004d6cb8",
      "PARAM",
      [
        "storage",
        "002b606d",
        null,
        "string"
      ]
    ],
    [
      "004d6cc0",
      "PARAM",
      [
        "storage",
        "002a8b60",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b3e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3cec.md#insn-004b3e38) · [`004b3e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3cec.md#insn-004b3e14) · [`004b3e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3cec.md#insn-004b3e18)
- 新版 [`004d6cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md#insn-004d6cd0) · [`004d6cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md#insn-004d6cac) · [`004d6cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md#insn-004d6cb0)

~~~diff
- 004b3e38 ["INT_ADD", "register:40f0:8", ["const:4b3e38:8", "const:4:8"]]
- 004b3e38 ["CALL", null, ["callee:00c58250:8"]]
+ 004d6cd0 ["INT_ADD", "register:40f0:8", ["const:4d6cd0:8", "const:4:8"]]
+ 004d6cd0 ["CALL", null, ["callee:00c58250:8"]]
- 004b3e38 bytes 729e1c94
+ 004d6cd0 bytes 60051e94
- 004b3e14 ["COPY", "register:4000:8", ["const:296000:8"]]
+ 004d6cac ["COPY", "register:4000:8", ["const:2a6000:8"]]
- 004b3e14 bytes 00effff0
+ 004d6cac bytes 80eeff90
- 004b3e18 ["COPY", "tmp:0:8", ["const:9cf:8"]]
- 004b3e18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004b3e18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004b3e18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d6cb0 ["COPY", "tmp:0:8", ["const:504:8"]]
+ 004d6cb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d6cb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d6cb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004b3e18 bytes 003c2791
+ 004d6cb0 bytes 00101491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27295d6644695a972ef885c99a77bef0"></a>

### [`004b47ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b47ec.md) → [`004d7684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md) FUN_004d7684

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004b868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b868c.md) [`004bd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd550.md) · 呼出先 9件 [`004aef94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004aef94.md) [`004af240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af240.md) [`004af83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af83c.md) [`004b02e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b0/004b02e0.md) [`004b105c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b1/004b105c.md)
- 新版 呼出元 2件 [`004db524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db524.md) [`004e03e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md) · 呼出先 9件 [`004d1e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1e2c.md) [`004d20d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d20d8.md) [`004d26d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d26d4.md) [`004d3178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d3/004d3178.md) [`004d3ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d3/004d3ef4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.46% / 新版 96.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d7824",
      "incomplete_value": false,
      "site": "004d7844",
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
            "const:477:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b498c",
      "incomplete_value": false,
      "site": "004b49ac",
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
            "const:a3e:8"
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
      "definition_site": "004d782c",
      "incomplete_value": false,
      "site": "004d7844",
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
            "const:b6f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b4994",
      "incomplete_value": false,
      "site": "004b49ac",
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
            "const:db1:8"
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
      "definition_site": "004d7834",
      "incomplete_value": false,
      "site": "004d7844",
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
            "const:22e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b499c",
      "incomplete_value": false,
      "site": "004b49ac",
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
            "const:58b:8"
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
      "004d7824",
      "PARAM",
      [
        "storage",
        "00295a3e",
        null,
        "string"
      ]
    ],
    [
      "004d782c",
      "PARAM",
      [
        "storage",
        "00298db1",
        null,
        "string"
      ]
    ],
    [
      "004d7834",
      "PARAM",
      [
        "storage",
        "002a958b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d7824",
      "PARAM",
      [
        "storage",
        "002a5477",
        null,
        "string"
      ]
    ],
    [
      "004d782c",
      "PARAM",
      [
        "storage",
        "002a8b6f",
        null,
        "string"
      ]
    ],
    [
      "004d7834",
      "PARAM",
      [
        "storage",
        "002ba22e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b49ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b47ec.md#insn-004b49ac) · [`004b492c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b47ec.md#insn-004b492c) · [`004b4988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b47ec.md#insn-004b4988)
- 新版 [`004d7844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md#insn-004d7844) · [`004d77c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md#insn-004d77c4) · [`004d7820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md#insn-004d7820)

~~~diff
- 004b49ac ["INT_ADD", "register:40f0:8", ["const:4b49ac:8", "const:4:8"]]
- 004b49ac ["CALL", null, ["callee:00c58250:8"]]
+ 004d7844 ["INT_ADD", "register:40f0:8", ["const:4d7844:8", "const:4:8"]]
+ 004d7844 ["CALL", null, ["callee:00c58250:8"]]
- 004b49ac bytes 959b1c94
+ 004d7844 bytes 83021e94
- 004b492c ["INT_ADD", "register:40f0:8", ["const:4b492c:8", "const:4:8"]]
- 004b492c ["CALL", null, ["callee:004d7848:8"]]
+ 004d77c4 ["INT_ADD", "register:40f0:8", ["const:4d77c4:8", "const:4:8"]]
+ 004d77c4 ["CALL", null, ["callee:004d7848:8"]]
- 004b492c bytes 21000094
+ 004d77c4 bytes 21000094
- 004b4988 ["COPY", "register:4000:8", ["const:295000:8"]]
+ 004d7820 ["COPY", "register:4000:8", ["const:2a5000:8"]]
- 004b4988 bytes 00efffb0
+ 004d7820 bytes 60eeffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc385b9ac04566489953c5e25f06453a"></a>

### [`004b5004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5004.md) → [`004d7e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7e9c.md) _ZN5Botan19generate_dsa_primesERNS_21RandomNumberGeneratorERNS_6BigIntES3_mmRKNSt6__ndk16vectorIhNS4_9allocatorIhEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc460.md) · 呼出先 25件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 1件 [`00c58eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58eb0.md) · 呼出先 25件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d7f2c",
      "incomplete_value": false,
      "site": "004d7f38",
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
            "const:7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5094",
      "incomplete_value": false,
      "site": "004b50a0",
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
            "const:64e:8"
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
      "definition_site": "004d7f58",
      "incomplete_value": false,
      "site": "004d7f60",
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
      "definition_site": "004b50c0",
      "incomplete_value": false,
      "site": "004b50c8",
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
      "definition_site": "004d7f9c",
      "incomplete_value": false,
      "site": "004d7fa4",
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
            "const:162:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5104",
      "incomplete_value": false,
      "site": "004b510c",
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
            "const:5f3:8"
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
      "004d7f2c",
      "PARAM",
      [
        "storage",
        "002a564e",
        null,
        "string"
      ]
    ],
    [
      "004d7f58",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ],
    [
      "004d7f9c",
      "PARAM",
      [
        "storage",
        "002a75f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d7f2c",
      "PARAM",
      [
        "storage",
        "002b607c",
        null,
        "string"
      ]
    ],
    [
      "004d7f58",
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ],
    [
      "004d7f9c",
      "PARAM",
      [
        "storage",
        "002b8162",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b50a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5004.md#insn-004b50a0) · [`004b50c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5004.md#insn-004b50c8) · [`004b510c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5004.md#insn-004b510c)
- 新版 [`004d7f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7e9c.md#insn-004d7f38) · [`004d7f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7e9c.md#insn-004d7f60) · [`004d7fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7e9c.md#insn-004d7fa4)

~~~diff
- 004b50a0 ["INT_ADD", "register:40f0:8", ["const:4b50a0:8", "const:4:8"]]
- 004b50a0 ["CALL", null, ["callee:00c57b60:8"]]
+ 004d7f38 ["INT_ADD", "register:40f0:8", ["const:4d7f38:8", "const:4:8"]]
+ 004d7f38 ["CALL", null, ["callee:00c57b60:8"]]
- 004b50a0 bytes 1c981c94
+ 004d7f38 bytes 0aff1d94
- 004b50c8 ["INT_ADD", "register:40f0:8", ["const:4b50c8:8", "const:4:8"]]
- 004b50c8 ["CALL", null, ["callee:00c57b70:8"]]
+ 004d7f60 ["INT_ADD", "register:40f0:8", ["const:4d7f60:8", "const:4:8"]]
+ 004d7f60 ["CALL", null, ["callee:00c57b70:8"]]
- 004b50c8 bytes 16981c94
+ 004d7f60 bytes 04ff1d94
- 004b510c ["INT_ADD", "register:40f0:8", ["const:4b510c:8", "const:4:8"]]
- 004b510c ["CALL", null, ["callee:00c57b70:8"]]
+ 004d7fa4 ["INT_ADD", "register:40f0:8", ["const:4d7fa4:8", "const:4:8"]]
+ 004d7fa4 ["CALL", null, ["callee:00c57b70:8"]]
- 004b510c bytes 05981c94
+ 004d7fa4 bytes f3fe1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8de0a849338303657664b75bce354136"></a>

### [`004b5c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5c14.md) → [`004d8aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d8/004d8aac.md) _ZN5Botan8is_primeERKNS_6BigIntERNS_21RandomNumberGeneratorEmb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc470.md) · 呼出先 14件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md) [`00bdbe70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe70.md)
- 新版 呼出元 1件 [`00c58ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ec0.md) · 呼出先 14件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md) [`00c588c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588c0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.17% / 新版 96.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 9件

アドレスに依存する影響 `call_target` 10件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d9278",
      "incomplete_value": true,
      "site": "004d9278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004b63e0",
      "incomplete_value": true,
      "site": "004b63e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d8b2c",
      "incomplete_value": true,
      "site": "004d8b2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b5c94",
      "incomplete_value": true,
      "site": "004b5c94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "kind": "call_target",
    "new": {
      "definition_site": "004d8b9c",
      "incomplete_value": true,
      "site": "004d8b9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b5d04",
      "incomplete_value": true,
      "site": "004b5d04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004d8b1c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004d8b8c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004d8bcc",
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
      "004d8b1c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004d8b8c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004d8bcc",
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

- 旧版 [`004b5c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5c14.md#insn-004b5c94) · [`004b5d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5c14.md#insn-004b5d04) · [`004b5d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b5/004b5c14.md#insn-004b5d44)
- 新版 [`004d8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d8/004d8aac.md#insn-004d8b2c) · [`004d8b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d8/004d8aac.md#insn-004d8b9c) · [`004d8bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d8/004d8aac.md#insn-004d8bdc)

~~~diff
- 004b5c94 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b5c94 ["INT_ADD", "register:40f0:8", ["const:4b5c94:8", "const:4:8"]]
- 004b5c94 ["CALLIND", null, ["register:0:8"]]
+ 004d8b2c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d8b2c ["INT_ADD", "register:40f0:8", ["const:4d8b2c:8", "const:4:8"]]
+ 004d8b2c ["CALLIND", null, ["register:0:8"]]
- 004b5c94 bytes 20013fd6
+ 004d8b2c bytes 20013fd6
- 004b5d04 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b5d04 ["INT_ADD", "register:40f0:8", ["const:4b5d04:8", "const:4:8"]]
- 004b5d04 ["CALLIND", null, ["register:0:8"]]
+ 004d8b9c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d8b9c ["INT_ADD", "register:40f0:8", ["const:4d8b9c:8", "const:4:8"]]
+ 004d8b9c ["CALLIND", null, ["register:0:8"]]
- 004b5d04 bytes 20013fd6
+ 004d8b9c bytes 20013fd6
- 004b5d44 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b5d44 ["INT_ADD", "register:40f0:8", ["const:4b5d44:8", "const:4:8"]]
- 004b5d44 ["CALLIND", null, ["register:0:8"]]
+ 004d8bdc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d8bdc ["INT_ADD", "register:40f0:8", ["const:4d8bdc:8", "const:4:8"]]
+ 004d8bdc ["CALLIND", null, ["register:0:8"]]
- 004b5d44 bytes 20013fd6
+ 004d8bdc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-085ced340d6dcf4a54bb8e0286aad5b5"></a>

### [`004b6640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6640.md) → [`004d94d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d94d8.md) _ZN5Botan6jacobiERKNS_6BigIntES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4e0.md) · 呼出先 15件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00496d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f30.md) · 呼出先 15件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.97% / 新版 92.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 10件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d9568",
      "incomplete_value": true,
      "site": "004d9568",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b66d0",
      "incomplete_value": true,
      "site": "004b66d0",
      "value": [
        "LOAD",
        "8",
        [
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
      "site": "004d9580",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b66e8",
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d958c",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b66f4",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
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
      "004d9558",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004d9580",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004d958c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ]
  ],
  "added": [
    [
      "004d9558",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004d9580",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004d958c",
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

- 旧版 [`004b66d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6640.md#insn-004b66d0) · [`004b66e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6640.md#insn-004b66e8) · [`004b66f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6640.md#insn-004b66f4)
- 新版 [`004d9568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d94d8.md#insn-004d9568) · [`004d9580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d94d8.md#insn-004d9580) · [`004d958c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d94d8.md#insn-004d958c)

~~~diff
- 004b66d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b66d0 ["INT_ADD", "register:40f0:8", ["const:4b66d0:8", "const:4:8"]]
- 004b66d0 ["CALLIND", null, ["register:0:8"]]
+ 004d9568 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d9568 ["INT_ADD", "register:40f0:8", ["const:4d9568:8", "const:4:8"]]
+ 004d9568 ["CALLIND", null, ["register:0:8"]]
- 004b66d0 bytes 20013fd6
+ 004d9568 bytes 20013fd6
- 004b66e8 ["INT_ADD", "register:40f0:8", ["const:4b66e8:8", "const:4:8"]]
- 004b66e8 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004d9580 ["INT_ADD", "register:40f0:8", ["const:4d9580:8", "const:4:8"]]
+ 004d9580 ["CALL", null, ["ram:c58740:8"]]
- 004b66e8 bytes 82951c94
+ 004d9580 bytes 70fc1d94
- 004b66f4 ["INT_ADD", "register:40f0:8", ["const:4b66f4:8", "const:4:8"]]
- 004b66f4 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004d958c ["INT_ADD", "register:40f0:8", ["const:4d958c:8", "const:4:8"]]
+ 004d958c ["CALL", null, ["ram:c58740:8"]]
- 004b66f4 bytes 7f951c94
+ 004d958c bytes 6dfc1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81919ff30098db3bb3b7dbe6b38d470a"></a>

### [`004b6d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6d50.md) → [`004d9be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d9be8.md) _ZN5Botan12random_primeERNS_21RandomNumberGeneratorEmRKNS_6BigIntEmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4f0.md) · 呼出先 21件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004b76d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b76d8.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c58f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f40.md) · 呼出先 21件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004da570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da570.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.71% / 新版 94.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 9件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d9c74",
      "incomplete_value": true,
      "site": "004d9c74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b6ddc",
      "incomplete_value": true,
      "site": "004b6ddc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004d9e1c",
      "value": [
        "leaf",
        "ram:c58f50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b6f84",
      "value": [
        "leaf",
        "ram:bdc500:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d9f30",
      "incomplete_value": true,
      "site": "004d9f30",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40e0:8"
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
      "definition_site": "004b7098",
      "incomplete_value": true,
      "site": "004b7098",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40e0:8"
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
      "004d9c64",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004d9ddc",
      "READ",
      [
        "storage",
        "00c1b1b8",
        null,
        "pointer"
      ]
    ],
    [
      "004d9e1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc500"
      ]
    ]
  ],
  "added": [
    [
      "004d9c64",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004d9ddc",
      "READ",
      [
        "storage",
        "00c9aba8",
        null,
        "pointer"
      ]
    ],
    [
      "004d9e1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58f50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b6ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6d50.md#insn-004b6ddc) · [`004b6f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6d50.md#insn-004b6f84) · [`004b7098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6d50.md#insn-004b7098)
- 新版 [`004d9c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d9be8.md#insn-004d9c74) · [`004d9e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d9be8.md#insn-004d9e1c) · [`004d9f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d9be8.md#insn-004d9f30)

~~~diff
- 004b6ddc ["COPY", "register:0:8", ["register:4048:8"]]
- 004b6ddc ["INT_ADD", "register:40f0:8", ["const:4b6ddc:8", "const:4:8"]]
- 004b6ddc ["CALLIND", null, ["register:0:8"]]
+ 004d9c74 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d9c74 ["INT_ADD", "register:40f0:8", ["const:4d9c74:8", "const:4:8"]]
+ 004d9c74 ["CALLIND", null, ["register:0:8"]]
- 004b6ddc bytes 20013fd6
+ 004d9c74 bytes 20013fd6
- 004b6f84 ["INT_ADD", "register:40f0:8", ["const:4b6f84:8", "const:4:8"]]
- 004b6f84 ["CALL", null, ["ram:bdc500:8"]]
+ 004d9e1c ["INT_ADD", "register:40f0:8", ["const:4d9e1c:8", "const:4:8"]]
+ 004d9e1c ["CALL", null, ["ram:c58f50:8"]]
- 004b6f84 bytes 5f951c94
+ 004d9e1c bytes 4dfc1d94
- 004b7098 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b7098 ["INT_ADD", "register:40f0:8", ["const:4b7098:8", "const:4:8"]]
- 004b7098 ["CALLIND", null, ["register:0:8"]]
+ 004d9f30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d9f30 ["INT_ADD", "register:40f0:8", ["const:4d9f30:8", "const:4:8"]]
+ 004d9f30 ["CALLIND", null, ["register:0:8"]]
- 004b7098 bytes 20013fd6
+ 004d9f30 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40e32b62815120b3b72e38fda0bffef0"></a>

### [`004b76d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b76d8.md) → [`004da570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da570.md) FUN_004da570

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004b6d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6d50.md) · 呼出先 7件 [`00521f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521f70.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`004d9be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d9be8.md) · 呼出先 7件 [`00544e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544e08.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
      "site": "004da624",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b778c",
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
      "definition_site": "004da634",
      "incomplete_value": true,
      "site": "004da63c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b779c",
      "incomplete_value": true,
      "site": "004b77a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004da638",
      "incomplete_value": true,
      "site": "004da63c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b77a0",
      "incomplete_value": true,
      "site": "004b77a4",
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
      "004da624",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "004da634",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004da634",
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
      "004da624",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "004da634",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004da634",
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

- 旧版 [`004b778c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b76d8.md#insn-004b778c) · [`004b77a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b76d8.md#insn-004b77a4) · [`004b7720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b76d8.md#insn-004b7720)
- 新版 [`004da624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da570.md#insn-004da624) · [`004da63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da570.md#insn-004da63c) · [`004da5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da570.md#insn-004da5b8)

~~~diff
- 004b778c ["INT_ADD", "register:40f0:8", ["const:4b778c:8", "const:4:8"]]
- 004b778c ["CALL", null, ["ram:bdbbf0:8"]]
+ 004da624 ["INT_ADD", "register:40f0:8", ["const:4da624:8", "const:4:8"]]
+ 004da624 ["CALL", null, ["ram:c58640:8"]]
- 004b778c bytes 19911c94
+ 004da624 bytes 07f81d94
- 004b77a4 ["INT_ADD", "register:40f0:8", ["const:4b77a4:8", "const:4:8"]]
- 004b77a4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004da63c ["INT_ADD", "register:40f0:8", ["const:4da63c:8", "const:4:8"]]
+ 004da63c ["CALL", null, ["callee:00c57b10:8"]]
- 004b77a4 bytes 478e1c94
+ 004da63c bytes 35f51d94
- 004b7720 ["INT_ADD", "register:40f0:8", ["const:4b7720:8", "const:4:8"]]
- 004b7720 ["CALL", null, ["callee:00c58630:8"]]
+ 004da5b8 ["INT_ADD", "register:40f0:8", ["const:4da5b8:8", "const:4:8"]]
+ 004da5b8 ["CALL", null, ["callee:00c58630:8"]]
- 004b7720 bytes 30911c94
+ 004da5b8 bytes 1ef81d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d5aaa333b9458950f5ce5f0daa7acfa"></a>

### [`004b77d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b77d0.md) → [`004da668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da668.md) _ZN5Botan3gcdERKNS_6BigIntES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc510.md) · 呼出先 9件 [`00496d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md)
- 新版 呼出元 1件 [`00c58f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f60.md) · 呼出先 9件 [`004b9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.05% / 新版 98.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004da7bc",
      "incomplete_value": true,
      "site": "004da7bc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b7924",
      "incomplete_value": true,
      "site": "004b7924",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004da7e8",
      "incomplete_value": true,
      "site": "004da7e8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b7950",
      "incomplete_value": true,
      "site": "004b7950",
      "value": [
        "LOAD",
        "8",
        [
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004da814",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b797c",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
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
      "004da7ac",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004da7d8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004da814",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ]
  ],
  "added": [
    [
      "004da7ac",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004da7d8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004da814",
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

- 旧版 [`004b7924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b77d0.md#insn-004b7924) · [`004b7950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b77d0.md#insn-004b7950) · [`004b797c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b77d0.md#insn-004b797c)
- 新版 [`004da7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da668.md#insn-004da7bc) · [`004da7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da668.md#insn-004da7e8) · [`004da814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da668.md#insn-004da814)

~~~diff
- 004b7924 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b7924 ["INT_ADD", "register:40f0:8", ["const:4b7924:8", "const:4:8"]]
- 004b7924 ["CALLIND", null, ["register:0:8"]]
+ 004da7bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004da7bc ["INT_ADD", "register:40f0:8", ["const:4da7bc:8", "const:4:8"]]
+ 004da7bc ["CALLIND", null, ["register:0:8"]]
- 004b7924 bytes 20013fd6
+ 004da7bc bytes 20013fd6
- 004b7950 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b7950 ["INT_ADD", "register:40f0:8", ["const:4b7950:8", "const:4:8"]]
- 004b7950 ["CALLIND", null, ["register:0:8"]]
+ 004da7e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004da7e8 ["INT_ADD", "register:40f0:8", ["const:4da7e8:8", "const:4:8"]]
+ 004da7e8 ["CALLIND", null, ["register:0:8"]]
- 004b7950 bytes 20013fd6
+ 004da7e8 bytes 20013fd6
- 004b797c ["INT_ADD", "register:40f0:8", ["const:4b797c:8", "const:4:8"]]
- 004b797c ["CALL", null, ["ram:bdbcf0:8"]]
+ 004da814 ["INT_ADD", "register:40f0:8", ["const:4da814:8", "const:4:8"]]
+ 004da814 ["CALL", null, ["ram:c58740:8"]]
- 004b797c bytes dd901c94
+ 004da814 bytes cbf71d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71de21e44eeef7c689c7051a8f54ae61"></a>

### [`004b8210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8210.md) → [`004db0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db0a8.md) _ZN5Botan17random_safe_primeERNS_21RandomNumberGeneratorEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.64% / 新版 93.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004db158",
      "value": [
        "leaf",
        "ram:c58820:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b82c0",
      "value": [
        "leaf",
        "ram:bdbdd0:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004db268",
      "incomplete_value": true,
      "site": "004db268",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b83d0",
      "incomplete_value": true,
      "site": "004b83d0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004db294",
      "incomplete_value": true,
      "site": "004db294",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b83fc",
      "incomplete_value": true,
      "site": "004b83fc",
      "value": [
        "LOAD",
        "8",
        [
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
      "004db158",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbdd0"
      ]
    ],
    [
      "004db258",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004db284",
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
      "004db158",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58820"
      ]
    ],
    [
      "004db258",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004db284",
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

- 旧版 [`004b82c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8210.md#insn-004b82c0) · [`004b83d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8210.md#insn-004b83d0) · [`004b83fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8210.md#insn-004b83fc)
- 新版 [`004db158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db0a8.md#insn-004db158) · [`004db268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db0a8.md#insn-004db268) · [`004db294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db0a8.md#insn-004db294)

~~~diff
- 004b82c0 ["INT_ADD", "register:40f0:8", ["const:4b82c0:8", "const:4:8"]]
- 004b82c0 ["CALL", null, ["ram:bdbdd0:8"]]
+ 004db158 ["INT_ADD", "register:40f0:8", ["const:4db158:8", "const:4:8"]]
+ 004db158 ["CALL", null, ["ram:c58820:8"]]
- 004b82c0 bytes c48e1c94
+ 004db158 bytes b2f51d94
- 004b83d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b83d0 ["INT_ADD", "register:40f0:8", ["const:4b83d0:8", "const:4:8"]]
- 004b83d0 ["CALLIND", null, ["register:0:8"]]
+ 004db268 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004db268 ["INT_ADD", "register:40f0:8", ["const:4db268:8", "const:4:8"]]
+ 004db268 ["CALLIND", null, ["register:0:8"]]
- 004b83d0 bytes 20013fd6
+ 004db268 bytes 20013fd6
- 004b83fc ["COPY", "register:0:8", ["register:4048:8"]]
- 004b83fc ["INT_ADD", "register:40f0:8", ["const:4b83fc:8", "const:4:8"]]
- 004b83fc ["CALLIND", null, ["register:0:8"]]
+ 004db294 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004db294 ["INT_ADD", "register:40f0:8", ["const:4db294:8", "const:4:8"]]
+ 004db294 ["CALLIND", null, ["register:0:8"]]
- 004b83fc bytes 20013fd6
+ 004db294 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-601442b73d953a56bd4c76a533099b9f"></a>

### [`004b868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b868c.md) → [`004db524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db524.md) _ZN5Botan6squareERKNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4c0.md) · 呼出先 6件 [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`004b47ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b47ec.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdd0.md)
- 新版 呼出元 1件 [`00c58f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f10.md) · 呼出先 6件 [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004d7684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58820.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

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
      "site": "004db594",
      "value": [
        "leaf",
        "ram:c58820:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b86fc",
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
      "definition_site": "004db5f4",
      "incomplete_value": true,
      "site": "004db5f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b875c",
      "incomplete_value": true,
      "site": "004b875c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004db594",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbdd0"
      ]
    ],
    [
      "004db5e4",
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
      "004db594",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58820"
      ]
    ],
    [
      "004db5e4",
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

- 旧版 [`004b86fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b868c.md#insn-004b86fc) · [`004b875c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b868c.md#insn-004b875c) · [`004b8710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b868c.md#insn-004b8710)
- 新版 [`004db594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db524.md#insn-004db594) · [`004db5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db524.md#insn-004db5f4) · [`004db5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db524.md#insn-004db5a8)

~~~diff
- 004b86fc ["INT_ADD", "register:40f0:8", ["const:4b86fc:8", "const:4:8"]]
- 004b86fc ["CALL", null, ["ram:bdbdd0:8"]]
+ 004db594 ["INT_ADD", "register:40f0:8", ["const:4db594:8", "const:4:8"]]
+ 004db594 ["CALL", null, ["ram:c58820:8"]]
- 004b86fc bytes b58d1c94
+ 004db594 bytes a3f41d94
- 004b875c ["COPY", "register:0:8", ["register:4048:8"]]
- 004b875c ["INT_ADD", "register:40f0:8", ["const:4b875c:8", "const:4:8"]]
- 004b875c ["CALLIND", null, ["register:0:8"]]
+ 004db5f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004db5f4 ["INT_ADD", "register:40f0:8", ["const:4db5f4:8", "const:4:8"]]
+ 004db5f4 ["CALLIND", null, ["register:0:8"]]
- 004b875c bytes 20013fd6
+ 004db5f4 bytes 20013fd6
- 004b8710 ["INT_ADD", "register:40f0:8", ["const:4b8710:8", "const:4:8"]]
- 004b8710 ["CALL", null, ["callee:004b8810:8"]]
+ 004db5a8 ["INT_ADD", "register:40f0:8", ["const:4db5a8:8", "const:4:8"]]
+ 004db5a8 ["CALL", null, ["callee:004b8810:8"]]
- 004b8710 bytes 9a74ff97
+ 004db5a8 bytes 9a74ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-579841889cadf945f90b084b96b8bb7c"></a>

### [`004b87c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b87c8.md) → [`004db660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md) _ZN5Botan7mul_addERKNS_6BigIntES2_S2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc520.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`004b3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3cec.md) [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)
- 新版 呼出元 1件 [`00c58f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f70.md) · 呼出先 12件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004d6b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md) [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.05% / 新版 98.05%

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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004db6f8",
      "value": [
        "leaf",
        "ram:c58820:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b8860",
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
      "definition_site": "004db838",
      "incomplete_value": true,
      "site": "004db838",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b89a0",
      "incomplete_value": true,
      "site": "004b89a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004db87c",
      "incomplete_value": false,
      "site": "004db884",
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
            "const:b89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b89e4",
      "incomplete_value": false,
      "site": "004b89ec",
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
            "const:dcb:8"
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
      "004db6f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbdd0"
      ]
    ],
    [
      "004db828",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004db87c",
      "PARAM",
      [
        "storage",
        "00298dcb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004db6f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58820"
      ]
    ],
    [
      "004db828",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004db87c",
      "PARAM",
      [
        "storage",
        "002a8b89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b87c8.md#insn-004b8860) · [`004b89a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b87c8.md#insn-004b89a0) · [`004b89ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b87c8.md#insn-004b89ec)
- 新版 [`004db6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md#insn-004db6f8) · [`004db838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md#insn-004db838) · [`004db884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md#insn-004db884)

~~~diff
- 004b8860 ["INT_ADD", "register:40f0:8", ["const:4b8860:8", "const:4:8"]]
- 004b8860 ["CALL", null, ["ram:bdbdd0:8"]]
+ 004db6f8 ["INT_ADD", "register:40f0:8", ["const:4db6f8:8", "const:4:8"]]
+ 004db6f8 ["CALL", null, ["ram:c58820:8"]]
- 004b8860 bytes 5c8d1c94
+ 004db6f8 bytes 4af41d94
- 004b89a0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b89a0 ["INT_ADD", "register:40f0:8", ["const:4b89a0:8", "const:4:8"]]
- 004b89a0 ["CALLIND", null, ["register:0:8"]]
+ 004db838 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004db838 ["INT_ADD", "register:40f0:8", ["const:4db838:8", "const:4:8"]]
+ 004db838 ["CALLIND", null, ["register:0:8"]]
- 004b89a0 bytes 20013fd6
+ 004db838 bytes 20013fd6
- 004b89ec ["INT_ADD", "register:40f0:8", ["const:4b89ec:8", "const:4:8"]]
- 004b89ec ["CALL", null, ["callee:0043dd98:8"]]
+ 004db884 ["INT_ADD", "register:40f0:8", ["const:4db884:8", "const:4:8"]]
+ 004db884 ["CALL", null, ["callee:0043dd98:8"]]
- 004b89ec bytes 2b8afd97
+ 004db884 bytes 4589fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81bb08717e213ecf3b3e61fbbc44891b"></a>

### [`004b8aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8aa0.md) → [`004db938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db938.md) _ZN5Botan7sub_mulERKNS_6BigIntES2_S2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc530.md) · 呼出先 9件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f80.md) · 呼出先 9件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004db97c",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b8ae4",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004db9cc",
      "incomplete_value": false,
      "site": "004db9d4",
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
            "const:415:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8b34",
      "incomplete_value": false,
      "site": "004b8b3c",
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
            "const:3a7:8"
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
      "definition_site": "004dba04",
      "incomplete_value": true,
      "site": "004dba10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b8b6c",
      "incomplete_value": true,
      "site": "004b8b78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004db97c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004db9cc",
      "PARAM",
      [
        "storage",
        "0029b3a7",
        null,
        "string"
      ]
    ],
    [
      "004dba00",
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
      "004db97c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004db9cc",
      "PARAM",
      [
        "storage",
        "002ab415",
        null,
        "string"
      ]
    ],
    [
      "004dba00",
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

- 旧版 [`004b8ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8aa0.md#insn-004b8ae4) · [`004b8b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8aa0.md#insn-004b8b3c) · [`004b8b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8aa0.md#insn-004b8b78)
- 新版 [`004db97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db938.md#insn-004db97c) · [`004db9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db938.md#insn-004db9d4) · [`004dba10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db938.md#insn-004dba10)

~~~diff
- 004b8ae4 ["INT_ADD", "register:40f0:8", ["const:4b8ae4:8", "const:4:8"]]
- 004b8ae4 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004db97c ["INT_ADD", "register:40f0:8", ["const:4db97c:8", "const:4:8"]]
+ 004db97c ["CALL", null, ["ram:c58740:8"]]
- 004b8ae4 bytes 838c1c94
+ 004db97c bytes 71f31d94
- 004b8b3c ["INT_ADD", "register:40f0:8", ["const:4b8b3c:8", "const:4:8"]]
- 004b8b3c ["CALL", null, ["callee:0043dd98:8"]]
+ 004db9d4 ["INT_ADD", "register:40f0:8", ["const:4db9d4:8", "const:4:8"]]
+ 004db9d4 ["CALL", null, ["callee:0043dd98:8"]]
- 004b8b3c bytes d789fd97
+ 004db9d4 bytes f188fd97
- 004b8b78 ["INT_ADD", "register:40f0:8", ["const:4b8b78:8", "const:4:8"]]
- 004b8b78 ["CALL", null, ["callee:00c57b10:8"]]
+ 004dba10 ["INT_ADD", "register:40f0:8", ["const:4dba10:8", "const:4:8"]]
+ 004dba10 ["CALL", null, ["callee:00c57b10:8"]]
- 004b8b78 bytes 52891c94
+ 004dba10 bytes 40f01d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c48f3efdba056e9e9ce626dceaa25544"></a>

### [`004b8bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8bd8.md) → [`004dba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dba70.md) _ZN5Botan7mul_subERKNS_6BigIntES2_S2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004dbaf4",
      "incomplete_value": false,
      "site": "004dbafc",
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
            "const:8df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8c5c",
      "incomplete_value": false,
      "site": "004b8c64",
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
            "const:867:8"
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
      "definition_site": "004dbb2c",
      "incomplete_value": true,
      "site": "004dbb38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b8c94",
      "incomplete_value": true,
      "site": "004b8ca0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004dbb28",
      "incomplete_value": false,
      "site": "004dbb38",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004b8c90",
      "incomplete_value": false,
      "site": "004b8ca0",
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
      "004dbaf4",
      "PARAM",
      [
        "storage",
        "002ac867",
        null,
        "string"
      ]
    ],
    [
      "004dbb28",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004dbb2c",
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
      "004dbaf4",
      "PARAM",
      [
        "storage",
        "002bd8df",
        null,
        "string"
      ]
    ],
    [
      "004dbb28",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004dbb2c",
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

- 旧版 [`004b8c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8bd8.md#insn-004b8c64) · [`004b8ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8bd8.md#insn-004b8ca0) · [`004b8ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8bd8.md#insn-004b8ca8)
- 新版 [`004dbafc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dba70.md#insn-004dbafc) · [`004dbb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dba70.md#insn-004dbb38) · [`004dbb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dba70.md#insn-004dbb40)

~~~diff
- 004b8c64 ["INT_ADD", "register:40f0:8", ["const:4b8c64:8", "const:4:8"]]
- 004b8c64 ["CALL", null, ["callee:0043dd98:8"]]
+ 004dbafc ["INT_ADD", "register:40f0:8", ["const:4dbafc:8", "const:4:8"]]
+ 004dbafc ["CALL", null, ["callee:0043dd98:8"]]
- 004b8c64 bytes 8d89fd97
+ 004dbafc bytes a788fd97
- 004b8ca0 ["INT_ADD", "register:40f0:8", ["const:4b8ca0:8", "const:4:8"]]
- 004b8ca0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004dbb38 ["INT_ADD", "register:40f0:8", ["const:4dbb38:8", "const:4:8"]]
+ 004dbb38 ["CALL", null, ["callee:00c57b10:8"]]
- 004b8ca0 bytes 08891c94
+ 004dbb38 bytes f6ef1d94
- 004b8ca8 ["INT_ADD", "register:40f0:8", ["const:4b8ca8:8", "const:4:8"]]
- 004b8ca8 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004dbb40 ["INT_ADD", "register:40f0:8", ["const:4dbb40:8", "const:4:8"]]
+ 004dbb40 ["CALL", null, ["ram:c58740:8"]]
- 004b8ca8 bytes 128c1c94
+ 004dbb40 bytes 00f31d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c121b51fe0f33b0771e4292ba3fdc1e"></a>

### [`004b8d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8d44.md) → [`004dbbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbbdc.md) _ZN5Botan3lcmERKNS_6BigIntES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc540.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbe00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe00.md) [`00bdbe40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe40.md) [`00bdc510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc510.md)
- 新版 呼出元 1件 [`00c58f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f90.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58850.md) [`00c58890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58890.md) [`00c58f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f60.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dbc54",
      "incomplete_value": true,
      "site": "004dbc54",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "definition_site": "004b8dbc",
      "incomplete_value": true,
      "site": "004b8dbc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "definition_site": "004dbc80",
      "incomplete_value": true,
      "site": "004dbc80",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "definition_site": "004b8de8",
      "incomplete_value": true,
      "site": "004b8de8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "004dbc44",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004dbc70",
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
      "004dbc44",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004dbc70",
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

- 旧版 [`004b8dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8d44.md#insn-004b8dbc) · [`004b8de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8d44.md#insn-004b8de8) · [`004b8d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8d44.md#insn-004b8d74)
- 新版 [`004dbc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbbdc.md#insn-004dbc54) · [`004dbc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbbdc.md#insn-004dbc80) · [`004dbc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbbdc.md#insn-004dbc0c)

~~~diff
- 004b8dbc ["COPY", "register:0:8", ["register:4048:8"]]
- 004b8dbc ["INT_ADD", "register:40f0:8", ["const:4b8dbc:8", "const:4:8"]]
- 004b8dbc ["CALLIND", null, ["register:0:8"]]
+ 004dbc54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dbc54 ["INT_ADD", "register:40f0:8", ["const:4dbc54:8", "const:4:8"]]
+ 004dbc54 ["CALLIND", null, ["register:0:8"]]
- 004b8dbc bytes 20013fd6
+ 004dbc54 bytes 20013fd6
- 004b8de8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b8de8 ["INT_ADD", "register:40f0:8", ["const:4b8de8:8", "const:4:8"]]
- 004b8de8 ["CALLIND", null, ["register:0:8"]]
+ 004dbc80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dbc80 ["INT_ADD", "register:40f0:8", ["const:4dbc80:8", "const:4:8"]]
+ 004dbc80 ["CALLIND", null, ["register:0:8"]]
- 004b8de8 bytes 20013fd6
+ 004dbc80 bytes 20013fd6
- 004b8d74 ["INT_ADD", "register:40f0:8", ["const:4b8d74:8", "const:4:8"]]
- 004b8d74 ["CALL", null, ["callee:00c58850:8"]]
+ 004dbc0c ["INT_ADD", "register:40f0:8", ["const:4dbc0c:8", "const:4:8"]]
+ 004dbc0c ["CALL", null, ["callee:00c58850:8"]]
- 004b8d74 bytes 238c1c94
+ 004dbc0c bytes 11f31d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44f4f102629b9c043c8db1d778009a42"></a>

### [`004b8e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8e58.md) → [`004dbcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbcf0.md) _ZN5Botan25almost_montgomery_inverseERNS_6BigIntERKS0_S3_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc550.md) · 呼出先 10件 [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc80.md)
- 新版 呼出元 1件 [`00c58fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fa0.md) · 呼出先 10件 [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c586d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004dbd30",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b8e98",
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004dbd3c",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b8ea4",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dbdb0",
      "incomplete_value": true,
      "site": "004dbdb0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b8f18",
      "incomplete_value": true,
      "site": "004b8f18",
      "value": [
        "LOAD",
        "8",
        [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004dbd30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004dbd3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004dbda0",
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
      "004dbd30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004dbd3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004dbda0",
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

- 旧版 [`004b8e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8e58.md#insn-004b8e98) · [`004b8ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8e58.md#insn-004b8ea4) · [`004b8f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b8e58.md#insn-004b8f18)
- 新版 [`004dbd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbcf0.md#insn-004dbd30) · [`004dbd3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbcf0.md#insn-004dbd3c) · [`004dbdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbcf0.md#insn-004dbdb0)

~~~diff
- 004b8e98 ["INT_ADD", "register:40f0:8", ["const:4b8e98:8", "const:4:8"]]
- 004b8e98 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004dbd30 ["INT_ADD", "register:40f0:8", ["const:4dbd30:8", "const:4:8"]]
+ 004dbd30 ["CALL", null, ["ram:c58740:8"]]
- 004b8e98 bytes 968b1c94
+ 004dbd30 bytes 84f21d94
- 004b8ea4 ["INT_ADD", "register:40f0:8", ["const:4b8ea4:8", "const:4:8"]]
- 004b8ea4 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004dbd3c ["INT_ADD", "register:40f0:8", ["const:4dbd3c:8", "const:4:8"]]
+ 004dbd3c ["CALL", null, ["ram:c58740:8"]]
- 004b8ea4 bytes 938b1c94
+ 004dbd3c bytes 81f21d94
- 004b8f18 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b8f18 ["INT_ADD", "register:40f0:8", ["const:4b8f18:8", "const:4:8"]]
- 004b8f18 ["CALLIND", null, ["register:0:8"]]
+ 004dbdb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dbdb0 ["INT_ADD", "register:40f0:8", ["const:4dbdb0:8", "const:4:8"]]
+ 004dbdb0 ["CALLIND", null, ["register:0:8"]]
- 004b8f18 bytes 20013fd6
+ 004dbdb0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f852c8f7e8f3b1286e545859527fa118"></a>

### [`004b9948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b9/004b9948.md) → [`004dc7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc7e0.md) _ZN5Botan26ct_inverse_mod_odd_modulusERKNS_6BigIntES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc560.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048924c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/0048924c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c58fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fb0.md) · 呼出先 16件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004ac0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac0e4.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.97% / 新版 94.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `call_target` 11件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dc890",
      "incomplete_value": true,
      "site": "004dc890",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b99f8",
      "incomplete_value": true,
      "site": "004b99f8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004dc8ec",
      "incomplete_value": true,
      "site": "004dc8ec",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b9a54",
      "incomplete_value": true,
      "site": "004b9a54",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dc918",
      "incomplete_value": true,
      "site": "004dc918",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b9a80",
      "incomplete_value": true,
      "site": "004b9a80",
      "value": [
        "LOAD",
        "8",
        [
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
      "004dc880",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004dc8dc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004dc908",
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
      "004dc880",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004dc8dc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004dc908",
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

- 旧版 [`004b99f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b9/004b9948.md#insn-004b99f8) · [`004b9a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b9/004b9948.md#insn-004b9a54) · [`004b9a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b9/004b9948.md#insn-004b9a80)
- 新版 [`004dc890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc7e0.md#insn-004dc890) · [`004dc8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc7e0.md#insn-004dc8ec) · [`004dc918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc7e0.md#insn-004dc918)

~~~diff
- 004b99f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b99f8 ["INT_ADD", "register:40f0:8", ["const:4b99f8:8", "const:4:8"]]
- 004b99f8 ["CALLIND", null, ["register:0:8"]]
+ 004dc890 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dc890 ["INT_ADD", "register:40f0:8", ["const:4dc890:8", "const:4:8"]]
+ 004dc890 ["CALLIND", null, ["register:0:8"]]
- 004b99f8 bytes 20013fd6
+ 004dc890 bytes 20013fd6
- 004b9a54 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b9a54 ["INT_ADD", "register:40f0:8", ["const:4b9a54:8", "const:4:8"]]
- 004b9a54 ["CALLIND", null, ["register:0:8"]]
+ 004dc8ec ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dc8ec ["INT_ADD", "register:40f0:8", ["const:4dc8ec:8", "const:4:8"]]
+ 004dc8ec ["CALLIND", null, ["register:0:8"]]
- 004b9a54 bytes 20013fd6
+ 004dc8ec bytes 20013fd6
- 004b9a80 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b9a80 ["INT_ADD", "register:40f0:8", ["const:4b9a80:8", "const:4:8"]]
- 004b9a80 ["CALLIND", null, ["register:0:8"]]
+ 004dc918 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dc918 ["INT_ADD", "register:40f0:8", ["const:4dc918:8", "const:4:8"]]
+ 004dc918 ["CALLIND", null, ["register:0:8"]]
- 004b9a80 bytes 20013fd6
+ 004dc918 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-145a8e2156e5c0710de6fd2185284e58"></a>

### [`004ba430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ba/004ba430.md) → [`004dd2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004dd2c8.md) _ZN5Botan11inverse_modERKNS_6BigIntES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc570.md) · 呼出先 15件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00496d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fc0.md) · 呼出先 15件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.91% / 新版 96.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 9件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dd38c",
      "incomplete_value": true,
      "site": "004dd390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004ba4f4",
      "incomplete_value": true,
      "site": "004ba4f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004dd3b0",
      "incomplete_value": true,
      "site": "004dd3b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004ba518",
      "incomplete_value": true,
      "site": "004ba51c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004dd3ac",
      "incomplete_value": false,
      "site": "004dd3b4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004ba514",
      "incomplete_value": false,
      "site": "004ba51c",
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
      "004dd378",
      "READ",
      [
        "storage",
        "00c1b010",
        null,
        "pointer"
      ]
    ],
    [
      "004dd390",
      "DATA",
      [
        "storage",
        "00becca0",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004dd3ac",
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
      "004dd378",
      "READ",
      [
        "storage",
        "00c9aa00",
        null,
        "pointer"
      ]
    ],
    [
      "004dd390",
      "DATA",
      [
        "storage",
        "00c69860",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004dd3ac",
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

- 旧版 [`004ba51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ba/004ba430.md#insn-004ba51c) · [`004ba5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ba/004ba430.md#insn-004ba5e8) · [`004ba5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ba/004ba430.md#insn-004ba5f8)
- 新版 [`004dd3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004dd2c8.md#insn-004dd3b4) · [`004dd480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004dd2c8.md#insn-004dd480) · [`004dd490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004dd2c8.md#insn-004dd490)

~~~diff
- 004ba51c ["INT_ADD", "register:40f0:8", ["const:4ba51c:8", "const:4:8"]]
- 004ba51c ["CALL", null, ["callee:00c57b10:8"]]
+ 004dd3b4 ["INT_ADD", "register:40f0:8", ["const:4dd3b4:8", "const:4:8"]]
+ 004dd3b4 ["CALL", null, ["callee:00c57b10:8"]]
- 004ba51c bytes e9821c94
+ 004dd3b4 bytes d7e91d94
- 004ba5e8 ["INT_ADD", "register:40f0:8", ["const:4ba5e8:8", "const:4:8"]]
- 004ba5e8 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004dd480 ["INT_ADD", "register:40f0:8", ["const:4dd480:8", "const:4:8"]]
+ 004dd480 ["CALL", null, ["ram:c58740:8"]]
- 004ba5e8 bytes c2851c94
+ 004dd480 bytes b0ec1d94
- 004ba5f8 ["INT_ADD", "register:40f0:8", ["const:4ba5f8:8", "const:4:8"]]
- 004ba5f8 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004dd490 ["INT_ADD", "register:40f0:8", ["const:4dd490:8", "const:4:8"]]
+ 004dd490 ["CALL", null, ["ram:c58740:8"]]
- 004ba5f8 bytes be851c94
+ 004dd490 bytes acec1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b01d58c726af23eafbdebc3fc7c8829"></a>

### [`004bb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb030.md) → [`004ddec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004ddec8.md) _ZN5Botan13monty_inverseEj

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc580.md) · 呼出先 8件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00498c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fd0.md) · 呼出先 8件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004bbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.59% / 新版 92.59%

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
      "definition_site": "004ddf84",
      "incomplete_value": false,
      "site": "004ddf8c",
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
            "const:767:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb0ec",
      "incomplete_value": false,
      "site": "004bb0f4",
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
            "const:b0e:8"
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
      "definition_site": "004ddfc0",
      "incomplete_value": true,
      "site": "004ddfcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bb128",
      "incomplete_value": true,
      "site": "004bb134",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ddfbc",
      "incomplete_value": false,
      "site": "004ddfcc",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004bb124",
      "incomplete_value": false,
      "site": "004bb134",
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
      "004ddf84",
      "PARAM",
      [
        "storage",
        "00297b0e",
        null,
        "string"
      ]
    ],
    [
      "004ddfbc",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004ddfc0",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ddf84",
      "PARAM",
      [
        "storage",
        "002a7767",
        null,
        "string"
      ]
    ],
    [
      "004ddfbc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ddfc0",
      "READ",
      [
        "storage",
        "00c9a988",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb030.md#insn-004bb0f4) · [`004bb134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb030.md#insn-004bb134) · [`004bb16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb030.md#insn-004bb16c)
- 新版 [`004ddf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004ddec8.md#insn-004ddf8c) · [`004ddfcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004ddec8.md#insn-004ddfcc) · [`004de004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004ddec8.md#insn-004de004)

~~~diff
- 004bb0f4 ["INT_ADD", "register:40f0:8", ["const:4bb0f4:8", "const:4:8"]]
- 004bb0f4 ["CALL", null, ["callee:0043dd98:8"]]
+ 004ddf8c ["INT_ADD", "register:40f0:8", ["const:4ddf8c:8", "const:4:8"]]
+ 004ddf8c ["CALL", null, ["callee:0043dd98:8"]]
- 004bb0f4 bytes 6980fd97
+ 004ddf8c bytes 837ffd97
- 004bb134 ["INT_ADD", "register:40f0:8", ["const:4bb134:8", "const:4:8"]]
- 004bb134 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ddfcc ["INT_ADD", "register:40f0:8", ["const:4ddfcc:8", "const:4:8"]]
+ 004ddfcc ["CALL", null, ["callee:00c57b10:8"]]
- 004bb134 bytes e37f1c94
+ 004ddfcc bytes d1e61d94
- 004bb16c ["INT_ADD", "register:40f0:8", ["const:4bb16c:8", "const:4:8"]]
- 004bb16c ["CALL", null, ["callee:00c58250:8"]]
+ 004de004 ["INT_ADD", "register:40f0:8", ["const:4de004:8", "const:4:8"]]
+ 004de004 ["CALL", null, ["callee:00c58250:8"]]
- 004bb16c bytes a5811c94
+ 004de004 bytes 93e81d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1421eeb98c57681670d129afde689d27"></a>

### [`004bb1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb1c0.md) → [`004de058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de058.md) _ZN5Botan9power_modERKNS_6BigIntES2_S2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc590.md) · 呼出先 9件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md) [`00bdbe70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe70.md) [`00bdc4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4a0.md)
- 新版 呼出元 1件 [`00c58fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fe0.md) · 呼出先 9件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md) [`00c588c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588c0.md) [`00c58ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ef0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.26% / 新版 98.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004de0dc",
      "incomplete_value": true,
      "site": "004de0dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004bb244",
      "incomplete_value": true,
      "site": "004bb244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "site": "004de09c",
      "value": [
        "leaf",
        "ram:c58ff0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004bb204",
      "value": [
        "leaf",
        "ram:bdc5a0:8"
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
      "site": "004de120",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004bb288",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
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
      "004de09c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc5a0"
      ]
    ],
    [
      "004de0d0",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "004de0dc",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "004de09c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58ff0"
      ]
    ],
    [
      "004de0d0",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "004de0dc",
      "DATA",
      [
        "storage",
        "00c66958",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb1c0.md#insn-004bb204) · [`004bb288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb1c0.md#insn-004bb288) · [`004bb30c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb1c0.md#insn-004bb30c)
- 新版 [`004de09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de058.md#insn-004de09c) · [`004de120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de058.md#insn-004de120) · [`004de1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de058.md#insn-004de1a4)

~~~diff
- 004bb204 ["INT_ADD", "register:40f0:8", ["const:4bb204:8", "const:4:8"]]
- 004bb204 ["CALL", null, ["ram:bdc5a0:8"]]
+ 004de09c ["INT_ADD", "register:40f0:8", ["const:4de09c:8", "const:4:8"]]
+ 004de09c ["CALL", null, ["ram:c58ff0:8"]]
- 004bb204 bytes e7841c94
+ 004de09c bytes d5eb1d94
- 004bb288 ["INT_ADD", "register:40f0:8", ["const:4bb288:8", "const:4:8"]]
- 004bb288 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004de120 ["INT_ADD", "register:40f0:8", ["const:4de120:8", "const:4:8"]]
+ 004de120 ["CALL", null, ["ram:c58740:8"]]
- 004bb288 bytes 9a821c94
+ 004de120 bytes 88e91d94
- 004bb30c ["COPY", "register:0:8", ["register:4048:8"]]
- 004bb30c ["INT_ADD", "register:40f0:8", ["const:4bb30c:8", "const:4:8"]]
- 004bb30c ["CALLIND", null, ["register:0:8"]]
+ 004de1a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004de1a4 ["INT_ADD", "register:40f0:8", ["const:4de1a4:8", "const:4:8"]]
+ 004de1a4 ["CALLIND", null, ["register:0:8"]]
- 004bb30c bytes 20013fd6
+ 004de1a4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dc89ad0c58cc31f36c55d560ec72885"></a>

### [`004bb3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb3f0.md) → [`004de288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de288.md) _ZNK5Botan9Power_Mod8set_baseERKNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4a0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ef0.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.40% / 新版 95.40%

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
      "definition_site": "004de2f8",
      "incomplete_value": false,
      "site": "004de300",
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
            "const:53a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb460",
      "incomplete_value": false,
      "site": "004bb468",
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
            "const:a05:8"
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
      "definition_site": "004de334",
      "incomplete_value": true,
      "site": "004de340",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bb49c",
      "incomplete_value": true,
      "site": "004bb4a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004de330",
      "incomplete_value": false,
      "site": "004de340",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004bb498",
      "incomplete_value": false,
      "site": "004bb4a8",
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
      "004de2f8",
      "PARAM",
      [
        "storage",
        "00296a05",
        null,
        "string"
      ]
    ],
    [
      "004de330",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004de334",
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
      "004de2f8",
      "PARAM",
      [
        "storage",
        "002a653a",
        null,
        "string"
      ]
    ],
    [
      "004de330",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004de334",
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

- 旧版 [`004bb468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb3f0.md#insn-004bb468) · [`004bb4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb3f0.md#insn-004bb4a8) · [`004bb508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb3f0.md#insn-004bb508)
- 新版 [`004de300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de288.md#insn-004de300) · [`004de340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de288.md#insn-004de340) · [`004de3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de288.md#insn-004de3a0)

~~~diff
- 004bb468 ["INT_ADD", "register:40f0:8", ["const:4bb468:8", "const:4:8"]]
- 004bb468 ["CALL", null, ["callee:0043dd98:8"]]
+ 004de300 ["INT_ADD", "register:40f0:8", ["const:4de300:8", "const:4:8"]]
+ 004de300 ["CALL", null, ["callee:0043dd98:8"]]
- 004bb468 bytes 8c7ffd97
+ 004de300 bytes a67efd97
- 004bb4a8 ["INT_ADD", "register:40f0:8", ["const:4bb4a8:8", "const:4:8"]]
- 004bb4a8 ["CALL", null, ["callee:00c57b10:8"]]
+ 004de340 ["INT_ADD", "register:40f0:8", ["const:4de340:8", "const:4:8"]]
+ 004de340 ["CALL", null, ["callee:00c57b10:8"]]
- 004bb4a8 bytes 067f1c94
+ 004de340 bytes f4e51d94
- 004bb508 ["INT_ADD", "register:40f0:8", ["const:4bb508:8", "const:4:8"]]
- 004bb508 ["CALL", null, ["callee:0043dd98:8"]]
+ 004de3a0 ["INT_ADD", "register:40f0:8", ["const:4de3a0:8", "const:4:8"]]
+ 004de3a0 ["CALL", null, ["callee:0043dd98:8"]]
- 004bb508 bytes 647ffd97
+ 004de3a0 bytes 7e7efd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa938a0e698c74bfd80a4706ad8063be"></a>

### [`004bb59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb59c.md) → [`004de434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de434.md) _ZNK5Botan9Power_Mod12set_exponentERKNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5b0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c59000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59000.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "definition_site": "004de4a4",
      "incomplete_value": false,
      "site": "004de4ac",
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
            "const:d45:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb60c",
      "incomplete_value": false,
      "site": "004bb614",
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
            "const:861:8"
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
      "definition_site": "004de4e0",
      "incomplete_value": true,
      "site": "004de4ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bb648",
      "incomplete_value": true,
      "site": "004bb654",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004de4dc",
      "incomplete_value": false,
      "site": "004de4ec",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004bb644",
      "incomplete_value": false,
      "site": "004bb654",
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
      "004de4a4",
      "PARAM",
      [
        "storage",
        "002ae861",
        null,
        "string"
      ]
    ],
    [
      "004de4dc",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004de4e0",
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
      "004de4a4",
      "PARAM",
      [
        "storage",
        "002bfd45",
        null,
        "string"
      ]
    ],
    [
      "004de4dc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004de4e0",
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

- 旧版 [`004bb614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb59c.md#insn-004bb614) · [`004bb654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb59c.md#insn-004bb654) · [`004bb678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb59c.md#insn-004bb678)
- 新版 [`004de4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de434.md#insn-004de4ac) · [`004de4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de434.md#insn-004de4ec) · [`004de510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de434.md#insn-004de510)

~~~diff
- 004bb614 ["INT_ADD", "register:40f0:8", ["const:4bb614:8", "const:4:8"]]
- 004bb614 ["CALL", null, ["callee:0043dd98:8"]]
+ 004de4ac ["INT_ADD", "register:40f0:8", ["const:4de4ac:8", "const:4:8"]]
+ 004de4ac ["CALL", null, ["callee:0043dd98:8"]]
- 004bb614 bytes 217ffd97
+ 004de4ac bytes 3b7efd97
- 004bb654 ["INT_ADD", "register:40f0:8", ["const:4bb654:8", "const:4:8"]]
- 004bb654 ["CALL", null, ["callee:00c57b10:8"]]
+ 004de4ec ["INT_ADD", "register:40f0:8", ["const:4de4ec:8", "const:4:8"]]
+ 004de4ec ["CALL", null, ["callee:00c57b10:8"]]
- 004bb654 bytes 9b7e1c94
+ 004de4ec bytes 89e51d94
- 004bb678 ["INT_ADD", "register:40f0:8", ["const:4bb678:8", "const:4:8"]]
- 004bb678 ["CALL", null, ["callee:0043dd98:8"]]
+ 004de510 ["INT_ADD", "register:40f0:8", ["const:4de510:8", "const:4:8"]]
+ 004de510 ["CALL", null, ["callee:0043dd98:8"]]
- 004bb678 bytes 087ffd97
+ 004de510 bytes 227efd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae55d27aeb413d1b7ddf9dfa84e2749a"></a>

### [`004bb70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb70c.md) → [`004de5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de5a4.md) _ZNK5Botan9Power_Mod7executeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4b0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f00.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
      "definition_site": "004de60c",
      "incomplete_value": false,
      "site": "004de614",
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
            "const:ee2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb774",
      "incomplete_value": false,
      "site": "004bb77c",
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
            "const:7d2:8"
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
      "definition_site": "004de648",
      "incomplete_value": true,
      "site": "004de654",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bb7b0",
      "incomplete_value": true,
      "site": "004bb7bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004de644",
      "incomplete_value": false,
      "site": "004de654",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004bb7ac",
      "incomplete_value": false,
      "site": "004bb7bc",
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
      "004de60c",
      "PARAM",
      [
        "storage",
        "002927d2",
        null,
        "string"
      ]
    ],
    [
      "004de644",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004de648",
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
      "004de60c",
      "PARAM",
      [
        "storage",
        "002a1ee2",
        null,
        "string"
      ]
    ],
    [
      "004de644",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004de648",
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

- 旧版 [`004bb77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb70c.md#insn-004bb77c) · [`004bb7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb70c.md#insn-004bb7bc) · [`004bb768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb70c.md#insn-004bb768)
- 新版 [`004de614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de5a4.md#insn-004de614) · [`004de654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de5a4.md#insn-004de654) · [`004de600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de5a4.md#insn-004de600)

~~~diff
- 004bb77c ["INT_ADD", "register:40f0:8", ["const:4bb77c:8", "const:4:8"]]
- 004bb77c ["CALL", null, ["callee:0043dd98:8"]]
+ 004de614 ["INT_ADD", "register:40f0:8", ["const:4de614:8", "const:4:8"]]
+ 004de614 ["CALL", null, ["callee:0043dd98:8"]]
- 004bb77c bytes c77efd97
+ 004de614 bytes e17dfd97
- 004bb7bc ["INT_ADD", "register:40f0:8", ["const:4bb7bc:8", "const:4:8"]]
- 004bb7bc ["CALL", null, ["callee:00c57b10:8"]]
+ 004de654 ["INT_ADD", "register:40f0:8", ["const:4de654:8", "const:4:8"]]
+ 004de654 ["CALL", null, ["callee:00c57b10:8"]]
- 004bb7bc bytes 417e1c94
+ 004de654 bytes 2fe51d94
- 004bb768 ["INT_ADD", "register:40f0:8", ["const:4bb768:8", "const:4:8"]]
- 004bb768 ["CALL", null, ["callee:00c57af0:8"]]
+ 004de600 ["INT_ADD", "register:40f0:8", ["const:4de600:8", "const:4:8"]]
+ 004de600 ["CALL", null, ["callee:00c57af0:8"]]
- 004bb768 bytes 4e7e1c94
+ 004de600 bytes 3ce51d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fda545a66c73dc0873a565580a182dc"></a>

### [`004bb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md) → [`004de6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md) FUN_004de6a8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0050ffa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050ffa4.md) [`005100e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00510/005100e0.md) [`00514bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00514/00514bd4.md) [`005162fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005162fc.md) [`005163b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00516/005163b4.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 7件 [`00532e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md) [`00532f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md) [`00537a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/00537a6c.md) [`00539194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539194.md) [`0053924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/0053924c.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004de6e0",
      "incomplete_value": true,
      "site": "004de6e0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bb848",
      "incomplete_value": true,
      "site": "004bb848",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004de70c",
      "incomplete_value": true,
      "site": "004de70c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bb874",
      "incomplete_value": true,
      "site": "004bb874",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004de738",
      "incomplete_value": true,
      "site": "004de738",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bb8a0",
      "incomplete_value": true,
      "site": "004bb8a0",
      "value": [
        "LOAD",
        "8",
        [
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
      "004de6d0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004de6fc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004de728",
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
      "004de6d0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004de6fc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004de728",
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

- 旧版 [`004bb848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md#insn-004bb848) · [`004bb874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md#insn-004bb874) · [`004bb8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb810.md#insn-004bb8a0)
- 新版 [`004de6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md#insn-004de6e0) · [`004de70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md#insn-004de70c) · [`004de738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md#insn-004de738)

~~~diff
- 004bb848 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bb848 ["INT_ADD", "register:40f0:8", ["const:4bb848:8", "const:4:8"]]
- 004bb848 ["CALLIND", null, ["register:0:8"]]
+ 004de6e0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004de6e0 ["INT_ADD", "register:40f0:8", ["const:4de6e0:8", "const:4:8"]]
+ 004de6e0 ["CALLIND", null, ["register:0:8"]]
- 004bb848 bytes 20013fd6
+ 004de6e0 bytes 20013fd6
- 004bb874 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bb874 ["INT_ADD", "register:40f0:8", ["const:4bb874:8", "const:4:8"]]
- 004bb874 ["CALLIND", null, ["register:0:8"]]
+ 004de70c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004de70c ["INT_ADD", "register:40f0:8", ["const:4de70c:8", "const:4:8"]]
+ 004de70c ["CALLIND", null, ["register:0:8"]]
- 004bb874 bytes 20013fd6
+ 004de70c bytes 20013fd6
- 004bb8a0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bb8a0 ["INT_ADD", "register:40f0:8", ["const:4bb8a0:8", "const:4:8"]]
- 004bb8a0 ["CALLIND", null, ["register:0:8"]]
+ 004de738 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004de738 ["INT_ADD", "register:40f0:8", ["const:4de738:8", "const:4:8"]]
+ 004de738 ["CALLIND", null, ["register:0:8"]]
- 004bb8a0 bytes 20013fd6
+ 004de738 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcbdc84175587f59cc432bc06242bbd6"></a>

### [`004bb8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb8d4.md) → [`004de76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de76c.md) _ZN5Botan9Power_ModC2ERKNS_6BigIntENS0_11Usage_HintsEb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5a0.md) · 呼出先 1件 [`00bdc5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5c0.md)
- 新版 呼出元 1件 [`00c58ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ff0.md) · 呼出先 1件 [`00c59010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004de788",
      "incomplete_value": true,
      "site": "004de788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004bb8f0",
      "incomplete_value": true,
      "site": "004bb8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "004de780",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "004de788",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "004de780",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "004de788",
      "DATA",
      [
        "storage",
        "00c66958",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb8d4.md#insn-004bb8e0) · [`004bb8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb8d4.md#insn-004bb8e8) · [`004bb8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb8d4.md#insn-004bb8f4)
- 新版 [`004de778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de76c.md#insn-004de778) · [`004de780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de76c.md#insn-004de780) · [`004de78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de76c.md#insn-004de78c)

~~~diff
- 004bb8e0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004de778 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004bb8e0 bytes 083b0090
+ 004de778 bytes e83d0090
- 004bb8e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
- 004bb8e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004de780 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
+ 004de780 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004bb8e8 bytes 08e140f9
+ 004de780 bytes 08d945f9
- 004bb8f4 ["INT_ADD", "register:40f0:8", ["const:4bb8f4:8", "const:4:8"]]
- 004bb8f4 ["CALL", null, ["callee:00c59010:8"]]
+ 004de78c ["INT_ADD", "register:40f0:8", ["const:4de78c:8", "const:4:8"]]
+ 004de78c ["CALL", null, ["callee:00c59010:8"]]
- 004bb8f4 bytes 33831c94
+ 004de78c bytes 21ea1d94
~~~


<a id="compare-e3e29530f808a4dfcda28bb995516472"></a>

### [`004bb928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb928.md) → [`004de7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de7c0.md) _ZNK5Botan9Power_Mod11set_modulusERKNS_6BigIntENS0_11Usage_HintsEb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5c0.md) · 呼出先 8件 [`004bd8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd8d4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md)
- 新版 呼出元 1件 [`00c59010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59010.md) · 呼出先 8件 [`004e076c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e076c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004de8b8",
      "incomplete_value": false,
      "site": "004de8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bba20",
      "incomplete_value": false,
      "site": "004bba20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "definition_site": "004de854",
      "incomplete_value": true,
      "site": "004de854",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bb9bc",
      "incomplete_value": true,
      "site": "004bb9bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004de8c0",
      "value": [
        "leaf",
        "ram:c58ee0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004bba28",
      "value": [
        "leaf",
        "ram:bdc490:8"
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
      "004de844",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004de8b8",
      "DATA",
      [
        "storage",
        "00be9df8",
        null,
        "undefined *"
      ]
    ],
    [
      "004de8c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc490"
      ]
    ]
  ],
  "added": [
    [
      "004de844",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004de8b8",
      "DATA",
      [
        "storage",
        "00c669b8",
        null,
        "undefined *"
      ]
    ],
    [
      "004de8c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58ee0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb928.md#insn-004bb9bc) · [`004bba28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb928.md#insn-004bba28) · [`004bb974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb928.md#insn-004bb974)
- 新版 [`004de854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de7c0.md#insn-004de854) · [`004de8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de7c0.md#insn-004de8c0) · [`004de80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de7c0.md#insn-004de80c)

~~~diff
- 004bb9bc ["COPY", "register:0:8", ["register:4048:8"]]
- 004bb9bc ["INT_ADD", "register:40f0:8", ["const:4bb9bc:8", "const:4:8"]]
- 004bb9bc ["CALLIND", null, ["register:0:8"]]
+ 004de854 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004de854 ["INT_ADD", "register:40f0:8", ["const:4de854:8", "const:4:8"]]
+ 004de854 ["CALLIND", null, ["register:0:8"]]
- 004bb9bc bytes 20013fd6
+ 004de854 bytes 20013fd6
- 004bba28 ["INT_ADD", "register:40f0:8", ["const:4bba28:8", "const:4:8"]]
- 004bba28 ["CALL", null, ["ram:bdc490:8"]]
+ 004de8c0 ["INT_ADD", "register:40f0:8", ["const:4de8c0:8", "const:4:8"]]
+ 004de8c0 ["CALL", null, ["ram:c58ee0:8"]]
- 004bba28 bytes 9a821c94
+ 004de8c0 bytes 88e91d94
- 004bb974 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bb974 ["INT_ADD", "register:40f0:8", ["const:4bb974:8", "const:4:8"]]
- 004bb974 ["CALLIND", null, ["register:0:8"]]
+ 004de80c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004de80c ["INT_ADD", "register:40f0:8", ["const:4de80c:8", "const:4:8"]]
+ 004de80c ["CALLIND", null, ["register:0:8"]]
- 004bb974 bytes 00013fd6
+ 004de80c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b5de17732d510d6e821fbb841d9aa8a"></a>

### [`004bbab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbab8.md) → [`004de950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de950.md) _ZN5Botan9Power_ModC1ERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004de970",
      "incomplete_value": true,
      "site": "004de974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004bbad8",
      "incomplete_value": true,
      "site": "004bbadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "004de964",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "004de974",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "004de964",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "004de974",
      "DATA",
      [
        "storage",
        "00c66958",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bbac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbab8.md#insn-004bbac4) · [`004bbacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbab8.md#insn-004bbacc) · [`004bbaec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbab8.md#insn-004bbaec)
- 新版 [`004de95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de950.md#insn-004de95c) · [`004de964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de950.md#insn-004de964) · [`004de984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de950.md#insn-004de984)

~~~diff
- 004bbac4 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004de95c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004bbac4 bytes 083b0090
+ 004de95c bytes e83d0090
- 004bbacc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
- 004bbacc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004de964 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
+ 004de964 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004bbacc bytes 08e140f9
+ 004de964 bytes 08d945f9
- 004bbaec ["COPY", "register:0:8", ["register:4040:8"]]
- 004bbaec ["INT_ADD", "register:40f0:8", ["const:4bbaec:8", "const:4:8"]]
- 004bbaec ["CALLIND", null, ["register:0:8"]]
+ 004de984 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004de984 ["INT_ADD", "register:40f0:8", ["const:4de984:8", "const:4:8"]]
+ 004de984 ["CALLIND", null, ["register:0:8"]]
- 004bbaec bytes 00013fd6
+ 004de984 bytes 00013fd6
~~~


<a id="compare-53ce96459907786aa947a4c6816d4da8"></a>

### [`004bbdd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbdd8.md) → [`004dec70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004dec70.md) _ZN5Botan20Fixed_Base_Power_ModC2ERKNS_6BigIntES3_NS_9Power_Mod11Usage_HintsE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md) [`00bdc4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4a0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md) [`00c58ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ef0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dee14",
      "incomplete_value": true,
      "site": "004dee14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004bbf7c",
      "incomplete_value": true,
      "site": "004bbf7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "store_value",
    "new": {
      "definition_site": "004dee34",
      "incomplete_value": true,
      "site": "004dee38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004bbf9c",
      "incomplete_value": true,
      "site": "004bbfa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004decec",
      "incomplete_value": true,
      "site": "004decec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bbe54",
      "incomplete_value": true,
      "site": "004bbe54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004decdc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004dee0c",
      "READ",
      [
        "storage",
        "00c1b1c0",
        null,
        "pointer"
      ]
    ],
    [
      "004dee14",
      "DATA",
      [
        "storage",
        "00be9d98",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "004decdc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004dee0c",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "004dee14",
      "DATA",
      [
        "storage",
        "00c66958",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bbe54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbdd8.md#insn-004bbe54) · [`004bbe18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbdd8.md#insn-004bbe18) · [`004bbe28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bbdd8.md#insn-004bbe28)
- 新版 [`004decec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004dec70.md#insn-004decec) · [`004decb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004dec70.md#insn-004decb0) · [`004decc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004dec70.md#insn-004decc0)

~~~diff
- 004bbe54 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bbe54 ["INT_ADD", "register:40f0:8", ["const:4bbe54:8", "const:4:8"]]
- 004bbe54 ["CALLIND", null, ["register:0:8"]]
+ 004decec ["COPY", "register:0:8", ["register:4048:8"]]
+ 004decec ["INT_ADD", "register:40f0:8", ["const:4decec:8", "const:4:8"]]
+ 004decec ["CALLIND", null, ["register:0:8"]]
- 004bbe54 bytes 20013fd6
+ 004decec bytes 20013fd6
- 004bbe18 ["INT_ADD", "register:40f0:8", ["const:4bbe18:8", "const:4:8"]]
- 004bbe18 ["CALL", null, ["callee:00c58520:8"]]
+ 004decb0 ["INT_ADD", "register:40f0:8", ["const:4decb0:8", "const:4:8"]]
+ 004decb0 ["CALL", null, ["callee:00c58520:8"]]
- 004bbe18 bytes 2e7f1c94
+ 004decb0 bytes 1ce61d94
- 004bbe28 ["INT_ADD", "register:40f0:8", ["const:4bbe28:8", "const:4:8"]]
- 004bbe28 ["CALL", null, ["callee:00c58720:8"]]
+ 004decc0 ["INT_ADD", "register:40f0:8", ["const:4decc0:8", "const:4:8"]]
+ 004decc0 ["CALL", null, ["callee:00c58720:8"]]
- 004bbe28 bytes aa7f1c94
+ 004decc0 bytes 98e61d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1226f4bd5b93394fee9efc4ba7d0e64"></a>

### [`004bc070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc070.md) → [`004def08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004def08.md) FUN_004def08

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00521f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521f84.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00544e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544e1c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df0a0",
      "incomplete_value": true,
      "site": "004df0a0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bc208",
      "incomplete_value": true,
      "site": "004bc208",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df12c",
      "incomplete_value": true,
      "site": "004df12c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bc294",
      "incomplete_value": true,
      "site": "004bc294",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df210",
      "incomplete_value": true,
      "site": "004df210",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bc378",
      "incomplete_value": true,
      "site": "004bc378",
      "value": [
        "LOAD",
        "8",
        [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004df018",
      "READ",
      [
        "storage",
        "002b99c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df018",
      "READ",
      [
        "storage",
        "002b99b0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df018",
      "READ",
      [
        "storage",
        "002b99a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004df018",
      "READ",
      [
        "storage",
        "002cb0d0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df018",
      "READ",
      [
        "storage",
        "002cb0c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df018",
      "READ",
      [
        "storage",
        "002cb0b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc070.md#insn-004bc208) · [`004bc294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc070.md#insn-004bc294) · [`004bc378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc070.md#insn-004bc378)
- 新版 [`004df0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004def08.md#insn-004df0a0) · [`004df12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004def08.md#insn-004df12c) · [`004df210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004def08.md#insn-004df210)

~~~diff
- 004bc208 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bc208 ["INT_ADD", "register:40f0:8", ["const:4bc208:8", "const:4:8"]]
- 004bc208 ["CALLIND", null, ["register:0:8"]]
+ 004df0a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df0a0 ["INT_ADD", "register:40f0:8", ["const:4df0a0:8", "const:4:8"]]
+ 004df0a0 ["CALLIND", null, ["register:0:8"]]
- 004bc208 bytes 20013fd6
+ 004df0a0 bytes 20013fd6
- 004bc294 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bc294 ["INT_ADD", "register:40f0:8", ["const:4bc294:8", "const:4:8"]]
- 004bc294 ["CALLIND", null, ["register:0:8"]]
+ 004df12c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df12c ["INT_ADD", "register:40f0:8", ["const:4df12c:8", "const:4:8"]]
+ 004df12c ["CALLIND", null, ["register:0:8"]]
- 004bc294 bytes 20013fd6
+ 004df12c bytes 20013fd6
- 004bc378 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bc378 ["INT_ADD", "register:40f0:8", ["const:4bc378:8", "const:4:8"]]
- 004bc378 ["CALLIND", null, ["register:0:8"]]
+ 004df210 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df210 ["INT_ADD", "register:40f0:8", ["const:4df210:8", "const:4:8"]]
+ 004df210 ["CALLIND", null, ["register:0:8"]]
- 004bc378 bytes 20013fd6
+ 004df210 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51fcba85f53202b03068fc086cd1d943"></a>

### [`004bc440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc440.md) → [`004df2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df2d8.md) FUN_004df2d8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbe00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe00.md) [`00bdbec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbec0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58850.md) [`00c58910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58910.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df454",
      "incomplete_value": true,
      "site": "004df454",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bc5bc",
      "incomplete_value": true,
      "site": "004bc5bc",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df4b8",
      "incomplete_value": true,
      "site": "004df4b8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bc620",
      "incomplete_value": true,
      "site": "004bc620",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df520",
      "incomplete_value": true,
      "site": "004df520",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bc688",
      "incomplete_value": true,
      "site": "004bc688",
      "value": [
        "LOAD",
        "8",
        [
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
      "004df444",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004df4a8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004df510",
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
      "004df444",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004df4a8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004df510",
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

- 旧版 [`004bc5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc440.md#insn-004bc5bc) · [`004bc620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc440.md#insn-004bc620) · [`004bc688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc440.md#insn-004bc688)
- 新版 [`004df454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df2d8.md#insn-004df454) · [`004df4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df2d8.md#insn-004df4b8) · [`004df520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df2d8.md#insn-004df520)

~~~diff
- 004bc5bc ["COPY", "register:0:8", ["register:4048:8"]]
- 004bc5bc ["INT_ADD", "register:40f0:8", ["const:4bc5bc:8", "const:4:8"]]
- 004bc5bc ["CALLIND", null, ["register:0:8"]]
+ 004df454 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df454 ["INT_ADD", "register:40f0:8", ["const:4df454:8", "const:4:8"]]
+ 004df454 ["CALLIND", null, ["register:0:8"]]
- 004bc5bc bytes 20013fd6
+ 004df454 bytes 20013fd6
- 004bc620 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bc620 ["INT_ADD", "register:40f0:8", ["const:4bc620:8", "const:4:8"]]
- 004bc620 ["CALLIND", null, ["register:0:8"]]
+ 004df4b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df4b8 ["INT_ADD", "register:40f0:8", ["const:4df4b8:8", "const:4:8"]]
+ 004df4b8 ["CALLIND", null, ["register:0:8"]]
- 004bc620 bytes 20013fd6
+ 004df4b8 bytes 20013fd6
- 004bc688 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bc688 ["INT_ADD", "register:40f0:8", ["const:4bc688:8", "const:4:8"]]
- 004bc688 ["CALLIND", null, ["register:0:8"]]
+ 004df520 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df520 ["INT_ADD", "register:40f0:8", ["const:4df520:8", "const:4:8"]]
+ 004df520 ["CALLIND", null, ["register:0:8"]]
- 004bc688 bytes 20013fd6
+ 004df520 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5436c826a4913dc108bf08a0cb43bbe"></a>

### [`004bc804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc804.md) → [`004df69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md) FUN_004df69c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`004b4c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4c94.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`004d7b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7b2c.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.16% / 新版 98.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df834",
      "incomplete_value": true,
      "site": "004df834",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bc99c",
      "incomplete_value": true,
      "site": "004bc99c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004df85c",
      "value": [
        "leaf",
        "ram:c58820:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004bc9c4",
      "value": [
        "leaf",
        "ram:bdbdd0:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df8ec",
      "incomplete_value": true,
      "site": "004df8ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bca54",
      "incomplete_value": true,
      "site": "004bca54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004df7b0",
      "READ",
      [
        "storage",
        "002b99c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df7b0",
      "READ",
      [
        "storage",
        "002b99b0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df7b0",
      "READ",
      [
        "storage",
        "002b99a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004df7b0",
      "READ",
      [
        "storage",
        "002cb0d0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df7b0",
      "READ",
      [
        "storage",
        "002cb0c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df7b0",
      "READ",
      [
        "storage",
        "002cb0b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc804.md#insn-004bc99c) · [`004bc9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc804.md#insn-004bc9c4) · [`004bca54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc804.md#insn-004bca54)
- 新版 [`004df834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md#insn-004df834) · [`004df85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md#insn-004df85c) · [`004df8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md#insn-004df8ec)

~~~diff
- 004bc99c ["COPY", "register:0:8", ["register:4048:8"]]
- 004bc99c ["INT_ADD", "register:40f0:8", ["const:4bc99c:8", "const:4:8"]]
- 004bc99c ["CALLIND", null, ["register:0:8"]]
+ 004df834 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df834 ["INT_ADD", "register:40f0:8", ["const:4df834:8", "const:4:8"]]
+ 004df834 ["CALLIND", null, ["register:0:8"]]
- 004bc99c bytes 20013fd6
+ 004df834 bytes 20013fd6
- 004bc9c4 ["INT_ADD", "register:40f0:8", ["const:4bc9c4:8", "const:4:8"]]
- 004bc9c4 ["CALL", null, ["ram:bdbdd0:8"]]
+ 004df85c ["INT_ADD", "register:40f0:8", ["const:4df85c:8", "const:4:8"]]
+ 004df85c ["CALL", null, ["ram:c58820:8"]]
- 004bc9c4 bytes 037d1c94
+ 004df85c bytes f1e31d94
- 004bca54 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bca54 ["INT_ADD", "register:40f0:8", ["const:4bca54:8", "const:4:8"]]
- 004bca54 ["CALLIND", null, ["register:0:8"]]
+ 004df8ec ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df8ec ["INT_ADD", "register:40f0:8", ["const:4df8ec:8", "const:4:8"]]
+ 004df8ec ["CALLIND", null, ["register:0:8"]]
- 004bca54 bytes 20013fd6
+ 004df8ec bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e120f8ff33580b11b4f4e26528b84cab"></a>

### [`004bcf24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bcf24.md) → [`004dfdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004dfdbc.md) _ZNK5Botan15Modular_Reducer6reduceERKNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc4d0.md) · 呼出先 20件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00496d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)
- 新版 呼出元 1件 [`00c58f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f20.md) · 呼出先 20件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)

変更の種類 call, call_argument_candidate, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.60% / 新版 98.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004dff1c",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004bd084",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
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
      "site": "004e00f4",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004bd25c",
      "value": [
        "leaf",
        "ram:bdbcf0:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e01fc",
      "incomplete_value": true,
      "site": "004e01fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bd364",
      "incomplete_value": true,
      "site": "004bd364",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004dff10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004dff1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004e00f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ]
  ],
  "added": [
    [
      "004dff10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004dff1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004e00f4",
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

- 旧版 [`004bd084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bcf24.md#insn-004bd084) · [`004bd25c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bcf24.md#insn-004bd25c) · [`004bd364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bcf24.md#insn-004bd364)
- 新版 [`004dff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004dfdbc.md#insn-004dff1c) · [`004e00f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004dfdbc.md#insn-004e00f4) · [`004e01fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004dfdbc.md#insn-004e01fc)

~~~diff
- 004bd084 ["INT_ADD", "register:40f0:8", ["const:4bd084:8", "const:4:8"]]
- 004bd084 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004dff1c ["INT_ADD", "register:40f0:8", ["const:4dff1c:8", "const:4:8"]]
+ 004dff1c ["CALL", null, ["ram:c58740:8"]]
- 004bd084 bytes 1b7b1c94
+ 004dff1c bytes 09e21d94
- 004bd25c ["INT_ADD", "register:40f0:8", ["const:4bd25c:8", "const:4:8"]]
- 004bd25c ["CALL", null, ["ram:bdbcf0:8"]]
+ 004e00f4 ["INT_ADD", "register:40f0:8", ["const:4e00f4:8", "const:4:8"]]
+ 004e00f4 ["CALL", null, ["ram:c58740:8"]]
- 004bd25c bytes a57a1c94
+ 004e00f4 bytes 93e11d94
- 004bd364 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bd364 ["INT_ADD", "register:40f0:8", ["const:4bd364:8", "const:4:8"]]
- 004bd364 ["CALLIND", null, ["register:0:8"]]
+ 004e01fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e01fc ["INT_ADD", "register:40f0:8", ["const:4e01fc:8", "const:4:8"]]
+ 004e01fc ["CALLIND", null, ["register:0:8"]]
- 004bd364 bytes 20013fd6
+ 004e01fc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-854ae4bfec96fe8da821cf1ffa3b1c4d"></a>

### [`004bd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd550.md) → [`004e03e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md) FUN_004e03e8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`004b47ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b47ec.md) [`004b4c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4c94.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 0件  · 呼出先 13件 [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`004d7684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md) [`004d7b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7b2c.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.98% / 新版 95.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e0428",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004bd590",
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e0440",
      "value": [
        "leaf",
        "ram:c58820:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004bd5a8",
      "value": [
        "leaf",
        "ram:bdbdd0:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e066c",
      "incomplete_value": true,
      "site": "004e066c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "definition_site": "004bd7d4",
      "incomplete_value": true,
      "site": "004bd7d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "004e0428",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004e0440",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbdd0"
      ]
    ],
    [
      "004e065c",
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
      "004e0428",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004e0440",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58820"
      ]
    ],
    [
      "004e065c",
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

- 旧版 [`004bd590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd550.md#insn-004bd590) · [`004bd5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd550.md#insn-004bd5a8) · [`004bd7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd550.md#insn-004bd7d4)
- 新版 [`004e0428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md#insn-004e0428) · [`004e0440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md#insn-004e0440) · [`004e066c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md#insn-004e066c)

~~~diff
- 004bd590 ["INT_ADD", "register:40f0:8", ["const:4bd590:8", "const:4:8"]]
- 004bd590 ["CALL", null, ["ram:bdbcf0:8"]]
+ 004e0428 ["INT_ADD", "register:40f0:8", ["const:4e0428:8", "const:4:8"]]
+ 004e0428 ["CALL", null, ["ram:c58740:8"]]
- 004bd590 bytes d8791c94
+ 004e0428 bytes c6e01d94
- 004bd5a8 ["INT_ADD", "register:40f0:8", ["const:4bd5a8:8", "const:4:8"]]
- 004bd5a8 ["CALL", null, ["ram:bdbdd0:8"]]
+ 004e0440 ["INT_ADD", "register:40f0:8", ["const:4e0440:8", "const:4:8"]]
+ 004e0440 ["CALL", null, ["ram:c58820:8"]]
- 004bd5a8 bytes 0a7a1c94
+ 004e0440 bytes f8e01d94
- 004bd7d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bd7d4 ["INT_ADD", "register:40f0:8", ["const:4bd7d4:8", "const:4:8"]]
- 004bd7d4 ["CALLIND", null, ["register:0:8"]]
+ 004e066c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e066c ["INT_ADD", "register:40f0:8", ["const:4e066c:8", "const:4:8"]]
+ 004e066c ["CALLIND", null, ["register:0:8"]]
- 004bd7d4 bytes 20013fd6
+ 004e066c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-141c071d354975b5bab7c3f40201cf9e"></a>

### [`004bd8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd8d4.md) → [`004e076c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e076c.md) FUN_004e076c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004bb928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb928.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`004de7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de7c0.md) · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.17% / 新版 93.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 6件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e07a0",
      "incomplete_value": false,
      "site": "004e07b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd908",
      "incomplete_value": false,
      "site": "004bd918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "site": "004e07c4",
      "value": [
        "leaf",
        "ram:c58740:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004bd92c",
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e07f0",
      "value": [
        "leaf",
        "ram:c58ee0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004bd958",
      "value": [
        "leaf",
        "ram:bdc490:8"
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
      "004e07b0",
      "DATA",
      [
        "storage",
        "00be9e38",
        null,
        "undefined *"
      ]
    ],
    [
      "004e07c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbcf0"
      ]
    ],
    [
      "004e07f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc490"
      ]
    ]
  ],
  "added": [
    [
      "004e07b0",
      "DATA",
      [
        "storage",
        "00c669f8",
        null,
        "undefined *"
      ]
    ],
    [
      "004e07c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58740"
      ]
    ],
    [
      "004e07f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58ee0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd8d4.md#insn-004bd92c) · [`004bd958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd8d4.md#insn-004bd958) · [`004bda94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd8d4.md#insn-004bda94)
- 新版 [`004e07c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e076c.md#insn-004e07c4) · [`004e07f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e076c.md#insn-004e07f0) · [`004e092c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e076c.md#insn-004e092c)

~~~diff
- 004bd92c ["INT_ADD", "register:40f0:8", ["const:4bd92c:8", "const:4:8"]]
- 004bd92c ["CALL", null, ["ram:bdbcf0:8"]]
+ 004e07c4 ["INT_ADD", "register:40f0:8", ["const:4e07c4:8", "const:4:8"]]
+ 004e07c4 ["CALL", null, ["ram:c58740:8"]]
- 004bd92c bytes f1781c94
+ 004e07c4 bytes dfdf1d94
- 004bd958 ["INT_ADD", "register:40f0:8", ["const:4bd958:8", "const:4:8"]]
- 004bd958 ["CALL", null, ["ram:bdc490:8"]]
+ 004e07f0 ["INT_ADD", "register:40f0:8", ["const:4e07f0:8", "const:4:8"]]
+ 004e07f0 ["CALL", null, ["ram:c58ee0:8"]]
- 004bd958 bytes ce7a1c94
+ 004e07f0 bytes bce11d94
- 004bda94 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bda94 ["INT_ADD", "register:40f0:8", ["const:4bda94:8", "const:4:8"]]
- 004bda94 ["CALLIND", null, ["register:0:8"]]
+ 004e092c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e092c ["INT_ADD", "register:40f0:8", ["const:4e092c:8", "const:4:8"]]
+ 004e092c ["CALLIND", null, ["register:0:8"]]
- 004bda94 bytes 20013fd6
+ 004e092c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-829e195146dae461480413cbfcd5150f"></a>

### [`004bdcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bdcd0.md) → [`004e0b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0b68.md) FUN_004e0b68

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

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
      "definition_site": "004e0bd0",
      "incomplete_value": true,
      "site": "004e0bd0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bdd38",
      "incomplete_value": true,
      "site": "004bdd38",
      "value": [
        "LOAD",
        "8",
        [
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
      "004e0bc0",
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
      "004e0bc0",
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

- 旧版 [`004bdd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bdcd0.md#insn-004bdd38) · [`004bdd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bdcd0.md#insn-004bdd00) · [`004bdd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bdcd0.md#insn-004bdd28)
- 新版 [`004e0bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0b68.md#insn-004e0bd0) · [`004e0b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0b68.md#insn-004e0b98) · [`004e0bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0b68.md#insn-004e0bc0)

~~~diff
- 004bdd38 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bdd38 ["INT_ADD", "register:40f0:8", ["const:4bdd38:8", "const:4:8"]]
- 004bdd38 ["CALLIND", null, ["register:0:8"]]
+ 004e0bd0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e0bd0 ["INT_ADD", "register:40f0:8", ["const:4e0bd0:8", "const:4:8"]]
+ 004e0bd0 ["CALLIND", null, ["register:0:8"]]
- 004bdd38 bytes 20013fd6
+ 004e0bd0 bytes 20013fd6
- 004bdd00 ["COPY", "register:40b0:8", ["const:bea000:8"]]
+ 004e0b98 ["COPY", "register:40b0:8", ["const:c67000:8"]]
- 004bdd00 bytes 763900b0
+ 004e0b98 bytes 363c00f0
- 004bdd28 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
- 004bdd28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e0bc0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:338:8"]]
+ 004e0bc0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bdd28 bytes c9be43f9
+ 004e0bc0 bytes c99e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-929d9342b9a87a2286c8e0d53df7f42f"></a>

### [`004bdd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bdd7c.md) → [`004e0c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0c14.md) _ZN5Botan15Modular_ReducerC1ERKNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc490.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c58ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ee0.md) · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e0cb8",
      "incomplete_value": true,
      "site": "004e0cb8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bde20",
      "incomplete_value": true,
      "site": "004bde20",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004e0d80",
      "incomplete_value": true,
      "site": "004e0d80",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bdee8",
      "incomplete_value": true,
      "site": "004bdee8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e0e38",
      "incomplete_value": true,
      "site": "004e0e38",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004bdfa0",
      "incomplete_value": true,
      "site": "004bdfa0",
      "value": [
        "LOAD",
        "8",
        [
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
      "004e0ca8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e0d70",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e0e28",
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
      "004e0ca8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e0d70",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e0e28",
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

- 旧版 [`004bde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bdd7c.md#insn-004bde20) · [`004bdee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bdd7c.md#insn-004bdee8) · [`004bdfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bdd7c.md#insn-004bdfa0)
- 新版 [`004e0cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0c14.md#insn-004e0cb8) · [`004e0d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0c14.md#insn-004e0d80) · [`004e0e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0c14.md#insn-004e0e38)

~~~diff
- 004bde20 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bde20 ["INT_ADD", "register:40f0:8", ["const:4bde20:8", "const:4:8"]]
- 004bde20 ["CALLIND", null, ["register:0:8"]]
+ 004e0cb8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e0cb8 ["INT_ADD", "register:40f0:8", ["const:4e0cb8:8", "const:4:8"]]
+ 004e0cb8 ["CALLIND", null, ["register:0:8"]]
- 004bde20 bytes 20013fd6
+ 004e0cb8 bytes 20013fd6
- 004bdee8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bdee8 ["INT_ADD", "register:40f0:8", ["const:4bdee8:8", "const:4:8"]]
- 004bdee8 ["CALLIND", null, ["register:0:8"]]
+ 004e0d80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e0d80 ["INT_ADD", "register:40f0:8", ["const:4e0d80:8", "const:4:8"]]
+ 004e0d80 ["CALLIND", null, ["register:0:8"]]
- 004bdee8 bytes 20013fd6
+ 004e0d80 bytes 20013fd6
- 004bdfa0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bdfa0 ["INT_ADD", "register:40f0:8", ["const:4bdfa0:8", "const:4:8"]]
- 004bdfa0 ["CALLIND", null, ["register:0:8"]]
+ 004e0e38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e0e38 ["INT_ADD", "register:40f0:8", ["const:4e0e38:8", "const:4:8"]]
+ 004e0e38 ["CALLIND", null, ["register:0:8"]]
- 004bdfa0 bytes 20013fd6
+ 004e0e38 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47d4ed7e6b302d9ca4c0bcf8d2987b67"></a>

### [`004be0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004be/004be0f4.md) → [`004e0f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0f8c.md) _ZN5Botan6ressolERKNS_6BigIntES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 25件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.40% / 新版 90.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 47件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e1008",
      "incomplete_value": true,
      "site": "004e1008",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004be170",
      "incomplete_value": true,
      "site": "004be170",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004e1058",
      "incomplete_value": true,
      "site": "004e1058",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004be1c0",
      "incomplete_value": true,
      "site": "004be1c0",
      "value": [
        "LOAD",
        "8",
        [
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
    "kind": "call_target",
    "new": {
      "definition_site": "004e10bc",
      "incomplete_value": true,
      "site": "004e10bc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004be224",
      "incomplete_value": true,
      "site": "004be224",
      "value": [
        "LOAD",
        "8",
        [
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
      "004e0ff8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e1048",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e10ac",
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
      "004e0ff8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e1048",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e10ac",
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

- 旧版 [`004be170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004be/004be0f4.md#insn-004be170) · [`004be1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004be/004be0f4.md#insn-004be1c0) · [`004be224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004be/004be0f4.md#insn-004be224)
- 新版 [`004e1008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0f8c.md#insn-004e1008) · [`004e1058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0f8c.md#insn-004e1058) · [`004e10bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0f8c.md#insn-004e10bc)

~~~diff
- 004be170 ["COPY", "register:0:8", ["register:4048:8"]]
- 004be170 ["INT_ADD", "register:40f0:8", ["const:4be170:8", "const:4:8"]]
- 004be170 ["CALLIND", null, ["register:0:8"]]
+ 004e1008 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e1008 ["INT_ADD", "register:40f0:8", ["const:4e1008:8", "const:4:8"]]
+ 004e1008 ["CALLIND", null, ["register:0:8"]]
- 004be170 bytes 20013fd6
+ 004e1008 bytes 20013fd6
- 004be1c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004be1c0 ["INT_ADD", "register:40f0:8", ["const:4be1c0:8", "const:4:8"]]
- 004be1c0 ["CALLIND", null, ["register:0:8"]]
+ 004e1058 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e1058 ["INT_ADD", "register:40f0:8", ["const:4e1058:8", "const:4:8"]]
+ 004e1058 ["CALLIND", null, ["register:0:8"]]
- 004be1c0 bytes 20013fd6
+ 004e1058 bytes 20013fd6
- 004be224 ["COPY", "register:0:8", ["register:4048:8"]]
- 004be224 ["INT_ADD", "register:40f0:8", ["const:4be224:8", "const:4:8"]]
- 004be224 ["CALLIND", null, ["register:0:8"]]
+ 004e10bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e10bc ["INT_ADD", "register:40f0:8", ["const:4e10bc:8", "const:4:8"]]
+ 004e10bc ["CALLIND", null, ["register:0:8"]]
- 004be224 bytes 20013fd6
+ 004e10bc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab10b37dc9e05429baa1dce649e09126"></a>

### [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) → [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) FUN_004e2414

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`004bf520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf520.md) [`004c0520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c0520.md) [`004c05d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05d4.md) [`004c8d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8d94.md) [`004c94e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c94e0.md) · 呼出先 40件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md)
- 新版 呼出元 6件 [`004e23b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e23b8.md) [`004e33b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e33b8.md) [`004e346c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e346c.md) [`004ebc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md) [`004ec378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec378.md) · 呼出先 40件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.08% / 新版 94.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 14件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e24bc",
      "incomplete_value": false,
      "site": "004e24bc",
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
      "definition_site": "004bf624",
      "incomplete_value": false,
      "site": "004bf624",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e2854",
      "incomplete_value": true,
      "site": "004e2854",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:308:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf9bc",
      "incomplete_value": true,
      "site": "004bf9bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:29a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e28b0",
      "incomplete_value": true,
      "site": "004e28b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bfa18",
      "incomplete_value": true,
      "site": "004bfa18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3bb:8"
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
      "004e244c",
      "PARAM",
      [
        "storage",
        "002ac833",
        null,
        "string"
      ]
    ],
    [
      "004e2478",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ],
    [
      "004e24bc",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004e244c",
      "PARAM",
      [
        "storage",
        "002bd8ab",
        null,
        "string"
      ]
    ],
    [
      "004e2478",
      "PARAM",
      [
        "storage",
        "002ab265",
        null,
        null
      ]
    ],
    [
      "004e24bc",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md#insn-004bf5d8) · [`004bf5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md#insn-004bf5e8) · [`004bf75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md#insn-004bf75c)
- 新版 [`004e2470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md#insn-004e2470) · [`004e2480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md#insn-004e2480) · [`004e25f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md#insn-004e25f4)

~~~diff
- 004bf5d8 ["INT_ADD", "register:40f0:8", ["const:4bf5d8:8", "const:4:8"]]
- 004bf5d8 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004e2470 ["INT_ADD", "register:40f0:8", ["const:4e2470:8", "const:4:8"]]
+ 004e2470 ["CALL", null, ["callee:00c57cb0:8"]]
- 004bf5d8 bytes 226f1c94
+ 004e2470 bytes 10d61d94
- 004bf5e8 ["INT_ADD", "register:40f0:8", ["const:4bf5e8:8", "const:4:8"]]
- 004bf5e8 ["CALL", null, ["callee:00c57b70:8"]]
+ 004e2480 ["INT_ADD", "register:40f0:8", ["const:4e2480:8", "const:4:8"]]
+ 004e2480 ["CALL", null, ["callee:00c57b70:8"]]
- 004bf5e8 bytes ce6e1c94
+ 004e2480 bytes bcd51d94
- 004bf75c ["INT_ADD", "register:40f0:8", ["const:4bf75c:8", "const:4:8"]]
- 004bf75c ["CALL", null, ["callee:00c57cb0:8"]]
+ 004e25f4 ["INT_ADD", "register:40f0:8", ["const:4e25f4:8", "const:4:8"]]
+ 004e25f4 ["CALL", null, ["callee:00c57cb0:8"]]
- 004bf75c bytes c16e1c94
+ 004e25f4 bytes afd51d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa001e911c55a951019f7b6c56b9d9b8"></a>

### [`004c05ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md) → [`004e3484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md) _ZN5Botan13pbes2_decryptERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc600.md) · 呼出先 36件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00513138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513138.md)
- 新版 呼出元 1件 [`00c59050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59050.md) · 呼出先 36件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535fd0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.19% / 新版 93.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 12件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e34d4",
      "incomplete_value": true,
      "site": "004e34d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c063c",
      "incomplete_value": true,
      "site": "004c063c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004e3668",
      "incomplete_value": true,
      "site": "004e3668",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c07d0",
      "incomplete_value": true,
      "site": "004c07d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3bb:8"
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
      "definition_site": "004e3788",
      "incomplete_value": true,
      "site": "004e3788",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:76f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c08f0",
      "incomplete_value": true,
      "site": "004c08f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6f7:8"
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
      "004e34c0",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004e34d4",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3508",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004e34c0",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004e34d4",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3508",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c06a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md#insn-004c06a4) · [`004c0728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md#insn-004c0728) · [`004c076c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c0/004c05ec.md#insn-004c076c)
- 新版 [`004e353c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md#insn-004e353c) · [`004e35c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md#insn-004e35c0) · [`004e3604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md#insn-004e3604)

~~~diff
- 004c06a4 ["INT_ADD", "register:40f0:8", ["const:4c06a4:8", "const:4:8"]]
- 004c06a4 ["CALL", null, ["ram:bdba30:8"]]
+ 004e353c ["INT_ADD", "register:40f0:8", ["const:4e353c:8", "const:4:8"]]
+ 004e353c ["CALL", null, ["ram:c58480:8"]]
- 004c06a4 bytes e36c1c94
+ 004e353c bytes d1d31d94
- 004c0728 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c0728 ["INT_ADD", "register:40f0:8", ["const:4c0728:8", "const:4:8"]]
- 004c0728 ["CALLIND", null, ["register:0:8"]]
+ 004e35c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e35c0 ["INT_ADD", "register:40f0:8", ["const:4e35c0:8", "const:4:8"]]
+ 004e35c0 ["CALLIND", null, ["register:0:8"]]
- 004c0728 bytes 20013fd6
+ 004e35c0 bytes 20013fd6
- 004c076c ["COPY", "register:0:8", ["register:4048:8"]]
- 004c076c ["INT_ADD", "register:40f0:8", ["const:4c076c:8", "const:4:8"]]
- 004c076c ["CALLIND", null, ["register:0:8"]]
+ 004e3604 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e3604 ["INT_ADD", "register:40f0:8", ["const:4e3604:8", "const:4:8"]]
+ 004e3604 ["CALLIND", null, ["register:0:8"]]
- 004c076c bytes 20013fd6
+ 004e3604 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65b27db03f5362e18daaebb515a7d95e"></a>

### [`004c13f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c13f0.md) → [`004e4288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4288.md) _ZN5Botan11BER_Decoder15decode_optionalImEERS0_RT_NS_8ASN1_TagES5_RKS3_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc610.md) · 呼出先 8件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8d0.md) [`00bdba40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba40.md) [`00bdbbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbd0.md)
- 新版 呼出元 1件 [`00c59060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59060.md) · 呼出先 8件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58320.md) [`00c58490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58490.md) [`00c58620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58620.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.92% / 新版 98.92%

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
      "site": "004e42f8",
      "value": [
        "leaf",
        "ram:c58490:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c1460",
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
      "definition_site": "004e4354",
      "incomplete_value": true,
      "site": "004e4354",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c14bc",
      "incomplete_value": true,
      "site": "004c14bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004e43c0",
      "incomplete_value": true,
      "site": "004e43c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c1528",
      "incomplete_value": true,
      "site": "004c1528",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e42f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba40"
      ]
    ],
    [
      "004e4344",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e43b0",
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
      "004e42f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58490"
      ]
    ],
    [
      "004e4344",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e43b0",
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

- 旧版 [`004c1460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c13f0.md#insn-004c1460) · [`004c14bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c13f0.md#insn-004c14bc) · [`004c1528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c13f0.md#insn-004c1528)
- 新版 [`004e42f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4288.md#insn-004e42f8) · [`004e4354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4288.md#insn-004e4354) · [`004e43c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4288.md#insn-004e43c0)

~~~diff
- 004c1460 ["INT_ADD", "register:40f0:8", ["const:4c1460:8", "const:4:8"]]
- 004c1460 ["CALL", null, ["ram:bdba40:8"]]
+ 004e42f8 ["INT_ADD", "register:40f0:8", ["const:4e42f8:8", "const:4:8"]]
+ 004e42f8 ["CALL", null, ["ram:c58490:8"]]
- 004c1460 bytes 78691c94
+ 004e42f8 bytes 66d01d94
- 004c14bc ["COPY", "register:0:8", ["register:4048:8"]]
- 004c14bc ["INT_ADD", "register:40f0:8", ["const:4c14bc:8", "const:4:8"]]
- 004c14bc ["CALLIND", null, ["register:0:8"]]
+ 004e4354 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e4354 ["INT_ADD", "register:40f0:8", ["const:4e4354:8", "const:4:8"]]
+ 004e4354 ["CALLIND", null, ["register:0:8"]]
- 004c14bc bytes 20013fd6
+ 004e4354 bytes 20013fd6
- 004c1528 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c1528 ["INT_ADD", "register:40f0:8", ["const:4c1528:8", "const:4:8"]]
- 004c1528 ["CALLIND", null, ["register:0:8"]]
+ 004e43c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e43c0 ["INT_ADD", "register:40f0:8", ["const:4e43c0:8", "const:4:8"]]
+ 004e43c0 ["CALLIND", null, ["register:0:8"]]
- 004c1528 bytes 20013fd6
+ 004e43c0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec5ca2da595ca249c840b4f5feff0130"></a>

### [`004c15a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c15a4.md) → [`004e443c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e443c.md) _ZN5Botan11BER_Decoder15decode_optionalINS_19AlgorithmIdentifierEEERS0_RT_NS_8ASN1_TagES6_RKS4_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc620.md) · 呼出先 9件 [`005192a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/005192a0.md) [`00525f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8d0.md)
- 新版 呼出元 1件 [`00c59070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59070.md) · 呼出先 9件 [`0053c138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md) [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58320.md)

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
      "site": "004e44ac",
      "value": [
        "leaf",
        "ram:c58490:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c1614",
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
      "definition_site": "004e4508",
      "incomplete_value": true,
      "site": "004e4508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c1670",
      "incomplete_value": true,
      "site": "004c1670",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004e4598",
      "incomplete_value": true,
      "site": "004e4598",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c1700",
      "incomplete_value": true,
      "site": "004c1700",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e44ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba40"
      ]
    ],
    [
      "004e44f8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e4588",
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
      "004e44ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58490"
      ]
    ],
    [
      "004e44f8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e4588",
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

- 旧版 [`004c1614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c15a4.md#insn-004c1614) · [`004c1670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c15a4.md#insn-004c1670) · [`004c1700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c15a4.md#insn-004c1700)
- 新版 [`004e44ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e443c.md#insn-004e44ac) · [`004e4508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e443c.md#insn-004e4508) · [`004e4598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e443c.md#insn-004e4598)

~~~diff
- 004c1614 ["INT_ADD", "register:40f0:8", ["const:4c1614:8", "const:4:8"]]
- 004c1614 ["CALL", null, ["ram:bdba40:8"]]
+ 004e44ac ["INT_ADD", "register:40f0:8", ["const:4e44ac:8", "const:4:8"]]
+ 004e44ac ["CALL", null, ["ram:c58490:8"]]
- 004c1614 bytes 0b691c94
+ 004e44ac bytes f9cf1d94
- 004c1670 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c1670 ["INT_ADD", "register:40f0:8", ["const:4c1670:8", "const:4:8"]]
- 004c1670 ["CALLIND", null, ["register:0:8"]]
+ 004e4508 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e4508 ["INT_ADD", "register:40f0:8", ["const:4e4508:8", "const:4:8"]]
+ 004e4508 ["CALLIND", null, ["register:0:8"]]
- 004c1670 bytes 20013fd6
+ 004e4508 bytes 20013fd6
- 004c1700 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c1700 ["INT_ADD", "register:40f0:8", ["const:4c1700:8", "const:4:8"]]
- 004c1700 ["CALLIND", null, ["register:0:8"]]
+ 004e4598 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e4598 ["INT_ADD", "register:40f0:8", ["const:4e4598:8", "const:4:8"]]
+ 004e4598 ["CALLIND", null, ["register:0:8"]]
- 004c1700 bytes 20013fd6
+ 004e4598 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f7cd360a8ccd1382773f797564ce547"></a>

### [`004c1804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1804.md) → [`004e469c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e469c.md) _ZN5Botan5PBKDF6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5d0.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`00c59020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59020.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.99% / 新版 98.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e49a4",
      "incomplete_value": true,
      "site": "004e49a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c1b0c",
      "incomplete_value": true,
      "site": "004c1b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e48d4",
      "incomplete_value": false,
      "site": "004e48e0",
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
            "const:8ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1a3c",
      "incomplete_value": false,
      "site": "004c1a48",
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
            "const:833:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e4900",
      "incomplete_value": false,
      "site": "004e4908",
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
            "const:265:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1a68",
      "incomplete_value": false,
      "site": "004c1a70",
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
            "const:284:8"
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
      "004e48d4",
      "PARAM",
      [
        "storage",
        "002ac833",
        null,
        "string"
      ]
    ],
    [
      "004e4900",
      "PARAM",
      [
        "storage",
        "0029b284",
        null,
        null
      ]
    ],
    [
      "004e4998",
      "READ",
      [
        "storage",
        "00c1b1d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e48d4",
      "PARAM",
      [
        "storage",
        "002bd8ab",
        null,
        "string"
      ]
    ],
    [
      "004e4900",
      "PARAM",
      [
        "storage",
        "002ab265",
        null,
        null
      ]
    ],
    [
      "004e4998",
      "READ",
      [
        "storage",
        "00c9abc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c1a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1804.md#insn-004c1a48) · [`004c1a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1804.md#insn-004c1a70) · [`004c1850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1804.md#insn-004c1850)
- 新版 [`004e48e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e469c.md#insn-004e48e0) · [`004e4908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e469c.md#insn-004e4908) · [`004e46e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e469c.md#insn-004e46e8)

~~~diff
- 004c1a48 ["INT_ADD", "register:40f0:8", ["const:4c1a48:8", "const:4:8"]]
- 004c1a48 ["CALL", null, ["callee:00c57b60:8"]]
+ 004e48e0 ["INT_ADD", "register:40f0:8", ["const:4e48e0:8", "const:4:8"]]
+ 004e48e0 ["CALL", null, ["callee:00c57b60:8"]]
- 004c1a48 bytes b2651c94
+ 004e48e0 bytes a0cc1d94
- 004c1a70 ["INT_ADD", "register:40f0:8", ["const:4c1a70:8", "const:4:8"]]
- 004c1a70 ["CALL", null, ["callee:00c57b70:8"]]
+ 004e4908 ["INT_ADD", "register:40f0:8", ["const:4e4908:8", "const:4:8"]]
+ 004e4908 ["CALL", null, ["callee:00c57b70:8"]]
- 004c1a70 bytes ac651c94
+ 004e4908 bytes 9acc1d94
- 004c1850 ["INT_ADD", "register:40f0:8", ["const:4c1850:8", "const:4:8"]]
- 004c1850 ["CALL", null, ["callee:0043bae0:8"]]
+ 004e46e8 ["INT_ADD", "register:40f0:8", ["const:4e46e8:8", "const:4:8"]]
+ 004e46e8 ["CALL", null, ["callee:0043bae0:8"]]
- 004c1850 bytes e45dfd97
+ 004e46e8 bytes fe5cfd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e66504383711f97734153813676adea7"></a>

### [`004c1c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1c00.md) → [`004e4a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4a98.md) _ZN5Botan5PBKDF15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

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
      "definition_site": "004e4b10",
      "incomplete_value": false,
      "site": "004e4b18",
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
            "const:c3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1c78",
      "incomplete_value": false,
      "site": "004c1c80",
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
            "const:5f0:8"
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
      "definition_site": "004e4b50",
      "incomplete_value": true,
      "site": "004e4b5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c1cb8",
      "incomplete_value": true,
      "site": "004c1cc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004e4b4c",
      "incomplete_value": false,
      "site": "004e4b5c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004c1cb4",
      "incomplete_value": false,
      "site": "004c1cc4",
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
      "004e4b10",
      "PARAM",
      [
        "storage",
        "002a15f0",
        null,
        "string"
      ]
    ],
    [
      "004e4b4c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004e4b50",
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
      "004e4b10",
      "PARAM",
      [
        "storage",
        "002b1c3c",
        null,
        "string"
      ]
    ],
    [
      "004e4b4c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004e4b50",
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

- 旧版 [`004c1c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1c00.md#insn-004c1c80) · [`004c1cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1c00.md#insn-004c1cc4) · [`004c1c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1c00.md#insn-004c1c34)
- 新版 [`004e4b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4a98.md#insn-004e4b18) · [`004e4b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4a98.md#insn-004e4b5c) · [`004e4acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4a98.md#insn-004e4acc)

~~~diff
- 004c1c80 ["INT_ADD", "register:40f0:8", ["const:4c1c80:8", "const:4:8"]]
- 004c1c80 ["CALL", null, ["callee:0043dd98:8"]]
+ 004e4b18 ["INT_ADD", "register:40f0:8", ["const:4e4b18:8", "const:4:8"]]
+ 004e4b18 ["CALL", null, ["callee:0043dd98:8"]]
- 004c1c80 bytes 8665fd97
+ 004e4b18 bytes a064fd97
- 004c1cc4 ["INT_ADD", "register:40f0:8", ["const:4c1cc4:8", "const:4:8"]]
- 004c1cc4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004e4b5c ["INT_ADD", "register:40f0:8", ["const:4e4b5c:8", "const:4:8"]]
+ 004e4b5c ["CALL", null, ["callee:00c57b10:8"]]
- 004c1cc4 bytes ff641c94
+ 004e4b5c bytes edcb1d94
- 004c1c34 ["INT_ADD", "register:40f0:8", ["const:4c1c34:8", "const:4:8"]]
- 004c1c34 ["CALL", null, ["callee:00c59020:8"]]
+ 004e4acc ["INT_ADD", "register:40f0:8", ["const:4e4acc:8", "const:4:8"]]
+ 004e4acc ["CALL", null, ["callee:00c59020:8"]]
- 004c1c34 bytes 676a1c94
+ 004e4acc bytes 55d11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-355771123adec39f1e2a9451e1eb7171"></a>

### [`004c1fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1fec.md) → [`004e4e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4e84.md) _ZNK5Botan5PBKDF16pbkdf_iterationsEPhmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKhmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5e0.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`00c59030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59030.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.11% / 新版 92.11%

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
      "definition_site": "004e4f14",
      "incomplete_value": false,
      "site": "004e4f1c",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c207c",
      "incomplete_value": false,
      "site": "004c2084",
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
            "const:5fd:8"
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
      "definition_site": "004e4f68",
      "incomplete_value": true,
      "site": "004e4f74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c20d0",
      "incomplete_value": true,
      "site": "004c20dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e4f64",
      "incomplete_value": false,
      "site": "004e4f74",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004c20cc",
      "incomplete_value": false,
      "site": "004c20dc",
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
      "004e4f14",
      "PARAM",
      [
        "storage",
        "002ab5fd",
        null,
        "string"
      ]
    ],
    [
      "004e4f64",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004e4f68",
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
      "004e4f14",
      "PARAM",
      [
        "storage",
        "002bc520",
        null,
        "string"
      ]
    ],
    [
      "004e4f64",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004e4f68",
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

- 旧版 [`004c2084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1fec.md#insn-004c2084) · [`004c20dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1fec.md#insn-004c20dc) · [`004c2114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c1/004c1fec.md#insn-004c2114)
- 新版 [`004e4f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4e84.md#insn-004e4f1c) · [`004e4f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4e84.md#insn-004e4f74) · [`004e4fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4e84.md#insn-004e4fac)

~~~diff
- 004c2084 ["INT_ADD", "register:40f0:8", ["const:4c2084:8", "const:4:8"]]
- 004c2084 ["CALL", null, ["callee:00c57b70:8"]]
+ 004e4f1c ["INT_ADD", "register:40f0:8", ["const:4e4f1c:8", "const:4:8"]]
+ 004e4f1c ["CALL", null, ["callee:00c57b70:8"]]
- 004c2084 bytes 27641c94
+ 004e4f1c bytes 15cb1d94
- 004c20dc ["INT_ADD", "register:40f0:8", ["const:4c20dc:8", "const:4:8"]]
- 004c20dc ["CALL", null, ["callee:00c57b10:8"]]
+ 004e4f74 ["INT_ADD", "register:40f0:8", ["const:4e4f74:8", "const:4:8"]]
+ 004e4f74 ["CALL", null, ["callee:00c57b10:8"]]
- 004c20dc bytes f9631c94
+ 004e4f74 bytes e7ca1d94
- 004c2114 ["INT_ADD", "register:40f0:8", ["const:4c2114:8", "const:4:8"]]
- 004c2114 ["CALL", null, ["callee:00c58250:8"]]
+ 004e4fac ["INT_ADD", "register:40f0:8", ["const:4e4fac:8", "const:4:8"]]
+ 004e4fac ["CALL", null, ["callee:00c58250:8"]]
- 004c2114 bytes bb651c94
+ 004e4fac bytes a9cc1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a841bac495420814738797591018334"></a>

### [`004c222c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c222c.md) → [`004e50c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e50c4.md) _ZN5Botan6pbkdf2ERNS_25MessageAuthenticationCodeEPhmRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPKhmmNS3_6chrono8du

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc630.md) · 呼出先 8件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) [`00bdb070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb070.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c59080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59080.md) · 呼出先 8件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) [`00c57ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ac0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e557c",
      "incomplete_value": true,
      "site": "004e557c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c26e4",
      "incomplete_value": true,
      "site": "004c26e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e55dc",
      "incomplete_value": false,
      "site": "004e55fc",
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
      "definition_site": "004c2744",
      "incomplete_value": false,
      "site": "004c2764",
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
    "ordinal": 18,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e55e4",
      "incomplete_value": false,
      "site": "004e55fc",
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
      "definition_site": "004c274c",
      "incomplete_value": false,
      "site": "004c2764",
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
      "004e556c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e55dc",
      "PARAM",
      [
        "storage",
        "002928e2",
        null,
        "string"
      ]
    ],
    [
      "004e55e4",
      "PARAM",
      [
        "storage",
        "0029b50f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e556c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e55dc",
      "PARAM",
      [
        "storage",
        "002a1ff2",
        null,
        "string"
      ]
    ],
    [
      "004e55e4",
      "PARAM",
      [
        "storage",
        "002ab57d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c26e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c222c.md#insn-004c26e4) · [`004c2764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c222c.md#insn-004c2764) · [`004c2280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c222c.md#insn-004c2280)
- 新版 [`004e557c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e50c4.md#insn-004e557c) · [`004e55fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e50c4.md#insn-004e55fc) · [`004e5118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e50c4.md#insn-004e5118)

~~~diff
- 004c26e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c26e4 ["INT_ADD", "register:40f0:8", ["const:4c26e4:8", "const:4:8"]]
- 004c26e4 ["CALLIND", null, ["register:0:8"]]
+ 004e557c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e557c ["INT_ADD", "register:40f0:8", ["const:4e557c:8", "const:4:8"]]
+ 004e557c ["CALLIND", null, ["register:0:8"]]
- 004c26e4 bytes 20013fd6
+ 004e557c bytes 20013fd6
- 004c2764 ["INT_ADD", "register:40f0:8", ["const:4c2764:8", "const:4:8"]]
- 004c2764 ["CALL", null, ["callee:00c58250:8"]]
+ 004e55fc ["INT_ADD", "register:40f0:8", ["const:4e55fc:8", "const:4:8"]]
+ 004e55fc ["CALL", null, ["callee:00c58250:8"]]
- 004c2764 bytes 27641c94
+ 004e55fc bytes 15cb1d94
- 004c2280 ["INT_ADD", "register:40f0:8", ["const:4c2280:8", "const:4:8"]]
- 004c2280 ["CALL", null, ["callee:00c57c90:8"]]
+ 004e5118 ["INT_ADD", "register:40f0:8", ["const:4e5118:8", "const:4:8"]]
+ 004e5118 ["CALL", null, ["callee:00c57c90:8"]]
- 004c2280 bytes f0631c94
+ 004e5118 bytes deca1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3effebcad93442a9ad01b8bcbc9b3da"></a>

### [`004c2990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2990.md) → [`004e5828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5828.md) _ZN5Botan8PEM_Code6encodeEPKhmRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 1件 [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.77% / 新版 97.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e5858",
      "incomplete_value": false,
      "site": "004e5870",
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
            "const:78b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c29c0",
      "incomplete_value": false,
      "site": "004c29d8",
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
            "const:5f2:8"
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
      "definition_site": "004e5878",
      "incomplete_value": false,
      "site": "004e5880",
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
            "const:53a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c29e0",
      "incomplete_value": false,
      "site": "004c29e8",
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
            "const:617:8"
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
      "definition_site": "004e58b0",
      "incomplete_value": false,
      "site": "004e58bc",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2a18",
      "incomplete_value": false,
      "site": "004c2a24",
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
            "const:59e:8"
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
      "004e5858",
      "PARAM",
      [
        "storage",
        "0029c5f2",
        null,
        "string"
      ]
    ],
    [
      "004e5878",
      "PARAM",
      [
        "storage",
        "002ab617",
        null,
        "string"
      ]
    ],
    [
      "004e58b0",
      "PARAM",
      [
        "storage",
        "002a059e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e5858",
      "PARAM",
      [
        "storage",
        "002ac78b",
        null,
        "string"
      ]
    ],
    [
      "004e5878",
      "PARAM",
      [
        "storage",
        "002bc53a",
        null,
        "string"
      ]
    ],
    [
      "004e58b0",
      "PARAM",
      [
        "storage",
        "002b0b58",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c29d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2990.md#insn-004c29d8) · [`004c29e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2990.md#insn-004c29e8) · [`004c2a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2990.md#insn-004c2a24)
- 新版 [`004e5870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5828.md#insn-004e5870) · [`004e5880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5828.md#insn-004e5880) · [`004e58bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5828.md#insn-004e58bc)

~~~diff
- 004c29d8 ["INT_ADD", "register:40f0:8", ["const:4c29d8:8", "const:4:8"]]
- 004c29d8 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004e5870 ["INT_ADD", "register:40f0:8", ["const:4e5870:8", "const:4:8"]]
+ 004e5870 ["CALL", null, ["callee:00c57cb0:8"]]
- 004c29d8 bytes 22621c94
+ 004e5870 bytes 10c91d94
- 004c29e8 ["INT_ADD", "register:40f0:8", ["const:4c29e8:8", "const:4:8"]]
- 004c29e8 ["CALL", null, ["callee:00c57b70:8"]]
+ 004e5880 ["INT_ADD", "register:40f0:8", ["const:4e5880:8", "const:4:8"]]
+ 004e5880 ["CALL", null, ["callee:00c57b70:8"]]
- 004c29e8 bytes ce611c94
+ 004e5880 bytes bcc81d94
- 004c2a24 ["INT_ADD", "register:40f0:8", ["const:4c2a24:8", "const:4:8"]]
- 004c2a24 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004e58bc ["INT_ADD", "register:40f0:8", ["const:4e58bc:8", "const:4:8"]]
+ 004e58bc ["CALL", null, ["callee:00c57cb0:8"]]
- 004c2a24 bytes 0f621c94
+ 004e58bc bytes fdc81d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d392d86d9d04a7495cdc24586e4ddd0"></a>

### [`004c2d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2d3c.md) → [`004e5bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5bd4.md) _ZN5Botan8PEM_Code18decode_check_labelERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc650.md) · 呼出先 11件 [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c590a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590a0.md) · 呼出先 11件 [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.94% / 新版 96.94%

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
      "definition_site": "004e5cd8",
      "incomplete_value": false,
      "site": "004e5ce0",
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
            "const:43f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2e40",
      "incomplete_value": false,
      "site": "004c2e48",
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
            "const:3d1:8"
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
      "definition_site": "004e5ce8",
      "incomplete_value": false,
      "site": "004e5cf0",
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
            "const:7ae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2e50",
      "incomplete_value": false,
      "site": "004c2e58",
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
            "const:b55:8"
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
      "definition_site": "004e5d48",
      "incomplete_value": true,
      "site": "004e5d54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c2eb0",
      "incomplete_value": true,
      "site": "004c2ebc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e5cd8",
      "PARAM",
      [
        "storage",
        "0029b3d1",
        null,
        "string"
      ]
    ],
    [
      "004e5ce8",
      "PARAM",
      [
        "storage",
        "00297b55",
        null,
        "string"
      ]
    ],
    [
      "004e5d44",
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
      "004e5cd8",
      "PARAM",
      [
        "storage",
        "002ab43f",
        null,
        "string"
      ]
    ],
    [
      "004e5ce8",
      "PARAM",
      [
        "storage",
        "002a77ae",
        null,
        "string"
      ]
    ],
    [
      "004e5d44",
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

- 旧版 [`004c2e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2d3c.md#insn-004c2e48) · [`004c2e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2d3c.md#insn-004c2e58) · [`004c2ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2d3c.md#insn-004c2ebc)
- 新版 [`004e5ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5bd4.md#insn-004e5ce0) · [`004e5cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5bd4.md#insn-004e5cf0) · [`004e5d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5bd4.md#insn-004e5d54)

~~~diff
- 004c2e48 ["INT_ADD", "register:40f0:8", ["const:4c2e48:8", "const:4:8"]]
- 004c2e48 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004e5ce0 ["INT_ADD", "register:40f0:8", ["const:4e5ce0:8", "const:4:8"]]
+ 004e5ce0 ["CALL", null, ["callee:00c57cb0:8"]]
- 004c2e48 bytes 06611c94
+ 004e5ce0 bytes f4c71d94
- 004c2e58 ["INT_ADD", "register:40f0:8", ["const:4c2e58:8", "const:4:8"]]
- 004c2e58 ["CALL", null, ["callee:00c57b70:8"]]
+ 004e5cf0 ["INT_ADD", "register:40f0:8", ["const:4e5cf0:8", "const:4:8"]]
+ 004e5cf0 ["CALL", null, ["callee:00c57b70:8"]]
- 004c2e58 bytes b2601c94
+ 004e5cf0 bytes a0c71d94
- 004c2ebc ["INT_ADD", "register:40f0:8", ["const:4c2ebc:8", "const:4:8"]]
- 004c2ebc ["CALL", null, ["callee:00c57b10:8"]]
+ 004e5d54 ["INT_ADD", "register:40f0:8", ["const:4e5d54:8", "const:4:8"]]
+ 004e5d54 ["CALL", null, ["callee:00c57b10:8"]]
- 004c2ebc bytes 81601c94
+ 004e5d54 bytes 6fc71d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0318d9571f9215b9d6d005fe9c280cb3"></a>

### [`004c2f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2f88.md) → [`004e5e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5e20.md) _ZN5Botan8PEM_Code6decodeERNS_10DataSourceERNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc660.md) · 呼出先 16件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00426e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md)
- 新版 呼出元 1件 [`00c590b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590b0.md) · 呼出先 16件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.47% / 新版 95.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e5ea0",
      "incomplete_value": true,
      "site": "004e5ea0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:78b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3008",
      "incomplete_value": true,
      "site": "004c3008",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5f2:8"
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
      "definition_site": "004e5f80",
      "incomplete_value": false,
      "site": "004e5f8c",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c30e8",
      "incomplete_value": false,
      "site": "004c30f4",
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
            "const:59e:8"
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
      "definition_site": "004e5f94",
      "incomplete_value": false,
      "site": "004e5f9c",
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
            "const:f35:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c30fc",
      "incomplete_value": false,
      "site": "004c3104",
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
            "const:825:8"
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
      "004e5e8c",
      "READ",
      [
        "storage",
        "0029c5f2",
        null,
        "string"
      ]
    ],
    [
      "004e5f80",
      "PARAM",
      [
        "storage",
        "002a059e",
        null,
        "string"
      ]
    ],
    [
      "004e5f94",
      "PARAM",
      [
        "storage",
        "00292825",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e5e8c",
      "READ",
      [
        "storage",
        "002ac78b",
        null,
        "string"
      ]
    ],
    [
      "004e5f80",
      "PARAM",
      [
        "storage",
        "002b0b58",
        null,
        "string"
      ]
    ],
    [
      "004e5f94",
      "PARAM",
      [
        "storage",
        "002a1f35",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c30f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2f88.md#insn-004c30f4) · [`004c3104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2f88.md#insn-004c3104) · [`004c3344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c2/004c2f88.md#insn-004c3344)
- 新版 [`004e5f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5e20.md#insn-004e5f8c) · [`004e5f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5e20.md#insn-004e5f9c) · [`004e61dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5e20.md#insn-004e61dc)

~~~diff
- 004c30f4 ["INT_ADD", "register:40f0:8", ["const:4c30f4:8", "const:4:8"]]
- 004c30f4 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004e5f8c ["INT_ADD", "register:40f0:8", ["const:4e5f8c:8", "const:4:8"]]
+ 004e5f8c ["CALL", null, ["callee:00c57cb0:8"]]
- 004c30f4 bytes 5b601c94
+ 004e5f8c bytes 49c71d94
- 004c3104 ["INT_ADD", "register:40f0:8", ["const:4c3104:8", "const:4:8"]]
- 004c3104 ["CALL", null, ["callee:00c57b70:8"]]
+ 004e5f9c ["INT_ADD", "register:40f0:8", ["const:4e5f9c:8", "const:4:8"]]
+ 004e5f9c ["CALL", null, ["callee:00c57b70:8"]]
- 004c3104 bytes 07601c94
+ 004e5f9c bytes f5c61d94
- 004c3344 ["INT_ADD", "register:40f0:8", ["const:4c3344:8", "const:4:8"]]
- 004c3344 ["CALL", null, ["callee:0043dd98:8"]]
+ 004e61dc ["INT_ADD", "register:40f0:8", ["const:4e61dc:8", "const:4:8"]]
+ 004e61dc ["CALL", null, ["callee:0043dd98:8"]]
- 004c3344 bytes d55ffd97
+ 004e61dc bytes ef5efd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7578cc05ef215174271db56b5bdd2c7"></a>

### [`004c36b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c36b4.md) → [`004e654c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e654c.md) _ZN5Botan8PEM_Code18decode_check_labelERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc650.md) [`00bdc670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc670.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c590a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590a0.md) [`00c590c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590c0.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

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
      "site": "004e657c",
      "value": [
        "leaf",
        "ram:c590c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c36e4",
      "value": [
        "leaf",
        "ram:bdc670:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e65b4",
      "incomplete_value": true,
      "site": "004e65b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c371c",
      "incomplete_value": true,
      "site": "004c371c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e657c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc670"
      ]
    ],
    [
      "004e65a4",
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
      "004e657c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c590c0"
      ]
    ],
    [
      "004e65a4",
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

- 旧版 [`004c36e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c36b4.md#insn-004c36e4) · [`004c371c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c36b4.md#insn-004c371c) · [`004c36f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c36b4.md#insn-004c36f4)
- 新版 [`004e657c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e654c.md#insn-004e657c) · [`004e65b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e654c.md#insn-004e65b4) · [`004e658c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e654c.md#insn-004e658c)

~~~diff
- 004c36e4 ["INT_ADD", "register:40f0:8", ["const:4c36e4:8", "const:4:8"]]
- 004c36e4 ["CALL", null, ["ram:bdc670:8"]]
+ 004e657c ["INT_ADD", "register:40f0:8", ["const:4e657c:8", "const:4:8"]]
+ 004e657c ["CALL", null, ["ram:c590c0:8"]]
- 004c36e4 bytes e3631c94
+ 004e657c bytes d1ca1d94
- 004c371c ["COPY", "register:0:8", ["register:4048:8"]]
- 004c371c ["INT_ADD", "register:40f0:8", ["const:4c371c:8", "const:4:8"]]
- 004c371c ["CALLIND", null, ["register:0:8"]]
+ 004e65b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e65b4 ["INT_ADD", "register:40f0:8", ["const:4e65b4:8", "const:4:8"]]
+ 004e65b4 ["CALLIND", null, ["register:0:8"]]
- 004c371c bytes 20013fd6
+ 004e65b4 bytes 20013fd6
- 004c36f4 ["INT_ADD", "register:40f0:8", ["const:4c36f4:8", "const:4:8"]]
- 004c36f4 ["CALL", null, ["callee:00c590a0:8"]]
+ 004e658c ["INT_ADD", "register:40f0:8", ["const:4e658c:8", "const:4:8"]]
+ 004e658c ["CALL", null, ["callee:00c590a0:8"]]
- 004c36f4 bytes d7631c94
+ 004e658c bytes c5ca1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55378088c0d4ecd763a0d275a0ce7645"></a>

### [`004c37cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c37cc.md) → [`004e6664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6664.md) _ZN5Botan8PEM_Code6decodeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERS7_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc660.md) [`00bdc670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc670.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c590b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590b0.md) [`00c590c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590c0.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

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
      "site": "004e6694",
      "value": [
        "leaf",
        "ram:c590c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c37fc",
      "value": [
        "leaf",
        "ram:bdc670:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e66cc",
      "incomplete_value": true,
      "site": "004e66cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c3834",
      "incomplete_value": true,
      "site": "004c3834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e6694",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc670"
      ]
    ],
    [
      "004e66bc",
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
      "004e6694",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c590c0"
      ]
    ],
    [
      "004e66bc",
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

- 旧版 [`004c37fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c37cc.md#insn-004c37fc) · [`004c3834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c37cc.md#insn-004c3834) · [`004c380c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c37cc.md#insn-004c380c)
- 新版 [`004e6694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6664.md#insn-004e6694) · [`004e66cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6664.md#insn-004e66cc) · [`004e66a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6664.md#insn-004e66a4)

~~~diff
- 004c37fc ["INT_ADD", "register:40f0:8", ["const:4c37fc:8", "const:4:8"]]
- 004c37fc ["CALL", null, ["ram:bdc670:8"]]
+ 004e6694 ["INT_ADD", "register:40f0:8", ["const:4e6694:8", "const:4:8"]]
+ 004e6694 ["CALL", null, ["ram:c590c0:8"]]
- 004c37fc bytes 9d631c94
+ 004e6694 bytes 8bca1d94
- 004c3834 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c3834 ["INT_ADD", "register:40f0:8", ["const:4c3834:8", "const:4:8"]]
- 004c3834 ["CALLIND", null, ["register:0:8"]]
+ 004e66cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e66cc ["INT_ADD", "register:40f0:8", ["const:4e66cc:8", "const:4:8"]]
+ 004e66cc ["CALLIND", null, ["register:0:8"]]
- 004c3834 bytes 20013fd6
+ 004e66cc bytes 20013fd6
- 004c380c ["INT_ADD", "register:40f0:8", ["const:4c380c:8", "const:4:8"]]
- 004c380c ["CALL", null, ["callee:00c590b0:8"]]
+ 004e66a4 ["INT_ADD", "register:40f0:8", ["const:4e66a4:8", "const:4:8"]]
+ 004e66a4 ["CALL", null, ["callee:00c590b0:8"]]
- 004c380c bytes 95631c94
+ 004e66a4 bytes 83ca1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86d6b8f98d26fe9798611ba429dbfee2"></a>

### [`004c3890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3890.md) → [`004e6728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6728.md) _ZN5Botan8PEM_Code7matchesERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc680.md) · 呼出先 6件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 1件 [`00c590d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590d0.md) · 呼出先 6件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e6748",
      "incomplete_value": false,
      "site": "004e675c",
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
            "const:78b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c38b0",
      "incomplete_value": false,
      "site": "004c38c4",
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
            "const:5f2:8"
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
      "definition_site": "004e6814",
      "incomplete_value": true,
      "site": "004e6814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c397c",
      "incomplete_value": true,
      "site": "004c397c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e6748",
      "PARAM",
      [
        "storage",
        "0029c5f2",
        null,
        "string"
      ]
    ],
    [
      "004e6804",
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
      "004e6748",
      "PARAM",
      [
        "storage",
        "002ac78b",
        null,
        "string"
      ]
    ],
    [
      "004e6804",
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

- 旧版 [`004c38c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3890.md#insn-004c38c4) · [`004c397c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3890.md#insn-004c397c) · [`004c38ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3890.md#insn-004c38ac)
- 新版 [`004e675c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6728.md#insn-004e675c) · [`004e6814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6728.md#insn-004e6814) · [`004e6744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6728.md#insn-004e6744)

~~~diff
- 004c38c4 ["INT_ADD", "register:40f0:8", ["const:4c38c4:8", "const:4:8"]]
- 004c38c4 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004e675c ["INT_ADD", "register:40f0:8", ["const:4e675c:8", "const:4:8"]]
+ 004e675c ["CALL", null, ["callee:00c57cb0:8"]]
- 004c38c4 bytes 675e1c94
+ 004e675c bytes 55c51d94
- 004c397c ["COPY", "register:0:8", ["register:4048:8"]]
- 004c397c ["INT_ADD", "register:40f0:8", ["const:4c397c:8", "const:4:8"]]
- 004c397c ["CALLIND", null, ["register:0:8"]]
+ 004e6814 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e6814 ["INT_ADD", "register:40f0:8", ["const:4e6814:8", "const:4:8"]]
+ 004e6814 ["CALLIND", null, ["register:0:8"]]
- 004c397c bytes 20013fd6
+ 004e6814 bytes 20013fd6
- 004c38ac ["COPY", "register:4000:8", ["const:29c000:8"]]
+ 004e6744 ["COPY", "register:4000:8", ["const:2ac000:8"]]
- 004c38ac bytes c0eeffb0
+ 004e6744 bytes 20eeffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaf89afeac5cf9337403c670e3467474"></a>

### [`004c3a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3a08.md) → [`004e68a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e68a0.md) _ZN5Botan7get_emeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

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
      "definition_site": "004e68d0",
      "incomplete_value": true,
      "site": "004e68d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3a38",
      "incomplete_value": true,
      "site": "004c3a40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
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
      "definition_site": "004e68cc",
      "incomplete_value": false,
      "site": "004e68d8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004c3a34",
      "incomplete_value": false,
      "site": "004c3a40",
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
      "004e68cc",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004e68d0",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004e68d0",
      "PARAM",
      [
        "storage",
        "00be9a58",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004e68cc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004e68d0",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      "004e68d0",
      "PARAM",
      [
        "storage",
        "00c66618",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c3a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3a08.md#insn-004c3a40) · [`004c3a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3a08.md#insn-004c3a1c) · [`004c3a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3a08.md#insn-004c3a28)
- 新版 [`004e68d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e68a0.md#insn-004e68d8) · [`004e68b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e68a0.md#insn-004e68b4) · [`004e68c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e68a0.md#insn-004e68c0)

~~~diff
- 004c3a40 ["INT_ADD", "register:40f0:8", ["const:4c3a40:8", "const:4:8"]]
- 004c3a40 ["CALL", null, ["callee:00c57b10:8"]]
+ 004e68d8 ["INT_ADD", "register:40f0:8", ["const:4e68d8:8", "const:4:8"]]
+ 004e68d8 ["CALL", null, ["callee:00c57b10:8"]]
- 004c3a40 bytes a05d1c94
+ 004e68d8 bytes 8ec41d94
- 004c3a1c ["INT_ADD", "register:40f0:8", ["const:4c3a1c:8", "const:4:8"]]
- 004c3a1c ["CALL", null, ["callee:00c57af0:8"]]
+ 004e68b4 ["INT_ADD", "register:40f0:8", ["const:4e68b4:8", "const:4:8"]]
+ 004e68b4 ["CALL", null, ["callee:00c57af0:8"]]
- 004c3a1c bytes a15d1c94
+ 004e68b4 bytes 8fc41d94
- 004c3a28 ["INT_ADD", "register:40f0:8", ["const:4c3a28:8", "const:4:8"]]
- 004c3a28 ["CALL", null, ["callee:00c58ba0:8"]]
+ 004e68c0 ["INT_ADD", "register:40f0:8", ["const:4e68c0:8", "const:4:8"]]
+ 004e68c0 ["CALL", null, ["callee:00c58ba0:8"]]
- 004c3a28 bytes ca611c94
+ 004e68c0 bytes b8c81d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-243ae6bd8d006a442e24f4a73295dee4"></a>

### [`004c3a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3a84.md) → [`004e691c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e691c.md) _ZNK5Botan4EMSA15config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e6964",
      "incomplete_value": false,
      "site": "004e6970",
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
            "const:55f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3acc",
      "incomplete_value": false,
      "site": "004c3ad8",
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
            "const:a2a:8"
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
      "definition_site": "004e6990",
      "incomplete_value": false,
      "site": "004e6998",
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
            "const:b1c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3af8",
      "incomplete_value": false,
      "site": "004c3b00",
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
            "const:c43:8"
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
      "site": "004e69c0",
      "value": [
        "leaf",
        "ram:c590e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c3b28",
      "value": [
        "leaf",
        "ram:bdc690:8"
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
      "004e6964",
      "PARAM",
      [
        "storage",
        "00296a2a",
        null,
        "string"
      ]
    ],
    [
      "004e6990",
      "PARAM",
      [
        "storage",
        "00299c43",
        null,
        "string"
      ]
    ],
    [
      "004e69c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc690"
      ]
    ]
  ],
  "added": [
    [
      "004e6964",
      "PARAM",
      [
        "storage",
        "002a655f",
        null,
        "string"
      ]
    ],
    [
      "004e6990",
      "PARAM",
      [
        "storage",
        "002a9b1c",
        null,
        "string"
      ]
    ],
    [
      "004e69c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c590e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c3ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3a84.md#insn-004c3ad8) · [`004c3b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3a84.md#insn-004c3b00) · [`004c3b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3a84.md#insn-004c3b28)
- 新版 [`004e6970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e691c.md#insn-004e6970) · [`004e6998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e691c.md#insn-004e6998) · [`004e69c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e691c.md#insn-004e69c0)

~~~diff
- 004c3ad8 ["INT_ADD", "register:40f0:8", ["const:4c3ad8:8", "const:4:8"]]
- 004c3ad8 ["CALL", null, ["callee:00c57b60:8"]]
+ 004e6970 ["INT_ADD", "register:40f0:8", ["const:4e6970:8", "const:4:8"]]
+ 004e6970 ["CALL", null, ["callee:00c57b60:8"]]
- 004c3ad8 bytes 8e5d1c94
+ 004e6970 bytes 7cc41d94
- 004c3b00 ["INT_ADD", "register:40f0:8", ["const:4c3b00:8", "const:4:8"]]
- 004c3b00 ["CALL", null, ["callee:00c57b70:8"]]
+ 004e6998 ["INT_ADD", "register:40f0:8", ["const:4e6998:8", "const:4:8"]]
+ 004e6998 ["CALL", null, ["callee:00c57b70:8"]]
- 004c3b00 bytes 885d1c94
+ 004e6998 bytes 76c41d94
- 004c3b28 ["INT_ADD", "register:40f0:8", ["const:4c3b28:8", "const:4:8"]]
- 004c3b28 ["CALL", null, ["ram:bdc690:8"]]
+ 004e69c0 ["INT_ADD", "register:40f0:8", ["const:4e69c0:8", "const:4:8"]]
+ 004e69c0 ["CALL", null, ["ram:c590e0:8"]]
- 004c3b28 bytes da621c94
+ 004e69c0 bytes c8c91d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b0d285c73c99e607c58ed192b06560c"></a>

### [`004c3c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3c00.md) → [`004e6a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6a98.md) _ZN5Botan8get_emsaERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6a0.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c590f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590f0.md) · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.33% / 新版 99.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e6d98",
      "value": [
        "leaf",
        "ram:c59110:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c3f00",
      "value": [
        "leaf",
        "ram:bdc6c0:8"
      ]
    },
    "ordinal": 17,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e704c",
      "value": [
        "leaf",
        "ram:c59120:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c41b4",
      "value": [
        "leaf",
        "ram:bdc6d0:8"
      ]
    },
    "ordinal": 26,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e717c",
      "incomplete_value": true,
      "site": "004e7184",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c42e4",
      "incomplete_value": true,
      "site": "004c42ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
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
      "004e6d98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc6c0"
      ]
    ],
    [
      "004e704c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc6d0"
      ]
    ],
    [
      "004e7178",
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
      "004e6d98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59110"
      ]
    ],
    [
      "004e704c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c59120"
      ]
    ],
    [
      "004e7178",
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

- 旧版 [`004c3f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3c00.md#insn-004c3f00) · [`004c41b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3c00.md#insn-004c41b4) · [`004c42ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c3/004c3c00.md#insn-004c42ec)
- 新版 [`004e6d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6a98.md#insn-004e6d98) · [`004e704c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6a98.md#insn-004e704c) · [`004e7184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6a98.md#insn-004e7184)

~~~diff
- 004c3f00 ["INT_ADD", "register:40f0:8", ["const:4c3f00:8", "const:4:8"]]
- 004c3f00 ["CALL", null, ["ram:bdc6c0:8"]]
+ 004e6d98 ["INT_ADD", "register:40f0:8", ["const:4e6d98:8", "const:4:8"]]
+ 004e6d98 ["CALL", null, ["ram:c59110:8"]]
- 004c3f00 bytes f0611c94
+ 004e6d98 bytes dec81d94
- 004c41b4 ["INT_ADD", "register:40f0:8", ["const:4c41b4:8", "const:4:8"]]
- 004c41b4 ["CALL", null, ["ram:bdc6d0:8"]]
+ 004e704c ["INT_ADD", "register:40f0:8", ["const:4e704c:8", "const:4:8"]]
+ 004e704c ["CALL", null, ["ram:c59120:8"]]
- 004c41b4 bytes 47611c94
+ 004e704c bytes 35c81d94
- 004c42ec ["INT_ADD", "register:40f0:8", ["const:4c42ec:8", "const:4:8"]]
- 004c42ec ["CALL", null, ["callee:00c57b10:8"]]
+ 004e7184 ["INT_ADD", "register:40f0:8", ["const:4e7184:8", "const:4:8"]]
+ 004e7184 ["CALL", null, ["callee:00c57b10:8"]]
- 004c42ec bytes 755b1c94
+ 004e7184 bytes 63c21d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56c1fef585626cb8a737bc314c42af32"></a>

### [`004c476c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c476c.md) → [`004e7604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md) _ZN5Botan16get_sig_paddingsENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf80.md) · 呼出先 5件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00522664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522664.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c589d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589d0.md) · 呼出先 5件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`005454fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005454fc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004e763c",
      "incomplete_value": true,
      "site": "004e763c",
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
      "definition_site": "004c47a4",
      "incomplete_value": true,
      "site": "004c47a4",
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
      "definition_site": "004e7708",
      "incomplete_value": false,
      "site": "004e7714",
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
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4870",
      "incomplete_value": false,
      "site": "004c487c",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e7790",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c48f8",
      "value": [
        "leaf",
        "ram:41fdf0:8"
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
      "004e7638",
      "READ",
      [
        "storage",
        "00c253b0",
        null,
        "undefined8"
      ]
    ],
    [
      "004e7708",
      "PARAM",
      [
        "storage",
        "00c253a8",
        null,
        null
      ]
    ],
    [
      "004e778c",
      "PARAM",
      [
        "storage",
        "00290bae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e7638",
      "READ",
      [
        "storage",
        "00ca4e70",
        null,
        "undefined8"
      ]
    ],
    [
      "004e7708",
      "PARAM",
      [
        "storage",
        "00ca4e68",
        null,
        null
      ]
    ],
    [
      "004e778c",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c487c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c476c.md#insn-004c487c) · [`004c48f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c476c.md#insn-004c48f8) · [`004c479c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c476c.md#insn-004c479c)
- 新版 [`004e7714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md#insn-004e7714) · [`004e7790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md#insn-004e7790) · [`004e7634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md#insn-004e7634)

~~~diff
- 004c487c ["INT_ADD", "register:40f0:8", ["const:4c487c:8", "const:4:8"]]
- 004c487c ["CALL", null, ["callee:005454fc:8"]]
+ 004e7714 ["INT_ADD", "register:40f0:8", ["const:4e7714:8", "const:4:8"]]
+ 004e7714 ["CALL", null, ["callee:005454fc:8"]]
- 004c487c bytes 7a770194
+ 004e7714 bytes 7a770194
- 004c48f8 ["INT_ADD", "register:40f0:8", ["const:4c48f8:8", "const:4:8"]]
- 004c48f8 ["CALL", null, ["ram:41fdf0:8"]]
+ 004e7790 ["INT_ADD", "register:40f0:8", ["const:4e7790:8", "const:4:8"]]
+ 004e7790 ["CALL", null, ["ram:4428f0:8"]]
- 004c48f8 bytes 3e6dfd97
+ 004e7790 bytes 586cfd97
- 004c479c ["COPY", "register:4048:8", ["const:c25000:8"]]
+ 004e7634 ["COPY", "register:4048:8", ["const:ca4000:8"]]
- 004c479c bytes 093b00b0
+ 004e7634 bytes e93d00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-049333215425a73cbbbe6eb0131702f5"></a>

### [`004c4900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4900.md) → [`004e7798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7798.md) _ZN5Botan7BlinderC2ERKNS_6BigIntERNS_21RandomNumberGeneratorENSt6__ndk18functionIFS1_S3_EEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdd140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd140.md) · 呼出先 6件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc490.md) [`00bdc500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc500.md)
- 新版 呼出元 1件 [`00c59b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b90.md) · 呼出先 6件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ee0.md) [`00c58f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f50.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.90% / 新版 95.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e77d4",
      "value": [
        "leaf",
        "ram:c58ee0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c493c",
      "value": [
        "leaf",
        "ram:bdc490:8"
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
      "site": "004e7910",
      "value": [
        "leaf",
        "ram:c58f50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c4a78",
      "value": [
        "leaf",
        "ram:bdc500:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e7990",
      "incomplete_value": true,
      "site": "004e7990",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c4af8",
      "incomplete_value": true,
      "site": "004c4af8",
      "value": [
        "LOAD",
        "8",
        [
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
      "004e77d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc490"
      ]
    ],
    [
      "004e7910",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc500"
      ]
    ],
    [
      "004e7980",
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
      "004e77d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58ee0"
      ]
    ],
    [
      "004e7910",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58f50"
      ]
    ],
    [
      "004e7980",
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

- 旧版 [`004c493c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4900.md#insn-004c493c) · [`004c4a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4900.md#insn-004c4a78) · [`004c4af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4900.md#insn-004c4af8)
- 新版 [`004e77d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7798.md#insn-004e77d4) · [`004e7910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7798.md#insn-004e7910) · [`004e7990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7798.md#insn-004e7990)

~~~diff
- 004c493c ["INT_ADD", "register:40f0:8", ["const:4c493c:8", "const:4:8"]]
- 004c493c ["CALL", null, ["ram:bdc490:8"]]
+ 004e77d4 ["INT_ADD", "register:40f0:8", ["const:4e77d4:8", "const:4:8"]]
+ 004e77d4 ["CALL", null, ["ram:c58ee0:8"]]
- 004c493c bytes d55e1c94
+ 004e77d4 bytes c3c51d94
- 004c4a78 ["INT_ADD", "register:40f0:8", ["const:4c4a78:8", "const:4:8"]]
- 004c4a78 ["CALL", null, ["ram:bdc500:8"]]
+ 004e7910 ["INT_ADD", "register:40f0:8", ["const:4e7910:8", "const:4:8"]]
+ 004e7910 ["CALL", null, ["ram:c58f50:8"]]
- 004c4a78 bytes a25e1c94
+ 004e7910 bytes 90c51d94
- 004c4af8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c4af8 ["INT_ADD", "register:40f0:8", ["const:4c4af8:8", "const:4:8"]]
- 004c4af8 ["CALLIND", null, ["register:0:8"]]
+ 004e7990 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e7990 ["INT_ADD", "register:40f0:8", ["const:4e7990:8", "const:4:8"]]
+ 004e7990 ["CALLIND", null, ["register:0:8"]]
- 004c4af8 bytes 20013fd6
+ 004e7990 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b6861dba66097964da50036721ce93b"></a>

### [`004c4ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4ce8.md) → [`004e7b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7b80.md) _ZNK5Botan7Blinder5blindERKNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc700.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c59150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59150.md) · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.92% / 新版 91.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 9件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004e7be8",
      "value": [
        "leaf",
        "ram:c58f50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c4d50",
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
      "definition_site": "004e7c68",
      "incomplete_value": true,
      "site": "004e7c68",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c4dd0",
      "incomplete_value": true,
      "site": "004c4dd0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004e7cf0",
      "incomplete_value": true,
      "site": "004e7cf0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c4e58",
      "incomplete_value": true,
      "site": "004c4e58",
      "value": [
        "LOAD",
        "8",
        [
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
      "004e7be8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc500"
      ]
    ],
    [
      "004e7c58",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e7ce0",
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
      "004e7be8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58f50"
      ]
    ],
    [
      "004e7c58",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e7ce0",
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

- 旧版 [`004c4d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4ce8.md#insn-004c4d50) · [`004c4dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4ce8.md#insn-004c4dd0) · [`004c4e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4ce8.md#insn-004c4e58)
- 新版 [`004e7be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7b80.md#insn-004e7be8) · [`004e7c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7b80.md#insn-004e7c68) · [`004e7cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7b80.md#insn-004e7cf0)

~~~diff
- 004c4d50 ["INT_ADD", "register:40f0:8", ["const:4c4d50:8", "const:4:8"]]
- 004c4d50 ["CALL", null, ["ram:bdc500:8"]]
+ 004e7be8 ["INT_ADD", "register:40f0:8", ["const:4e7be8:8", "const:4:8"]]
+ 004e7be8 ["CALL", null, ["ram:c58f50:8"]]
- 004c4d50 bytes ec5d1c94
+ 004e7be8 bytes dac41d94
- 004c4dd0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c4dd0 ["INT_ADD", "register:40f0:8", ["const:4c4dd0:8", "const:4:8"]]
- 004c4dd0 ["CALLIND", null, ["register:0:8"]]
+ 004e7c68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e7c68 ["INT_ADD", "register:40f0:8", ["const:4e7c68:8", "const:4:8"]]
+ 004e7c68 ["CALLIND", null, ["register:0:8"]]
- 004c4dd0 bytes 20013fd6
+ 004e7c68 bytes 20013fd6
- 004c4e58 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c4e58 ["INT_ADD", "register:40f0:8", ["const:4c4e58:8", "const:4:8"]]
- 004c4e58 ["CALLIND", null, ["register:0:8"]]
+ 004e7cf0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e7cf0 ["INT_ADD", "register:40f0:8", ["const:4e7cf0:8", "const:4:8"]]
+ 004e7cf0 ["CALLIND", null, ["register:0:8"]]
- 004c4e58 bytes 20013fd6
+ 004e7cf0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36004ef7f4ea145be0d460668d5afb30"></a>

### [`004c5180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5180.md) → [`004e8018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8018.md) _ZNK5Botan7Blinder7unblindERKNS_6BigIntE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc710.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c59160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59160.md) · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

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
      "definition_site": "004e8090",
      "incomplete_value": true,
      "site": "004e8090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c51f8",
      "incomplete_value": true,
      "site": "004c51f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004e80d0",
      "incomplete_value": false,
      "site": "004e80d8",
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
            "const:852:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5238",
      "incomplete_value": false,
      "site": "004c5240",
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
            "const:4cd:8"
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
      "definition_site": "004e8108",
      "incomplete_value": true,
      "site": "004e8114",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c5270",
      "incomplete_value": true,
      "site": "004c527c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e8080",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004e80d0",
      "PARAM",
      [
        "storage",
        "0029e4cd",
        null,
        "string"
      ]
    ],
    [
      "004e8104",
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
      "004e8080",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e80d0",
      "PARAM",
      [
        "storage",
        "002ae852",
        null,
        "string"
      ]
    ],
    [
      "004e8104",
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

- 旧版 [`004c51f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5180.md#insn-004c51f8) · [`004c5240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5180.md#insn-004c5240) · [`004c527c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5180.md#insn-004c527c)
- 新版 [`004e8090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8018.md#insn-004e8090) · [`004e80d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8018.md#insn-004e80d8) · [`004e8114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8018.md#insn-004e8114)

~~~diff
- 004c51f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c51f8 ["INT_ADD", "register:40f0:8", ["const:4c51f8:8", "const:4:8"]]
- 004c51f8 ["CALLIND", null, ["register:0:8"]]
+ 004e8090 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e8090 ["INT_ADD", "register:40f0:8", ["const:4e8090:8", "const:4:8"]]
+ 004e8090 ["CALLIND", null, ["register:0:8"]]
- 004c51f8 bytes 20013fd6
+ 004e8090 bytes 20013fd6
- 004c5240 ["INT_ADD", "register:40f0:8", ["const:4c5240:8", "const:4:8"]]
- 004c5240 ["CALL", null, ["callee:0043dd98:8"]]
+ 004e80d8 ["INT_ADD", "register:40f0:8", ["const:4e80d8:8", "const:4:8"]]
+ 004e80d8 ["CALL", null, ["callee:0043dd98:8"]]
- 004c5240 bytes 1658fd97
+ 004e80d8 bytes 3057fd97
- 004c527c ["INT_ADD", "register:40f0:8", ["const:4c527c:8", "const:4:8"]]
- 004c527c ["CALL", null, ["callee:00c57b10:8"]]
+ 004e8114 ["INT_ADD", "register:40f0:8", ["const:4e8114:8", "const:4:8"]]
+ 004e8114 ["CALL", null, ["callee:00c57b10:8"]]
- 004c527c bytes 91571c94
+ 004e8114 bytes 7fbe1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e29af643f167340901b6d8b72bbd5a45"></a>

### [`004c52e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c52e0.md) → [`004e8178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md) _ZN5Botan15load_public_keyERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS3_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc720.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md) [`00524c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c98.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c59170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59170.md) · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e81b8",
      "incomplete_value": false,
      "site": "004e81c0",
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
      "definition_site": "004c5320",
      "incomplete_value": false,
      "site": "004c5328",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e8350",
      "incomplete_value": false,
      "site": "004e835c",
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
            "const:c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c54b8",
      "incomplete_value": false,
      "site": "004c54c4",
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
            "const:a9d:8"
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
      "definition_site": "004e838c",
      "incomplete_value": true,
      "site": "004e8398",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c54f4",
      "incomplete_value": true,
      "site": "004c5500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e81c0",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e8204",
      "READ",
      [
        "storage",
        "00bed710",
        null,
        "pointer"
      ]
    ],
    [
      "004e8204",
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
      "004e81c0",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e8204",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004e8204",
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

- 旧版 [`004c54c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c52e0.md#insn-004c54c4) · [`004c5500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c52e0.md#insn-004c5500) · [`004c5530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c52e0.md#insn-004c5530)
- 新版 [`004e835c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md#insn-004e835c) · [`004e8398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md#insn-004e8398) · [`004e83c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md#insn-004e83c8)

~~~diff
- 004c54c4 ["INT_ADD", "register:40f0:8", ["const:4c54c4:8", "const:4:8"]]
- 004c54c4 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004e835c ["INT_ADD", "register:40f0:8", ["const:4e835c:8", "const:4:8"]]
+ 004e835c ["CALL", null, ["callee:00c57cb0:8"]]
- 004c54c4 bytes 67571c94
+ 004e835c bytes 55be1d94
- 004c5500 ["INT_ADD", "register:40f0:8", ["const:4c5500:8", "const:4:8"]]
- 004c5500 ["CALL", null, ["callee:00c57b10:8"]]
+ 004e8398 ["INT_ADD", "register:40f0:8", ["const:4e8398:8", "const:4:8"]]
+ 004e8398 ["CALL", null, ["callee:00c57b10:8"]]
- 004c5500 bytes f0561c94
+ 004e8398 bytes debd1d94
- 004c5530 ["INT_ADD", "register:40f0:8", ["const:4c5530:8", "const:4:8"]]
- 004c5530 ["CALL", null, ["callee:00c57b60:8"]]
+ 004e83c8 ["INT_ADD", "register:40f0:8", ["const:4e83c8:8", "const:4:8"]]
+ 004e83c8 ["CALL", null, ["callee:00c57b60:8"]]
- 004c5530 bytes f8561c94
+ 004e83c8 bytes e6bd1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97b4ef97fd52e7590a09a668e080c257"></a>

### [`004c56b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c56b0.md) → [`004e8548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8548.md) _ZN5Botan13RSA_PublicKeyC1ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc730.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) [`00bdb8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8c0.md) [`00bdba30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba30.md)
- 新版 呼出元 1件 [`00c59180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59180.md) · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) [`00c58310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58310.md) [`00c58480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58480.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8578",
      "incomplete_value": true,
      "site": "004e8580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c56e0",
      "incomplete_value": true,
      "site": "004c56e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:80:8"
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
      "site": "004e85a4",
      "value": [
        "leaf",
        "ram:c58480:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c570c",
      "value": [
        "leaf",
        "ram:bdba30:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e8628",
      "incomplete_value": true,
      "site": "004e8628",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "definition_site": "004c5790",
      "incomplete_value": true,
      "site": "004c5790",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "004e8568",
      "READ",
      [
        "storage",
        "00c1b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "004e8580",
      "DATA",
      [
        "storage",
        "00bea0e8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "004e85a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdba30"
      ]
    ]
  ],
  "added": [
    [
      "004e8568",
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      "004e8580",
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "004e85a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58480"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c570c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c56b0.md#insn-004c570c) · [`004c5790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c56b0.md#insn-004c5790) · [`004c57d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c56b0.md#insn-004c57d4)
- 新版 [`004e85a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8548.md#insn-004e85a4) · [`004e8628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8548.md#insn-004e8628) · [`004e866c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8548.md#insn-004e866c)

~~~diff
- 004c570c ["INT_ADD", "register:40f0:8", ["const:4c570c:8", "const:4:8"]]
- 004c570c ["CALL", null, ["ram:bdba30:8"]]
+ 004e85a4 ["INT_ADD", "register:40f0:8", ["const:4e85a4:8", "const:4:8"]]
+ 004e85a4 ["CALL", null, ["ram:c58480:8"]]
- 004c570c bytes c9581c94
+ 004e85a4 bytes b7bf1d94
- 004c5790 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c5790 ["INT_ADD", "register:40f0:8", ["const:4c5790:8", "const:4:8"]]
- 004c5790 ["CALLIND", null, ["register:0:8"]]
+ 004e8628 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e8628 ["INT_ADD", "register:40f0:8", ["const:4e8628:8", "const:4:8"]]
+ 004e8628 ["CALLIND", null, ["register:0:8"]]
- 004c5790 bytes 20013fd6
+ 004e8628 bytes 20013fd6
- 004c57d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c57d4 ["INT_ADD", "register:40f0:8", ["const:4c57d4:8", "const:4:8"]]
- 004c57d4 ["CALLIND", null, ["register:0:8"]]
+ 004e866c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e866c ["INT_ADD", "register:40f0:8", ["const:4e866c:8", "const:4:8"]]
+ 004e866c ["CALLIND", null, ["register:0:8"]]
- 004c57d4 bytes 20013fd6
+ 004e866c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8661ad584d8aa9d416ed12791f81d2e6"></a>

### [`004c585c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c585c.md) → [`004e86f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e86f4.md) _ZN5Botan16load_private_keyERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc740.md) · 呼出先 12件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c59190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59190.md) · 呼出先 12件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

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
      "definition_site": "004e87e8",
      "incomplete_value": false,
      "site": "004e87f4",
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
            "const:b62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5950",
      "incomplete_value": false,
      "site": "004c595c",
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
            "const:5a8:8"
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
      "definition_site": "004e883c",
      "incomplete_value": true,
      "site": "004e8848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c59a4",
      "incomplete_value": true,
      "site": "004c59b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e8838",
      "incomplete_value": false,
      "site": "004e8848",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004c59a0",
      "incomplete_value": false,
      "site": "004c59b0",
      "value": [
        "leaf",
        "const:512990:8"
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e87e8",
      "PARAM",
      [
        "storage",
        "002a05a8",
        null,
        "string"
      ]
    ],
    [
      "004e8838",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004e883c",
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
      "004e87e8",
      "PARAM",
      [
        "storage",
        "002b0b62",
        null,
        "string"
      ]
    ],
    [
      "004e8838",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004e883c",
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

- 旧版 [`004c595c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c585c.md#insn-004c595c) · [`004c59b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c585c.md#insn-004c59b0) · [`004c59d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c585c.md#insn-004c59d4)
- 新版 [`004e87f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e86f4.md#insn-004e87f4) · [`004e8848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e86f4.md#insn-004e8848) · [`004e886c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e86f4.md#insn-004e886c)

~~~diff
- 004c595c ["INT_ADD", "register:40f0:8", ["const:4c595c:8", "const:4:8"]]
- 004c595c ["CALL", null, ["callee:00c57b60:8"]]
+ 004e87f4 ["INT_ADD", "register:40f0:8", ["const:4e87f4:8", "const:4:8"]]
+ 004e87f4 ["CALL", null, ["callee:00c57b60:8"]]
- 004c595c bytes ed551c94
+ 004e87f4 bytes dbbc1d94
- 004c59b0 ["INT_ADD", "register:40f0:8", ["const:4c59b0:8", "const:4:8"]]
- 004c59b0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004e8848 ["INT_ADD", "register:40f0:8", ["const:4e8848:8", "const:4:8"]]
+ 004e8848 ["CALL", null, ["callee:00c57b10:8"]]
- 004c59b0 bytes c4551c94
+ 004e8848 bytes b2bc1d94
- 004c59d4 ["INT_ADD", "register:40f0:8", ["const:4c59d4:8", "const:4:8"]]
- 004c59d4 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004e886c ["INT_ADD", "register:40f0:8", ["const:4e886c:8", "const:4:8"]]
+ 004e886c ["CALL", null, ["callee:00c57cb0:8"]]
- 004c59d4 bytes 23561c94
+ 004e886c bytes 11bd1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0492c30293344af01405a80006a1d29"></a>

### [`004c5ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5ac8.md) → [`004e8960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8960.md) _ZN5Botan14RSA_PrivateKeyC1ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc750.md) · 呼出先 14件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c591a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591a0.md) · 呼出先 14件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.06% / 新版 90.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e89d0",
      "incomplete_value": true,
      "site": "004e89d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5b38",
      "incomplete_value": true,
      "site": "004c5b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1a0:8"
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
      "definition_site": "004e89ac",
      "incomplete_value": true,
      "site": "004e89ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5b14",
      "incomplete_value": true,
      "site": "004c5b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:80:8"
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
      "definition_site": "004e8a68",
      "incomplete_value": true,
      "site": "004e8a7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004c5bd0",
      "incomplete_value": true,
      "site": "004c5be4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "004e898c",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "004e89d0",
      "DATA",
      [
        "storage",
        "00bea2f8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004e89ec",
      "DATA",
      [
        "storage",
        "00bea1d8",
        null,
        "undefined1[528]"
      ]
    ]
  ],
  "added": [
    [
      "004e898c",
      "READ",
      [
        "storage",
        "00c9abe0",
        null,
        "pointer"
      ]
    ],
    [
      "004e89d0",
      "DATA",
      [
        "storage",
        "00c66eb8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004e89ec",
      "DATA",
      [
        "storage",
        "00c66d98",
        null,
        "undefined1[528]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5ac8.md#insn-004c5ba0) · [`004c5cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5ac8.md#insn-004c5cd4) · [`004c5d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5ac8.md#insn-004c5d18)
- 新版 [`004e8a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8960.md#insn-004e8a38) · [`004e8b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8960.md#insn-004e8b6c) · [`004e8bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8960.md#insn-004e8bb0)

~~~diff
- 004c5ba0 ["INT_ADD", "register:40f0:8", ["const:4c5ba0:8", "const:4:8"]]
- 004c5ba0 ["CALL", null, ["ram:bdba40:8"]]
+ 004e8a38 ["INT_ADD", "register:40f0:8", ["const:4e8a38:8", "const:4:8"]]
+ 004e8a38 ["CALL", null, ["ram:c58490:8"]]
- 004c5ba0 bytes a8571c94
+ 004e8a38 bytes 96be1d94
- 004c5cd4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c5cd4 ["INT_ADD", "register:40f0:8", ["const:4c5cd4:8", "const:4:8"]]
- 004c5cd4 ["CALLIND", null, ["register:0:8"]]
+ 004e8b6c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e8b6c ["INT_ADD", "register:40f0:8", ["const:4e8b6c:8", "const:4:8"]]
+ 004e8b6c ["CALLIND", null, ["register:0:8"]]
- 004c5cd4 bytes 20013fd6
+ 004e8b6c bytes 20013fd6
- 004c5d18 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c5d18 ["INT_ADD", "register:40f0:8", ["const:4c5d18:8", "const:4:8"]]
- 004c5d18 ["CALLIND", null, ["register:0:8"]]
+ 004e8bb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e8bb0 ["INT_ADD", "register:40f0:8", ["const:4e8bb0:8", "const:4:8"]]
+ 004e8bb0 ["CALLIND", null, ["register:0:8"]]
- 004c5d18 bytes 20013fd6
+ 004e8bb0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f5645f5046d91c81afdd46b63097694"></a>

### [`004c5f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5f28.md) → [`004e8dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8dc0.md) _ZN5Botan14RSA_PrivateKeyC1ERNS_21RandomNumberGeneratorEmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc760.md) · 呼出先 17件 [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c591b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591b0.md) · 呼出先 17件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.41% / 新版 98.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8e10",
      "incomplete_value": true,
      "site": "004e8e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5f78",
      "incomplete_value": true,
      "site": "004c5f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:80:8"
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
      "definition_site": "004e8e30",
      "incomplete_value": true,
      "site": "004e8e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5f98",
      "incomplete_value": true,
      "site": "004c5f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e8f30",
      "incomplete_value": true,
      "site": "004e8f30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c6098",
      "incomplete_value": true,
      "site": "004c6098",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e8dfc",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "004e8e18",
      "DATA",
      [
        "storage",
        "00bea1d8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004e8e30",
      "DATA",
      [
        "storage",
        "00bea2f8",
        null,
        "undefined1[528]"
      ]
    ]
  ],
  "added": [
    [
      "004e8dfc",
      "READ",
      [
        "storage",
        "00c9abe0",
        null,
        "pointer"
      ]
    ],
    [
      "004e8e18",
      "DATA",
      [
        "storage",
        "00c66d98",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004e8e30",
      "DATA",
      [
        "storage",
        "00c66eb8",
        null,
        "undefined1[528]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c6098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5f28.md#insn-004c6098) · [`004c6138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5f28.md#insn-004c6138) · [`004c6234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c5/004c5f28.md#insn-004c6234)
- 新版 [`004e8f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8dc0.md#insn-004e8f30) · [`004e8fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8dc0.md#insn-004e8fd0) · [`004e90cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8dc0.md#insn-004e90cc)

~~~diff
- 004c6098 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c6098 ["INT_ADD", "register:40f0:8", ["const:4c6098:8", "const:4:8"]]
- 004c6098 ["CALLIND", null, ["register:0:8"]]
+ 004e8f30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e8f30 ["INT_ADD", "register:40f0:8", ["const:4e8f30:8", "const:4:8"]]
+ 004e8f30 ["CALLIND", null, ["register:0:8"]]
- 004c6098 bytes 20013fd6
+ 004e8f30 bytes 20013fd6
- 004c6138 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c6138 ["INT_ADD", "register:40f0:8", ["const:4c6138:8", "const:4:8"]]
- 004c6138 ["CALLIND", null, ["register:0:8"]]
+ 004e8fd0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e8fd0 ["INT_ADD", "register:40f0:8", ["const:4e8fd0:8", "const:4:8"]]
+ 004e8fd0 ["CALLIND", null, ["register:0:8"]]
- 004c6138 bytes 20013fd6
+ 004e8fd0 bytes 20013fd6
- 004c6234 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c6234 ["INT_ADD", "register:40f0:8", ["const:4c6234:8", "const:4:8"]]
- 004c6234 ["CALLIND", null, ["register:0:8"]]
+ 004e90cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e90cc ["INT_ADD", "register:40f0:8", ["const:4e90cc:8", "const:4:8"]]
+ 004e90cc ["CALLIND", null, ["register:0:8"]]
- 004c6234 bytes 20013fd6
+ 004e90cc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae3c75e5d4428634283deaabe015cba1"></a>

### [`004c734c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c734c.md) → [`004ea1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea1e4.md) FUN_004ea1e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

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
      "definition_site": "004ea200",
      "incomplete_value": true,
      "site": "004ea200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c7368",
      "incomplete_value": true,
      "site": "004c7368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004ea234",
      "incomplete_value": true,
      "site": "004ea238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c739c",
      "incomplete_value": true,
      "site": "004c73a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "004ea1f8",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea200",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004ea230",
      "READ",
      [
        "storage",
        "00c1b200",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ea1f8",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea200",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004ea230",
      "READ",
      [
        "storage",
        "00c9abf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c734c.md#insn-004c7358) · [`004c7360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c734c.md#insn-004c7360) · [`004c7390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c734c.md#insn-004c7390)
- 新版 [`004ea1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea1e4.md#insn-004ea1f0) · [`004ea1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea1e4.md#insn-004ea1f8) · [`004ea228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea1e4.md#insn-004ea228)

~~~diff
- 004c7358 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004ea1f0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004c7358 bytes 883a00f0
+ 004ea1f0 bytes 883d0090
- 004c7360 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
- 004c7360 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea1f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 004ea1f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7360 bytes 08f147f9
+ 004ea1f8 bytes 08e944f9
- 004c7390 ["INT_ADD", "register:40f0:8", ["const:4c7390:8", "const:4:8"]]
- 004c7390 ["CALL", null, ["callee:0043bae0:8"]]
+ 004ea228 ["INT_ADD", "register:40f0:8", ["const:4ea228:8", "const:4:8"]]
+ 004ea228 ["CALL", null, ["callee:0043bae0:8"]]
- 004c7390 bytes 1447fd97
+ 004ea228 bytes 2e46fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61c0ea364db60378d0dee01508056933"></a>

### [`004c73c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c73c4.md) → [`004ea25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea25c.md) _ZNK5Botan11Private_Key16private_key_infoEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc790.md) · 呼出先 11件 [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md)
- 新版 呼出元 1件 [`00c591e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591e0.md) · 呼出先 11件 [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.04% / 新版 95.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ea2e8",
      "incomplete_value": true,
      "site": "004ea2e8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c7450",
      "incomplete_value": true,
      "site": "004c7450",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c74e4",
      "incomplete_value": true,
      "site": "004c74e4",
      "value": [
        "LOAD",
        "8",
        [
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ea408",
      "incomplete_value": true,
      "site": "004ea408",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c7570",
      "incomplete_value": true,
      "site": "004c7570",
      "value": [
        "LOAD",
        "8",
        [
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
      "004ea2d8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004ea36c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004ea3f8",
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
      "004ea2d8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ea36c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ea3f8",
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

- 旧版 [`004c7450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c73c4.md#insn-004c7450) · [`004c74e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c73c4.md#insn-004c74e4) · [`004c7570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c73c4.md#insn-004c7570)
- 新版 [`004ea2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea25c.md#insn-004ea2e8) · [`004ea37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea25c.md#insn-004ea37c) · [`004ea408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea25c.md#insn-004ea408)

~~~diff
- 004c7450 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c7450 ["INT_ADD", "register:40f0:8", ["const:4c7450:8", "const:4:8"]]
- 004c7450 ["CALLIND", null, ["register:0:8"]]
+ 004ea2e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ea2e8 ["INT_ADD", "register:40f0:8", ["const:4ea2e8:8", "const:4:8"]]
+ 004ea2e8 ["CALLIND", null, ["register:0:8"]]
- 004c7450 bytes 20013fd6
+ 004ea2e8 bytes 20013fd6
- 004c74e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c74e4 ["INT_ADD", "register:40f0:8", ["const:4c74e4:8", "const:4:8"]]
- 004c74e4 ["CALLIND", null, ["register:0:8"]]
+ 004ea37c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ea37c ["INT_ADD", "register:40f0:8", ["const:4ea37c:8", "const:4:8"]]
+ 004ea37c ["CALLIND", null, ["register:0:8"]]
- 004c74e4 bytes 20013fd6
+ 004ea37c bytes 20013fd6
- 004c7570 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c7570 ["INT_ADD", "register:40f0:8", ["const:4c7570:8", "const:4:8"]]
- 004c7570 ["CALLIND", null, ["register:0:8"]]
+ 004ea408 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ea408 ["INT_ADD", "register:40f0:8", ["const:4ea408:8", "const:4:8"]]
+ 004ea408 ["CALLIND", null, ["register:0:8"]]
- 004c7570 bytes 20013fd6
+ 004ea408 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e87e9050b441b3ffb4942fb2d7b9647"></a>

### [`004c7790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7790.md) → [`004ea628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea628.md) _ZNK5Botan10Public_Key20create_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.80% / 新版 91.80%

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
      "definition_site": "004ea6b0",
      "incomplete_value": true,
      "site": "004ea6b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c7818",
      "incomplete_value": true,
      "site": "004c7818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004ea6e8",
      "incomplete_value": true,
      "site": "004ea6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c7850",
      "incomplete_value": true,
      "site": "004c7854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ea674",
      "incomplete_value": false,
      "site": "004ea67c",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c77dc",
      "incomplete_value": false,
      "site": "004c77e4",
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
            "const:a02:8"
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
      "004ea674",
      "PARAM",
      [
        "storage",
        "002ada02",
        null,
        "string"
      ]
    ],
    [
      "004ea69c",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea6b0",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004ea674",
      "PARAM",
      [
        "storage",
        "002bed28",
        null,
        "string"
      ]
    ],
    [
      "004ea69c",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea6b0",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c77e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7790.md#insn-004c77e4) · [`004c787c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7790.md#insn-004c787c) · [`004c77bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7790.md#insn-004c77bc)
- 新版 [`004ea67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea628.md#insn-004ea67c) · [`004ea714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea628.md#insn-004ea714) · [`004ea654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea628.md#insn-004ea654)

~~~diff
- 004c77e4 ["INT_ADD", "register:40f0:8", ["const:4c77e4:8", "const:4:8"]]
- 004c77e4 ["CALL", null, ["callee:00c57b70:8"]]
+ 004ea67c ["INT_ADD", "register:40f0:8", ["const:4ea67c:8", "const:4:8"]]
+ 004ea67c ["CALL", null, ["callee:00c57b70:8"]]
- 004c77e4 bytes 4f4e1c94
+ 004ea67c bytes 3db51d94
- 004c787c ["INT_ADD", "register:40f0:8", ["const:4c787c:8", "const:4:8"]]
- 004c787c ["CALL", null, ["callee:00c57b10:8"]]
+ 004ea714 ["INT_ADD", "register:40f0:8", ["const:4ea714:8", "const:4:8"]]
+ 004ea714 ["CALL", null, ["callee:00c57b10:8"]]
- 004c787c bytes 114e1c94
+ 004ea714 bytes ffb41d94
- 004c77bc ["INT_ADD", "register:40f0:8", ["const:4c77bc:8", "const:4:8"]]
- 004c77bc ["CALL", null, ["callee:00c57af0:8"]]
+ 004ea654 ["INT_ADD", "register:40f0:8", ["const:4ea654:8", "const:4:8"]]
+ 004ea654 ["CALL", null, ["callee:00c57af0:8"]]
- 004c77bc bytes 394e1c94
+ 004ea654 bytes 27b51d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8a5348ccfba1b056372c9f081acb54f"></a>

### [`004c7914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7914.md) → [`004ea7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea7ac.md) _ZNK5Botan10Public_Key24create_kem_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocator

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.80% / 新版 91.80%

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
      "definition_site": "004ea834",
      "incomplete_value": true,
      "site": "004ea834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c799c",
      "incomplete_value": true,
      "site": "004c799c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004ea86c",
      "incomplete_value": true,
      "site": "004ea870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c79d4",
      "incomplete_value": true,
      "site": "004c79d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ea7f8",
      "incomplete_value": false,
      "site": "004ea800",
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
            "const:abc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7960",
      "incomplete_value": false,
      "site": "004c7968",
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
            "const:3e2:8"
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
      "004ea7f8",
      "PARAM",
      [
        "storage",
        "002a33e2",
        null,
        "string"
      ]
    ],
    [
      "004ea820",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea834",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004ea7f8",
      "PARAM",
      [
        "storage",
        "002b3abc",
        null,
        "string"
      ]
    ],
    [
      "004ea820",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea834",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7914.md#insn-004c7968) · [`004c7a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7914.md#insn-004c7a00) · [`004c7940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7914.md#insn-004c7940)
- 新版 [`004ea800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea7ac.md#insn-004ea800) · [`004ea898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea7ac.md#insn-004ea898) · [`004ea7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea7ac.md#insn-004ea7d8)

~~~diff
- 004c7968 ["INT_ADD", "register:40f0:8", ["const:4c7968:8", "const:4:8"]]
- 004c7968 ["CALL", null, ["callee:00c57b70:8"]]
+ 004ea800 ["INT_ADD", "register:40f0:8", ["const:4ea800:8", "const:4:8"]]
+ 004ea800 ["CALL", null, ["callee:00c57b70:8"]]
- 004c7968 bytes ee4d1c94
+ 004ea800 bytes dcb41d94
- 004c7a00 ["INT_ADD", "register:40f0:8", ["const:4c7a00:8", "const:4:8"]]
- 004c7a00 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ea898 ["INT_ADD", "register:40f0:8", ["const:4ea898:8", "const:4:8"]]
+ 004ea898 ["CALL", null, ["callee:00c57b10:8"]]
- 004c7a00 bytes b04d1c94
+ 004ea898 bytes 9eb41d94
- 004c7940 ["INT_ADD", "register:40f0:8", ["const:4c7940:8", "const:4:8"]]
- 004c7940 ["CALL", null, ["callee:00c57af0:8"]]
+ 004ea7d8 ["INT_ADD", "register:40f0:8", ["const:4ea7d8:8", "const:4:8"]]
+ 004ea7d8 ["CALL", null, ["callee:00c57af0:8"]]
- 004c7940 bytes d84d1c94
+ 004ea7d8 bytes c6b41d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d328deef06657da9ac7703a05f76a4b"></a>

### [`004c7a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7a98.md) → [`004ea930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea930.md) _ZNK5Botan10Public_Key22create_verification_opERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.80% / 新版 91.80%

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
      "definition_site": "004ea9b8",
      "incomplete_value": true,
      "site": "004ea9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c7b20",
      "incomplete_value": true,
      "site": "004c7b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004ea9f0",
      "incomplete_value": true,
      "site": "004ea9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c7b58",
      "incomplete_value": true,
      "site": "004c7b5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ea97c",
      "incomplete_value": false,
      "site": "004ea984",
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
            "const:569:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7ae4",
      "incomplete_value": false,
      "site": "004c7aec",
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
            "const:a34:8"
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
      "004ea97c",
      "PARAM",
      [
        "storage",
        "00296a34",
        null,
        "string"
      ]
    ],
    [
      "004ea9a4",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea9b8",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004ea97c",
      "PARAM",
      [
        "storage",
        "002a6569",
        null,
        "string"
      ]
    ],
    [
      "004ea9a4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea9b8",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7a98.md#insn-004c7aec) · [`004c7b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7a98.md#insn-004c7b84) · [`004c7ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7a98.md#insn-004c7ac4)
- 新版 [`004ea984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea930.md#insn-004ea984) · [`004eaa1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea930.md#insn-004eaa1c) · [`004ea95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea930.md#insn-004ea95c)

~~~diff
- 004c7aec ["INT_ADD", "register:40f0:8", ["const:4c7aec:8", "const:4:8"]]
- 004c7aec ["CALL", null, ["callee:00c57b70:8"]]
+ 004ea984 ["INT_ADD", "register:40f0:8", ["const:4ea984:8", "const:4:8"]]
+ 004ea984 ["CALL", null, ["callee:00c57b70:8"]]
- 004c7aec bytes 8d4d1c94
+ 004ea984 bytes 7bb41d94
- 004c7b84 ["INT_ADD", "register:40f0:8", ["const:4c7b84:8", "const:4:8"]]
- 004c7b84 ["CALL", null, ["callee:00c57b10:8"]]
+ 004eaa1c ["INT_ADD", "register:40f0:8", ["const:4eaa1c:8", "const:4:8"]]
+ 004eaa1c ["CALL", null, ["callee:00c57b10:8"]]
- 004c7b84 bytes 4f4d1c94
+ 004eaa1c bytes 3db41d94
- 004c7ac4 ["INT_ADD", "register:40f0:8", ["const:4c7ac4:8", "const:4:8"]]
- 004c7ac4 ["CALL", null, ["callee:00c57af0:8"]]
+ 004ea95c ["INT_ADD", "register:40f0:8", ["const:4ea95c:8", "const:4:8"]]
+ 004ea95c ["CALL", null, ["callee:00c57af0:8"]]
- 004c7ac4 bytes 774d1c94
+ 004ea95c bytes 65b41d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e46b0a21effab40b72d0733459d23cc"></a>

### [`004c7c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7c1c.md) → [`004eaab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaab4.md) _ZNK5Botan11Private_Key20create_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

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
      "definition_site": "004eab44",
      "incomplete_value": true,
      "site": "004eab44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c7cac",
      "incomplete_value": true,
      "site": "004c7cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004eab7c",
      "incomplete_value": true,
      "site": "004eab80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c7ce4",
      "incomplete_value": true,
      "site": "004c7ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eab08",
      "incomplete_value": false,
      "site": "004eab10",
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
            "const:add:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7c70",
      "incomplete_value": false,
      "site": "004c7c78",
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
            "const:403:8"
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
      "004eab08",
      "PARAM",
      [
        "storage",
        "002a3403",
        null,
        "string"
      ]
    ],
    [
      "004eab30",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004eab44",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004eab08",
      "PARAM",
      [
        "storage",
        "002b3add",
        null,
        "string"
      ]
    ],
    [
      "004eab30",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004eab44",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7c1c.md#insn-004c7c78) · [`004c7d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7c1c.md#insn-004c7d10) · [`004c7c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7c1c.md#insn-004c7c48)
- 新版 [`004eab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaab4.md#insn-004eab10) · [`004eaba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaab4.md#insn-004eaba8) · [`004eaae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaab4.md#insn-004eaae0)

~~~diff
- 004c7c78 ["INT_ADD", "register:40f0:8", ["const:4c7c78:8", "const:4:8"]]
- 004c7c78 ["CALL", null, ["callee:00c57b70:8"]]
+ 004eab10 ["INT_ADD", "register:40f0:8", ["const:4eab10:8", "const:4:8"]]
+ 004eab10 ["CALL", null, ["callee:00c57b70:8"]]
- 004c7c78 bytes 2a4d1c94
+ 004eab10 bytes 18b41d94
- 004c7d10 ["INT_ADD", "register:40f0:8", ["const:4c7d10:8", "const:4:8"]]
- 004c7d10 ["CALL", null, ["callee:00c57b10:8"]]
+ 004eaba8 ["INT_ADD", "register:40f0:8", ["const:4eaba8:8", "const:4:8"]]
+ 004eaba8 ["CALL", null, ["callee:00c57b10:8"]]
- 004c7d10 bytes ec4c1c94
+ 004eaba8 bytes dab31d94
- 004c7c48 ["INT_ADD", "register:40f0:8", ["const:4c7c48:8", "const:4:8"]]
- 004c7c48 ["CALL", null, ["callee:00c57af0:8"]]
+ 004eaae0 ["INT_ADD", "register:40f0:8", ["const:4eaae0:8", "const:4:8"]]
+ 004eaae0 ["CALL", null, ["callee:00c57af0:8"]]
- 004c7c48 bytes 164d1c94
+ 004eaae0 bytes 04b41d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ad57ede5b0a344fdccab368090bd92d"></a>

### [`004c7da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7da8.md) → [`004eac40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eac40.md) _ZNK5Botan11Private_Key24create_kem_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocato

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

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
      "definition_site": "004eacd0",
      "incomplete_value": true,
      "site": "004eacd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c7e38",
      "incomplete_value": true,
      "site": "004c7e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004ead08",
      "incomplete_value": true,
      "site": "004ead0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c7e70",
      "incomplete_value": true,
      "site": "004c7e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eac94",
      "incomplete_value": false,
      "site": "004eac9c",
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
            "const:253:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7dfc",
      "incomplete_value": false,
      "site": "004c7e04",
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
            "const:5b0:8"
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
      "004eac94",
      "PARAM",
      [
        "storage",
        "002a95b0",
        null,
        "string"
      ]
    ],
    [
      "004eacbc",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004eacd0",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004eac94",
      "PARAM",
      [
        "storage",
        "002ba253",
        null,
        "string"
      ]
    ],
    [
      "004eacbc",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004eacd0",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7da8.md#insn-004c7e04) · [`004c7e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7da8.md#insn-004c7e9c) · [`004c7dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7da8.md#insn-004c7dd4)
- 新版 [`004eac9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eac40.md#insn-004eac9c) · [`004ead34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eac40.md#insn-004ead34) · [`004eac6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eac40.md#insn-004eac6c)

~~~diff
- 004c7e04 ["INT_ADD", "register:40f0:8", ["const:4c7e04:8", "const:4:8"]]
- 004c7e04 ["CALL", null, ["callee:00c57b70:8"]]
+ 004eac9c ["INT_ADD", "register:40f0:8", ["const:4eac9c:8", "const:4:8"]]
+ 004eac9c ["CALL", null, ["callee:00c57b70:8"]]
- 004c7e04 bytes c74c1c94
+ 004eac9c bytes b5b31d94
- 004c7e9c ["INT_ADD", "register:40f0:8", ["const:4c7e9c:8", "const:4:8"]]
- 004c7e9c ["CALL", null, ["callee:00c57b10:8"]]
+ 004ead34 ["INT_ADD", "register:40f0:8", ["const:4ead34:8", "const:4:8"]]
+ 004ead34 ["CALL", null, ["callee:00c57b10:8"]]
- 004c7e9c bytes 894c1c94
+ 004ead34 bytes 77b31d94
- 004c7dd4 ["INT_ADD", "register:40f0:8", ["const:4c7dd4:8", "const:4:8"]]
- 004c7dd4 ["CALL", null, ["callee:00c57af0:8"]]
+ 004eac6c ["INT_ADD", "register:40f0:8", ["const:4eac6c:8", "const:4:8"]]
+ 004eac6c ["CALL", null, ["callee:00c57af0:8"]]
- 004c7dd4 bytes b34c1c94
+ 004eac6c bytes a1b31d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0adde386999c036893ecd6ce59f00f7a"></a>

### [`004c7f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7f34.md) → [`004eadcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eadcc.md) _ZNK5Botan11Private_Key19create_signature_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

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
      "definition_site": "004eae5c",
      "incomplete_value": true,
      "site": "004eae5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c7fc4",
      "incomplete_value": true,
      "site": "004c7fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004eae94",
      "incomplete_value": true,
      "site": "004eae98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c7ffc",
      "incomplete_value": true,
      "site": "004c8000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eae20",
      "incomplete_value": false,
      "site": "004eae28",
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
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7f88",
      "incomplete_value": false,
      "site": "004c7f90",
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
            "const:659:8"
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
      "004eae20",
      "PARAM",
      [
        "storage",
        "002a7659",
        null,
        "string"
      ]
    ],
    [
      "004eae48",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004eae5c",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004eae20",
      "PARAM",
      [
        "storage",
        "002b81c8",
        null,
        "string"
      ]
    ],
    [
      "004eae48",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004eae5c",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7f34.md#insn-004c7f90) · [`004c8028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7f34.md#insn-004c8028) · [`004c7f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c7/004c7f34.md#insn-004c7f60)
- 新版 [`004eae28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eadcc.md#insn-004eae28) · [`004eaec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eadcc.md#insn-004eaec0) · [`004eadf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eadcc.md#insn-004eadf8)

~~~diff
- 004c7f90 ["INT_ADD", "register:40f0:8", ["const:4c7f90:8", "const:4:8"]]
- 004c7f90 ["CALL", null, ["callee:00c57b70:8"]]
+ 004eae28 ["INT_ADD", "register:40f0:8", ["const:4eae28:8", "const:4:8"]]
+ 004eae28 ["CALL", null, ["callee:00c57b70:8"]]
- 004c7f90 bytes 644c1c94
+ 004eae28 bytes 52b31d94
- 004c8028 ["INT_ADD", "register:40f0:8", ["const:4c8028:8", "const:4:8"]]
- 004c8028 ["CALL", null, ["callee:00c57b10:8"]]
+ 004eaec0 ["INT_ADD", "register:40f0:8", ["const:4eaec0:8", "const:4:8"]]
+ 004eaec0 ["CALL", null, ["callee:00c57b10:8"]]
- 004c8028 bytes 264c1c94
+ 004eaec0 bytes 14b31d94
- 004c7f60 ["INT_ADD", "register:40f0:8", ["const:4c7f60:8", "const:4:8"]]
- 004c7f60 ["CALL", null, ["callee:00c57af0:8"]]
+ 004eadf8 ["INT_ADD", "register:40f0:8", ["const:4eadf8:8", "const:4:8"]]
+ 004eadf8 ["CALL", null, ["callee:00c57af0:8"]]
- 004c7f60 bytes 504c1c94
+ 004eadf8 bytes 3eb31d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43f75c8cc0a25c4dda6165bb8a91222f"></a>

### [`004c80c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c80c0.md) → [`004eaf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaf58.md) _ZNK5Botan11Private_Key23create_key_agreement_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocator

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

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
      "definition_site": "004eafe8",
      "incomplete_value": true,
      "site": "004eafe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c8150",
      "incomplete_value": true,
      "site": "004c8150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004eb020",
      "incomplete_value": true,
      "site": "004eb024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c8188",
      "incomplete_value": true,
      "site": "004c818c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eafac",
      "incomplete_value": false,
      "site": "004eafb4",
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
            "const:fac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8114",
      "incomplete_value": false,
      "site": "004c811c",
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
            "const:a6a:8"
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
      "004eafac",
      "PARAM",
      [
        "storage",
        "00290a6a",
        null,
        "string"
      ]
    ],
    [
      "004eafd4",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004eafe8",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004eafac",
      "PARAM",
      [
        "storage",
        "0029ffac",
        null,
        "string"
      ]
    ],
    [
      "004eafd4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004eafe8",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c811c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c80c0.md#insn-004c811c) · [`004c81b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c80c0.md#insn-004c81b4) · [`004c80ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c80c0.md#insn-004c80ec)
- 新版 [`004eafb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaf58.md#insn-004eafb4) · [`004eb04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaf58.md#insn-004eb04c) · [`004eaf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaf58.md#insn-004eaf84)

~~~diff
- 004c811c ["INT_ADD", "register:40f0:8", ["const:4c811c:8", "const:4:8"]]
- 004c811c ["CALL", null, ["callee:00c57b70:8"]]
+ 004eafb4 ["INT_ADD", "register:40f0:8", ["const:4eafb4:8", "const:4:8"]]
+ 004eafb4 ["CALL", null, ["callee:00c57b70:8"]]
- 004c811c bytes 014c1c94
+ 004eafb4 bytes efb21d94
- 004c81b4 ["INT_ADD", "register:40f0:8", ["const:4c81b4:8", "const:4:8"]]
- 004c81b4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004eb04c ["INT_ADD", "register:40f0:8", ["const:4eb04c:8", "const:4:8"]]
+ 004eb04c ["CALL", null, ["callee:00c57b10:8"]]
- 004c81b4 bytes c34b1c94
+ 004eb04c bytes b1b21d94
- 004c80ec ["INT_ADD", "register:40f0:8", ["const:4c80ec:8", "const:4:8"]]
- 004c80ec ["CALL", null, ["callee:00c57af0:8"]]
+ 004eaf84 ["INT_ADD", "register:40f0:8", ["const:4eaf84:8", "const:4:8"]]
+ 004eaf84 ["CALL", null, ["callee:00c57af0:8"]]
- 004c80ec bytes ed4b1c94
+ 004eaf84 bytes dbb21d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07903fdea109437bc8eaf7f570a531dd"></a>

### [`004c824c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c824c.md) → [`004eb0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb0e4.md) FUN_004eb0e4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004d29f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d29f8.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md) [`00bdc6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6a0.md)
- 新版 呼出元 1件 [`004f5890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5890.md) · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md) [`00c590f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb0f8",
      "incomplete_value": false,
      "site": "004eb100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8260",
      "incomplete_value": false,
      "site": "004c8268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "definition_site": "004eb15c",
      "incomplete_value": true,
      "site": "004eb164",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c82c4",
      "incomplete_value": true,
      "site": "004c82cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
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
      "definition_site": "004eb158",
      "incomplete_value": false,
      "site": "004eb164",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004c82c0",
      "incomplete_value": false,
      "site": "004c82cc",
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
      "004eb100",
      "DATA",
      [
        "storage",
        "00be9ea8",
        null,
        "undefined *"
      ]
    ],
    [
      "004eb158",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004eb15c",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004eb100",
      "DATA",
      [
        "storage",
        "00c66a68",
        null,
        "undefined *"
      ]
    ],
    [
      "004eb158",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004eb15c",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c82cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c824c.md#insn-004c82cc) · [`004c825c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c824c.md#insn-004c825c) · [`004c8260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c824c.md#insn-004c8260)
- 新版 [`004eb164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb0e4.md#insn-004eb164) · [`004eb0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb0e4.md#insn-004eb0f4) · [`004eb0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb0e4.md#insn-004eb0f8)

~~~diff
- 004c82cc ["INT_ADD", "register:40f0:8", ["const:4c82cc:8", "const:4:8"]]
- 004c82cc ["CALL", null, ["callee:00c57b10:8"]]
+ 004eb164 ["INT_ADD", "register:40f0:8", ["const:4eb164:8", "const:4:8"]]
+ 004eb164 ["CALL", null, ["callee:00c57b10:8"]]
- 004c82cc bytes 7d4b1c94
+ 004eb164 bytes 6bb21d94
- 004c825c ["COPY", "register:4040:8", ["const:be9000:8"]]
+ 004eb0f4 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004c825c bytes 083900b0
+ 004eb0f4 bytes c83b00f0
- 004c8260 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 004c8260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004c8260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004c8260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004eb0f8 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 004eb0f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004eb0f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004eb0f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004c8260 bytes 08a13a91
+ 004eb0f8 bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d531458985ce61448287120d86adaf7d"></a>

### [`004c8434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8434.md) → [`004eb2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb2cc.md) FUN_004eb2cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

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
      "definition_site": "004eb388",
      "incomplete_value": true,
      "site": "004eb388",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "definition_site": "004c84f0",
      "incomplete_value": true,
      "site": "004c84f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "definition_site": "004eb3b4",
      "incomplete_value": true,
      "site": "004eb3b4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "definition_site": "004c851c",
      "incomplete_value": true,
      "site": "004c851c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
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
      "004eb378",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004eb3a4",
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
      "004eb378",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004eb3a4",
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

- 旧版 [`004c84f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8434.md#insn-004c84f0) · [`004c851c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8434.md#insn-004c851c) · [`004c8478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8434.md#insn-004c8478)
- 新版 [`004eb388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb2cc.md#insn-004eb388) · [`004eb3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb2cc.md#insn-004eb3b4) · [`004eb310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb2cc.md#insn-004eb310)

~~~diff
- 004c84f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c84f0 ["INT_ADD", "register:40f0:8", ["const:4c84f0:8", "const:4:8"]]
- 004c84f0 ["CALLIND", null, ["register:0:8"]]
+ 004eb388 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eb388 ["INT_ADD", "register:40f0:8", ["const:4eb388:8", "const:4:8"]]
+ 004eb388 ["CALLIND", null, ["register:0:8"]]
- 004c84f0 bytes 20013fd6
+ 004eb388 bytes 20013fd6
- 004c851c ["COPY", "register:0:8", ["register:4048:8"]]
- 004c851c ["INT_ADD", "register:40f0:8", ["const:4c851c:8", "const:4:8"]]
- 004c851c ["CALLIND", null, ["register:0:8"]]
+ 004eb3b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eb3b4 ["INT_ADD", "register:40f0:8", ["const:4eb3b4:8", "const:4:8"]]
+ 004eb3b4 ["CALLIND", null, ["register:0:8"]]
- 004c851c bytes 20013fd6
+ 004eb3b4 bytes 20013fd6
- 004c8478 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c8478 ["INT_ADD", "register:40f0:8", ["const:4c8478:8", "const:4:8"]]
- 004c8478 ["CALLIND", null, ["register:0:8"]]
+ 004eb310 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eb310 ["INT_ADD", "register:40f0:8", ["const:4eb310:8", "const:4:8"]]
+ 004eb310 ["CALLIND", null, ["register:0:8"]]
- 004c8478 bytes 20013fd6
+ 004eb310 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-304f25c93d6b4854bc7d666f2edcbab7"></a>

### [`004c8590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8590.md) → [`004eb428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb428.md) FUN_004eb428

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004d2528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d2/004d2528.md) · 呼出先 6件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdc150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc150.md) [`00bdc6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6a0.md)
- 新版 呼出元 1件 [`004f53c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f53c0.md) · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md) [`00c590f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb43c",
      "incomplete_value": false,
      "site": "004eb444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c85a4",
      "incomplete_value": false,
      "site": "004c85ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eb4a0",
      "incomplete_value": true,
      "site": "004eb4a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8608",
      "incomplete_value": true,
      "site": "004c8610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
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
      "definition_site": "004eb49c",
      "incomplete_value": false,
      "site": "004eb4a8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004c8604",
      "incomplete_value": false,
      "site": "004c8610",
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
      "004eb444",
      "DATA",
      [
        "storage",
        "00be9ef8",
        null,
        "undefined *"
      ]
    ],
    [
      "004eb49c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004eb4a0",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004eb444",
      "DATA",
      [
        "storage",
        "00c66ab8",
        null,
        "undefined *"
      ]
    ],
    [
      "004eb49c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004eb4a0",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8590.md#insn-004c8610) · [`004c85a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8590.md#insn-004c85a0) · [`004c85a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8590.md#insn-004c85a4)
- 新版 [`004eb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb428.md#insn-004eb4a8) · [`004eb438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb428.md#insn-004eb438) · [`004eb43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb428.md#insn-004eb43c)

~~~diff
- 004c8610 ["INT_ADD", "register:40f0:8", ["const:4c8610:8", "const:4:8"]]
- 004c8610 ["CALL", null, ["callee:00c57b10:8"]]
+ 004eb4a8 ["INT_ADD", "register:40f0:8", ["const:4eb4a8:8", "const:4:8"]]
+ 004eb4a8 ["CALL", null, ["callee:00c57b10:8"]]
- 004c8610 bytes ac4a1c94
+ 004eb4a8 bytes 9ab11d94
- 004c85a0 ["COPY", "register:4040:8", ["const:be9000:8"]]
+ 004eb438 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004c85a0 bytes 083900b0
+ 004eb438 bytes c83b00f0
- 004c85a4 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 004c85a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004c85a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004c85a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004eb43c ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 004eb43c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004eb43c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004eb43c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004c85a4 bytes 08e13b91
+ 004eb43c bytes 08e12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50dc30b75e4afea08166c61ad56438d9"></a>

### [`004c898c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c898c.md) → [`004eb824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb824.md) FUN_004eb824

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004eb90c",
      "incomplete_value": true,
      "site": "004eb90c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c8a74",
      "incomplete_value": true,
      "site": "004c8a74",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004eb950",
      "incomplete_value": true,
      "site": "004eb950",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c8ab8",
      "incomplete_value": true,
      "site": "004c8ab8",
      "value": [
        "LOAD",
        "8",
        [
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
      "004eb8fc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004eb940",
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
      "004eb8fc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004eb940",
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

- 旧版 [`004c8a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c898c.md#insn-004c8a74) · [`004c8ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c898c.md#insn-004c8ab8) · [`004c89e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c898c.md#insn-004c89e0)
- 新版 [`004eb90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb824.md#insn-004eb90c) · [`004eb950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb824.md#insn-004eb950) · [`004eb878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb824.md#insn-004eb878)

~~~diff
- 004c8a74 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c8a74 ["INT_ADD", "register:40f0:8", ["const:4c8a74:8", "const:4:8"]]
- 004c8a74 ["CALLIND", null, ["register:0:8"]]
+ 004eb90c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eb90c ["INT_ADD", "register:40f0:8", ["const:4eb90c:8", "const:4:8"]]
+ 004eb90c ["CALLIND", null, ["register:0:8"]]
- 004c8a74 bytes 20013fd6
+ 004eb90c bytes 20013fd6
- 004c8ab8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c8ab8 ["INT_ADD", "register:40f0:8", ["const:4c8ab8:8", "const:4:8"]]
- 004c8ab8 ["CALLIND", null, ["register:0:8"]]
+ 004eb950 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eb950 ["INT_ADD", "register:40f0:8", ["const:4eb950:8", "const:4:8"]]
+ 004eb950 ["CALLIND", null, ["register:0:8"]]
- 004c8ab8 bytes 20013fd6
+ 004eb950 bytes 20013fd6
- 004c89e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c89e0 ["INT_ADD", "register:40f0:8", ["const:4c89e0:8", "const:4:8"]]
- 004c89e0 ["CALLIND", null, ["register:0:8"]]
+ 004eb878 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004eb878 ["INT_ADD", "register:40f0:8", ["const:4eb878:8", "const:4:8"]]
+ 004eb878 ["CALLIND", null, ["register:0:8"]]
- 004c89e0 bytes 00013fd6
+ 004eb878 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-562c10bec8c8ec95d8b3a1a6351de4d8"></a>

### [`004c8c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8c88.md) → [`004ebb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebb20.md) _ZN5Botan5PKCS810PEM_encodeERKNS_11Private_KeyE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7a0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) [`00bdc790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc790.md)
- 新版 呼出元 1件 [`00c591f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591f0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c591e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591e0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ebb78",
      "incomplete_value": true,
      "site": "004ebb78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:73:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8ce0",
      "incomplete_value": true,
      "site": "004c8ce0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a5a:8"
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
      "definition_site": "004ebbc0",
      "incomplete_value": true,
      "site": "004ebbc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c8d28",
      "incomplete_value": true,
      "site": "004c8d28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ebb64",
      "READ",
      [
        "storage",
        "00291a5a",
        null,
        "string"
      ]
    ],
    [
      "004ebbb0",
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
      "004ebb64",
      "READ",
      [
        "storage",
        "002a1073",
        null,
        "string"
      ]
    ],
    [
      "004ebbb0",
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

- 旧版 [`004c8d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8c88.md#insn-004c8d28) · [`004c8cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8c88.md#insn-004c8cb0) · [`004c8cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8c88.md#insn-004c8cb8)
- 新版 [`004ebbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebb20.md#insn-004ebbc0) · [`004ebb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebb20.md#insn-004ebb48) · [`004ebb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebb20.md#insn-004ebb50)

~~~diff
- 004c8d28 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c8d28 ["INT_ADD", "register:40f0:8", ["const:4c8d28:8", "const:4:8"]]
- 004c8d28 ["CALLIND", null, ["register:0:8"]]
+ 004ebbc0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ebbc0 ["INT_ADD", "register:40f0:8", ["const:4ebbc0:8", "const:4:8"]]
+ 004ebbc0 ["CALLIND", null, ["register:0:8"]]
- 004c8d28 bytes 20013fd6
+ 004ebbc0 bytes 20013fd6
- 004c8cb0 ["INT_ADD", "register:40f0:8", ["const:4c8cb0:8", "const:4:8"]]
- 004c8cb0 ["CALL", null, ["callee:00c591e0:8"]]
+ 004ebb48 ["INT_ADD", "register:40f0:8", ["const:4ebb48:8", "const:4:8"]]
+ 004ebb48 ["CALL", null, ["callee:00c591e0:8"]]
- 004c8cb0 bytes b84e1c94
+ 004ebb48 bytes a6b51d94
- 004c8cb8 ["COPY", "register:4048:8", ["const:291000:8"]]
+ 004ebb50 ["COPY", "register:4048:8", ["const:2a1000:8"]]
- 004c8cb8 bytes 49eeffb0
+ 004ebb50 bytes a9edffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-541d32ececdb5f510b1259ce3f0c2ed3"></a>

### [`004c8d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8d94.md) → [`004ebc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md) _ZN5Botan5PKCS810BER_encodeERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIc

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7b0.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md)
- 新版 呼出元 1件 [`00c59200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59200.md) · 呼出先 20件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.67% / 新版 95.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004ebd28",
      "incomplete_value": false,
      "site": "004ebd28",
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
            "const:c3a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8e90",
      "incomplete_value": false,
      "site": "004c8e90",
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
            "const:914:8"
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
      "definition_site": "004ebd28",
      "incomplete_value": false,
      "site": "004ebd28",
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
            "const:a56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8e90",
      "incomplete_value": false,
      "site": "004c8e90",
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
            "const:b7d:8"
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
      "definition_site": "004ebf08",
      "incomplete_value": false,
      "site": "004ebf08",
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
            "const:38d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9070",
      "incomplete_value": false,
      "site": "004c9070",
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
            "const:31f:8"
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
      "004ebd28",
      "DATA",
      [
        "storage",
        "002ad914",
        null,
        "string"
      ]
    ],
    [
      "004ebd28",
      "DATA",
      [
        "storage",
        "00299b7d",
        null,
        "string"
      ]
    ],
    [
      "004ebf08",
      "DATA",
      [
        "storage",
        "0029b31f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ebd28",
      "DATA",
      [
        "storage",
        "002bec3a",
        null,
        "string"
      ]
    ],
    [
      "004ebd28",
      "DATA",
      [
        "storage",
        "002a9a56",
        null,
        "string"
      ]
    ],
    [
      "004ebf08",
      "DATA",
      [
        "storage",
        "002ab38d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c90ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8d94.md#insn-004c90ec) · [`004c91b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8d94.md#insn-004c91b4) · [`004c925c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c8/004c8d94.md#insn-004c925c)
- 新版 [`004ebf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md#insn-004ebf84) · [`004ec04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md#insn-004ec04c) · [`004ec0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md#insn-004ec0f4)

~~~diff
- 004c90ec ["COPY", "register:0:8", ["register:4048:8"]]
- 004c90ec ["INT_ADD", "register:40f0:8", ["const:4c90ec:8", "const:4:8"]]
- 004c90ec ["CALLIND", null, ["register:0:8"]]
+ 004ebf84 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ebf84 ["INT_ADD", "register:40f0:8", ["const:4ebf84:8", "const:4:8"]]
+ 004ebf84 ["CALLIND", null, ["register:0:8"]]
- 004c90ec bytes 20013fd6
+ 004ebf84 bytes 20013fd6
- 004c91b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c91b4 ["INT_ADD", "register:40f0:8", ["const:4c91b4:8", "const:4:8"]]
- 004c91b4 ["CALLIND", null, ["register:0:8"]]
+ 004ec04c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ec04c ["INT_ADD", "register:40f0:8", ["const:4ec04c:8", "const:4:8"]]
+ 004ec04c ["CALLIND", null, ["register:0:8"]]
- 004c91b4 bytes 20013fd6
+ 004ec04c bytes 20013fd6
- 004c925c ["INT_ADD", "register:40f0:8", ["const:4c925c:8", "const:4:8"]]
- 004c925c ["CALL", null, ["callee:00c57cb0:8"]]
+ 004ec0f4 ["INT_ADD", "register:40f0:8", ["const:4ec0f4:8", "const:4:8"]]
+ 004ec0f4 ["CALL", null, ["callee:00c57cb0:8"]]
- 004c925c bytes 01481c94
+ 004ec0f4 bytes efae1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61632b2591dd0d2925d93305574a5580"></a>

### [`004c93c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c93c4.md) → [`004ec25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec25c.md) _ZN5Botan5PKCS810PEM_encodeERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIc

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) [`00bdc7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7a0.md) [`00bdc7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c591f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591f0.md) [`00c59200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59200.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec2b0",
      "incomplete_value": true,
      "site": "004ec2c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9418",
      "incomplete_value": true,
      "site": "004c9428",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:513:8"
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
      "definition_site": "004ec2c4",
      "incomplete_value": true,
      "site": "004ec2c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004c942c",
      "incomplete_value": true,
      "site": "004c942c",
      "value": [
        "LOAD",
        "8",
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
      "004ec2b0",
      "READ",
      [
        "storage",
        "002a4513",
        null,
        "string"
      ]
    ],
    [
      "004ec2b4",
      "READ",
      [
        "storage",
        "002a4520",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ec2b0",
      "READ",
      [
        "storage",
        "002b4d80",
        null,
        "string"
      ]
    ],
    [
      "004ec2b4",
      "READ",
      [
        "storage",
        "002b4d8d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c93c4.md#insn-004c9400) · [`004c9408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c93c4.md#insn-004c9408) · [`004c940c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c93c4.md#insn-004c940c)
- 新版 [`004ec298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec25c.md#insn-004ec298) · [`004ec2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec25c.md#insn-004ec2a0) · [`004ec2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec25c.md#insn-004ec2a4)

~~~diff
- 004c9400 ["INT_ADD", "register:40f0:8", ["const:4c9400:8", "const:4:8"]]
- 004c9400 ["CALL", null, ["callee:00c59200:8"]]
+ 004ec298 ["INT_ADD", "register:40f0:8", ["const:4ec298:8", "const:4:8"]]
+ 004ec298 ["CALL", null, ["callee:00c59200:8"]]
- 004c9400 bytes ec4c1c94
+ 004ec298 bytes dab31d94
- 004c9408 ["COPY", "register:4048:8", ["const:2a4000:8"]]
+ 004ec2a0 ["COPY", "register:4048:8", ["const:2b4000:8"]]
- 004c9408 bytes c9eefff0
+ 004ec2a0 bytes 49eeff90
- 004c940c ["COPY", "tmp:0:8", ["const:513:8"]]
- 004c940c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004c940c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004c940c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ec2a4 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 004ec2a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec2a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec2a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004c940c bytes 294d1491
+ 004ec2a4 bytes 29013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da708ecd16458ff4ac306dcebbc5d9fa"></a>

### [`004c94e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c94e0.md) → [`004ec378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec378.md) _ZN5Botan5PKCS831BER_encode_encrypted_pbkdf_iterERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7c0.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c59210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59210.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.93% / 新版 95.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec410",
      "incomplete_value": true,
      "site": "004ec410",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c3a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9578",
      "incomplete_value": true,
      "site": "004c9578",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:914:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004ec4f4",
      "incomplete_value": true,
      "site": "004ec4f4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c965c",
      "incomplete_value": true,
      "site": "004c965c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ec5bc",
      "incomplete_value": true,
      "site": "004ec5bc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c9724",
      "incomplete_value": true,
      "site": "004c9724",
      "value": [
        "LOAD",
        "8",
        [
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
      "004ec3fc",
      "READ",
      [
        "storage",
        "002ad914",
        null,
        "string"
      ]
    ],
    [
      "004ec4e4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004ec5ac",
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
      "004ec3fc",
      "READ",
      [
        "storage",
        "002bec3a",
        null,
        "string"
      ]
    ],
    [
      "004ec4e4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ec5ac",
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

- 旧版 [`004c965c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c94e0.md#insn-004c965c) · [`004c9724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c94e0.md#insn-004c9724) · [`004c9524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c94e0.md#insn-004c9524)
- 新版 [`004ec4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec378.md#insn-004ec4f4) · [`004ec5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec378.md#insn-004ec5bc) · [`004ec3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec378.md#insn-004ec3bc)

~~~diff
- 004c965c ["COPY", "register:0:8", ["register:4048:8"]]
- 004c965c ["INT_ADD", "register:40f0:8", ["const:4c965c:8", "const:4:8"]]
- 004c965c ["CALLIND", null, ["register:0:8"]]
+ 004ec4f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ec4f4 ["INT_ADD", "register:40f0:8", ["const:4ec4f4:8", "const:4:8"]]
+ 004ec4f4 ["CALLIND", null, ["register:0:8"]]
- 004c965c bytes 20013fd6
+ 004ec4f4 bytes 20013fd6
- 004c9724 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c9724 ["INT_ADD", "register:40f0:8", ["const:4c9724:8", "const:4:8"]]
- 004c9724 ["CALLIND", null, ["register:0:8"]]
+ 004ec5bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ec5bc ["INT_ADD", "register:40f0:8", ["const:4ec5bc:8", "const:4:8"]]
+ 004ec5bc ["CALLIND", null, ["register:0:8"]]
- 004c9724 bytes 20013fd6
+ 004ec5bc bytes 20013fd6
- 004c9524 ["INT_ADD", "register:40f0:8", ["const:4c9524:8", "const:4:8"]]
- 004c9524 ["CALL", null, ["callee:00c591e0:8"]]
+ 004ec3bc ["INT_ADD", "register:40f0:8", ["const:4ec3bc:8", "const:4:8"]]
+ 004ec3bc ["CALL", null, ["callee:00c591e0:8"]]
- 004c9524 bytes 9b4c1c94
+ 004ec3bc bytes 89b31d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9dc2084570862e80f6f6c3b73624b02"></a>

### [`004c9804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9804.md) → [`004ec69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec69c.md) _ZN5Botan5PKCS831PEM_encode_encrypted_pbkdf_iterERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) [`00bdc7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c59210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec6d8",
      "incomplete_value": true,
      "site": "004ec6e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9840",
      "incomplete_value": true,
      "site": "004c9850",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:513:8"
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
      "definition_site": "004ec6ec",
      "incomplete_value": true,
      "site": "004ec6ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004c9854",
      "incomplete_value": true,
      "site": "004c9854",
      "value": [
        "LOAD",
        "8",
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
      "004ec6d8",
      "READ",
      [
        "storage",
        "002a4513",
        null,
        "string"
      ]
    ],
    [
      "004ec6dc",
      "READ",
      [
        "storage",
        "002a4520",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ec6d8",
      "READ",
      [
        "storage",
        "002b4d80",
        null,
        "string"
      ]
    ],
    [
      "004ec6dc",
      "READ",
      [
        "storage",
        "002b4d8d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9804.md#insn-004c9828) · [`004c9830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9804.md#insn-004c9830) · [`004c9834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9804.md#insn-004c9834)
- 新版 [`004ec6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec69c.md#insn-004ec6c0) · [`004ec6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec69c.md#insn-004ec6c8) · [`004ec6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec69c.md#insn-004ec6cc)

~~~diff
- 004c9828 ["INT_ADD", "register:40f0:8", ["const:4c9828:8", "const:4:8"]]
- 004c9828 ["CALL", null, ["callee:00c59210:8"]]
+ 004ec6c0 ["INT_ADD", "register:40f0:8", ["const:4ec6c0:8", "const:4:8"]]
+ 004ec6c0 ["CALL", null, ["callee:00c59210:8"]]
- 004c9828 bytes e64b1c94
+ 004ec6c0 bytes d4b21d94
- 004c9830 ["COPY", "register:4048:8", ["const:2a4000:8"]]
+ 004ec6c8 ["COPY", "register:4048:8", ["const:2b4000:8"]]
- 004c9830 bytes c9eefff0
+ 004ec6c8 bytes 49eeff90
- 004c9834 ["COPY", "tmp:0:8", ["const:513:8"]]
- 004c9834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004c9834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004c9834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ec6cc ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 004ec6cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec6cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec6cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004c9834 bytes 294d1491
+ 004ec6cc bytes 29013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b98e0cb1ecd20e97902a94f920d4631e"></a>

### [`004c98e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c98e8.md) → [`004ec780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec780.md) _ZN5Botan5PKCS831BER_encode_encrypted_pbkdf_msecERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7d0.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`004bf57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bf/004bf57c.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c59220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59220.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.09% / 新版 96.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec820",
      "incomplete_value": true,
      "site": "004ec820",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c3a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9988",
      "incomplete_value": true,
      "site": "004c9988",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:914:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004ec914",
      "incomplete_value": true,
      "site": "004ec914",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c9a7c",
      "incomplete_value": true,
      "site": "004c9a7c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ec9dc",
      "incomplete_value": true,
      "site": "004ec9dc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c9b44",
      "incomplete_value": true,
      "site": "004c9b44",
      "value": [
        "LOAD",
        "8",
        [
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
      "004ec80c",
      "READ",
      [
        "storage",
        "002ad914",
        null,
        "string"
      ]
    ],
    [
      "004ec904",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004ec9cc",
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
      "004ec80c",
      "READ",
      [
        "storage",
        "002bec3a",
        null,
        "string"
      ]
    ],
    [
      "004ec904",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ec9cc",
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

- 旧版 [`004c9a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c98e8.md#insn-004c9a7c) · [`004c9b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c98e8.md#insn-004c9b44) · [`004c9934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c98e8.md#insn-004c9934)
- 新版 [`004ec914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec780.md#insn-004ec914) · [`004ec9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec780.md#insn-004ec9dc) · [`004ec7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec780.md#insn-004ec7cc)

~~~diff
- 004c9a7c ["COPY", "register:0:8", ["register:4048:8"]]
- 004c9a7c ["INT_ADD", "register:40f0:8", ["const:4c9a7c:8", "const:4:8"]]
- 004c9a7c ["CALLIND", null, ["register:0:8"]]
+ 004ec914 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ec914 ["INT_ADD", "register:40f0:8", ["const:4ec914:8", "const:4:8"]]
+ 004ec914 ["CALLIND", null, ["register:0:8"]]
- 004c9a7c bytes 20013fd6
+ 004ec914 bytes 20013fd6
- 004c9b44 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c9b44 ["INT_ADD", "register:40f0:8", ["const:4c9b44:8", "const:4:8"]]
- 004c9b44 ["CALLIND", null, ["register:0:8"]]
+ 004ec9dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ec9dc ["INT_ADD", "register:40f0:8", ["const:4ec9dc:8", "const:4:8"]]
+ 004ec9dc ["CALLIND", null, ["register:0:8"]]
- 004c9b44 bytes 20013fd6
+ 004ec9dc bytes 20013fd6
- 004c9934 ["INT_ADD", "register:40f0:8", ["const:4c9934:8", "const:4:8"]]
- 004c9934 ["CALL", null, ["callee:00c591e0:8"]]
+ 004ec7cc ["INT_ADD", "register:40f0:8", ["const:4ec7cc:8", "const:4:8"]]
+ 004ec7cc ["CALL", null, ["callee:00c591e0:8"]]
- 004c9934 bytes 974b1c94
+ 004ec7cc bytes 85b21d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f22bd3e8d778a67836c0b042aa64b45"></a>

### [`004c9c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9c28.md) → [`004ecac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecac0.md) _ZN5Botan5PKCS831PEM_encode_encrypted_pbkdf_msecERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc640.md) [`00bdc7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc7d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c59220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59220.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ecafc",
      "incomplete_value": true,
      "site": "004ecb0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9c64",
      "incomplete_value": true,
      "site": "004c9c74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:513:8"
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
      "definition_site": "004ecb10",
      "incomplete_value": true,
      "site": "004ecb10",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004c9c78",
      "incomplete_value": true,
      "site": "004c9c78",
      "value": [
        "LOAD",
        "8",
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
      "004ecafc",
      "READ",
      [
        "storage",
        "002a4513",
        null,
        "string"
      ]
    ],
    [
      "004ecb00",
      "READ",
      [
        "storage",
        "002a4520",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ecafc",
      "READ",
      [
        "storage",
        "002b4d80",
        null,
        "string"
      ]
    ],
    [
      "004ecb00",
      "READ",
      [
        "storage",
        "002b4d8d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9c28.md#insn-004c9c4c) · [`004c9c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9c28.md#insn-004c9c54) · [`004c9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9c28.md#insn-004c9c58)
- 新版 [`004ecae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecac0.md#insn-004ecae4) · [`004ecaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecac0.md#insn-004ecaec) · [`004ecaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecac0.md#insn-004ecaf0)

~~~diff
- 004c9c4c ["INT_ADD", "register:40f0:8", ["const:4c9c4c:8", "const:4:8"]]
- 004c9c4c ["CALL", null, ["callee:00c59220:8"]]
+ 004ecae4 ["INT_ADD", "register:40f0:8", ["const:4ecae4:8", "const:4:8"]]
+ 004ecae4 ["CALL", null, ["callee:00c59220:8"]]
- 004c9c4c bytes e14a1c94
+ 004ecae4 bytes cfb11d94
- 004c9c54 ["COPY", "register:4048:8", ["const:2a4000:8"]]
+ 004ecaec ["COPY", "register:4048:8", ["const:2b4000:8"]]
- 004c9c54 bytes c9eefff0
+ 004ecaec bytes 49eeff90
- 004c9c58 ["COPY", "tmp:0:8", ["const:513:8"]]
- 004c9c58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004c9c58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004c9c58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ecaf0 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 004ecaf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ecaf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ecaf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004c9c58 bytes 294d1491
+ 004ecaf0 bytes 29013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5871fbc2bda0b5f5281a101b687414ad"></a>

### [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) → [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) FUN_004eccd0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 9件 [`004c9d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9d0c.md) [`004cadbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cadbc.md) [`004caf04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004caf04.md) [`004cafdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ca/004cafdc.md) [`004cb140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb140.md) · 呼出先 34件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`004828a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004828a4.md) [`004840c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/004840c4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)
- 新版 呼出元 9件 [`004ecba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecba4.md) [`004edc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edc54.md) [`004edd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edd9c.md) [`004ede74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004ede74.md) [`004edfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edfd8.md) · 呼出先 34件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004a6f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.64% / 新版 93.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 10件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ecd14",
      "incomplete_value": true,
      "site": "004ecd1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c9e7c",
      "incomplete_value": true,
      "site": "004c9e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004ecf5c",
      "incomplete_value": true,
      "site": "004ecf5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004ca0c4",
      "incomplete_value": true,
      "site": "004ca0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ed204",
      "incomplete_value": true,
      "site": "004ed218",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:224:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ca36c",
      "incomplete_value": true,
      "site": "004ca380",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:90e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 60,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ecd00",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004ecd1c",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ecd94",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004ecd00",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004ecd1c",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ecd94",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md#insn-004c9fac) · [`004ca108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md#insn-004ca108) · [`004ca144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md#insn-004ca144)
- 新版 [`004ece44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md#insn-004ece44) · [`004ecfa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md#insn-004ecfa0) · [`004ecfdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md#insn-004ecfdc)

~~~diff
- 004c9fac ["COPY", "register:0:8", ["register:4048:8"]]
- 004c9fac ["INT_ADD", "register:40f0:8", ["const:4c9fac:8", "const:4:8"]]
- 004c9fac ["CALLIND", null, ["register:0:8"]]
+ 004ece44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ece44 ["INT_ADD", "register:40f0:8", ["const:4ece44:8", "const:4:8"]]
+ 004ece44 ["CALLIND", null, ["register:0:8"]]
- 004c9fac bytes 20013fd6
+ 004ece44 bytes 20013fd6
- 004ca108 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ca108 ["INT_ADD", "register:40f0:8", ["const:4ca108:8", "const:4:8"]]
- 004ca108 ["CALLIND", null, ["register:0:8"]]
+ 004ecfa0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ecfa0 ["INT_ADD", "register:40f0:8", ["const:4ecfa0:8", "const:4:8"]]
+ 004ecfa0 ["CALLIND", null, ["register:0:8"]]
- 004ca108 bytes 20013fd6
+ 004ecfa0 bytes 20013fd6
- 004ca144 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ca144 ["INT_ADD", "register:40f0:8", ["const:4ca144:8", "const:4:8"]]
- 004ca144 ["CALLIND", null, ["register:0:8"]]
+ 004ecfdc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ecfdc ["INT_ADD", "register:40f0:8", ["const:4ecfdc:8", "const:4:8"]]
+ 004ecfdc ["CALLIND", null, ["register:0:8"]]
- 004ca144 bytes 20013fd6
+ 004ecfdc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

