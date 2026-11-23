# v15.7.4 → v16.0.0 · 最優先の変更候補 (8)

[一覧の目次](README.md)

<a id="compare-4cc955f1bdbe20fe668f41c269e93e3e"></a>

### [`0049af04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049af04.md) → [`004bdd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bdd9c.md) _ZN5Botan14CTS_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.99% / 新版 94.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004be120",
      "incomplete_value": true,
      "site": "004be120",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049b288",
      "incomplete_value": true,
      "site": "0049b288",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004be1ec",
      "incomplete_value": false,
      "site": "004be20c",
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
      "definition_site": "0049b354",
      "incomplete_value": false,
      "site": "0049b374",
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
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004be1f4",
      "incomplete_value": false,
      "site": "004be20c",
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
      "definition_site": "0049b35c",
      "incomplete_value": false,
      "site": "0049b374",
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
      "004be110",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004be1ec",
      "PARAM",
      [
        "storage",
        "0029d49b",
        null,
        "string"
      ]
    ],
    [
      "004be1f4",
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
      "004be110",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004be1ec",
      "PARAM",
      [
        "storage",
        "002ad725",
        null,
        "string"
      ]
    ],
    [
      "004be1f4",
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

- 旧版 [`0049b288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049af04.md#insn-0049b288) · [`0049b374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049af04.md#insn-0049b374) · [`0049b39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049af04.md#insn-0049b39c)
- 新版 `004be120`（命令位置の公開資料なし） · `004be20c`（命令位置の公開資料なし） · `004be234`（命令位置の公開資料なし）

~~~diff
- 0049b288 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049b288 ["INT_ADD", "register:40f0:8", ["const:49b288:8", "const:4:8"]]
- 0049b288 ["CALLIND", null, ["register:0:8"]]
+ 004be120 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004be120 ["INT_ADD", "register:40f0:8", ["const:4be120:8", "const:4:8"]]
+ 004be120 ["CALLIND", null, ["register:0:8"]]
- 0049b288 bytes 20013fd6
+ 004be120 bytes 20013fd6
- 0049b374 ["INT_ADD", "register:40f0:8", ["const:49b374:8", "const:4:8"]]
- 0049b374 ["CALL", null, ["callee:00c58250:8"]]
+ 004be20c ["INT_ADD", "register:40f0:8", ["const:4be20c:8", "const:4:8"]]
+ 004be20c ["CALL", null, ["callee:00c58250:8"]]
- 0049b374 bytes 23011d94
+ 004be20c bytes 11681e94
- 0049b39c ["INT_ADD", "register:40f0:8", ["const:49b39c:8", "const:4:8"]]
- 0049b39c ["CALL", null, ["callee:00c57b70:8"]]
+ 004be234 ["INT_ADD", "register:40f0:8", ["const:4be234:8", "const:4:8"]]
+ 004be234 ["CALL", null, ["callee:00c57b70:8"]]
- 0049b39c bytes 61ff1c94
+ 004be234 bytes 4f661e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be3ed41089e45b972aa3bcf442757c98"></a>

### [`0049b54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049b54c.md) → [`004be3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004be3e4.md) _ZN5Botan5CPUID9to_stringEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf50.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c589a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589a0.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.80% / 新版 97.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004be794",
      "incomplete_value": true,
      "site": "004be794",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b8fc",
      "incomplete_value": true,
      "site": "0049b8fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:248:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004be854",
      "incomplete_value": true,
      "site": "004be854",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b9bc",
      "incomplete_value": true,
      "site": "0049b9bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:248:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004be428",
      "incomplete_value": true,
      "site": "004be428",
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
      "definition_site": "0049b590",
      "incomplete_value": true,
      "site": "0049b590",
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
      "004be414",
      "READ",
      [
        "storage",
        "00c1af28",
        null,
        "pointer"
      ]
    ],
    [
      "004be41c",
      "READ",
      [
        "storage",
        "00c25378",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004be534",
      "READ",
      [
        "storage",
        "00c25378",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004be414",
      "READ",
      [
        "storage",
        "00c9a918",
        null,
        "pointer"
      ]
    ],
    [
      "004be41c",
      "READ",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004be534",
      "READ",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049b574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049b54c.md#insn-0049b574) · [`0049b57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049b54c.md#insn-0049b57c) · [`0049b5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049b54c.md#insn-0049b5b0)
- 新版 `004be40c`（命令位置の公開資料なし） · `004be414`（命令位置の公開資料なし） · `004be448`（命令位置の公開資料なし）

~~~diff
- 0049b574 ["COPY", "register:40c0:8", ["const:c1a000:8"]]
+ 004be40c ["COPY", "register:40c0:8", ["const:c9a000:8"]]
- 0049b574 bytes f83b00f0
+ 004be40c bytes f83e0090
- 0049b57c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:f28:8"]]
- 0049b57c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004be414 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:918:8"]]
+ 004be414 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 0049b57c bytes 189747f9
+ 004be414 bytes 188f44f9
- 0049b5b0 ["INT_ADD", "register:40f0:8", ["const:49b5b0:8", "const:4:8"]]
- 0049b5b0 ["CALL", null, ["callee:00c57a90:8"]]
+ 004be448 ["INT_ADD", "register:40f0:8", ["const:4be448:8", "const:4:8"]]
+ 004be448 ["CALL", null, ["callee:00c57a90:8"]]
- 0049b5b0 bytes a4fe1c94
+ 004be448 bytes 92651e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fb5925b1eb457cb908f60e208856423"></a>

### [`0049bcc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bcc4.md) → [`004beb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beb5c.md) _ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c589a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004beb78",
      "incomplete_value": false,
      "site": "004beb88",
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
            "const:4ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bce0",
      "incomplete_value": false,
      "site": "0049bcf0",
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
            "const:9b7:8"
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
      "definition_site": "004bebc0",
      "incomplete_value": false,
      "site": "004bebc8",
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
      "definition_site": "0049bd28",
      "incomplete_value": false,
      "site": "0049bd30",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004beb78",
      "PARAM",
      [
        "storage",
        "002969b7",
        null,
        "string"
      ]
    ],
    [
      "004bebc0",
      "PARAM",
      [
        "storage",
        "002a4333",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004beb78",
      "PARAM",
      [
        "storage",
        "002a64ec",
        null,
        "string"
      ]
    ],
    [
      "004bebc0",
      "PARAM",
      [
        "storage",
        "002b4ba0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049bcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bcc4.md#insn-0049bcf0) · [`0049bd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bcc4.md#insn-0049bd30) · [`0049bcdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bcc4.md#insn-0049bcdc)
- 新版 `004beb88`（命令位置の公開資料なし） · `004bebc8`（命令位置の公開資料なし） · `004beb74`（命令位置の公開資料なし）

~~~diff
- 0049bcf0 ["INT_ADD", "register:40f0:8", ["const:49bcf0:8", "const:4:8"]]
- 0049bcf0 ["CALL", null, ["callee:00459490:8"]]
+ 004beb88 ["INT_ADD", "register:40f0:8", ["const:4beb88:8", "const:4:8"]]
+ 004beb88 ["CALL", null, ["callee:00459490:8"]]
- 0049bcf0 bytes 426afe97
+ 004beb88 bytes 426afe97
- 0049bd30 ["INT_ADD", "register:40f0:8", ["const:49bd30:8", "const:4:8"]]
- 0049bd30 ["CALL", null, ["callee:00459490:8"]]
+ 004bebc8 ["INT_ADD", "register:40f0:8", ["const:4bebc8:8", "const:4:8"]]
+ 004bebc8 ["CALL", null, ["callee:00459490:8"]]
- 0049bd30 bytes 326afe97
+ 004bebc8 bytes 326afe97
- 0049bcdc ["COPY", "register:4008:8", ["const:296000:8"]]
+ 004beb74 ["COPY", "register:4008:8", ["const:2a6000:8"]]
- 0049bcdc bytes c1effff0
+ 004beb74 bytes 41efff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ba64b78c9bcd6f5f0193fac630792dd"></a>

### [`0049bd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bd98.md) → [`004bec30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bec30.md) _ZN5Botan5CPUID10initializeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "004bec3c",
      "incomplete_value": true,
      "site": "004bec3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:918:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bda4",
      "incomplete_value": true,
      "site": "0049bda4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f28:8"
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
      "004bec38",
      "READ",
      [
        "storage",
        "00c1af28",
        null,
        "pointer"
      ]
    ],
    [
      "004bec3c",
      "WRITE",
      [
        "storage",
        "00c25378",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004bec38",
      "READ",
      [
        "storage",
        "00c9a918",
        null,
        "pointer"
      ]
    ],
    [
      "004bec3c",
      "WRITE",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049bd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bd98.md#insn-0049bd98) · [`0049bda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bd98.md#insn-0049bda0)
- 新版 `004bec30`（命令位置の公開資料なし） · `004bec38`（命令位置の公開資料なし）

~~~diff
- 0049bd98 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 004bec30 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0049bd98 bytes e83b00f0
+ 004bec30 bytes e83e0090
- 0049bda0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f28:8"]]
- 0049bda0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bec38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:918:8"]]
+ 004bec38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0049bda0 bytes 089547f9
+ 004bec38 bytes 088d44f9
~~~


<a id="compare-a686a92171da76d16754d8cde23efb4d"></a>

### [`0049c054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c054.md) → [`004beeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beeec.md) _ZN5Botan8ECB_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf60.md) · 呼出先 8件 [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c589b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589b0.md) · 呼出先 8件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.14% / 新版 93.14%

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
      "definition_site": "004bef28",
      "incomplete_value": true,
      "site": "004bef28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049c090",
      "incomplete_value": true,
      "site": "0049c090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004befa8",
      "incomplete_value": false,
      "site": "004befb4",
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
      "definition_site": "0049c110",
      "incomplete_value": false,
      "site": "0049c11c",
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
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004befd4",
      "incomplete_value": false,
      "site": "004befdc",
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
      "definition_site": "0049c13c",
      "incomplete_value": false,
      "site": "0049c144",
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
      "004bef14",
      "READ",
      [
        "storage",
        "00c1b058",
        null,
        "pointer"
      ]
    ],
    [
      "004bef28",
      "DATA",
      [
        "storage",
        "00be9518",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004befa8",
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
      "004bef14",
      "READ",
      [
        "storage",
        "00c9aa48",
        null,
        "pointer"
      ]
    ],
    [
      "004bef28",
      "DATA",
      [
        "storage",
        "00c660d8",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004befa8",
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

- 旧版 [`0049c11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c054.md#insn-0049c11c) · [`0049c144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c054.md#insn-0049c144) · [`0049c190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c054.md#insn-0049c190)
- 新版 `004befb4`（命令位置の公開資料なし） · `004befdc`（命令位置の公開資料なし） · `004bf028`（命令位置の公開資料なし）

~~~diff
- 0049c11c ["INT_ADD", "register:40f0:8", ["const:49c11c:8", "const:4:8"]]
- 0049c11c ["CALL", null, ["callee:00c57b60:8"]]
+ 004befb4 ["INT_ADD", "register:40f0:8", ["const:4befb4:8", "const:4:8"]]
+ 004befb4 ["CALL", null, ["callee:00c57b60:8"]]
- 0049c11c bytes fdfb1c94
+ 004befb4 bytes eb621e94
- 0049c144 ["INT_ADD", "register:40f0:8", ["const:49c144:8", "const:4:8"]]
- 0049c144 ["CALL", null, ["callee:00c57b70:8"]]
+ 004befdc ["INT_ADD", "register:40f0:8", ["const:4befdc:8", "const:4:8"]]
+ 004befdc ["CALL", null, ["callee:00c57b70:8"]]
- 0049c144 bytes f7fb1c94
+ 004befdc bytes e5621e94
- 0049c190 ["INT_ADD", "register:40f0:8", ["const:49c190:8", "const:4:8"]]
- 0049c190 ["CALL", null, ["callee:00c57b70:8"]]
+ 004bf028 ["INT_ADD", "register:40f0:8", ["const:4bf028:8", "const:4:8"]]
+ 004bf028 ["CALL", null, ["callee:00c57b70:8"]]
- 0049c190 bytes e4fb1c94
+ 004bf028 bytes d2621e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fc2fa5d08372eb887b7b723398c4d33"></a>

### [`0049c360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c360.md) → [`004bf1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf1f8.md) _ZNK5Botan8ECB_Mode4nameEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf70.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 1件 [`00c589c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589c0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf238",
      "incomplete_value": false,
      "site": "004bf240",
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
            "const:4fa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c3a0",
      "incomplete_value": false,
      "site": "0049c3a8",
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
            "const:9c5:8"
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
      "004bf238",
      "PARAM",
      [
        "storage",
        "002969c5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf238",
      "PARAM",
      [
        "storage",
        "002a64fa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049c3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c360.md#insn-0049c3a8) · [`0049c398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c360.md#insn-0049c398) · [`0049c39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c360.md#insn-0049c39c)
- 新版 `004bf240`（命令位置の公開資料なし） · `004bf230`（命令位置の公開資料なし） · `004bf234`（命令位置の公開資料なし）

~~~diff
- 0049c3a8 ["INT_ADD", "register:40f0:8", ["const:49c3a8:8", "const:4:8"]]
- 0049c3a8 ["CALL", null, ["callee:00c57b70:8"]]
+ 004bf240 ["INT_ADD", "register:40f0:8", ["const:4bf240:8", "const:4:8"]]
+ 004bf240 ["CALL", null, ["callee:00c57b70:8"]]
- 0049c3a8 bytes 5efb1c94
+ 004bf240 bytes 4c621e94
- 0049c398 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049c398 ["INT_ADD", "register:40f0:8", ["const:49c398:8", "const:4:8"]]
- 0049c398 ["CALLIND", null, ["register:0:8"]]
+ 004bf230 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bf230 ["INT_ADD", "register:40f0:8", ["const:4bf230:8", "const:4:8"]]
+ 004bf230 ["CALLIND", null, ["register:0:8"]]
- 0049c398 bytes 20013fd6
+ 004bf230 bytes 20013fd6
- 0049c39c ["COPY", "register:4008:8", ["const:296000:8"]]
+ 004bf234 ["COPY", "register:4008:8", ["const:2a6000:8"]]
- 0049c39c bytes c1efffd0
+ 004bf234 bytes 21effff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dc3c5396827d5aeb205932953ea85ce"></a>

### [`0049c574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c574.md) → [`004bf40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf40c.md) _ZN5Botan8ECB_Mode9start_msgEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58990.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "definition_site": "004bf4b4",
      "incomplete_value": true,
      "site": "004bf4c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049c61c",
      "incomplete_value": true,
      "site": "0049c628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf4b0",
      "incomplete_value": false,
      "site": "004bf4c0",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0049c618",
      "incomplete_value": false,
      "site": "0049c628",
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
      "004bf4b0",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004bf4b4",
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ],
    [
      "004bf4b4",
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
      "004bf4b0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bf4b4",
      "READ",
      [
        "storage",
        "00c9aa40",
        null,
        "pointer"
      ]
    ],
    [
      "004bf4b4",
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

- 旧版 [`0049c628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c574.md#insn-0049c628) · [`0049c5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c574.md#insn-0049c5cc) · [`0049c5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c574.md#insn-0049c5e4)
- 新版 `004bf4c0`（命令位置の公開資料なし） · `004bf464`（命令位置の公開資料なし） · `004bf47c`（命令位置の公開資料なし）

~~~diff
- 0049c628 ["INT_ADD", "register:40f0:8", ["const:49c628:8", "const:4:8"]]
- 0049c628 ["CALL", null, ["callee:00c57b10:8"]]
+ 004bf4c0 ["INT_ADD", "register:40f0:8", ["const:4bf4c0:8", "const:4:8"]]
+ 004bf4c0 ["CALL", null, ["callee:00c57b10:8"]]
- 0049c628 bytes a6fa1c94
+ 004bf4c0 bytes 94611e94
- 0049c5cc ["INT_ADD", "register:40f0:8", ["const:49c5cc:8", "const:4:8"]]
- 0049c5cc ["CALL", null, ["callee:00c57af0:8"]]
+ 004bf464 ["INT_ADD", "register:40f0:8", ["const:4bf464:8", "const:4:8"]]
+ 004bf464 ["CALL", null, ["callee:00c57af0:8"]]
- 0049c5cc bytes b5fa1c94
+ 004bf464 bytes a3611e94
- 0049c5e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049c5e4 ["INT_ADD", "register:40f0:8", ["const:49c5e4:8", "const:4:8"]]
- 0049c5e4 ["CALLIND", null, ["register:0:8"]]
+ 004bf47c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bf47c ["INT_ADD", "register:40f0:8", ["const:4bf47c:8", "const:4:8"]]
+ 004bf47c ["CALLIND", null, ["register:0:8"]]
- 0049c5e4 bytes 20013fd6
+ 004bf47c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-368f5e3da00544c7dbbc684878da8f75"></a>

### [`0049c684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c684.md) → [`004bf51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf51c.md) _ZNK5Botan14ECB_Encryption13output_lengthEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf56c",
      "incomplete_value": false,
      "site": "004bf58c",
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
      "definition_site": "0049c6d4",
      "incomplete_value": false,
      "site": "0049c6f4",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf574",
      "incomplete_value": false,
      "site": "004bf58c",
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
      "definition_site": "0049c6dc",
      "incomplete_value": false,
      "site": "0049c6f4",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf57c",
      "incomplete_value": false,
      "site": "004bf58c",
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
      "definition_site": "0049c6e4",
      "incomplete_value": false,
      "site": "0049c6f4",
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
      "004bf56c",
      "PARAM",
      [
        "storage",
        "002928e2",
        null,
        "string"
      ]
    ],
    [
      "004bf574",
      "PARAM",
      [
        "storage",
        "0029b50f",
        null,
        "string"
      ]
    ],
    [
      "004bf57c",
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
      "004bf56c",
      "PARAM",
      [
        "storage",
        "002a1ff2",
        null,
        "string"
      ]
    ],
    [
      "004bf574",
      "PARAM",
      [
        "storage",
        "002ab57d",
        null,
        "string"
      ]
    ],
    [
      "004bf57c",
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

- 旧版 [`0049c6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c684.md#insn-0049c6f4) · [`0049c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c684.md#insn-0049c6a0) · [`0049c6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c684.md#insn-0049c6d0)
- 新版 `004bf58c`（命令位置の公開資料なし） · `004bf538`（命令位置の公開資料なし） · `004bf568`（命令位置の公開資料なし）

~~~diff
- 0049c6f4 ["INT_ADD", "register:40f0:8", ["const:49c6f4:8", "const:4:8"]]
- 0049c6f4 ["CALL", null, ["callee:00c58250:8"]]
+ 004bf58c ["INT_ADD", "register:40f0:8", ["const:4bf58c:8", "const:4:8"]]
+ 004bf58c ["CALL", null, ["callee:00c58250:8"]]
- 0049c6f4 bytes 43fc1c94
+ 004bf58c bytes 31631e94
- 0049c6a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049c6a0 ["INT_ADD", "register:40f0:8", ["const:49c6a0:8", "const:4:8"]]
- 0049c6a0 ["CALLIND", null, ["register:0:8"]]
+ 004bf538 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf538 ["INT_ADD", "register:40f0:8", ["const:4bf538:8", "const:4:8"]]
+ 004bf538 ["CALLIND", null, ["register:0:8"]]
- 0049c6a0 bytes 00013fd6
+ 004bf538 bytes 00013fd6
- 0049c6d0 ["COPY", "register:4000:8", ["const:292000:8"]]
+ 004bf568 ["COPY", "register:4000:8", ["const:2a1000:8"]]
- 0049c6d0 bytes a0efffd0
+ 004bf568 bytes 00efffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3372c619872a776717b681ccdfc0678f"></a>

### [`0049c6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c6f8.md) → [`004bf590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf590.md) _ZN5Botan14ECB_Encryption7processEPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf5f8",
      "incomplete_value": false,
      "site": "004bf618",
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
      "definition_site": "0049c760",
      "incomplete_value": false,
      "site": "0049c780",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf600",
      "incomplete_value": false,
      "site": "004bf618",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c768",
      "incomplete_value": false,
      "site": "0049c780",
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
            "const:82f:8"
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
      "definition_site": "004bf608",
      "incomplete_value": false,
      "site": "004bf618",
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
      "definition_site": "0049c770",
      "incomplete_value": false,
      "site": "0049c780",
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
      "004bf5f8",
      "PARAM",
      [
        "storage",
        "00298d95",
        null,
        "string"
      ]
    ],
    [
      "004bf600",
      "PARAM",
      [
        "storage",
        "0029382f",
        null,
        "string"
      ]
    ],
    [
      "004bf608",
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
      "004bf5f8",
      "PARAM",
      [
        "storage",
        "002a8b53",
        null,
        "string"
      ]
    ],
    [
      "004bf600",
      "PARAM",
      [
        "storage",
        "002a3028",
        null,
        "string"
      ]
    ],
    [
      "004bf608",
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

- 旧版 [`0049c780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c6f8.md#insn-0049c780) · [`0049c720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c6f8.md#insn-0049c720) · [`0049c744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c6f8.md#insn-0049c744)
- 新版 `004bf618`（命令位置の公開資料なし） · `004bf5b8`（命令位置の公開資料なし） · `004bf5dc`（命令位置の公開資料なし）

~~~diff
- 0049c780 ["INT_ADD", "register:40f0:8", ["const:49c780:8", "const:4:8"]]
- 0049c780 ["CALL", null, ["callee:00c58250:8"]]
+ 004bf618 ["INT_ADD", "register:40f0:8", ["const:4bf618:8", "const:4:8"]]
+ 004bf618 ["CALL", null, ["callee:00c58250:8"]]
- 0049c780 bytes 20fc1c94
+ 004bf618 bytes 0e631e94
- 0049c720 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049c720 ["INT_ADD", "register:40f0:8", ["const:49c720:8", "const:4:8"]]
- 0049c720 ["CALLIND", null, ["register:0:8"]]
+ 004bf5b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf5b8 ["INT_ADD", "register:40f0:8", ["const:4bf5b8:8", "const:4:8"]]
+ 004bf5b8 ["CALLIND", null, ["register:0:8"]]
- 0049c720 bytes 00013fd6
+ 004bf5b8 bytes 00013fd6
- 0049c744 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049c744 ["INT_ADD", "register:40f0:8", ["const:49c744:8", "const:4:8"]]
- 0049c744 ["CALLIND", null, ["register:0:8"]]
+ 004bf5dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf5dc ["INT_ADD", "register:40f0:8", ["const:4bf5dc:8", "const:4:8"]]
+ 004bf5dc ["CALLIND", null, ["register:0:8"]]
- 0049c744 bytes 00013fd6
+ 004bf5dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a00acc5f4d806bb498423393452a4d3"></a>

### [`0049c784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c784.md) → [`004bf61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf61c.md) _ZN5Botan14ECB_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.37% / 新版 92.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf748",
      "incomplete_value": false,
      "site": "004bf768",
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
      "definition_site": "0049c8b0",
      "incomplete_value": false,
      "site": "0049c8d0",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf750",
      "incomplete_value": false,
      "site": "004bf768",
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
      "definition_site": "0049c8b8",
      "incomplete_value": false,
      "site": "0049c8d0",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf758",
      "incomplete_value": false,
      "site": "004bf768",
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
      "definition_site": "0049c8c0",
      "incomplete_value": false,
      "site": "0049c8d0",
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
      "004bf748",
      "PARAM",
      [
        "storage",
        "0029d49b",
        null,
        "string"
      ]
    ],
    [
      "004bf750",
      "PARAM",
      [
        "storage",
        "002a4470",
        null,
        "string"
      ]
    ],
    [
      "004bf758",
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
      "004bf748",
      "PARAM",
      [
        "storage",
        "002ad725",
        null,
        "string"
      ]
    ],
    [
      "004bf750",
      "PARAM",
      [
        "storage",
        "002b4cdd",
        null,
        "string"
      ]
    ],
    [
      "004bf758",
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

- 旧版 [`0049c8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c784.md#insn-0049c8d0) · [`0049c8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c784.md#insn-0049c8fc) · [`0049c950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c784.md#insn-0049c950)
- 新版 `004bf768`（命令位置の公開資料なし） · `004bf794`（命令位置の公開資料なし） · `004bf7e8`（命令位置の公開資料なし）

~~~diff
- 0049c8d0 ["INT_ADD", "register:40f0:8", ["const:49c8d0:8", "const:4:8"]]
- 0049c8d0 ["CALL", null, ["callee:00c58250:8"]]
+ 004bf768 ["INT_ADD", "register:40f0:8", ["const:4bf768:8", "const:4:8"]]
+ 004bf768 ["CALL", null, ["callee:00c58250:8"]]
- 0049c8d0 bytes ccfb1c94
+ 004bf768 bytes ba621e94
- 0049c8fc ["INT_ADD", "register:40f0:8", ["const:49c8fc:8", "const:4:8"]]
- 0049c8fc ["CALL", null, ["callee:00c57b60:8"]]
+ 004bf794 ["INT_ADD", "register:40f0:8", ["const:4bf794:8", "const:4:8"]]
+ 004bf794 ["CALL", null, ["callee:00c57b60:8"]]
- 0049c8fc bytes 05fa1c94
+ 004bf794 bytes f3601e94
- 0049c950 ["INT_ADD", "register:40f0:8", ["const:49c950:8", "const:4:8"]]
- 0049c950 ["CALL", null, ["callee:00c57b10:8"]]
+ 004bf7e8 ["INT_ADD", "register:40f0:8", ["const:4bf7e8:8", "const:4:8"]]
+ 004bf7e8 ["CALL", null, ["callee:00c57b10:8"]]
- 0049c950 bytes dcf91c94
+ 004bf7e8 bytes ca601e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61b2a94683849b8e0c4f262920ba32d7"></a>

### [`0049ca18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ca18.md) → [`004bf8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf8b0.md) _ZN5Botan14ECB_Decryption7processEPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf918",
      "incomplete_value": false,
      "site": "004bf938",
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
      "definition_site": "0049ca80",
      "incomplete_value": false,
      "site": "0049caa0",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf920",
      "incomplete_value": false,
      "site": "004bf938",
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
      "definition_site": "0049ca88",
      "incomplete_value": false,
      "site": "0049caa0",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf928",
      "incomplete_value": false,
      "site": "004bf938",
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
      "definition_site": "0049ca90",
      "incomplete_value": false,
      "site": "0049caa0",
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
      "004bf918",
      "PARAM",
      [
        "storage",
        "00298d95",
        null,
        "string"
      ]
    ],
    [
      "004bf920",
      "PARAM",
      [
        "storage",
        "002a052d",
        null,
        "string"
      ]
    ],
    [
      "004bf928",
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
      "004bf918",
      "PARAM",
      [
        "storage",
        "002a8b53",
        null,
        "string"
      ]
    ],
    [
      "004bf920",
      "PARAM",
      [
        "storage",
        "002b0ae7",
        null,
        "string"
      ]
    ],
    [
      "004bf928",
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

- 旧版 [`0049caa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ca18.md#insn-0049caa0) · [`0049ca40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ca18.md#insn-0049ca40) · [`0049ca64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ca18.md#insn-0049ca64)
- 新版 `004bf938`（命令位置の公開資料なし） · `004bf8d8`（命令位置の公開資料なし） · `004bf8fc`（命令位置の公開資料なし）

~~~diff
- 0049caa0 ["INT_ADD", "register:40f0:8", ["const:49caa0:8", "const:4:8"]]
- 0049caa0 ["CALL", null, ["callee:00c58250:8"]]
+ 004bf938 ["INT_ADD", "register:40f0:8", ["const:4bf938:8", "const:4:8"]]
+ 004bf938 ["CALL", null, ["callee:00c58250:8"]]
- 0049caa0 bytes 58fb1c94
+ 004bf938 bytes 46621e94
- 0049ca40 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049ca40 ["INT_ADD", "register:40f0:8", ["const:49ca40:8", "const:4:8"]]
- 0049ca40 ["CALLIND", null, ["register:0:8"]]
+ 004bf8d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf8d8 ["INT_ADD", "register:40f0:8", ["const:4bf8d8:8", "const:4:8"]]
+ 004bf8d8 ["CALLIND", null, ["register:0:8"]]
- 0049ca40 bytes 00013fd6
+ 004bf8d8 bytes 00013fd6
- 0049ca64 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049ca64 ["INT_ADD", "register:40f0:8", ["const:49ca64:8", "const:4:8"]]
- 0049ca64 ["CALLIND", null, ["register:0:8"]]
+ 004bf8fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf8fc ["INT_ADD", "register:40f0:8", ["const:4bf8fc:8", "const:4:8"]]
+ 004bf8fc ["CALLIND", null, ["register:0:8"]]
- 0049ca64 bytes 00013fd6
+ 004bf8fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae2c677f836917086512116ff4ea3d1f"></a>

### [`0049caa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049caa4.md) → [`004bf93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf93c.md) _ZN5Botan14ECB_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bfaac",
      "incomplete_value": false,
      "site": "004bfab4",
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
      "definition_site": "0049cc14",
      "incomplete_value": false,
      "site": "0049cc1c",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bfafc",
      "incomplete_value": true,
      "site": "004bfb08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049cc64",
      "incomplete_value": true,
      "site": "0049cc70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bfaf8",
      "incomplete_value": false,
      "site": "004bfb08",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0049cc60",
      "incomplete_value": false,
      "site": "0049cc70",
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
      "004bfaac",
      "PARAM",
      [
        "storage",
        "002af9ef",
        null,
        "string"
      ]
    ],
    [
      "004bfaf8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004bfafc",
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
      "004bfaac",
      "PARAM",
      [
        "storage",
        "002c1013",
        null,
        "string"
      ]
    ],
    [
      "004bfaf8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bfafc",
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

- 旧版 [`0049cc1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049caa4.md#insn-0049cc1c) · [`0049cc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049caa4.md#insn-0049cc70) · [`0049cca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049caa4.md#insn-0049cca8)
- 新版 `004bfab4`（命令位置の公開資料なし） · `004bfb08`（命令位置の公開資料なし） · `004bfb40`（命令位置の公開資料なし）

~~~diff
- 0049cc1c ["INT_ADD", "register:40f0:8", ["const:49cc1c:8", "const:4:8"]]
- 0049cc1c ["CALL", null, ["callee:00c57b70:8"]]
+ 004bfab4 ["INT_ADD", "register:40f0:8", ["const:4bfab4:8", "const:4:8"]]
+ 004bfab4 ["CALL", null, ["callee:00c57b70:8"]]
- 0049cc1c bytes 41f91c94
+ 004bfab4 bytes 2f601e94
- 0049cc70 ["INT_ADD", "register:40f0:8", ["const:49cc70:8", "const:4:8"]]
- 0049cc70 ["CALL", null, ["callee:00c57b10:8"]]
+ 004bfb08 ["INT_ADD", "register:40f0:8", ["const:4bfb08:8", "const:4:8"]]
+ 004bfb08 ["CALL", null, ["callee:00c57b10:8"]]
- 0049cc70 bytes 14f91c94
+ 004bfb08 bytes 02601e94
- 0049cca8 ["INT_ADD", "register:40f0:8", ["const:49cca8:8", "const:4:8"]]
- 0049cca8 ["CALL", null, ["callee:00c58250:8"]]
+ 004bfb40 ["INT_ADD", "register:40f0:8", ["const:4bfb40:8", "const:4:8"]]
+ 004bfb40 ["CALL", null, ["callee:00c58250:8"]]
- 0049cca8 bytes d6fa1c94
+ 004bfb40 bytes c4611e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c06cd6b2485bc41f18bb9b029cf195d4"></a>

### [`0049ce2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ce2c.md) → [`004bfcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfcc4.md) _ZN5Botan13EMSA_PKCS1v1511encoding_ofERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmRNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0049cf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cf60.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004bfdf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfdf8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.61% / 新版 96.61%

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
      "definition_site": "004bfd64",
      "incomplete_value": false,
      "site": "004bfd6c",
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
            "const:cec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049cecc",
      "incomplete_value": false,
      "site": "0049ced4",
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
            "const:47f:8"
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
      "definition_site": "004bfd9c",
      "incomplete_value": true,
      "site": "004bfda8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049cf04",
      "incomplete_value": true,
      "site": "0049cf10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bfd98",
      "incomplete_value": false,
      "site": "004bfda8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0049cf00",
      "incomplete_value": false,
      "site": "0049cf10",
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
      "004bfd64",
      "PARAM",
      [
        "storage",
        "002a447f",
        null,
        "string"
      ]
    ],
    [
      "004bfd98",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004bfd9c",
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
      "004bfd64",
      "PARAM",
      [
        "storage",
        "002b4cec",
        null,
        "string"
      ]
    ],
    [
      "004bfd98",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bfd9c",
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

- 旧版 [`0049ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ce2c.md#insn-0049ced4) · [`0049cf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ce2c.md#insn-0049cf10) · [`0049ce74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ce2c.md#insn-0049ce74)
- 新版 `004bfd6c`（命令位置の公開資料なし） · `004bfda8`（命令位置の公開資料なし） · `004bfd0c`（命令位置の公開資料なし）

~~~diff
- 0049ced4 ["INT_ADD", "register:40f0:8", ["const:49ced4:8", "const:4:8"]]
- 0049ced4 ["CALL", null, ["callee:0043dd98:8"]]
+ 004bfd6c ["INT_ADD", "register:40f0:8", ["const:4bfd6c:8", "const:4:8"]]
+ 004bfd6c ["CALL", null, ["callee:0043dd98:8"]]
- 0049ced4 bytes f1f8fd97
+ 004bfd6c bytes 0bf8fd97
- 0049cf10 ["INT_ADD", "register:40f0:8", ["const:49cf10:8", "const:4:8"]]
- 0049cf10 ["CALL", null, ["callee:00c57b10:8"]]
+ 004bfda8 ["INT_ADD", "register:40f0:8", ["const:4bfda8:8", "const:4:8"]]
+ 004bfda8 ["CALL", null, ["callee:00c57b10:8"]]
- 0049cf10 bytes 6cf81c94
+ 004bfda8 bytes 5a5f1e94
- 0049ce74 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049ce74 ["INT_ADD", "register:40f0:8", ["const:49ce74:8", "const:4:8"]]
- 0049ce74 ["CALLIND", null, ["register:0:8"]]
+ 004bfd0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bfd0c ["INT_ADD", "register:40f0:8", ["const:4bfd0c:8", "const:4:8"]]
+ 004bfd0c ["CALLIND", null, ["register:0:8"]]
- 0049ce74 bytes 00013fd6
+ 004bfd0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2231053ac21504878ab73699609105e5"></a>

### [`0049cf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cf60.md) → [`004bfdf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfdf8.md) FUN_004bfdf8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0049ce2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049ce2c.md) [`0049d19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d19c.md) [`0049e834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e834.md) [`0049e84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e84c.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 4件 [`004bfcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfcc4.md) [`004c0034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0034.md) [`004c16cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c16cc.md) [`004c16e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c16e4.md) · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.04% / 新版 95.04%

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
      "definition_site": "004bff58",
      "incomplete_value": false,
      "site": "004bff60",
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
            "const:c51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d0c0",
      "incomplete_value": false,
      "site": "0049d0c8",
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
            "const:e93:8"
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
      "definition_site": "004bff90",
      "incomplete_value": true,
      "site": "004bff9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049d0f8",
      "incomplete_value": true,
      "site": "0049d104",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bff8c",
      "incomplete_value": false,
      "site": "004bff9c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0049d0f4",
      "incomplete_value": false,
      "site": "0049d104",
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
      "004bff58",
      "PARAM",
      [
        "storage",
        "00298e93",
        null,
        "string"
      ]
    ],
    [
      "004bff8c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004bff90",
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
      "004bff58",
      "PARAM",
      [
        "storage",
        "002a8c51",
        null,
        "string"
      ]
    ],
    [
      "004bff8c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bff90",
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

- 旧版 [`0049d0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cf60.md#insn-0049d0c8) · [`0049d104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cf60.md#insn-0049d104) · [`0049d13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cf60.md#insn-0049d13c)
- 新版 `004bff60`（命令位置の公開資料なし） · `004bff9c`（命令位置の公開資料なし） · `004bffd4`（命令位置の公開資料なし）

~~~diff
- 0049d0c8 ["INT_ADD", "register:40f0:8", ["const:49d0c8:8", "const:4:8"]]
- 0049d0c8 ["CALL", null, ["callee:0043dd98:8"]]
+ 004bff60 ["INT_ADD", "register:40f0:8", ["const:4bff60:8", "const:4:8"]]
+ 004bff60 ["CALL", null, ["callee:0043dd98:8"]]
- 0049d0c8 bytes 74f8fd97
+ 004bff60 bytes 8ef7fd97
- 0049d104 ["INT_ADD", "register:40f0:8", ["const:49d104:8", "const:4:8"]]
- 0049d104 ["CALL", null, ["callee:00c57b10:8"]]
+ 004bff9c ["INT_ADD", "register:40f0:8", ["const:4bff9c:8", "const:4:8"]]
+ 004bff9c ["CALL", null, ["callee:00c57b10:8"]]
- 0049d104 bytes eff71c94
+ 004bff9c bytes dd5e1e94
- 0049d13c ["INT_ADD", "register:40f0:8", ["const:49d13c:8", "const:4:8"]]
- 0049d13c ["CALL", null, ["callee:00c58250:8"]]
+ 004bffd4 ["INT_ADD", "register:40f0:8", ["const:4bffd4:8", "const:4:8"]]
+ 004bffd4 ["CALL", null, ["callee:00c58250:8"]]
- 0049d13c bytes b1f91c94
+ 004bffd4 bytes 9f601e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f594fae32794b18602eb6a45c3ba355"></a>

### [`0049d19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d19c.md) → [`004c0034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0034.md) _ZN5Botan13EMSA_PKCS1v156verifyERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEES7_m

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0049cf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cf60.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004bfdf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfdf8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c00f8",
      "incomplete_value": true,
      "site": "004c00f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049d260",
      "incomplete_value": true,
      "site": "0049d260",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c00e8",
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
      "004c00e8",
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

- 旧版 [`0049d260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d19c.md#insn-0049d260) · [`0049d1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d19c.md#insn-0049d1e4) · [`0049d204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d19c.md#insn-0049d204)
- 新版 `004c00f8`（命令位置の公開資料なし） · `004c007c`（命令位置の公開資料なし） · `004c009c`（命令位置の公開資料なし）

~~~diff
- 0049d260 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049d260 ["INT_ADD", "register:40f0:8", ["const:49d260:8", "const:4:8"]]
- 0049d260 ["CALLIND", null, ["register:0:8"]]
+ 004c00f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c00f8 ["INT_ADD", "register:40f0:8", ["const:4c00f8:8", "const:4:8"]]
+ 004c00f8 ["CALLIND", null, ["register:0:8"]]
- 0049d260 bytes 20013fd6
+ 004c00f8 bytes 20013fd6
- 0049d1e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049d1e4 ["INT_ADD", "register:40f0:8", ["const:49d1e4:8", "const:4:8"]]
- 0049d1e4 ["CALLIND", null, ["register:0:8"]]
+ 004c007c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c007c ["INT_ADD", "register:40f0:8", ["const:4c007c:8", "const:4:8"]]
+ 004c007c ["CALLIND", null, ["register:0:8"]]
- 0049d1e4 bytes 00013fd6
+ 004c007c bytes 00013fd6
- 0049d204 ["INT_ADD", "register:40f0:8", ["const:49d204:8", "const:4:8"]]
- 0049d204 ["CALL", null, ["callee:004bfdf8:8"]]
+ 004c009c ["INT_ADD", "register:40f0:8", ["const:4c009c:8", "const:4:8"]]
+ 004c009c ["CALL", null, ["callee:004bfdf8:8"]]
- 0049d204 bytes 57ffff97
+ 004c009c bytes 57ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a6aea768e936053f9fc6b50038e4d26"></a>

### [`0049d2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d2b0.md) → [`004c0148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0148.md) _ZNK5Botan13EMSA_PKCS1v1515config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0049d8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d8dc.md) [`0049da90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049da90.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004c0774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0774.md) [`004c0928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0928.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.96% / 新版 96.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c0284",
      "incomplete_value": true,
      "site": "004c0284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049d3ec",
      "incomplete_value": true,
      "site": "0049d3ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c02cc",
      "incomplete_value": false,
      "site": "004c02d4",
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
      "definition_site": "0049d434",
      "incomplete_value": false,
      "site": "0049d43c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c0488",
      "incomplete_value": false,
      "site": "004c0490",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d5f0",
      "incomplete_value": false,
      "site": "0049d5f8",
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
            "const:745:8"
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
      "004c0278",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004c0284",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c02cc",
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
      "004c0278",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004c0284",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c02cc",
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

- 旧版 [`0049d43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d2b0.md#insn-0049d43c) · [`0049d5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d2b0.md#insn-0049d5f8) · [`0049d634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d2b0.md#insn-0049d634)
- 新版 `004c02d4`（命令位置の公開資料なし） · `004c0490`（命令位置の公開資料なし） · `004c04cc`（命令位置の公開資料なし）

~~~diff
- 0049d43c ["INT_ADD", "register:40f0:8", ["const:49d43c:8", "const:4:8"]]
- 0049d43c ["CALL", null, ["callee:00c57b70:8"]]
+ 004c02d4 ["INT_ADD", "register:40f0:8", ["const:4c02d4:8", "const:4:8"]]
+ 004c02d4 ["CALL", null, ["callee:00c57b70:8"]]
- 0049d43c bytes 39f71c94
+ 004c02d4 bytes 275e1e94
- 0049d5f8 ["INT_ADD", "register:40f0:8", ["const:49d5f8:8", "const:4:8"]]
- 0049d5f8 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c0490 ["INT_ADD", "register:40f0:8", ["const:4c0490:8", "const:4:8"]]
+ 004c0490 ["CALL", null, ["callee:0043dd98:8"]]
- 0049d5f8 bytes 28f7fd97
+ 004c0490 bytes 42f6fd97
- 0049d634 ["INT_ADD", "register:40f0:8", ["const:49d634:8", "const:4:8"]]
- 0049d634 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c04cc ["INT_ADD", "register:40f0:8", ["const:4c04cc:8", "const:4:8"]]
+ 004c04cc ["CALL", null, ["callee:00c57b10:8"]]
- 0049d634 bytes a3f61c94
+ 004c04cc bytes 915d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-247561a55fbde551d74399264ab5112b"></a>

### [`0049da90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049da90.md) → [`004c0928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0928.md) FUN_004c0928

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049d2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d2b0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 1件 [`004c0148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0148.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

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
      "definition_site": "004c0960",
      "incomplete_value": false,
      "site": "004c096c",
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
            "const:dcc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049dac8",
      "incomplete_value": false,
      "site": "0049dad4",
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
            "const:aa6:8"
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
      "definition_site": "004c098c",
      "incomplete_value": false,
      "site": "004c0994",
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
      "definition_site": "0049daf4",
      "incomplete_value": false,
      "site": "0049dafc",
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
      "004c0960",
      "PARAM",
      [
        "storage",
        "002adaa6",
        null,
        "string"
      ]
    ],
    [
      "004c098c",
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
      "004c0960",
      "PARAM",
      [
        "storage",
        "002bedcc",
        null,
        "string"
      ]
    ],
    [
      "004c098c",
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

- 旧版 [`0049dad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049da90.md#insn-0049dad4) · [`0049dafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049da90.md#insn-0049dafc) · [`0049dac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049da90.md#insn-0049dac0)
- 新版 `004c096c`（命令位置の公開資料なし） · `004c0994`（命令位置の公開資料なし） · `004c0958`（命令位置の公開資料なし）

~~~diff
- 0049dad4 ["INT_ADD", "register:40f0:8", ["const:49dad4:8", "const:4:8"]]
- 0049dad4 ["CALL", null, ["callee:00c57b60:8"]]
+ 004c096c ["INT_ADD", "register:40f0:8", ["const:4c096c:8", "const:4:8"]]
+ 004c096c ["CALL", null, ["callee:00c57b60:8"]]
- 0049dad4 bytes 8ff51c94
+ 004c096c bytes 7d5c1e94
- 0049dafc ["INT_ADD", "register:40f0:8", ["const:49dafc:8", "const:4:8"]]
- 0049dafc ["CALL", null, ["callee:00c57b70:8"]]
+ 004c0994 ["INT_ADD", "register:40f0:8", ["const:4c0994:8", "const:4:8"]]
+ 004c0994 ["CALL", null, ["callee:00c57b70:8"]]
- 0049dafc bytes 89f51c94
+ 004c0994 bytes 775c1e94
- 0049dac0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049dac0 ["INT_ADD", "register:40f0:8", ["const:49dac0:8", "const:4:8"]]
- 0049dac0 ["CALLIND", null, ["register:0:8"]]
+ 004c0958 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c0958 ["INT_ADD", "register:40f0:8", ["const:4c0958:8", "const:4:8"]]
+ 004c0958 ["CALLIND", null, ["register:0:8"]]
- 0049dac0 bytes 20013fd6
+ 004c0958 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-413739f5d79ad038dea434d47660ea96"></a>

### [`0049dbe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dbe4.md) → [`004c0a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0a7c.md) _ZN5Botan13EMSA_PKCS1v15C2EPNS_12HashFunctionE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6c0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf90.md)
- 新版 呼出元 1件 [`00c59110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59110.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c589e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c0aac",
      "incomplete_value": true,
      "site": "004c0ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049dc14",
      "incomplete_value": true,
      "site": "0049dc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c0aa0",
      "READ",
      [
        "storage",
        "00c1b060",
        null,
        "pointer"
      ]
    ],
    [
      "004c0ab8",
      "DATA",
      [
        "storage",
        "00be95b8",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c0aa0",
      "READ",
      [
        "storage",
        "00c9aa50",
        null,
        "pointer"
      ]
    ],
    [
      "004c0ab8",
      "DATA",
      [
        "storage",
        "00c66178",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049dbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dbe4.md#insn-0049dbfc) · [`0049dc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dbe4.md#insn-0049dc08) · [`0049dc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dbe4.md#insn-0049dc0c)
- 新版 `004c0a94`（命令位置の公開資料なし） · `004c0aa0`（命令位置の公開資料なし）

~~~diff
- 0049dbfc ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004c0a94 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0049dbfc bytes e93b00d0
+ 004c0a94 bytes c93e00d0
- 0049dc08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:60:8"]]
- 0049dc08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c0aa0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a50:8"]]
+ 004c0aa0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049dc08 bytes 293140f9
+ 004c0aa0 bytes 292945f9
- 0049dc0c ["COPY", "register:4098:8", ["register:4000:8"]]
- 0049dc0c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89ac16bdbd3300139db7f8a8b6906465"></a>

### [`0049dd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dd0c.md) → [`004c0ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0ba4.md) _ZN5Botan12pkcs_hash_idERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf90.md) · 呼出先 9件 [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`004a92b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a92b4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c589e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589e0.md) · 呼出先 9件 [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`004cc14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc14c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.57% / 新版 90.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c0cfc",
      "incomplete_value": true,
      "site": "004c0d0c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:e86:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049de64",
      "incomplete_value": true,
      "site": "0049de74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:776:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c0dbc",
      "incomplete_value": false,
      "site": "004c0dc4",
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
            "const:77e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049df24",
      "incomplete_value": false,
      "site": "0049df2c",
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
            "const:3f9:8"
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
      "definition_site": "004c0dec",
      "incomplete_value": false,
      "site": "004c0df4",
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
      "definition_site": "0049df54",
      "incomplete_value": false,
      "site": "0049df5c",
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
      "004c0cfc",
      "READ",
      [
        "storage",
        "002b9776",
        null,
        null
      ]
    ],
    [
      "004c0dbc",
      "PARAM",
      [
        "storage",
        "0029e3f9",
        null,
        "string"
      ]
    ],
    [
      "004c0de0",
      "PARAM",
      [
        "storage",
        "002b97a6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c0cfc",
      "READ",
      [
        "storage",
        "002cae86",
        null,
        null
      ]
    ],
    [
      "004c0dbc",
      "PARAM",
      [
        "storage",
        "002ae77e",
        null,
        "string"
      ]
    ],
    [
      "004c0de0",
      "PARAM",
      [
        "storage",
        "002caeb6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049df2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dd0c.md#insn-0049df2c) · [`0049df5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dd0c.md#insn-0049df5c) · [`0049df8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dd0c.md#insn-0049df8c)
- 新版 `004c0dc4`（命令位置の公開資料なし） · `004c0df4`（命令位置の公開資料なし） · `004c0e24`（命令位置の公開資料なし）

~~~diff
- 0049df2c ["INT_ADD", "register:40f0:8", ["const:49df2c:8", "const:4:8"]]
- 0049df2c ["CALL", null, ["callee:00441e54:8"]]
+ 004c0dc4 ["INT_ADD", "register:40f0:8", ["const:4c0dc4:8", "const:4:8"]]
+ 004c0dc4 ["CALL", null, ["callee:00441e54:8"]]
- 0049df2c bytes 0a05fe97
+ 004c0dc4 bytes 2404fe97
- 0049df5c ["INT_ADD", "register:40f0:8", ["const:49df5c:8", "const:4:8"]]
- 0049df5c ["CALL", null, ["callee:00441e54:8"]]
+ 004c0df4 ["INT_ADD", "register:40f0:8", ["const:4c0df4:8", "const:4:8"]]
+ 004c0df4 ["CALL", null, ["callee:00441e54:8"]]
- 0049df5c bytes fe04fe97
+ 004c0df4 bytes 1804fe97
- 0049df8c ["INT_ADD", "register:40f0:8", ["const:49df8c:8", "const:4:8"]]
- 0049df8c ["CALL", null, ["callee:00441e54:8"]]
+ 004c0e24 ["INT_ADD", "register:40f0:8", ["const:4c0e24:8", "const:4:8"]]
+ 004c0e24 ["CALL", null, ["callee:00441e54:8"]]
- 0049df8c bytes f204fe97
+ 004c0e24 bytes 0c04fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3a5bd298ef2a27a3220ea35e9967a08"></a>

### [`0049e24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e24c.md) → [`004c10e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c10e4.md) _ZN5Botan17EMSA_PKCS1v15_RawC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc6b0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf90.md) [`00bdbfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfa0.md)
- 新版 呼出元 1件 [`00c59100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59100.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c589e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589e0.md) [`00c589f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c1118",
      "incomplete_value": true,
      "site": "004c1120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049e280",
      "incomplete_value": true,
      "site": "0049e288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c1108",
      "READ",
      [
        "storage",
        "00c1b068",
        null,
        "pointer"
      ]
    ],
    [
      "004c1120",
      "DATA",
      [
        "storage",
        "00be9610",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c1108",
      "READ",
      [
        "storage",
        "00c9aa58",
        null,
        "pointer"
      ]
    ],
    [
      "004c1120",
      "DATA",
      [
        "storage",
        "00c661d0",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049e264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e24c.md#insn-0049e264) · [`0049e270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e24c.md#insn-0049e270) · [`0049e2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e24c.md#insn-0049e2c8)
- 新版 `004c10fc`（命令位置の公開資料なし） · `004c1108`（命令位置の公開資料なし） · `004c1160`（命令位置の公開資料なし）

~~~diff
- 0049e264 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c10fc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0049e264 bytes e83b00b0
+ 004c10fc bytes c83e00b0
- 0049e270 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:68:8"]]
- 0049e270 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c1108 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a58:8"]]
+ 004c1108 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0049e270 bytes 083540f9
+ 004c1108 bytes 082d45f9
- 0049e2c8 ["INT_ADD", "register:40f0:8", ["const:49e2c8:8", "const:4:8"]]
- 0049e2c8 ["CALL", null, ["callee:00c589e0:8"]]
+ 004c1160 ["INT_ADD", "register:40f0:8", ["const:4c1160:8", "const:4:8"]]
+ 004c1160 ["CALL", null, ["callee:00c589e0:8"]]
- 0049e2c8 bytes 32f71c94
+ 004c1160 bytes 205e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-398301a6742c672a321d09047ccc2778"></a>

### [`0049e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md) → [`004c128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c128c.md) _ZN5Botan12HashFunction6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfa0.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00499040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499040.md) [`004a8854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8854.md) [`004a8a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8a10.md) [`004a8bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8bc4.md)
- 新版 呼出元 1件 [`00c589f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589f0.md) · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004bbed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbed8.md) [`004cb6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb6ec.md) [`004cb8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb8a8.md) [`004cba5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cba5c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.32% / 新版 99.32%

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
      "site": "004c14d0",
      "value": [
        "leaf",
        "ram:4cb8a8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0049e638",
      "value": [
        "leaf",
        "ram:4a8a10:8"
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
      "004c14d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004a8a10"
      ]
    ]
  ],
  "added": [
    [
      "004c14d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004cb8a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049e638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md#insn-0049e638) · [`0049e52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md#insn-0049e52c) · [`0049e534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md#insn-0049e534)
- 新版 `004c14d0`（命令位置の公開資料なし） · `004c13c4`（命令位置の公開資料なし） · `004c13cc`（命令位置の公開資料なし）

~~~diff
- 0049e638 ["INT_ADD", "register:40f0:8", ["const:49e638:8", "const:4:8"]]
- 0049e638 ["CALL", null, ["ram:4a8a10:8"]]
+ 004c14d0 ["INT_ADD", "register:40f0:8", ["const:4c14d0:8", "const:4:8"]]
+ 004c14d0 ["CALL", null, ["ram:4cb8a8:8"]]
- 0049e638 bytes f6280094
+ 004c14d0 bytes f6280094
- 0049e52c ["INT_ADD", "register:40f0:8", ["const:49e52c:8", "const:4:8"]]
- 0049e52c ["CALL", null, ["callee:00c57a90:8"]]
+ 004c13c4 ["INT_ADD", "register:40f0:8", ["const:4c13c4:8", "const:4:8"]]
+ 004c13c4 ["CALL", null, ["callee:00c57a90:8"]]
- 0049e52c bytes c5f21c94
+ 004c13c4 bytes b3591e94
- 0049e534 ["INT_ADD", "register:40f0:8", ["const:49e534:8", "const:4:8"]]
- 0049e534 ["CALL", null, ["callee:004cba5c:8"]]
+ 004c13cc ["INT_ADD", "register:40f0:8", ["const:4c13cc:8", "const:4:8"]]
+ 004c13cc ["CALL", null, ["callee:004cba5c:8"]]
- 0049e534 bytes a4290094
+ 004c13cc bytes a4290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edc5e691ebd24ac35f4b5b9a1c233ca0"></a>

### [`0049e708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e708.md) → [`004c15a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c15a0.md) _ZN5Botan17EMSA_PKCS1v15_Raw8raw_dataEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
      "definition_site": "004c1628",
      "incomplete_value": false,
      "site": "004c1630",
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
            "const:f84:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049e790",
      "incomplete_value": false,
      "site": "0049e798",
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
            "const:556:8"
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
      "definition_site": "004c1664",
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
      "definition_site": "0049e7cc",
      "incomplete_value": true,
      "site": "0049e7d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c1660",
      "incomplete_value": false,
      "site": "004c1670",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0049e7c8",
      "incomplete_value": false,
      "site": "0049e7d8",
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
      "004c1628",
      "PARAM",
      [
        "storage",
        "002a5556",
        null,
        "string"
      ]
    ],
    [
      "004c1660",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c1664",
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
      "004c1628",
      "PARAM",
      [
        "storage",
        "002b5f84",
        null,
        "string"
      ]
    ],
    [
      "004c1660",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c1664",
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

- 旧版 [`0049e798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e708.md#insn-0049e798) · [`0049e7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e708.md#insn-0049e7d8) · [`0049e784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e708.md#insn-0049e784)
- 新版 `004c1630`（命令位置の公開資料なし） · `004c1670`（命令位置の公開資料なし） · `004c161c`（命令位置の公開資料なし）

~~~diff
- 0049e798 ["INT_ADD", "register:40f0:8", ["const:49e798:8", "const:4:8"]]
- 0049e798 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c1630 ["INT_ADD", "register:40f0:8", ["const:4c1630:8", "const:4:8"]]
+ 004c1630 ["CALL", null, ["callee:0043dd98:8"]]
- 0049e798 bytes c0f2fd97
+ 004c1630 bytes daf1fd97
- 0049e7d8 ["INT_ADD", "register:40f0:8", ["const:49e7d8:8", "const:4:8"]]
- 0049e7d8 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c1670 ["INT_ADD", "register:40f0:8", ["const:4c1670:8", "const:4:8"]]
+ 004c1670 ["CALL", null, ["callee:00c57b10:8"]]
- 0049e7d8 bytes 3af21c94
+ 004c1670 bytes 28591e94
- 0049e784 ["INT_ADD", "register:40f0:8", ["const:49e784:8", "const:4:8"]]
- 0049e784 ["CALL", null, ["callee:00c57af0:8"]]
+ 004c161c ["INT_ADD", "register:40f0:8", ["const:4c161c:8", "const:4:8"]]
+ 004c161c ["CALL", null, ["callee:00c57af0:8"]]
- 0049e784 bytes 47f21c94
+ 004c161c bytes 35591e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0a3bb338975c5ae6026ac36ef7784d6"></a>

### [`0049e948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e948.md) → [`004c17e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c17e0.md) _ZN5Botan4PSSRC2EPNS_12HashFunctionE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c1800",
      "incomplete_value": true,
      "site": "004c1804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049e968",
      "incomplete_value": true,
      "site": "0049e96c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c17f8",
      "READ",
      [
        "storage",
        "00c1b070",
        null,
        "pointer"
      ]
    ],
    [
      "004c1804",
      "DATA",
      [
        "storage",
        "00be9668",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c17f8",
      "READ",
      [
        "storage",
        "00c9aa60",
        null,
        "pointer"
      ]
    ],
    [
      "004c1804",
      "DATA",
      [
        "storage",
        "00c66228",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049e954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e948.md#insn-0049e954) · [`0049e960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e948.md#insn-0049e960) · [`0049e978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e948.md#insn-0049e978)
- 新版 `004c17ec`（命令位置の公開資料なし） · `004c17f8`（命令位置の公開資料なし） · `004c1810`（命令位置の公開資料なし）

~~~diff
- 0049e954 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c17ec ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0049e954 bytes e83b00b0
+ 004c17ec bytes c83e00b0
- 0049e960 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:70:8"]]
- 0049e960 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c17f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a60:8"]]
+ 004c17f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0049e960 bytes 083940f9
+ 004c17f8 bytes 083145f9
- 0049e978 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049e978 ["INT_ADD", "register:40f0:8", ["const:49e978:8", "const:4:8"]]
- 0049e978 ["CALLIND", null, ["register:0:8"]]
+ 004c1810 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c1810 ["INT_ADD", "register:40f0:8", ["const:4c1810:8", "const:4:8"]]
+ 004c1810 ["CALLIND", null, ["register:0:8"]]
- 0049e978 bytes 00013fd6
+ 004c1810 bytes 00013fd6
~~~


<a id="compare-0acaa6a6728c6f5b33735c5dc48f8f93"></a>

### [`0049eb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049eb38.md) → [`004c19d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c19d0.md) FUN_004c19d0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0049ea3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049ea3c.md) [`0049ffc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049ffc4.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 2件 [`004c18d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c18d4.md) [`004c2e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2e5c.md) · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.30% / 新版 98.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c1c80",
      "incomplete_value": true,
      "site": "004c1c80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049ede8",
      "incomplete_value": true,
      "site": "0049ede8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 18,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c1cd0",
      "incomplete_value": false,
      "site": "004c1cd8",
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
            "const:662:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ee38",
      "incomplete_value": false,
      "site": "0049ee40",
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
            "const:73f:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c1d0c",
      "incomplete_value": true,
      "site": "004c1d18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049ee74",
      "incomplete_value": true,
      "site": "0049ee80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c1c70",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c1cd0",
      "PARAM",
      [
        "storage",
        "002ab73f",
        null,
        "string"
      ]
    ],
    [
      "004c1d08",
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
      "004c1c70",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004c1cd0",
      "PARAM",
      [
        "storage",
        "002bc662",
        null,
        "string"
      ]
    ],
    [
      "004c1d08",
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

- 旧版 [`0049ede8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049eb38.md#insn-0049ede8) · [`0049ee40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049eb38.md#insn-0049ee40) · [`0049ee80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049eb38.md#insn-0049ee80)
- 新版 `004c1c80`（命令位置の公開資料なし） · `004c1cd8`（命令位置の公開資料なし） · `004c1d18`（命令位置の公開資料なし）

~~~diff
- 0049ede8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049ede8 ["INT_ADD", "register:40f0:8", ["const:49ede8:8", "const:4:8"]]
- 0049ede8 ["CALLIND", null, ["register:0:8"]]
+ 004c1c80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c1c80 ["INT_ADD", "register:40f0:8", ["const:4c1c80:8", "const:4:8"]]
+ 004c1c80 ["CALLIND", null, ["register:0:8"]]
- 0049ede8 bytes 20013fd6
+ 004c1c80 bytes 20013fd6
- 0049ee40 ["INT_ADD", "register:40f0:8", ["const:49ee40:8", "const:4:8"]]
- 0049ee40 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c1cd8 ["INT_ADD", "register:40f0:8", ["const:4c1cd8:8", "const:4:8"]]
+ 004c1cd8 ["CALL", null, ["callee:0043dd98:8"]]
- 0049ee40 bytes 16f1fd97
+ 004c1cd8 bytes 30f0fd97
- 0049ee80 ["INT_ADD", "register:40f0:8", ["const:49ee80:8", "const:4:8"]]
- 0049ee80 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c1d18 ["INT_ADD", "register:40f0:8", ["const:4c1d18:8", "const:4:8"]]
+ 004c1d18 ["CALL", null, ["callee:00c57b10:8"]]
- 0049ee80 bytes 90f01c94
+ 004c1d18 bytes 7e571e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba346490747306afde25ffe7c97bbb0a"></a>

### [`0049ef6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049ef6c.md) → [`004c1e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1e04.md) FUN_004c1e04

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0049ef64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049ef64.md) [`004a00c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a00c0.md) · 呼出先 10件 [`0048e51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e51c.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0049cdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cdcc.md) [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00520980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520980.md)
- 新版 呼出元 2件 [`004c1dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1dfc.md) [`004c2f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2f58.md) · 呼出先 10件 [`004b13b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b13b4.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`004bfc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfc64.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00543818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543818.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c21f0",
      "incomplete_value": true,
      "site": "004c21f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049f358",
      "incomplete_value": true,
      "site": "0049f358",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c21e0",
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
      "004c21e0",
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

- 旧版 [`0049f358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049ef6c.md#insn-0049f358) · [`0049efac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049ef6c.md#insn-0049efac) · [`0049f014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049ef6c.md#insn-0049f014)
- 新版 `004c21f0`（命令位置の公開資料なし） · `004c1e44`（命令位置の公開資料なし） · `004c1eac`（命令位置の公開資料なし）

~~~diff
- 0049f358 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049f358 ["INT_ADD", "register:40f0:8", ["const:49f358:8", "const:4:8"]]
- 0049f358 ["CALLIND", null, ["register:0:8"]]
+ 004c21f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c21f0 ["INT_ADD", "register:40f0:8", ["const:4c21f0:8", "const:4:8"]]
+ 004c21f0 ["CALLIND", null, ["register:0:8"]]
- 0049f358 bytes 20013fd6
+ 004c21f0 bytes 20013fd6
- 0049efac ["COPY", "register:0:8", ["register:4040:8"]]
- 0049efac ["INT_ADD", "register:40f0:8", ["const:49efac:8", "const:4:8"]]
- 0049efac ["CALLIND", null, ["register:0:8"]]
+ 004c1e44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c1e44 ["INT_ADD", "register:40f0:8", ["const:4c1e44:8", "const:4:8"]]
+ 004c1e44 ["CALLIND", null, ["register:0:8"]]
- 0049efac bytes 00013fd6
+ 004c1e44 bytes 00013fd6
- 0049f014 ["INT_ADD", "register:40f0:8", ["const:49f014:8", "const:4:8"]]
- 0049f014 ["CALL", null, ["callee:00540264:8"]]
+ 004c1eac ["INT_ADD", "register:40f0:8", ["const:4c1eac:8", "const:4:8"]]
+ 004c1eac ["CALL", null, ["callee:00540264:8"]]
- 0049f014 bytes eef80194
+ 004c1eac bytes eef80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c1f3569e4825c5b459944f402c7d526"></a>

### [`0049f3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f3b8.md) → [`004c2250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2250.md) _ZNK5Botan4PSSR4nameEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c2290",
      "incomplete_value": false,
      "site": "004c229c",
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
            "const:f21:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049f3f8",
      "incomplete_value": false,
      "site": "0049f404",
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
            "const:27f:8"
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
      "definition_site": "004c22bc",
      "incomplete_value": false,
      "site": "004c22c4",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049f424",
      "incomplete_value": false,
      "site": "0049f42c",
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
            "const:4d4:8"
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
      "definition_site": "004c232c",
      "incomplete_value": false,
      "site": "004c2334",
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
      "definition_site": "0049f494",
      "incomplete_value": false,
      "site": "0049f49c",
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
      "004c2290",
      "PARAM",
      [
        "storage",
        "002a827f",
        null,
        "string"
      ]
    ],
    [
      "004c22bc",
      "PARAM",
      [
        "storage",
        "0029d4d4",
        null,
        "string"
      ]
    ],
    [
      "004c232c",
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
      "004c2290",
      "PARAM",
      [
        "storage",
        "002b8f21",
        null,
        "string"
      ]
    ],
    [
      "004c22bc",
      "PARAM",
      [
        "storage",
        "002ad75e",
        null,
        "string"
      ]
    ],
    [
      "004c232c",
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

- 旧版 [`0049f404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f3b8.md#insn-0049f404) · [`0049f42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f3b8.md#insn-0049f42c) · [`0049f49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f3b8.md#insn-0049f49c)
- 新版 `004c229c`（命令位置の公開資料なし） · `004c22c4`（命令位置の公開資料なし） · `004c2334`（命令位置の公開資料なし）

~~~diff
- 0049f404 ["INT_ADD", "register:40f0:8", ["const:49f404:8", "const:4:8"]]
- 0049f404 ["CALL", null, ["callee:00c57b60:8"]]
+ 004c229c ["INT_ADD", "register:40f0:8", ["const:4c229c:8", "const:4:8"]]
+ 004c229c ["CALL", null, ["callee:00c57b60:8"]]
- 0049f404 bytes 43ef1c94
+ 004c229c bytes 31561e94
- 0049f42c ["INT_ADD", "register:40f0:8", ["const:49f42c:8", "const:4:8"]]
- 0049f42c ["CALL", null, ["callee:00c57b70:8"]]
+ 004c22c4 ["INT_ADD", "register:40f0:8", ["const:4c22c4:8", "const:4:8"]]
+ 004c22c4 ["CALL", null, ["callee:00c57b70:8"]]
- 0049f42c bytes 3def1c94
+ 004c22c4 bytes 2b561e94
- 0049f49c ["INT_ADD", "register:40f0:8", ["const:49f49c:8", "const:4:8"]]
- 0049f49c ["CALL", null, ["callee:00c57b70:8"]]
+ 004c2334 ["INT_ADD", "register:40f0:8", ["const:4c2334:8", "const:4:8"]]
+ 004c2334 ["CALL", null, ["callee:00c57b70:8"]]
- 0049f49c bytes 21ef1c94
+ 004c2334 bytes 0f561e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9c6e8772d3c847dcc5981c8687f0e9a"></a>

### [`0049f624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f624.md) → [`004c24bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c24bc.md) _ZNK5Botan4PSSR15config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 22件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`0049d8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d8dc.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004c0774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0774.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.49% / 新版 94.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 6件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c25f8",
      "incomplete_value": true,
      "site": "004c25f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049f760",
      "incomplete_value": true,
      "site": "0049f760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c2638",
      "incomplete_value": true,
      "site": "004c2638",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049f7a0",
      "incomplete_value": true,
      "site": "0049f7a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b2:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c26b8",
      "value": [
        "leaf",
        "ram:c58a10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0049f820",
      "value": [
        "leaf",
        "ram:bdbfc0:8"
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
      "004c25ec",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "004c25f8",
      "DATA",
      [
        "storage",
        "00be91e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c2620",
      "READ",
      [
        "storage",
        "002a13b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c25ec",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004c25f8",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c2620",
      "READ",
      [
        "storage",
        "002b19fe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049f820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f624.md#insn-0049f820) · [`0049f87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f624.md#insn-0049f87c) · [`0049f91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f624.md#insn-0049f91c)
- 新版 `004c26b8`（命令位置の公開資料なし） · `004c2714`（命令位置の公開資料なし） · `004c27b4`（命令位置の公開資料なし）

~~~diff
- 0049f820 ["INT_ADD", "register:40f0:8", ["const:49f820:8", "const:4:8"]]
- 0049f820 ["CALL", null, ["ram:bdbfc0:8"]]
+ 004c26b8 ["INT_ADD", "register:40f0:8", ["const:4c26b8:8", "const:4:8"]]
+ 004c26b8 ["CALL", null, ["ram:c58a10:8"]]
- 0049f820 bytes e8f11c94
+ 004c26b8 bytes d6581e94
- 0049f87c ["INT_ADD", "register:40f0:8", ["const:49f87c:8", "const:4:8"]]
- 0049f87c ["CALL", null, ["ram:bdbfc0:8"]]
+ 004c2714 ["INT_ADD", "register:40f0:8", ["const:4c2714:8", "const:4:8"]]
+ 004c2714 ["CALL", null, ["ram:c58a10:8"]]
- 0049f87c bytes d1f11c94
+ 004c2714 bytes bf581e94
- 0049f91c ["COPY", "register:0:8", ["register:4048:8"]]
- 0049f91c ["INT_ADD", "register:40f0:8", ["const:49f91c:8", "const:4:8"]]
- 0049f91c ["CALLIND", null, ["register:0:8"]]
+ 004c27b4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c27b4 ["INT_ADD", "register:40f0:8", ["const:4c27b4:8", "const:4:8"]]
+ 004c27b4 ["CALLIND", null, ["register:0:8"]]
- 0049f91c bytes 20013fd6
+ 004c27b4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41a52b9b4b729ab951135df714d793d5"></a>

### [`0049fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049fddc.md) → [`004c2c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2c74.md) _ZN5Botan8PSSR_RawC1EPNS_12HashFunctionE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c2c94",
      "incomplete_value": true,
      "site": "004c2c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0049fdfc",
      "incomplete_value": true,
      "site": "0049fe00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c2c8c",
      "READ",
      [
        "storage",
        "00c1b078",
        null,
        "pointer"
      ]
    ],
    [
      "004c2c98",
      "DATA",
      [
        "storage",
        "00be96c0",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c2c8c",
      "READ",
      [
        "storage",
        "00c9aa68",
        null,
        "pointer"
      ]
    ],
    [
      "004c2c98",
      "DATA",
      [
        "storage",
        "00c66280",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049fde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049fddc.md#insn-0049fde8) · [`0049fdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049fddc.md#insn-0049fdf4) · [`0049fe0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049fddc.md#insn-0049fe0c)
- 新版 `004c2c80`（命令位置の公開資料なし） · `004c2c8c`（命令位置の公開資料なし） · `004c2ca4`（命令位置の公開資料なし）

~~~diff
- 0049fde8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c2c80 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0049fde8 bytes e83b0090
+ 004c2c80 bytes c83e0090
- 0049fdf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:78:8"]]
- 0049fdf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c2c8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 004c2c8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0049fdf4 bytes 083d40f9
+ 004c2c8c bytes 083545f9
- 0049fe0c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049fe0c ["INT_ADD", "register:40f0:8", ["const:49fe0c:8", "const:4:8"]]
- 0049fe0c ["CALLIND", null, ["register:0:8"]]
+ 004c2ca4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c2ca4 ["INT_ADD", "register:40f0:8", ["const:4c2ca4:8", "const:4:8"]]
+ 004c2ca4 ["CALLIND", null, ["register:0:8"]]
- 0049fe0c bytes 00013fd6
+ 004c2ca4 bytes 00013fd6
~~~


<a id="compare-7b9c124f2c767e4862ca214d83785532"></a>

### [`0049fe7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049fe7c.md) → [`004c2d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2d14.md) _ZN5Botan8PSSR_Raw8raw_dataEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

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
      "definition_site": "004c2db8",
      "incomplete_value": false,
      "site": "004c2dc0",
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
            "const:41:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ff20",
      "incomplete_value": false,
      "site": "0049ff28",
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
            "const:848:8"
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
      "definition_site": "004c2df0",
      "incomplete_value": true,
      "site": "004c2dfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049ff58",
      "incomplete_value": true,
      "site": "0049ff64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c2dec",
      "incomplete_value": false,
      "site": "004c2dfc",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "0049ff54",
      "incomplete_value": false,
      "site": "0049ff64",
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
      "004c2db8",
      "PARAM",
      [
        "storage",
        "00293848",
        null,
        "string"
      ]
    ],
    [
      "004c2dec",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c2df0",
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
      "004c2db8",
      "PARAM",
      [
        "storage",
        "002a3041",
        null,
        "string"
      ]
    ],
    [
      "004c2dec",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c2df0",
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

- 旧版 [`0049ff28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049fe7c.md#insn-0049ff28) · [`0049ff64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049fe7c.md#insn-0049ff64) · [`0049fed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049fe7c.md#insn-0049fed0)
- 新版 `004c2dc0`（命令位置の公開資料なし） · `004c2dfc`（命令位置の公開資料なし） · `004c2d68`（命令位置の公開資料なし）

~~~diff
- 0049ff28 ["INT_ADD", "register:40f0:8", ["const:49ff28:8", "const:4:8"]]
- 0049ff28 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c2dc0 ["INT_ADD", "register:40f0:8", ["const:4c2dc0:8", "const:4:8"]]
+ 004c2dc0 ["CALL", null, ["callee:0043dd98:8"]]
- 0049ff28 bytes dcecfd97
+ 004c2dc0 bytes f6ebfd97
- 0049ff64 ["INT_ADD", "register:40f0:8", ["const:49ff64:8", "const:4:8"]]
- 0049ff64 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c2dfc ["INT_ADD", "register:40f0:8", ["const:4c2dfc:8", "const:4:8"]]
+ 004c2dfc ["CALL", null, ["callee:00c57b10:8"]]
- 0049ff64 bytes 57ec1c94
+ 004c2dfc bytes 45531e94
- 0049fed0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049fed0 ["INT_ADD", "register:40f0:8", ["const:49fed0:8", "const:4:8"]]
- 0049fed0 ["CALLIND", null, ["register:0:8"]]
+ 004c2d68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2d68 ["INT_ADD", "register:40f0:8", ["const:4c2d68:8", "const:4:8"]]
+ 004c2d68 ["CALLIND", null, ["register:0:8"]]
- 0049fed0 bytes 20013fd6
+ 004c2d68 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-646002f2bfdd406afd565eead1448114"></a>

### [`004a00c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a00c8.md) → [`004c2f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2f60.md) _ZNK5Botan8PSSR_Raw4nameEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c2fa0",
      "incomplete_value": false,
      "site": "004c2fac",
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
            "const:fa1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0108",
      "incomplete_value": false,
      "site": "004a0114",
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
            "const:988:8"
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
      "definition_site": "004c2fcc",
      "incomplete_value": false,
      "site": "004c2fd4",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0134",
      "incomplete_value": false,
      "site": "004a013c",
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
            "const:4d4:8"
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
      "definition_site": "004c303c",
      "incomplete_value": false,
      "site": "004c3044",
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
      "definition_site": "004a01a4",
      "incomplete_value": false,
      "site": "004a01ac",
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
      "004c2fa0",
      "PARAM",
      [
        "storage",
        "00291988",
        null,
        "string"
      ]
    ],
    [
      "004c2fcc",
      "PARAM",
      [
        "storage",
        "0029d4d4",
        null,
        "string"
      ]
    ],
    [
      "004c303c",
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
      "004c2fa0",
      "PARAM",
      [
        "storage",
        "002a0fa1",
        null,
        "string"
      ]
    ],
    [
      "004c2fcc",
      "PARAM",
      [
        "storage",
        "002ad75e",
        null,
        "string"
      ]
    ],
    [
      "004c303c",
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

- 旧版 [`004a0114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a00c8.md#insn-004a0114) · [`004a013c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a00c8.md#insn-004a013c) · [`004a01ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a00c8.md#insn-004a01ac)
- 新版 `004c2fac`（命令位置の公開資料なし） · `004c2fd4`（命令位置の公開資料なし） · `004c3044`（命令位置の公開資料なし）

~~~diff
- 004a0114 ["INT_ADD", "register:40f0:8", ["const:4a0114:8", "const:4:8"]]
- 004a0114 ["CALL", null, ["callee:00c57b60:8"]]
+ 004c2fac ["INT_ADD", "register:40f0:8", ["const:4c2fac:8", "const:4:8"]]
+ 004c2fac ["CALL", null, ["callee:00c57b60:8"]]
- 004a0114 bytes ffeb1c94
+ 004c2fac bytes ed521e94
- 004a013c ["INT_ADD", "register:40f0:8", ["const:4a013c:8", "const:4:8"]]
- 004a013c ["CALL", null, ["callee:00c57b70:8"]]
+ 004c2fd4 ["INT_ADD", "register:40f0:8", ["const:4c2fd4:8", "const:4:8"]]
+ 004c2fd4 ["CALL", null, ["callee:00c57b70:8"]]
- 004a013c bytes f9eb1c94
+ 004c2fd4 bytes e7521e94
- 004a01ac ["INT_ADD", "register:40f0:8", ["const:4a01ac:8", "const:4:8"]]
- 004a01ac ["CALL", null, ["callee:00c57b70:8"]]
+ 004c3044 ["INT_ADD", "register:40f0:8", ["const:4c3044:8", "const:4:8"]]
+ 004c3044 ["CALL", null, ["callee:00c57b70:8"]]
- 004a01ac bytes ddeb1c94
+ 004c3044 bytes cb521e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10eb0e841ba5068f16aa3f0dedf2995a"></a>

### [`004a0334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0334.md) → [`004c31cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c31cc.md) _ZN5Botan14Entropy_Source6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004c3290",
      "incomplete_value": false,
      "site": "004c3298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a03f8",
      "incomplete_value": false,
      "site": "004a0400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bec000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "004c3298",
      "DATA",
      [
        "storage",
        "00beccc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004c3298",
      "DATA",
      [
        "storage",
        "00c69888",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a03f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0334.md#insn-004a03f0) · [`004a03f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0334.md#insn-004a03f4) · [`004a03f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0334.md#insn-004a03f8)
- 新版 `004c3288`（命令位置の公開資料なし） · `004c328c`（命令位置の公開資料なし） · `004c3290`（命令位置の公開資料なし）

~~~diff
- 004a03f0 ["INT_ADD", "register:40f0:8", ["const:4a03f0:8", "const:4:8"]]
- 004a03f0 ["CALL", null, ["callee:00c57a90:8"]]
+ 004c3288 ["INT_ADD", "register:40f0:8", ["const:4c3288:8", "const:4:8"]]
+ 004c3288 ["CALL", null, ["callee:00c57a90:8"]]
- 004a03f0 bytes 14eb1c94
+ 004c3288 bytes 02521e94
- 004a03f4 ["COPY", "register:4048:8", ["const:bec000:8"]]
+ 004c328c ["COPY", "register:4048:8", ["const:c69000:8"]]
- 004a03f4 bytes 693a0090
+ 004c328c bytes 293d00d0
- 004a03f8 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 004a03f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004a03f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004a03f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004c3290 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 004c3290 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004c3290 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004c3290 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004a03f8 bytes 29213391
+ 004c3290 bytes 29212291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2636f199a9927d193499ef9096eb85ee"></a>

### [`004a0c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0c64.md) → [`004c3afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3afc.md) _ZN5Botan15Entropy_Sources14global_sourcesEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004a0fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0fc4.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004c3e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3e5c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 87.23% / 新版 87.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 1件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c3b64",
      "incomplete_value": false,
      "site": "004c3b68",
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
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0ccc",
      "incomplete_value": false,
      "site": "004a0cd0",
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
            "const:3a0:8"
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
      "definition_site": "004c3b74",
      "incomplete_value": false,
      "site": "004c3b80",
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
            "const:d19:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0cdc",
      "incomplete_value": false,
      "site": "004a0ce8",
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
            "const:4ac:8"
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
      "definition_site": "004c3b8c",
      "incomplete_value": false,
      "site": "004c3b94",
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
            "const:ad4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0cf4",
      "incomplete_value": false,
      "site": "004a0cfc",
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
            "const:bfb:8"
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
      "004c3b28",
      "READ",
      [
        "storage",
        "00c253a0",
        null,
        "undefined1"
      ]
    ],
    [
      "004c3b44",
      "DATA",
      [
        "storage",
        "00c25388",
        null,
        null
      ]
    ],
    [
      "004c3b64",
      "PARAM",
      [
        "storage",
        "00c253a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004c3b28",
      "READ",
      [
        "storage",
        "00ca4e60",
        null,
        "undefined1"
      ]
    ],
    [
      "004c3b44",
      "DATA",
      [
        "storage",
        "00ca4e48",
        null,
        null
      ]
    ],
    [
      "004c3b64",
      "PARAM",
      [
        "storage",
        "00ca4e60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a0cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0c64.md#insn-004a0cd0) · [`004a0ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0c64.md#insn-004a0ce8) · [`004a0cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0c64.md#insn-004a0cfc)
- 新版 `004c3b68`（命令位置の公開資料なし） · `004c3b80`（命令位置の公開資料なし） · `004c3b94`（命令位置の公開資料なし）

~~~diff
- 004a0cd0 ["INT_ADD", "register:40f0:8", ["const:4a0cd0:8", "const:4:8"]]
- 004a0cd0 ["CALL", null, ["callee:00c57a50:8"]]
+ 004c3b68 ["INT_ADD", "register:40f0:8", ["const:4c3b68:8", "const:4:8"]]
+ 004c3b68 ["CALL", null, ["callee:00c57a50:8"]]
- 004a0cd0 bytes cce81c94
+ 004c3b68 bytes ba4f1e94
- 004a0ce8 ["INT_ADD", "register:40f0:8", ["const:4a0ce8:8", "const:4:8"]]
- 004a0ce8 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c3b80 ["INT_ADD", "register:40f0:8", ["const:4c3b80:8", "const:4:8"]]
+ 004c3b80 ["CALL", null, ["callee:0043dd98:8"]]
- 004a0ce8 bytes 6ce9fd97
+ 004c3b80 bytes 86e8fd97
- 004a0cfc ["INT_ADD", "register:40f0:8", ["const:4a0cfc:8", "const:4:8"]]
- 004a0cfc ["CALL", null, ["callee:0043dd98:8"]]
+ 004c3b94 ["INT_ADD", "register:40f0:8", ["const:4c3b94:8", "const:4:8"]]
+ 004c3b94 ["CALL", null, ["callee:0043dd98:8"]]
- 004a0cfc bytes 67e9fd97
+ 004c3b94 bytes 81e8fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91a387ac8bc1b604969a6cd8d5c7d4ae"></a>

### [`004a1040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1040.md) → [`004c3ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3ed8.md) _ZN5Botan19StreamCipher_FilterC1EPNS_12StreamCipherE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.94% / 新版 85.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c3f0c",
      "incomplete_value": true,
      "site": "004c3f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1074",
      "incomplete_value": true,
      "site": "004a107c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c3f48",
      "incomplete_value": true,
      "site": "004c3f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a10b0",
      "incomplete_value": true,
      "site": "004a10b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c3fb8",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a1120",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
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
      "004c3ef8",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c3f14",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c3f3c",
      "READ",
      [
        "storage",
        "00c1b088",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c3ef8",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c3f14",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c3f3c",
      "READ",
      [
        "storage",
        "00c9aa78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1040.md#insn-004a1120) · [`004a1138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1040.md#insn-004a1138) · [`004a1054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1040.md#insn-004a1054)
- 新版 `004c3fb8`（命令位置の公開資料なし） · `004c3fd0`（命令位置の公開資料なし） · `004c3eec`（命令位置の公開資料なし）

~~~diff
- 004a1120 ["INT_ADD", "register:40f0:8", ["const:4a1120:8", "const:4:8"]]
- 004a1120 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004c3fb8 ["INT_ADD", "register:40f0:8", ["const:4c3fb8:8", "const:4:8"]]
+ 004c3fb8 ["CALL", null, ["ram:c58640:8"]]
- 004a1120 bytes b4ea1c94
+ 004c3fb8 bytes a2511e94
- 004a1138 ["INT_ADD", "register:40f0:8", ["const:4a1138:8", "const:4:8"]]
- 004a1138 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c3fd0 ["INT_ADD", "register:40f0:8", ["const:4c3fd0:8", "const:4:8"]]
+ 004c3fd0 ["CALL", null, ["callee:00c57b10:8"]]
- 004a1138 bytes e2e71c94
+ 004c3fd0 bytes d04e1e94
- 004a1054 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c3eec ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a1054 bytes c83b00d0
+ 004c3eec bytes a83e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83811e650afee2c0f9ebf462e4c4a306"></a>

### [`004a1190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1190.md) → [`004c4028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4028.md) _ZN5Botan19StreamCipher_FilterC1EPNS_12StreamCipherERKNS_11OctetStringE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c4064",
      "incomplete_value": true,
      "site": "004c406c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a11cc",
      "incomplete_value": true,
      "site": "004a11d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c40a4",
      "incomplete_value": true,
      "site": "004c40ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a120c",
      "incomplete_value": true,
      "site": "004a1214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c4128",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a1290",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
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
      "004c4050",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c406c",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4094",
      "READ",
      [
        "storage",
        "00c1b088",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4050",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c406c",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4094",
      "READ",
      [
        "storage",
        "00c9aa78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1190.md#insn-004a1290) · [`004a12a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1190.md#insn-004a12a8) · [`004a11ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1190.md#insn-004a11ac)
- 新版 `004c4128`（命令位置の公開資料なし） · `004c4140`（命令位置の公開資料なし） · `004c4044`（命令位置の公開資料なし）

~~~diff
- 004a1290 ["INT_ADD", "register:40f0:8", ["const:4a1290:8", "const:4:8"]]
- 004a1290 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004c4128 ["INT_ADD", "register:40f0:8", ["const:4c4128:8", "const:4:8"]]
+ 004c4128 ["CALL", null, ["ram:c58640:8"]]
- 004a1290 bytes 58ea1c94
+ 004c4128 bytes 46511e94
- 004a12a8 ["INT_ADD", "register:40f0:8", ["const:4a12a8:8", "const:4:8"]]
- 004a12a8 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c4140 ["INT_ADD", "register:40f0:8", ["const:4c4140:8", "const:4:8"]]
+ 004c4140 ["CALL", null, ["callee:00c57b10:8"]]
- 004a12a8 bytes 86e71c94
+ 004c4140 bytes 744e1e94
- 004a11ac ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004c4044 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004a11ac bytes c93b00d0
+ 004c4044 bytes a93e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f66853f8f22de2c9f014ad7717be189d"></a>

### [`004a1328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1328.md) → [`004c41c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c41c0.md) _ZN5Botan19StreamCipher_FilterC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.67% / 新版 87.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c41f4",
      "incomplete_value": true,
      "site": "004c41fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a135c",
      "incomplete_value": true,
      "site": "004a1364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c4234",
      "incomplete_value": true,
      "site": "004c423c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a139c",
      "incomplete_value": true,
      "site": "004a13a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "site": "004c42c4",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a142c",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
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
      "004c41e0",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c41fc",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4224",
      "READ",
      [
        "storage",
        "00c1b088",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c41e0",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c41fc",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4224",
      "READ",
      [
        "storage",
        "00c9aa78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a142c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1328.md#insn-004a142c) · [`004a1444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1328.md#insn-004a1444) · [`004a133c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1328.md#insn-004a133c)
- 新版 `004c42c4`（命令位置の公開資料なし） · `004c42dc`（命令位置の公開資料なし） · `004c41d4`（命令位置の公開資料なし）

~~~diff
- 004a142c ["INT_ADD", "register:40f0:8", ["const:4a142c:8", "const:4:8"]]
- 004a142c ["CALL", null, ["ram:bdbbf0:8"]]
+ 004c42c4 ["INT_ADD", "register:40f0:8", ["const:4c42c4:8", "const:4:8"]]
+ 004c42c4 ["CALL", null, ["ram:c58640:8"]]
- 004a142c bytes f1e91c94
+ 004c42c4 bytes df501e94
- 004a1444 ["INT_ADD", "register:40f0:8", ["const:4a1444:8", "const:4:8"]]
- 004a1444 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c42dc ["INT_ADD", "register:40f0:8", ["const:4c42dc:8", "const:4:8"]]
+ 004c42dc ["CALL", null, ["callee:00c57b10:8"]]
- 004a1444 bytes 1fe71c94
+ 004c42dc bytes 0d4e1e94
- 004a133c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c41d4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a133c bytes c83b00d0
+ 004c41d4 bytes a83e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b989b162c0ae52eaedabe0480f37fd81"></a>

### [`004a14bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a14bc.md) → [`004c4354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4354.md) _ZN5Botan12StreamCipher15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc000.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a50.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
      "definition_site": "004c43cc",
      "incomplete_value": false,
      "site": "004c43d4",
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
            "const:274:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1534",
      "incomplete_value": false,
      "site": "004a153c",
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
            "const:5d1:8"
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
      "definition_site": "004c440c",
      "incomplete_value": true,
      "site": "004c4418",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a1574",
      "incomplete_value": true,
      "site": "004a1580",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c4408",
      "incomplete_value": false,
      "site": "004c4418",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a1570",
      "incomplete_value": false,
      "site": "004a1580",
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
      "004c43cc",
      "PARAM",
      [
        "storage",
        "002a95d1",
        null,
        "string"
      ]
    ],
    [
      "004c4408",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c440c",
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
      "004c43cc",
      "PARAM",
      [
        "storage",
        "002ba274",
        null,
        "string"
      ]
    ],
    [
      "004c4408",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c440c",
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

- 旧版 [`004a153c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a14bc.md#insn-004a153c) · [`004a1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a14bc.md#insn-004a1580) · [`004a14f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a14bc.md#insn-004a14f0)
- 新版 `004c43d4`（命令位置の公開資料なし） · `004c4418`（命令位置の公開資料なし） · `004c4388`（命令位置の公開資料なし）

~~~diff
- 004a153c ["INT_ADD", "register:40f0:8", ["const:4a153c:8", "const:4:8"]]
- 004a153c ["CALL", null, ["callee:0043dd98:8"]]
+ 004c43d4 ["INT_ADD", "register:40f0:8", ["const:4c43d4:8", "const:4:8"]]
+ 004c43d4 ["CALL", null, ["callee:0043dd98:8"]]
- 004a153c bytes 57e7fd97
+ 004c43d4 bytes 71e6fd97
- 004a1580 ["INT_ADD", "register:40f0:8", ["const:4a1580:8", "const:4:8"]]
- 004a1580 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c4418 ["INT_ADD", "register:40f0:8", ["const:4c4418:8", "const:4:8"]]
+ 004c4418 ["CALL", null, ["callee:00c57b10:8"]]
- 004a1580 bytes d0e61c94
+ 004c4418 bytes be4d1e94
- 004a14f0 ["INT_ADD", "register:40f0:8", ["const:4a14f0:8", "const:4:8"]]
- 004a14f0 ["CALL", null, ["callee:00c58a60:8"]]
+ 004c4388 ["INT_ADD", "register:40f0:8", ["const:4c4388:8", "const:4:8"]]
+ 004c4388 ["CALL", null, ["callee:00c58a60:8"]]
- 004a14f0 bytes c8ea1c94
+ 004c4388 bytes b6511e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff1232a2f280aa9ad43149b30b75ba9c"></a>

### [`004a15d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a15d0.md) → [`004c4468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4468.md) _ZN5Botan19StreamCipher_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_11OctetStringE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 10件 [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.75% / 新版 88.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c44a4",
      "incomplete_value": true,
      "site": "004c44ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a160c",
      "incomplete_value": true,
      "site": "004a1614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c44e4",
      "incomplete_value": true,
      "site": "004c44ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a164c",
      "incomplete_value": true,
      "site": "004a1654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c4588",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a16f0",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
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
      "004c4490",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c44ac",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c44d4",
      "READ",
      [
        "storage",
        "00c1b088",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4490",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c44ac",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c44d4",
      "READ",
      [
        "storage",
        "00c9aa78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a16f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a15d0.md#insn-004a16f0) · [`004a1708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a15d0.md#insn-004a1708) · [`004a15ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a15d0.md#insn-004a15ec)
- 新版 `004c4588`（命令位置の公開資料なし） · `004c45a0`（命令位置の公開資料なし） · `004c4484`（命令位置の公開資料なし）

~~~diff
- 004a16f0 ["INT_ADD", "register:40f0:8", ["const:4a16f0:8", "const:4:8"]]
- 004a16f0 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004c4588 ["INT_ADD", "register:40f0:8", ["const:4c4588:8", "const:4:8"]]
+ 004c4588 ["CALL", null, ["ram:c58640:8"]]
- 004a16f0 bytes 40e91c94
+ 004c4588 bytes 2e501e94
- 004a1708 ["INT_ADD", "register:40f0:8", ["const:4a1708:8", "const:4:8"]]
- 004a1708 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c45a0 ["INT_ADD", "register:40f0:8", ["const:4c45a0:8", "const:4:8"]]
+ 004c45a0 ["CALL", null, ["callee:00c57b10:8"]]
- 004a1708 bytes 6ee61c94
+ 004c45a0 bytes 5c4d1e94
- 004a15ec ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004c4484 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004a15ec bytes c93b00d0
+ 004c4484 bytes a93e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-514731e756045d7c50afe2471fca86a0"></a>

### [`004a181c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a181c.md) → [`004c46b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c46b4.md) _ZN5Botan11Hash_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc020.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

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
      "definition_site": "004c46f0",
      "incomplete_value": true,
      "site": "004c46f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1858",
      "incomplete_value": true,
      "site": "004a1860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c4724",
      "incomplete_value": true,
      "site": "004c472c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a188c",
      "incomplete_value": true,
      "site": "004a1894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c46dc",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c46f8",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4718",
      "READ",
      [
        "storage",
        "00c1b090",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c46dc",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c46f8",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4718",
      "READ",
      [
        "storage",
        "00c9aa80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a181c.md#insn-004a1838) · [`004a1844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a181c.md#insn-004a1844) · [`004a1878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a181c.md#insn-004a1878)
- 新版 `004c46d0`（命令位置の公開資料なし） · `004c46dc`（命令位置の公開資料なし） · `004c4710`（命令位置の公開資料なし）

~~~diff
- 004a1838 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004c46d0 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004a1838 bytes c93b00d0
+ 004c46d0 bytes a93e00d0
- 004a1844 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
- 004a1844 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c46dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
+ 004c46dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1844 bytes 294140f9
+ 004c46dc bytes 293945f9
- 004a1878 ["INT_ADD", "register:40f0:8", ["const:4a1878:8", "const:4:8"]]
- 004a1878 ["CALL", null, ["callee:00543c1c:8"]]
+ 004c4710 ["INT_ADD", "register:40f0:8", ["const:4c4710:8", "const:4:8"]]
+ 004c4710 ["CALL", null, ["callee:00543c1c:8"]]
- 004a1878 bytes 43fd0194
+ 004c4710 bytes 43fd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3d0314eb74a83f5fa1fbe5db0211421"></a>

### [`004a1940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1940.md) → [`004c47d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c47d8.md) _ZN5Botan6FilterC2Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c47fc",
      "incomplete_value": true,
      "site": "004c4800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1964",
      "incomplete_value": true,
      "site": "004a1968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c47f4",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c4800",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c47f4",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4800",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1940.md#insn-004a1950) · [`004a195c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1940.md#insn-004a195c) · [`004a1960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1940.md#insn-004a1960)
- 新版 `004c47e8`（命令位置の公開資料なし） · `004c47f4`（命令位置の公開資料なし）

~~~diff
- 004a1950 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c47e8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a1950 bytes c83b00d0
+ 004c47e8 bytes a83e00d0
- 004a195c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 004a195c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c47f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 004c47f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a195c bytes 084140f9
+ 004c47f4 bytes 083945f9
- 004a1960 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 004a1960 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236379194b36e93afb7cf25f28ea1f31"></a>

### [`004a19c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a19c4.md) → [`004c485c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c485c.md) _ZN5Botan12HashFunction15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc020.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a70.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
      "definition_site": "004c48d4",
      "incomplete_value": false,
      "site": "004c48dc",
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
            "const:ecf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1a3c",
      "incomplete_value": false,
      "site": "004a1a44",
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
            "const:7bf:8"
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
      "definition_site": "004c4914",
      "incomplete_value": true,
      "site": "004c4920",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a1a7c",
      "incomplete_value": true,
      "site": "004a1a88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c4910",
      "incomplete_value": false,
      "site": "004c4920",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a1a78",
      "incomplete_value": false,
      "site": "004a1a88",
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
      "004c48d4",
      "PARAM",
      [
        "storage",
        "002927bf",
        null,
        null
      ]
    ],
    [
      "004c4910",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c4914",
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
      "004c48d4",
      "PARAM",
      [
        "storage",
        "002a1ecf",
        null,
        null
      ]
    ],
    [
      "004c4910",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c4914",
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

- 旧版 [`004a1a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a19c4.md#insn-004a1a44) · [`004a1a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a19c4.md#insn-004a1a88) · [`004a19f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a19c4.md#insn-004a19f8)
- 新版 `004c48dc`（命令位置の公開資料なし） · `004c4920`（命令位置の公開資料なし） · `004c4890`（命令位置の公開資料なし）

~~~diff
- 004a1a44 ["INT_ADD", "register:40f0:8", ["const:4a1a44:8", "const:4:8"]]
- 004a1a44 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c48dc ["INT_ADD", "register:40f0:8", ["const:4c48dc:8", "const:4:8"]]
+ 004c48dc ["CALL", null, ["callee:0043dd98:8"]]
- 004a1a44 bytes 15e6fd97
+ 004c48dc bytes 2fe5fd97
- 004a1a88 ["INT_ADD", "register:40f0:8", ["const:4a1a88:8", "const:4:8"]]
- 004a1a88 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c4920 ["INT_ADD", "register:40f0:8", ["const:4c4920:8", "const:4:8"]]
+ 004c4920 ["CALL", null, ["callee:00c57b10:8"]]
- 004a1a88 bytes 8ee51c94
+ 004c4920 bytes 7c4c1e94
- 004a19f8 ["INT_ADD", "register:40f0:8", ["const:4a19f8:8", "const:4:8"]]
- 004a19f8 ["CALL", null, ["callee:00c589f0:8"]]
+ 004c4890 ["INT_ADD", "register:40f0:8", ["const:4c4890:8", "const:4:8"]]
+ 004c4890 ["CALL", null, ["callee:00c589f0:8"]]
- 004a19f8 bytes 6ae91c94
+ 004c4890 bytes 58501e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19355011e0852af65079b4069615842a"></a>

### [`004a1bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1bfc.md) → [`004c4a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4a94.md) _ZN5Botan10MAC_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc030.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

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
      "definition_site": "004c4ad0",
      "incomplete_value": true,
      "site": "004c4ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1c38",
      "incomplete_value": true,
      "site": "004a1c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c4b04",
      "incomplete_value": true,
      "site": "004c4b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1c6c",
      "incomplete_value": true,
      "site": "004a1c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c4abc",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c4ad8",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4af8",
      "READ",
      [
        "storage",
        "00c1b098",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4abc",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4ad8",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4af8",
      "READ",
      [
        "storage",
        "00c9aa88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1bfc.md#insn-004a1c18) · [`004a1c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1bfc.md#insn-004a1c24) · [`004a1c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1bfc.md#insn-004a1c58)
- 新版 `004c4ab0`（命令位置の公開資料なし） · `004c4abc`（命令位置の公開資料なし） · `004c4af0`（命令位置の公開資料なし）

~~~diff
- 004a1c18 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004c4ab0 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004a1c18 bytes c93b00d0
+ 004c4ab0 bytes a93e00d0
- 004a1c24 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
- 004a1c24 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4abc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
+ 004c4abc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1c24 bytes 294140f9
+ 004c4abc bytes 293945f9
- 004a1c58 ["INT_ADD", "register:40f0:8", ["const:4a1c58:8", "const:4:8"]]
- 004a1c58 ["CALL", null, ["callee:00543c1c:8"]]
+ 004c4af0 ["INT_ADD", "register:40f0:8", ["const:4c4af0:8", "const:4:8"]]
+ 004c4af0 ["CALL", null, ["callee:00543c1c:8"]]
- 004a1c58 bytes 4bfc0194
+ 004c4af0 bytes 4bfc0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-730790b0e51d12c7b9da2c982deb50ba"></a>

### [`004a1d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1d20.md) → [`004c4bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4bb8.md) _ZN5Botan25MessageAuthenticationCode15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc030.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a80.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
      "definition_site": "004c4c30",
      "incomplete_value": false,
      "site": "004c4c38",
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
            "const:723:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1d98",
      "incomplete_value": false,
      "site": "004a1da0",
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
            "const:58a:8"
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
      "definition_site": "004c4c70",
      "incomplete_value": true,
      "site": "004c4c7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a1dd8",
      "incomplete_value": true,
      "site": "004a1de4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c4c6c",
      "incomplete_value": false,
      "site": "004c4c7c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a1dd4",
      "incomplete_value": false,
      "site": "004a1de4",
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
      "004c4c30",
      "PARAM",
      [
        "storage",
        "0029c58a",
        null,
        null
      ]
    ],
    [
      "004c4c6c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c4c70",
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
      "004c4c30",
      "PARAM",
      [
        "storage",
        "002ac723",
        null,
        null
      ]
    ],
    [
      "004c4c6c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c4c70",
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

- 旧版 [`004a1da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1d20.md#insn-004a1da0) · [`004a1de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1d20.md#insn-004a1de4) · [`004a1d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1d20.md#insn-004a1d54)
- 新版 `004c4c38`（命令位置の公開資料なし） · `004c4c7c`（命令位置の公開資料なし） · `004c4bec`（命令位置の公開資料なし）

~~~diff
- 004a1da0 ["INT_ADD", "register:40f0:8", ["const:4a1da0:8", "const:4:8"]]
- 004a1da0 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c4c38 ["INT_ADD", "register:40f0:8", ["const:4c4c38:8", "const:4:8"]]
+ 004c4c38 ["CALL", null, ["callee:0043dd98:8"]]
- 004a1da0 bytes 3ee5fd97
+ 004c4c38 bytes 58e4fd97
- 004a1de4 ["INT_ADD", "register:40f0:8", ["const:4a1de4:8", "const:4:8"]]
- 004a1de4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c4c7c ["INT_ADD", "register:40f0:8", ["const:4c4c7c:8", "const:4:8"]]
+ 004c4c7c ["CALL", null, ["callee:00c57b10:8"]]
- 004a1de4 bytes b7e41c94
+ 004c4c7c bytes a54b1e94
- 004a1d54 ["INT_ADD", "register:40f0:8", ["const:4a1d54:8", "const:4:8"]]
- 004a1d54 ["CALL", null, ["callee:00c58a90:8"]]
+ 004c4bec ["INT_ADD", "register:40f0:8", ["const:4c4bec:8", "const:4:8"]]
+ 004c4bec ["CALL", null, ["callee:00c58a90:8"]]
- 004a1d54 bytes bbe81c94
+ 004c4bec bytes a94f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-507bdc448f4c529c24e61da14a95b137"></a>

### [`004a1e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1e34.md) → [`004c4ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4ccc.md) _ZN5Botan10MAC_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_11OctetStringEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00499b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499b28.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc030.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.98% / 新版 92.98%

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
      "definition_site": "004c4d0c",
      "incomplete_value": true,
      "site": "004c4d14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1e74",
      "incomplete_value": true,
      "site": "004a1e7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c4d40",
      "incomplete_value": true,
      "site": "004c4d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a1ea8",
      "incomplete_value": true,
      "site": "004a1eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c4cf4",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c4d14",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4d34",
      "READ",
      [
        "storage",
        "00c1b098",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4cf4",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4d14",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4d34",
      "READ",
      [
        "storage",
        "00c9aa88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1e34.md#insn-004a1e50) · [`004a1e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1e34.md#insn-004a1e5c) · [`004a1e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1e34.md#insn-004a1e78)
- 新版 `004c4ce8`（命令位置の公開資料なし） · `004c4cf4`（命令位置の公開資料なし）

~~~diff
- 004a1e50 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004c4ce8 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004a1e50 bytes c93b00d0
+ 004c4ce8 bytes a93e00d0
- 004a1e5c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
- 004a1e5c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4cf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
+ 004c4cf4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a1e5c bytes 294140f9
+ 004c4cf4 bytes 293945f9
- 004a1e78 ["COPY", "register:40b8:8", ["register:4000:8"]]
- 004a1e78 bytes f70300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acea2480be7d800a5f6857249d32c9d2"></a>

### [`004a20b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a20b4.md) → [`004c4f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4f4c.md) _ZN5Botan12Keyed_Filter6set_ivERKNS_11OctetStringE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbf40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58990.md)

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
      "definition_site": "004c5000",
      "incomplete_value": true,
      "site": "004c500c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a2168",
      "incomplete_value": true,
      "site": "004a2174",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c4ffc",
      "incomplete_value": false,
      "site": "004c500c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a2164",
      "incomplete_value": false,
      "site": "004a2174",
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
      "004c4ffc",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c5000",
      "READ",
      [
        "storage",
        "00c1b050",
        null,
        "pointer"
      ]
    ],
    [
      "004c5000",
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
      "004c4ffc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c5000",
      "READ",
      [
        "storage",
        "00c9aa40",
        null,
        "pointer"
      ]
    ],
    [
      "004c5000",
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

- 旧版 [`004a2174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a20b4.md#insn-004a2174) · [`004a2114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a20b4.md#insn-004a2114) · [`004a212c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a20b4.md#insn-004a212c)
- 新版 `004c500c`（命令位置の公開資料なし） · `004c4fac`（命令位置の公開資料なし） · `004c4fc4`（命令位置の公開資料なし）

~~~diff
- 004a2174 ["INT_ADD", "register:40f0:8", ["const:4a2174:8", "const:4:8"]]
- 004a2174 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c500c ["INT_ADD", "register:40f0:8", ["const:4c500c:8", "const:4:8"]]
+ 004c500c ["CALL", null, ["callee:00c57b10:8"]]
- 004a2174 bytes d3e31c94
+ 004c500c bytes c14a1e94
- 004a2114 ["INT_ADD", "register:40f0:8", ["const:4a2114:8", "const:4:8"]]
- 004a2114 ["CALL", null, ["callee:00c57af0:8"]]
+ 004c4fac ["INT_ADD", "register:40f0:8", ["const:4c4fac:8", "const:4:8"]]
+ 004c4fac ["CALL", null, ["callee:00c57af0:8"]]
- 004a2114 bytes e3e31c94
+ 004c4fac bytes d14a1e94
- 004a212c ["COPY", "register:0:8", ["register:4048:8"]]
- 004a212c ["INT_ADD", "register:40f0:8", ["const:4a212c:8", "const:4:8"]]
- 004a212c ["CALLIND", null, ["register:0:8"]]
+ 004c4fc4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c4fc4 ["INT_ADD", "register:40f0:8", ["const:4c4fc4:8", "const:4:8"]]
+ 004c4fc4 ["CALLIND", null, ["register:0:8"]]
- 004a212c bytes 20013fd6
+ 004c4fc4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86d395cf0da89503fda0234aa1527cd6"></a>

### [`004a21c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a21c8.md) → [`004c5060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5060.md) _ZN5Botan5ChainC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.12% / 新版 97.12%

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
      "definition_site": "004c5098",
      "incomplete_value": true,
      "site": "004c509c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2200",
      "incomplete_value": true,
      "site": "004a2204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c50c8",
      "incomplete_value": true,
      "site": "004c50cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2230",
      "incomplete_value": true,
      "site": "004a2234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c5080",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c509c",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c50bc",
      "READ",
      [
        "storage",
        "00c1b0a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5080",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c509c",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c50bc",
      "READ",
      [
        "storage",
        "00c9aa90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a21e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a21c8.md#insn-004a21e0) · [`004a21e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a21c8.md#insn-004a21e8) · [`004a221c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a21c8.md#insn-004a221c)
- 新版 `004c5078`（命令位置の公開資料なし） · `004c5080`（命令位置の公開資料なし） · `004c50b4`（命令位置の公開資料なし）

~~~diff
- 004a21e0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c5078 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a21e0 bytes c83b00b0
+ 004c5078 bytes a83e00b0
- 004a21e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 004a21e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5080 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 004c5080 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a21e8 bytes 084140f9
+ 004c5080 bytes 083945f9
- 004a221c ["INT_ADD", "register:40f0:8", ["const:4a221c:8", "const:4:8"]]
- 004a221c ["CALL", null, ["callee:00543c1c:8"]]
+ 004c50b4 ["INT_ADD", "register:40f0:8", ["const:4c50b4:8", "const:4:8"]]
+ 004c50b4 ["CALL", null, ["callee:00543c1c:8"]]
- 004a221c bytes dafa0194
+ 004c50b4 bytes dafa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59732581ff14d3ecdb56813449b053f2"></a>

### [`004a2390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2390.md) → [`004c5228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5228.md) _ZN5Botan5ChainC1EPPNS_6FilterEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "definition_site": "004c5254",
      "incomplete_value": true,
      "site": "004c5258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a23bc",
      "incomplete_value": true,
      "site": "004a23c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c5284",
      "incomplete_value": true,
      "site": "004c5288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a23ec",
      "incomplete_value": true,
      "site": "004a23f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c5244",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c5258",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5278",
      "READ",
      [
        "storage",
        "00c1b0a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5244",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5258",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5278",
      "READ",
      [
        "storage",
        "00c9aa90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a23a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2390.md#insn-004a23a0) · [`004a23ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2390.md#insn-004a23ac) · [`004a23d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2390.md#insn-004a23d8)
- 新版 `004c5238`（命令位置の公開資料なし） · `004c5244`（命令位置の公開資料なし） · `004c5270`（命令位置の公開資料なし）

~~~diff
- 004a23a0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c5238 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a23a0 bytes c83b00b0
+ 004c5238 bytes a83e00b0
- 004a23ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 004a23ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5244 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 004c5244 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a23ac bytes 084140f9
+ 004c5244 bytes 083945f9
- 004a23d8 ["INT_ADD", "register:40f0:8", ["const:4a23d8:8", "const:4:8"]]
- 004a23d8 ["CALL", null, ["callee:00543c1c:8"]]
+ 004c5270 ["INT_ADD", "register:40f0:8", ["const:4c5270:8", "const:4:8"]]
+ 004c5270 ["CALL", null, ["callee:00543c1c:8"]]
- 004a23d8 bytes 6bfa0194
+ 004c5270 bytes 6bfa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eab813d5084c30337b65366bf8570b1f"></a>

### [`004a24b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a24b0.md) → [`004c5348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5348.md) _ZN5Botan4ForkC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00520ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ec4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00543d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543d5c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

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
      "definition_site": "004c5390",
      "incomplete_value": true,
      "site": "004c5398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a24f8",
      "incomplete_value": true,
      "site": "004a2500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c53c8",
      "incomplete_value": true,
      "site": "004c53d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2530",
      "incomplete_value": true,
      "site": "004a2538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c5374",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c5398",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c53bc",
      "READ",
      [
        "storage",
        "00c1b0a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5374",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5398",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c53bc",
      "READ",
      [
        "storage",
        "00c9aa98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a24d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a24b0.md#insn-004a24d0) · [`004a24dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a24b0.md#insn-004a24dc) · [`004a24fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a24b0.md#insn-004a24fc)
- 新版 `004c5368`（命令位置の公開資料なし） · `004c5374`（命令位置の公開資料なし）

~~~diff
- 004a24d0 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004c5368 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004a24d0 bytes c93b00b0
+ 004c5368 bytes a93e00b0
- 004a24dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
- 004a24dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5374 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
+ 004c5374 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a24dc bytes 294140f9
+ 004c5374 bytes 293945f9
- 004a24fc ["COPY", "register:40c0:8", ["register:4000:8"]]
- 004a24fc bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad432b30ed59e423e8c04085fac89133"></a>

### [`004a2608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2608.md) → [`004c54a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c54a0.md) _ZN5Botan4ForkC1EPPNS_6FilterEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00520ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ec4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00543d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543d5c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

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
      "definition_site": "004c54cc",
      "incomplete_value": true,
      "site": "004c54d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2634",
      "incomplete_value": true,
      "site": "004a2638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c5500",
      "incomplete_value": true,
      "site": "004c5508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2668",
      "incomplete_value": true,
      "site": "004a2670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c54bc",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c54d0",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c54f0",
      "READ",
      [
        "storage",
        "00c1b0a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c54bc",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c54d0",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c54f0",
      "READ",
      [
        "storage",
        "00c9aa98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a2618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2608.md#insn-004a2618) · [`004a2624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2608.md#insn-004a2624) · [`004a2650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2608.md#insn-004a2650)
- 新版 `004c54b0`（命令位置の公開資料なし） · `004c54bc`（命令位置の公開資料なし） · `004c54e8`（命令位置の公開資料なし）

~~~diff
- 004a2618 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c54b0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a2618 bytes c83b00b0
+ 004c54b0 bytes a83e00b0
- 004a2624 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 004a2624 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c54bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 004c54bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a2624 bytes 084140f9
+ 004c54bc bytes 083945f9
- 004a2650 ["INT_ADD", "register:40f0:8", ["const:4a2650:8", "const:4:8"]]
- 004a2650 ["CALL", null, ["callee:00543c1c:8"]]
+ 004c54e8 ["INT_ADD", "register:40f0:8", ["const:4c54e8:8", "const:4:8"]]
+ 004c54e8 ["CALL", null, ["callee:00543c1c:8"]]
- 004a2650 bytes cdf90194
+ 004c54e8 bytes cdf90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c4d023087e38aceb2db1a5fca319a65"></a>

### [`004a2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2710.md) → [`004c55a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c55a8.md) _ZN5Botan15Buffered_FilterC2Emm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc050.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58aa0.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.36% / 新版 91.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c55dc",
      "incomplete_value": true,
      "site": "004c55dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2744",
      "incomplete_value": true,
      "site": "004a2744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c5648",
      "incomplete_value": false,
      "site": "004c5650",
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
            "const:9d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a27b0",
      "incomplete_value": false,
      "site": "004a27b8",
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
            "const:787:8"
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
      "definition_site": "004c5680",
      "incomplete_value": true,
      "site": "004c568c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a27e8",
      "incomplete_value": true,
      "site": "004a27f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c55d0",
      "READ",
      [
        "storage",
        "00c1b0b0",
        null,
        "pointer"
      ]
    ],
    [
      "004c55dc",
      "DATA",
      [
        "storage",
        "00be98e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c5648",
      "PARAM",
      [
        "storage",
        "00294787",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c55d0",
      "READ",
      [
        "storage",
        "00c9aaa0",
        null,
        "pointer"
      ]
    ],
    [
      "004c55dc",
      "DATA",
      [
        "storage",
        "00c664a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c5648",
      "PARAM",
      [
        "storage",
        "002a409d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a27b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2710.md#insn-004a27b8) · [`004a27f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2710.md#insn-004a27f4) · [`004a2814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2710.md#insn-004a2814)
- 新版 `004c5650`（命令位置の公開資料なし） · `004c568c`（命令位置の公開資料なし） · `004c56ac`（命令位置の公開資料なし）

~~~diff
- 004a27b8 ["INT_ADD", "register:40f0:8", ["const:4a27b8:8", "const:4:8"]]
- 004a27b8 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c5650 ["INT_ADD", "register:40f0:8", ["const:4c5650:8", "const:4:8"]]
+ 004c5650 ["CALL", null, ["callee:0043dd98:8"]]
- 004a27b8 bytes b8e2fd97
+ 004c5650 bytes d2e1fd97
- 004a27f4 ["INT_ADD", "register:40f0:8", ["const:4a27f4:8", "const:4:8"]]
- 004a27f4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c568c ["INT_ADD", "register:40f0:8", ["const:4c568c:8", "const:4:8"]]
+ 004c568c ["CALL", null, ["callee:00c57b10:8"]]
- 004a27f4 bytes 33e21c94
+ 004c568c bytes 21491e94
- 004a2814 ["INT_ADD", "register:40f0:8", ["const:4a2814:8", "const:4:8"]]
- 004a2814 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c56ac ["INT_ADD", "register:40f0:8", ["const:4c56ac:8", "const:4:8"]]
+ 004c56ac ["CALL", null, ["callee:0043dd98:8"]]
- 004a2814 bytes a1e2fd97
+ 004c56ac bytes bbe1fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b39a6944965ef15d7dd848e952c5c83e"></a>

### [`004a29fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a29fc.md) → [`004c5894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5894.md) _ZN5Botan15Buffered_Filter7end_msgEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc070.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ac0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.10% / 新版 97.10%

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
      "definition_site": "004c595c",
      "incomplete_value": false,
      "site": "004c5964",
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
            "const:6f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a2ac4",
      "incomplete_value": false,
      "site": "004a2acc",
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
            "const:876:8"
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
      "definition_site": "004c5994",
      "incomplete_value": true,
      "site": "004c59a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a2afc",
      "incomplete_value": true,
      "site": "004a2b08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c5990",
      "incomplete_value": false,
      "site": "004c59a0",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a2af8",
      "incomplete_value": false,
      "site": "004a2b08",
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
      "004c595c",
      "PARAM",
      [
        "storage",
        "00293876",
        null,
        "string"
      ]
    ],
    [
      "004c5990",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c5994",
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
      "004c595c",
      "PARAM",
      [
        "storage",
        "002a306f",
        null,
        "string"
      ]
    ],
    [
      "004c5990",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c5994",
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

- 旧版 [`004a2acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a29fc.md#insn-004a2acc) · [`004a2b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a29fc.md#insn-004a2b08) · [`004a2a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a29fc.md#insn-004a2a68)
- 新版 `004c5964`（命令位置の公開資料なし） · `004c59a0`（命令位置の公開資料なし） · `004c5900`（命令位置の公開資料なし）

~~~diff
- 004a2acc ["INT_ADD", "register:40f0:8", ["const:4a2acc:8", "const:4:8"]]
- 004a2acc ["CALL", null, ["callee:0043dd98:8"]]
+ 004c5964 ["INT_ADD", "register:40f0:8", ["const:4c5964:8", "const:4:8"]]
+ 004c5964 ["CALL", null, ["callee:0043dd98:8"]]
- 004a2acc bytes f3e1fd97
+ 004c5964 bytes 0de1fd97
- 004a2b08 ["INT_ADD", "register:40f0:8", ["const:4a2b08:8", "const:4:8"]]
- 004a2b08 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c59a0 ["INT_ADD", "register:40f0:8", ["const:4c59a0:8", "const:4:8"]]
+ 004c59a0 ["CALL", null, ["callee:00c57b10:8"]]
- 004a2b08 bytes 6ee11c94
+ 004c59a0 bytes 5c481e94
- 004a2a68 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a2a68 ["INT_ADD", "register:40f0:8", ["const:4a2a68:8", "const:4:8"]]
- 004a2a68 ["CALLIND", null, ["register:0:8"]]
+ 004c5900 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c5900 ["INT_ADD", "register:40f0:8", ["const:4c5900:8", "const:4:8"]]
+ 004c5900 ["CALLIND", null, ["register:0:8"]]
- 004a2a68 bytes 00013fd6
+ 004c5900 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a52d818432c93042d93d2373eac2675"></a>

### [`004a2b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2b58.md) → [`004c59f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c59f0.md) _ZN5Botan18Cipher_Mode_FilterC1EPNS_11Cipher_ModeE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc140.md) · 呼出先 7件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c58b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b90.md) · 呼出先 7件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c5a18",
      "incomplete_value": true,
      "site": "004c5a1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2b80",
      "incomplete_value": true,
      "site": "004a2b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c5a48",
      "incomplete_value": true,
      "site": "004c5a4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2bb0",
      "incomplete_value": true,
      "site": "004a2bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "004c5abc",
      "incomplete_value": true,
      "site": "004c5ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a2c24",
      "incomplete_value": true,
      "site": "004a2c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c5a0c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c5a1c",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5a3c",
      "READ",
      [
        "storage",
        "00c1b0b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5a0c",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5a1c",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5a3c",
      "READ",
      [
        "storage",
        "00c9aaa8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a2cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2b58.md#insn-004a2cd4) · [`004a2b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2b58.md#insn-004a2b6c) · [`004a2b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2b58.md#insn-004a2b74)
- 新版 `004c5b6c`（命令位置の公開資料なし） · `004c5a04`（命令位置の公開資料なし） · `004c5a0c`（命令位置の公開資料なし）

~~~diff
- 004a2cd4 ["INT_ADD", "register:40f0:8", ["const:4a2cd4:8", "const:4:8"]]
- 004a2cd4 ["CALL", null, ["callee:00c58250:8"]]
+ 004c5b6c ["INT_ADD", "register:40f0:8", ["const:4c5b6c:8", "const:4:8"]]
+ 004c5b6c ["CALL", null, ["callee:00c58250:8"]]
- 004a2cd4 bytes cbe21c94
+ 004c5b6c bytes b9491e94
- 004a2b6c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c5a04 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a2b6c bytes c83b00b0
+ 004c5a04 bytes a83e00b0
- 004a2b74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 004a2b74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5a0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 004c5a0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a2b74 bytes 084140f9
+ 004c5a0c bytes 083945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc3f39791a40af09efa056d7bb381b68"></a>

### [`004a2f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2f20.md) → [`004c5db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5db8.md) _ZN5Botan18Cipher_Mode_Filter9start_msgEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.39% / 新版 96.39%

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
      "definition_site": "004c5e70",
      "incomplete_value": false,
      "site": "004c5e7c",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a2fd8",
      "incomplete_value": false,
      "site": "004a2fe4",
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
            "const:79f:8"
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
      "definition_site": "004c5e9c",
      "incomplete_value": false,
      "site": "004c5ea4",
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
            "const:6ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a3004",
      "incomplete_value": false,
      "site": "004a300c",
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
            "const:553:8"
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
      "definition_site": "004c5ef0",
      "incomplete_value": true,
      "site": "004c5efc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a3058",
      "incomplete_value": true,
      "site": "004a3064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c5e70",
      "PARAM",
      [
        "storage",
        "002a679f",
        null,
        "string"
      ]
    ],
    [
      "004c5e9c",
      "PARAM",
      [
        "storage",
        "0029c553",
        null,
        "string"
      ]
    ],
    [
      "004c5eec",
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
      "004c5e70",
      "PARAM",
      [
        "storage",
        "002b7290",
        null,
        "string"
      ]
    ],
    [
      "004c5e9c",
      "PARAM",
      [
        "storage",
        "002ac6ec",
        null,
        "string"
      ]
    ],
    [
      "004c5eec",
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

- 旧版 [`004a2fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2f20.md#insn-004a2fe4) · [`004a300c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2f20.md#insn-004a300c) · [`004a3064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a2f20.md#insn-004a3064)
- 新版 `004c5e7c`（命令位置の公開資料なし） · `004c5ea4`（命令位置の公開資料なし） · `004c5efc`（命令位置の公開資料なし）

~~~diff
- 004a2fe4 ["INT_ADD", "register:40f0:8", ["const:4a2fe4:8", "const:4:8"]]
- 004a2fe4 ["CALL", null, ["callee:00c57b60:8"]]
+ 004c5e7c ["INT_ADD", "register:40f0:8", ["const:4c5e7c:8", "const:4:8"]]
+ 004c5e7c ["CALL", null, ["callee:00c57b60:8"]]
- 004a2fe4 bytes 4be01c94
+ 004c5e7c bytes 39471e94
- 004a300c ["INT_ADD", "register:40f0:8", ["const:4a300c:8", "const:4:8"]]
- 004a300c ["CALL", null, ["callee:00c57b70:8"]]
+ 004c5ea4 ["INT_ADD", "register:40f0:8", ["const:4c5ea4:8", "const:4:8"]]
+ 004c5ea4 ["CALL", null, ["callee:00c57b70:8"]]
- 004a300c bytes 45e01c94
+ 004c5ea4 bytes 33471e94
- 004a3064 ["INT_ADD", "register:40f0:8", ["const:4a3064:8", "const:4:8"]]
- 004a3064 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c5efc ["INT_ADD", "register:40f0:8", ["const:4c5efc:8", "const:4:8"]]
+ 004c5efc ["CALL", null, ["callee:00c57b10:8"]]
- 004a3064 bytes 17e01c94
+ 004c5efc bytes 05471e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e86662df2056f4b4a25eac935f13f4d"></a>

### [`004a32dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a32dc.md) → [`004c6174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6174.md) _ZN5Botan15DataSink_Stream5writeEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

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
      "definition_site": "004c61f0",
      "incomplete_value": false,
      "site": "004c61fc",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a3358",
      "incomplete_value": false,
      "site": "004a3364",
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
            "const:7a7:8"
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
      "definition_site": "004c6230",
      "incomplete_value": true,
      "site": "004c623c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:980:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a3398",
      "incomplete_value": true,
      "site": "004a33a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f90:8"
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
      "definition_site": "004c622c",
      "incomplete_value": false,
      "site": "004c623c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a3394",
      "incomplete_value": false,
      "site": "004a33a4",
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
      "004c61f0",
      "PARAM",
      [
        "storage",
        "002a67a7",
        null,
        "string"
      ]
    ],
    [
      "004c622c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c6230",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c61f0",
      "PARAM",
      [
        "storage",
        "002b7298",
        null,
        "string"
      ]
    ],
    [
      "004c622c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c6230",
      "READ",
      [
        "storage",
        "00c9a980",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a3364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a32dc.md#insn-004a3364) · [`004a33a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a32dc.md#insn-004a33a4) · [`004a3304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a32dc.md#insn-004a3304)
- 新版 `004c61fc`（命令位置の公開資料なし） · `004c623c`（命令位置の公開資料なし） · `004c619c`（命令位置の公開資料なし）

~~~diff
- 004a3364 ["INT_ADD", "register:40f0:8", ["const:4a3364:8", "const:4:8"]]
- 004a3364 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004c61fc ["INT_ADD", "register:40f0:8", ["const:4c61fc:8", "const:4:8"]]
+ 004c61fc ["CALL", null, ["callee:00c57cb0:8"]]
- 004a3364 bytes bfdf1c94
+ 004c61fc bytes ad461e94
- 004a33a4 ["INT_ADD", "register:40f0:8", ["const:4a33a4:8", "const:4:8"]]
- 004a33a4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c623c ["INT_ADD", "register:40f0:8", ["const:4c623c:8", "const:4:8"]]
+ 004c623c ["CALL", null, ["callee:00c57b10:8"]]
- 004a33a4 bytes 47df1c94
+ 004c623c bytes 35461e94
- 004a3304 ["INT_ADD", "register:40f0:8", ["const:4a3304:8", "const:4:8"]]
- 004a3304 ["CALL", null, ["callee:00c58870:8"]]
+ 004c619c ["INT_ADD", "register:40f0:8", ["const:4c619c:8", "const:4:8"]]
+ 004c619c ["CALL", null, ["callee:00c58870:8"]]
- 004a3304 bytes c7e21c94
+ 004c619c bytes b5491e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5afc6c18188d772a72aa5090b7a4824a"></a>

### [`004a3400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3400.md) → [`004c6298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6298.md) _ZN5Botan15DataSink_StreamC2ERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEERKNS1_12basic_stringIcS4_NS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "004c62c4",
      "incomplete_value": true,
      "site": "004c62c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a342c",
      "incomplete_value": true,
      "site": "004a3430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c62f4",
      "incomplete_value": true,
      "site": "004c62f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a345c",
      "incomplete_value": true,
      "site": "004a3460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c62b4",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c62c8",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c62e8",
      "READ",
      [
        "storage",
        "00c1b0c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c62b4",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c62c8",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c62e8",
      "READ",
      [
        "storage",
        "00c9aab8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a3410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3400.md#insn-004a3410) · [`004a341c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3400.md#insn-004a341c) · [`004a3448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3400.md#insn-004a3448)
- 新版 `004c62a8`（命令位置の公開資料なし） · `004c62b4`（命令位置の公開資料なし） · `004c62e0`（命令位置の公開資料なし）

~~~diff
- 004a3410 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c62a8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a3410 bytes c83b0090
+ 004c62a8 bytes a83e0090
- 004a341c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 004a341c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c62b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 004c62b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a341c bytes 084140f9
+ 004c62b4 bytes 083945f9
- 004a3448 ["INT_ADD", "register:40f0:8", ["const:4a3448:8", "const:4:8"]]
- 004a3448 ["CALL", null, ["callee:00543c1c:8"]]
+ 004c62e0 ["INT_ADD", "register:40f0:8", ["const:4c62e0:8", "const:4:8"]]
+ 004c62e0 ["CALL", null, ["callee:00543c1c:8"]]
- 004a3448 bytes 4ff60194
+ 004c62e0 bytes 4ff60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fb538b9b25864a8b95812c8a79b3ca0"></a>

### [`004a34dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a34dc.md) → [`004c6374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6374.md) _ZN5Botan15DataSink_StreamC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004a36fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a36fc.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004c6594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6594.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.38% / 新版 94.38%

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
      "definition_site": "004c63b0",
      "incomplete_value": true,
      "site": "004c63b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a3518",
      "incomplete_value": true,
      "site": "004a3520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c63e4",
      "incomplete_value": true,
      "site": "004c63e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a354c",
      "incomplete_value": true,
      "site": "004a3550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c6488",
      "incomplete_value": false,
      "site": "004c6494",
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
            "const:afc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a35f0",
      "incomplete_value": false,
      "site": "004a35fc",
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
            "const:542:8"
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
      "004c639c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c63b8",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c63d8",
      "READ",
      [
        "storage",
        "00c1b0c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c639c",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c63b8",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c63d8",
      "READ",
      [
        "storage",
        "00c9aab8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a35fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a34dc.md#insn-004a35fc) · [`004a3638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a34dc.md#insn-004a3638) · [`004a34f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a34dc.md#insn-004a34f8)
- 新版 `004c6494`（命令位置の公開資料なし） · `004c64d0`（命令位置の公開資料なし） · `004c6390`（命令位置の公開資料なし）

~~~diff
- 004a35fc ["INT_ADD", "register:40f0:8", ["const:4a35fc:8", "const:4:8"]]
- 004a35fc ["CALL", null, ["callee:00c57cb0:8"]]
+ 004c6494 ["INT_ADD", "register:40f0:8", ["const:4c6494:8", "const:4:8"]]
+ 004c6494 ["CALL", null, ["callee:00c57cb0:8"]]
- 004a35fc bytes 19df1c94
+ 004c6494 bytes 07461e94
- 004a3638 ["INT_ADD", "register:40f0:8", ["const:4a3638:8", "const:4:8"]]
- 004a3638 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c64d0 ["INT_ADD", "register:40f0:8", ["const:4c64d0:8", "const:4:8"]]
+ 004c64d0 ["CALL", null, ["callee:00c57b10:8"]]
- 004a3638 bytes a2de1c94
+ 004c64d0 bytes 90451e94
- 004a34f8 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004c6390 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004a34f8 bytes c93b0090
+ 004c6390 bytes a93e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-483da07a8557692fea2c9d8024252a92"></a>

### [`004a36fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a36fc.md) → [`004c6594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6594.md) FUN_004c6594

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004a34dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a34dc.md) · 呼出先 4件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0b0.md) [`00bdc0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0c0.md)
- 新版 呼出元 1件 [`004c6374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6374.md) · 呼出先 4件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c58b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b00.md) [`00c58b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b10.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.45% / 新版 85.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c65d8",
      "incomplete_value": true,
      "site": "004c65d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004a3740",
      "incomplete_value": true,
      "site": "004a3740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c65d0",
      "incomplete_value": true,
      "site": "004c65dc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a3738",
      "incomplete_value": true,
      "site": "004a3744",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004c65e4",
      "incomplete_value": true,
      "site": "004c65e4",
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
      "definition_site": "004a374c",
      "incomplete_value": true,
      "site": "004a374c",
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
    "ordinal": 13,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c65b8",
      "READ",
      [
        "storage",
        "00c1b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "004c65bc",
      "READ",
      [
        "storage",
        "00c1b0d8",
        null,
        "pointer"
      ]
    ],
    [
      "004c65d0",
      "READ",
      [
        "storage",
        "00c13328",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004c65b8",
      "READ",
      [
        "storage",
        "00c9aac0",
        null,
        "pointer"
      ]
    ],
    [
      "004c65bc",
      "READ",
      [
        "storage",
        "00c9aac8",
        null,
        "pointer"
      ]
    ],
    [
      "004c65d0",
      "READ",
      [
        "storage",
        "00c92cd0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a3714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a36fc.md#insn-004a3714) · [`004a3718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a36fc.md#insn-004a3718) · [`004a3720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a36fc.md#insn-004a3720)
- 新版 `004c65ac`（命令位置の公開資料なし） · `004c65b0`（命令位置の公開資料なし） · `004c65b8`（命令位置の公開資料なし）

~~~diff
- 004a3714 ["COPY", "register:40c8:8", ["const:c1b000:8"]]
+ 004c65ac ["COPY", "register:40c8:8", ["const:c9a000:8"]]
- 004a3714 bytes d93b0090
+ 004c65ac bytes b93e0090
- 004a3718 ["COPY", "register:40c0:8", ["const:c1b000:8"]]
+ 004c65b0 ["COPY", "register:40c0:8", ["const:c9a000:8"]]
- 004a3718 bytes d83b0090
+ 004c65b0 bytes b83e0090
- 004a3720 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d0:8"]]
- 004a3720 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c65b8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:ac0:8"]]
+ 004c65b8 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004a3720 bytes 396b40f9
+ 004c65b8 bytes 396345f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30422829f5c0ce83e43e73cf7216ac14"></a>

### [`004a3b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3b2c.md) → [`004c69c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c69c4.md) _ZN5Botan6Filter8set_portEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
      "definition_site": "004c6a30",
      "incomplete_value": false,
      "site": "004c6a38",
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
            "const:3d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a3b98",
      "incomplete_value": false,
      "site": "004a3ba0",
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
            "const:a19:8"
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
      "definition_site": "004c6a6c",
      "incomplete_value": true,
      "site": "004c6a78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a3bd4",
      "incomplete_value": true,
      "site": "004a3be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c6a68",
      "incomplete_value": false,
      "site": "004c6a78",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a3bd0",
      "incomplete_value": false,
      "site": "004a3be0",
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
      "004c6a30",
      "PARAM",
      [
        "storage",
        "002afa19",
        null,
        "string"
      ]
    ],
    [
      "004c6a68",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c6a6c",
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
      "004c6a30",
      "PARAM",
      [
        "storage",
        "002c103d",
        null,
        "string"
      ]
    ],
    [
      "004c6a68",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c6a6c",
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

- 旧版 [`004a3ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3b2c.md#insn-004a3ba0) · [`004a3be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3b2c.md#insn-004a3be0) · [`004a3b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3b2c.md#insn-004a3b8c)
- 新版 `004c6a38`（命令位置の公開資料なし） · `004c6a78`（命令位置の公開資料なし） · `004c6a24`（命令位置の公開資料なし）

~~~diff
- 004a3ba0 ["INT_ADD", "register:40f0:8", ["const:4a3ba0:8", "const:4:8"]]
- 004a3ba0 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c6a38 ["INT_ADD", "register:40f0:8", ["const:4c6a38:8", "const:4:8"]]
+ 004c6a38 ["CALL", null, ["callee:0043dd98:8"]]
- 004a3ba0 bytes beddfd97
+ 004c6a38 bytes d8dcfd97
- 004a3be0 ["INT_ADD", "register:40f0:8", ["const:4a3be0:8", "const:4:8"]]
- 004a3be0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c6a78 ["INT_ADD", "register:40f0:8", ["const:4c6a78:8", "const:4:8"]]
+ 004c6a78 ["CALL", null, ["callee:00c57b10:8"]]
- 004a3be0 bytes 38dd1c94
+ 004c6a78 bytes 26441e94
- 004a3b8c ["INT_ADD", "register:40f0:8", ["const:4a3b8c:8", "const:4:8"]]
- 004a3b8c ["CALL", null, ["callee:00c57af0:8"]]
+ 004c6a24 ["INT_ADD", "register:40f0:8", ["const:4c6a24:8", "const:4:8"]]
+ 004c6a24 ["CALL", null, ["callee:00c57af0:8"]]
- 004a3b8c bytes 45dd1c94
+ 004c6a24 bytes 33441e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a4bc96c8203906f0c47f3d2b34371ef"></a>

### [`004a3c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3c6c.md) → [`004c6b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6b04.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_10Cipher_DirE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc120.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b70.md) · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.78% / 新版 97.78%

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
      "definition_site": "004c6ba8",
      "incomplete_value": true,
      "site": "004c6bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a3d10",
      "incomplete_value": true,
      "site": "004a3d18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c6ba4",
      "incomplete_value": false,
      "site": "004c6bb0",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a3d0c",
      "incomplete_value": false,
      "site": "004a3d18",
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
      "004c6ba4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c6ba8",
      "READ",
      [
        "storage",
        "00c1b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "004c6ba8",
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
      "004c6ba4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c6ba8",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      "004c6ba8",
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

- 旧版 [`004a3d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3c6c.md#insn-004a3d18) · [`004a3c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3c6c.md#insn-004a3c98) · [`004a3ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3c6c.md#insn-004a3ca8)
- 新版 `004c6bb0`（命令位置の公開資料なし） · `004c6b30`（命令位置の公開資料なし） · `004c6b40`（命令位置の公開資料なし）

~~~diff
- 004a3d18 ["INT_ADD", "register:40f0:8", ["const:4a3d18:8", "const:4:8"]]
- 004a3d18 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c6bb0 ["INT_ADD", "register:40f0:8", ["const:4c6bb0:8", "const:4:8"]]
+ 004c6bb0 ["CALL", null, ["callee:00c57b10:8"]]
- 004a3d18 bytes eadc1c94
+ 004c6bb0 bytes d8431e94
- 004a3c98 ["INT_ADD", "register:40f0:8", ["const:4a3c98:8", "const:4:8"]]
- 004a3c98 ["CALL", null, ["callee:00c58b80:8"]]
+ 004c6b30 ["INT_ADD", "register:40f0:8", ["const:4c6b30:8", "const:4:8"]]
+ 004c6b30 ["CALL", null, ["callee:00c58b80:8"]]
- 004a3c98 bytes 26e11c94
+ 004c6b30 bytes 14481e94
- 004a3ca8 ["INT_ADD", "register:40f0:8", ["const:4a3ca8:8", "const:4:8"]]
- 004a3ca8 ["CALL", null, ["callee:00c57a90:8"]]
+ 004c6b40 ["INT_ADD", "register:40f0:8", ["const:4c6b40:8", "const:4:8"]]
+ 004c6b40 ["CALL", null, ["callee:00c57a90:8"]]
- 004a3ca8 bytes e6dc1c94
+ 004c6b40 bytes d4431e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64aa8fa43e2218bcb69f4358aae3d386"></a>

### [`004a3d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3d70.md) → [`004c6c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6c08.md) _ZN5Botan15get_cipher_modeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_10Cipher_DirES8_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc130.md) · 呼出先 27件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`004aec4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004aec4c.md) [`004aece4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004aece4.md) [`00524c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c94.md)
- 新版 呼出元 1件 [`00c58b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b80.md) · 呼出先 27件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`004d1ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1ae4.md) [`004d1b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1b7c.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c6c68",
      "incomplete_value": true,
      "site": "004c6c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a3dd0",
      "incomplete_value": true,
      "site": "004a3dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004c6cc4",
      "incomplete_value": false,
      "site": "004c6cd0",
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
      "definition_site": "004a3e2c",
      "incomplete_value": false,
      "site": "004a3e38",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c6d94",
      "incomplete_value": true,
      "site": "004c6d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004a3efc",
      "incomplete_value": true,
      "site": "004a3f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "004c6c60",
      "READ",
      [
        "storage",
        "00c1b0e8",
        null,
        "pointer"
      ]
    ],
    [
      "004c6c68",
      "DATA",
      [
        "storage",
        "00becda0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004c6cd0",
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
      "004c6c60",
      "READ",
      [
        "storage",
        "00c9aad8",
        null,
        "pointer"
      ]
    ],
    [
      "004c6c68",
      "DATA",
      [
        "storage",
        "00c69960",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004c6cd0",
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

- 旧版 [`004a3dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3d70.md#insn-004a3dac) · [`004a3dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3d70.md#insn-004a3dbc) · [`004a3dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3d70.md#insn-004a3dc0)
- 新版 `004c6c44`（命令位置の公開資料なし） · `004c6c54`（命令位置の公開資料なし） · `004c6c58`（命令位置の公開資料なし）

~~~diff
- 004a3dac ["INT_ADD", "register:40f0:8", ["const:4a3dac:8", "const:4:8"]]
- 004a3dac ["CALL", null, ["callee:00c58a60:8"]]
+ 004c6c44 ["INT_ADD", "register:40f0:8", ["const:4c6c44:8", "const:4:8"]]
+ 004c6c44 ["CALL", null, ["callee:00c58a60:8"]]
- 004a3dac bytes 99e01c94
+ 004c6c44 bytes 87471e94
- 004a3dbc ["INT_ADD", "register:40f0:8", ["const:4a3dbc:8", "const:4:8"]]
- 004a3dbc ["CALL", null, ["callee:00c57a90:8"]]
+ 004c6c54 ["INT_ADD", "register:40f0:8", ["const:4c6c54:8", "const:4:8"]]
+ 004c6c54 ["CALL", null, ["callee:00c57a90:8"]]
- 004a3dbc bytes a1dc1c94
+ 004c6c54 bytes 8f431e94
- 004a3dc0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c6c58 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a3dc0 bytes c83b0090
+ 004c6c58 bytes a83e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b4a17fd28165e4783a1d0543f9fd433"></a>

### [`004a4974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4974.md) → [`004c780c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c780c.md) _ZN5Botan11SecureQueue4readEPhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1a0.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00c58bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bf0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c78e0",
      "incomplete_value": true,
      "site": "004c78e0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004a4a48",
      "incomplete_value": true,
      "site": "004a4a48",
      "value": [
        "LOAD",
        "8",
        [
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
      "004c78d0",
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
      "004c78d0",
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

- 旧版 [`004a4a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4974.md#insn-004a4a48) · [`004a49a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4974.md#insn-004a49a8) · [`004a49f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4974.md#insn-004a49f8)
- 新版 `004c78e0`（命令位置の公開資料なし） · `004c7840`（命令位置の公開資料なし） · `004c7890`（命令位置の公開資料なし）

~~~diff
- 004a4a48 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a4a48 ["INT_ADD", "register:40f0:8", ["const:4a4a48:8", "const:4:8"]]
- 004a4a48 ["CALLIND", null, ["register:0:8"]]
+ 004c78e0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c78e0 ["INT_ADD", "register:40f0:8", ["const:4c78e0:8", "const:4:8"]]
+ 004c78e0 ["CALLIND", null, ["register:0:8"]]
- 004a4a48 bytes 20013fd6
+ 004c78e0 bytes 20013fd6
- 004a49a8 ["COPY", "register:40d0:8", ["const:bea000:8"]]
+ 004c7840 ["COPY", "register:40d0:8", ["const:c67000:8"]]
- 004a49a8 bytes 3a3a00d0
+ 004c7840 bytes 1a3d0090
- 004a49f8 ["INT_ADD", "register:40f0:8", ["const:4a49f8:8", "const:4:8"]]
- 004a49f8 ["CALL", null, ["callee:00c57b40:8"]]
+ 004c7890 ["INT_ADD", "register:40f0:8", ["const:4c7890:8", "const:4:8"]]
+ 004c7890 ["CALL", null, ["callee:00c57b40:8"]]
- 004a49f8 bytes bed91c94
+ 004c7890 bytes ac401e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f009e2c7d09d84b49515f8e939eb449b"></a>

### [`004a4bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4bf0.md) → [`004c7a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7a88.md) FUN_004c7a88

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004a5d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5d40.md) · 呼出先 3件 [`00520ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ff4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 1件 [`004c8bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8bd8.md) · 呼出先 3件 [`00543e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c7b60",
      "incomplete_value": false,
      "site": "004c7b80",
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
            "const:adb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a4cc8",
      "incomplete_value": false,
      "site": "004a4ce8",
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
            "const:c02:8"
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
      "definition_site": "004c7b68",
      "incomplete_value": false,
      "site": "004c7b80",
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
            "const:ae1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a4cd0",
      "incomplete_value": false,
      "site": "004a4ce8",
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
            "const:c08:8"
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
      "definition_site": "004c7b70",
      "incomplete_value": false,
      "site": "004c7b80",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a4cd8",
      "incomplete_value": false,
      "site": "004a4ce8",
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
            "const:9cb:8"
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
      "004c7b60",
      "PARAM",
      [
        "storage",
        "00299c02",
        null,
        "string"
      ]
    ],
    [
      "004c7b68",
      "PARAM",
      [
        "storage",
        "00299c08",
        null,
        "string"
      ]
    ],
    [
      "004c7b70",
      "PARAM",
      [
        "storage",
        "002969cb",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c7b60",
      "PARAM",
      [
        "storage",
        "002a9adb",
        null,
        "string"
      ]
    ],
    [
      "004c7b68",
      "PARAM",
      [
        "storage",
        "002a9ae1",
        null,
        "string"
      ]
    ],
    [
      "004c7b70",
      "PARAM",
      [
        "storage",
        "002a6500",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a4ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4bf0.md#insn-004a4ce8) · [`004a4d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4bf0.md#insn-004a4d20) · [`004a4c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4bf0.md#insn-004a4c64)
- 新版 `004c7b80`（命令位置の公開資料なし） · `004c7bb8`（命令位置の公開資料なし） · `004c7afc`（命令位置の公開資料なし）

~~~diff
- 004a4ce8 ["INT_ADD", "register:40f0:8", ["const:4a4ce8:8", "const:4:8"]]
- 004a4ce8 ["CALL", null, ["callee:00c58250:8"]]
+ 004c7b80 ["INT_ADD", "register:40f0:8", ["const:4c7b80:8", "const:4:8"]]
+ 004c7b80 ["CALL", null, ["callee:00c58250:8"]]
- 004a4ce8 bytes c6da1c94
+ 004c7b80 bytes b4411e94
- 004a4d20 ["INT_ADD", "register:40f0:8", ["const:4a4d20:8", "const:4:8"]]
- 004a4d20 ["CALL", null, ["callee:00c58250:8"]]
+ 004c7bb8 ["INT_ADD", "register:40f0:8", ["const:4c7bb8:8", "const:4:8"]]
+ 004c7bb8 ["CALL", null, ["callee:00c58250:8"]]
- 004a4d20 bytes b8da1c94
+ 004c7bb8 bytes a6411e94
- 004a4c64 ["INT_ADD", "register:40f0:8", ["const:4a4c64:8", "const:4:8"]]
- 004a4c64 ["CALL", null, ["callee:00543e8c:8"]]
+ 004c7afc ["INT_ADD", "register:40f0:8", ["const:4c7afc:8", "const:4:8"]]
+ 004c7afc ["CALL", null, ["callee:00543e8c:8"]]
- 004a4c64 bytes e4f00194
+ 004c7afc bytes e4f00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bf3e1373e39d56a852d0f8c9bc640e6"></a>

### [`004a4ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4ea0.md) → [`004c7d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7d38.md) _ZN5Botan4PipeC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdc1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c10.md)

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
      "definition_site": "004c7d6c",
      "incomplete_value": true,
      "site": "004c7d74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a4ed4",
      "incomplete_value": true,
      "site": "004a4edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c7d58",
      "READ",
      [
        "storage",
        "00c1b110",
        null,
        "pointer"
      ]
    ],
    [
      "004c7d74",
      "DATA",
      [
        "storage",
        "00be9a80",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c7d58",
      "READ",
      [
        "storage",
        "00c9ab00",
        null,
        "pointer"
      ]
    ],
    [
      "004c7d74",
      "DATA",
      [
        "storage",
        "00c66640",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a4eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4ea0.md#insn-004a4eb4) · [`004a4ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4ea0.md#insn-004a4ec0) · [`004a4ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4ea0.md#insn-004a4ee4)
- 新版 `004c7d4c`（命令位置の公開資料なし） · `004c7d58`（命令位置の公開資料なし） · `004c7d7c`（命令位置の公開資料なし）

~~~diff
- 004a4eb4 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c7d4c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a4eb4 bytes a83b00f0
+ 004c7d4c bytes 883e00f0
- 004a4ec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:110:8"]]
- 004a4ec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7d58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b00:8"]]
+ 004c7d58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a4ec0 bytes 088940f9
+ 004c7d58 bytes 088145f9
- 004a4ee4 ["INT_ADD", "register:40f0:8", ["const:4a4ee4:8", "const:4:8"]]
- 004a4ee4 ["CALL", null, ["callee:00c57a90:8"]]
+ 004c7d7c ["INT_ADD", "register:40f0:8", ["const:4c7d7c:8", "const:4:8"]]
+ 004c7d7c ["CALL", null, ["callee:00c57a90:8"]]
- 004a4ee4 bytes 57d81c94
+ 004c7d7c bytes 453f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f12aa9bd8bf669b27016012d08fa7a0"></a>

### [`004a4f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4f60.md) → [`004c7df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7df8.md) _ZN5Botan4PipeC2ESt16initializer_listIPNS_6FilterEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdc1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c10.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c7e24",
      "incomplete_value": true,
      "site": "004c7e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a4f8c",
      "incomplete_value": true,
      "site": "004a4f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c7e14",
      "READ",
      [
        "storage",
        "00c1b110",
        null,
        "pointer"
      ]
    ],
    [
      "004c7e28",
      "DATA",
      [
        "storage",
        "00be9a80",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c7e14",
      "READ",
      [
        "storage",
        "00c9ab00",
        null,
        "pointer"
      ]
    ],
    [
      "004c7e28",
      "DATA",
      [
        "storage",
        "00c66640",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a4f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4f60.md#insn-004a4f70) · [`004a4f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4f60.md#insn-004a4f7c) · [`004a4f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4f60.md#insn-004a4f98)
- 新版 `004c7e08`（命令位置の公開資料なし） · `004c7e14`（命令位置の公開資料なし） · `004c7e30`（命令位置の公開資料なし）

~~~diff
- 004a4f70 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c7e08 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a4f70 bytes a83b00f0
+ 004c7e08 bytes 883e00f0
- 004a4f7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:110:8"]]
- 004a4f7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7e14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b00:8"]]
+ 004c7e14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a4f7c bytes 088940f9
+ 004c7e14 bytes 088145f9
- 004a4f98 ["INT_ADD", "register:40f0:8", ["const:4a4f98:8", "const:4:8"]]
- 004a4f98 ["CALL", null, ["callee:00c57a90:8"]]
+ 004c7e30 ["INT_ADD", "register:40f0:8", ["const:4c7e30:8", "const:4:8"]]
+ 004c7e30 ["CALL", null, ["callee:00c57a90:8"]]
- 004a4f98 bytes 2ad81c94
+ 004c7e30 bytes 183f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-533533e5eb7752c0104744031790dfaa"></a>

### [`004a5000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5000.md) → [`004c7e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7e98.md) _ZN5Botan4Pipe9do_appendEPNS_6FilterE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1c0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c10.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 94.96% / 新版 94.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004c7ecc",
      "incomplete_value": true,
      "site": "004c7ed0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004a5034",
      "incomplete_value": true,
      "site": "004a5038",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004c7f64",
      "incomplete_value": false,
      "site": "004c7f6c",
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
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a50cc",
      "incomplete_value": false,
      "site": "004a50d4",
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
            "const:39f:8"
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
      "definition_site": "004c7fa0",
      "incomplete_value": true,
      "site": "004c7fac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a5108",
      "incomplete_value": true,
      "site": "004a5114",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c7ec0",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ],
    [
      "004c7f64",
      "PARAM",
      [
        "storage",
        "002a239f",
        null,
        "string"
      ]
    ],
    [
      "004c7f9c",
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
      "004c7ec0",
      "READ",
      [
        "storage",
        "00c9ab08",
        null,
        "pointer"
      ]
    ],
    [
      "004c7f64",
      "PARAM",
      [
        "storage",
        "002b2a60",
        null,
        "string"
      ]
    ],
    [
      "004c7f9c",
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

- 旧版 [`004a50d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5000.md#insn-004a50d4) · [`004a5114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5000.md#insn-004a5114) · [`004a5138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5000.md#insn-004a5138)
- 新版 `004c7f6c`（命令位置の公開資料なし） · `004c7fac`（命令位置の公開資料なし） · `004c7fd0`（命令位置の公開資料なし）

~~~diff
- 004a50d4 ["INT_ADD", "register:40f0:8", ["const:4a50d4:8", "const:4:8"]]
- 004a50d4 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c7f6c ["INT_ADD", "register:40f0:8", ["const:4c7f6c:8", "const:4:8"]]
+ 004c7f6c ["CALL", null, ["callee:0043dd98:8"]]
- 004a50d4 bytes 71d8fd97
+ 004c7f6c bytes 8bd7fd97
- 004a5114 ["INT_ADD", "register:40f0:8", ["const:4a5114:8", "const:4:8"]]
- 004a5114 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c7fac ["INT_ADD", "register:40f0:8", ["const:4c7fac:8", "const:4:8"]]
+ 004c7fac ["CALL", null, ["callee:00c57b10:8"]]
- 004a5114 bytes ebd71c94
+ 004c7fac bytes d93e1e94
- 004a5138 ["INT_ADD", "register:40f0:8", ["const:4a5138:8", "const:4:8"]]
- 004a5138 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c7fd0 ["INT_ADD", "register:40f0:8", ["const:4c7fd0:8", "const:4:8"]]
+ 004c7fd0 ["CALL", null, ["callee:0043dd98:8"]]
- 004a5138 bytes 58d8fd97
+ 004c7fd0 bytes 72d7fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33fe97472a7da42ed40d6c17da1eaa53"></a>

### [`004a52c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a52c0.md) → [`004c8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8158.md) _ZN5Botan4Pipe8destructEPNS_6FilterE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1d0.md) · 呼出先 1件 [`00bdc1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1d0.md)
- 新版 呼出元 1件 [`00c58c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c20.md) · 呼出先 1件 [`00c58c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c20.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004c8180",
      "incomplete_value": true,
      "site": "004c8184",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004a52e8",
      "incomplete_value": true,
      "site": "004a52ec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c8174",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c8174",
      "READ",
      [
        "storage",
        "00c9ab08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a52d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a52c0.md#insn-004a52d4) · [`004a52dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a52c0.md#insn-004a52dc) · [`004a530c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a52c0.md#insn-004a530c)
- 新版 `004c816c`（命令位置の公開資料なし） · `004c8174`（命令位置の公開資料なし） · `004c81a4`（命令位置の公開資料なし）

~~~diff
- 004a52d4 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c816c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a52d4 bytes a83b00d0
+ 004c816c bytes 883e00d0
- 004a52dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:118:8"]]
- 004a52dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c8174 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b08:8"]]
+ 004c8174 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a52dc bytes 088d40f9
+ 004c8174 bytes 088545f9
- 004a530c ["INT_ADD", "register:40f0:8", ["const:4a530c:8", "const:4:8"]]
- 004a530c ["CALL", null, ["callee:00c58c20:8"]]
+ 004c81a4 ["INT_ADD", "register:40f0:8", ["const:4c81a4:8", "const:4:8"]]
+ 004c81a4 ["CALL", null, ["callee:00c58c20:8"]]
- 004a530c bytes b1db1c94
+ 004c81a4 bytes 9f421e94
~~~


<a id="compare-10e2e03ae43aff33d374fbefb45055e5"></a>

### [`004a5350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5350.md) → [`004c81e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c81e8.md) _ZN5Botan4PipeD0Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c30.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "site": "004c81f8",
      "value": [
        "leaf",
        "ram:c58c30:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a5360",
      "value": [
        "leaf",
        "ram:bdc1e0:8"
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
      "004c81f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdc1e0"
      ]
    ]
  ],
  "added": [
    [
      "004c81f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58c30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5350.md#insn-004a5360)
- 新版 `004c81f8`（命令位置の公開資料なし）

~~~diff
- 004a5360 ["INT_ADD", "register:40f0:8", ["const:4a5360:8", "const:4:8"]]
- 004a5360 ["CALL", null, ["ram:bdc1e0:8"]]
+ 004c81f8 ["INT_ADD", "register:40f0:8", ["const:4c81f8:8", "const:4:8"]]
+ 004c81f8 ["CALL", null, ["ram:c58c30:8"]]
- 004a5360 bytes a0db1c94
+ 004c81f8 bytes 8e421e94
~~~


<a id="compare-794750e3f49a361576206fdd9e71383b"></a>

### [`004a53c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a53c0.md) → [`004c8258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8258.md) _ZNK5Botan4Pipe9remainingEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1f0.md) · 呼出先 5件 [`004a6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c40.md) · 呼出先 5件 [`004c96cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

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
      "definition_site": "004c828c",
      "incomplete_value": true,
      "site": "004c828c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a53f4",
      "incomplete_value": true,
      "site": "004a53f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b3:8"
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
      "definition_site": "004c8380",
      "incomplete_value": true,
      "site": "004c8388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a54e8",
      "incomplete_value": true,
      "site": "004a54f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:120:8"
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
      "definition_site": "004c837c",
      "incomplete_value": false,
      "site": "004c8388",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a54e4",
      "incomplete_value": false,
      "site": "004a54f0",
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
      "004c8278",
      "READ",
      [
        "storage",
        "002a44b3",
        null,
        "string"
      ]
    ],
    [
      "004c837c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c8380",
      "READ",
      [
        "storage",
        "00c1b120",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c8278",
      "READ",
      [
        "storage",
        "002b4d20",
        null,
        "string"
      ]
    ],
    [
      "004c837c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c8380",
      "READ",
      [
        "storage",
        "00c9ab10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a54f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a53c0.md#insn-004a54f0) · [`004a53d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a53c0.md#insn-004a53d4) · [`004a53d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a53c0.md#insn-004a53d8)
- 新版 `004c8388`（命令位置の公開資料なし） · `004c826c`（命令位置の公開資料なし） · `004c8270`（命令位置の公開資料なし）

~~~diff
- 004a54f0 ["INT_ADD", "register:40f0:8", ["const:4a54f0:8", "const:4:8"]]
- 004a54f0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c8388 ["INT_ADD", "register:40f0:8", ["const:4c8388:8", "const:4:8"]]
+ 004c8388 ["CALL", null, ["callee:00c57b10:8"]]
- 004a54f0 bytes f4d61c94
+ 004c8388 bytes e23d1e94
- 004a53d4 ["COPY", "register:4050:8", ["const:2a4000:8"]]
+ 004c826c ["COPY", "register:4050:8", ["const:2b4000:8"]]
- 004a53d4 bytes eaeffff0
+ 004c826c bytes 6aefff90
- 004a53d8 ["COPY", "tmp:0:8", ["const:4b3:8"]]
- 004a53d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004a53d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004a53d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004c8270 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 004c8270 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004c8270 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004c8270 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004a53d8 bytes 4acd1291
+ 004c8270 bytes 4a813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aeb23d21879ead02be9cc75c4aea0d0"></a>

### [`004a5538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5538.md) → [`004c83d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c83d0.md) _ZN5Botan4Pipe15set_default_msgEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

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
      "definition_site": "004c8440",
      "incomplete_value": false,
      "site": "004c8448",
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
            "const:b92:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a55a8",
      "incomplete_value": false,
      "site": "004a55b0",
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
            "const:546:8"
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
      "definition_site": "004c847c",
      "incomplete_value": true,
      "site": "004c8488",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a55e4",
      "incomplete_value": true,
      "site": "004a55f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c8478",
      "incomplete_value": false,
      "site": "004c8488",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a55e0",
      "incomplete_value": false,
      "site": "004a55f0",
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
      "004c8440",
      "PARAM",
      [
        "storage",
        "002a1546",
        null,
        "string"
      ]
    ],
    [
      "004c8478",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c847c",
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
      "004c8440",
      "PARAM",
      [
        "storage",
        "002b1b92",
        null,
        "string"
      ]
    ],
    [
      "004c8478",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c847c",
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

- 旧版 [`004a55b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5538.md#insn-004a55b0) · [`004a55f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5538.md#insn-004a55f0) · [`004a559c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5538.md#insn-004a559c)
- 新版 `004c8448`（命令位置の公開資料なし） · `004c8488`（命令位置の公開資料なし） · `004c8434`（命令位置の公開資料なし）

~~~diff
- 004a55b0 ["INT_ADD", "register:40f0:8", ["const:4a55b0:8", "const:4:8"]]
- 004a55b0 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c8448 ["INT_ADD", "register:40f0:8", ["const:4c8448:8", "const:4:8"]]
+ 004c8448 ["CALL", null, ["callee:0043dd98:8"]]
- 004a55b0 bytes 3ad7fd97
+ 004c8448 bytes 54d6fd97
- 004a55f0 ["INT_ADD", "register:40f0:8", ["const:4a55f0:8", "const:4:8"]]
- 004a55f0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c8488 ["INT_ADD", "register:40f0:8", ["const:4c8488:8", "const:4:8"]]
+ 004c8488 ["CALL", null, ["callee:00c57b10:8"]]
- 004a55f0 bytes b4d61c94
+ 004c8488 bytes a23d1e94
- 004a559c ["INT_ADD", "register:40f0:8", ["const:4a559c:8", "const:4:8"]]
- 004a559c ["CALL", null, ["callee:00c57af0:8"]]
+ 004c8434 ["INT_ADD", "register:40f0:8", ["const:4c8434:8", "const:4:8"]]
+ 004c8434 ["CALL", null, ["callee:00c57af0:8"]]
- 004a559c bytes c1d61c94
+ 004c8434 bytes af3d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-855aab62a610ac8a833938db1c231f1f"></a>

### [`004a5698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5698.md) → [`004c8530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8530.md) _ZN5Botan4Pipe9start_msgEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c58c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

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
      "definition_site": "004c8584",
      "incomplete_value": true,
      "site": "004c8588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a56ec",
      "incomplete_value": true,
      "site": "004a56f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004c85a8",
      "incomplete_value": false,
      "site": "004c85b4",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a5710",
      "incomplete_value": false,
      "site": "004a571c",
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
            "const:b98:8"
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
      "definition_site": "004c8610",
      "incomplete_value": false,
      "site": "004c8618",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a5778",
      "incomplete_value": false,
      "site": "004a5780",
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
            "const:ab7:8"
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
      "004c857c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c8588",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c85b4",
      "DATA",
      [
        "storage",
        "00be9b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004c857c",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c8588",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c85b4",
      "DATA",
      [
        "storage",
        "00c66758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5698.md#insn-004a5780) · [`004a57bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5698.md#insn-004a57bc) · [`004a56d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5698.md#insn-004a56d4)
- 新版 `004c8618`（命令位置の公開資料なし） · `004c8654`（命令位置の公開資料なし） · `004c856c`（命令位置の公開資料なし）

~~~diff
- 004a5780 ["INT_ADD", "register:40f0:8", ["const:4a5780:8", "const:4:8"]]
- 004a5780 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c8618 ["INT_ADD", "register:40f0:8", ["const:4c8618:8", "const:4:8"]]
+ 004c8618 ["CALL", null, ["callee:0043dd98:8"]]
- 004a5780 bytes c6d6fd97
+ 004c8618 bytes e0d5fd97
- 004a57bc ["INT_ADD", "register:40f0:8", ["const:4a57bc:8", "const:4:8"]]
- 004a57bc ["CALL", null, ["callee:00c57b10:8"]]
+ 004c8654 ["INT_ADD", "register:40f0:8", ["const:4c8654:8", "const:4:8"]]
+ 004c8654 ["CALL", null, ["callee:00c57b10:8"]]
- 004a57bc bytes 41d61c94
+ 004c8654 bytes 2f3d1e94
- 004a56d4 ["INT_ADD", "register:40f0:8", ["const:4a56d4:8", "const:4:8"]]
- 004a56d4 ["CALL", null, ["callee:00c57a90:8"]]
+ 004c856c ["INT_ADD", "register:40f0:8", ["const:4c856c:8", "const:4:8"]]
+ 004c856c ["CALL", null, ["callee:00c57a90:8"]]
- 004a56d4 bytes 5bd61c94
+ 004c856c bytes 493d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfc47f526403b9dfc3eca7a47a344ad1"></a>

### [`004a5838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5838.md) → [`004c86d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c86d0.md) _ZN5Botan4Pipe5writeEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

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
      "definition_site": "004c873c",
      "incomplete_value": false,
      "site": "004c8744",
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
            "const:fab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a58a4",
      "incomplete_value": false,
      "site": "004a58ac",
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
            "const:992:8"
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
      "definition_site": "004c8778",
      "incomplete_value": true,
      "site": "004c8784",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a58e0",
      "incomplete_value": true,
      "site": "004a58ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c8774",
      "incomplete_value": false,
      "site": "004c8784",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a58dc",
      "incomplete_value": false,
      "site": "004a58ec",
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
      "004c873c",
      "PARAM",
      [
        "storage",
        "00291992",
        null,
        "string"
      ]
    ],
    [
      "004c8774",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c8778",
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
      "004c873c",
      "PARAM",
      [
        "storage",
        "002a0fab",
        null,
        "string"
      ]
    ],
    [
      "004c8774",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c8778",
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

- 旧版 [`004a58ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5838.md#insn-004a58ac) · [`004a58ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5838.md#insn-004a58ec) · [`004a5898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5838.md#insn-004a5898)
- 新版 `004c8744`（命令位置の公開資料なし） · `004c8784`（命令位置の公開資料なし） · `004c8730`（命令位置の公開資料なし）

~~~diff
- 004a58ac ["INT_ADD", "register:40f0:8", ["const:4a58ac:8", "const:4:8"]]
- 004a58ac ["CALL", null, ["callee:0043dd98:8"]]
+ 004c8744 ["INT_ADD", "register:40f0:8", ["const:4c8744:8", "const:4:8"]]
+ 004c8744 ["CALL", null, ["callee:0043dd98:8"]]
- 004a58ac bytes 7bd6fd97
+ 004c8744 bytes 95d5fd97
- 004a58ec ["INT_ADD", "register:40f0:8", ["const:4a58ec:8", "const:4:8"]]
- 004a58ec ["CALL", null, ["callee:00c57b10:8"]]
+ 004c8784 ["INT_ADD", "register:40f0:8", ["const:4c8784:8", "const:4:8"]]
+ 004c8784 ["CALL", null, ["callee:00c57b10:8"]]
- 004a58ec bytes f5d51c94
+ 004c8784 bytes e33c1e94
- 004a5898 ["INT_ADD", "register:40f0:8", ["const:4a5898:8", "const:4:8"]]
- 004a5898 ["CALL", null, ["callee:00c57af0:8"]]
+ 004c8730 ["INT_ADD", "register:40f0:8", ["const:4c8730:8", "const:4:8"]]
+ 004c8730 ["CALL", null, ["callee:00c57af0:8"]]
- 004a5898 bytes 02d61c94
+ 004c8730 bytes f03c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be6a99b0bf70791223df533cdc0db59b"></a>

### [`004a5940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5940.md) → [`004c87d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c87d8.md) _ZN5Botan4Pipe7end_msgEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`004a4d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d88.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c58c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md) · 呼出先 12件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`004c7c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7c20.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c8840",
      "incomplete_value": true,
      "site": "004c8844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a59a8",
      "incomplete_value": true,
      "site": "004a59ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "004c8830",
      "incomplete_value": true,
      "site": "004c8830",
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
      "definition_site": "004a5998",
      "incomplete_value": true,
      "site": "004a5998",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c8878",
      "incomplete_value": true,
      "site": "004c8878",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a59e0",
      "incomplete_value": true,
      "site": "004a59e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c8838",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c8844",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c8868",
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
      "004c8838",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c8844",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c8868",
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

- 旧版 [`004a59e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5940.md#insn-004a59e0) · [`004a5a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5940.md#insn-004a5a3c) · [`004a5a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5940.md#insn-004a5a78)
- 新版 `004c8878`（命令位置の公開資料なし） · `004c88d4`（命令位置の公開資料なし） · `004c8910`（命令位置の公開資料なし）

~~~diff
- 004a59e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a59e0 ["INT_ADD", "register:40f0:8", ["const:4a59e0:8", "const:4:8"]]
- 004a59e0 ["CALLIND", null, ["register:0:8"]]
+ 004c8878 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c8878 ["INT_ADD", "register:40f0:8", ["const:4c8878:8", "const:4:8"]]
+ 004c8878 ["CALLIND", null, ["register:0:8"]]
- 004a59e0 bytes 20013fd6
+ 004c8878 bytes 20013fd6
- 004a5a3c ["INT_ADD", "register:40f0:8", ["const:4a5a3c:8", "const:4:8"]]
- 004a5a3c ["CALL", null, ["callee:0043dd98:8"]]
+ 004c88d4 ["INT_ADD", "register:40f0:8", ["const:4c88d4:8", "const:4:8"]]
+ 004c88d4 ["CALL", null, ["callee:0043dd98:8"]]
- 004a5a3c bytes 17d6fd97
+ 004c88d4 bytes 31d5fd97
- 004a5a78 ["INT_ADD", "register:40f0:8", ["const:4a5a78:8", "const:4:8"]]
- 004a5a78 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c8910 ["INT_ADD", "register:40f0:8", ["const:4c8910:8", "const:4:8"]]
+ 004c8910 ["CALL", null, ["callee:00c57b10:8"]]
- 004a5a78 bytes 92d51c94
+ 004c8910 bytes 803c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efca0611a98b845c8d54974ddcc1379d"></a>

### [`004a5bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5bdc.md) → [`004c8a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8a74.md) _ZN5Botan4Pipe5writeERNS_10DataSourceE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc250.md) · 呼出先 9件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 1件 [`00c58ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ca0.md) · 呼出先 9件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.95% / 新版 95.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c8b30",
      "incomplete_value": true,
      "site": "004c8b30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a5c98",
      "incomplete_value": true,
      "site": "004a5c98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c8b6c",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a5cd4",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c8b8c",
      "incomplete_value": true,
      "site": "004c8b94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a5cf4",
      "incomplete_value": true,
      "site": "004a5cfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c8b1c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c8b6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "004c8b8c",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c8b1c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004c8b6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "004c8b8c",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5bdc.md#insn-004a5c98) · [`004a5cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5bdc.md#insn-004a5cd4) · [`004a5cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5bdc.md#insn-004a5cfc)
- 新版 `004c8b30`（命令位置の公開資料なし） · `004c8b6c`（命令位置の公開資料なし） · `004c8b94`（命令位置の公開資料なし）

~~~diff
- 004a5c98 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a5c98 ["INT_ADD", "register:40f0:8", ["const:4a5c98:8", "const:4:8"]]
- 004a5c98 ["CALLIND", null, ["register:0:8"]]
+ 004c8b30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c8b30 ["INT_ADD", "register:40f0:8", ["const:4c8b30:8", "const:4:8"]]
+ 004c8b30 ["CALLIND", null, ["register:0:8"]]
- 004a5c98 bytes 20013fd6
+ 004c8b30 bytes 20013fd6
- 004a5cd4 ["INT_ADD", "register:40f0:8", ["const:4a5cd4:8", "const:4:8"]]
- 004a5cd4 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004c8b6c ["INT_ADD", "register:40f0:8", ["const:4c8b6c:8", "const:4:8"]]
+ 004c8b6c ["CALL", null, ["ram:c58640:8"]]
- 004a5cd4 bytes c7d71c94
+ 004c8b6c bytes b53e1e94
- 004a5cfc ["INT_ADD", "register:40f0:8", ["const:4a5cfc:8", "const:4:8"]]
- 004a5cfc ["CALL", null, ["callee:00c57b10:8"]]
+ 004c8b94 ["INT_ADD", "register:40f0:8", ["const:4c8b94:8", "const:4:8"]]
+ 004c8b94 ["CALL", null, ["callee:00c57b10:8"]]
- 004a5cfc bytes f1d41c94
+ 004c8b94 bytes df3b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38b0cda313a6cf3bffb5dc1171ddc118"></a>

### [`004a5e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5e90.md) → [`004c8d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8d28.md) _ZN5Botan4Pipe13append_filterEPNS_6FilterE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

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
      "definition_site": "004c8d90",
      "incomplete_value": false,
      "site": "004c8d98",
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
            "const:3eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a5ef8",
      "incomplete_value": false,
      "site": "004a5f00",
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
            "const:9b2:8"
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
      "definition_site": "004c8dcc",
      "incomplete_value": true,
      "site": "004c8dd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a5f34",
      "incomplete_value": true,
      "site": "004a5f40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c8dc8",
      "incomplete_value": false,
      "site": "004c8dd8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a5f30",
      "incomplete_value": false,
      "site": "004a5f40",
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
      "004c8d90",
      "PARAM",
      [
        "storage",
        "002959b2",
        null,
        "string"
      ]
    ],
    [
      "004c8dc8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c8dcc",
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
      "004c8d90",
      "PARAM",
      [
        "storage",
        "002a53eb",
        null,
        "string"
      ]
    ],
    [
      "004c8dc8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c8dcc",
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

- 旧版 [`004a5f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5e90.md#insn-004a5f00) · [`004a5f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5e90.md#insn-004a5f40) · [`004a5eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5e90.md#insn-004a5eec)
- 新版 `004c8d98`（命令位置の公開資料なし） · `004c8dd8`（命令位置の公開資料なし） · `004c8d84`（命令位置の公開資料なし）

~~~diff
- 004a5f00 ["INT_ADD", "register:40f0:8", ["const:4a5f00:8", "const:4:8"]]
- 004a5f00 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c8d98 ["INT_ADD", "register:40f0:8", ["const:4c8d98:8", "const:4:8"]]
+ 004c8d98 ["CALL", null, ["callee:0043dd98:8"]]
- 004a5f00 bytes e6d4fd97
+ 004c8d98 bytes 00d4fd97
- 004a5f40 ["INT_ADD", "register:40f0:8", ["const:4a5f40:8", "const:4:8"]]
- 004a5f40 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c8dd8 ["INT_ADD", "register:40f0:8", ["const:4c8dd8:8", "const:4:8"]]
+ 004c8dd8 ["CALL", null, ["callee:00c57b10:8"]]
- 004a5f40 bytes 60d41c94
+ 004c8dd8 bytes 4e3b1e94
- 004a5eec ["INT_ADD", "register:40f0:8", ["const:4a5eec:8", "const:4:8"]]
- 004a5eec ["CALL", null, ["callee:00c57af0:8"]]
+ 004c8d84 ["INT_ADD", "register:40f0:8", ["const:4c8d84:8", "const:4:8"]]
+ 004c8d84 ["CALL", null, ["callee:00c57af0:8"]]
- 004a5eec bytes 6dd41c94
+ 004c8d84 bytes 5b3b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cdde95b0322a5a87004d1988847ae66"></a>

### [`004a5f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5f94.md) → [`004c8e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8e2c.md) _ZN5Botan4Pipe7prependEPNS_6FilterE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 94.96% / 新版 94.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004c8e68",
      "incomplete_value": true,
      "site": "004c8e6c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "004a5fd0",
      "incomplete_value": true,
      "site": "004a5fd4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c8ef8",
      "incomplete_value": false,
      "site": "004c8f00",
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
            "const:13:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6060",
      "incomplete_value": false,
      "site": "004a6068",
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
            "const:5e5:8"
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
      "definition_site": "004c8f34",
      "incomplete_value": true,
      "site": "004c8f40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a609c",
      "incomplete_value": true,
      "site": "004a60a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c8e5c",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ],
    [
      "004c8ef8",
      "PARAM",
      [
        "storage",
        "002a55e5",
        null,
        "string"
      ]
    ],
    [
      "004c8f30",
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
      "004c8e5c",
      "READ",
      [
        "storage",
        "00c9ab08",
        null,
        "pointer"
      ]
    ],
    [
      "004c8ef8",
      "PARAM",
      [
        "storage",
        "002b6013",
        null,
        "string"
      ]
    ],
    [
      "004c8f30",
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

- 旧版 [`004a6068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5f94.md#insn-004a6068) · [`004a60a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5f94.md#insn-004a60a8) · [`004a60cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5f94.md#insn-004a60cc)
- 新版 `004c8f00`（命令位置の公開資料なし） · `004c8f40`（命令位置の公開資料なし） · `004c8f64`（命令位置の公開資料なし）

~~~diff
- 004a6068 ["INT_ADD", "register:40f0:8", ["const:4a6068:8", "const:4:8"]]
- 004a6068 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c8f00 ["INT_ADD", "register:40f0:8", ["const:4c8f00:8", "const:4:8"]]
+ 004c8f00 ["CALL", null, ["callee:0043dd98:8"]]
- 004a6068 bytes 8cd4fd97
+ 004c8f00 bytes a6d3fd97
- 004a60a8 ["INT_ADD", "register:40f0:8", ["const:4a60a8:8", "const:4:8"]]
- 004a60a8 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c8f40 ["INT_ADD", "register:40f0:8", ["const:4c8f40:8", "const:4:8"]]
+ 004c8f40 ["CALL", null, ["callee:00c57b10:8"]]
- 004a60a8 bytes 06d41c94
+ 004c8f40 bytes f43a1e94
- 004a60cc ["INT_ADD", "register:40f0:8", ["const:4a60cc:8", "const:4:8"]]
- 004a60cc ["CALL", null, ["callee:0043dd98:8"]]
+ 004c8f64 ["INT_ADD", "register:40f0:8", ["const:4c8f64:8", "const:4:8"]]
+ 004c8f64 ["CALL", null, ["callee:0043dd98:8"]]
- 004a60cc bytes 73d4fd97
+ 004c8f64 bytes 8dd3fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed0c018103d74bd74c36e2b87a1a0796"></a>

### [`004a61cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a61cc.md) → [`004c9064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9064.md) _ZN5Botan4Pipe3popEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

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
      "definition_site": "004c9110",
      "incomplete_value": false,
      "site": "004c9118",
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
            "const:44a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6278",
      "incomplete_value": false,
      "site": "004a6280",
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
            "const:a11:8"
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
      "definition_site": "004c914c",
      "incomplete_value": true,
      "site": "004c9158",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a62b4",
      "incomplete_value": true,
      "site": "004a62c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c9148",
      "incomplete_value": false,
      "site": "004c9158",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a62b0",
      "incomplete_value": false,
      "site": "004a62c0",
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
      "004c9110",
      "PARAM",
      [
        "storage",
        "00295a11",
        null,
        "string"
      ]
    ],
    [
      "004c9148",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c914c",
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
      "004c9110",
      "PARAM",
      [
        "storage",
        "002a544a",
        null,
        "string"
      ]
    ],
    [
      "004c9148",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c914c",
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

- 旧版 [`004a6280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a61cc.md#insn-004a6280) · [`004a62c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a61cc.md#insn-004a62c0) · [`004a62e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a61cc.md#insn-004a62e4)
- 新版 `004c9118`（命令位置の公開資料なし） · `004c9158`（命令位置の公開資料なし） · `004c917c`（命令位置の公開資料なし）

~~~diff
- 004a6280 ["INT_ADD", "register:40f0:8", ["const:4a6280:8", "const:4:8"]]
- 004a6280 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c9118 ["INT_ADD", "register:40f0:8", ["const:4c9118:8", "const:4:8"]]
+ 004c9118 ["CALL", null, ["callee:0043dd98:8"]]
- 004a6280 bytes 06d4fd97
+ 004c9118 bytes 20d3fd97
- 004a62c0 ["INT_ADD", "register:40f0:8", ["const:4a62c0:8", "const:4:8"]]
- 004a62c0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c9158 ["INT_ADD", "register:40f0:8", ["const:4c9158:8", "const:4:8"]]
+ 004c9158 ["CALL", null, ["callee:00c57b10:8"]]
- 004a62c0 bytes 80d31c94
+ 004c9158 bytes 6e3a1e94
- 004a62e4 ["INT_ADD", "register:40f0:8", ["const:4a62e4:8", "const:4:8"]]
- 004a62e4 ["CALL", null, ["callee:0043dd98:8"]]
+ 004c917c ["INT_ADD", "register:40f0:8", ["const:4c917c:8", "const:4:8"]]
+ 004c917c ["CALL", null, ["callee:0043dd98:8"]]
- 004a62e4 bytes edd3fd97
+ 004c917c bytes 07d3fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e1e0f73f620b0d1dd6284847aef0870"></a>

### [`004a6378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6378.md) → [`004c9210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9210.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERNS_4PipeE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c92e8",
      "incomplete_value": true,
      "site": "004c92e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a6450",
      "incomplete_value": true,
      "site": "004a6450",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c9328",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a6490",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9348",
      "incomplete_value": true,
      "site": "004c9350",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a64b0",
      "incomplete_value": true,
      "site": "004a64b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c92d8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c9328",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "004c9348",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c92d8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004c9328",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "004c9348",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6378.md#insn-004a6450) · [`004a6490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6378.md#insn-004a6490) · [`004a64b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6378.md#insn-004a64b8)
- 新版 `004c92e8`（命令位置の公開資料なし） · `004c9328`（命令位置の公開資料なし） · `004c9350`（命令位置の公開資料なし）

~~~diff
- 004a6450 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a6450 ["INT_ADD", "register:40f0:8", ["const:4a6450:8", "const:4:8"]]
- 004a6450 ["CALLIND", null, ["register:0:8"]]
+ 004c92e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c92e8 ["INT_ADD", "register:40f0:8", ["const:4c92e8:8", "const:4:8"]]
+ 004c92e8 ["CALLIND", null, ["register:0:8"]]
- 004a6450 bytes 20013fd6
+ 004c92e8 bytes 20013fd6
- 004a6490 ["INT_ADD", "register:40f0:8", ["const:4a6490:8", "const:4:8"]]
- 004a6490 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004c9328 ["INT_ADD", "register:40f0:8", ["const:4c9328:8", "const:4:8"]]
+ 004c9328 ["CALL", null, ["ram:c58640:8"]]
- 004a6490 bytes d8d51c94
+ 004c9328 bytes c63c1e94
- 004a64b8 ["INT_ADD", "register:40f0:8", ["const:4a64b8:8", "const:4:8"]]
- 004a64b8 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c9350 ["INT_ADD", "register:40f0:8", ["const:4c9350:8", "const:4:8"]]
+ 004c9350 ["CALL", null, ["callee:00c57b10:8"]]
- 004a64b8 bytes 02d31c94
+ 004c9350 bytes f0391e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c417f8d6a3530dc2dfa5bbcc516f9700"></a>

### [`004a6590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6590.md) → [`004c9428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9428.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_4PipeE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.90% / 新版 94.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c94e8",
      "incomplete_value": true,
      "site": "004c94e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a6650",
      "incomplete_value": true,
      "site": "004a6650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "site": "004c9528",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a6690",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9548",
      "incomplete_value": true,
      "site": "004c9550",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a66b0",
      "incomplete_value": true,
      "site": "004a66b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c94d8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c9528",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "004c9548",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c94d8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004c9528",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "004c9548",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6590.md#insn-004a6650) · [`004a6690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6590.md#insn-004a6690) · [`004a66b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6590.md#insn-004a66b8)
- 新版 `004c94e8`（命令位置の公開資料なし） · `004c9528`（命令位置の公開資料なし） · `004c9550`（命令位置の公開資料なし）

~~~diff
- 004a6650 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a6650 ["INT_ADD", "register:40f0:8", ["const:4a6650:8", "const:4:8"]]
- 004a6650 ["CALLIND", null, ["register:0:8"]]
+ 004c94e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c94e8 ["INT_ADD", "register:40f0:8", ["const:4c94e8:8", "const:4:8"]]
+ 004c94e8 ["CALLIND", null, ["register:0:8"]]
- 004a6650 bytes 20013fd6
+ 004c94e8 bytes 20013fd6
- 004a6690 ["INT_ADD", "register:40f0:8", ["const:4a6690:8", "const:4:8"]]
- 004a6690 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004c9528 ["INT_ADD", "register:40f0:8", ["const:4c9528:8", "const:4:8"]]
+ 004c9528 ["CALL", null, ["ram:c58640:8"]]
- 004a6690 bytes 58d51c94
+ 004c9528 bytes 463c1e94
- 004a66b8 ["INT_ADD", "register:40f0:8", ["const:4a66b8:8", "const:4:8"]]
- 004a66b8 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c9550 ["INT_ADD", "register:40f0:8", ["const:4c9550:8", "const:4:8"]]
+ 004c9550 ["CALL", null, ["callee:00c57b10:8"]]
- 004a66b8 bytes 82d21c94
+ 004c9550 bytes 70391e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d1b8714e9ba367b6d09b4636ef8b17c"></a>

### [`004a6788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6788.md) → [`004c9620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9620.md) _ZNK5Botan4Pipe14get_message_noERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004a6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004c96cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

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
      "definition_site": "004c96ac",
      "incomplete_value": true,
      "site": "004c96b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6814",
      "incomplete_value": true,
      "site": "004a681c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:120:8"
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
      "definition_site": "004c96a8",
      "incomplete_value": false,
      "site": "004c96b4",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a6810",
      "incomplete_value": false,
      "site": "004a681c",
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
      "004c96a8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c96ac",
      "READ",
      [
        "storage",
        "00c1b120",
        null,
        "pointer"
      ]
    ],
    [
      "004c96ac",
      "PARAM",
      [
        "storage",
        "00be9bd8",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c96a8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c96ac",
      "READ",
      [
        "storage",
        "00c9ab10",
        null,
        "pointer"
      ]
    ],
    [
      "004c96ac",
      "PARAM",
      [
        "storage",
        "00c66798",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6788.md#insn-004a681c) · [`004a67f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6788.md#insn-004a67f4) · [`004a6804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6788.md#insn-004a6804)
- 新版 `004c96b4`（命令位置の公開資料なし） · `004c968c`（命令位置の公開資料なし） · `004c969c`（命令位置の公開資料なし）

~~~diff
- 004a681c ["INT_ADD", "register:40f0:8", ["const:4a681c:8", "const:4:8"]]
- 004a681c ["CALL", null, ["callee:00c57b10:8"]]
+ 004c96b4 ["INT_ADD", "register:40f0:8", ["const:4c96b4:8", "const:4:8"]]
+ 004c96b4 ["CALL", null, ["callee:00c57b10:8"]]
- 004a681c bytes 29d21c94
+ 004c96b4 bytes 17391e94
- 004a67f4 ["INT_ADD", "register:40f0:8", ["const:4a67f4:8", "const:4:8"]]
- 004a67f4 ["CALL", null, ["callee:00c57af0:8"]]
+ 004c968c ["INT_ADD", "register:40f0:8", ["const:4c968c:8", "const:4:8"]]
+ 004c968c ["CALL", null, ["callee:00c57af0:8"]]
- 004a67f4 bytes 2bd21c94
+ 004c968c bytes 19391e94
- 004a6804 ["INT_ADD", "register:40f0:8", ["const:4a6804:8", "const:4:8"]]
- 004a6804 ["CALL", null, ["callee:004c96cc:8"]]
+ 004c969c ["INT_ADD", "register:40f0:8", ["const:4c969c:8", "const:4:8"]]
+ 004c969c ["CALL", null, ["callee:004c96cc:8"]]
- 004a6804 bytes 0c000094
+ 004c969c bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c5cbe3b2cd1b3fa538f718ff96bb5b0"></a>

### [`004a6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md) → [`004c96cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md) FUN_004c96cc

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`004a53c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a53c0.md) [`004a6788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6788.md) [`004a6aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6aa8.md) [`004a6e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6e24.md) · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)
- 新版 呼出元 4件 [`004c8258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8258.md) [`004c9620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9620.md) [`004c9940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9940.md) [`004c9cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9cbc.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c9794",
      "incomplete_value": true,
      "site": "004c9798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a68fc",
      "incomplete_value": true,
      "site": "004a6900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c97c8",
      "incomplete_value": true,
      "site": "004c97cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a6930",
      "incomplete_value": true,
      "site": "004a6934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c96ec",
      "incomplete_value": false,
      "site": "004c9700",
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
            "const:9c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6854",
      "incomplete_value": false,
      "site": "004a6868",
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
            "const:949:8"
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
      "004c96ec",
      "PARAM",
      [
        "storage",
        "002ac949",
        null,
        "string"
      ]
    ],
    [
      "004c9708",
      "PARAM",
      [
        "storage",
        "002aa6ec",
        null,
        "string"
      ]
    ],
    [
      "004c9778",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c96ec",
      "PARAM",
      [
        "storage",
        "002bd9c1",
        null,
        "string"
      ]
    ],
    [
      "004c9708",
      "PARAM",
      [
        "storage",
        "002bb468",
        null,
        "string"
      ]
    ],
    [
      "004c9778",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md#insn-004a6868) · [`004a6878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md#insn-004a6878) · [`004a68ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md#insn-004a68ec)
- 新版 `004c9700`（命令位置の公開資料なし） · `004c9710`（命令位置の公開資料なし） · `004c9784`（命令位置の公開資料なし）

~~~diff
- 004a6868 ["INT_ADD", "register:40f0:8", ["const:4a6868:8", "const:4:8"]]
- 004a6868 ["CALL", null, ["callee:00c57cb0:8"]]
+ 004c9700 ["INT_ADD", "register:40f0:8", ["const:4c9700:8", "const:4:8"]]
+ 004c9700 ["CALL", null, ["callee:00c57cb0:8"]]
- 004a6868 bytes 7ed21c94
+ 004c9700 bytes 6c391e94
- 004a6878 ["INT_ADD", "register:40f0:8", ["const:4a6878:8", "const:4:8"]]
- 004a6878 ["CALL", null, ["callee:00c57b70:8"]]
+ 004c9710 ["INT_ADD", "register:40f0:8", ["const:4c9710:8", "const:4:8"]]
+ 004c9710 ["CALL", null, ["callee:00c57b70:8"]]
- 004a6878 bytes 2ad21c94
+ 004c9710 bytes 18391e94
- 004a68ec ["INT_ADD", "register:40f0:8", ["const:4a68ec:8", "const:4:8"]]
- 004a68ec ["CALL", null, ["ram:bdb930:8"]]
+ 004c9784 ["INT_ADD", "register:40f0:8", ["const:4c9784:8", "const:4:8"]]
+ 004c9784 ["CALL", null, ["ram:c58380:8"]]
- 004a68ec bytes 11d41c94
+ 004c9784 bytes ff3a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc817957a85d8459020544f6ec9610a6"></a>

### [`004a6aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6aa8.md) → [`004c9940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9940.md) _ZN5Botan4Pipe4readEPhmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc270.md) · 呼出先 6件 [`004a6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58cc0.md) · 呼出先 6件 [`004c96cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

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
      "definition_site": "004c9a44",
      "incomplete_value": true,
      "site": "004c9a4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6bac",
      "incomplete_value": true,
      "site": "004a6bb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:120:8"
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
      "definition_site": "004c9a40",
      "incomplete_value": false,
      "site": "004c9a4c",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a6ba8",
      "incomplete_value": false,
      "site": "004a6bb4",
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
      "004c9a40",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c9a44",
      "READ",
      [
        "storage",
        "00c1b120",
        null,
        "pointer"
      ]
    ],
    [
      "004c9a44",
      "PARAM",
      [
        "storage",
        "00be9bd8",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9a40",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c9a44",
      "READ",
      [
        "storage",
        "00c9ab10",
        null,
        "pointer"
      ]
    ],
    [
      "004c9a44",
      "PARAM",
      [
        "storage",
        "00c66798",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6aa8.md#insn-004a6bb4) · [`004a6b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6aa8.md#insn-004a6b4c) · [`004a6b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6aa8.md#insn-004a6b7c)
- 新版 `004c9a4c`（命令位置の公開資料なし） · `004c99e4`（命令位置の公開資料なし） · `004c9a14`（命令位置の公開資料なし）

~~~diff
- 004a6bb4 ["INT_ADD", "register:40f0:8", ["const:4a6bb4:8", "const:4:8"]]
- 004a6bb4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c9a4c ["INT_ADD", "register:40f0:8", ["const:4c9a4c:8", "const:4:8"]]
+ 004c9a4c ["CALL", null, ["callee:00c57b10:8"]]
- 004a6bb4 bytes 43d11c94
+ 004c9a4c bytes 31381e94
- 004a6b4c ["INT_ADD", "register:40f0:8", ["const:4a6b4c:8", "const:4:8"]]
- 004a6b4c ["CALL", null, ["callee:00c58bf0:8"]]
+ 004c99e4 ["INT_ADD", "register:40f0:8", ["const:4c99e4:8", "const:4:8"]]
+ 004c99e4 ["CALL", null, ["callee:00c58bf0:8"]]
- 004a6b4c bytes 95d51c94
+ 004c99e4 bytes 833c1e94
- 004a6b7c ["INT_ADD", "register:40f0:8", ["const:4a6b7c:8", "const:4:8"]]
- 004a6b7c ["CALL", null, ["callee:00c57af0:8"]]
+ 004c9a14 ["INT_ADD", "register:40f0:8", ["const:4c9a14:8", "const:4:8"]]
+ 004c9a14 ["CALL", null, ["callee:00c57af0:8"]]
- 004a6b7c bytes 49d11c94
+ 004c9a14 bytes 37381e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67d3bad20ca787acbec335a513a3c727"></a>

### [`004a6c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6c9c.md) → [`004c9b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9b34.md) _ZN5Botan4Pipe18read_all_as_stringEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c9c04",
      "incomplete_value": true,
      "site": "004c9c04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a6d6c",
      "incomplete_value": true,
      "site": "004a6d6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004c9c40",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a6da8",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9c60",
      "incomplete_value": true,
      "site": "004c9c68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a6dc8",
      "incomplete_value": true,
      "site": "004a6dd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c9bf0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004c9c40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "004c9c60",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c9bf0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004c9c40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "004c9c60",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6c9c.md#insn-004a6d6c) · [`004a6da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6c9c.md#insn-004a6da8) · [`004a6dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6c9c.md#insn-004a6dd0)
- 新版 `004c9c04`（命令位置の公開資料なし） · `004c9c40`（命令位置の公開資料なし） · `004c9c68`（命令位置の公開資料なし）

~~~diff
- 004a6d6c ["COPY", "register:0:8", ["register:4048:8"]]
- 004a6d6c ["INT_ADD", "register:40f0:8", ["const:4a6d6c:8", "const:4:8"]]
- 004a6d6c ["CALLIND", null, ["register:0:8"]]
+ 004c9c04 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c9c04 ["INT_ADD", "register:40f0:8", ["const:4c9c04:8", "const:4:8"]]
+ 004c9c04 ["CALLIND", null, ["register:0:8"]]
- 004a6d6c bytes 20013fd6
+ 004c9c04 bytes 20013fd6
- 004a6da8 ["INT_ADD", "register:40f0:8", ["const:4a6da8:8", "const:4:8"]]
- 004a6da8 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004c9c40 ["INT_ADD", "register:40f0:8", ["const:4c9c40:8", "const:4:8"]]
+ 004c9c40 ["CALL", null, ["ram:c58640:8"]]
- 004a6da8 bytes 92d31c94
+ 004c9c40 bytes 803a1e94
- 004a6dd0 ["INT_ADD", "register:40f0:8", ["const:4a6dd0:8", "const:4:8"]]
- 004a6dd0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c9c68 ["INT_ADD", "register:40f0:8", ["const:4c9c68:8", "const:4:8"]]
+ 004c9c68 ["CALL", null, ["callee:00c57b10:8"]]
- 004a6dd0 bytes bcd01c94
+ 004c9c68 bytes aa371e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a99d6c48cb787a154e3ff5dcaa88eda"></a>

### [`004a6e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6e24.md) → [`004c9cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9cbc.md) _ZNK5Botan4Pipe4peekEPhmmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc290.md) · 呼出先 6件 [`004a6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6834.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ce0.md) · 呼出先 6件 [`004c96cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.67% / 新版 98.67%

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
      "definition_site": "004c9dd8",
      "incomplete_value": true,
      "site": "004c9de0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6f40",
      "incomplete_value": true,
      "site": "004a6f48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:120:8"
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
      "definition_site": "004c9dd4",
      "incomplete_value": false,
      "site": "004c9de0",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a6f3c",
      "incomplete_value": false,
      "site": "004a6f48",
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
      "004c9dd4",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004c9dd8",
      "READ",
      [
        "storage",
        "00c1b120",
        null,
        "pointer"
      ]
    ],
    [
      "004c9dd8",
      "PARAM",
      [
        "storage",
        "00be9bd8",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9dd4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c9dd8",
      "READ",
      [
        "storage",
        "00c9ab10",
        null,
        "pointer"
      ]
    ],
    [
      "004c9dd8",
      "PARAM",
      [
        "storage",
        "00c66798",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6e24.md#insn-004a6f48) · [`004a6f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6e24.md#insn-004a6f0c) · [`004a6f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6e24.md#insn-004a6f1c)
- 新版 `004c9de0`（命令位置の公開資料なし） · `004c9da4`（命令位置の公開資料なし） · `004c9db4`（命令位置の公開資料なし）

~~~diff
- 004a6f48 ["INT_ADD", "register:40f0:8", ["const:4a6f48:8", "const:4:8"]]
- 004a6f48 ["CALL", null, ["callee:00c57b10:8"]]
+ 004c9de0 ["INT_ADD", "register:40f0:8", ["const:4c9de0:8", "const:4:8"]]
+ 004c9de0 ["CALL", null, ["callee:00c57b10:8"]]
- 004a6f48 bytes 5ed01c94
+ 004c9de0 bytes 4c371e94
- 004a6f0c ["INT_ADD", "register:40f0:8", ["const:4a6f0c:8", "const:4:8"]]
- 004a6f0c ["CALL", null, ["callee:00c57af0:8"]]
+ 004c9da4 ["INT_ADD", "register:40f0:8", ["const:4c9da4:8", "const:4:8"]]
+ 004c9da4 ["CALL", null, ["callee:00c57af0:8"]]
- 004a6f0c bytes 65d01c94
+ 004c9da4 bytes 53371e94
- 004a6f1c ["INT_ADD", "register:40f0:8", ["const:4a6f1c:8", "const:4:8"]]
- 004a6f1c ["CALL", null, ["callee:004c96cc:8"]]
+ 004c9db4 ["INT_ADD", "register:40f0:8", ["const:4c9db4:8", "const:4:8"]]
+ 004c9db4 ["CALL", null, ["callee:004c96cc:8"]]
- 004a6f1c bytes 46feff97
+ 004c9db4 bytes 46feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c757397933230adfb1a4da2caa8524b"></a>

### [`004a6fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6fa8.md) → [`004c9e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9e40.md) _ZNK5Botan4Pipe14get_bytes_readEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9ea0",
      "incomplete_value": false,
      "site": "004c9ec0",
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
            "const:2bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7008",
      "incomplete_value": false,
      "site": "004a7028",
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
            "const:7cc:8"
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
      "definition_site": "004c9ea8",
      "incomplete_value": false,
      "site": "004c9ec0",
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
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7010",
      "incomplete_value": false,
      "site": "004a7028",
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
            "const:5e4:8"
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
      "definition_site": "004c9eb0",
      "incomplete_value": false,
      "site": "004c9ec0",
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
            "const:af4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7018",
      "incomplete_value": false,
      "site": "004a7028",
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
            "const:c1b:8"
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
      "004c9ea0",
      "PARAM",
      [
        "storage",
        "002a67cc",
        null,
        "string"
      ]
    ],
    [
      "004c9ea8",
      "PARAM",
      [
        "storage",
        "002aa5e4",
        null,
        "string"
      ]
    ],
    [
      "004c9eb0",
      "PARAM",
      [
        "storage",
        "00299c1b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c9ea0",
      "PARAM",
      [
        "storage",
        "002b72bd",
        null,
        "string"
      ]
    ],
    [
      "004c9ea8",
      "PARAM",
      [
        "storage",
        "002bb360",
        null,
        "string"
      ]
    ],
    [
      "004c9eb0",
      "PARAM",
      [
        "storage",
        "002a9af4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6fa8.md#insn-004a7028) · [`004a7004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6fa8.md#insn-004a7004) · [`004a7008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6fa8.md#insn-004a7008)
- 新版 `004c9ec0`（命令位置の公開資料なし） · `004c9e9c`（命令位置の公開資料なし） · `004c9ea0`（命令位置の公開資料なし）

~~~diff
- 004a7028 ["INT_ADD", "register:40f0:8", ["const:4a7028:8", "const:4:8"]]
- 004a7028 ["CALL", null, ["callee:00c58250:8"]]
+ 004c9ec0 ["INT_ADD", "register:40f0:8", ["const:4c9ec0:8", "const:4:8"]]
+ 004c9ec0 ["CALL", null, ["callee:00c58250:8"]]
- 004a7028 bytes f6d11c94
+ 004c9ec0 bytes e4381e94
- 004a7004 ["COPY", "register:4000:8", ["const:2a6000:8"]]
+ 004c9e9c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 004a7004 bytes e0effff0
+ 004c9e9c bytes 60efffd0
- 004a7008 ["COPY", "tmp:0:8", ["const:7cc:8"]]
- 004a7008 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a7008 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a7008 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c9ea0 ["COPY", "tmp:0:8", ["const:2bd:8"]]
+ 004c9ea0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c9ea0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c9ea0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a7008 bytes 00301f91
+ 004c9ea0 bytes 00f40a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1f308da76b16533458413ec525ab738"></a>

### [`004a702c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a702c.md) → [`004c9ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9ec4.md) _ZNK5Botan4Pipe14get_bytes_readEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9f24",
      "incomplete_value": false,
      "site": "004c9f44",
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
            "const:2bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a708c",
      "incomplete_value": false,
      "site": "004a70ac",
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
            "const:7cc:8"
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
      "definition_site": "004c9f2c",
      "incomplete_value": false,
      "site": "004c9f44",
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
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7094",
      "incomplete_value": false,
      "site": "004a70ac",
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
            "const:5e4:8"
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
      "definition_site": "004c9f34",
      "incomplete_value": false,
      "site": "004c9f44",
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
            "const:af4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a709c",
      "incomplete_value": false,
      "site": "004a70ac",
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
            "const:c1b:8"
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
      "004c9f24",
      "PARAM",
      [
        "storage",
        "002a67cc",
        null,
        "string"
      ]
    ],
    [
      "004c9f2c",
      "PARAM",
      [
        "storage",
        "002aa5e4",
        null,
        "string"
      ]
    ],
    [
      "004c9f34",
      "PARAM",
      [
        "storage",
        "00299c1b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c9f24",
      "PARAM",
      [
        "storage",
        "002b72bd",
        null,
        "string"
      ]
    ],
    [
      "004c9f2c",
      "PARAM",
      [
        "storage",
        "002bb360",
        null,
        "string"
      ]
    ],
    [
      "004c9f34",
      "PARAM",
      [
        "storage",
        "002a9af4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a70ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a702c.md#insn-004a70ac) · [`004a7088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a702c.md#insn-004a7088) · [`004a708c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a702c.md#insn-004a708c)
- 新版 `004c9f44`（命令位置の公開資料なし） · `004c9f20`（命令位置の公開資料なし） · `004c9f24`（命令位置の公開資料なし）

~~~diff
- 004a70ac ["INT_ADD", "register:40f0:8", ["const:4a70ac:8", "const:4:8"]]
- 004a70ac ["CALL", null, ["callee:00c58250:8"]]
+ 004c9f44 ["INT_ADD", "register:40f0:8", ["const:4c9f44:8", "const:4:8"]]
+ 004c9f44 ["CALL", null, ["callee:00c58250:8"]]
- 004a70ac bytes d5d11c94
+ 004c9f44 bytes c3381e94
- 004a7088 ["COPY", "register:4000:8", ["const:2a6000:8"]]
+ 004c9f20 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 004a7088 bytes e0effff0
+ 004c9f20 bytes 60efffd0
- 004a708c ["COPY", "tmp:0:8", ["const:7cc:8"]]
- 004a708c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a708c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a708c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c9f24 ["COPY", "tmp:0:8", ["const:2bd:8"]]
+ 004c9f24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c9f24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c9f24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a708c bytes 00301f91
+ 004c9f24 bytes 00f40a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b30572227ab4193dabcb6532728e75d5"></a>

### [`004a710c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a710c.md) → [`004c9fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9fa4.md) _ZN5Botan11SecureQueueC1Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc260.md) · 呼出先 8件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00c58cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58cb0.md) · 呼出先 8件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c9fd4",
      "incomplete_value": true,
      "site": "004c9fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a713c",
      "incomplete_value": true,
      "site": "004a7144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ca008",
      "incomplete_value": true,
      "site": "004ca010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a7170",
      "incomplete_value": true,
      "site": "004a7178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ca018",
      "incomplete_value": true,
      "site": "004ca018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7180",
      "incomplete_value": true,
      "site": "004a7180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:88:8"
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
      "004c9fc4",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004c9fdc",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c9ffc",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c9fc4",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c9fdc",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c9ffc",
      "READ",
      [
        "storage",
        "00c9ab08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a720c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a710c.md#insn-004a720c) · [`004a7224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a710c.md#insn-004a7224) · [`004a7120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a710c.md#insn-004a7120)
- 新版 `004ca0a4`（命令位置の公開資料なし） · `004ca0bc`（命令位置の公開資料なし） · `004c9fb8`（命令位置の公開資料なし）

~~~diff
- 004a720c ["INT_ADD", "register:40f0:8", ["const:4a720c:8", "const:4:8"]]
- 004a720c ["CALL", null, ["ram:bdbbf0:8"]]
+ 004ca0a4 ["INT_ADD", "register:40f0:8", ["const:4ca0a4:8", "const:4:8"]]
+ 004ca0a4 ["CALL", null, ["ram:c58640:8"]]
- 004a720c bytes 79d21c94
+ 004ca0a4 bytes 67391e94
- 004a7224 ["INT_ADD", "register:40f0:8", ["const:4a7224:8", "const:4:8"]]
- 004a7224 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ca0bc ["INT_ADD", "register:40f0:8", ["const:4ca0bc:8", "const:4:8"]]
+ 004ca0bc ["CALL", null, ["callee:00c57b10:8"]]
- 004a7224 bytes a7cf1c94
+ 004ca0bc bytes 95361e94
- 004a7120 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004c9fb8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a7120 bytes a83b0090
+ 004c9fb8 bytes 883e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b633e22ae1dea450e63ddadf823a5c6d"></a>

### [`004a728c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a728c.md) → [`004ca124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca124.md) _ZN5Botan11SecureQueueC2ERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ca164",
      "incomplete_value": true,
      "site": "004ca16c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a72cc",
      "incomplete_value": true,
      "site": "004a72d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ca194",
      "incomplete_value": true,
      "site": "004ca19c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a72fc",
      "incomplete_value": true,
      "site": "004a7304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ca1a4",
      "incomplete_value": true,
      "site": "004ca1a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a730c",
      "incomplete_value": true,
      "site": "004a730c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:88:8"
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
      "004ca158",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004ca16c",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ca188",
      "READ",
      [
        "storage",
        "00c1b118",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ca158",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004ca16c",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ca188",
      "READ",
      [
        "storage",
        "00c9ab08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a73c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a728c.md#insn-004a73c0) · [`004a73d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a728c.md#insn-004a73d8) · [`004a72bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a728c.md#insn-004a72bc)
- 新版 `004ca258`（命令位置の公開資料なし） · `004ca270`（命令位置の公開資料なし） · `004ca154`（命令位置の公開資料なし）

~~~diff
- 004a73c0 ["INT_ADD", "register:40f0:8", ["const:4a73c0:8", "const:4:8"]]
- 004a73c0 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004ca258 ["INT_ADD", "register:40f0:8", ["const:4ca258:8", "const:4:8"]]
+ 004ca258 ["CALL", null, ["ram:c58640:8"]]
- 004a73c0 bytes 0cd21c94
+ 004ca258 bytes fa381e94
- 004a73d8 ["INT_ADD", "register:40f0:8", ["const:4a73d8:8", "const:4:8"]]
- 004a73d8 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ca270 ["INT_ADD", "register:40f0:8", ["const:4ca270:8", "const:4:8"]]
+ 004ca270 ["CALL", null, ["callee:00c57b10:8"]]
- 004a73d8 bytes 3acf1c94
+ 004ca270 bytes 28361e94
- 004a72bc ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004ca154 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a72bc bytes a83b0090
+ 004ca154 bytes 883e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a2757db9744c042ef00902d7ad225a6"></a>

### [`004a7444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7444.md) → [`004ca2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca2dc.md) _ZN5Botan11SecureQueue5writeEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2a0.md) · 呼出先 8件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c58cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58cf0.md) · 呼出先 8件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ca444",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a75ac",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ca454",
      "incomplete_value": true,
      "site": "004ca45c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a75bc",
      "incomplete_value": true,
      "site": "004a75c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ca458",
      "incomplete_value": true,
      "site": "004ca45c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a75c0",
      "incomplete_value": true,
      "site": "004a75c4",
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
      "004ca444",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "004ca454",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004ca454",
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
      "004ca444",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "004ca454",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004ca454",
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

- 旧版 [`004a75ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7444.md#insn-004a75ac) · [`004a75c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7444.md#insn-004a75c4) · [`004a75e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7444.md#insn-004a75e4)
- 新版 `004ca444`（命令位置の公開資料なし） · `004ca45c`（命令位置の公開資料なし） · `004ca47c`（命令位置の公開資料なし）

~~~diff
- 004a75ac ["INT_ADD", "register:40f0:8", ["const:4a75ac:8", "const:4:8"]]
- 004a75ac ["CALL", null, ["ram:bdbbf0:8"]]
+ 004ca444 ["INT_ADD", "register:40f0:8", ["const:4ca444:8", "const:4:8"]]
+ 004ca444 ["CALL", null, ["ram:c58640:8"]]
- 004a75ac bytes 91d11c94
+ 004ca444 bytes 7f381e94
- 004a75c4 ["INT_ADD", "register:40f0:8", ["const:4a75c4:8", "const:4:8"]]
- 004a75c4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ca45c ["INT_ADD", "register:40f0:8", ["const:4ca45c:8", "const:4:8"]]
+ 004ca45c ["CALL", null, ["callee:00c57b10:8"]]
- 004a75c4 bytes bfce1c94
+ 004ca45c bytes ad351e94
- 004a75e4 ["INT_ADD", "register:40f0:8", ["const:4a75e4:8", "const:4:8"]]
- 004a75e4 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004ca47c ["INT_ADD", "register:40f0:8", ["const:4ca47c:8", "const:4:8"]]
+ 004ca47c ["CALL", null, ["ram:c58640:8"]]
- 004a75e4 bytes 83d11c94
+ 004ca47c bytes 71381e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca8914e6af6fd939ba933f097fea934e"></a>

### [`004a7634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7634.md) → [`004ca4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca4cc.md) _ZN5Botan11SecureQueue7destroyEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

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
      "definition_site": "004ca52c",
      "incomplete_value": true,
      "site": "004ca52c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004a7694",
      "incomplete_value": true,
      "site": "004a7694",
      "value": [
        "LOAD",
        "8",
        [
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
      "004ca51c",
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
      "004ca51c",
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

- 旧版 [`004a7694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7634.md#insn-004a7694) · [`004a7654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7634.md#insn-004a7654) · [`004a7660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7634.md#insn-004a7660)
- 新版 `004ca52c`（命令位置の公開資料なし） · `004ca4ec`（命令位置の公開資料なし） · `004ca4f8`（命令位置の公開資料なし）

~~~diff
- 004a7694 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a7694 ["INT_ADD", "register:40f0:8", ["const:4a7694:8", "const:4:8"]]
- 004a7694 ["CALLIND", null, ["register:0:8"]]
+ 004ca52c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ca52c ["INT_ADD", "register:40f0:8", ["const:4ca52c:8", "const:4:8"]]
+ 004ca52c ["CALLIND", null, ["register:0:8"]]
- 004a7694 bytes 20013fd6
+ 004ca52c bytes 20013fd6
- 004a7654 ["COPY", "register:40b0:8", ["const:bea000:8"]]
+ 004ca4ec ["COPY", "register:40b0:8", ["const:c67000:8"]]
- 004a7654 bytes 163a00f0
+ 004ca4ec bytes f63c00b0
- 004a7660 ["INT_ADD", "register:40f0:8", ["const:4a7660:8", "const:4:8"]]
- 004a7660 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004ca4f8 ["INT_ADD", "register:40f0:8", ["const:4ca4f8:8", "const:4:8"]]
+ 004ca4f8 ["CALL", null, ["callee:00c57ab0:8"]]
- 004a7660 bytes 80ce1c94
+ 004ca4f8 bytes 6e351e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-971cd29982d38c3545d387d481804e64"></a>

### [`004a76c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a76c0.md) → [`004ca558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca558.md) _ZN5Botan11SecureQueueaSERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.68% / 新版 94.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ca5dc",
      "incomplete_value": true,
      "site": "004ca5dc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004a7744",
      "incomplete_value": true,
      "site": "004a7744",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004ca6b0",
      "value": [
        "leaf",
        "ram:c58640:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a7818",
      "value": [
        "leaf",
        "ram:bdbbf0:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ca6c0",
      "incomplete_value": true,
      "site": "004ca6c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a7828",
      "incomplete_value": true,
      "site": "004a7830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ca5cc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004ca6b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdbbf0"
      ]
    ],
    [
      "004ca6c0",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ca5cc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ca6b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c58640"
      ]
    ],
    [
      "004ca6c0",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a76c0.md#insn-004a7744) · [`004a7818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a76c0.md#insn-004a7818) · [`004a7830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a76c0.md#insn-004a7830)
- 新版 `004ca5dc`（命令位置の公開資料なし） · `004ca6b0`（命令位置の公開資料なし） · `004ca6c8`（命令位置の公開資料なし）

~~~diff
- 004a7744 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a7744 ["INT_ADD", "register:40f0:8", ["const:4a7744:8", "const:4:8"]]
- 004a7744 ["CALLIND", null, ["register:0:8"]]
+ 004ca5dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ca5dc ["INT_ADD", "register:40f0:8", ["const:4ca5dc:8", "const:4:8"]]
+ 004ca5dc ["CALLIND", null, ["register:0:8"]]
- 004a7744 bytes 20013fd6
+ 004ca5dc bytes 20013fd6
- 004a7818 ["INT_ADD", "register:40f0:8", ["const:4a7818:8", "const:4:8"]]
- 004a7818 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004ca6b0 ["INT_ADD", "register:40f0:8", ["const:4ca6b0:8", "const:4:8"]]
+ 004ca6b0 ["CALL", null, ["ram:c58640:8"]]
- 004a7818 bytes f6d01c94
+ 004ca6b0 bytes e4371e94
- 004a7830 ["INT_ADD", "register:40f0:8", ["const:4a7830:8", "const:4:8"]]
- 004a7830 ["CALL", null, ["callee:00c57b10:8"]]
+ 004ca6c8 ["INT_ADD", "register:40f0:8", ["const:4ca6c8:8", "const:4:8"]]
+ 004ca6c8 ["CALL", null, ["callee:00c57b10:8"]]
- 004a7830 bytes 24ce1c94
+ 004ca6c8 bytes 12351e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b7065666d1ab50ed2b584c8d347066e"></a>

### [`004a791c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a791c.md) → [`004ca7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca7b4.md) _ZN5Botan13Threaded_ForkC2EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d00.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.14% / 新版 90.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ca7fc",
      "incomplete_value": true,
      "site": "004ca804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a7964",
      "incomplete_value": true,
      "site": "004a796c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ca83c",
      "incomplete_value": true,
      "site": "004ca844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a79a4",
      "incomplete_value": true,
      "site": "004a79ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ca7e0",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004ca804",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ca82c",
      "READ",
      [
        "storage",
        "00c1b130",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ca7e0",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004ca804",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ca82c",
      "READ",
      [
        "storage",
        "00c9ab20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a793c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a791c.md#insn-004a793c) · [`004a7948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a791c.md#insn-004a7948) · [`004a7968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a791c.md#insn-004a7968)
- 新版 `004ca7d4`（命令位置の公開資料なし） · `004ca7e0`（命令位置の公開資料なし）

~~~diff
- 004a793c ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 004ca7d4 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 004a793c bytes a93b0090
+ 004ca7d4 bytes 893e0090
- 004a7948 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
- 004a7948 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ca7e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
+ 004ca7e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a7948 bytes 294140f9
+ 004ca7e0 bytes 293945f9
- 004a7968 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 004a7968 bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a35a982575719945be3939ee3c7bd076"></a>

### [`004a7da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7da8.md) → [`004cac40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004cac40.md) _ZN5Botan13Threaded_ForkC2EPPNS_6FilterEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdc2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.68% / 新版 88.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cac6c",
      "incomplete_value": true,
      "site": "004cac70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a7dd4",
      "incomplete_value": true,
      "site": "004a7dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004caca8",
      "incomplete_value": true,
      "site": "004cacb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a7e10",
      "incomplete_value": true,
      "site": "004a7e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004cac5c",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "004cac70",
      "DATA",
      [
        "storage",
        "00be9a18",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004cac98",
      "READ",
      [
        "storage",
        "00c1b130",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004cac5c",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004cac70",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004cac98",
      "READ",
      [
        "storage",
        "00c9ab20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7da8.md#insn-004a7db8) · [`004a7dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7da8.md#insn-004a7dc4) · [`004a7df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7da8.md#insn-004a7df0)
- 新版 `004cac50`（命令位置の公開資料なし） · `004cac5c`（命令位置の公開資料なし） · `004cac88`（命令位置の公開資料なし）

~~~diff
- 004a7db8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 004cac50 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 004a7db8 bytes a83b0090
+ 004cac50 bytes 883e0090
- 004a7dc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 004a7dc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cac5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 004cac5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a7dc4 bytes 084140f9
+ 004cac5c bytes 083945f9
- 004a7df0 ["INT_ADD", "register:40f0:8", ["const:4a7df0:8", "const:4:8"]]
- 004a7df0 ["CALL", null, ["callee:00543c1c:8"]]
+ 004cac88 ["INT_ADD", "register:40f0:8", ["const:4cac88:8", "const:4:8"]]
+ 004cac88 ["CALL", null, ["callee:00543c1c:8"]]
- 004a7df0 bytes e5e30194
+ 004cac88 bytes e5e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c139f2ed16f8a3b74a6b2d832fd5dd21"></a>

### [`004a7ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7ed0.md) → [`004cad68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004cad68.md) _ZN5Botan13Threaded_ForkD1Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2d0.md) · 呼出先 11件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md)
- 新版 呼出元 1件 [`00c58d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d20.md) · 呼出先 11件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004caea8",
      "incomplete_value": true,
      "site": "004caeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8010",
      "incomplete_value": true,
      "site": "004a8014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004cae10",
      "value": [
        "leaf",
        "ram:c57cd0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a7f78",
      "value": [
        "leaf",
        "ram:bdb280:8"
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
      "site": "004cae20",
      "value": [
        "leaf",
        "ram:c57cd0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a7f88",
      "value": [
        "leaf",
        "ram:bdb280:8"
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
      "004cae10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb280"
      ]
    ],
    [
      "004cae20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb280"
      ]
    ],
    [
      "004caea0",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004cae10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57cd0"
      ]
    ],
    [
      "004cae20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57cd0"
      ]
    ],
    [
      "004caea0",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7ed0.md#insn-004a7f78) · [`004a7f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7ed0.md#insn-004a7f88) · [`004a8048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7ed0.md#insn-004a8048)
- 新版 `004cae10`（命令位置の公開資料なし） · `004cae20`（命令位置の公開資料なし） · `004caee0`（命令位置の公開資料なし）

~~~diff
- 004a7f78 ["INT_ADD", "register:40f0:8", ["const:4a7f78:8", "const:4:8"]]
- 004a7f78 ["CALL", null, ["ram:bdb280:8"]]
+ 004cae10 ["INT_ADD", "register:40f0:8", ["const:4cae10:8", "const:4:8"]]
+ 004cae10 ["CALL", null, ["ram:c57cd0:8"]]
- 004a7f78 bytes c2cc1c94
+ 004cae10 bytes b0331e94
- 004a7f88 ["INT_ADD", "register:40f0:8", ["const:4a7f88:8", "const:4:8"]]
- 004a7f88 ["CALL", null, ["ram:bdb280:8"]]
+ 004cae20 ["INT_ADD", "register:40f0:8", ["const:4cae20:8", "const:4:8"]]
+ 004cae20 ["CALL", null, ["ram:c57cd0:8"]]
- 004a7f88 bytes becc1c94
+ 004cae20 bytes ac331e94
- 004a8048 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a8048 ["INT_ADD", "register:40f0:8", ["const:4a8048:8", "const:4:8"]]
- 004a8048 ["CALLIND", null, ["register:0:8"]]
+ 004caee0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004caee0 ["INT_ADD", "register:40f0:8", ["const:4caee0:8", "const:4:8"]]
+ 004caee0 ["CALLIND", null, ["register:0:8"]]
- 004a8048 bytes 20013fd6
+ 004caee0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05058e62137b2ad8a536581de23f66ed"></a>

### [`004a80a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a80a0.md) → [`004caf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004caf38.md) _ZNK5Botan13Threaded_Fork4nameEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "004caf54",
      "incomplete_value": true,
      "site": "004caf54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:715:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a80bc",
      "incomplete_value": true,
      "site": "004a80bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:57c:8"
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
      "definition_site": "004caf58",
      "incomplete_value": true,
      "site": "004caf58",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a80c0",
      "incomplete_value": true,
      "site": "004a80c0",
      "value": [
        "LOAD",
        "8",
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
      "004caf44",
      "READ",
      [
        "storage",
        "0029c57c",
        null,
        "string"
      ]
    ],
    [
      "004caf4c",
      "READ",
      [
        "storage",
        "0029c581",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004caf44",
      "READ",
      [
        "storage",
        "002ac715",
        null,
        "string"
      ]
    ],
    [
      "004caf4c",
      "READ",
      [
        "storage",
        "002ac71a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a80a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a80a0.md#insn-004a80a4) · [`004a80a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a80a0.md#insn-004a80a8)
- 新版 `004caf3c`（命令位置の公開資料なし） · `004caf40`（命令位置の公開資料なし）

~~~diff
- 004a80a4 ["COPY", "register:4050:8", ["const:29c000:8"]]
+ 004caf3c ["COPY", "register:4050:8", ["const:2ac000:8"]]
- 004a80a4 bytes aaefff90
+ 004caf3c bytes 0aefffd0
- 004a80a8 ["COPY", "tmp:0:8", ["const:57c:8"]]
- 004a80a8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004a80a8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004a80a8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004caf40 ["COPY", "tmp:0:8", ["const:715:8"]]
+ 004caf40 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004caf40 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004caf40 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004a80a8 bytes 4af11591
+ 004caf40 bytes 4a551c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15b2523bc7e94f74781f72a89d1cbbe4"></a>

### [`004a832c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a832c.md) → [`004cb1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb1c4.md) FUN_004cb1c4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004a7a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7a98.md) · 呼出先 6件 [`00521aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521aec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) [`00bdb2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2c0.md)
- 新版 呼出元 1件 [`004ca930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca930.md) · 呼出先 6件 [`00544984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544984.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d00.md) [`00c57d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

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
      "definition_site": "004cb224",
      "incomplete_value": false,
      "site": "004cb230",
      "value": [
        "leaf",
        "const:544984:8"
      ]
    },
    "old": {
      "definition_site": "004a838c",
      "incomplete_value": false,
      "site": "004a8398",
      "value": [
        "leaf",
        "const:521aec:8"
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cb270",
      "incomplete_value": false,
      "site": "004cb274",
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
      "definition_site": "004a83d8",
      "incomplete_value": false,
      "site": "004a83dc",
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
      "004cb224",
      "PARAM",
      [
        "storage",
        "00521aec",
        null,
        null
      ]
    ],
    [
      "004cb270",
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
      "004cb224",
      "PARAM",
      [
        "storage",
        "00544984",
        null,
        null
      ]
    ],
    [
      "004cb270",
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

- 旧版 [`004a8398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a832c.md#insn-004a8398) · [`004a83dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a832c.md#insn-004a83dc) · [`004a8358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a832c.md#insn-004a8358)
- 新版 `004cb230`（命令位置の公開資料なし） · `004cb274`（命令位置の公開資料なし） · `004cb1f0`（命令位置の公開資料なし）

~~~diff
- 004a8398 ["INT_ADD", "register:40f0:8", ["const:4a8398:8", "const:4:8"]]
- 004a8398 ["CALL", null, ["callee:00c57d10:8"]]
+ 004cb230 ["INT_ADD", "register:40f0:8", ["const:4cb230:8", "const:4:8"]]
+ 004cb230 ["CALL", null, ["callee:00c57d10:8"]]
- 004a8398 bytes cacb1c94
+ 004cb230 bytes b8321e94
- 004a83dc ["INT_ADD", "register:40f0:8", ["const:4a83dc:8", "const:4:8"]]
- 004a83dc ["CALL", null, ["callee:00c57d20:8"]]
+ 004cb274 ["INT_ADD", "register:40f0:8", ["const:4cb274:8", "const:4:8"]]
+ 004cb274 ["CALL", null, ["callee:00c57d20:8"]]
- 004a83dc bytes bdcb1c94
+ 004cb274 bytes ab321e94
- 004a8358 ["INT_ADD", "register:40f0:8", ["const:4a8358:8", "const:4:8"]]
- 004a8358 ["CALL", null, ["callee:00c57a90:8"]]
+ 004cb1f0 ["INT_ADD", "register:40f0:8", ["const:4cb1f0:8", "const:4:8"]]
+ 004cb1f0 ["CALL", null, ["callee:00c57a90:8"]]
- 004a8358 bytes 3acb1c94
+ 004cb1f0 bytes 28321e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a2ee8cbd6589f4aa9bbe9e6e2c9600a"></a>

### [`004a8854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8854.md) → [`004cb6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb6ec.md) FUN_004cb6ec

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0049e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md) [`0050db94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050db94.md) · 呼出先 6件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbe0.md)
- 新版 呼出元 2件 [`004c128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c128c.md) [`00530a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a2c.md) · 呼出先 6件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58630.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.53% / 新版 90.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cb718",
      "incomplete_value": true,
      "site": "004cb720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8880",
      "incomplete_value": true,
      "site": "004a8888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004cb780",
      "incomplete_value": true,
      "site": "004cb780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a88e8",
      "incomplete_value": true,
      "site": "004a88e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004cb7b0",
      "incomplete_value": true,
      "site": "004cb7c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004a8918",
      "incomplete_value": true,
      "site": "004a8928",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "004cb70c",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004cb720",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cb76c",
      "READ",
      [
        "storage",
        "00c1b150",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004cb70c",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004cb720",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cb76c",
      "READ",
      [
        "storage",
        "00c9ab40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8854.md#insn-004a8974) · [`004a898c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8854.md#insn-004a898c) · [`004a89b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8854.md#insn-004a89b0)
- 新版 `004cb80c`（命令位置の公開資料なし） · `004cb824`（命令位置の公開資料なし） · `004cb848`（命令位置の公開資料なし）

~~~diff
- 004a8974 ["INT_ADD", "register:40f0:8", ["const:4a8974:8", "const:4:8"]]
- 004a8974 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004cb80c ["INT_ADD", "register:40f0:8", ["const:4cb80c:8", "const:4:8"]]
+ 004cb80c ["CALL", null, ["ram:c58640:8"]]
- 004a8974 bytes 9fcc1c94
+ 004cb80c bytes 8d331e94
- 004a898c ["INT_ADD", "register:40f0:8", ["const:4a898c:8", "const:4:8"]]
- 004a898c ["CALL", null, ["callee:00c57b10:8"]]
+ 004cb824 ["INT_ADD", "register:40f0:8", ["const:4cb824:8", "const:4:8"]]
+ 004cb824 ["CALL", null, ["callee:00c57b10:8"]]
- 004a898c bytes cdc91c94
+ 004cb824 bytes bb301e94
- 004a89b0 ["INT_ADD", "register:40f0:8", ["const:4a89b0:8", "const:4:8"]]
- 004a89b0 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004cb848 ["INT_ADD", "register:40f0:8", ["const:4cb848:8", "const:4:8"]]
+ 004cb848 ["CALL", null, ["ram:c58640:8"]]
- 004a89b0 bytes 90cc1c94
+ 004cb848 bytes 7e331e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa432f592fd8a817a2e2987ee28230db"></a>

### [`004a8bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8bc4.md) → [`004cba5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cba5c.md) FUN_004cba5c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0049e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md) [`0050dee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050dee4.md) · 呼出先 6件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbe0.md)
- 新版 呼出元 2件 [`004c128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c128c.md) [`00530d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530d7c.md) · 呼出先 6件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58630.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cba88",
      "incomplete_value": true,
      "site": "004cba90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8bf0",
      "incomplete_value": true,
      "site": "004a8bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004cbaf0",
      "incomplete_value": true,
      "site": "004cbaf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8c58",
      "incomplete_value": true,
      "site": "004a8c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004cbb20",
      "incomplete_value": true,
      "site": "004cbb2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:120:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8c88",
      "incomplete_value": true,
      "site": "004a8c94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a50:8"
              ]
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
      "004cba7c",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004cba90",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cbadc",
      "READ",
      [
        "storage",
        "00c1b160",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004cba7c",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004cba90",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cbadc",
      "READ",
      [
        "storage",
        "00c9ab50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8bc4.md#insn-004a8cdc) · [`004a8cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8bc4.md#insn-004a8cf4) · [`004a8d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8bc4.md#insn-004a8d18)
- 新版 `004cbb74`（命令位置の公開資料なし） · `004cbb8c`（命令位置の公開資料なし） · `004cbbb0`（命令位置の公開資料なし）

~~~diff
- 004a8cdc ["INT_ADD", "register:40f0:8", ["const:4a8cdc:8", "const:4:8"]]
- 004a8cdc ["CALL", null, ["ram:bdbbf0:8"]]
+ 004cbb74 ["INT_ADD", "register:40f0:8", ["const:4cbb74:8", "const:4:8"]]
+ 004cbb74 ["CALL", null, ["ram:c58640:8"]]
- 004a8cdc bytes c5cb1c94
+ 004cbb74 bytes b3321e94
- 004a8cf4 ["INT_ADD", "register:40f0:8", ["const:4a8cf4:8", "const:4:8"]]
- 004a8cf4 ["CALL", null, ["callee:00c57b10:8"]]
+ 004cbb8c ["INT_ADD", "register:40f0:8", ["const:4cbb8c:8", "const:4:8"]]
+ 004cbb8c ["CALL", null, ["callee:00c57b10:8"]]
- 004a8cf4 bytes f3c81c94
+ 004cbb8c bytes e12f1e94
- 004a8d18 ["INT_ADD", "register:40f0:8", ["const:4a8d18:8", "const:4:8"]]
- 004a8d18 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004cbbb0 ["INT_ADD", "register:40f0:8", ["const:4cbbb0:8", "const:4:8"]]
+ 004cbbb0 ["CALL", null, ["ram:c58640:8"]]
- 004a8d18 bytes b6cb1c94
+ 004cbbb0 bytes a4321e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4695e2dd0a4743de276e2ce05606308d"></a>

### [`004a8d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8d78.md) → [`004cbc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbc10.md) FUN_004cbc10

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0049e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md) [`0050d508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d508.md) · 呼出先 6件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdbbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbe0.md)
- 新版 呼出元 2件 [`004c128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c128c.md) [`005303a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005303a0.md) · 呼出先 6件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58630.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 3件, `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cbc3c",
      "incomplete_value": true,
      "site": "004cbc44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8da4",
      "incomplete_value": true,
      "site": "004a8dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004cbca8",
      "incomplete_value": true,
      "site": "004cbca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004a8e10",
      "incomplete_value": true,
      "site": "004a8e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004cbd14",
      "incomplete_value": true,
      "site": "004cbd18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004a8e7c",
      "incomplete_value": true,
      "site": "004a8e80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 39,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004cbc30",
      "READ",
      [
        "storage",
        "00c1b148",
        null,
        "pointer"
      ]
    ],
    [
      "004cbc44",
      "DATA",
      [
        "storage",
        "00be9d18",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cbc94",
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
      "004cbc30",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004cbc44",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cbc94",
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

- 旧版 [`004a8eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8d78.md#insn-004a8eb8) · [`004a8ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8d78.md#insn-004a8ed0) · [`004a8ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8d78.md#insn-004a8ef4)
- 新版 `004cbd50`（命令位置の公開資料なし） · `004cbd68`（命令位置の公開資料なし） · `004cbd8c`（命令位置の公開資料なし）

~~~diff
- 004a8eb8 ["INT_ADD", "register:40f0:8", ["const:4a8eb8:8", "const:4:8"]]
- 004a8eb8 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004cbd50 ["INT_ADD", "register:40f0:8", ["const:4cbd50:8", "const:4:8"]]
+ 004cbd50 ["CALL", null, ["ram:c58640:8"]]
- 004a8eb8 bytes 4ecb1c94
+ 004cbd50 bytes 3c321e94
- 004a8ed0 ["INT_ADD", "register:40f0:8", ["const:4a8ed0:8", "const:4:8"]]
- 004a8ed0 ["CALL", null, ["callee:00c57b10:8"]]
+ 004cbd68 ["INT_ADD", "register:40f0:8", ["const:4cbd68:8", "const:4:8"]]
+ 004cbd68 ["CALL", null, ["callee:00c57b10:8"]]
- 004a8ed0 bytes 7cc81c94
+ 004cbd68 bytes 6a2f1e94
- 004a8ef4 ["INT_ADD", "register:40f0:8", ["const:4a8ef4:8", "const:4:8"]]
- 004a8ef4 ["CALL", null, ["ram:bdbbf0:8"]]
+ 004cbd8c ["INT_ADD", "register:40f0:8", ["const:4cbd8c:8", "const:4:8"]]
+ 004cbd8c ["CALL", null, ["ram:c58640:8"]]
- 004a8ef4 bytes 3fcb1c94
+ 004cbd8c bytes 2d321e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbab6710b0b0e616b9dd36f32be323f8"></a>

### [`004a933c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a933c.md) → [`004cc1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc1d4.md) _ZN5Botan16ieee1363_hash_idERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc2cc",
      "incomplete_value": false,
      "site": "004cc2d4",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9434",
      "incomplete_value": false,
      "site": "004a943c",
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
            "const:52d:8"
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
      "definition_site": "004cc2e8",
      "incomplete_value": false,
      "site": "004cc2f0",
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
            "const:625:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9450",
      "incomplete_value": false,
      "site": "004a9458",
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
            "const:48c:8"
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
      "definition_site": "004cc32c",
      "incomplete_value": false,
      "site": "004cc334",
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
            "const:3e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9494",
      "incomplete_value": false,
      "site": "004a949c",
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
            "const:373:8"
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
      "004cc2cc",
      "PARAM",
      [
        "storage",
        "002aa52d",
        null,
        "string"
      ]
    ],
    [
      "004cc2e8",
      "PARAM",
      [
        "storage",
        "0029c48c",
        null,
        "string"
      ]
    ],
    [
      "004cc32c",
      "PARAM",
      [
        "storage",
        "0029b373",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004cc2cc",
      "PARAM",
      [
        "storage",
        "002bb2a9",
        null,
        "string"
      ]
    ],
    [
      "004cc2e8",
      "PARAM",
      [
        "storage",
        "002ac625",
        null,
        "string"
      ]
    ],
    [
      "004cc32c",
      "PARAM",
      [
        "storage",
        "002ab3e1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a943c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a933c.md#insn-004a943c) · [`004a9458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a933c.md#insn-004a9458) · [`004a949c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a933c.md#insn-004a949c)
- 新版 `004cc2d4`（命令位置の公開資料なし） · `004cc2f0`（命令位置の公開資料なし） · `004cc334`（命令位置の公開資料なし）

~~~diff
- 004a943c ["INT_ADD", "register:40f0:8", ["const:4a943c:8", "const:4:8"]]
- 004a943c ["CALL", null, ["callee:00441e54:8"]]
+ 004cc2d4 ["INT_ADD", "register:40f0:8", ["const:4cc2d4:8", "const:4:8"]]
+ 004cc2d4 ["CALL", null, ["callee:00441e54:8"]]
- 004a943c bytes c6d7fd97
+ 004cc2d4 bytes e0d6fd97
- 004a9458 ["INT_ADD", "register:40f0:8", ["const:4a9458:8", "const:4:8"]]
- 004a9458 ["CALL", null, ["callee:00441e54:8"]]
+ 004cc2f0 ["INT_ADD", "register:40f0:8", ["const:4cc2f0:8", "const:4:8"]]
+ 004cc2f0 ["CALL", null, ["callee:00441e54:8"]]
- 004a9458 bytes bfd7fd97
+ 004cc2f0 bytes d9d6fd97
- 004a949c ["INT_ADD", "register:40f0:8", ["const:4a949c:8", "const:4:8"]]
- 004a949c ["CALL", null, ["callee:00441e54:8"]]
+ 004cc334 ["INT_ADD", "register:40f0:8", ["const:4cc334:8", "const:4:8"]]
+ 004cc334 ["CALL", null, ["callee:00441e54:8"]]
- 004a949c bytes aed7fd97
+ 004cc334 bytes c8d6fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ab5169a2c50368a4a050987d4eada1e"></a>

### [`004a94c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a94c8.md) → [`004cc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc360.md) _ZN5Botan10hex_decodeEPhPKcmRmb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdc2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2f0.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c58d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d40.md) · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc428",
      "incomplete_value": false,
      "site": "004cc43c",
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
      "definition_site": "004a9590",
      "incomplete_value": false,
      "site": "004a95a4",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc498",
      "incomplete_value": false,
      "site": "004cc4a0",
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
      "definition_site": "004a9600",
      "incomplete_value": false,
      "site": "004a9608",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc4c8",
      "incomplete_value": false,
      "site": "004cc4d0",
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
            "const:92d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a9630",
      "incomplete_value": false,
      "site": "004a9638",
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
            "const:51a:8"
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
      "004cc408",
      "DATA",
      [
        "storage",
        "002b9876",
        null,
        null
      ]
    ],
    [
      "004cc428",
      "PARAM",
      [
        "storage",
        "0029e457",
        null,
        null
      ]
    ],
    [
      "004cc448",
      "PARAM",
      [
        "storage",
        "002ab5b2",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004cc408",
      "DATA",
      [
        "storage",
        "002caf86",
        null,
        null
      ]
    ],
    [
      "004cc428",
      "PARAM",
      [
        "storage",
        "002ae7dc",
        null,
        null
      ]
    ],
    [
      "004cc448",
      "PARAM",
      [
        "storage",
        "002bc4d5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a95a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a94c8.md#insn-004a95a4) · [`004a9608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a94c8.md#insn-004a9608) · [`004a9638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a94c8.md#insn-004a9638)
- 新版 `004cc43c`（命令位置の公開資料なし） · `004cc4a0`（命令位置の公開資料なし） · `004cc4d0`（命令位置の公開資料なし）

~~~diff
- 004a95a4 ["INT_ADD", "register:40f0:8", ["const:4a95a4:8", "const:4:8"]]
- 004a95a4 ["CALL", null, ["callee:00441e54:8"]]
+ 004cc43c ["INT_ADD", "register:40f0:8", ["const:4cc43c:8", "const:4:8"]]
+ 004cc43c ["CALL", null, ["callee:00441e54:8"]]
- 004a95a4 bytes 6cd7fd97
+ 004cc43c bytes 86d6fd97
- 004a9608 ["INT_ADD", "register:40f0:8", ["const:4a9608:8", "const:4:8"]]
- 004a9608 ["CALL", null, ["callee:00441e54:8"]]
+ 004cc4a0 ["INT_ADD", "register:40f0:8", ["const:4cc4a0:8", "const:4:8"]]
+ 004cc4a0 ["CALL", null, ["callee:00441e54:8"]]
- 004a9608 bytes 53d7fd97
+ 004cc4a0 bytes 6dd6fd97
- 004a9638 ["INT_ADD", "register:40f0:8", ["const:4a9638:8", "const:4:8"]]
- 004a9638 ["CALL", null, ["callee:0043dd98:8"]]
+ 004cc4d0 ["INT_ADD", "register:40f0:8", ["const:4cc4d0:8", "const:4:8"]]
+ 004cc4d0 ["CALL", null, ["callee:0043dd98:8"]]
- 004a9638 bytes 18c7fd97
+ 004cc4d0 bytes 32c6fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8797776893385835a77052f96cae325c"></a>

### [`004a9770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9770.md) → [`004cc608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc608.md) _ZN5Botan10hex_decodeEPhPKcmb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc90.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 1件 [`00c586e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586e0.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

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
      "definition_site": "004cc680",
      "incomplete_value": false,
      "site": "004cc688",
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
            "const:43:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a97e8",
      "incomplete_value": false,
      "site": "004a97f0",
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
            "const:615:8"
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
      "definition_site": "004cc6bc",
      "incomplete_value": true,
      "site": "004cc6c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004a9824",
      "incomplete_value": true,
      "site": "004a9830",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004cc6b8",
      "incomplete_value": false,
      "site": "004cc6c8",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "old": {
      "definition_site": "004a9820",
      "incomplete_value": false,
      "site": "004a9830",
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
      "004cc680",
      "PARAM",
      [
        "storage",
        "002a5615",
        null,
        "string"
      ]
    ],
    [
      "004cc6b8",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "004cc6bc",
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
      "004cc680",
      "PARAM",
      [
        "storage",
        "002b6043",
        null,
        "string"
      ]
    ],
    [
      "004cc6b8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004cc6bc",
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

- 旧版 [`004a97f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9770.md#insn-004a97f0) · [`004a9830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9770.md#insn-004a9830) · [`004a97a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9770.md#insn-004a97a0)
- 新版 `004cc688`（命令位置の公開資料なし） · `004cc6c8`（命令位置の公開資料なし） · `004cc638`（命令位置の公開資料なし）

~~~diff
- 004a97f0 ["INT_ADD", "register:40f0:8", ["const:4a97f0:8", "const:4:8"]]
- 004a97f0 ["CALL", null, ["callee:0043dd98:8"]]
+ 004cc688 ["INT_ADD", "register:40f0:8", ["const:4cc688:8", "const:4:8"]]
+ 004cc688 ["CALL", null, ["callee:0043dd98:8"]]
- 004a97f0 bytes aac6fd97
+ 004cc688 bytes c4c5fd97
- 004a9830 ["INT_ADD", "register:40f0:8", ["const:4a9830:8", "const:4:8"]]
- 004a9830 ["CALL", null, ["callee:00c57b10:8"]]
+ 004cc6c8 ["INT_ADD", "register:40f0:8", ["const:4cc6c8:8", "const:4:8"]]
+ 004cc6c8 ["CALL", null, ["callee:00c57b10:8"]]
- 004a9830 bytes 24c61c94
+ 004cc6c8 bytes 122d1e94
- 004a97a0 ["INT_ADD", "register:40f0:8", ["const:4a97a0:8", "const:4:8"]]
- 004a97a0 ["CALL", null, ["callee:00c58d40:8"]]
+ 004cc638 ["INT_ADD", "register:40f0:8", ["const:4cc638:8", "const:4:8"]]
+ 004cc638 ["CALL", null, ["callee:00c58d40:8"]]
- 004a97a0 bytes d4ca1c94
+ 004cc638 bytes c2311e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

