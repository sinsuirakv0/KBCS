# v16.0.2 → v16.0.3 · 最優先の変更候補 (77)

[一覧の目次](README.md)

<a id="compare-851b288fbd9c526716c20e04f22c5240"></a>

### [`00b59d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b59/00b59d40.md) → [`00b5ad34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5a/00b5ad34.md) _ZN8firebase10app_common15LibraryRegistry15RegisterLibraryEPKcS3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b7d0.md) · 呼出先 12件 [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`00493e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5c7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c7a0.md) · 呼出先 12件 [`0046d908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d908.md) [`00494128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494128.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.63% / 新版 99.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5afa0",
      "incomplete_value": false,
      "site": "00b5afb0",
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
            "const:1d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b59fac",
      "incomplete_value": false,
      "site": "00b59fbc",
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
            "const:fb:8"
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
      "00b5afa0",
      "PARAM",
      [
        "storage",
        "002bd0fb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5afa0",
      "PARAM",
      [
        "storage",
        "002bd1d9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b59fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b59/00b59d40.md#insn-00b59fbc) · [`00b59d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b59/00b59d40.md#insn-00b59d84) · [`00b59dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b59/00b59d40.md#insn-00b59dc0)
- 新版 [`00b5afb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5a/00b5ad34.md#insn-00b5afb0) · [`00b5ad78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5a/00b5ad34.md#insn-00b5ad78) · [`00b5adb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5a/00b5ad34.md#insn-00b5adb4)

~~~diff
- 00b59fbc ["INT_ADD", "register:40f0:8", ["const:b59fbc:8", "const:4:8"]]
- 00b59fbc ["CALL", null, ["callee:00c5be80:8"]]
+ 00b5afb0 ["INT_ADD", "register:40f0:8", ["const:b5afb0:8", "const:4:8"]]
+ 00b5afb0 ["CALL", null, ["callee:00c5be80:8"]]
- 00b59fbc bytes bd030494
+ 00b5afb0 bytes b4030494
- 00b59d84 ["INT_ADD", "register:40f0:8", ["const:b59d84:8", "const:4:8"]]
- 00b59d84 ["CALL", null, ["callee:00c59080:8"]]
+ 00b5ad78 ["INT_ADD", "register:40f0:8", ["const:b5ad78:8", "const:4:8"]]
+ 00b5ad78 ["CALL", null, ["callee:00c59080:8"]]
- 00b59d84 bytes cbf80394
+ 00b5ad78 bytes c2f80394
- 00b59dc0 ["INT_ADD", "register:40f0:8", ["const:b59dc0:8", "const:4:8"]]
- 00b59dc0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5adb4 ["INT_ADD", "register:40f0:8", ["const:b5adb4:8", "const:4:8"]]
+ 00b5adb4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b59dc0 bytes 68f80394
+ 00b5adb4 bytes 5ff80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2093f3038ec636248b205b7aaabc6cd"></a>

### [`00b5a52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5a52c.md) → [`00b5b520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5b520.md) _ZN8firebase10app_common16RegisterSdkUsageEPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b810.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b880.md)
- 新版 呼出元 1件 [`00c5c7e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c7e0.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c850.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_condition` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5b550",
      "incomplete_value": true,
      "site": "00b5b550",
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
      "definition_site": "00b5a55c",
      "incomplete_value": true,
      "site": "00b5a55c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5b53c",
      "incomplete_value": true,
      "site": "00b5b540",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a548",
      "incomplete_value": true,
      "site": "00b5a54c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c0:8"
              ]
            ]
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
      "definition_site": "00b5b58c",
      "incomplete_value": false,
      "site": "00b5b598",
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
            "const:6ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a598",
      "incomplete_value": false,
      "site": "00b5a5a4",
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
            "const:5e0:8"
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
      "00b5b534",
      "READ",
      [
        "storage",
        "011260c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b548",
      "READ",
      [
        "storage",
        "00c9b820",
        null,
        "pointer"
      ]
    ],
    [
      "00b5b54c",
      "READ",
      [
        "storage",
        "011260c8",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5b534",
      "READ",
      [
        "storage",
        "01127080",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b548",
      "READ",
      [
        "storage",
        "00c9c7f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5b54c",
      "READ",
      [
        "storage",
        "01127088",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5a52c.md#insn-00b5a54c) · [`00b5a5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5a52c.md#insn-00b5a5a4) · [`00b5a5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5a52c.md#insn-00b5a5c0)
- 新版 [`00b5b540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5b520.md#insn-00b5b540) · [`00b5b598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5b520.md#insn-00b5b598) · [`00b5b5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5b520.md#insn-00b5b5b4)

~~~diff
- 00b5a54c ["INT_ADD", "register:40f0:8", ["const:b5a54c:8", "const:4:8"]]
- 00b5a54c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5b540 ["INT_ADD", "register:40f0:8", ["const:b5b540:8", "const:4:8"]]
+ 00b5b540 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5a54c bytes 61010494
+ 00b5b540 bytes 58010494
- 00b5a5a4 ["INT_ADD", "register:40f0:8", ["const:b5a5a4:8", "const:4:8"]]
- 00b5a5a4 ["CALL", null, ["callee:00c5c850:8"]]
+ 00b5b598 ["INT_ADD", "register:40f0:8", ["const:b5b598:8", "const:4:8"]]
+ 00b5b598 ["CALL", null, ["callee:00c5c850:8"]]
- 00b5a5a4 bytes b7040494
+ 00b5b598 bytes ae040494
- 00b5a5c0 ["INT_ADD", "register:40f0:8", ["const:b5a5c0:8", "const:4:8"]]
- 00b5a5c0 ["CALL", null, ["callee:00c5c850:8"]]
+ 00b5b5b4 ["INT_ADD", "register:40f0:8", ["const:b5b5b4:8", "const:4:8"]]
+ 00b5b5b4 ["CALL", null, ["callee:00c5c850:8"]]
- 00b5a5c0 bytes b0040494
+ 00b5b5b4 bytes a7040494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f6cfd31f9507ad811842cd4f795c742"></a>

### [`00b5a63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5a63c.md) → [`00b5b630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5b630.md) _ZN8firebase10app_common12GetUserAgentEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b7b0.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5c780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c780.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5b658",
      "incomplete_value": true,
      "site": "00b5b658",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b5a664",
      "incomplete_value": true,
      "site": "00b5a664",
      "value": [
        "INT_NOTEQUAL",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5b644",
      "incomplete_value": true,
      "site": "00b5b648",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a650",
      "incomplete_value": true,
      "site": "00b5a654",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00b5a664"
      ],
      [
        "FALL_THROUGH",
        "00b5b658"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b5b658",
      "incomplete_value": true,
      "site": "00b5b668",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b5a664",
      "incomplete_value": true,
      "site": "00b5a674",
      "value": [
        "INT_NOTEQUAL",
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
      "00b5b640",
      "READ",
      [
        "storage",
        "011260c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b650",
      "READ",
      [
        "storage",
        "00c9b820",
        null,
        "pointer"
      ]
    ],
    [
      "00b5b654",
      "READ",
      [
        "storage",
        "011260c8",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5b640",
      "READ",
      [
        "storage",
        "01127080",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5b650",
      "READ",
      [
        "storage",
        "00c9c7f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5b654",
      "READ",
      [
        "storage",
        "01127088",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5a63c.md#insn-00b5a654) · [`00b5a648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5a63c.md#insn-00b5a648) · [`00b5a64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5a63c.md#insn-00b5a64c)
- 新版 [`00b5b648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5b630.md#insn-00b5b648) · [`00b5b63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5b630.md#insn-00b5b63c) · [`00b5b640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5b630.md#insn-00b5b640)

~~~diff
- 00b5a654 ["INT_ADD", "register:40f0:8", ["const:b5a654:8", "const:4:8"]]
- 00b5a654 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5b648 ["INT_ADD", "register:40f0:8", ["const:b5b648:8", "const:4:8"]]
+ 00b5b648 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5a654 bytes 1f010494
+ 00b5b648 bytes 16010494
- 00b5a648 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b5b63c ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b5a648 bytes 682e0090
+ 00b5b63c bytes 682e0090
- 00b5a64c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c0:8"]]
- 00b5a64c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5b640 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 00b5b640 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5a64c bytes 136140f9
+ 00b5b640 bytes 134140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-956de8374dd98b3667898e161c70a160"></a>

### [`00b5ab18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ab18.md) → [`00b5bb0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bb0c.md) _ZN8firebase10app_common19FindAppLoggerByNameEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5bb50",
      "incomplete_value": true,
      "site": "00b5bb50",
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
      "definition_site": "00b5ab5c",
      "incomplete_value": true,
      "site": "00b5ab5c",
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
      "definition_site": "00b5bbec",
      "incomplete_value": true,
      "site": "00b5bbf0",
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
                "live",
                "register:40a0:8"
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
      "definition_site": "00b5abf8",
      "incomplete_value": true,
      "site": "00b5abfc",
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
                "live",
                "register:40a0:8"
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5bb40",
      "incomplete_value": true,
      "site": "00b5bb44",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ab4c",
      "incomplete_value": true,
      "site": "00b5ab50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "00b5bb3c",
      "READ",
      [
        "storage",
        "011260c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bb4c",
      "READ",
      [
        "storage",
        "011260d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bbe4",
      "READ",
      [
        "storage",
        "011260d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5bb3c",
      "READ",
      [
        "storage",
        "01127080",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bb4c",
      "READ",
      [
        "storage",
        "01127098",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5bbe4",
      "READ",
      [
        "storage",
        "01127098",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ab50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ab18.md#insn-00b5ab50) · [`00b5ab44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ab18.md#insn-00b5ab44) · [`00b5ab48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ab18.md#insn-00b5ab48)
- 新版 [`00b5bb44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bb0c.md#insn-00b5bb44) · [`00b5bb38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bb0c.md#insn-00b5bb38) · [`00b5bb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bb0c.md#insn-00b5bb3c)

~~~diff
- 00b5ab50 ["INT_ADD", "register:40f0:8", ["const:b5ab50:8", "const:4:8"]]
- 00b5ab50 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5bb44 ["INT_ADD", "register:40f0:8", ["const:b5bb44:8", "const:4:8"]]
+ 00b5bb44 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5ab50 bytes e0ff0394
+ 00b5bb44 bytes d7ff0394
- 00b5ab44 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b5bb38 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b5ab44 bytes 682e0090
+ 00b5bb38 bytes 682e0090
- 00b5ab48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c0:8"]]
- 00b5ab48 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5bb3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 00b5bb3c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ab48 bytes 136140f9
+ 00b5bb3c bytes 134140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74512c6717c08367577f5f2f89ab3652"></a>

### [`00b5b258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b258.md) → [`00b5c24c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c24c.md) _INIT_279

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b5b2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b2a8.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b5c29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c29c.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5bd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5c290",
      "incomplete_value": false,
      "site": "00b5c290",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b29c",
      "incomplete_value": false,
      "site": "00b5b29c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:c0:8"
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
      "definition_site": "00b5c260",
      "incomplete_value": true,
      "site": "00b5c270",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:790:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b26c",
      "incomplete_value": true,
      "site": "00b5b27c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c0:8"
              ]
            ]
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
      "definition_site": "00b5c264",
      "incomplete_value": true,
      "site": "00b5c270",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:7f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b270",
      "incomplete_value": true,
      "site": "00b5b27c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:828:8"
              ]
            ]
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
      "00b5c260",
      "READ",
      [
        "storage",
        "00c9b7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c260",
      "PARAM",
      [
        "storage",
        "00b5b2a8",
        "_ZN8firebase6LoggerD1Ev",
        null
      ]
    ],
    [
      "00b5c264",
      "READ",
      [
        "storage",
        "00c9b828",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5c260",
      "READ",
      [
        "storage",
        "00c9c790",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c260",
      "PARAM",
      [
        "storage",
        "00b5c29c",
        "_ZN8firebase6LoggerD1Ev",
        null
      ]
    ],
    [
      "00b5c264",
      "READ",
      [
        "storage",
        "00c9c7f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b258.md#insn-00b5b27c) · [`00b5b29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b258.md#insn-00b5b29c) · [`00b5b264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b258.md#insn-00b5b264)
- 新版 [`00b5c270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c24c.md#insn-00b5c270) · [`00b5c290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c24c.md#insn-00b5c290) · [`00b5c258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c24c.md#insn-00b5c258)

~~~diff
- 00b5b27c ["INT_ADD", "register:40f0:8", ["const:b5b27c:8", "const:4:8"]]
- 00b5b27c ["CALL", null, ["callee:00c58ed0:8"]]
+ 00b5c270 ["INT_ADD", "register:40f0:8", ["const:b5c270:8", "const:4:8"]]
+ 00b5c270 ["CALL", null, ["callee:00c58ed0:8"]]
- 00b5b27c bytes 21f30394
+ 00b5c270 bytes 18f30394
- 00b5b29c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c0:8"]]
- 00b5b29c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00b5c290 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
+ 00b5c290 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b5b29c bytes 136100f9
+ 00b5c290 bytes 134100f9
- 00b5b264 ["COPY", "register:4000:8", ["const:c9b000:8"]]
+ 00b5c258 ["COPY", "register:4000:8", ["const:c9c000:8"]]
- 00b5b264 bytes 000a0090
+ 00b5c258 bytes 000a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a40e8e5ae11e6a4f3cf666ca05cb8132"></a>

### [`00b5b9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b9e0.md) → [`00b5c9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c9d4.md) _ZN8firebase8callback10InitializeEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8a0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md)
- 新版 呼出元 1件 [`00c5c870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c870.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5ca34",
      "incomplete_value": false,
      "site": "00b5ca34",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ba40",
      "incomplete_value": false,
      "site": "00b5ba40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5ca3c",
      "incomplete_value": true,
      "site": "00b5ca3c",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ba48",
      "incomplete_value": true,
      "site": "00b5ba48",
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
            "const:e8:8"
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
      "definition_site": "00b5c9ec",
      "incomplete_value": true,
      "site": "00b5c9f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b9f8",
      "incomplete_value": true,
      "site": "00b5b9fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "00b5c9e8",
      "READ",
      [
        "storage",
        "011260e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c9f8",
      "READ",
      [
        "storage",
        "011260e8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5ca2c",
      "READ",
      [
        "storage",
        "011260e8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b5c9e8",
      "READ",
      [
        "storage",
        "011270a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c9f8",
      "READ",
      [
        "storage",
        "011270a8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5ca2c",
      "READ",
      [
        "storage",
        "011270a8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b9fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b9e0.md#insn-00b5b9fc) · [`00b5ba40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b9e0.md#insn-00b5ba40) · [`00b5ba48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b9e0.md#insn-00b5ba48)
- 新版 [`00b5c9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c9d4.md#insn-00b5c9f0) · [`00b5ca34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c9d4.md#insn-00b5ca34) · [`00b5ca3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c9d4.md#insn-00b5ca3c)

~~~diff
- 00b5b9fc ["INT_ADD", "register:40f0:8", ["const:b5b9fc:8", "const:4:8"]]
- 00b5b9fc ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5c9f0 ["INT_ADD", "register:40f0:8", ["const:b5c9f0:8", "const:4:8"]]
+ 00b5c9f0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5b9fc bytes 35fc0394
+ 00b5c9f0 bytes 2cfc0394
- 00b5ba40 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f0:8"]]
- 00b5ba40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00b5ca34 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b0:8"]]
+ 00b5ca34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00b5ba40 bytes 347900f9
+ 00b5ca34 bytes 345900f9
- 00b5ba48 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e8:8"]]
- 00b5ba48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b5ca3c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a8:8"]]
+ 00b5ca3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b5ba48 bytes a8ea00b9
+ 00b5ca3c bytes a8aa00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bbd95919b38ddbcf5724343c172ea95"></a>

### [`00b5bbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bbd0.md) → [`00b5cbc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cbc4.md) FUN_00b5cbc4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00b5ba74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5ba74.md) [`00b5bfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bfa8.md) [`00b5c0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c0d4.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md)
- 新版 呼出元 3件 [`00b5ca68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5ca68.md) [`00b5cf9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cf9c.md) [`00b5d0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d0c8.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be80.md) [`00c5c1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cbf8",
      "incomplete_value": true,
      "site": "00b5cbf8",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bc04",
      "incomplete_value": true,
      "site": "00b5bc04",
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
            "const:e8:8"
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
      "definition_site": "00b5cc18",
      "incomplete_value": true,
      "site": "00b5cc18",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bc24",
      "incomplete_value": true,
      "site": "00b5bc24",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cc2c",
      "incomplete_value": false,
      "site": "00b5cc2c",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bc38",
      "incomplete_value": false,
      "site": "00b5bc38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "00b5cbd8",
      "READ",
      [
        "storage",
        "011260e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cbec",
      "READ",
      [
        "storage",
        "011260e8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5cbf8",
      "WRITE",
      [
        "storage",
        "011260e8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b5cbd8",
      "READ",
      [
        "storage",
        "011270a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cbec",
      "READ",
      [
        "storage",
        "011270a8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5cbf8",
      "WRITE",
      [
        "storage",
        "011270a8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bbd0.md#insn-00b5bbf0) · [`00b5bc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bbd0.md#insn-00b5bc04) · [`00b5bc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bbd0.md#insn-00b5bc14)
- 新版 [`00b5cbe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cbc4.md#insn-00b5cbe4) · [`00b5cbf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cbc4.md#insn-00b5cbf8) · [`00b5cc08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cbc4.md#insn-00b5cc08)

~~~diff
- 00b5bbf0 ["INT_ADD", "register:40f0:8", ["const:b5bbf0:8", "const:4:8"]]
- 00b5bbf0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5cbe4 ["INT_ADD", "register:40f0:8", ["const:b5cbe4:8", "const:4:8"]]
+ 00b5cbe4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5bbf0 bytes b8fb0394
+ 00b5cbe4 bytes affb0394
- 00b5bc04 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e8:8"]]
- 00b5bc04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
+ 00b5cbf8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a8:8"]]
+ 00b5cbf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
- 00b5bc04 bytes a1ea00b9
+ 00b5cbf8 bytes a1aa00b9
- 00b5bc14 ["INT_ADD", "register:40f0:8", ["const:b5bc14:8", "const:4:8"]]
- 00b5bc14 ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00b5cc08 ["INT_ADD", "register:40f0:8", ["const:b5cc08:8", "const:4:8"]]
+ 00b5cc08 ["CALL", null, ["callee:00c5c1d0:8"]]
- 00b5bc14 bytes 7bfd0394
+ 00b5cc08 bytes 72fd0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8e9ae3e6c53c48d5aeb9664b74eaf9e"></a>

### [`00b5bc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bc90.md) → [`00b5cc84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cc84.md) _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5bbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bbc0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md) [`00c5bbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bbe0.md)
- 新版 呼出元 1件 [`00c5cb90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb90.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd20.md) [`00c5cbb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cbb0.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 84.78% / 新版 84.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5ccf8",
      "incomplete_value": true,
      "site": "00b5ccf8",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bd04",
      "incomplete_value": true,
      "site": "00b5bd04",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5cd04",
      "incomplete_value": true,
      "site": "00b5cd04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bd10",
      "incomplete_value": true,
      "site": "00b5bd10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "definition_site": "00b5cca4",
      "incomplete_value": true,
      "site": "00b5cca8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bcb0",
      "incomplete_value": true,
      "site": "00b5bcb4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "00b5cc9c",
      "READ",
      [
        "storage",
        "011260e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ccac",
      "READ",
      [
        "storage",
        "011260e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ccbc",
      "READ",
      [
        "storage",
        "011260e8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b5cc9c",
      "READ",
      [
        "storage",
        "011270a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ccac",
      "READ",
      [
        "storage",
        "011270a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ccbc",
      "READ",
      [
        "storage",
        "011270a8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bcb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bc90.md#insn-00b5bcb4) · [`00b5bcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bc90.md#insn-00b5bcc0) · [`00b5bd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bc90.md#insn-00b5bd04)
- 新版 [`00b5cca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cc84.md#insn-00b5cca8) · [`00b5ccb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cc84.md#insn-00b5ccb4) · [`00b5ccf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cc84.md#insn-00b5ccf8)

~~~diff
- 00b5bcb4 ["INT_ADD", "register:40f0:8", ["const:b5bcb4:8", "const:4:8"]]
- 00b5bcb4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5cca8 ["INT_ADD", "register:40f0:8", ["const:b5cca8:8", "const:4:8"]]
+ 00b5cca8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5bcb4 bytes 87fb0394
+ 00b5cca8 bytes 7efb0394
- 00b5bcc0 ["INT_ADD", "register:40f0:8", ["const:b5bcc0:8", "const:4:8"]]
- 00b5bcc0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5ccb4 ["INT_ADD", "register:40f0:8", ["const:b5ccb4:8", "const:4:8"]]
+ 00b5ccb4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5bcc0 bytes 84fb0394
+ 00b5ccb4 bytes 7bfb0394
- 00b5bd04 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:f0:8"]]
- 00b5bd04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
+ 00b5ccf8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:b0:8"]]
+ 00b5ccf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00b5bd04 bytes f67a00f9
+ 00b5ccf8 bytes f65a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1384cbcd27f43f629c5f5ba178eb807a"></a>

### [`00b5bfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bfa8.md) → [`00b5cf9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cf9c.md) _ZN8firebase8callback14RemoveCallbackEPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b5bbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bbd0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b5cbc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cbc4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.33% / 新版 85.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d020",
      "incomplete_value": true,
      "site": "00b5d020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c02c",
      "incomplete_value": true,
      "site": "00b5c02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d02c",
      "incomplete_value": true,
      "site": "00b5d02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c038",
      "incomplete_value": true,
      "site": "00b5c038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "definition_site": "00b5cfc0",
      "incomplete_value": true,
      "site": "00b5cfc4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5bfcc",
      "incomplete_value": true,
      "site": "00b5bfd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "00b5cfb8",
      "READ",
      [
        "storage",
        "011260e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cfcc",
      "READ",
      [
        "storage",
        "011260e8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5cfd8",
      "READ",
      [
        "storage",
        "011260e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cfb8",
      "READ",
      [
        "storage",
        "011270a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cfcc",
      "READ",
      [
        "storage",
        "011270a8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5cfd8",
      "READ",
      [
        "storage",
        "011270a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bfa8.md#insn-00b5bfd0) · [`00b5bfec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bfa8.md#insn-00b5bfec) · [`00b5c02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bfa8.md#insn-00b5c02c)
- 新版 [`00b5cfc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cf9c.md#insn-00b5cfc4) · [`00b5cfe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cf9c.md#insn-00b5cfe0) · [`00b5d020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cf9c.md#insn-00b5d020)

~~~diff
- 00b5bfd0 ["INT_ADD", "register:40f0:8", ["const:b5bfd0:8", "const:4:8"]]
- 00b5bfd0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5cfc4 ["INT_ADD", "register:40f0:8", ["const:b5cfc4:8", "const:4:8"]]
+ 00b5cfc4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5bfd0 bytes c0fa0394
+ 00b5cfc4 bytes b7fa0394
- 00b5bfec ["INT_ADD", "register:40f0:8", ["const:b5bfec:8", "const:4:8"]]
- 00b5bfec ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5cfe0 ["INT_ADD", "register:40f0:8", ["const:b5cfe0:8", "const:4:8"]]
+ 00b5cfe0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5bfec bytes b9fa0394
+ 00b5cfe0 bytes b0fa0394
- 00b5c02c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:f0:8"]]
- 00b5c02c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
+ 00b5d020 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:b0:8"]]
+ 00b5d020 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00b5c02c bytes 367b00f9
+ 00b5d020 bytes 365b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdd376e5cf6f87758360518358f0a0ce"></a>

### [`00b5c0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c0d4.md) → [`00b5d0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d0c8.md) _ZN8firebase8callback13PollCallbacksEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b5bbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bbd0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c586f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586f0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b5cbc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cbc4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c596c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596c0.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d144",
      "incomplete_value": true,
      "site": "00b5d144",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c150",
      "incomplete_value": true,
      "site": "00b5c150",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d150",
      "incomplete_value": true,
      "site": "00b5d150",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c15c",
      "incomplete_value": true,
      "site": "00b5c15c",
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
            "const:e8:8"
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
      "definition_site": "00b5d16c",
      "incomplete_value": false,
      "site": "00b5d16c",
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
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c178",
      "incomplete_value": false,
      "site": "00b5c178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:100:8"
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
      "00b5d0e0",
      "READ",
      [
        "storage",
        "011260e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d0f0",
      "READ",
      [
        "storage",
        "011260e8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5d0fc",
      "READ",
      [
        "storage",
        "011260e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d0e0",
      "READ",
      [
        "storage",
        "011270a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d0f0",
      "READ",
      [
        "storage",
        "011270a8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5d0fc",
      "READ",
      [
        "storage",
        "011270a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c0d4.md#insn-00b5c0f4) · [`00b5c110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c0d4.md#insn-00b5c110) · [`00b5c150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c0d4.md#insn-00b5c150)
- 新版 [`00b5d0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d0c8.md#insn-00b5d0e8) · [`00b5d104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d0c8.md#insn-00b5d104) · [`00b5d144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d0c8.md#insn-00b5d144)

~~~diff
- 00b5c0f4 ["INT_ADD", "register:40f0:8", ["const:b5c0f4:8", "const:4:8"]]
- 00b5c0f4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5d0e8 ["INT_ADD", "register:40f0:8", ["const:b5d0e8:8", "const:4:8"]]
+ 00b5d0e8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5c0f4 bytes 77fa0394
+ 00b5d0e8 bytes 6efa0394
- 00b5c110 ["INT_ADD", "register:40f0:8", ["const:b5c110:8", "const:4:8"]]
- 00b5c110 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5d104 ["INT_ADD", "register:40f0:8", ["const:b5d104:8", "const:4:8"]]
+ 00b5d104 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5c110 bytes 70fa0394
+ 00b5d104 bytes 67fa0394
- 00b5c150 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:f0:8"]]
- 00b5c150 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 00b5d144 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:b0:8"]]
+ 00b5d144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b5c150 bytes d57a00f9
+ 00b5d144 bytes d55a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e7574edfcb5304edd312a9f31f70dcc"></a>

### [`00b5c2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c2f8.md) → [`00b5d2ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d2ec.md) _ZN8firebase8callback18CallbackDispatcherD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc10.md) · 呼出先 6件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md)
- 新版 呼出元 1件 [`00c5cbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cbe0.md) · 呼出先 6件 [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d318",
      "incomplete_value": false,
      "site": "00b5d31c",
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
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c324",
      "incomplete_value": false,
      "site": "00b5c328",
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
            "const:106:8"
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
      "00b5d318",
      "PARAM",
      [
        "storage",
        "002ae106",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5d318",
      "PARAM",
      [
        "storage",
        "002ae1d3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c2f8.md#insn-00b5c328) · [`00b5c314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c2f8.md#insn-00b5c314) · [`00b5c324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c2f8.md#insn-00b5c324)
- 新版 [`00b5d31c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d2ec.md#insn-00b5d31c) · [`00b5d308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d2ec.md#insn-00b5d308) · [`00b5d318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d2ec.md#insn-00b5d318)

~~~diff
- 00b5c328 ["INT_ADD", "register:40f0:8", ["const:b5c328:8", "const:4:8"]]
- 00b5c328 ["CALL", null, ["callee:00c5be80:8"]]
+ 00b5d31c ["INT_ADD", "register:40f0:8", ["const:b5d31c:8", "const:4:8"]]
+ 00b5d31c ["CALL", null, ["callee:00c5be80:8"]]
- 00b5c328 bytes e2fa0394
+ 00b5d31c bytes d9fa0394
- 00b5c314 ["INT_ADD", "register:40f0:8", ["const:b5c314:8", "const:4:8"]]
- 00b5c314 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5d308 ["INT_ADD", "register:40f0:8", ["const:b5d308:8", "const:4:8"]]
+ 00b5d308 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5c314 bytes eff90394
+ 00b5d308 bytes e6f90394
- 00b5c324 ["COPY", "tmp:0:8", ["const:106:8"]]
- 00b5c324 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c324 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c324 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5d318 ["COPY", "tmp:0:8", ["const:1d3:8"]]
+ 00b5d318 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d318 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d318 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5c324 bytes 00180491
+ 00b5d318 bytes 004c0791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc3167d08b53087f02d9c0a41ea7a602"></a>

### [`00b5c490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c490.md) → [`00b5d484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d484.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

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
      "definition_site": "00b5d4a4",
      "incomplete_value": true,
      "site": "00b5d4a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5c4b0",
      "incomplete_value": true,
      "site": "00b5c4b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b5d49c",
      "READ",
      [
        "storage",
        "00c9b858",
        null,
        "pointer"
      ]
    ],
    [
      "00b5d4a8",
      "DATA",
      [
        "storage",
        "00c903e8",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00b5d49c",
      "READ",
      [
        "storage",
        "00c9c828",
        null,
        "pointer"
      ]
    ],
    [
      "00b5d4a8",
      "DATA",
      [
        "storage",
        "00c913b8",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c490.md#insn-00b5c4a0) · [`00b5c4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c490.md#insn-00b5c4a8) · [`00b5c4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c490.md#insn-00b5c4bc)
- 新版 [`00b5d494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d484.md#insn-00b5d494) · [`00b5d49c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d484.md#insn-00b5d49c) · [`00b5d4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d484.md#insn-00b5d4b0)

~~~diff
- 00b5c4a0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b5d494 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b5c4a0 bytes e80900f0
+ 00b5d494 bytes e80900f0
- 00b5c4a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:858:8"]]
- 00b5c4a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d49c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:828:8"]]
+ 00b5d49c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5c4a8 bytes 082d44f9
+ 00b5d49c bytes 081544f9
- 00b5c4bc ["INT_ADD", "register:40f0:8", ["const:b5c4bc:8", "const:4:8"]]
- 00b5c4bc ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5d4b0 ["INT_ADD", "register:40f0:8", ["const:b5d4b0:8", "const:4:8"]]
+ 00b5d4b0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5c4bc bytes 85f90394
+ 00b5d4b0 bytes 7cf90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4936dd54e218348ccf61a329a40f036c"></a>

### [`00b5c600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c600.md) → [`00b5d5f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d5f4.md) _ZN8firebase8callback16BlockingCallbackD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5bc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5cc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc20.md)

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
      "definition_site": "00b5d610",
      "incomplete_value": true,
      "site": "00b5d614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5c61c",
      "incomplete_value": true,
      "site": "00b5c620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "00b5d608",
      "READ",
      [
        "storage",
        "00c9b850",
        null,
        "pointer"
      ]
    ],
    [
      "00b5d614",
      "DATA",
      [
        "storage",
        "00c90438",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b5d608",
      "READ",
      [
        "storage",
        "00c9c820",
        null,
        "pointer"
      ]
    ],
    [
      "00b5d614",
      "DATA",
      [
        "storage",
        "00c91408",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c600.md#insn-00b5c60c) · [`00b5c614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c600.md#insn-00b5c614) · [`00b5c628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c600.md#insn-00b5c628)
- 新版 [`00b5d600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d5f4.md#insn-00b5d600) · [`00b5d608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d5f4.md#insn-00b5d608) · [`00b5d61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d5f4.md#insn-00b5d61c)

~~~diff
- 00b5c60c ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00b5d600 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00b5c60c bytes e90900f0
+ 00b5d600 bytes e90900f0
- 00b5c614 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:850:8"]]
- 00b5c614 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d608 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:820:8"]]
+ 00b5d608 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5c614 bytes 292944f9
+ 00b5d608 bytes 291144f9
- 00b5c628 ["INT_ADD", "register:40f0:8", ["const:b5c628:8", "const:4:8"]]
- 00b5c628 ["CALL", null, ["callee:00c5cc20:8"]]
+ 00b5d61c ["INT_ADD", "register:40f0:8", ["const:b5d61c:8", "const:4:8"]]
+ 00b5d61c ["CALL", null, ["callee:00c5cc20:8"]]
- 00b5c628 bytes 8afd0394
+ 00b5d61c bytes 81fd0394
~~~


<a id="compare-473b994f172320d5144f2038560fc2a1"></a>

### [`00b5c77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c77c.md) → [`00b5d770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d770.md) _INIT_280

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5bd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd20.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d79c",
      "incomplete_value": true,
      "site": "00b5d79c",
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
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c7a8",
      "incomplete_value": true,
      "site": "00b5c7a8",
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
            "const:e0:8"
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
      "definition_site": "00b5d7a0",
      "incomplete_value": false,
      "site": "00b5d7a0",
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
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c7ac",
      "incomplete_value": false,
      "site": "00b5c7ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:100:8"
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
      "00b5d79c",
      "WRITE",
      [
        "storage",
        "011260e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d7a0",
      "WRITE",
      [
        "storage",
        "01126100",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d79c",
      "WRITE",
      [
        "storage",
        "011270a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d7a0",
      "WRITE",
      [
        "storage",
        "011270c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c77c.md#insn-00b5c7a8) · [`00b5c7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c77c.md#insn-00b5c7ac) · [`00b5c78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c77c.md#insn-00b5c78c)
- 新版 [`00b5d79c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d770.md#insn-00b5d79c) · [`00b5d7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d770.md#insn-00b5d7a0) · [`00b5d780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d770.md#insn-00b5d780)

~~~diff
- 00b5c7a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e0:8"]]
- 00b5c7a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00b5d79c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a0:8"]]
+ 00b5d79c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b5c7a8 bytes 137100f9
+ 00b5d79c bytes 135100f9
- 00b5c7ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:100:8"]]
- 00b5c7ac ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5c7ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b5d7a0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c0:8"]]
+ 00b5d7a0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b5d7a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5c7ac bytes 3f8100f9
+ 00b5d7a0 bytes 3f6100f9
- 00b5c78c ["INT_ADD", "register:40f0:8", ["const:b5c78c:8", "const:4:8"]]
- 00b5c78c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5d780 ["INT_ADD", "register:40f0:8", ["const:b5d780:8", "const:4:8"]]
+ 00b5d780 ["CALL", null, ["callee:00c58f30:8"]]
- 00b5c78c bytes f5ed0394
+ 00b5d780 bytes eced0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93b2494ba9a8c0b943900f98cd5ff674"></a>

### [`00b5c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c990.md) → [`00b5d984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d984.md) _ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5bc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc80.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5bc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc70.md)
- 新版 呼出元 1件 [`00c5cc50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc50.md) · 呼出先 3件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5cc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.88% / 新版 93.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5d9a8",
      "incomplete_value": true,
      "site": "00b5d9ac",
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
      "definition_site": "00b5c9b4",
      "incomplete_value": true,
      "site": "00b5c9b8",
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
      "00b5d99c",
      "READ",
      [
        "storage",
        "00c9b868",
        null,
        "pointer"
      ]
    ],
    [
      "00b5d9a4",
      "READ",
      [
        "storage",
        "01126108",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b5d9c0",
      "READ",
      [
        "storage",
        "00c9b860",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5d99c",
      "READ",
      [
        "storage",
        "00c9c838",
        null,
        "pointer"
      ]
    ],
    [
      "00b5d9a4",
      "READ",
      [
        "storage",
        "011270c8",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b5d9c0",
      "READ",
      [
        "storage",
        "00c9c830",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c990.md#insn-00b5c9b8) · [`00b5c9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c990.md#insn-00b5c9a4) · [`00b5c9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c990.md#insn-00b5c9a8)
- 新版 [`00b5d9ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d984.md#insn-00b5d9ac) · [`00b5d998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d984.md#insn-00b5d998) · [`00b5d99c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d984.md#insn-00b5d99c)

~~~diff
- 00b5c9b8 ["INT_ADD", "register:40f0:8", ["const:b5c9b8:8", "const:4:8"]]
- 00b5c9b8 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5d9ac ["INT_ADD", "register:40f0:8", ["const:b5d9ac:8", "const:4:8"]]
+ 00b5d9ac ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5c9b8 bytes 46f80394
+ 00b5d9ac bytes 3df80394
- 00b5c9a4 ["COPY", "register:40b0:8", ["const:c9b000:8"]]
+ 00b5d998 ["COPY", "register:40b0:8", ["const:c9c000:8"]]
- 00b5c9a4 bytes f60900f0
+ 00b5d998 bytes f60900f0
- 00b5c9a8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:868:8"]]
- 00b5c9a8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d99c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:838:8"]]
+ 00b5d99c ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5c9a8 bytes d63644f9
+ 00b5d99c bytes d61e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1346c5c2f1ff50ef5823c1a7bfecd906"></a>

### [`00b5cc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5cc64.md) → [`00b5dc58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5dc58.md) _ZN8firebase15CleanupNotifier15UnregisterOwnerEPS0_Pv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5bc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5cc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc40.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5dc8c",
      "incomplete_value": true,
      "site": "00b5dc8c",
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
      "definition_site": "00b5cc98",
      "incomplete_value": true,
      "site": "00b5cc98",
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
      "00b5dc68",
      "READ",
      [
        "storage",
        "00c9b868",
        null,
        "pointer"
      ]
    ],
    [
      "00b5dc70",
      "READ",
      [
        "storage",
        "01126108",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b5dc80",
      "READ",
      [
        "storage",
        "00c9b860",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5dc68",
      "READ",
      [
        "storage",
        "00c9c838",
        null,
        "pointer"
      ]
    ],
    [
      "00b5dc70",
      "READ",
      [
        "storage",
        "011270c8",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b5dc80",
      "READ",
      [
        "storage",
        "00c9c830",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5cc64.md#insn-00b5cc70) · [`00b5cc74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5cc64.md#insn-00b5cc74) · [`00b5cc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5cc64.md#insn-00b5cc84)
- 新版 [`00b5dc64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5dc58.md#insn-00b5dc64) · [`00b5dc68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5dc58.md#insn-00b5dc68) · [`00b5dc78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5dc58.md#insn-00b5dc78)

~~~diff
- 00b5cc70 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b5dc64 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b5cc70 bytes e80900f0
+ 00b5dc64 bytes e80900f0
- 00b5cc74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:868:8"]]
- 00b5cc74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5dc68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:838:8"]]
+ 00b5dc68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cc74 bytes 083544f9
+ 00b5dc68 bytes 081d44f9
- 00b5cc84 ["INT_ADD", "register:40f0:8", ["const:b5cc84:8", "const:4:8"]]
- 00b5cc84 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5dc78 ["INT_ADD", "register:40f0:8", ["const:b5dc78:8", "const:4:8"]]
+ 00b5dc78 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5cc84 bytes 93f70394
+ 00b5dc78 bytes 8af70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65a17c26606266fe6afbf8ab865612e0"></a>

### [`00b5e9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e9ec.md) → [`00b5f9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f9e0.md) _ZN8firebase17FutureBackingDataD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bd60.md) · 呼出先 10件 [`00b60f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60f48.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md)
- 新版 呼出元 1件 [`00c5cd30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cd30.md) · 呼出先 10件 [`00b61f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61f3c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.76% / 新版 98.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5fa14",
      "incomplete_value": false,
      "site": "00b5fa18",
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
            "const:9d7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ea20",
      "incomplete_value": false,
      "site": "00b5ea24",
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
            "const:98d:8"
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
      "definition_site": "00b5fa3c",
      "incomplete_value": false,
      "site": "00b5fa40",
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
            "const:631:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ea48",
      "incomplete_value": false,
      "site": "00b5ea4c",
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
            "const:5e7:8"
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
      "00b5fa14",
      "PARAM",
      [
        "storage",
        "002c098d",
        null,
        "string"
      ]
    ],
    [
      "00b5fa3c",
      "PARAM",
      [
        "storage",
        "002b25e7",
        null,
        "string"
      ]
    ],
    [
      "00b5fa74",
      "READ",
      [
        "storage",
        "00c9b878",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5fa14",
      "PARAM",
      [
        "storage",
        "002c09d7",
        null,
        "string"
      ]
    ],
    [
      "00b5fa3c",
      "PARAM",
      [
        "storage",
        "002b2631",
        null,
        "string"
      ]
    ],
    [
      "00b5fa74",
      "READ",
      [
        "storage",
        "00c9c848",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ea24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e9ec.md#insn-00b5ea24) · [`00b5ea4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e9ec.md#insn-00b5ea4c) · [`00b5ea08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e9ec.md#insn-00b5ea08)
- 新版 [`00b5fa18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f9e0.md#insn-00b5fa18) · [`00b5fa40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f9e0.md#insn-00b5fa40) · [`00b5f9fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f9e0.md#insn-00b5f9fc)

~~~diff
- 00b5ea24 ["INT_ADD", "register:40f0:8", ["const:b5ea24:8", "const:4:8"]]
- 00b5ea24 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b5fa18 ["INT_ADD", "register:40f0:8", ["const:b5fa18:8", "const:4:8"]]
+ 00b5fa18 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b5ea24 bytes abf10394
+ 00b5fa18 bytes a2f10394
- 00b5ea4c ["INT_ADD", "register:40f0:8", ["const:b5ea4c:8", "const:4:8"]]
- 00b5ea4c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b5fa40 ["INT_ADD", "register:40f0:8", ["const:b5fa40:8", "const:4:8"]]
+ 00b5fa40 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b5ea4c bytes a1f10394
+ 00b5fa40 bytes 98f10394
- 00b5ea08 ["INT_ADD", "register:40f0:8", ["const:b5ea08:8", "const:4:8"]]
- 00b5ea08 ["CALL", null, ["callee:00c5cd20:8"]]
+ 00b5f9fc ["INT_ADD", "register:40f0:8", ["const:b5f9fc:8", "const:4:8"]]
+ 00b5f9fc ["CALL", null, ["callee:00c5cd20:8"]]
- 00b5ea08 bytes d2f40394
+ 00b5f9fc bytes c9f40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2444888a18cba4c3263690f425e9d747"></a>

### [`00b5ed6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ed6c.md) → [`00b5fd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5fd60.md) _ZN8firebase26ReferenceCountedFutureImplD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c5ad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad20.md) [`00c5bda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bda0.md) · 呼出先 11件 [`00b613bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b613bc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md)
- 新版 呼出元 2件 [`00c5bcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcf0.md) [`00c5cd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cd70.md) · 呼出先 11件 [`00b623b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b623b0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb40.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.83% / 新版 96.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5fd8c",
      "incomplete_value": true,
      "site": "00b5fd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5ed98",
      "incomplete_value": true,
      "site": "00b5ed9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b5fd80",
      "READ",
      [
        "storage",
        "00c9b780",
        null,
        "pointer"
      ]
    ],
    [
      "00b5fd90",
      "DATA",
      [
        "storage",
        "00c90490",
        null,
        "undefined1[120]"
      ]
    ],
    [
      "00b5fe40",
      "PARAM",
      [
        "storage",
        "0029f955",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5fd80",
      "READ",
      [
        "storage",
        "00c9c750",
        null,
        "pointer"
      ]
    ],
    [
      "00b5fd90",
      "DATA",
      [
        "storage",
        "00c91460",
        null,
        "undefined1[120]"
      ]
    ],
    [
      "00b5fe40",
      "PARAM",
      [
        "storage",
        "0029f995",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ed84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ed6c.md#insn-00b5ed84) · [`00b5ed8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ed6c.md#insn-00b5ed8c) · [`00b5edb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ed6c.md#insn-00b5edb4)
- 新版 [`00b5fd78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5fd60.md#insn-00b5fd78) · [`00b5fd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5fd60.md#insn-00b5fd80) · [`00b5fda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5fd60.md#insn-00b5fda8)

~~~diff
- 00b5ed84 ["COPY", "register:4050:8", ["const:c9b000:8"]]
+ 00b5fd78 ["COPY", "register:4050:8", ["const:c9c000:8"]]
- 00b5ed84 bytes ea0900b0
+ 00b5fd78 bytes ea0900b0
- 00b5ed8c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:780:8"]]
- 00b5ed8c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5fd80 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:750:8"]]
+ 00b5fd80 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ed8c bytes 4ac143f9
+ 00b5fd80 bytes 4aa943f9
- 00b5edb4 ["INT_ADD", "register:40f0:8", ["const:b5edb4:8", "const:4:8"]]
- 00b5edb4 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b5fda8 ["INT_ADD", "register:40f0:8", ["const:b5fda8:8", "const:4:8"]]
+ 00b5fda8 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b5edb4 bytes 4bef0394
+ 00b5fda8 bytes 42ef0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96928cfd0bd52318f6eded6a24f72fd9"></a>

### [`00b5f588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f588.md) → [`00b6057c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b6057c.md) _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5bf00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf00.md) · 呼出先 3件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b605e4",
      "incomplete_value": false,
      "site": "00b605e8",
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
            "const:d9f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f5f0",
      "incomplete_value": false,
      "site": "00b5f5f4",
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
            "const:cd0:8"
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
      "definition_site": "00b605fc",
      "incomplete_value": false,
      "site": "00b60600",
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
            "const:5ca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f608",
      "incomplete_value": false,
      "site": "00b5f60c",
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
            "const:580:8"
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
      "00b605e4",
      "PARAM",
      [
        "storage",
        "002b7cd0",
        null,
        "string"
      ]
    ],
    [
      "00b605fc",
      "PARAM",
      [
        "storage",
        "002b3580",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b605e4",
      "PARAM",
      [
        "storage",
        "002b7d9f",
        null,
        "string"
      ]
    ],
    [
      "00b605fc",
      "PARAM",
      [
        "storage",
        "002b35ca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f588.md#insn-00b5f5f4) · [`00b5f60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f588.md#insn-00b5f60c) · [`00b5f5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f588.md#insn-00b5f5a8)
- 新版 [`00b605e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b6057c.md#insn-00b605e8) · [`00b60600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b6057c.md#insn-00b60600) · [`00b6059c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b6057c.md#insn-00b6059c)

~~~diff
- 00b5f5f4 ["INT_ADD", "register:40f0:8", ["const:b5f5f4:8", "const:4:8"]]
- 00b5f5f4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b605e8 ["INT_ADD", "register:40f0:8", ["const:b605e8:8", "const:4:8"]]
+ 00b605e8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b5f5f4 bytes b7ee0394
+ 00b605e8 bytes aeee0394
- 00b5f60c ["INT_ADD", "register:40f0:8", ["const:b5f60c:8", "const:4:8"]]
- 00b5f60c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b60600 ["INT_ADD", "register:40f0:8", ["const:b60600:8", "const:4:8"]]
+ 00b60600 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b5f60c bytes b1ee0394
+ 00b60600 bytes a8ee0394
- 00b5f5a8 ["INT_ADD", "register:40f0:8", ["const:b5f5a8:8", "const:4:8"]]
- 00b5f5a8 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b6059c ["INT_ADD", "register:40f0:8", ["const:b6059c:8", "const:4:8"]]
+ 00b6059c ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5f5a8 bytes 4aed0394
+ 00b6059c bytes 41ed0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7f2483162abdf394021c7d3f6b27fe4"></a>

### [`00b5f6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f6bc.md) → [`00b606b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b606b0.md) _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5af60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af60.md) · 呼出先 10件 [`00b60f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60f48.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5bf30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf30.md) · 呼出先 10件 [`00b61f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61f3c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.51% / 新版 99.51%

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
      "definition_site": "00b6073c",
      "incomplete_value": false,
      "site": "00b60740",
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
            "const:d9f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f748",
      "incomplete_value": false,
      "site": "00b5f74c",
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
            "const:cd0:8"
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
      "definition_site": "00b607a0",
      "incomplete_value": false,
      "site": "00b607ac",
      "value": [
        "leaf",
        "const:b61f3c:8"
      ]
    },
    "old": {
      "definition_site": "00b5f7ac",
      "incomplete_value": false,
      "site": "00b5f7b8",
      "value": [
        "leaf",
        "const:b60f48:8"
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
      "00b6073c",
      "PARAM",
      [
        "storage",
        "002b7cd0",
        null,
        "string"
      ]
    ],
    [
      "00b607a0",
      "PARAM",
      [
        "storage",
        "00b60f48",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6073c",
      "PARAM",
      [
        "storage",
        "002b7d9f",
        null,
        "string"
      ]
    ],
    [
      "00b607a0",
      "PARAM",
      [
        "storage",
        "00b61f3c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f6bc.md#insn-00b5f74c) · [`00b5f7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f6bc.md#insn-00b5f7b8) · [`00b5f6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f6bc.md#insn-00b5f6fc)
- 新版 [`00b60740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b606b0.md#insn-00b60740) · [`00b607ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b606b0.md#insn-00b607ac) · [`00b606f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b606b0.md#insn-00b606f0)

~~~diff
- 00b5f74c ["INT_ADD", "register:40f0:8", ["const:b5f74c:8", "const:4:8"]]
- 00b5f74c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b60740 ["INT_ADD", "register:40f0:8", ["const:b60740:8", "const:4:8"]]
+ 00b60740 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b5f74c bytes 61ee0394
+ 00b60740 bytes 58ee0394
- 00b5f7b8 ["INT_ADD", "register:40f0:8", ["const:b5f7b8:8", "const:4:8"]]
- 00b5f7b8 ["CALL", null, ["callee:00c5bca0:8"]]
+ 00b607ac ["INT_ADD", "register:40f0:8", ["const:b607ac:8", "const:4:8"]]
+ 00b607ac ["CALL", null, ["callee:00c5bca0:8"]]
- 00b5f7b8 bytes 46ed0394
+ 00b607ac bytes 3ded0394
- 00b5f6fc ["INT_ADD", "register:40f0:8", ["const:b5f6fc:8", "const:4:8"]]
- 00b5f6fc ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b606f0 ["INT_ADD", "register:40f0:8", ["const:b606f0:8", "const:4:8"]]
+ 00b606f0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5f6fc bytes f5ec0394
+ 00b606f0 bytes ecec0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32c5733a7182e0e7979cc91a0cdcb61c"></a>

### [`00b5fb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fb94.md) → [`00b60b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60b88.md) _ZN8firebase26ReferenceCountedFutureImpl13ReleaseFutureERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6a0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c670.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60bfc",
      "incomplete_value": false,
      "site": "00b60c00",
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
            "const:687:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5fc08",
      "incomplete_value": false,
      "site": "00b5fc0c",
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
            "const:5a9:8"
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
      "00b60bfc",
      "PARAM",
      [
        "storage",
        "002be5a9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b60bfc",
      "PARAM",
      [
        "storage",
        "002be687",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5fc0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fb94.md#insn-00b5fc0c) · [`00b5fbb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fb94.md#insn-00b5fbb4) · [`00b5fc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fb94.md#insn-00b5fc08)
- 新版 [`00b60c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60b88.md#insn-00b60c00) · [`00b60ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60b88.md#insn-00b60ba8) · [`00b60bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60b88.md#insn-00b60bfc)

~~~diff
- 00b5fc0c ["INT_ADD", "register:40f0:8", ["const:b5fc0c:8", "const:4:8"]]
- 00b5fc0c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b60c00 ["INT_ADD", "register:40f0:8", ["const:b60c00:8", "const:4:8"]]
+ 00b60c00 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b5fc0c bytes 31ed0394
+ 00b60c00 bytes 28ed0394
- 00b5fbb4 ["INT_ADD", "register:40f0:8", ["const:b5fbb4:8", "const:4:8"]]
- 00b5fbb4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60ba8 ["INT_ADD", "register:40f0:8", ["const:b60ba8:8", "const:4:8"]]
+ 00b60ba8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5fbb4 bytes c7eb0394
+ 00b60ba8 bytes beeb0394
- 00b5fc08 ["COPY", "tmp:0:8", ["const:5a9:8"]]
- 00b5fc08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5fc08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5fc08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b60bfc ["COPY", "tmp:0:8", ["const:687:8"]]
+ 00b60bfc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b60bfc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b60bfc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5fc08 bytes 00a41691
+ 00b60bfc bytes 001c1a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b001fe19c68fadc6c8af3e19ee16156e"></a>

### [`00b60320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60320.md) → [`00b61314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61314.md) _ZN8firebase26ReferenceCountedFutureImpl27AddCompletionCallbackLambdaERKNS_12FutureHandleENSt6__ndk18functionIFvRKNS_10FutureBaseEEEEb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b60530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60530.md) [`00b60568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60568.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b61524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61524.md) [`00b6155c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b6155c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b613ac",
      "incomplete_value": false,
      "site": "00b613ac",
      "value": [
        "leaf",
        "const:b61524:8"
      ]
    },
    "old": {
      "definition_site": "00b603b8",
      "incomplete_value": false,
      "site": "00b603b8",
      "value": [
        "leaf",
        "const:b60530:8"
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b613b4",
      "incomplete_value": false,
      "site": "00b613c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b61000:8"
          ],
          [
            "leaf",
            "const:55c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b603c0",
      "incomplete_value": false,
      "site": "00b603cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b60000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "00b613ac",
      "DATA",
      [
        "storage",
        "00b60530",
        null,
        null
      ]
    ],
    [
      "00b613c0",
      "DATA",
      [
        "storage",
        "00b60568",
        null,
        null
      ]
    ],
    [
      "00b614f4",
      "DATA",
      [
        "storage",
        "00b60568",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b613ac",
      "DATA",
      [
        "storage",
        "00b61524",
        null,
        null
      ]
    ],
    [
      "00b613c0",
      "DATA",
      [
        "storage",
        "00b6155c",
        null,
        null
      ]
    ],
    [
      "00b614f4",
      "DATA",
      [
        "storage",
        "00b6155c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60320.md#insn-00b60350) · [`00b6035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60320.md#insn-00b6035c) · [`00b60380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60320.md#insn-00b60380)
- 新版 [`00b61344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61314.md#insn-00b61344) · [`00b61350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61314.md#insn-00b61350) · [`00b61374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61314.md#insn-00b61374)

~~~diff
- 00b60350 ["INT_ADD", "register:40f0:8", ["const:b60350:8", "const:4:8"]]
- 00b60350 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b61344 ["INT_ADD", "register:40f0:8", ["const:b61344:8", "const:4:8"]]
+ 00b61344 ["CALL", null, ["callee:00c58f30:8"]]
- 00b60350 bytes 04df0394
+ 00b61344 bytes fbde0394
- 00b6035c ["INT_ADD", "register:40f0:8", ["const:b6035c:8", "const:4:8"]]
- 00b6035c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b61350 ["INT_ADD", "register:40f0:8", ["const:b61350:8", "const:4:8"]]
+ 00b61350 ["CALL", null, ["callee:00c58f30:8"]]
- 00b6035c bytes 01df0394
+ 00b61350 bytes f8de0394
- 00b60380 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b60380 ["INT_ADD", "register:40f0:8", ["const:b60380:8", "const:4:8"]]
- 00b60380 ["CALLIND", null, ["register:0:8"]]
+ 00b61374 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b61374 ["INT_ADD", "register:40f0:8", ["const:b61374:8", "const:4:8"]]
+ 00b61374 ["CALLIND", null, ["register:0:8"]]
- 00b60380 bytes 20013fd6
+ 00b61374 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-999ca0fe20c02d8d1feedaab4f4c73f6"></a>

### [`00b60804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60804.md) → [`00b617f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b617f8.md) _ZN8firebase26ReferenceCountedFutureImpl14SetContextDataERKNS_12FutureHandleEPvPFvS4_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5bd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bd70.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5cd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cd40.md) · 呼出先 3件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b618a8",
      "incomplete_value": false,
      "site": "00b618ac",
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
            "const:b69:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b608b4",
      "incomplete_value": false,
      "site": "00b608b8",
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
            "const:a9a:8"
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
      "00b618a8",
      "PARAM",
      [
        "storage",
        "002b8a9a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b618a8",
      "PARAM",
      [
        "storage",
        "002b8b69",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b608b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60804.md#insn-00b608b8) · [`00b60830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60804.md#insn-00b60830) · [`00b6083c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60804.md#insn-00b6083c)
- 新版 [`00b618ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b617f8.md#insn-00b618ac) · [`00b61824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b617f8.md#insn-00b61824) · [`00b61830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b617f8.md#insn-00b61830)

~~~diff
- 00b608b8 ["INT_ADD", "register:40f0:8", ["const:b608b8:8", "const:4:8"]]
- 00b608b8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b618ac ["INT_ADD", "register:40f0:8", ["const:b618ac:8", "const:4:8"]]
+ 00b618ac ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b608b8 bytes 06ea0394
+ 00b618ac bytes fde90394
- 00b60830 ["INT_ADD", "register:40f0:8", ["const:b60830:8", "const:4:8"]]
- 00b60830 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b61824 ["INT_ADD", "register:40f0:8", ["const:b61824:8", "const:4:8"]]
+ 00b61824 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b60830 bytes a8e80394
+ 00b61824 bytes 9fe80394
- 00b6083c ["INT_ADD", "register:40f0:8", ["const:b6083c:8", "const:4:8"]]
- 00b6083c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b61830 ["INT_ADD", "register:40f0:8", ["const:b61830:8", "const:4:8"]]
+ 00b61830 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b6083c bytes a5e80394
+ 00b61830 bytes 9ce80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6235fca513b53ac7d8c391c9fc96d0e"></a>

### [`00b6108c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6108c.md) → [`00b62080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62080.md) _ZN8firebase12FutureHandleC1EOS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bd30.md) · 呼出先 3件 [`00b60f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60f48.md) [`00c5acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acd0.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)
- 新版 呼出元 1件 [`00c5cd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cd00.md) · 呼出先 3件 [`00b61f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61f3c.md) [`00c5bca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bca0.md) [`00c5bcb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b620b8",
      "incomplete_value": false,
      "site": "00b620bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b61000:8"
          ],
          [
            "leaf",
            "const:f3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b610c4",
      "incomplete_value": false,
      "site": "00b610c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b60000:8"
          ],
          [
            "leaf",
            "const:f48:8"
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
      "00b620b8",
      "PARAM",
      [
        "storage",
        "00b60f48",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b620b8",
      "PARAM",
      [
        "storage",
        "00b61f3c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b610c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6108c.md#insn-00b610c8) · [`00b610b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6108c.md#insn-00b610b8) · [`00b610c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6108c.md#insn-00b610c4)
- 新版 [`00b620bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62080.md#insn-00b620bc) · [`00b620ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62080.md#insn-00b620ac) · [`00b620b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62080.md#insn-00b620b8)

~~~diff
- 00b610c8 ["INT_ADD", "register:40f0:8", ["const:b610c8:8", "const:4:8"]]
- 00b610c8 ["CALL", null, ["callee:00c5bca0:8"]]
+ 00b620bc ["INT_ADD", "register:40f0:8", ["const:b620bc:8", "const:4:8"]]
+ 00b620bc ["CALL", null, ["callee:00c5bca0:8"]]
- 00b610c8 bytes 02e70394
+ 00b620bc bytes f9e60394
- 00b610b8 ["COPY", "register:4010:8", ["const:b60000:8"]]
+ 00b620ac ["COPY", "register:4010:8", ["const:b61000:8"]]
- 00b610b8 bytes e2fffff0
+ 00b620ac bytes e2fffff0
- 00b610c4 ["COPY", "tmp:0:8", ["const:f48:8"]]
- 00b610c4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b610c4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b610c4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b620b8 ["COPY", "tmp:0:8", ["const:f3c:8"]]
+ 00b620b8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b620b8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b620b8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b610c4 bytes 42203d91
+ 00b620b8 bytes 42f03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32185df27cbdc43f5505f348d9257aff"></a>

### [`00b610ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b610ec.md) → [`00b620e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b620e0.md) _ZN8firebase12FutureHandleaSEOS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bd40.md) · 呼出先 3件 [`00b60f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60f48.md) [`00c5acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acd0.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)
- 新版 呼出元 1件 [`00c5cd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cd10.md) · 呼出先 3件 [`00b61f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61f3c.md) [`00c5bca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bca0.md) [`00c5bcb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b62144",
      "incomplete_value": false,
      "site": "00b6214c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b61000:8"
          ],
          [
            "leaf",
            "const:f3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61150",
      "incomplete_value": false,
      "site": "00b61158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b60000:8"
          ],
          [
            "leaf",
            "const:f48:8"
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
      "00b62144",
      "PARAM",
      [
        "storage",
        "00b60f48",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62144",
      "PARAM",
      [
        "storage",
        "00b61f3c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b610ec.md#insn-00b61158) · [`00b61110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b610ec.md#insn-00b61110) · [`00b61124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b610ec.md#insn-00b61124)
- 新版 [`00b6214c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b620e0.md#insn-00b6214c) · [`00b62104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b620e0.md#insn-00b62104) · [`00b62118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b620e0.md#insn-00b62118)

~~~diff
- 00b61158 ["INT_ADD", "register:40f0:8", ["const:b61158:8", "const:4:8"]]
- 00b61158 ["CALL", null, ["callee:00c5bca0:8"]]
+ 00b6214c ["INT_ADD", "register:40f0:8", ["const:b6214c:8", "const:4:8"]]
+ 00b6214c ["CALL", null, ["callee:00c5bca0:8"]]
- 00b61158 bytes dee60394
+ 00b6214c bytes d5e60394
- 00b61110 ["INT_ADD", "register:40f0:8", ["const:b61110:8", "const:4:8"]]
- 00b61110 ["CALL", null, ["callee:00c5bcb0:8"]]
+ 00b62104 ["INT_ADD", "register:40f0:8", ["const:b62104:8", "const:4:8"]]
+ 00b62104 ["CALL", null, ["callee:00c5bcb0:8"]]
- 00b61110 bytes f4e60394
+ 00b62104 bytes ebe60394
- 00b61124 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61124 ["INT_ADD", "register:40f0:8", ["const:b61124:8", "const:4:8"]]
- 00b61124 ["CALLIND", null, ["register:0:8"]]
+ 00b62118 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62118 ["INT_ADD", "register:40f0:8", ["const:b62118:8", "const:4:8"]]
+ 00b62118 ["CALLIND", null, ["register:0:8"]]
- 00b61124 bytes 00013fd6
+ 00b62118 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb5885d81a8a7b0b11e3417a3d6465ff"></a>

### [`00b614d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b614d0.md) → [`00b624c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b624c4.md) _ZN8firebase17ModuleInitializerD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcf0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b624e0",
      "incomplete_value": true,
      "site": "00b624e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b614ec",
      "incomplete_value": true,
      "site": "00b614f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b624d8",
      "READ",
      [
        "storage",
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      "00b624e4",
      "DATA",
      [
        "storage",
        "00c905a8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b624d8",
      "READ",
      [
        "storage",
        "00c9c888",
        null,
        "pointer"
      ]
    ],
    [
      "00b624e4",
      "DATA",
      [
        "storage",
        "00c91578",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b614dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b614d0.md#insn-00b614dc) · [`00b614e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b614d0.md#insn-00b614e4) · [`00b61504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b614d0.md#insn-00b61504)
- 新版 [`00b624d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b624c4.md#insn-00b624d0) · [`00b624d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b624c4.md#insn-00b624d8) · [`00b624f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b624c4.md#insn-00b624f8)

~~~diff
- 00b614dc ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b624d0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b614dc bytes c80900d0
+ 00b624d0 bytes c80900d0
- 00b614e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8b8:8"]]
- 00b614e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b624d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:888:8"]]
+ 00b624d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b614e4 bytes 085d44f9
+ 00b624d8 bytes 084544f9
- 00b61504 ["INT_ADD", "register:40f0:8", ["const:b61504:8", "const:4:8"]]
- 00b61504 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b624f8 ["INT_ADD", "register:40f0:8", ["const:b624f8:8", "const:4:8"]]
+ 00b624f8 ["CALL", null, ["callee:00c58f50:8"]]
- 00b61504 bytes 9fda0394
+ 00b624f8 bytes 96da0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e07d407a737b47ac60e449cadf16af25"></a>

### [`00b61590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61590.md) → [`00b62584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62584.md) _ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPFNS_10InitResultES2_S3_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5be20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5cdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cdf0.md)

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
      "definition_site": "00b62610",
      "incomplete_value": false,
      "site": "00b62614",
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
            "const:653:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6161c",
      "incomplete_value": false,
      "site": "00b61620",
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
            "const:609:8"
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
      "definition_site": "00b62620",
      "incomplete_value": false,
      "site": "00b62624",
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
            "const:8c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6162c",
      "incomplete_value": false,
      "site": "00b61630",
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
            "const:7e8:8"
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
      "00b62610",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      "00b62620",
      "PARAM",
      [
        "storage",
        "002bf7e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b62610",
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      "00b62620",
      "PARAM",
      [
        "storage",
        "002bf8c6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61590.md#insn-00b61620) · [`00b61630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61590.md#insn-00b61630) · [`00b615ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61590.md#insn-00b615ec)
- 新版 [`00b62614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62584.md#insn-00b62614) · [`00b62624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62584.md#insn-00b62624) · [`00b625e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62584.md#insn-00b625e0)

~~~diff
- 00b61620 ["INT_ADD", "register:40f0:8", ["const:b61620:8", "const:4:8"]]
- 00b61620 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b62614 ["INT_ADD", "register:40f0:8", ["const:b62614:8", "const:4:8"]]
+ 00b62614 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b61620 bytes ace60394
+ 00b62614 bytes a3e60394
- 00b61630 ["INT_ADD", "register:40f0:8", ["const:b61630:8", "const:4:8"]]
- 00b61630 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b62624 ["INT_ADD", "register:40f0:8", ["const:b62624:8", "const:4:8"]]
+ 00b62624 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b61630 bytes a8e60394
+ 00b62624 bytes 9fe60394
- 00b615ec ["INT_ADD", "register:40f0:8", ["const:b615ec:8", "const:4:8"]]
- 00b615ec ["CALL", null, ["callee:00c5cdf0:8"]]
+ 00b625e0 ["INT_ADD", "register:40f0:8", ["const:b625e0:8", "const:4:8"]]
+ 00b625e0 ["CALL", null, ["callee:00c5cdf0:8"]]
- 00b615ec bytes 0dea0394
+ 00b625e0 bytes 04ea0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71b87ce0a02b92c78c73ac4aaa92824d"></a>

### [`00b6163c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6163c.md) → [`00b62630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62630.md) _ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPKPFNS_10InitResultES2_S3_Em

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5be20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be20.md) · 呼出先 14件 [`00b617f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b617f0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5cdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cdf0.md) · 呼出先 14件 [`00b627e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b627e4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.17% / 新版 98.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b62750",
      "incomplete_value": false,
      "site": "00b62754",
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
            "const:653:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6175c",
      "incomplete_value": false,
      "site": "00b61760",
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
            "const:609:8"
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
      "definition_site": "00b62760",
      "incomplete_value": false,
      "site": "00b62764",
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
            "const:234:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6176c",
      "incomplete_value": false,
      "site": "00b61770",
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
            "const:156:8"
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
      "00b62750",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      "00b62760",
      "PARAM",
      [
        "storage",
        "002bd156",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b62750",
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      "00b62760",
      "PARAM",
      [
        "storage",
        "002bd234",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6163c.md#insn-00b61760) · [`00b61770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6163c.md#insn-00b61770) · [`00b61690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6163c.md#insn-00b61690)
- 新版 [`00b62754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62630.md#insn-00b62754) · [`00b62764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62630.md#insn-00b62764) · [`00b62684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62630.md#insn-00b62684)

~~~diff
- 00b61760 ["INT_ADD", "register:40f0:8", ["const:b61760:8", "const:4:8"]]
- 00b61760 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b62754 ["INT_ADD", "register:40f0:8", ["const:b62754:8", "const:4:8"]]
+ 00b62754 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b61760 bytes 5ce60394
+ 00b62754 bytes 53e60394
- 00b61770 ["INT_ADD", "register:40f0:8", ["const:b61770:8", "const:4:8"]]
- 00b61770 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b62764 ["INT_ADD", "register:40f0:8", ["const:b62764:8", "const:4:8"]]
+ 00b62764 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b61770 bytes 58e60394
+ 00b62764 bytes 4fe60394
- 00b61690 ["INT_ADD", "register:40f0:8", ["const:b61690:8", "const:4:8"]]
- 00b61690 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00b62684 ["INT_ADD", "register:40f0:8", ["const:b62684:8", "const:4:8"]]
+ 00b62684 ["CALL", null, ["callee:00c5bea0:8"]]
- 00b61690 bytes 10e60394
+ 00b62684 bytes 07e60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-221fa6ef0c987f5c6c5c7d482bdc8ccc"></a>

### [`00b617f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b617f0.md) → [`00b627e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b627e4.md) FUN_00b627e4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b6163c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6163c.md) [`00b629b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b629b4.md) · 呼出先 15件 [`00b62990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62990.md) [`00b629a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b629a8.md) [`00b629b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b629b4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`00b62630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62630.md) [`00b639a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b639a8.md) · 呼出先 15件 [`00b63984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63984.md) [`00b6399c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b6399c.md) [`00b639a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b639a8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.83% / 新版 96.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b62900",
      "incomplete_value": false,
      "site": "00b62900",
      "value": [
        "leaf",
        "const:b639a8:8"
      ]
    },
    "old": {
      "definition_site": "00b6190c",
      "incomplete_value": false,
      "site": "00b6190c",
      "value": [
        "leaf",
        "const:b629b4:8"
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b628bc",
      "incomplete_value": false,
      "site": "00b628c0",
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
            "const:20b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b618c8",
      "incomplete_value": false,
      "site": "00b618cc",
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
            "const:13e:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b62918",
      "incomplete_value": true,
      "site": "00b62930",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61924",
      "incomplete_value": true,
      "site": "00b6193c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b0:8"
              ]
            ]
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
      "00b628bc",
      "PARAM",
      [
        "storage",
        "002ae13e",
        null,
        "string"
      ]
    ],
    [
      "00b62900",
      "DATA",
      [
        "storage",
        "00b629b4",
        null,
        null
      ]
    ],
    [
      "00b62918",
      "READ",
      [
        "storage",
        "00c9b8b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b628bc",
      "PARAM",
      [
        "storage",
        "002ae20b",
        null,
        "string"
      ]
    ],
    [
      "00b62900",
      "DATA",
      [
        "storage",
        "00b639a8",
        null,
        null
      ]
    ],
    [
      "00b62918",
      "READ",
      [
        "storage",
        "00c9c880",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b618cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b617f0.md#insn-00b618cc) · [`00b6193c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b617f0.md#insn-00b6193c) · [`00b61830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b617f0.md#insn-00b61830)
- 新版 [`00b628c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b627e4.md#insn-00b628c0) · [`00b62930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b627e4.md#insn-00b62930) · [`00b62824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b627e4.md#insn-00b62824)

~~~diff
- 00b618cc ["INT_ADD", "register:40f0:8", ["const:b618cc:8", "const:4:8"]]
- 00b618cc ["CALL", null, ["callee:00c5be80:8"]]
+ 00b628c0 ["INT_ADD", "register:40f0:8", ["const:b628c0:8", "const:4:8"]]
+ 00b628c0 ["CALL", null, ["callee:00c5be80:8"]]
- 00b618cc bytes 79e50394
+ 00b628c0 bytes 70e50394
- 00b6193c ["COPY", "register:0:8", ["register:4048:8"]]
- 00b6193c ["INT_ADD", "register:40f0:8", ["const:b6193c:8", "const:4:8"]]
- 00b6193c ["CALLIND", null, ["register:0:8"]]
+ 00b62930 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b62930 ["INT_ADD", "register:40f0:8", ["const:b62930:8", "const:4:8"]]
+ 00b62930 ["CALLIND", null, ["register:0:8"]]
- 00b6193c bytes 20013fd6
+ 00b62930 bytes 20013fd6
- 00b61830 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61830 ["INT_ADD", "register:40f0:8", ["const:b61830:8", "const:4:8"]]
- 00b61830 ["CALLIND", null, ["register:0:8"]]
+ 00b62824 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62824 ["INT_ADD", "register:40f0:8", ["const:b62824:8", "const:4:8"]]
+ 00b62824 ["CALLIND", null, ["register:0:8"]]
- 00b61830 bytes 00013fd6
+ 00b62824 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed4939decc1f00031c701d9f0fc2e585"></a>

### [`00b61e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61e3c.md) → [`00b62e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62e30.md) _ZN8firebase11AppCallback16SetEnabledByNameEPKcb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 94.79% / 新版 94.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62e84",
      "incomplete_value": true,
      "site": "00b62e84",
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
      "definition_site": "00b61e90",
      "incomplete_value": true,
      "site": "00b61e90",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b62e70",
      "incomplete_value": true,
      "site": "00b62e74",
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
      "definition_site": "00b61e7c",
      "incomplete_value": true,
      "site": "00b61e80",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b62f44",
      "incomplete_value": true,
      "site": "00b62f50",
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
            "const:3f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61f50",
      "incomplete_value": true,
      "site": "00b61f5c",
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
            "const:31d:8"
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
      "00b62e68",
      "READ",
      [
        "storage",
        "00c9b890",
        null,
        "pointer"
      ]
    ],
    [
      "00b62e6c",
      "READ",
      [
        "storage",
        "01126130",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b62e7c",
      "READ",
      [
        "storage",
        "00c9b888",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b62e68",
      "READ",
      [
        "storage",
        "00c9c860",
        null,
        "pointer"
      ]
    ],
    [
      "00b62e6c",
      "READ",
      [
        "storage",
        "011270f0",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b62e7c",
      "READ",
      [
        "storage",
        "00c9c858",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61e3c.md#insn-00b61e80) · [`00b61f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61e3c.md#insn-00b61f5c) · [`00b61f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61e3c.md#insn-00b61f78)
- 新版 [`00b62e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62e30.md#insn-00b62e74) · [`00b62f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62e30.md#insn-00b62f50) · [`00b62f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62e30.md#insn-00b62f6c)

~~~diff
- 00b61e80 ["INT_ADD", "register:40f0:8", ["const:b61e80:8", "const:4:8"]]
- 00b61e80 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b62e74 ["INT_ADD", "register:40f0:8", ["const:b62e74:8", "const:4:8"]]
+ 00b62e74 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b61e80 bytes 14e30394
+ 00b62e74 bytes 0be30394
- 00b61f5c ["INT_ADD", "register:40f0:8", ["const:b61f5c:8", "const:4:8"]]
- 00b61f5c ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00b62f50 ["INT_ADD", "register:40f0:8", ["const:b62f50:8", "const:4:8"]]
+ 00b62f50 ["CALL", null, ["callee:00c5c1d0:8"]]
- 00b61f5c bytes a9e40394
+ 00b62f50 bytes a0e40394
- 00b61f78 ["INT_ADD", "register:40f0:8", ["const:b61f78:8", "const:4:8"]]
- 00b61f78 ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00b62f6c ["INT_ADD", "register:40f0:8", ["const:b62f6c:8", "const:4:8"]]
+ 00b62f6c ["CALL", null, ["callee:00c5c1d0:8"]]
- 00b61f78 bytes a2e40394
+ 00b62f6c bytes 99e40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b664b3994d9ea5da1234f968ea40884f"></a>

### [`00b61fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61fbc.md) → [`00b62fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62fb0.md) _ZN8firebase11AppCallback13SetEnabledAllEb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1d0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62fe8",
      "incomplete_value": true,
      "site": "00b62fe8",
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
      "definition_site": "00b61ff4",
      "incomplete_value": true,
      "site": "00b61ff4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b62fd4",
      "incomplete_value": true,
      "site": "00b62fd8",
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
      "definition_site": "00b61fe0",
      "incomplete_value": true,
      "site": "00b61fe4",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63008",
      "incomplete_value": true,
      "site": "00b6300c",
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
            "const:6a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62014",
      "incomplete_value": true,
      "site": "00b62018",
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
            "const:5c6:8"
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
      "00b62fc8",
      "READ",
      [
        "storage",
        "00c9b890",
        null,
        "pointer"
      ]
    ],
    [
      "00b62fd0",
      "READ",
      [
        "storage",
        "01126130",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b62fe0",
      "READ",
      [
        "storage",
        "00c9b888",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b62fc8",
      "READ",
      [
        "storage",
        "00c9c860",
        null,
        "pointer"
      ]
    ],
    [
      "00b62fd0",
      "READ",
      [
        "storage",
        "011270f0",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b62fe0",
      "READ",
      [
        "storage",
        "00c9c858",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61fbc.md#insn-00b61fe4) · [`00b62018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61fbc.md#insn-00b62018) · [`00b61fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61fbc.md#insn-00b61fd0)
- 新版 [`00b62fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62fb0.md#insn-00b62fd8) · [`00b6300c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62fb0.md#insn-00b6300c) · [`00b62fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62fb0.md#insn-00b62fc4)

~~~diff
- 00b61fe4 ["INT_ADD", "register:40f0:8", ["const:b61fe4:8", "const:4:8"]]
- 00b61fe4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b62fd8 ["INT_ADD", "register:40f0:8", ["const:b62fd8:8", "const:4:8"]]
+ 00b62fd8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b61fe4 bytes bbe20394
+ 00b62fd8 bytes b2e20394
- 00b62018 ["INT_ADD", "register:40f0:8", ["const:b62018:8", "const:4:8"]]
- 00b62018 ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00b6300c ["INT_ADD", "register:40f0:8", ["const:b6300c:8", "const:4:8"]]
+ 00b6300c ["CALL", null, ["callee:00c5c1d0:8"]]
- 00b62018 bytes 7ae40394
+ 00b6300c bytes 71e40394
- 00b61fd0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b62fc4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b61fd0 bytes c80900d0
+ 00b62fc4 bytes c80900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f816d7c50ac27bee2bf8bbe7eb1cbbe"></a>

### [`00b620e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b620e4.md) → [`00b630d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b630d8.md) _ZN8firebase11AppCallback11AddCallbackEPS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ac90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac90.md) · 呼出先 11件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5bc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc60.md) · 呼出先 11件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.82% / 新版 96.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b63114",
      "incomplete_value": true,
      "site": "00b63114",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b62120",
      "incomplete_value": true,
      "site": "00b62120",
      "value": [
        "INT_NOTEQUAL",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b631e4",
      "incomplete_value": false,
      "site": "00b631e8",
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
            "const:733:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b621f0",
      "incomplete_value": false,
      "site": "00b621f4",
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
            "const:655:8"
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
      "definition_site": "00b63234",
      "incomplete_value": false,
      "site": "00b63238",
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
            "const:77c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62240",
      "incomplete_value": false,
      "site": "00b62244",
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
            "const:69e:8"
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
      "00b6310c",
      "READ",
      [
        "storage",
        "00c9b888",
        null,
        "pointer"
      ]
    ],
    [
      "00b63110",
      "READ",
      [
        "storage",
        "01126128",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ],
    [
      "00b63134",
      "WRITE",
      [
        "storage",
        "01126128",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6310c",
      "READ",
      [
        "storage",
        "00c9c858",
        null,
        "pointer"
      ]
    ],
    [
      "00b63110",
      "READ",
      [
        "storage",
        "011270e8",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ],
    [
      "00b63134",
      "WRITE",
      [
        "storage",
        "011270e8",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b621f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b620e4.md#insn-00b621f4) · [`00b62244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b620e4.md#insn-00b62244) · [`00b6210c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b620e4.md#insn-00b6210c)
- 新版 [`00b631e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b630d8.md#insn-00b631e8) · [`00b63238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b630d8.md#insn-00b63238) · [`00b63100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b630d8.md#insn-00b63100)

~~~diff
- 00b621f4 ["INT_ADD", "register:40f0:8", ["const:b621f4:8", "const:4:8"]]
- 00b621f4 ["CALL", null, ["callee:00c5be80:8"]]
+ 00b631e8 ["INT_ADD", "register:40f0:8", ["const:b631e8:8", "const:4:8"]]
+ 00b631e8 ["CALL", null, ["callee:00c5be80:8"]]
- 00b621f4 bytes 2fe30394
+ 00b631e8 bytes 26e30394
- 00b62244 ["INT_ADD", "register:40f0:8", ["const:b62244:8", "const:4:8"]]
- 00b62244 ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00b63238 ["INT_ADD", "register:40f0:8", ["const:b63238:8", "const:4:8"]]
+ 00b63238 ["CALL", null, ["callee:00c5c1d0:8"]]
- 00b62244 bytes efe30394
+ 00b63238 bytes e6e30394
- 00b6210c ["COPY", "register:40c8:8", ["const:c9b000:8"]]
+ 00b63100 ["COPY", "register:40c8:8", ["const:c9c000:8"]]
- 00b6210c bytes d90900b0
+ 00b63100 bytes d90900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4319627192b8babf368c30d6ceb97b51"></a>

### [`00b6284c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b6284c.md) → [`00b63840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63840.md) _ZN8firebase19CreateApiIdentifierEPKcPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5be30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be30.md) · 呼出先 2件 [`00b628ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b628ec.md) [`00c586c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586c0.md)
- 新版 呼出元 1件 [`00c5ce00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce00.md) · 呼出先 2件 [`00b638e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b638e0.md) [`00c59690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59690.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6388c",
      "incomplete_value": true,
      "site": "00b6388c",
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
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62898",
      "incomplete_value": true,
      "site": "00b62898",
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
            "const:148:8"
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
      "00b6385c",
      "READ",
      [
        "storage",
        "01126148",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6388c",
      "WRITE",
      [
        "storage",
        "01126148",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b6385c",
      "READ",
      [
        "storage",
        "01127108",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6388c",
      "WRITE",
      [
        "storage",
        "01127108",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b6284c.md#insn-00b62898) · [`00b62864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b6284c.md#insn-00b62864) · [`00b62868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b6284c.md#insn-00b62868)
- 新版 [`00b6388c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63840.md#insn-00b6388c) · [`00b63858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63840.md#insn-00b63858) · [`00b6385c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63840.md#insn-00b6385c)

~~~diff
- 00b62898 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
- 00b62898 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b6388c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:108:8"]]
+ 00b6388c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b62898 bytes 094901b9
+ 00b6388c bytes 090901b9
- 00b62864 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b63858 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b62864 bytes 282e0090
+ 00b63858 bytes 282e0090
- 00b62868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
- 00b62868 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b62868 ["INT_ZEXT", "register:40b0:8", ["tmp:1:4"]]
+ 00b6385c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:108:8"]]
+ 00b6385c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00b6385c ["INT_ZEXT", "register:40b0:8", ["tmp:1:4"]]
- 00b62868 bytes 164941b9
+ 00b6385c bytes 160941b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ef28354c28d00df8c5dbefb07580a08"></a>

### [`00b628ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b628ec.md) → [`00b638e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b638e0.md) FUN_00b638e0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b6284c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b6284c.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5be90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be90.md)
- 新版 呼出元 1件 [`00b63840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63840.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5ce60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63948",
      "incomplete_value": false,
      "site": "00b6395c",
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
            "const:a25:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62954",
      "incomplete_value": false,
      "site": "00b62968",
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
            "const:9e5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 5
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b63948",
      "PARAM",
      [
        "storage",
        "0029f9e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b63948",
      "PARAM",
      [
        "storage",
        "0029fa25",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b628ec.md#insn-00b62968) · [`00b62954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b628ec.md#insn-00b62954) · [`00b6298c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b628ec.md#insn-00b6298c)
- 新版 [`00b6395c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b638e0.md#insn-00b6395c) · [`00b63948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b638e0.md#insn-00b63948) · [`00b63980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b638e0.md#insn-00b63980)

~~~diff
- 00b62968 ["INT_ADD", "register:40f0:8", ["const:b62968:8", "const:4:8"]]
- 00b62968 ["CALL", null, ["callee:00c5ce60:8"]]
+ 00b6395c ["INT_ADD", "register:40f0:8", ["const:b6395c:8", "const:4:8"]]
+ 00b6395c ["CALL", null, ["callee:00c5ce60:8"]]
- 00b62968 bytes 4ae50394
+ 00b6395c bytes 41e50394
- 00b62954 ["COPY", "tmp:0:8", ["const:9e5:8"]]
- 00b62954 ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
- 00b62954 ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
- 00b62954 ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
+ 00b63948 ["COPY", "tmp:0:8", ["const:a25:8"]]
+ 00b63948 ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
+ 00b63948 ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
+ 00b63948 ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
- 00b62954 bytes 84942791
+ 00b63948 bytes 84942891
- 00b6298c ["INT_ADD", "register:40f0:8", ["const:b6298c:8", "const:4:8"]]
- 00b6298c ["CALL", null, ["callee:00c58f80:8"]]
+ 00b63980 ["INT_ADD", "register:40f0:8", ["const:b63980:8", "const:4:8"]]
+ 00b63980 ["CALL", null, ["callee:00c58f80:8"]]
- 00b6298c bytes 89d50394
+ 00b63980 bytes 80d50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ab0afd57b04e5c75a0a032f3ee0f159"></a>

### [`00b629b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b629b4.md) → [`00b639a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b639a8.md) FUN_00b639a8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b617f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b617f0.md) · 呼出先 12件 [`00b617f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b617f0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00b627e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b627e4.md) · 呼出先 12件 [`00b627e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b627e4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63a38",
      "incomplete_value": false,
      "site": "00b63a3c",
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
            "const:23c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62a44",
      "incomplete_value": false,
      "site": "00b62a48",
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
            "const:16f:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63a6c",
      "incomplete_value": false,
      "site": "00b63a70",
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
            "const:40a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62a78",
      "incomplete_value": false,
      "site": "00b62a7c",
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
            "const:333:8"
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
      "definition_site": "00b63a98",
      "incomplete_value": false,
      "site": "00b63aac",
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
            "const:a34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62aa4",
      "incomplete_value": false,
      "site": "00b62ab8",
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
            "const:9f4:8"
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
      "00b63a38",
      "PARAM",
      [
        "storage",
        "002ae16f",
        null,
        "string"
      ]
    ],
    [
      "00b63a6c",
      "PARAM",
      [
        "storage",
        "002af333",
        null,
        "string"
      ]
    ],
    [
      "00b63a98",
      "PARAM",
      [
        "storage",
        "0029f9f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b63a38",
      "PARAM",
      [
        "storage",
        "002ae23c",
        null,
        "string"
      ]
    ],
    [
      "00b63a6c",
      "PARAM",
      [
        "storage",
        "002af40a",
        null,
        "string"
      ]
    ],
    [
      "00b63a98",
      "PARAM",
      [
        "storage",
        "0029fa34",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b629b4.md#insn-00b62a48) · [`00b62a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b629b4.md#insn-00b62a7c) · [`00b62ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b629b4.md#insn-00b62ab8)
- 新版 [`00b63a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b639a8.md#insn-00b63a3c) · [`00b63a70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b639a8.md#insn-00b63a70) · [`00b63aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b639a8.md#insn-00b63aac)

~~~diff
- 00b62a48 ["INT_ADD", "register:40f0:8", ["const:b62a48:8", "const:4:8"]]
- 00b62a48 ["CALL", null, ["callee:00c5c080:8"]]
+ 00b63a3c ["INT_ADD", "register:40f0:8", ["const:b63a3c:8", "const:4:8"]]
+ 00b63a3c ["CALL", null, ["callee:00c5c080:8"]]
- 00b62a48 bytes 9ae10394
+ 00b63a3c bytes 91e10394
- 00b62a7c ["INT_ADD", "register:40f0:8", ["const:b62a7c:8", "const:4:8"]]
- 00b62a7c ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b63a70 ["INT_ADD", "register:40f0:8", ["const:b63a70:8", "const:4:8"]]
+ 00b63a70 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b62a7c bytes bde00394
+ 00b63a70 bytes b4e00394
- 00b62ab8 ["INT_ADD", "register:40f0:8", ["const:b62ab8:8", "const:4:8"]]
- 00b62ab8 ["CALL", null, ["callee:00c5be40:8"]]
+ 00b63aac ["INT_ADD", "register:40f0:8", ["const:b63aac:8", "const:4:8"]]
+ 00b63aac ["CALL", null, ["callee:00c5be40:8"]]
- 00b62ab8 bytes eee00394
+ 00b63aac bytes e5e00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c5ac4ffbca5fc8f58ebd7c78e92b51b"></a>

### [`00b62fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62fdc.md) → [`00b63fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63fd0.md) _ZN8firebase7VariantaSERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md) · 呼出先 11件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5b990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b990.md) · 呼出先 11件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 82.30% / 新版 82.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b64044",
      "incomplete_value": false,
      "site": "00b64048",
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
            "const:26c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63050",
      "incomplete_value": false,
      "site": "00b63054",
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
            "const:19f:8"
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
      "definition_site": "00b64060",
      "incomplete_value": false,
      "site": "00b6406c",
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
            "const:432:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6306c",
      "incomplete_value": false,
      "site": "00b63078",
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
            "const:35b:8"
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
      "definition_site": "00b64068",
      "incomplete_value": false,
      "site": "00b6406c",
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
            "const:8df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63074",
      "incomplete_value": false,
      "site": "00b63078",
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
            "const:801:8"
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
      "00b64028",
      "DATA",
      [
        "storage",
        "0030bc49",
        "switchD_00b6303c::switchdataD_0030bc49",
        "byte"
      ]
    ],
    [
      "00b64044",
      "PARAM",
      [
        "storage",
        "002ae19f",
        null,
        "string"
      ]
    ],
    [
      "00b64054",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b64028",
      "DATA",
      [
        "storage",
        "0030bc89",
        "switchD_00b64030::switchdataD_0030bc89",
        "byte"
      ]
    ],
    [
      "00b64044",
      "PARAM",
      [
        "storage",
        "002ae26c",
        null,
        "string"
      ]
    ],
    [
      "00b64054",
      "READ",
      [
        "storage",
        "00c9c890",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62fdc.md#insn-00b63054) · [`00b63078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62fdc.md#insn-00b63078) · [`00b630cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62fdc.md#insn-00b630cc)
- 新版 [`00b64048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63fd0.md#insn-00b64048) · [`00b6406c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63fd0.md#insn-00b6406c) · [`00b640c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63fd0.md#insn-00b640c0)

~~~diff
- 00b63054 ["INT_ADD", "register:40f0:8", ["const:b63054:8", "const:4:8"]]
- 00b63054 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b64048 ["INT_ADD", "register:40f0:8", ["const:b64048:8", "const:4:8"]]
+ 00b64048 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b63054 bytes 47df0394
+ 00b64048 bytes 3edf0394
- 00b63078 ["INT_ADD", "register:40f0:8", ["const:b63078:8", "const:4:8"]]
- 00b63078 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b6406c ["INT_ADD", "register:40f0:8", ["const:b6406c:8", "const:4:8"]]
+ 00b6406c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b63078 bytes 16e00394
+ 00b6406c bytes 0de00394
- 00b630cc ["INT_ADD", "register:40f0:8", ["const:b630cc:8", "const:4:8"]]
- 00b630cc ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b640c0 ["INT_ADD", "register:40f0:8", ["const:b640c0:8", "const:4:8"]]
+ 00b640c0 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b630cc bytes 29df0394
+ 00b640c0 bytes 20df0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-342b6a0e5f918543063741936026fec0"></a>

### [`00b63320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63320.md) → [`00b64314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64314.md) _ZN8firebase7Variant5ClearENS0_4TypeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b63320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63320.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) · 呼出先 6件 [`00b63320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63320.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md)
- 新版 呼出元 2件 [`00b64314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64314.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) · 呼出先 6件 [`00b64314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64314.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5cec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cec0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.14% / 新版 93.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b64570",
      "incomplete_value": false,
      "site": "00b64574",
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
            "const:4e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6357c",
      "incomplete_value": false,
      "site": "00b63580",
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
            "const:38e:8"
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
      "definition_site": "00b6444c",
      "incomplete_value": false,
      "site": "00b64450",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63458",
      "incomplete_value": false,
      "site": "00b6345c",
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
            "const:de0:8"
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
      "00b6434c",
      "DATA",
      [
        "storage",
        "0030bc54",
        "switchD_00b63360::switchdataD_0030bc54",
        "byte"
      ]
    ],
    [
      "00b6444c",
      "PARAM",
      [
        "storage",
        "0029ede0",
        null,
        "string"
      ]
    ],
    [
      "00b6450c",
      "DATA",
      [
        "storage",
        "0030bc5f",
        "switchD_00b63520::switchdataD_0030bc5f",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b6434c",
      "DATA",
      [
        "storage",
        "0030bc94",
        "switchD_00b64354::switchdataD_0030bc94",
        "byte"
      ]
    ],
    [
      "00b6444c",
      "PARAM",
      [
        "storage",
        "0029ee20",
        null,
        "string"
      ]
    ],
    [
      "00b6450c",
      "DATA",
      [
        "storage",
        "0030bc9f",
        "switchD_00b64514::switchdataD_0030bc9f",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6345c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63320.md#insn-00b6345c) · [`00b63350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63320.md#insn-00b63350) · [`00b63354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63320.md#insn-00b63354)
- 新版 [`00b64450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64314.md#insn-00b64450) · [`00b64344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64314.md#insn-00b64344)

~~~diff
- 00b6345c ["INT_ADD", "register:40f0:8", ["const:b6345c:8", "const:4:8"]]
- 00b6345c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b64450 ["INT_ADD", "register:40f0:8", ["const:b64450:8", "const:4:8"]]
+ 00b64450 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b6345c bytes 1ddf0394
+ 00b64450 bytes 14df0394
- 00b63350 ["COPY", "tmp:0:8", ["const:c54:8"]]
- 00b63350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b63350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b63350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b64344 ["COPY", "tmp:0:8", ["const:c94:8"]]
+ 00b64344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b64344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b64344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b63350 bytes 08513191
+ 00b64344 bytes 08513291
- 00b63354 ["COPY", "register:4050:8", ["const:b63364:8"]]
- 00b63354 bytes 8a000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6110bb05abdf3f91640d5d67eaf33939"></a>

### [`00b635dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b635dc.md) → [`00b645d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b645d0.md) _ZNK8firebase7Variant14mutable_stringEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5beb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5beb0.md) · 呼出先 3件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b690.md)
- 新版 呼出元 1件 [`00c5ce80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce80.md) · 呼出先 3件 [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c660.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b64620",
      "incomplete_value": false,
      "site": "00b64624",
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
            "const:6c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6362c",
      "incomplete_value": false,
      "site": "00b63630",
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
            "const:5eb:8"
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
      "definition_site": "00b64630",
      "incomplete_value": false,
      "site": "00b64638",
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
            "const:8e5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6363c",
      "incomplete_value": false,
      "site": "00b63644",
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
            "const:807:8"
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
      "definition_site": "00b6467c",
      "incomplete_value": false,
      "site": "00b64680",
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
            "const:6c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63688",
      "incomplete_value": false,
      "site": "00b6368c",
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
            "const:5eb:8"
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
      "00b645ec",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b64620",
      "PARAM",
      [
        "storage",
        "002be5eb",
        null,
        "string"
      ]
    ],
    [
      "00b64630",
      "PARAM",
      [
        "storage",
        "002bf807",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b645ec",
      "READ",
      [
        "storage",
        "00c9c890",
        null,
        "pointer"
      ]
    ],
    [
      "00b64620",
      "PARAM",
      [
        "storage",
        "002be6c9",
        null,
        "string"
      ]
    ],
    [
      "00b64630",
      "PARAM",
      [
        "storage",
        "002bf8e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b635dc.md#insn-00b63630) · [`00b63644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b635dc.md#insn-00b63644) · [`00b6368c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b635dc.md#insn-00b6368c)
- 新版 [`00b64624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b645d0.md#insn-00b64624) · [`00b64638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b645d0.md#insn-00b64638) · [`00b64680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b645d0.md#insn-00b64680)

~~~diff
- 00b63630 ["INT_ADD", "register:40f0:8", ["const:b63630:8", "const:4:8"]]
- 00b63630 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b64624 ["INT_ADD", "register:40f0:8", ["const:b64624:8", "const:4:8"]]
+ 00b64624 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b63630 bytes d0dd0394
+ 00b64624 bytes c7dd0394
- 00b63644 ["INT_ADD", "register:40f0:8", ["const:b63644:8", "const:4:8"]]
- 00b63644 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b64638 ["INT_ADD", "register:40f0:8", ["const:b64638:8", "const:4:8"]]
+ 00b64638 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b63644 bytes a3de0394
+ 00b64638 bytes 9ade0394
- 00b6368c ["INT_ADD", "register:40f0:8", ["const:b6368c:8", "const:4:8"]]
- 00b6368c ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b64680 ["INT_ADD", "register:40f0:8", ["const:b64680:8", "const:4:8"]]
+ 00b64680 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b6368c bytes b9dd0394
+ 00b64680 bytes b0dd0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc32816510e7ea955fc9a022f351b994"></a>

### [`00b636dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b636dc.md) → [`00b646d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b646d0.md) _ZN8firebase7Variant16set_mutable_blobEPKvm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5bea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bea0.md) · 呼出先 5件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5bf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf20.md)
- 新版 呼出元 1件 [`00c5ce70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce70.md) · 呼出先 5件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5cef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6472c",
      "incomplete_value": false,
      "site": "00b64730",
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
            "const:ed2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63738",
      "incomplete_value": false,
      "site": "00b6373c",
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
            "const:df4:8"
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
      "definition_site": "00b64744",
      "incomplete_value": false,
      "site": "00b6474c",
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
            "const:2b1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63750",
      "incomplete_value": false,
      "site": "00b63758",
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
            "const:159:8"
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
      "definition_site": "00b64748",
      "incomplete_value": true,
      "site": "00b6474c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63754",
      "incomplete_value": true,
      "site": "00b63758",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b6472c",
      "PARAM",
      [
        "storage",
        "002bbdf4",
        null,
        "string"
      ]
    ],
    [
      "00b6473c",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b64744",
      "PARAM",
      [
        "storage",
        "002a7159",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6472c",
      "PARAM",
      [
        "storage",
        "002bbed2",
        null,
        "string"
      ]
    ],
    [
      "00b6473c",
      "READ",
      [
        "storage",
        "00c9c890",
        null,
        "pointer"
      ]
    ],
    [
      "00b64744",
      "PARAM",
      [
        "storage",
        "002a72b1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6373c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b636dc.md#insn-00b6373c) · [`00b63758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b636dc.md#insn-00b63758) · [`00b636fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b636dc.md#insn-00b636fc)
- 新版 [`00b64730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b646d0.md#insn-00b64730) · [`00b6474c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b646d0.md#insn-00b6474c) · [`00b646f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b646d0.md#insn-00b646f0)

~~~diff
- 00b6373c ["INT_ADD", "register:40f0:8", ["const:b6373c:8", "const:4:8"]]
- 00b6373c ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b64730 ["INT_ADD", "register:40f0:8", ["const:b64730:8", "const:4:8"]]
+ 00b64730 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b6373c bytes 8ddd0394
+ 00b64730 bytes 84dd0394
- 00b63758 ["INT_ADD", "register:40f0:8", ["const:b63758:8", "const:4:8"]]
- 00b63758 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b6474c ["INT_ADD", "register:40f0:8", ["const:b6474c:8", "const:4:8"]]
+ 00b6474c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b63758 bytes 5ede0394
+ 00b6474c bytes 55de0394
- 00b636fc ["INT_ADD", "register:40f0:8", ["const:b636fc:8", "const:4:8"]]
- 00b636fc ["CALL", null, ["callee:00c5cef0:8"]]
+ 00b646f0 ["INT_ADD", "register:40f0:8", ["const:b646f0:8", "const:4:8"]]
+ 00b646f0 ["CALL", null, ["callee:00c5cef0:8"]]
- 00b636fc bytes 09e20394
+ 00b646f0 bytes 00e20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-839167bec5f786911d10d8055a059ee2"></a>

### [`00b63770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63770.md) → [`00b64764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64764.md) _ZN8firebase7VariantaSEOS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) · 呼出先 3件 [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md) · 呼出先 3件 [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b64810",
      "incomplete_value": false,
      "site": "00b64814",
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
            "const:ed2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6381c",
      "incomplete_value": false,
      "site": "00b63820",
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
            "const:df4:8"
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
      "definition_site": "00b64828",
      "incomplete_value": false,
      "site": "00b64830",
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
            "const:2b1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63834",
      "incomplete_value": false,
      "site": "00b6383c",
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
            "const:159:8"
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
      "definition_site": "00b6482c",
      "incomplete_value": true,
      "site": "00b64830",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63838",
      "incomplete_value": true,
      "site": "00b6383c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b647b8",
      "DATA",
      [
        "storage",
        "0030bc6a",
        "switchD_00b637cc::switchdataD_0030bc6a",
        "byte"
      ]
    ],
    [
      "00b64810",
      "PARAM",
      [
        "storage",
        "002bbdf4",
        null,
        "string"
      ]
    ],
    [
      "00b64820",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b647b8",
      "DATA",
      [
        "storage",
        "0030bcaa",
        "switchD_00b647c0::switchdataD_0030bcaa",
        "byte"
      ]
    ],
    [
      "00b64810",
      "PARAM",
      [
        "storage",
        "002bbed2",
        null,
        "string"
      ]
    ],
    [
      "00b64820",
      "READ",
      [
        "storage",
        "00c9c890",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63770.md#insn-00b63820) · [`00b6383c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63770.md#insn-00b6383c) · [`00b63870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63770.md#insn-00b63870)
- 新版 [`00b64814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64764.md#insn-00b64814) · [`00b64830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64764.md#insn-00b64830) · [`00b64864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64764.md#insn-00b64864)

~~~diff
- 00b63820 ["INT_ADD", "register:40f0:8", ["const:b63820:8", "const:4:8"]]
- 00b63820 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b64814 ["INT_ADD", "register:40f0:8", ["const:b64814:8", "const:4:8"]]
+ 00b64814 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b63820 bytes 54dd0394
+ 00b64814 bytes 4bdd0394
- 00b6383c ["INT_ADD", "register:40f0:8", ["const:b6383c:8", "const:4:8"]]
- 00b6383c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b64830 ["INT_ADD", "register:40f0:8", ["const:b64830:8", "const:4:8"]]
+ 00b64830 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b6383c bytes 25de0394
+ 00b64830 bytes 1cde0394
- 00b63870 ["INT_ADD", "register:40f0:8", ["const:b63870:8", "const:4:8"]]
- 00b63870 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b64864 ["INT_ADD", "register:40f0:8", ["const:b64864:8", "const:4:8"]]
+ 00b64864 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b63870 bytes 18de0394
+ 00b64864 bytes 0fde0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b0dd17e0774123276f3e7b83b95504b"></a>

### [`00b63888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63888.md) → [`00b6487c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b6487c.md) _ZNK8firebase7VarianteqERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b63888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63888.md) [`00c5bec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bec0.md) · 呼出先 5件 [`00b63888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63888.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 2件 [`00b6487c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b6487c.md) [`00c5ce90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce90.md) · 呼出先 5件 [`00b6487c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b6487c.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.33% / 新版 84.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 34件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b64984",
      "incomplete_value": false,
      "site": "00b64988",
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
            "const:ed2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63990",
      "incomplete_value": false,
      "site": "00b63994",
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
            "const:df4:8"
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
      "definition_site": "00b64994",
      "incomplete_value": false,
      "site": "00b6499c",
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
            "const:2b1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b639a0",
      "incomplete_value": false,
      "site": "00b639a8",
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
            "const:159:8"
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
      "definition_site": "00b649b8",
      "incomplete_value": false,
      "site": "00b649bc",
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
            "const:ed2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b639c4",
      "incomplete_value": false,
      "site": "00b639c8",
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
            "const:df4:8"
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
      "00b64914",
      "DATA",
      [
        "storage",
        "0030bc75",
        "switchD_00b6392c::switchdataD_0030bc75",
        "byte"
      ]
    ],
    [
      "00b64970",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b64984",
      "PARAM",
      [
        "storage",
        "002bbdf4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b64914",
      "DATA",
      [
        "storage",
        "0030bcb5",
        "switchD_00b64920::switchdataD_0030bcb5",
        "byte"
      ]
    ],
    [
      "00b64970",
      "READ",
      [
        "storage",
        "00c9c890",
        null,
        "pointer"
      ]
    ],
    [
      "00b64984",
      "PARAM",
      [
        "storage",
        "002bbed2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63888.md#insn-00b63994) · [`00b639a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63888.md#insn-00b639a8) · [`00b639c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63888.md#insn-00b639c8)
- 新版 [`00b64988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b6487c.md#insn-00b64988) · [`00b6499c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b6487c.md#insn-00b6499c) · [`00b649bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b6487c.md#insn-00b649bc)

~~~diff
- 00b63994 ["INT_ADD", "register:40f0:8", ["const:b63994:8", "const:4:8"]]
- 00b63994 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b64988 ["INT_ADD", "register:40f0:8", ["const:b64988:8", "const:4:8"]]
+ 00b64988 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b63994 bytes f7dc0394
+ 00b64988 bytes eedc0394
- 00b639a8 ["INT_ADD", "register:40f0:8", ["const:b639a8:8", "const:4:8"]]
- 00b639a8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b6499c ["INT_ADD", "register:40f0:8", ["const:b6499c:8", "const:4:8"]]
+ 00b6499c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b639a8 bytes cadd0394
+ 00b6499c bytes c1dd0394
- 00b639c8 ["INT_ADD", "register:40f0:8", ["const:b639c8:8", "const:4:8"]]
- 00b639c8 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b649bc ["INT_ADD", "register:40f0:8", ["const:b649bc:8", "const:4:8"]]
+ 00b649bc ["CALL", null, ["callee:00c5bd40:8"]]
- 00b639c8 bytes eadc0394
+ 00b649bc bytes e1dc0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b852f20ab2380fbc7c891c9471b96e3d"></a>

### [`00b63e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63e04.md) → [`00b64df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64df8.md) _ZNK8firebase7VariantltERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5b670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b670.md) · 呼出先 5件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md) [`00c5bec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bec0.md)
- 新版 呼出元 1件 [`00c5c640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c640.md) · 呼出先 5件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md) [`00c5ce90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.20% / 新版 87.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 46件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b64fbc",
      "incomplete_value": false,
      "site": "00b64fc4",
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
            "const:2ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63fc8",
      "incomplete_value": false,
      "site": "00b63fd0",
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
            "const:155:8"
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
      "definition_site": "00b64ff0",
      "incomplete_value": false,
      "site": "00b64ff8",
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
            "const:2ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63ffc",
      "incomplete_value": false,
      "site": "00b64004",
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
            "const:155:8"
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
      "definition_site": "00b6502c",
      "incomplete_value": false,
      "site": "00b65034",
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
            "const:2ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64038",
      "incomplete_value": false,
      "site": "00b64040",
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
            "const:155:8"
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
      "00b64e1c",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b64ecc",
      "DATA",
      [
        "storage",
        "0030bc82",
        "switchD_00b63ee0::switchdataD_0030bc82",
        "ushort"
      ]
    ],
    [
      "00b64ee8",
      "PARAM",
      [
        "storage",
        "002ae19f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b64e1c",
      "READ",
      [
        "storage",
        "00c9c890",
        null,
        "pointer"
      ]
    ],
    [
      "00b64ecc",
      "DATA",
      [
        "storage",
        "0030bcc2",
        "switchD_00b64ed4::switchdataD_0030bcc2",
        "ushort"
      ]
    ],
    [
      "00b64ee8",
      "PARAM",
      [
        "storage",
        "002ae26c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63e04.md#insn-00b63fd0) · [`00b64004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63e04.md#insn-00b64004) · [`00b64040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63e04.md#insn-00b64040)
- 新版 [`00b64fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64df8.md#insn-00b64fc4) · [`00b64ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64df8.md#insn-00b64ff8) · [`00b65034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b64/00b64df8.md#insn-00b65034)

~~~diff
- 00b63fd0 ["INT_ADD", "register:40f0:8", ["const:b63fd0:8", "const:4:8"]]
- 00b63fd0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b64fc4 ["INT_ADD", "register:40f0:8", ["const:b64fc4:8", "const:4:8"]]
+ 00b64fc4 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b63fd0 bytes 40dc0394
+ 00b64fc4 bytes 37dc0394
- 00b64004 ["INT_ADD", "register:40f0:8", ["const:b64004:8", "const:4:8"]]
- 00b64004 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b64ff8 ["INT_ADD", "register:40f0:8", ["const:b64ff8:8", "const:4:8"]]
+ 00b64ff8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b64004 bytes 33dc0394
+ 00b64ff8 bytes 2adc0394
- 00b64040 ["INT_ADD", "register:40f0:8", ["const:b64040:8", "const:4:8"]]
- 00b64040 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b65034 ["INT_ADD", "register:40f0:8", ["const:b65034:8", "const:4:8"]]
+ 00b65034 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b64040 bytes 24dc0394
+ 00b65034 bytes 1bdc0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2023fb51348c0c8c6dcb60bb918afefd"></a>

### [`00b64670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64670.md) → [`00b65664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65664.md) _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5abd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abd0.md) · 呼出先 2件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5bba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bba0.md) · 呼出先 2件 [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65690",
      "incomplete_value": false,
      "site": "00b65698",
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
            "const:26c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6469c",
      "incomplete_value": false,
      "site": "00b646a4",
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
            "const:19f:8"
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
      "00b65690",
      "PARAM",
      [
        "storage",
        "002ae19f",
        null,
        "string"
      ]
    ],
    [
      "00b656a4",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b656b0",
      "PARAM",
      [
        "storage",
        "002af35b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65690",
      "PARAM",
      [
        "storage",
        "002ae26c",
        null,
        "string"
      ]
    ],
    [
      "00b656a4",
      "READ",
      [
        "storage",
        "00c9c890",
        null,
        "pointer"
      ]
    ],
    [
      "00b656b0",
      "PARAM",
      [
        "storage",
        "002af432",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b646a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64670.md#insn-00b646a4) · [`00b6469c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64670.md#insn-00b6469c) · [`00b646a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64670.md#insn-00b646a8)
- 新版 [`00b65698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65664.md#insn-00b65698) · [`00b65690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65664.md#insn-00b65690) · [`00b6569c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65664.md#insn-00b6569c)

~~~diff
- 00b646a4 ["INT_ADD", "register:40f0:8", ["const:b646a4:8", "const:4:8"]]
- 00b646a4 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b65698 ["INT_ADD", "register:40f0:8", ["const:b65698:8", "const:4:8"]]
+ 00b65698 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b646a4 bytes b3d90394
+ 00b65698 bytes aad90394
- 00b6469c ["COPY", "tmp:0:8", ["const:19f:8"]]
- 00b6469c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6469c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6469c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65690 ["COPY", "tmp:0:8", ["const:26c:8"]]
+ 00b65690 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65690 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65690 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6469c bytes 007c0691
+ 00b65690 bytes 00b00991
- 00b646a8 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00b6569c ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00b646a8 bytes a90900f0
+ 00b6569c bytes a90900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd8e0e1e81c06861ed648c5c7de9ce0"></a>

### [`00b646d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b646d0.md) → [`00b656c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b656c4.md) _ZNK8firebase7Variant18assert_is_not_typeENS0_4TypeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b656ec",
      "incomplete_value": false,
      "site": "00b656f4",
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
            "const:26c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b646f8",
      "incomplete_value": false,
      "site": "00b64700",
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
            "const:19f:8"
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
      "00b656ec",
      "PARAM",
      [
        "storage",
        "002ae19f",
        null,
        "string"
      ]
    ],
    [
      "00b656fc",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b65708",
      "PARAM",
      [
        "storage",
        "002a95e9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b656ec",
      "PARAM",
      [
        "storage",
        "002ae26c",
        null,
        "string"
      ]
    ],
    [
      "00b656fc",
      "READ",
      [
        "storage",
        "00c9c890",
        null,
        "pointer"
      ]
    ],
    [
      "00b65708",
      "PARAM",
      [
        "storage",
        "002a96b6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b646d0.md#insn-00b64700) · [`00b646f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b646d0.md#insn-00b646f8) · [`00b64704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b646d0.md#insn-00b64704)
- 新版 [`00b656f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b656c4.md#insn-00b656f4) · [`00b656ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b656c4.md#insn-00b656ec) · [`00b656f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b656c4.md#insn-00b656f8)

~~~diff
- 00b64700 ["INT_ADD", "register:40f0:8", ["const:b64700:8", "const:4:8"]]
- 00b64700 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b656f4 ["INT_ADD", "register:40f0:8", ["const:b656f4:8", "const:4:8"]]
+ 00b656f4 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b64700 bytes 9cd90394
+ 00b656f4 bytes 93d90394
- 00b646f8 ["COPY", "tmp:0:8", ["const:19f:8"]]
- 00b646f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b646f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b646f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b656ec ["COPY", "tmp:0:8", ["const:26c:8"]]
+ 00b656ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b656ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b656ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b646f8 bytes 007c0691
+ 00b656ec bytes 00b00991
- 00b64704 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b656f8 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b64704 bytes a80900f0
+ 00b656f8 bytes a80900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eecf6a4ac893d6d865f2436347aac9c"></a>

### [`00b64724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64724.md) → [`00b65718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65718.md) _ZNK8firebase7Variant16assert_is_stringEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5abf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abf0.md) · 呼出先 2件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5bbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bbc0.md) · 呼出先 2件 [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65758",
      "incomplete_value": false,
      "site": "00b6575c",
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
            "const:6c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64764",
      "incomplete_value": false,
      "site": "00b64768",
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
            "const:5eb:8"
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
      "00b65758",
      "PARAM",
      [
        "storage",
        "002be5eb",
        null,
        "string"
      ]
    ],
    [
      "00b65768",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b65774",
      "PARAM",
      [
        "storage",
        "002bf807",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65758",
      "PARAM",
      [
        "storage",
        "002be6c9",
        null,
        "string"
      ]
    ],
    [
      "00b65768",
      "READ",
      [
        "storage",
        "00c9c890",
        null,
        "pointer"
      ]
    ],
    [
      "00b65774",
      "PARAM",
      [
        "storage",
        "002bf8e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64724.md#insn-00b64768) · [`00b64764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64724.md#insn-00b64764) · [`00b6476c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64724.md#insn-00b6476c)
- 新版 [`00b6575c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65718.md#insn-00b6575c) · [`00b65758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65718.md#insn-00b65758) · [`00b65760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65718.md#insn-00b65760)

~~~diff
- 00b64768 ["INT_ADD", "register:40f0:8", ["const:b64768:8", "const:4:8"]]
- 00b64768 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b6575c ["INT_ADD", "register:40f0:8", ["const:b6575c:8", "const:4:8"]]
+ 00b6575c ["CALL", null, ["callee:00c5bd40:8"]]
- 00b64768 bytes 82d90394
+ 00b6575c bytes 79d90394
- 00b64764 ["COPY", "tmp:0:8", ["const:5eb:8"]]
- 00b64764 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b64764 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b64764 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65758 ["COPY", "tmp:0:8", ["const:6c9:8"]]
+ 00b65758 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65758 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65758 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b64764 bytes 00ac1791
+ 00b65758 bytes 00241b91
- 00b6476c ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00b65760 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00b6476c bytes a90900f0
+ 00b65760 bytes a90900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3644c93077bb50861a2d6d1acf0d3cb5"></a>

### [`00b64790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64790.md) → [`00b65784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65784.md) _ZNK8firebase7Variant14assert_is_blobEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5b660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b660.md) · 呼出先 2件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c630.md) · 呼出先 2件 [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b657b4",
      "incomplete_value": false,
      "site": "00b657b8",
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
            "const:ed2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b647c0",
      "incomplete_value": false,
      "site": "00b647c4",
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
            "const:df4:8"
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
      "00b657b4",
      "PARAM",
      [
        "storage",
        "002bbdf4",
        null,
        "string"
      ]
    ],
    [
      "00b657c4",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b657d0",
      "PARAM",
      [
        "storage",
        "002a7159",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b657b4",
      "PARAM",
      [
        "storage",
        "002bbed2",
        null,
        "string"
      ]
    ],
    [
      "00b657c4",
      "READ",
      [
        "storage",
        "00c9c890",
        null,
        "pointer"
      ]
    ],
    [
      "00b657d0",
      "PARAM",
      [
        "storage",
        "002a72b1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b647c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64790.md#insn-00b647c4) · [`00b647c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64790.md#insn-00b647c0) · [`00b647c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64790.md#insn-00b647c8)
- 新版 [`00b657b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65784.md#insn-00b657b8) · [`00b657b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65784.md#insn-00b657b4) · [`00b657bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65784.md#insn-00b657bc)

~~~diff
- 00b647c4 ["INT_ADD", "register:40f0:8", ["const:b647c4:8", "const:4:8"]]
- 00b647c4 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b657b8 ["INT_ADD", "register:40f0:8", ["const:b657b8:8", "const:4:8"]]
+ 00b657b8 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b647c4 bytes 6bd90394
+ 00b657b8 bytes 62d90394
- 00b647c0 ["COPY", "tmp:0:8", ["const:df4:8"]]
- 00b647c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b647c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b647c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b657b4 ["COPY", "tmp:0:8", ["const:ed2:8"]]
+ 00b657b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b657b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b657b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b647c0 bytes 00d03791
+ 00b657b4 bytes 00483b91
- 00b647c8 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00b657bc ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00b647c8 bytes a90900f0
+ 00b657bc bytes a90900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2fe8033a5a3d5d961356ad956fd57c1"></a>

### [`00b647ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b647ec.md) → [`00b657e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b657e0.md) _ZNK8firebase7Variant8AsStringEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5abe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abe0.md) · 呼出先 10件 [`00b64990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64990.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`00c5bbb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bbb0.md) · 呼出先 10件 [`00b65984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65984.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65870",
      "incomplete_value": false,
      "site": "00b65878",
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
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6487c",
      "incomplete_value": false,
      "site": "00b64884",
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
            "const:bb:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b658a4",
      "incomplete_value": false,
      "site": "00b658ac",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b648b0",
      "incomplete_value": false,
      "site": "00b648b8",
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
            "const:61b:8"
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
      "00b65824",
      "DATA",
      [
        "storage",
        "0030bc98",
        "switchD_00b6483c::switchdataD_0030bc98",
        "byte"
      ]
    ],
    [
      "00b65870",
      "PARAM",
      [
        "storage",
        "002ad0bb",
        null,
        null
      ]
    ],
    [
      "00b658a4",
      "PARAM",
      [
        "storage",
        "002a961b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65824",
      "DATA",
      [
        "storage",
        "0030bcd8",
        "switchD_00b65830::switchdataD_0030bcd8",
        "byte"
      ]
    ],
    [
      "00b65870",
      "PARAM",
      [
        "storage",
        "002ad188",
        null,
        null
      ]
    ],
    [
      "00b658a4",
      "PARAM",
      [
        "storage",
        "002a96e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b647ec.md#insn-00b64884) · [`00b648b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b647ec.md#insn-00b648b8) · [`00b64828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b647ec.md#insn-00b64828)
- 新版 [`00b65878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b657e0.md#insn-00b65878) · [`00b658ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b657e0.md#insn-00b658ac) · [`00b6581c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b657e0.md#insn-00b6581c)

~~~diff
- 00b64884 ["INT_ADD", "register:40f0:8", ["const:b64884:8", "const:4:8"]]
- 00b64884 ["CALL", null, ["callee:00b65984:8"]]
+ 00b65878 ["INT_ADD", "register:40f0:8", ["const:b65878:8", "const:4:8"]]
+ 00b65878 ["CALL", null, ["callee:00b65984:8"]]
- 00b64884 bytes 43000094
+ 00b65878 bytes 43000094
- 00b648b8 ["INT_ADD", "register:40f0:8", ["const:b648b8:8", "const:4:8"]]
- 00b648b8 ["CALL", null, ["callee:00b65984:8"]]
+ 00b658ac ["INT_ADD", "register:40f0:8", ["const:b658ac:8", "const:4:8"]]
+ 00b658ac ["CALL", null, ["callee:00b65984:8"]]
- 00b648b8 bytes 36000094
+ 00b658ac bytes 36000094
- 00b64828 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00b64828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b64828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b64828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6581c ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00b6581c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6581c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6581c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b64828 bytes 08613291
+ 00b6581c bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-947ab3d85ef6a4e959d11b06c1faca6b"></a>

### [`00b64c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64c14.md) → [`00b65c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65c08.md) _ZNK8firebase7Variant6AsBoolEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5bec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bec0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5ce90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b65d30",
      "incomplete_value": false,
      "site": "00b65d3c",
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
            "const:4e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64d3c",
      "incomplete_value": false,
      "site": "00b64d48",
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
            "const:38e:8"
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
      "definition_site": "00b65dbc",
      "incomplete_value": false,
      "site": "00b65dc8",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64dc8",
      "incomplete_value": false,
      "site": "00b64dd4",
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
            "const:de0:8"
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
      "00b65d3c",
      "DATA",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65dc8",
      "DATA",
      [
        "storage",
        "0029ede0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65d3c",
      "DATA",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65dc8",
      "DATA",
      [
        "storage",
        "0029ee20",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64c14.md#insn-00b64c48) · [`00b64c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64c14.md#insn-00b64c5c) · [`00b64c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64c14.md#insn-00b64c6c)
- 新版 [`00b65c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65c08.md#insn-00b65c3c) · [`00b65c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65c08.md#insn-00b65c50) · [`00b65c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65c08.md#insn-00b65c60)

~~~diff
- 00b64c48 ["INT_ADD", "register:40f0:8", ["const:b64c48:8", "const:4:8"]]
- 00b64c48 ["CALL", null, ["callee:00c5ce90:8"]]
+ 00b65c3c ["INT_ADD", "register:40f0:8", ["const:b65c3c:8", "const:4:8"]]
+ 00b65c3c ["CALL", null, ["callee:00c5ce90:8"]]
- 00b64c48 bytes 9edc0394
+ 00b65c3c bytes 95dc0394
- 00b64c5c ["INT_ADD", "register:40f0:8", ["const:b64c5c:8", "const:4:8"]]
- 00b64c5c ["CALL", null, ["callee:00c5b8d0:8"]]
+ 00b65c50 ["INT_ADD", "register:40f0:8", ["const:b65c50:8", "const:4:8"]]
+ 00b65c50 ["CALL", null, ["callee:00c5b8d0:8"]]
- 00b64c5c bytes 29d70394
+ 00b65c50 bytes 20d70394
- 00b64c6c ["INT_ADD", "register:40f0:8", ["const:b64c6c:8", "const:4:8"]]
- 00b64c6c ["CALL", null, ["callee:00c5ce90:8"]]
+ 00b65c60 ["INT_ADD", "register:40f0:8", ["const:b65c60:8", "const:4:8"]]
+ 00b65c60 ["CALL", null, ["callee:00c5ce90:8"]]
- 00b64c6c bytes 95dc0394
+ 00b65c60 bytes 8cdc0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecef58639aa9a74adeba9768eeb7a892"></a>

### [`00b64e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64e78.md) → [`00b65e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65e6c.md) _ZN8firebase7Variant8TypeNameENS0_4TypeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0c0.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c090.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b65e98",
      "incomplete_value": true,
      "site": "00b65e98",
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
            "const:10c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64ea4",
      "incomplete_value": true,
      "site": "00b64ea4",
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
            "const:14c:8"
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
      "definition_site": "00b65eb0",
      "incomplete_value": false,
      "site": "00b65eb4",
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
            "const:6ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64ebc",
      "incomplete_value": false,
      "site": "00b64ec0",
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
            "const:621:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b65ec4",
      "incomplete_value": true,
      "site": "00b65ecc",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64ed0",
      "incomplete_value": true,
      "site": "00b64ed8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b65e7c",
      "READ",
      [
        "storage",
        "0112614c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65e98",
      "WRITE",
      [
        "storage",
        "0112614c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65eb0",
      "PARAM",
      [
        "storage",
        "002a9621",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65e7c",
      "READ",
      [
        "storage",
        "0112710c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65e98",
      "WRITE",
      [
        "storage",
        "0112710c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65eb0",
      "PARAM",
      [
        "storage",
        "002a96ee",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64e78.md#insn-00b64ea4) · [`00b64ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64e78.md#insn-00b64ec0) · [`00b64e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64e78.md#insn-00b64e84)
- 新版 [`00b65e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65e6c.md#insn-00b65e98) · [`00b65eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65e6c.md#insn-00b65eb4) · [`00b65e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65e6c.md#insn-00b65e78)

~~~diff
- 00b64ea4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b64ea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:14c:8"]]
- 00b64ea4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b65e98 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 00b65e98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:10c:8"]]
+ 00b65e98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b64ea4 bytes 28310539
+ 00b65e98 bytes 28310439
- 00b64ec0 ["INT_ADD", "register:40f0:8", ["const:b64ec0:8", "const:4:8"]]
- 00b64ec0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b65eb4 ["INT_ADD", "register:40f0:8", ["const:b65eb4:8", "const:4:8"]]
+ 00b65eb4 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b64ec0 bytes 84d80394
+ 00b65eb4 bytes 7bd80394
- 00b64e84 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00b65e78 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00b64e84 bytes 092e00d0
+ 00b65e78 bytes 092e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f9f6a40e5dd8768836ce12464d7587f"></a>

### [`00b654f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b654f0.md) → [`00b664e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b664e4.md) _ZN8firebase5MutexC1ENS0_4ModeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md) · 呼出先 6件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5bf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf50.md) [`00c5bf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf60.md) [`00c5bf70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf70.md)
- 新版 呼出元 2件 [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd20.md) · 呼出先 6件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5cf20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf20.md) [`00c5cf30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf30.md) [`00c5cf40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6651c",
      "incomplete_value": false,
      "site": "00b66520",
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
            "const:18c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65528",
      "incomplete_value": false,
      "site": "00b6552c",
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
            "const:bf:8"
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
      "definition_site": "00b6653c",
      "incomplete_value": false,
      "site": "00b66540",
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
            "const:18c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65548",
      "incomplete_value": false,
      "site": "00b6554c",
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
            "const:bf:8"
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
      "definition_site": "00b66558",
      "incomplete_value": false,
      "site": "00b6655c",
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
            "const:18c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65564",
      "incomplete_value": false,
      "site": "00b65568",
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
            "const:bf:8"
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
      "00b6651c",
      "PARAM",
      [
        "storage",
        "002ad0bf",
        null,
        "string"
      ]
    ],
    [
      "00b6653c",
      "PARAM",
      [
        "storage",
        "002ad0bf",
        null,
        "string"
      ]
    ],
    [
      "00b66558",
      "PARAM",
      [
        "storage",
        "002ad0bf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6651c",
      "PARAM",
      [
        "storage",
        "002ad18c",
        null,
        "string"
      ]
    ],
    [
      "00b6653c",
      "PARAM",
      [
        "storage",
        "002ad18c",
        null,
        "string"
      ]
    ],
    [
      "00b66558",
      "PARAM",
      [
        "storage",
        "002ad18c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6552c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b654f0.md#insn-00b6552c) · [`00b6554c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b654f0.md#insn-00b6554c) · [`00b65568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b654f0.md#insn-00b65568)
- 新版 [`00b66520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b664e4.md#insn-00b66520) · [`00b66540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b664e4.md#insn-00b66540) · [`00b6655c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b664e4.md#insn-00b6655c)

~~~diff
- 00b6552c ["INT_ADD", "register:40f0:8", ["const:b6552c:8", "const:4:8"]]
- 00b6552c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b66520 ["INT_ADD", "register:40f0:8", ["const:b66520:8", "const:4:8"]]
+ 00b66520 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b6552c bytes e9d60394
+ 00b66520 bytes e0d60394
- 00b6554c ["INT_ADD", "register:40f0:8", ["const:b6554c:8", "const:4:8"]]
- 00b6554c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b66540 ["INT_ADD", "register:40f0:8", ["const:b66540:8", "const:4:8"]]
+ 00b66540 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b6554c bytes e1d60394
+ 00b66540 bytes d8d60394
- 00b65568 ["INT_ADD", "register:40f0:8", ["const:b65568:8", "const:4:8"]]
- 00b65568 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b6655c ["INT_ADD", "register:40f0:8", ["const:b6655c:8", "const:4:8"]]
+ 00b6655c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b65568 bytes dad60394
+ 00b6655c bytes d1d60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72ca1def9cb6293485bb6cfbc635cefc"></a>

### [`00b6562c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6562c.md) → [`00b66620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66620.md) _ZN8firebase3app19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEENS_4util16Clas

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6664c",
      "incomplete_value": true,
      "site": "00b6664c",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65658",
      "incomplete_value": true,
      "site": "00b65658",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66634",
      "incomplete_value": true,
      "site": "00b66634",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65640",
      "incomplete_value": true,
      "site": "00b65640",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66640",
      "incomplete_value": false,
      "site": "00b66644",
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
            "const:dba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6564c",
      "incomplete_value": false,
      "site": "00b65650",
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
            "const:ceb:8"
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
      "00b66630",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66640",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ],
    [
      "00b6664c",
      "WRITE",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66630",
      "READ",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66640",
      "PARAM",
      [
        "storage",
        "002b6dba",
        null,
        "string"
      ]
    ],
    [
      "00b6664c",
      "WRITE",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6562c.md#insn-00b65650) · [`00b65658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6562c.md#insn-00b65658) · [`00b65638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6562c.md#insn-00b65638)
- 新版 [`00b66644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66620.md#insn-00b66644) · [`00b6664c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66620.md#insn-00b6664c) · [`00b6662c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66620.md#insn-00b6662c)

~~~diff
- 00b65650 ["INT_ADD", "register:40f0:8", ["const:b65650:8", "const:4:8"]]
- 00b65650 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66644 ["INT_ADD", "register:40f0:8", ["const:b66644:8", "const:4:8"]]
+ 00b66644 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65650 bytes 64d60394
+ 00b66644 bytes 5bd60394
- 00b65658 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:150:8"]]
- 00b65658 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6664c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:110:8"]]
+ 00b6664c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65658 bytes 60aa00f9
+ 00b6664c bytes 608a00f9
- 00b65638 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b6662c ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b65638 bytes 132e00b0
+ 00b6662c bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ac8c924edd833bb6d2c4d542fe32474"></a>

### [`00b6566c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6566c.md) → [`00b66660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66660.md) _ZN8firebase3app19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6668c",
      "incomplete_value": true,
      "site": "00b6668c",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65698",
      "incomplete_value": true,
      "site": "00b65698",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66674",
      "incomplete_value": true,
      "site": "00b66674",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65680",
      "incomplete_value": true,
      "site": "00b65680",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b6667c",
      "incomplete_value": false,
      "site": "00b66684",
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
            "const:dba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65688",
      "incomplete_value": false,
      "site": "00b65690",
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
            "const:ceb:8"
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
      "00b66670",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6667c",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ],
    [
      "00b6668c",
      "WRITE",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66670",
      "READ",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6667c",
      "PARAM",
      [
        "storage",
        "002b6dba",
        null,
        "string"
      ]
    ],
    [
      "00b6668c",
      "WRITE",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6566c.md#insn-00b65690) · [`00b65698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6566c.md#insn-00b65698) · [`00b65678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6566c.md#insn-00b65678)
- 新版 [`00b66684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66660.md#insn-00b66684) · [`00b6668c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66660.md#insn-00b6668c) · [`00b6666c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66660.md#insn-00b6666c)

~~~diff
- 00b65690 ["INT_ADD", "register:40f0:8", ["const:b65690:8", "const:4:8"]]
- 00b65690 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66684 ["INT_ADD", "register:40f0:8", ["const:b66684:8", "const:4:8"]]
+ 00b66684 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65690 bytes 54d60394
+ 00b66684 bytes 4bd60394
- 00b65698 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:150:8"]]
- 00b65698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6668c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:110:8"]]
+ 00b6668c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65698 bytes 60aa00f9
+ 00b6668c bytes 608a00f9
- 00b65678 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b6666c ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b65678 bytes 132e00b0
+ 00b6666c bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-145325287a21b0afafa8b73bd880f778"></a>

### [`00b656ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b656ac.md) → [`00b666a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b666a0.md) _ZN8firebase3app10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b666d0",
      "incomplete_value": true,
      "site": "00b666d0",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b656dc",
      "incomplete_value": true,
      "site": "00b656dc",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b666b4",
      "incomplete_value": true,
      "site": "00b666b4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b656c0",
      "incomplete_value": true,
      "site": "00b656c0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b666c0",
      "incomplete_value": false,
      "site": "00b666c8",
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
            "const:dba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b656cc",
      "incomplete_value": false,
      "site": "00b656d4",
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
            "const:ceb:8"
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
      "00b666b0",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b666c0",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ],
    [
      "00b666d0",
      "WRITE",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b666b0",
      "READ",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b666c0",
      "PARAM",
      [
        "storage",
        "002b6dba",
        null,
        "string"
      ]
    ],
    [
      "00b666d0",
      "WRITE",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b656d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b656ac.md#insn-00b656d4) · [`00b656dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b656ac.md#insn-00b656dc) · [`00b656b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b656ac.md#insn-00b656b8)
- 新版 [`00b666c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b666a0.md#insn-00b666c8) · [`00b666d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b666a0.md#insn-00b666d0) · [`00b666ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b666a0.md#insn-00b666ac)

~~~diff
- 00b656d4 ["INT_ADD", "register:40f0:8", ["const:b656d4:8", "const:4:8"]]
- 00b656d4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b666c8 ["INT_ADD", "register:40f0:8", ["const:b666c8:8", "const:4:8"]]
+ 00b666c8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b656d4 bytes 43d60394
+ 00b666c8 bytes 3ad60394
- 00b656dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:150:8"]]
- 00b656dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b666d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:110:8"]]
+ 00b666d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b656dc bytes 60aa00f9
+ 00b666d0 bytes 608a00f9
- 00b656b8 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b666ac ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b656b8 bytes 132e00b0
+ 00b666ac bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c1dcbeb088ca6a3810402b13b54647b"></a>

### [`00b656f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b656f0.md) → [`00b666e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b666e4.md) _ZN8firebase3app10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66714",
      "incomplete_value": true,
      "site": "00b66714",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65720",
      "incomplete_value": true,
      "site": "00b65720",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b666f8",
      "incomplete_value": true,
      "site": "00b666f8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65704",
      "incomplete_value": true,
      "site": "00b65704",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66700",
      "incomplete_value": true,
      "site": "00b6670c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:dba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6570c",
      "incomplete_value": true,
      "site": "00b65718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:ceb:8"
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
      "00b666f4",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66700",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ],
    [
      "00b66714",
      "WRITE",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b666f4",
      "READ",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66700",
      "PARAM",
      [
        "storage",
        "002b6dba",
        null,
        "string"
      ]
    ],
    [
      "00b66714",
      "WRITE",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b656f0.md#insn-00b65718) · [`00b65720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b656f0.md#insn-00b65720) · [`00b656fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b656f0.md#insn-00b656fc)
- 新版 [`00b6670c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b666e4.md#insn-00b6670c) · [`00b66714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b666e4.md#insn-00b66714) · [`00b666f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b666e4.md#insn-00b666f0)

~~~diff
- 00b65718 ["INT_ADD", "register:40f0:8", ["const:b65718:8", "const:4:8"]]
- 00b65718 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b6670c ["INT_ADD", "register:40f0:8", ["const:b6670c:8", "const:4:8"]]
+ 00b6670c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65718 bytes 32d60394
+ 00b6670c bytes 29d60394
- 00b65720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:150:8"]]
- 00b65720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66714 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:110:8"]]
+ 00b66714 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65720 bytes 60aa00f9
+ 00b66714 bytes 608a00f9
- 00b656fc ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b666f0 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b656fc bytes 132e00b0
+ 00b666f0 bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c5e044e5d92a88a372d36bf4b3d0a91"></a>

### [`00b65740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65740.md) → [`00b66734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66734.md) _ZN8firebase3app15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6678c",
      "incomplete_value": true,
      "site": "00b6678c",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65798",
      "incomplete_value": true,
      "site": "00b65798",
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
            "const:158:8"
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
      "definition_site": "00b66768",
      "incomplete_value": true,
      "site": "00b66774",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:110:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65774",
      "incomplete_value": true,
      "site": "00b65780",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:150:8"
              ]
            ]
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
      "00b66748",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66768",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6678c",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66748",
      "READ",
      [
        "storage",
        "01127118",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66768",
      "READ",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6678c",
      "WRITE",
      [
        "storage",
        "01127118",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65740.md#insn-00b65780) · [`00b65798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65740.md#insn-00b65798) · [`00b65750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65740.md#insn-00b65750)
- 新版 [`00b66774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66734.md#insn-00b66774) · [`00b6678c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66734.md#insn-00b6678c) · [`00b66744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66734.md#insn-00b66744)

~~~diff
- 00b65780 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65780 ["INT_ADD", "register:40f0:8", ["const:b65780:8", "const:4:8"]]
- 00b65780 ["CALLIND", null, ["register:0:8"]]
+ 00b66774 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66774 ["INT_ADD", "register:40f0:8", ["const:b66774:8", "const:4:8"]]
+ 00b66774 ["CALLIND", null, ["register:0:8"]]
- 00b65780 bytes 00013fd6
+ 00b66774 bytes 00013fd6
- 00b65798 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65798 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:158:8"]]
- 00b65798 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6678c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6678c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:118:8"]]
+ 00b6678c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65798 bytes a0620539
+ 00b6678c bytes a0620439
- 00b65750 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00b66744 ["COPY", "register:40a8:8", ["const:1127000:8"]]
- 00b65750 bytes 152e00b0
+ 00b66744 bytes 152e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8245120f2e1b6e795f91f0c32a6f3f45"></a>

### [`00b657ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b657ac.md) → [`00b667a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b667a0.md) _ZN8firebase3app12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b667dc",
      "incomplete_value": true,
      "site": "00b667dc",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b657e8",
      "incomplete_value": true,
      "site": "00b657e8",
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
            "const:158:8"
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
      "definition_site": "00b667fc",
      "incomplete_value": true,
      "site": "00b667fc",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65808",
      "incomplete_value": true,
      "site": "00b65808",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b667b8",
      "incomplete_value": true,
      "site": "00b667b8",
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
      "definition_site": "00b657c4",
      "incomplete_value": true,
      "site": "00b657c4",
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
      "00b667b4",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b667c0",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined1"
      ]
    ],
    [
      "00b667dc",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b667b4",
      "READ",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b667c0",
      "READ",
      [
        "storage",
        "01127118",
        null,
        "undefined1"
      ]
    ],
    [
      "00b667dc",
      "WRITE",
      [
        "storage",
        "01127118",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b657e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b657ac.md#insn-00b657e8) · [`00b65804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b657ac.md#insn-00b65804) · [`00b65808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b657ac.md#insn-00b65808)
- 新版 [`00b667dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b667a0.md#insn-00b667dc) · [`00b667f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b667a0.md#insn-00b667f8) · [`00b667fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b667a0.md#insn-00b667fc)

~~~diff
- 00b657e8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b657e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b657e8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:158:8"]]
- 00b657e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b667dc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b667dc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b667dc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:118:8"]]
+ 00b667dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b657e8 bytes bf620539
+ 00b667dc bytes bf620439
- 00b65804 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65804 ["INT_ADD", "register:40f0:8", ["const:b65804:8", "const:4:8"]]
- 00b65804 ["CALLIND", null, ["register:0:8"]]
+ 00b667f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b667f8 ["INT_ADD", "register:40f0:8", ["const:b667f8:8", "const:4:8"]]
+ 00b667f8 ["CALLIND", null, ["register:0:8"]]
- 00b65804 bytes 00013fd6
+ 00b667f8 bytes 00013fd6
- 00b65808 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:150:8"]]
- 00b65808 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b65808 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b667fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:110:8"]]
+ 00b667fc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b667fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b65808 bytes 9faa00f9
+ 00b667fc bytes 9f8a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b7b0d63f6a56c52ebcd29c9a08ae727"></a>

### [`00b6581c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6581c.md) → [`00b66810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66810.md) _ZN8firebase3app14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66850",
      "incomplete_value": true,
      "site": "00b66850",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6585c",
      "incomplete_value": true,
      "site": "00b6585c",
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
            "const:150:8"
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
      "definition_site": "00b6682c",
      "incomplete_value": true,
      "site": "00b6682c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65838",
      "incomplete_value": true,
      "site": "00b65838",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66834",
      "incomplete_value": false,
      "site": "00b66848",
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
            "const:dba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65840",
      "incomplete_value": false,
      "site": "00b65854",
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
            "const:ceb:8"
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
      "00b66824",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66834",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ],
    [
      "00b66850",
      "WRITE",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66824",
      "READ",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66834",
      "PARAM",
      [
        "storage",
        "002b6dba",
        null,
        "string"
      ]
    ],
    [
      "00b66850",
      "WRITE",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6581c.md#insn-00b65854) · [`00b6585c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6581c.md#insn-00b6585c) · [`00b65828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6581c.md#insn-00b65828)
- 新版 [`00b66848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66810.md#insn-00b66848) · [`00b66850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66810.md#insn-00b66850) · [`00b6681c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66810.md#insn-00b6681c)

~~~diff
- 00b65854 ["INT_ADD", "register:40f0:8", ["const:b65854:8", "const:4:8"]]
- 00b65854 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66848 ["INT_ADD", "register:40f0:8", ["const:b66848:8", "const:4:8"]]
+ 00b66848 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65854 bytes e3d50394
+ 00b66848 bytes dad50394
- 00b6585c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:150:8"]]
- 00b6585c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66850 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:110:8"]]
+ 00b66850 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6585c bytes 80aa00f9
+ 00b66850 bytes 808a00f9
- 00b65828 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00b6681c ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00b65828 bytes 142e00b0
+ 00b6681c bytes 142e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b47e0cbfd87b796dc9999e1ac6f0d86"></a>

### [`00b6588c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6588c.md) → [`00b66880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66880.md) _ZN8firebase3app11GetMethodIdENS0_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6689c",
      "incomplete_value": false,
      "site": "00b668a0",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b658a8",
      "incomplete_value": false,
      "site": "00b658ac",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b668ac",
      "incomplete_value": true,
      "site": "00b668b8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b658b8",
      "incomplete_value": true,
      "site": "00b658c4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b6689c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b668ac",
      "DATA",
      [
        "storage",
        "01126160",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6689c",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b668ac",
      "DATA",
      [
        "storage",
        "01127120",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b658ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6588c.md#insn-00b658ac) · [`00b658a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6588c.md#insn-00b658a8) · [`00b658b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6588c.md#insn-00b658b0)
- 新版 [`00b668a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66880.md#insn-00b668a0) · [`00b6689c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66880.md#insn-00b6689c) · [`00b668a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66880.md#insn-00b668a4)

~~~diff
- 00b658ac ["INT_ADD", "register:40f0:8", ["const:b658ac:8", "const:4:8"]]
- 00b658ac ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b668a0 ["INT_ADD", "register:40f0:8", ["const:b668a0:8", "const:4:8"]]
+ 00b668a0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b658ac bytes 09d60394
+ 00b668a0 bytes 00d60394
- 00b658a8 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b658a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b658a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b658a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6689c ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b6689c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6689c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6689c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b658a8 bytes 002c0c91
+ 00b6689c bytes 008c1191
- 00b658b0 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b668a4 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b658b0 bytes 082e00b0
+ 00b668a4 bytes 082e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae96f016f23fe44842b96fd54552522a"></a>

### [`00b658c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b658c8.md) → [`00b668bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b668bc.md) _ZN8firebase3app13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b668fc",
      "incomplete_value": true,
      "site": "00b668fc",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65908",
      "incomplete_value": true,
      "site": "00b65908",
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
            "const:150:8"
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
      "definition_site": "00b668d8",
      "incomplete_value": true,
      "site": "00b668d8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b658e4",
      "incomplete_value": true,
      "site": "00b658e4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b668e0",
      "incomplete_value": false,
      "site": "00b668f4",
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
            "const:dba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b658ec",
      "incomplete_value": false,
      "site": "00b65900",
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
            "const:ceb:8"
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
      "00b668d0",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b668e0",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ],
    [
      "00b668fc",
      "WRITE",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b668d0",
      "READ",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b668e0",
      "PARAM",
      [
        "storage",
        "002b6dba",
        null,
        "string"
      ]
    ],
    [
      "00b668fc",
      "WRITE",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b658c8.md#insn-00b65900) · [`00b65908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b658c8.md#insn-00b65908) · [`00b658d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b658c8.md#insn-00b658d4)
- 新版 [`00b668f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b668bc.md#insn-00b668f4) · [`00b668fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b668bc.md#insn-00b668fc) · [`00b668c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b668bc.md#insn-00b668c8)

~~~diff
- 00b65900 ["INT_ADD", "register:40f0:8", ["const:b65900:8", "const:4:8"]]
- 00b65900 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b668f4 ["INT_ADD", "register:40f0:8", ["const:b668f4:8", "const:4:8"]]
+ 00b668f4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65900 bytes b8d50394
+ 00b668f4 bytes afd50394
- 00b65908 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:150:8"]]
- 00b65908 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b668fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:110:8"]]
+ 00b668fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65908 bytes 80aa00f9
+ 00b668fc bytes 808a00f9
- 00b658d4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00b668c8 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00b658d4 bytes 142e00b0
+ 00b668c8 bytes 142e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2840ff12f9904907b4f7820890c6daeb"></a>

### [`00b65938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65938.md) → [`00b6692c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b6692c.md) _ZN8firebase3app10GetFieldIdENS0_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66948",
      "incomplete_value": false,
      "site": "00b6694c",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65954",
      "incomplete_value": false,
      "site": "00b65958",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b66958",
      "incomplete_value": true,
      "site": "00b66964",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65964",
      "incomplete_value": true,
      "site": "00b65970",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b66948",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b66958",
      "DATA",
      [
        "storage",
        "011261a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b66948",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b66958",
      "DATA",
      [
        "storage",
        "01127168",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65938.md#insn-00b65958) · [`00b65954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65938.md#insn-00b65954) · [`00b6595c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65938.md#insn-00b6595c)
- 新版 [`00b6694c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b6692c.md#insn-00b6694c) · [`00b66948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b6692c.md#insn-00b66948) · [`00b66950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b6692c.md#insn-00b66950)

~~~diff
- 00b65958 ["INT_ADD", "register:40f0:8", ["const:b65958:8", "const:4:8"]]
- 00b65958 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b6694c ["INT_ADD", "register:40f0:8", ["const:b6694c:8", "const:4:8"]]
+ 00b6694c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b65958 bytes ded50394
+ 00b6694c bytes d5d50394
- 00b65954 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b65954 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65954 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65954 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66948 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b66948 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66948 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66948 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65954 bytes 00341591
+ 00b66948 bytes 00681891
- 00b6595c ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b66950 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b6595c bytes 082e00b0
+ 00b66950 bytes 082e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43930db6da2c7d394a348c3b0b87816d"></a>

### [`00b65974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65974.md) → [`00b66968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66968.md) _ZN8firebase15options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEN

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66994",
      "incomplete_value": true,
      "site": "00b66994",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b659a0",
      "incomplete_value": true,
      "site": "00b659a0",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6697c",
      "incomplete_value": true,
      "site": "00b6697c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65988",
      "incomplete_value": true,
      "site": "00b65988",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66988",
      "incomplete_value": false,
      "site": "00b6698c",
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
            "const:ad4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65994",
      "incomplete_value": false,
      "site": "00b65998",
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
            "const:a09:8"
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
      "00b66978",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66988",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ],
    [
      "00b66994",
      "WRITE",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66978",
      "READ",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66988",
      "PARAM",
      [
        "storage",
        "002a2ad4",
        null,
        "string"
      ]
    ],
    [
      "00b66994",
      "WRITE",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65974.md#insn-00b65998) · [`00b659a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65974.md#insn-00b659a0) · [`00b65980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65974.md#insn-00b65980)
- 新版 [`00b6698c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66968.md#insn-00b6698c) · [`00b66994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66968.md#insn-00b66994) · [`00b66974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66968.md#insn-00b66974)

~~~diff
- 00b65998 ["INT_ADD", "register:40f0:8", ["const:b65998:8", "const:4:8"]]
- 00b65998 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b6698c ["INT_ADD", "register:40f0:8", ["const:b6698c:8", "const:4:8"]]
+ 00b6698c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65998 bytes 92d50394
+ 00b6698c bytes 89d50394
- 00b659a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
- 00b659a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66994 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:170:8"]]
+ 00b66994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b659a0 bytes 60da00f9
+ 00b66994 bytes 60ba00f9
- 00b65980 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b66974 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b65980 bytes 132e00b0
+ 00b66974 bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-100ce01151d24609bbf184c607a7feb1"></a>

### [`00b659b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b659b4.md) → [`00b669a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b669a8.md) _ZN8firebase15options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b669d4",
      "incomplete_value": true,
      "site": "00b669d4",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b659e0",
      "incomplete_value": true,
      "site": "00b659e0",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b669bc",
      "incomplete_value": true,
      "site": "00b669bc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b659c8",
      "incomplete_value": true,
      "site": "00b659c8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b669c4",
      "incomplete_value": false,
      "site": "00b669cc",
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
            "const:ad4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b659d0",
      "incomplete_value": false,
      "site": "00b659d8",
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
            "const:a09:8"
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
      "00b669b8",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b669c4",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ],
    [
      "00b669d4",
      "WRITE",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b669b8",
      "READ",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ],
    [
      "00b669c4",
      "PARAM",
      [
        "storage",
        "002a2ad4",
        null,
        "string"
      ]
    ],
    [
      "00b669d4",
      "WRITE",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b659d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b659b4.md#insn-00b659d8) · [`00b659e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b659b4.md#insn-00b659e0) · [`00b659c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b659b4.md#insn-00b659c0)
- 新版 [`00b669cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b669a8.md#insn-00b669cc) · [`00b669d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b669a8.md#insn-00b669d4) · [`00b669b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b669a8.md#insn-00b669b4)

~~~diff
- 00b659d8 ["INT_ADD", "register:40f0:8", ["const:b659d8:8", "const:4:8"]]
- 00b659d8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b669cc ["INT_ADD", "register:40f0:8", ["const:b669cc:8", "const:4:8"]]
+ 00b669cc ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b659d8 bytes 82d50394
+ 00b669cc bytes 79d50394
- 00b659e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
- 00b659e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b669d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:170:8"]]
+ 00b669d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b659e0 bytes 60da00f9
+ 00b669d4 bytes 60ba00f9
- 00b659c0 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b669b4 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b659c0 bytes 132e00b0
+ 00b669b4 bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-030fd5f72010aa1ca90ab41ad9952f20"></a>

### [`00b659f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b659f4.md) → [`00b669e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b669e8.md) _ZN8firebase15options_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66a18",
      "incomplete_value": true,
      "site": "00b66a18",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65a24",
      "incomplete_value": true,
      "site": "00b65a24",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b669fc",
      "incomplete_value": true,
      "site": "00b669fc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65a08",
      "incomplete_value": true,
      "site": "00b65a08",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66a08",
      "incomplete_value": false,
      "site": "00b66a10",
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
            "const:ad4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65a14",
      "incomplete_value": false,
      "site": "00b65a1c",
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
            "const:a09:8"
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
      "00b669f8",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66a08",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ],
    [
      "00b66a18",
      "WRITE",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b669f8",
      "READ",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66a08",
      "PARAM",
      [
        "storage",
        "002a2ad4",
        null,
        "string"
      ]
    ],
    [
      "00b66a18",
      "WRITE",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b659f4.md#insn-00b65a1c) · [`00b65a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b659f4.md#insn-00b65a24) · [`00b65a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b659f4.md#insn-00b65a00)
- 新版 [`00b66a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b669e8.md#insn-00b66a10) · [`00b66a18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b669e8.md#insn-00b66a18) · [`00b669f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b669e8.md#insn-00b669f4)

~~~diff
- 00b65a1c ["INT_ADD", "register:40f0:8", ["const:b65a1c:8", "const:4:8"]]
- 00b65a1c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66a10 ["INT_ADD", "register:40f0:8", ["const:b66a10:8", "const:4:8"]]
+ 00b66a10 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65a1c bytes 71d50394
+ 00b66a10 bytes 68d50394
- 00b65a24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
- 00b65a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66a18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:170:8"]]
+ 00b66a18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65a24 bytes 60da00f9
+ 00b66a18 bytes 60ba00f9
- 00b65a00 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b669f4 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b65a00 bytes 132e00b0
+ 00b669f4 bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-827fa56314a89b173d2ad2c2577f4c68"></a>

### [`00b65a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65a38.md) → [`00b66a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66a2c.md) _ZN8firebase15options_builder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66a5c",
      "incomplete_value": true,
      "site": "00b66a5c",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65a68",
      "incomplete_value": true,
      "site": "00b65a68",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66a40",
      "incomplete_value": true,
      "site": "00b66a40",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65a4c",
      "incomplete_value": true,
      "site": "00b65a4c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66a48",
      "incomplete_value": false,
      "site": "00b66a54",
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
            "const:ad4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65a54",
      "incomplete_value": false,
      "site": "00b65a60",
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
            "const:a09:8"
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
      "00b66a3c",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66a48",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ],
    [
      "00b66a5c",
      "WRITE",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66a3c",
      "READ",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66a48",
      "PARAM",
      [
        "storage",
        "002a2ad4",
        null,
        "string"
      ]
    ],
    [
      "00b66a5c",
      "WRITE",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65a38.md#insn-00b65a60) · [`00b65a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65a38.md#insn-00b65a68) · [`00b65a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65a38.md#insn-00b65a44)
- 新版 [`00b66a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66a2c.md#insn-00b66a54) · [`00b66a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66a2c.md#insn-00b66a5c) · [`00b66a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66a2c.md#insn-00b66a38)

~~~diff
- 00b65a60 ["INT_ADD", "register:40f0:8", ["const:b65a60:8", "const:4:8"]]
- 00b65a60 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66a54 ["INT_ADD", "register:40f0:8", ["const:b66a54:8", "const:4:8"]]
+ 00b66a54 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65a60 bytes 60d50394
+ 00b66a54 bytes 57d50394
- 00b65a68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
- 00b65a68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66a5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:170:8"]]
+ 00b66a5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65a68 bytes 60da00f9
+ 00b66a5c bytes 60ba00f9
- 00b65a44 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b66a38 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b65a44 bytes 132e00b0
+ 00b66a38 bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-115ad6497eab21c0bf083577827f983a"></a>

### [`00b65a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65a88.md) → [`00b66a7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66a7c.md) _ZN8firebase15options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66ad4",
      "incomplete_value": true,
      "site": "00b66ad4",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ae0",
      "incomplete_value": true,
      "site": "00b65ae0",
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
            "const:1b8:8"
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
      "definition_site": "00b66ab0",
      "incomplete_value": true,
      "site": "00b66abc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:170:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65abc",
      "incomplete_value": true,
      "site": "00b65ac8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "00b66a90",
      "READ",
      [
        "storage",
        "011261b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66ab0",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66ad4",
      "WRITE",
      [
        "storage",
        "011261b8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66a90",
      "READ",
      [
        "storage",
        "01127178",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66ab0",
      "READ",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66ad4",
      "WRITE",
      [
        "storage",
        "01127178",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65a88.md#insn-00b65ac8) · [`00b65ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65a88.md#insn-00b65ae0) · [`00b65a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65a88.md#insn-00b65a98)
- 新版 [`00b66abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66a7c.md#insn-00b66abc) · [`00b66ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66a7c.md#insn-00b66ad4) · [`00b66a8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66a7c.md#insn-00b66a8c)

~~~diff
- 00b65ac8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65ac8 ["INT_ADD", "register:40f0:8", ["const:b65ac8:8", "const:4:8"]]
- 00b65ac8 ["CALLIND", null, ["register:0:8"]]
+ 00b66abc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66abc ["INT_ADD", "register:40f0:8", ["const:b66abc:8", "const:4:8"]]
+ 00b66abc ["CALLIND", null, ["register:0:8"]]
- 00b65ac8 bytes 00013fd6
+ 00b66abc bytes 00013fd6
- 00b65ae0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65ae0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1b8:8"]]
- 00b65ae0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b66ad4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b66ad4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:178:8"]]
+ 00b66ad4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65ae0 bytes a0e20639
+ 00b66ad4 bytes a0e20539
- 00b65a98 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00b66a8c ["COPY", "register:40a8:8", ["const:1127000:8"]]
- 00b65a98 bytes 152e00b0
+ 00b66a8c bytes 152e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba3d9dcaa5674e8ef1382e2c3fe6f9ea"></a>

### [`00b65af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65af4.md) → [`00b66ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ae8.md) _ZN8firebase15options_builder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66b24",
      "incomplete_value": true,
      "site": "00b66b24",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b30",
      "incomplete_value": true,
      "site": "00b65b30",
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
            "const:1b8:8"
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
      "definition_site": "00b66b44",
      "incomplete_value": true,
      "site": "00b66b44",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b50",
      "incomplete_value": true,
      "site": "00b65b50",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66b00",
      "incomplete_value": true,
      "site": "00b66b00",
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
      "definition_site": "00b65b0c",
      "incomplete_value": true,
      "site": "00b65b0c",
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
      "00b66afc",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66b08",
      "READ",
      [
        "storage",
        "011261b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66b24",
      "WRITE",
      [
        "storage",
        "011261b8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66afc",
      "READ",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66b08",
      "READ",
      [
        "storage",
        "01127178",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66b24",
      "WRITE",
      [
        "storage",
        "01127178",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65af4.md#insn-00b65b30) · [`00b65b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65af4.md#insn-00b65b4c) · [`00b65b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65af4.md#insn-00b65b50)
- 新版 [`00b66b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ae8.md#insn-00b66b24) · [`00b66b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ae8.md#insn-00b66b40) · [`00b66b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ae8.md#insn-00b66b44)

~~~diff
- 00b65b30 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65b30 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65b30 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:1b8:8"]]
- 00b65b30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b66b24 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b66b24 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b66b24 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:178:8"]]
+ 00b66b24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65b30 bytes bfe20639
+ 00b66b24 bytes bfe20539
- 00b65b4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65b4c ["INT_ADD", "register:40f0:8", ["const:b65b4c:8", "const:4:8"]]
- 00b65b4c ["CALLIND", null, ["register:0:8"]]
+ 00b66b40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66b40 ["INT_ADD", "register:40f0:8", ["const:b66b40:8", "const:4:8"]]
+ 00b66b40 ["CALLIND", null, ["register:0:8"]]
- 00b65b4c bytes 00013fd6
+ 00b66b40 bytes 00013fd6
- 00b65b50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b0:8"]]
- 00b65b50 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b65b50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b66b44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:170:8"]]
+ 00b66b44 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b66b44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b65b50 bytes 9fda00f9
+ 00b66b44 bytes 9fba00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-366a9a0a5e292b51bad86224eef352fb"></a>

### [`00b65b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65b64.md) → [`00b66b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66b58.md) _ZN8firebase15options_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66b98",
      "incomplete_value": true,
      "site": "00b66b98",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ba4",
      "incomplete_value": true,
      "site": "00b65ba4",
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
            "const:1b0:8"
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
      "definition_site": "00b66b74",
      "incomplete_value": true,
      "site": "00b66b74",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65b80",
      "incomplete_value": true,
      "site": "00b65b80",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66b7c",
      "incomplete_value": false,
      "site": "00b66b90",
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
            "const:ad4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b88",
      "incomplete_value": false,
      "site": "00b65b9c",
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
            "const:a09:8"
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
      "00b66b6c",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66b7c",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ],
    [
      "00b66b98",
      "WRITE",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66b6c",
      "READ",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66b7c",
      "PARAM",
      [
        "storage",
        "002a2ad4",
        null,
        "string"
      ]
    ],
    [
      "00b66b98",
      "WRITE",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65b64.md#insn-00b65b9c) · [`00b65ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65b64.md#insn-00b65ba4) · [`00b65b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65b64.md#insn-00b65b70)
- 新版 [`00b66b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66b58.md#insn-00b66b90) · [`00b66b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66b58.md#insn-00b66b98) · [`00b66b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66b58.md#insn-00b66b64)

~~~diff
- 00b65b9c ["INT_ADD", "register:40f0:8", ["const:b65b9c:8", "const:4:8"]]
- 00b65b9c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66b90 ["INT_ADD", "register:40f0:8", ["const:b66b90:8", "const:4:8"]]
+ 00b66b90 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65b9c bytes 11d50394
+ 00b66b90 bytes 08d50394
- 00b65ba4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b0:8"]]
- 00b65ba4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66b98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:170:8"]]
+ 00b66b98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65ba4 bytes 80da00f9
+ 00b66b98 bytes 80ba00f9
- 00b65b70 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00b66b64 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00b65b70 bytes 142e00b0
+ 00b66b64 bytes 142e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b9c4e75930b2733b13f24b3a81982a3"></a>

### [`00b65bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65bd4.md) → [`00b66bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66bc8.md) _ZN8firebase15options_builder11GetMethodIdENS0_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66be4",
      "incomplete_value": false,
      "site": "00b66be8",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65bf0",
      "incomplete_value": false,
      "site": "00b65bf4",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b66bf4",
      "incomplete_value": true,
      "site": "00b66c00",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c00",
      "incomplete_value": true,
      "site": "00b65c0c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b66be4",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b66bf4",
      "DATA",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66be4",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b66bf4",
      "DATA",
      [
        "storage",
        "01127180",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65bd4.md#insn-00b65bf4) · [`00b65bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65bd4.md#insn-00b65bf0) · [`00b65bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65bd4.md#insn-00b65bf8)
- 新版 [`00b66be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66bc8.md#insn-00b66be8) · [`00b66be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66bc8.md#insn-00b66be4) · [`00b66bec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66bc8.md#insn-00b66bec)

~~~diff
- 00b65bf4 ["INT_ADD", "register:40f0:8", ["const:b65bf4:8", "const:4:8"]]
- 00b65bf4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b66be8 ["INT_ADD", "register:40f0:8", ["const:b66be8:8", "const:4:8"]]
+ 00b66be8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b65bf4 bytes 37d50394
+ 00b66be8 bytes 2ed50394
- 00b65bf0 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b65bf0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65bf0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65bf0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66be4 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b66be4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66be4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66be4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65bf0 bytes 002c0c91
+ 00b66be4 bytes 008c1191
- 00b65bf8 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b66bec ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b65bf8 bytes 082e00b0
+ 00b66bec bytes 082e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72bd18c51f41bca3c8b3e56009712dc6"></a>

### [`00b65c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65c10.md) → [`00b66c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66c04.md) _ZN8firebase15options_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66c44",
      "incomplete_value": true,
      "site": "00b66c44",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c50",
      "incomplete_value": true,
      "site": "00b65c50",
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
            "const:1b0:8"
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
      "definition_site": "00b66c20",
      "incomplete_value": true,
      "site": "00b66c20",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65c2c",
      "incomplete_value": true,
      "site": "00b65c2c",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b65c2c"
      ],
      [
        "FALL_THROUGH",
        "00b66c20"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b66c20",
      "incomplete_value": true,
      "site": "00b66c44",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65c2c",
      "incomplete_value": true,
      "site": "00b65c50",
      "value": [
        "INT_NOTEQUAL",
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
      "00b66c18",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66c28",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ],
    [
      "00b66c44",
      "WRITE",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66c18",
      "READ",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66c28",
      "PARAM",
      [
        "storage",
        "002a2ad4",
        null,
        "string"
      ]
    ],
    [
      "00b66c44",
      "WRITE",
      [
        "storage",
        "01127170",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65c10.md#insn-00b65c50) · [`00b65c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65c10.md#insn-00b65c1c) · [`00b65c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65c10.md#insn-00b65c24)
- 新版 [`00b66c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66c04.md#insn-00b66c44) · [`00b66c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66c04.md#insn-00b66c10) · [`00b66c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66c04.md#insn-00b66c18)

~~~diff
- 00b65c50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b0:8"]]
- 00b65c50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66c44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:170:8"]]
+ 00b66c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65c50 bytes 80da00f9
+ 00b66c44 bytes 80ba00f9
- 00b65c1c ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00b66c10 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00b65c1c bytes 142e00b0
+ 00b66c10 bytes 142e00b0
- 00b65c24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b0:8"]]
- 00b65c24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66c18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:170:8"]]
+ 00b66c18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65c24 bytes 81da40f9
+ 00b66c18 bytes 81ba40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2539bf15cc7f632cf55b6723ac1be253"></a>

### [`00b65c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65c80.md) → [`00b66c74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66c74.md) _ZN8firebase15options_builder10GetFieldIdENS0_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b66c90",
      "incomplete_value": false,
      "site": "00b66c94",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c9c",
      "incomplete_value": false,
      "site": "00b65ca0",
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
            "const:54d:8"
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
      "00b66c90",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b66ca0",
      "DATA",
      [
        "storage",
        "01126200",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b66c90",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b66ca0",
      "DATA",
      [
        "storage",
        "011271c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65c80.md#insn-00b65ca0) · [`00b65c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65c80.md#insn-00b65c9c) · [`00b65ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65c80.md#insn-00b65ca4)
- 新版 [`00b66c94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66c74.md#insn-00b66c94) · [`00b66c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66c74.md#insn-00b66c90) · [`00b66c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66c74.md#insn-00b66c98)

~~~diff
- 00b65ca0 ["INT_ADD", "register:40f0:8", ["const:b65ca0:8", "const:4:8"]]
- 00b65ca0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b66c94 ["INT_ADD", "register:40f0:8", ["const:b66c94:8", "const:4:8"]]
+ 00b66c94 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b65ca0 bytes 0cd50394
+ 00b66c94 bytes 03d50394
- 00b65c9c ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b65c9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65c9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65c9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66c90 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b66c90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66c90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66c90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65c9c bytes 00341591
+ 00b66c90 bytes 00681891
- 00b65ca4 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b66c98 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b65ca4 bytes 082e00b0
+ 00b66c98 bytes 082e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63605dab2f54630c56ed2f98536e3601"></a>

### [`00b65cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65cbc.md) → [`00b66cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66cb0.md) _ZN8firebase7options19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEENS_4util16

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66cdc",
      "incomplete_value": true,
      "site": "00b66cdc",
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
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ce8",
      "incomplete_value": true,
      "site": "00b65ce8",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66cc4",
      "incomplete_value": true,
      "site": "00b66cc4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65cd0",
      "incomplete_value": true,
      "site": "00b65cd0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66cd0",
      "incomplete_value": false,
      "site": "00b66cd4",
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
            "const:a7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65cdc",
      "incomplete_value": false,
      "site": "00b65ce0",
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
            "const:9ab:8"
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
      "00b66cc0",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66cd0",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b66cdc",
      "WRITE",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66cc0",
      "READ",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66cd0",
      "PARAM",
      [
        "storage",
        "002b5a7a",
        null,
        "string"
      ]
    ],
    [
      "00b66cdc",
      "WRITE",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65cbc.md#insn-00b65ce0) · [`00b65ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65cbc.md#insn-00b65ce8) · [`00b65cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65cbc.md#insn-00b65cc8)
- 新版 [`00b66cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66cb0.md#insn-00b66cd4) · [`00b66cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66cb0.md#insn-00b66cdc) · [`00b66cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66cb0.md#insn-00b66cbc)

~~~diff
- 00b65ce0 ["INT_ADD", "register:40f0:8", ["const:b65ce0:8", "const:4:8"]]
- 00b65ce0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66cd4 ["INT_ADD", "register:40f0:8", ["const:b66cd4:8", "const:4:8"]]
+ 00b66cd4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65ce0 bytes c0d40394
+ 00b66cd4 bytes b7d40394
- 00b65ce8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:208:8"]]
- 00b65ce8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66cdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1c8:8"]]
+ 00b66cdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65ce8 bytes 600601f9
+ 00b66cdc bytes 60e600f9
- 00b65cc8 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b66cbc ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b65cc8 bytes 132e00b0
+ 00b66cbc bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3170ba733050bd5c8dc0a052c1ba284"></a>

### [`00b65cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65cfc.md) → [`00b66cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66cf0.md) _ZN8firebase7options19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66d1c",
      "incomplete_value": true,
      "site": "00b66d1c",
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
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d28",
      "incomplete_value": true,
      "site": "00b65d28",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66d04",
      "incomplete_value": true,
      "site": "00b66d04",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65d10",
      "incomplete_value": true,
      "site": "00b65d10",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66d0c",
      "incomplete_value": false,
      "site": "00b66d14",
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
            "const:a7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d18",
      "incomplete_value": false,
      "site": "00b65d20",
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
            "const:9ab:8"
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
      "00b66d00",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66d0c",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b66d1c",
      "WRITE",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66d00",
      "READ",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66d0c",
      "PARAM",
      [
        "storage",
        "002b5a7a",
        null,
        "string"
      ]
    ],
    [
      "00b66d1c",
      "WRITE",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65cfc.md#insn-00b65d20) · [`00b65d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65cfc.md#insn-00b65d28) · [`00b65d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65cfc.md#insn-00b65d08)
- 新版 [`00b66d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66cf0.md#insn-00b66d14) · [`00b66d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66cf0.md#insn-00b66d1c) · [`00b66cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66cf0.md#insn-00b66cfc)

~~~diff
- 00b65d20 ["INT_ADD", "register:40f0:8", ["const:b65d20:8", "const:4:8"]]
- 00b65d20 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66d14 ["INT_ADD", "register:40f0:8", ["const:b66d14:8", "const:4:8"]]
+ 00b66d14 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65d20 bytes b0d40394
+ 00b66d14 bytes a7d40394
- 00b65d28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:208:8"]]
- 00b65d28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66d1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1c8:8"]]
+ 00b66d1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65d28 bytes 600601f9
+ 00b66d1c bytes 60e600f9
- 00b65d08 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b66cfc ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b65d08 bytes 132e00b0
+ 00b66cfc bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88f791d1bc0d4432ed5376b7f126d59f"></a>

### [`00b65d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65d3c.md) → [`00b66d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66d30.md) _ZN8firebase7options10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66d60",
      "incomplete_value": true,
      "site": "00b66d60",
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
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d6c",
      "incomplete_value": true,
      "site": "00b65d6c",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66d44",
      "incomplete_value": true,
      "site": "00b66d44",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65d50",
      "incomplete_value": true,
      "site": "00b65d50",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66d50",
      "incomplete_value": false,
      "site": "00b66d58",
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
            "const:a7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d5c",
      "incomplete_value": false,
      "site": "00b65d64",
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
            "const:9ab:8"
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
      "00b66d40",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66d50",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b66d60",
      "WRITE",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66d40",
      "READ",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66d50",
      "PARAM",
      [
        "storage",
        "002b5a7a",
        null,
        "string"
      ]
    ],
    [
      "00b66d60",
      "WRITE",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65d3c.md#insn-00b65d64) · [`00b65d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65d3c.md#insn-00b65d6c) · [`00b65d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65d3c.md#insn-00b65d48)
- 新版 [`00b66d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66d30.md#insn-00b66d58) · [`00b66d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66d30.md#insn-00b66d60) · [`00b66d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66d30.md#insn-00b66d3c)

~~~diff
- 00b65d64 ["INT_ADD", "register:40f0:8", ["const:b65d64:8", "const:4:8"]]
- 00b65d64 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66d58 ["INT_ADD", "register:40f0:8", ["const:b66d58:8", "const:4:8"]]
+ 00b66d58 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65d64 bytes 9fd40394
+ 00b66d58 bytes 96d40394
- 00b65d6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:208:8"]]
- 00b65d6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66d60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1c8:8"]]
+ 00b66d60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65d6c bytes 600601f9
+ 00b66d60 bytes 60e600f9
- 00b65d48 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b66d3c ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b65d48 bytes 132e00b0
+ 00b66d3c bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd15e215a52cf2fa69eae9ac0ec2a34"></a>

### [`00b65d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65d80.md) → [`00b66d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66d74.md) _ZN8firebase7options10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66da4",
      "incomplete_value": true,
      "site": "00b66da4",
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
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65db0",
      "incomplete_value": true,
      "site": "00b65db0",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66d88",
      "incomplete_value": true,
      "site": "00b66d88",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65d94",
      "incomplete_value": true,
      "site": "00b65d94",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66d90",
      "incomplete_value": false,
      "site": "00b66d9c",
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
            "const:a7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d9c",
      "incomplete_value": false,
      "site": "00b65da8",
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
            "const:9ab:8"
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
      "00b66d84",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66d90",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b66da4",
      "WRITE",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66d84",
      "READ",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66d90",
      "PARAM",
      [
        "storage",
        "002b5a7a",
        null,
        "string"
      ]
    ],
    [
      "00b66da4",
      "WRITE",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65d80.md#insn-00b65da8) · [`00b65db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65d80.md#insn-00b65db0) · [`00b65d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65d80.md#insn-00b65d8c)
- 新版 [`00b66d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66d74.md#insn-00b66d9c) · [`00b66da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66d74.md#insn-00b66da4) · [`00b66d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66d74.md#insn-00b66d80)

~~~diff
- 00b65da8 ["INT_ADD", "register:40f0:8", ["const:b65da8:8", "const:4:8"]]
- 00b65da8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66d9c ["INT_ADD", "register:40f0:8", ["const:b66d9c:8", "const:4:8"]]
+ 00b66d9c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65da8 bytes 8ed40394
+ 00b66d9c bytes 85d40394
- 00b65db0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:208:8"]]
- 00b65db0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66da4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1c8:8"]]
+ 00b66da4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65db0 bytes 600601f9
+ 00b66da4 bytes 60e600f9
- 00b65d8c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b66d80 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b65d8c bytes 132e00b0
+ 00b66d80 bytes 132e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6ec15b6da68d0982fbf41d9dccffbe5"></a>

### [`00b65dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65dd0.md) → [`00b66dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66dc4.md) _ZN8firebase7options15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66e1c",
      "incomplete_value": true,
      "site": "00b66e1c",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e28",
      "incomplete_value": true,
      "site": "00b65e28",
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
            "const:210:8"
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
      "definition_site": "00b66df8",
      "incomplete_value": true,
      "site": "00b66e04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:1c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e04",
      "incomplete_value": true,
      "site": "00b65e10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:208:8"
              ]
            ]
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
      "00b66dd8",
      "READ",
      [
        "storage",
        "01126210",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66df8",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66e1c",
      "WRITE",
      [
        "storage",
        "01126210",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66dd8",
      "READ",
      [
        "storage",
        "011271d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66df8",
      "READ",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66e1c",
      "WRITE",
      [
        "storage",
        "011271d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65dd0.md#insn-00b65e10) · [`00b65e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65dd0.md#insn-00b65e28) · [`00b65de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65dd0.md#insn-00b65de0)
- 新版 [`00b66e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66dc4.md#insn-00b66e04) · [`00b66e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66dc4.md#insn-00b66e1c) · [`00b66dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66dc4.md#insn-00b66dd4)

~~~diff
- 00b65e10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65e10 ["INT_ADD", "register:40f0:8", ["const:b65e10:8", "const:4:8"]]
- 00b65e10 ["CALLIND", null, ["register:0:8"]]
+ 00b66e04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66e04 ["INT_ADD", "register:40f0:8", ["const:b66e04:8", "const:4:8"]]
+ 00b66e04 ["CALLIND", null, ["register:0:8"]]
- 00b65e10 bytes 00013fd6
+ 00b66e04 bytes 00013fd6
- 00b65e28 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65e28 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:210:8"]]
- 00b65e28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b66e1c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b66e1c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1d0:8"]]
+ 00b66e1c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65e28 bytes a0420839
+ 00b66e1c bytes a0420739
- 00b65de0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00b66dd4 ["COPY", "register:40a8:8", ["const:1127000:8"]]
- 00b65de0 bytes 152e00b0
+ 00b66dd4 bytes 152e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2134fbc049b3216161cdebe455f82bda"></a>

### [`00b65e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65e3c.md) → [`00b66e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66e30.md) _ZN8firebase7options12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66e6c",
      "incomplete_value": true,
      "site": "00b66e6c",
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
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e78",
      "incomplete_value": true,
      "site": "00b65e78",
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
            "const:210:8"
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
      "definition_site": "00b66e8c",
      "incomplete_value": true,
      "site": "00b66e8c",
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
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e98",
      "incomplete_value": true,
      "site": "00b65e98",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66e48",
      "incomplete_value": true,
      "site": "00b66e48",
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
      "definition_site": "00b65e54",
      "incomplete_value": true,
      "site": "00b65e54",
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
      "00b66e44",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66e50",
      "READ",
      [
        "storage",
        "01126210",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66e6c",
      "WRITE",
      [
        "storage",
        "01126210",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66e44",
      "READ",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66e50",
      "READ",
      [
        "storage",
        "011271d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66e6c",
      "WRITE",
      [
        "storage",
        "011271d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65e3c.md#insn-00b65e78) · [`00b65e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65e3c.md#insn-00b65e94) · [`00b65e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65e3c.md#insn-00b65e98)
- 新版 [`00b66e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66e30.md#insn-00b66e6c) · [`00b66e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66e30.md#insn-00b66e88) · [`00b66e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66e30.md#insn-00b66e8c)

~~~diff
- 00b65e78 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65e78 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65e78 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:210:8"]]
- 00b65e78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b66e6c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b66e6c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b66e6c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:1d0:8"]]
+ 00b66e6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65e78 bytes bf420839
+ 00b66e6c bytes bf420739
- 00b65e94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65e94 ["INT_ADD", "register:40f0:8", ["const:b65e94:8", "const:4:8"]]
- 00b65e94 ["CALLIND", null, ["register:0:8"]]
+ 00b66e88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66e88 ["INT_ADD", "register:40f0:8", ["const:b66e88:8", "const:4:8"]]
+ 00b66e88 ["CALLIND", null, ["register:0:8"]]
- 00b65e94 bytes 00013fd6
+ 00b66e88 bytes 00013fd6
- 00b65e98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:208:8"]]
- 00b65e98 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b65e98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b66e8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1c8:8"]]
+ 00b66e8c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b66e8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b65e98 bytes 9f0601f9
+ 00b66e8c bytes 9fe600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dc8ee9e4706580ff84cf68c0bbdd28c"></a>

### [`00b65eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65eac.md) → [`00b66ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ea0.md) _ZN8firebase7options14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66ee0",
      "incomplete_value": true,
      "site": "00b66ee0",
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
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65eec",
      "incomplete_value": true,
      "site": "00b65eec",
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
            "const:208:8"
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
      "definition_site": "00b66ebc",
      "incomplete_value": true,
      "site": "00b66ebc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65ec8",
      "incomplete_value": true,
      "site": "00b65ec8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66ec4",
      "incomplete_value": false,
      "site": "00b66ed8",
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
            "const:a7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ed0",
      "incomplete_value": false,
      "site": "00b65ee4",
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
            "const:9ab:8"
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
      "00b66eb4",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66ec4",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b66ee0",
      "WRITE",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66eb4",
      "READ",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66ec4",
      "PARAM",
      [
        "storage",
        "002b5a7a",
        null,
        "string"
      ]
    ],
    [
      "00b66ee0",
      "WRITE",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65eac.md#insn-00b65ee4) · [`00b65eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65eac.md#insn-00b65eec) · [`00b65eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65eac.md#insn-00b65eb8)
- 新版 [`00b66ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ea0.md#insn-00b66ed8) · [`00b66ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ea0.md#insn-00b66ee0) · [`00b66eac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ea0.md#insn-00b66eac)

~~~diff
- 00b65ee4 ["INT_ADD", "register:40f0:8", ["const:b65ee4:8", "const:4:8"]]
- 00b65ee4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66ed8 ["INT_ADD", "register:40f0:8", ["const:b66ed8:8", "const:4:8"]]
+ 00b66ed8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65ee4 bytes 3fd40394
+ 00b66ed8 bytes 36d40394
- 00b65eec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:208:8"]]
- 00b65eec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66ee0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1c8:8"]]
+ 00b66ee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65eec bytes 800601f9
+ 00b66ee0 bytes 80e600f9
- 00b65eb8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00b66eac ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00b65eb8 bytes 142e00b0
+ 00b66eac bytes 142e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c85a59c95e04fab071be4f15c92a64c"></a>

### [`00b65f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65f1c.md) → [`00b66f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66f10.md) _ZN8firebase7options11GetMethodIdENS0_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66f2c",
      "incomplete_value": false,
      "site": "00b66f30",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f38",
      "incomplete_value": false,
      "site": "00b65f3c",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b66f3c",
      "incomplete_value": true,
      "site": "00b66f48",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f48",
      "incomplete_value": true,
      "site": "00b65f54",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b66f2c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b66f3c",
      "DATA",
      [
        "storage",
        "01126218",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66f2c",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b66f3c",
      "DATA",
      [
        "storage",
        "011271d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65f1c.md#insn-00b65f3c) · [`00b65f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65f1c.md#insn-00b65f38) · [`00b65f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65f1c.md#insn-00b65f40)
- 新版 [`00b66f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66f10.md#insn-00b66f30) · [`00b66f2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66f10.md#insn-00b66f2c) · [`00b66f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66f10.md#insn-00b66f34)

~~~diff
- 00b65f3c ["INT_ADD", "register:40f0:8", ["const:b65f3c:8", "const:4:8"]]
- 00b65f3c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b66f30 ["INT_ADD", "register:40f0:8", ["const:b66f30:8", "const:4:8"]]
+ 00b66f30 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b65f3c bytes 65d40394
+ 00b66f30 bytes 5cd40394
- 00b65f38 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b65f38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65f38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65f38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66f2c ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b66f2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66f2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66f2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65f38 bytes 002c0c91
+ 00b66f2c bytes 008c1191
- 00b65f40 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b66f34 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b65f40 bytes 082e00b0
+ 00b66f34 bytes 082e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd570cbf457144691d3fc6fb408b5bae"></a>

### [`00b65f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65f58.md) → [`00b66f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66f4c.md) _ZN8firebase7options13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66f8c",
      "incomplete_value": true,
      "site": "00b66f8c",
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
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f98",
      "incomplete_value": true,
      "site": "00b65f98",
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
            "const:208:8"
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
      "definition_site": "00b66f68",
      "incomplete_value": true,
      "site": "00b66f68",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b65f74",
      "incomplete_value": true,
      "site": "00b65f74",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66f70",
      "incomplete_value": false,
      "site": "00b66f84",
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
            "const:a7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f7c",
      "incomplete_value": false,
      "site": "00b65f90",
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
            "const:9ab:8"
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
      "00b66f60",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66f70",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b66f8c",
      "WRITE",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66f60",
      "READ",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66f70",
      "PARAM",
      [
        "storage",
        "002b5a7a",
        null,
        "string"
      ]
    ],
    [
      "00b66f8c",
      "WRITE",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65f58.md#insn-00b65f90) · [`00b65f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65f58.md#insn-00b65f98) · [`00b65f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65f58.md#insn-00b65f64)
- 新版 [`00b66f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66f4c.md#insn-00b66f84) · [`00b66f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66f4c.md#insn-00b66f8c) · [`00b66f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66f4c.md#insn-00b66f58)

~~~diff
- 00b65f90 ["INT_ADD", "register:40f0:8", ["const:b65f90:8", "const:4:8"]]
- 00b65f90 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b66f84 ["INT_ADD", "register:40f0:8", ["const:b66f84:8", "const:4:8"]]
+ 00b66f84 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b65f90 bytes 14d40394
+ 00b66f84 bytes 0bd40394
- 00b65f98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:208:8"]]
- 00b65f98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66f8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1c8:8"]]
+ 00b66f8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65f98 bytes 800601f9
+ 00b66f8c bytes 80e600f9
- 00b65f64 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00b66f58 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00b65f64 bytes 142e00b0
+ 00b66f58 bytes 142e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5a629bccd3c731e8264b412482ca6b3"></a>

### [`00b65fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65fc8.md) → [`00b66fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66fbc.md) _ZN8firebase7options10GetFieldIdENS0_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66fd8",
      "incomplete_value": false,
      "site": "00b66fdc",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65fe4",
      "incomplete_value": false,
      "site": "00b65fe8",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b66fe8",
      "incomplete_value": true,
      "site": "00b66ff4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ff4",
      "incomplete_value": true,
      "site": "00b66000",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b66fd8",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b66fe8",
      "DATA",
      [
        "storage",
        "01126250",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b66fd8",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b66fe8",
      "DATA",
      [
        "storage",
        "01127210",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65fc8.md#insn-00b65fe8) · [`00b65fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65fc8.md#insn-00b65fe4) · [`00b65fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65fc8.md#insn-00b65fec)
- 新版 [`00b66fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66fbc.md#insn-00b66fdc) · [`00b66fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66fbc.md#insn-00b66fd8) · [`00b66fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66fbc.md#insn-00b66fe0)

~~~diff
- 00b65fe8 ["INT_ADD", "register:40f0:8", ["const:b65fe8:8", "const:4:8"]]
- 00b65fe8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b66fdc ["INT_ADD", "register:40f0:8", ["const:b66fdc:8", "const:4:8"]]
+ 00b66fdc ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b65fe8 bytes 3ad40394
+ 00b66fdc bytes 31d40394
- 00b65fe4 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b65fe4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65fe4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65fe4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66fd8 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b66fd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66fd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66fd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65fe4 bytes 00341591
+ 00b66fd8 bytes 00681891
- 00b65fec ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b66fe0 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b65fec bytes 082e00b0
+ 00b66fe0 bytes 082e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4864e8a7faacbd570a37e80c0a59346e"></a>

### [`00b66004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66004.md) → [`00b66ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ff8.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b67024",
      "incomplete_value": true,
      "site": "00b67024",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66030",
      "incomplete_value": true,
      "site": "00b66030",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6700c",
      "incomplete_value": true,
      "site": "00b6700c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66018",
      "incomplete_value": true,
      "site": "00b66018",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b67018",
      "incomplete_value": false,
      "site": "00b6701c",
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
            "const:a04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66024",
      "incomplete_value": false,
      "site": "00b66028",
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
            "const:9ba:8"
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
      "00b67008",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67018",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b67024",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67008",
      "READ",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67018",
      "PARAM",
      [
        "storage",
        "002c0a04",
        null,
        "string"
      ]
    ],
    [
      "00b67024",
      "WRITE",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66004.md#insn-00b66028) · [`00b66030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66004.md#insn-00b66030) · [`00b66010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66004.md#insn-00b66010)
- 新版 [`00b6701c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ff8.md#insn-00b6701c) · [`00b67024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ff8.md#insn-00b67024) · [`00b67004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66ff8.md#insn-00b67004)

~~~diff
- 00b66028 ["INT_ADD", "register:40f0:8", ["const:b66028:8", "const:4:8"]]
- 00b66028 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b6701c ["INT_ADD", "register:40f0:8", ["const:b6701c:8", "const:4:8"]]
+ 00b6701c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b66028 bytes eed30394
+ 00b6701c bytes e5d30394
- 00b66030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00b66030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67024 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b67024 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66030 bytes 602e01f9
+ 00b67024 bytes 600e01f9
- 00b66010 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b67004 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b66010 bytes 132e0090
+ 00b67004 bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8b8c14ed031bc14fb4bc9b3b7871762"></a>

### [`00b66044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66044.md) → [`00b67038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67038.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b67064",
      "incomplete_value": true,
      "site": "00b67064",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66070",
      "incomplete_value": true,
      "site": "00b66070",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6704c",
      "incomplete_value": true,
      "site": "00b6704c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66058",
      "incomplete_value": true,
      "site": "00b66058",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b67054",
      "incomplete_value": false,
      "site": "00b6705c",
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
            "const:a04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66060",
      "incomplete_value": false,
      "site": "00b66068",
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
            "const:9ba:8"
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
      "00b67048",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67054",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b67064",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67048",
      "READ",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67054",
      "PARAM",
      [
        "storage",
        "002c0a04",
        null,
        "string"
      ]
    ],
    [
      "00b67064",
      "WRITE",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66044.md#insn-00b66068) · [`00b66070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66044.md#insn-00b66070) · [`00b66050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66044.md#insn-00b66050)
- 新版 [`00b6705c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67038.md#insn-00b6705c) · [`00b67064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67038.md#insn-00b67064) · [`00b67044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67038.md#insn-00b67044)

~~~diff
- 00b66068 ["INT_ADD", "register:40f0:8", ["const:b66068:8", "const:4:8"]]
- 00b66068 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b6705c ["INT_ADD", "register:40f0:8", ["const:b6705c:8", "const:4:8"]]
+ 00b6705c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b66068 bytes ded30394
+ 00b6705c bytes d5d30394
- 00b66070 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00b66070 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67064 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b67064 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66070 bytes 602e01f9
+ 00b67064 bytes 600e01f9
- 00b66050 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b67044 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b66050 bytes 132e0090
+ 00b67044 bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bf9db1446c1cc92b613468eac7d8fc7"></a>

### [`00b66084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66084.md) → [`00b67078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67078.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b670a8",
      "incomplete_value": true,
      "site": "00b670a8",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b660b4",
      "incomplete_value": true,
      "site": "00b660b4",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6708c",
      "incomplete_value": true,
      "site": "00b6708c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66098",
      "incomplete_value": true,
      "site": "00b66098",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b67098",
      "incomplete_value": false,
      "site": "00b670a0",
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
            "const:a04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b660a4",
      "incomplete_value": false,
      "site": "00b660ac",
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
            "const:9ba:8"
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
      "00b67088",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67098",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b670a8",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67088",
      "READ",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67098",
      "PARAM",
      [
        "storage",
        "002c0a04",
        null,
        "string"
      ]
    ],
    [
      "00b670a8",
      "WRITE",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b660ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66084.md#insn-00b660ac) · [`00b660b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66084.md#insn-00b660b4) · [`00b66090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66084.md#insn-00b66090)
- 新版 [`00b670a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67078.md#insn-00b670a0) · [`00b670a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67078.md#insn-00b670a8) · [`00b67084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67078.md#insn-00b67084)

~~~diff
- 00b660ac ["INT_ADD", "register:40f0:8", ["const:b660ac:8", "const:4:8"]]
- 00b660ac ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b670a0 ["INT_ADD", "register:40f0:8", ["const:b670a0:8", "const:4:8"]]
+ 00b670a0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b660ac bytes cdd30394
+ 00b670a0 bytes c4d30394
- 00b660b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00b660b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b670a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b670a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b660b4 bytes 602e01f9
+ 00b670a8 bytes 600e01f9
- 00b66090 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b67084 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b66090 bytes 132e0090
+ 00b67084 bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26a9107b55f673d550a5c14f13ca9521"></a>

### [`00b660c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b660c8.md) → [`00b670bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b670bc.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b670ec",
      "incomplete_value": true,
      "site": "00b670ec",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b660f8",
      "incomplete_value": true,
      "site": "00b660f8",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b670d0",
      "incomplete_value": true,
      "site": "00b670d0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b660dc",
      "incomplete_value": true,
      "site": "00b660dc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b670d8",
      "incomplete_value": false,
      "site": "00b670e4",
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
            "const:a04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b660e4",
      "incomplete_value": false,
      "site": "00b660f0",
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
            "const:9ba:8"
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
      "00b670cc",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b670d8",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b670ec",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b670cc",
      "READ",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b670d8",
      "PARAM",
      [
        "storage",
        "002c0a04",
        null,
        "string"
      ]
    ],
    [
      "00b670ec",
      "WRITE",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b660f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b660c8.md#insn-00b660f0) · [`00b660f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b660c8.md#insn-00b660f8) · [`00b660d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b660c8.md#insn-00b660d4)
- 新版 [`00b670e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b670bc.md#insn-00b670e4) · [`00b670ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b670bc.md#insn-00b670ec) · [`00b670c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b670bc.md#insn-00b670c8)

~~~diff
- 00b660f0 ["INT_ADD", "register:40f0:8", ["const:b660f0:8", "const:4:8"]]
- 00b660f0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b670e4 ["INT_ADD", "register:40f0:8", ["const:b670e4:8", "const:4:8"]]
+ 00b670e4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b660f0 bytes bcd30394
+ 00b670e4 bytes b3d30394
- 00b660f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00b660f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b670ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b670ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b660f8 bytes 602e01f9
+ 00b670ec bytes 600e01f9
- 00b660d4 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00b670c8 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00b660d4 bytes 132e0090
+ 00b670c8 bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87e528aa0b629936236de1e48960b3f4"></a>

### [`00b66118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66118.md) → [`00b6710c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b6710c.md) _ZN8firebase17version_registrar15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b67164",
      "incomplete_value": true,
      "site": "00b67164",
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
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66170",
      "incomplete_value": true,
      "site": "00b66170",
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
            "const:260:8"
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
      "definition_site": "00b67140",
      "incomplete_value": true,
      "site": "00b6714c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:218:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6614c",
      "incomplete_value": true,
      "site": "00b66158",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:258:8"
              ]
            ]
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
      "00b67120",
      "READ",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67140",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67164",
      "WRITE",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67120",
      "READ",
      [
        "storage",
        "01127220",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67140",
      "READ",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67164",
      "WRITE",
      [
        "storage",
        "01127220",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66118.md#insn-00b66158) · [`00b66170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66118.md#insn-00b66170) · [`00b66128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66118.md#insn-00b66128)
- 新版 [`00b6714c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b6710c.md#insn-00b6714c) · [`00b67164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b6710c.md#insn-00b67164) · [`00b6711c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b6710c.md#insn-00b6711c)

~~~diff
- 00b66158 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66158 ["INT_ADD", "register:40f0:8", ["const:b66158:8", "const:4:8"]]
- 00b66158 ["CALLIND", null, ["register:0:8"]]
+ 00b6714c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6714c ["INT_ADD", "register:40f0:8", ["const:b6714c:8", "const:4:8"]]
+ 00b6714c ["CALLIND", null, ["register:0:8"]]
- 00b66158 bytes 00013fd6
+ 00b6714c bytes 00013fd6
- 00b66170 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b66170 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:260:8"]]
- 00b66170 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b67164 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b67164 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:220:8"]]
+ 00b67164 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b66170 bytes a0820939
+ 00b67164 bytes a0820839
- 00b66128 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00b6711c ["COPY", "register:40a8:8", ["const:1127000:8"]]
- 00b66128 bytes 152e0090
+ 00b6711c bytes 152e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c056f43229c42ea119f4955999f05320"></a>

### [`00b66184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66184.md) → [`00b67178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67178.md) _ZN8firebase17version_registrar12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b671b4",
      "incomplete_value": true,
      "site": "00b671b4",
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
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b661c0",
      "incomplete_value": true,
      "site": "00b661c0",
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
            "const:260:8"
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
      "definition_site": "00b671d4",
      "incomplete_value": true,
      "site": "00b671d4",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b661e0",
      "incomplete_value": true,
      "site": "00b661e0",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67190",
      "incomplete_value": true,
      "site": "00b67190",
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
      "definition_site": "00b6619c",
      "incomplete_value": true,
      "site": "00b6619c",
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
      "00b6718c",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67198",
      "READ",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ],
    [
      "00b671b4",
      "WRITE",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6718c",
      "READ",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67198",
      "READ",
      [
        "storage",
        "01127220",
        null,
        "undefined1"
      ]
    ],
    [
      "00b671b4",
      "WRITE",
      [
        "storage",
        "01127220",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b661c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66184.md#insn-00b661c0) · [`00b661dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66184.md#insn-00b661dc) · [`00b661e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66184.md#insn-00b661e0)
- 新版 [`00b671b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67178.md#insn-00b671b4) · [`00b671d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67178.md#insn-00b671d0) · [`00b671d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67178.md#insn-00b671d4)

~~~diff
- 00b661c0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b661c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b661c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:260:8"]]
- 00b661c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b671b4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b671b4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b671b4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:220:8"]]
+ 00b671b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b661c0 bytes bf820939
+ 00b671b4 bytes bf820839
- 00b661dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b661dc ["INT_ADD", "register:40f0:8", ["const:b661dc:8", "const:4:8"]]
- 00b661dc ["CALLIND", null, ["register:0:8"]]
+ 00b671d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b671d0 ["INT_ADD", "register:40f0:8", ["const:b671d0:8", "const:4:8"]]
+ 00b671d0 ["CALLIND", null, ["register:0:8"]]
- 00b661dc bytes 00013fd6
+ 00b671d0 bytes 00013fd6
- 00b661e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
- 00b661e0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b661e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b671d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
+ 00b671d4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b671d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b661e0 bytes 9f2e01f9
+ 00b671d4 bytes 9f0e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b4f069dd6e9f17e56fb4ecad90be4f1"></a>

### [`00b661f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b661f4.md) → [`00b671e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b671e8.md) _ZN8firebase17version_registrar14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b67228",
      "incomplete_value": true,
      "site": "00b67228",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66234",
      "incomplete_value": true,
      "site": "00b66234",
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
            "const:258:8"
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
      "definition_site": "00b67204",
      "incomplete_value": true,
      "site": "00b67204",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b66210",
      "incomplete_value": true,
      "site": "00b66210",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b6720c",
      "incomplete_value": false,
      "site": "00b67220",
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
            "const:a04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66218",
      "incomplete_value": false,
      "site": "00b6622c",
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
            "const:9ba:8"
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
      "00b671fc",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6720c",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b67228",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b671fc",
      "READ",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6720c",
      "PARAM",
      [
        "storage",
        "002c0a04",
        null,
        "string"
      ]
    ],
    [
      "00b67228",
      "WRITE",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6622c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b661f4.md#insn-00b6622c) · [`00b66234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b661f4.md#insn-00b66234) · [`00b66200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b661f4.md#insn-00b66200)
- 新版 [`00b67220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b671e8.md#insn-00b67220) · [`00b67228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b671e8.md#insn-00b67228) · [`00b671f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b671e8.md#insn-00b671f4)

~~~diff
- 00b6622c ["INT_ADD", "register:40f0:8", ["const:b6622c:8", "const:4:8"]]
- 00b6622c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b67220 ["INT_ADD", "register:40f0:8", ["const:b67220:8", "const:4:8"]]
+ 00b67220 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b6622c bytes 6dd30394
+ 00b67220 bytes 64d30394
- 00b66234 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
- 00b66234 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67228 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
+ 00b67228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66234 bytes 802e01f9
+ 00b67228 bytes 800e01f9
- 00b66200 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00b671f4 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00b66200 bytes 142e0090
+ 00b671f4 bytes 142e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff1dda04d8c3cf890f6d9f987b00808b"></a>

### [`00b66264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66264.md) → [`00b67258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67258.md) _ZN8firebase17version_registrar11GetMethodIdENS0_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67274",
      "incomplete_value": false,
      "site": "00b67278",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66280",
      "incomplete_value": false,
      "site": "00b66284",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b67284",
      "incomplete_value": true,
      "site": "00b67290",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66290",
      "incomplete_value": true,
      "site": "00b6629c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b67274",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b67284",
      "DATA",
      [
        "storage",
        "01126268",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67274",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b67284",
      "DATA",
      [
        "storage",
        "01127228",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66264.md#insn-00b66284) · [`00b66280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66264.md#insn-00b66280) · [`00b66288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66264.md#insn-00b66288)
- 新版 [`00b67278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67258.md#insn-00b67278) · [`00b67274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67258.md#insn-00b67274) · [`00b6727c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67258.md#insn-00b6727c)

~~~diff
- 00b66284 ["INT_ADD", "register:40f0:8", ["const:b66284:8", "const:4:8"]]
- 00b66284 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b67278 ["INT_ADD", "register:40f0:8", ["const:b67278:8", "const:4:8"]]
+ 00b67278 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b66284 bytes 93d30394
+ 00b67278 bytes 8ad30394
- 00b66280 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b66280 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66280 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66280 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67274 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b67274 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67274 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67274 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66280 bytes 002c0c91
+ 00b67274 bytes 008c1191
- 00b66288 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b6727c ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b66288 bytes 082e0090
+ 00b6727c bytes 082e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df63b0f9f12f87099aea47f999b1f60c"></a>

### [`00b662a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b662a0.md) → [`00b67294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67294.md) _ZN8firebase17version_registrar13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b672d4",
      "incomplete_value": true,
      "site": "00b672d4",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662e0",
      "incomplete_value": true,
      "site": "00b662e0",
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
            "const:258:8"
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
      "definition_site": "00b672b0",
      "incomplete_value": true,
      "site": "00b672b0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b662bc",
      "incomplete_value": true,
      "site": "00b662bc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b672b8",
      "incomplete_value": false,
      "site": "00b672cc",
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
            "const:a04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662c4",
      "incomplete_value": false,
      "site": "00b662d8",
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
            "const:9ba:8"
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
      "00b672a8",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b672b8",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b672d4",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b672a8",
      "READ",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b672b8",
      "PARAM",
      [
        "storage",
        "002c0a04",
        null,
        "string"
      ]
    ],
    [
      "00b672d4",
      "WRITE",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b662d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b662a0.md#insn-00b662d8) · [`00b662e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b662a0.md#insn-00b662e0) · [`00b662ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b662a0.md#insn-00b662ac)
- 新版 [`00b672cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67294.md#insn-00b672cc) · [`00b672d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67294.md#insn-00b672d4) · [`00b672a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67294.md#insn-00b672a0)

~~~diff
- 00b662d8 ["INT_ADD", "register:40f0:8", ["const:b662d8:8", "const:4:8"]]
- 00b662d8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b672cc ["INT_ADD", "register:40f0:8", ["const:b672cc:8", "const:4:8"]]
+ 00b672cc ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b662d8 bytes 42d30394
+ 00b672cc bytes 39d30394
- 00b662e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
- 00b662e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b672d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
+ 00b672d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b662e0 bytes 802e01f9
+ 00b672d4 bytes 800e01f9
- 00b662ac ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00b672a0 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00b662ac bytes 142e0090
+ 00b672a0 bytes 142e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c4096a956559aa81ed504da6af67de0"></a>

### [`00b66310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66310.md) → [`00b67304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67304.md) _ZN8firebase17version_registrar10GetFieldIdENS0_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67320",
      "incomplete_value": false,
      "site": "00b67324",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6632c",
      "incomplete_value": false,
      "site": "00b66330",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b67330",
      "incomplete_value": true,
      "site": "00b6733c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6633c",
      "incomplete_value": true,
      "site": "00b66348",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b67320",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b67330",
      "DATA",
      [
        "storage",
        "01126280",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b67320",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b67330",
      "DATA",
      [
        "storage",
        "01127240",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66310.md#insn-00b66330) · [`00b6632c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66310.md#insn-00b6632c) · [`00b66334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66310.md#insn-00b66334)
- 新版 [`00b67324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67304.md#insn-00b67324) · [`00b67320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67304.md#insn-00b67320) · [`00b67328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67304.md#insn-00b67328)

~~~diff
- 00b66330 ["INT_ADD", "register:40f0:8", ["const:b66330:8", "const:4:8"]]
- 00b66330 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b67324 ["INT_ADD", "register:40f0:8", ["const:b67324:8", "const:4:8"]]
+ 00b67324 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b66330 bytes 68d30394
+ 00b67324 bytes 5fd30394
- 00b6632c ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b6632c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6632c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6632c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67320 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b67320 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67320 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67320 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6632c bytes 00341591
+ 00b67320 bytes 00681891
- 00b66334 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b67328 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b66334 bytes 082e0090
+ 00b67328 bytes 082e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b64588acbda9d3ca08dc7999c54640b"></a>

### [`00b6634c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b6634c.md) → [`00b67340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67340.md) _ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bf90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf90.md) · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md) [`00b666d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b666d8.md) [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00c5cf60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf60.md) · 呼出先 13件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00b674e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b674e4.md) [`00b676cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b676cc.md) [`00b67ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67ad8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67388",
      "incomplete_value": true,
      "site": "00b67398",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:1c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66394",
      "incomplete_value": true,
      "site": "00b663a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:208:8"
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
      "definition_site": "00b6738c",
      "incomplete_value": true,
      "site": "00b67398",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
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
      "definition_site": "00b66398",
      "incomplete_value": true,
      "site": "00b663a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:218:8"
              ]
            ]
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
      "00b67388",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6738c",
      "READ",
      [
        "storage",
        "01126218",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67388",
      "READ",
      [
        "storage",
        "011271c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6738c",
      "READ",
      [
        "storage",
        "011271d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b663a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b6634c.md#insn-00b663a4) · [`00b66384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b6634c.md#insn-00b66384) · [`00b6638c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b6634c.md#insn-00b6638c)
- 新版 [`00b67398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67340.md#insn-00b67398) · [`00b67378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67340.md#insn-00b67378) · [`00b67380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67340.md#insn-00b67380)

~~~diff
- 00b663a4 ["INT_ADD", "register:40f0:8", ["const:b663a4:8", "const:4:8"]]
- 00b663a4 ["CALL", null, ["callee:00c5bc40:8"]]
+ 00b67398 ["INT_ADD", "register:40f0:8", ["const:b67398:8", "const:4:8"]]
+ 00b67398 ["CALL", null, ["callee:00c5bc40:8"]]
- 00b663a4 bytes 33d20394
+ 00b67398 bytes 2ad20394
- 00b66384 ["INT_ADD", "register:40f0:8", ["const:b66384:8", "const:4:8"]]
- 00b66384 ["CALL", null, ["callee:00b674e4:8"]]
+ 00b67378 ["INT_ADD", "register:40f0:8", ["const:b67378:8", "const:4:8"]]
+ 00b67378 ["CALL", null, ["callee:00b674e4:8"]]
- 00b66384 bytes 5b000094
+ 00b67378 bytes 5b000094
- 00b6638c ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00b67380 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00b6638c bytes 082e0090
+ 00b67380 bytes 082e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f89a23c14c5a698e70b77951f9dd577"></a>

### [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md) → [`00b674e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b674e4.md) FUN_00b674e4

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b6634c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b6634c.md) [`00b66d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66d48.md) [`00b66e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66e40.md) [`00b682dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md) · 呼出先 5件 [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md) [`00c5af70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af70.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md) [`00c5bdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdd0.md)
- 新版 呼出元 4件 [`00b67340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67340.md) [`00b67d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67d3c.md) [`00b67e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67e34.md) [`00b692d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b692d0.md) · 呼出先 5件 [`00b67ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67ad8.md) [`00c5bf40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf40.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md) [`00c5cda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cda0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 81.97% / 新版 81.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 4件, `store_condition` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b67500",
      "incomplete_value": false,
      "site": "00b67500",
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
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6650c",
      "incomplete_value": false,
      "site": "00b6650c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:288:8"
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
      "definition_site": "00b6754c",
      "incomplete_value": true,
      "site": "00b6754c",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66558",
      "incomplete_value": true,
      "site": "00b66558",
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
            "const:150:8"
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
      "definition_site": "00b675a4",
      "incomplete_value": true,
      "site": "00b675a4",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b665b0",
      "incomplete_value": true,
      "site": "00b665b0",
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
            "const:1b0:8"
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
      "00b674f8",
      "READ",
      [
        "storage",
        "01126288",
        null,
        "undefined4"
      ]
    ],
    [
      "00b67500",
      "WRITE",
      [
        "storage",
        "01126288",
        null,
        "undefined4"
      ]
    ],
    [
      "00b67524",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b674f8",
      "READ",
      [
        "storage",
        "01127248",
        null,
        "undefined4"
      ]
    ],
    [
      "00b67500",
      "WRITE",
      [
        "storage",
        "01127248",
        null,
        "undefined4"
      ]
    ],
    [
      "00b67524",
      "READ",
      [
        "storage",
        "01127110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6650c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md#insn-00b6650c) · [`00b66550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md#insn-00b66550) · [`00b66558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md#insn-00b66558)
- 新版 [`00b67500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b674e4.md#insn-00b67500) · [`00b67544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b674e4.md#insn-00b67544) · [`00b6754c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b674e4.md#insn-00b6754c)

~~~diff
- 00b6650c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:288:8"]]
- 00b6650c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b67500 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:248:8"]]
+ 00b67500 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b6650c bytes a98a02b9
+ 00b67500 bytes a94a02b9
- 00b66550 ["INT_ADD", "register:40f0:8", ["const:b66550:8", "const:4:8"]]
- 00b66550 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b67544 ["INT_ADD", "register:40f0:8", ["const:b67544:8", "const:4:8"]]
+ 00b67544 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b66550 bytes a4d20394
+ 00b67544 bytes 9bd20394
- 00b66558 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:150:8"]]
- 00b66558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6754c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:110:8"]]
+ 00b6754c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66558 bytes a0aa00f9
+ 00b6754c bytes a08a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c0520791f3fa4fe66372d3d88dad61b"></a>

### [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md) → [`00b67ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67ad8.md) FUN_00b67ad8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00b6634c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b6634c.md) [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md) [`00b66c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66c94.md) [`00b66d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66d48.md) [`00b66e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66e40.md) · 呼出先 4件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0a0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5bdf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdf0.md)
- 新版 呼出元 6件 [`00b67340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67340.md) [`00b674e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b674e4.md) [`00b67c88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67c88.md) [`00b67d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67d3c.md) [`00b67e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67e34.md) · 呼出先 4件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c070.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5cdc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cdc0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.05% / 新版 85.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 10件

アドレスに依存する影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b67b0c",
      "incomplete_value": true,
      "site": "00b67b0c",
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
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66b18",
      "incomplete_value": true,
      "site": "00b66b18",
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
            "const:288:8"
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
      "definition_site": "00b67b4c",
      "incomplete_value": true,
      "site": "00b67b4c",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66b58",
      "incomplete_value": true,
      "site": "00b66b58",
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
            "const:158:8"
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
      "definition_site": "00b67b6c",
      "incomplete_value": true,
      "site": "00b67b6c",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66b78",
      "incomplete_value": true,
      "site": "00b66b78",
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
            "const:150:8"
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
      "00b67aec",
      "READ",
      [
        "storage",
        "01126288",
        null,
        "undefined4"
      ]
    ],
    [
      "00b67afc",
      "PARAM",
      [
        "storage",
        "002bbdfe",
        null,
        "string"
      ]
    ],
    [
      "00b67b04",
      "READ",
      [
        "storage",
        "01126288",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b67aec",
      "READ",
      [
        "storage",
        "01127248",
        null,
        "undefined4"
      ]
    ],
    [
      "00b67afc",
      "PARAM",
      [
        "storage",
        "002bbedc",
        null,
        "string"
      ]
    ],
    [
      "00b67b04",
      "READ",
      [
        "storage",
        "01127248",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md#insn-00b66b0c) · [`00b66b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md#insn-00b66b18) · [`00b66b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md#insn-00b66b58)
- 新版 [`00b67b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67ad8.md#insn-00b67b00) · [`00b67b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67ad8.md#insn-00b67b0c) · [`00b67b4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67ad8.md#insn-00b67b4c)

~~~diff
- 00b66b0c ["INT_ADD", "register:40f0:8", ["const:b66b0c:8", "const:4:8"]]
- 00b66b0c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b67b00 ["INT_ADD", "register:40f0:8", ["const:b67b00:8", "const:4:8"]]
+ 00b67b00 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b66b0c bytes 71d10394
+ 00b67b00 bytes 68d10394
- 00b66b18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:288:8"]]
- 00b66b18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b67b0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:248:8"]]
+ 00b67b0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b66b18 bytes 888a02b9
+ 00b67b0c bytes 884a02b9
- 00b66b58 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b66b58 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b66b58 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:158:8"]]
- 00b66b58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b67b4c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b67b4c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b67b4c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:118:8"]]
+ 00b67b4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b66b58 bytes bf620539
+ 00b67b4c bytes bf620439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8e8d8398677f7bf12b3af6e7b35b750"></a>

### [`00b66d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66d48.md) → [`00b67d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67d3c.md) _ZN8firebase3App6CreateEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5aa20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa20.md) · 呼出先 7件 [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md) [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md)
- 新版 呼出元 1件 [`00c5b9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b9f0.md) · 呼出先 7件 [`0087ac8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087ac8c.md) [`00b674e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b674e4.md) [`00b67ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67ad8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

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
      "definition_site": "00b67db8",
      "incomplete_value": true,
      "site": "00b67dbc",
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
      "definition_site": "00b66dc4",
      "incomplete_value": true,
      "site": "00b66dc8",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67dd4",
      "incomplete_value": false,
      "site": "00b67dd8",
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
            "const:dbe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66de0",
      "incomplete_value": false,
      "site": "00b66de4",
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
            "const:cef:8"
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
      "00b67da8",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00b67db8",
      "READ",
      [
        "storage",
        "00c902d0",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b67db8",
      "PARAM",
      [
        "storage",
        "002b5972",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b67da8",
      "READ",
      [
        "storage",
        "00c9c818",
        null,
        "pointer"
      ]
    ],
    [
      "00b67db8",
      "READ",
      [
        "storage",
        "00c912a0",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b67db8",
      "PARAM",
      [
        "storage",
        "002b5a41",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66d48.md#insn-00b66dc8) · [`00b66de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66d48.md#insn-00b66de4) · [`00b66d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66d48.md#insn-00b66d70)
- 新版 [`00b67dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67d3c.md#insn-00b67dbc) · [`00b67dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67d3c.md#insn-00b67dd8) · [`00b67d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67d3c.md#insn-00b67d64)

~~~diff
- 00b66dc8 ["INT_ADD", "register:40f0:8", ["const:b66dc8:8", "const:4:8"]]
- 00b66dc8 ["CALL", null, ["callee:00c5cf70:8"]]
+ 00b67dbc ["INT_ADD", "register:40f0:8", ["const:b67dbc:8", "const:4:8"]]
+ 00b67dbc ["CALL", null, ["callee:00c5cf70:8"]]
- 00b66dc8 bytes 76d40394
+ 00b67dbc bytes 6dd40394
- 00b66de4 ["INT_ADD", "register:40f0:8", ["const:b66de4:8", "const:4:8"]]
- 00b66de4 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b67dd8 ["INT_ADD", "register:40f0:8", ["const:b67dd8:8", "const:4:8"]]
+ 00b67dd8 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b66de4 bytes e3cf0394
+ 00b67dd8 bytes dacf0394
- 00b66d70 ["INT_ADD", "register:40f0:8", ["const:b66d70:8", "const:4:8"]]
- 00b66d70 ["CALL", null, ["callee:00b674e4:8"]]
+ 00b67d64 ["INT_ADD", "register:40f0:8", ["const:b67d64:8", "const:4:8"]]
+ 00b67d64 ["CALL", null, ["callee:00b674e4:8"]]
- 00b66d70 bytes e0fdff97
+ 00b67d64 bytes e0fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8649cff2dac1017ac9436e311b9d6a32"></a>

### [`00b66e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66e40.md) → [`00b67e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67e34.md) _ZN8firebase3App6CreateERKNS_10AppOptionsEPKcP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bfa0.md) · 呼出先 28件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md)
- 新版 呼出元 1件 [`00c5cf70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf70.md) · 呼出先 28件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00589a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`0087ac8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087ac8c.md) [`00b674e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b674e4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.57% / 新版 98.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件

アドレスに依存する影響 `call_argument_candidate` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b67e84",
      "incomplete_value": false,
      "site": "00b67e8c",
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
            "const:a79:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66e90",
      "incomplete_value": false,
      "site": "00b66e98",
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
            "const:a39:8"
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
      "definition_site": "00b67ea0",
      "incomplete_value": false,
      "site": "00b67eac",
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
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66eac",
      "incomplete_value": false,
      "site": "00b66eb8",
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
            "const:16a:8"
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
      "definition_site": "00b67ea8",
      "incomplete_value": true,
      "site": "00b67eac",
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
      "definition_site": "00b66eb4",
      "incomplete_value": true,
      "site": "00b66eb8",
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
      "00b67e84",
      "PARAM",
      [
        "storage",
        "0029fa39",
        null,
        "string"
      ]
    ],
    [
      "00b67e98",
      "READ",
      [
        "storage",
        "00c9b8c8",
        null,
        "pointer"
      ]
    ],
    [
      "00b67ea0",
      "PARAM",
      [
        "storage",
        "002bd16a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b67e84",
      "PARAM",
      [
        "storage",
        "0029fa79",
        null,
        "string"
      ]
    ],
    [
      "00b67e98",
      "READ",
      [
        "storage",
        "00c9c898",
        null,
        "pointer"
      ]
    ],
    [
      "00b67ea0",
      "PARAM",
      [
        "storage",
        "002bd248",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66e40.md#insn-00b66e98) · [`00b66ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66e40.md#insn-00b66ea4) · [`00b66eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66e40.md#insn-00b66eb8)
- 新版 [`00b67e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67e34.md#insn-00b67e8c) · [`00b67e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67e34.md#insn-00b67e98) · [`00b67eac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67e34.md#insn-00b67eac)

~~~diff
- 00b66e98 ["INT_ADD", "register:40f0:8", ["const:b66e98:8", "const:4:8"]]
- 00b66e98 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b67e8c ["INT_ADD", "register:40f0:8", ["const:b67e8c:8", "const:4:8"]]
+ 00b67e8c ["CALL", null, ["callee:00c5bd40:8"]]
- 00b66e98 bytes b6cf0394
+ 00b67e8c bytes adcf0394
- 00b66ea4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8c8:8"]]
- 00b66ea4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67e98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:898:8"]]
+ 00b67e98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66ea4 bytes 086544f9
+ 00b67e98 bytes 084d44f9
- 00b66eb8 ["INT_ADD", "register:40f0:8", ["const:b66eb8:8", "const:4:8"]]
- 00b66eb8 ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00b67eac ["INT_ADD", "register:40f0:8", ["const:b67eac:8", "const:4:8"]]
+ 00b67eac ["CALL", null, ["callee:00c5c1d0:8"]]
- 00b66eb8 bytes d2d00394
+ 00b67eac bytes c9d00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5db98e96057d36cedf19aa9c9eb0c6a2"></a>

### [`00b680e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b680e4.md) → [`00b690d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b690d8.md) _ZN8firebase3App15RegisterLibraryEPKcS2_Pv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5b880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b880.md) · 呼出先 5件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b7f0.md)
- 新版 呼出元 1件 [`00c5c850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c850.md) · 呼出先 5件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5bc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c7c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.18% / 新版 91.18%

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
      "definition_site": "00b69100",
      "incomplete_value": false,
      "site": "00b69104",
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
            "const:baa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6810c",
      "incomplete_value": false,
      "site": "00b68110",
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
            "const:adb:8"
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
      "definition_site": "00b69110",
      "incomplete_value": true,
      "site": "00b6911c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:218:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6811c",
      "incomplete_value": true,
      "site": "00b68128",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:258:8"
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
      "definition_site": "00b69114",
      "incomplete_value": true,
      "site": "00b6911c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:228:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68120",
      "incomplete_value": true,
      "site": "00b68128",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:268:8"
              ]
            ]
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
      "00b690f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b68114"
      ]
    ],
    [
      "00b69100",
      "PARAM",
      [
        "storage",
        "002b8adb",
        null,
        "string"
      ]
    ],
    [
      "00b69110",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b690f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b69108"
      ]
    ],
    [
      "00b69100",
      "PARAM",
      [
        "storage",
        "002b8baa",
        null,
        "string"
      ]
    ],
    [
      "00b69110",
      "READ",
      [
        "storage",
        "01127218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b680e4.md#insn-00b68110) · [`00b68128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b680e4.md#insn-00b68128) · [`00b68144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b680e4.md#insn-00b68144)
- 新版 [`00b69104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b690d8.md#insn-00b69104) · [`00b6911c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b690d8.md#insn-00b6911c) · [`00b69138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b690d8.md#insn-00b69138)

~~~diff
- 00b68110 ["INT_ADD", "register:40f0:8", ["const:b68110:8", "const:4:8"]]
- 00b68110 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b69104 ["INT_ADD", "register:40f0:8", ["const:b69104:8", "const:4:8"]]
+ 00b69104 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b68110 bytes f0cb0394
+ 00b69104 bytes e7cb0394
- 00b68128 ["INT_ADD", "register:40f0:8", ["const:b68128:8", "const:4:8"]]
- 00b68128 ["CALL", null, ["callee:00c5bc40:8"]]
+ 00b6911c ["INT_ADD", "register:40f0:8", ["const:b6911c:8", "const:4:8"]]
+ 00b6911c ["CALL", null, ["callee:00c5bc40:8"]]
- 00b68128 bytes d2ca0394
+ 00b6911c bytes c9ca0394
- 00b68144 ["INT_ADD", "register:40f0:8", ["const:b68144:8", "const:4:8"]]
- 00b68144 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b69138 ["INT_ADD", "register:40f0:8", ["const:b69138:8", "const:4:8"]]
+ 00b69138 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b68144 bytes e3cb0394
+ 00b69138 bytes dacb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44fd11f386986033200f24f08db383e8"></a>

### [`00b681f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b681f8.md) → [`00b691ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b691ec.md) _ZN8firebase3App31SetDataCollectionDefaultEnabledEb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c460.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b69204",
      "incomplete_value": true,
      "site": "00b69204",
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
      "definition_site": "00b68210",
      "incomplete_value": true,
      "site": "00b68210",
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
      "definition_site": "00b69220",
      "incomplete_value": true,
      "site": "00b69230",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:160:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6822c",
      "incomplete_value": true,
      "site": "00b6823c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:1a0:8"
              ]
            ]
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
      "00b69200",
      "READ",
      [
        "storage",
        "011261a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b69220",
      "READ",
      [
        "storage",
        "011261a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b69254",
      "PARAM",
      [
        "storage",
        "002bd18a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b69200",
      "READ",
      [
        "storage",
        "01127160",
        null,
        "undefined8"
      ]
    ],
    [
      "00b69220",
      "READ",
      [
        "storage",
        "01127160",
        null,
        "undefined8"
      ]
    ],
    [
      "00b69254",
      "PARAM",
      [
        "storage",
        "002bd268",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6823c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b681f8.md#insn-00b6823c) · [`00b68208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b681f8.md#insn-00b68208) · [`00b6820c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b681f8.md#insn-00b6820c)
- 新版 [`00b69230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b691ec.md#insn-00b69230) · [`00b691fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b691ec.md#insn-00b691fc) · [`00b69200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b691ec.md#insn-00b69200)

~~~diff
- 00b6823c ["INT_ADD", "register:40f0:8", ["const:b6823c:8", "const:4:8"]]
- 00b6823c ["CALL", null, ["callee:0057504c:8"]]
+ 00b69230 ["INT_ADD", "register:40f0:8", ["const:b69230:8", "const:4:8"]]
+ 00b69230 ["CALL", null, ["callee:0057504c:8"]]
- 00b6823c bytes bc32e897
+ 00b69230 bytes 872fe897
- 00b68208 ["COPY", "register:40b0:8", ["const:1126000:8"]]
+ 00b691fc ["COPY", "register:40b0:8", ["const:1127000:8"]]
- 00b68208 bytes f62d00d0
+ 00b691fc bytes f62d00d0
- 00b6820c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:1a0:8"]]
- 00b6820c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b69200 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:160:8"]]
+ 00b69200 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6820c bytes c8d240f9
+ 00b69200 bytes c8b240f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02e05668ef22cd9d75d0c8251e873e59"></a>

### [`00b6826c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6826c.md) → [`00b69260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69260.md) _ZNK8firebase3App30IsDataCollectionDefaultEnabledEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c460.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b69274",
      "incomplete_value": true,
      "site": "00b69274",
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
      "definition_site": "00b68280",
      "incomplete_value": true,
      "site": "00b68280",
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
      "definition_site": "00b6928c",
      "incomplete_value": true,
      "site": "00b69298",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:158:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68298",
      "incomplete_value": true,
      "site": "00b682a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:198:8"
              ]
            ]
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
      "00b69270",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6928c",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b69270",
      "READ",
      [
        "storage",
        "01127158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6928c",
      "READ",
      [
        "storage",
        "01127158",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b682a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6826c.md#insn-00b682a4) · [`00b68278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6826c.md#insn-00b68278) · [`00b6827c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6826c.md#insn-00b6827c)
- 新版 [`00b69298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69260.md#insn-00b69298) · [`00b6926c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69260.md#insn-00b6926c) · [`00b69270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69260.md#insn-00b69270)

~~~diff
- 00b682a4 ["INT_ADD", "register:40f0:8", ["const:b682a4:8", "const:4:8"]]
- 00b682a4 ["CALL", null, ["callee:00497da8:8"]]
+ 00b69298 ["INT_ADD", "register:40f0:8", ["const:b69298:8", "const:4:8"]]
+ 00b69298 ["CALL", null, ["callee:00497da8:8"]]
- 00b682a4 bytes f9bde497
+ 00b69298 bytes c4bae497
- 00b68278 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00b6926c ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00b68278 bytes f42d00d0
+ 00b6926c bytes f42d00d0
- 00b6827c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:198:8"]]
- 00b6827c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b69270 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
+ 00b69270 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6827c bytes 88ce40f9
+ 00b69270 bytes 88ae40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e460062c854b162ba2942fe9c288421c"></a>

### [`00b6887c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6887c.md) → [`00b69870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69870.md) _ZN8firebase10AppOptions18LoadFromJsonConfigEPKcPS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 15件 [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0087ac8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087ac8c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b69908",
      "incomplete_value": true,
      "site": "00b6992c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68914",
      "incomplete_value": true,
      "site": "00b68938",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:db0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b698c8",
      "incomplete_value": true,
      "site": "00b698d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:7e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b688d4",
      "incomplete_value": true,
      "site": "00b688e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:810:8"
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
      "definition_site": "00b69970",
      "incomplete_value": true,
      "site": "00b69974",
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
            "const:68a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6897c",
      "incomplete_value": true,
      "site": "00b68980",
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
            "const:640:8"
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
      "00b698c8",
      "READ",
      [
        "storage",
        "00c9b810",
        null,
        "pointer"
      ]
    ],
    [
      "00b698c8",
      "PARAM",
      [
        "storage",
        "0030bd18",
        "_ZN8firebase3fbs29google_services_resource_dataE",
        "string"
      ]
    ],
    [
      "00b69908",
      "READ",
      [
        "storage",
        "002c3db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b698c8",
      "READ",
      [
        "storage",
        "00c9c7e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b698c8",
      "PARAM",
      [
        "storage",
        "0030bd58",
        "_ZN8firebase3fbs29google_services_resource_dataE",
        "string"
      ]
    ],
    [
      "00b69908",
      "READ",
      [
        "storage",
        "002c3e00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b688e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6887c.md#insn-00b688e4) · [`00b68980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6887c.md#insn-00b68980) · [`00b689a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6887c.md#insn-00b689a0)
- 新版 [`00b698d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69870.md#insn-00b698d8) · [`00b69974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69870.md#insn-00b69974) · [`00b69994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69870.md#insn-00b69994)

~~~diff
- 00b688e4 ["INT_ADD", "register:40f0:8", ["const:b688e4:8", "const:4:8"]]
- 00b688e4 ["CALL", null, ["callee:00c5cfb0:8"]]
+ 00b698d8 ["INT_ADD", "register:40f0:8", ["const:b698d8:8", "const:4:8"]]
+ 00b698d8 ["CALL", null, ["callee:00c5cfb0:8"]]
- 00b688e4 bytes bfcd0394
+ 00b698d8 bytes b6cd0394
- 00b68980 ["INT_ADD", "register:40f0:8", ["const:b68980:8", "const:4:8"]]
- 00b68980 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b69974 ["INT_ADD", "register:40f0:8", ["const:b69974:8", "const:4:8"]]
+ 00b69974 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b68980 bytes fcc80394
+ 00b69974 bytes f3c80394
- 00b689a0 ["INT_ADD", "register:40f0:8", ["const:b689a0:8", "const:4:8"]]
- 00b689a0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b69994 ["INT_ADD", "register:40f0:8", ["const:b69994:8", "const:4:8"]]
+ 00b69994 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b689a0 bytes ccc90394
+ 00b69994 bytes c3c90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8271416987dd70bf4b85fe8083b8ce92"></a>

### [`00b6905c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b69/00b6905c.md) → [`00b6a050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6a/00b6a050.md) _ZN11flatbuffers10IDLOptionsC2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b960.md) · 呼出先 1件 [`00c5b690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b690.md)
- 新版 呼出元 1件 [`00c5c930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c930.md) · 呼出先 1件 [`00c5c660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c660.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.57% / 新版 94.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6a060",
      "incomplete_value": true,
      "site": "00b6a090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:110:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6906c",
      "incomplete_value": true,
      "site": "00b6909c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c0:8"
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
      "definition_site": "00b6a07c",
      "incomplete_value": false,
      "site": "00b6a098",
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
            "const:641:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69088",
      "incomplete_value": false,
      "site": "00b690a4",
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
            "const:4e9:8"
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
      "definition_site": "00b6a0e4",
      "incomplete_value": false,
      "site": "00b6a128",
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
            "const:33d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b690f0",
      "incomplete_value": false,
      "site": "00b69134",
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
            "const:25f:8"
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
      "00b6a060",
      "READ",
      [
        "storage",
        "002c40c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6a07c",
      "PARAM",
      [
        "storage",
        "002a84e9",
        null,
        "string"
      ]
    ],
    [
      "00b6a0a4",
      "PARAM",
      [
        "storage",
        "002a0089",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6a060",
      "READ",
      [
        "storage",
        "002c4110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6a07c",
      "PARAM",
      [
        "storage",
        "002a8641",
        null,
        "string"
      ]
    ],
    [
      "00b6a0a4",
      "PARAM",
      [
        "storage",
        "002a00c9",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b690a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b69/00b6905c.md#insn-00b690a4) · [`00b69134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b69/00b6905c.md#insn-00b69134) · [`00b691a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b69/00b6905c.md#insn-00b691a4)
- 新版 [`00b6a098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6a/00b6a050.md#insn-00b6a098) · [`00b6a128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6a/00b6a050.md#insn-00b6a128) · [`00b6a198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6a/00b6a050.md#insn-00b6a198)

~~~diff
- 00b690a4 ["INT_ADD", "register:40f0:8", ["const:b690a4:8", "const:4:8"]]
- 00b690a4 ["CALL", null, ["callee:00c5c660:8"]]
+ 00b6a098 ["INT_ADD", "register:40f0:8", ["const:b6a098:8", "const:4:8"]]
+ 00b6a098 ["CALL", null, ["callee:00c5c660:8"]]
- 00b690a4 bytes 7bc90394
+ 00b6a098 bytes 72c90394
- 00b69134 ["INT_ADD", "register:40f0:8", ["const:b69134:8", "const:4:8"]]
- 00b69134 ["CALL", null, ["callee:00c5c660:8"]]
+ 00b6a128 ["INT_ADD", "register:40f0:8", ["const:b6a128:8", "const:4:8"]]
+ 00b6a128 ["CALL", null, ["callee:00c5c660:8"]]
- 00b69134 bytes 57c90394
+ 00b6a128 bytes 4ec90394
- 00b691a4 ["INT_ADD", "register:40f0:8", ["const:b691a4:8", "const:4:8"]]
- 00b691a4 ["CALL", null, ["callee:00c5c660:8"]]
+ 00b6a198 ["INT_ADD", "register:40f0:8", ["const:b6a198:8", "const:4:8"]]
+ 00b6a198 ["CALL", null, ["callee:00c5c660:8"]]
- 00b691a4 bytes 3bc90394
+ 00b6a198 bytes 32c90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

